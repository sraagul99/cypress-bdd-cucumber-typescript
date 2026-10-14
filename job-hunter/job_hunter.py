#!/usr/bin/env python3
"""Find publicly indexed LinkedIn QA vacancies and recruiter posts, then send email alerts."""
from __future__ import annotations

import html
import json
import smtplib
from email.message import EmailMessage
import os
import re
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent
SEEN_FILE = ROOT / "seen_jobs.json"
EMAIL_TO = os.getenv("EMAIL_TO", "").strip()
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "").strip()
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD", "").strip()
MAX_SEEN = 1500
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; SriLankaQAJobHunter/1.0)"}

# Google News RSS indexes public web results. It cannot access private LinkedIn content.
QUERIES = [
    'site:linkedin.com/jobs/view ("QA Engineer" OR "Quality Assurance Engineer" OR "Software Tester") ("Sri Lanka" OR Colombo)',
    'site:linkedin.com/jobs/view ("Senior QA" OR "QA Automation" OR "SDET" OR "Test Automation Engineer") ("Sri Lanka" OR Colombo)',
    'site:linkedin.com/posts ("QA Engineer" OR "Quality Assurance" OR "QA hiring" OR "QA vacancy") ("Sri Lanka" OR Colombo)',
    'site:linkedin.com/posts (hiring OR vacancy OR "we are looking") ("QA Engineer" OR "Automation Tester" OR "Software Tester") ("Sri Lanka" OR Colombo)',
]

QA_TERMS = re.compile(r"\b(qa|quality assurance|software test|software tester|test automation|sdet|quality engineer|automation tester|manual tester)\b", re.I)
LOCATION_TERMS = re.compile(r"\b(sri lanka|colombo|kandy|galle|negombo|remote.{0,20}sri lanka|sri lanka.{0,20}remote)\b", re.I)
SENIOR_TERMS = re.compile(r"\b(senior|sr\.?\s|lead|principal|manager|experienced|mid[- ]?level|3\+\s*years|3\s*years|four years|4\+\s*years|5\+\s*years|qa engineer ii|level 2)\b", re.I)
JUNIOR_TERMS = re.compile(r"\b(intern(ship)?|trainee|graduate|junior|entry[- ]level|associate|apprentice|fresh(er)?|undergraduate)\b", re.I)
EXPERIENCE_TERMS = re.compile(r"\b(3\+?\s*(years|yrs)|minimum of 3 years|at least 3 years|3 to 5 years|3-5 years|4\+?\s*(years|yrs)|5\+?\s*(years|yrs)|mid[- ]level|senior|lead)\b", re.I)

def load_seen() -> set[str]:
    try:
        data = json.loads(SEEN_FILE.read_text(encoding="utf-8"))
        return set(data if isinstance(data, list) else [])
    except (OSError, json.JSONDecodeError):
        return set()

def save_seen(seen: set[str]) -> None:
    SEEN_FILE.write_text(json.dumps(sorted(seen)[-MAX_SEEN:], indent=2), encoding="utf-8")

def rss_items(query: str) -> list[dict[str, str]]:
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode({
        "q": query, "hl": "en", "gl": "LK", "ceid": "LK:en"
    })
    response = requests.get(url, headers=HEADERS, timeout=25)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    items = []
    for item in root.findall(".//item"):
        title = html.unescape(item.findtext("title", default="")).strip()
        link = item.findtext("link", default="").strip()
        description = html.unescape(item.findtext("description", default="")).strip()
        description = re.sub(r"<[^>]+>", " ", description)
        description = re.sub(r"\s+", " ", description).strip()
        pub_date = item.findtext("pubDate", default="").strip()
        if title and link:
            items.append({"title": title, "link": link, "description": description, "date": pub_date})
    return items

def resolve_link(link: str) -> str:
    try:
        response = requests.get(link, headers=HEADERS, timeout=15, allow_redirects=True, stream=True)
        final_url = response.url
        response.close()
        # Do not return a Google News wrapper when it fails to resolve.
        return final_url if "linkedin.com/" in final_url.lower() else link
    except requests.RequestException:
        return link

def qualifies(item: dict[str, str]) -> tuple[bool, str]:
    text = f"{item['title']} {item['description']}"
    title = item["title"]
    link = item["link"].lower()
    if "linkedin.com/" not in link and "linkedin.com/" not in text.lower():
        # Search results can have Google News wrapper links; the search query itself is LinkedIn-scoped.
        pass
    if not QA_TERMS.search(text):
        return False, "Not clearly a QA/testing role"
    if JUNIOR_TERMS.search(text):
        return False, "Junior, entry-level, or training role"
    if not (LOCATION_TERMS.search(text) or "sri lanka" in title.lower() or "colombo" in title.lower()):
        return False, "Sri Lanka location not evident in indexed result"
    # Include roles that explicitly request 3+ years, signal a senior/lead level, or have no clear level
    # but use a non-junior QA Engineer title. Label the last case for manual review.
    if EXPERIENCE_TERMS.search(text) or SENIOR_TERMS.search(text):
        return True, "Experience/level signal found"
    if re.search(r"\b(qa engineer|quality assurance engineer|test automation engineer|automation tester|software tester|sdet)\b", title, re.I):
        return True, "Potential match — verify the 3+ years requirement"
    return False, "Role level unclear"

def email_send(subject: str, text_body: str, html_body: str) -> None:
    if not EMAIL_TO or not EMAIL_SENDER or not EMAIL_APP_PASSWORD:
        raise RuntimeError("Email is not configured. Add EMAIL_TO, EMAIL_SENDER, and EMAIL_APP_PASSWORD as GitHub Actions secrets.")
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_TO
    message.set_content(text_body)
    message.add_alternative(html_body, subtype="html")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_APP_PASSWORD)
        smtp.send_message(message)

def format_alert(item: dict[str, str]) -> tuple[str, str, str]:
    subject = f"QA Job Alert: {item['title']}"
    text_body = (
        f"NEW SRI LANKA QA OPPORTUNITY\\n\\n"
        f"Job: {item['title']}\\n"
        f"Date: {item['date'] or 'Date not shown'}\\n"
        f"Match: {item['reason']}\\n"
        f"Link: {item['resolved_link']}\\n\\n"
        f"Details: {item['description'][:1000] or 'Open the link to review the details.'}\\n\\n"
        "Automated alert from your Sri Lanka QA Job Hunter."
    )
    safe_title = html.escape(item["title"])
    safe_date = html.escape(item["date"] or "Date not shown")
    safe_reason = html.escape(item["reason"])
    safe_description = html.escape(item["description"][:1000] or "Open the link to review the details.")
    safe_link = html.escape(item["resolved_link"], quote=True)
    html_body = (
        '<div style="font-family:Arial,sans-serif;line-height:1.5">'
        '<h2>🔎 New Sri Lanka QA Opportunity</h2>'
        f'<h3>{safe_title}</h3>'
        f'<p><b>Date:</b> {safe_date}<br><b>Match:</b> {safe_reason}</p>'
        f'<p><a href="{safe_link}">Open LinkedIn result</a></p>'
        f'<p>{safe_description}</p>'
        '<hr><small>Automated alert from your Sri Lanka QA Job Hunter.</small></div>'
    )
    return subject, text_body, html_body

def main() -> None:
    if not EMAIL_TO or not EMAIL_SENDER or not EMAIL_APP_PASSWORD:
        raise RuntimeError("Email is not configured. Add EMAIL_TO, EMAIL_SENDER, and EMAIL_APP_PASSWORD as GitHub Actions secrets.")

    seen = load_seen()
    candidates: dict[str, dict[str, str]] = {}
    errors = []
    for query in QUERIES:
        try:
            for item in rss_items(query):
                # Google RSS wrapper is a stable de-duplication key until resolved.
                key = item["link"]
                if key not in candidates:
                    candidates[key] = item
            time.sleep(1)
        except (requests.RequestException, ET.ParseError) as exc:
            errors.append(f"{query}: {exc}")

    matches = []
    for key, item in candidates.items():
        if key in seen:
            continue
        ok, reason = qualifies(item)
        if not ok:
            continue
        item["resolved_link"] = resolve_link(item["link"])
        item["reason"] = reason
        matches.append((key, item))

    # Oldest-to-newest ordering is not guaranteed by the RSS feed; cap each run.
    matches = matches[:15]
    for key, item in matches:
        subject, text_body, html_body = format_alert(item)
        email_send(subject, text_body, html_body)
        seen.add(key)
        time.sleep(1)

    # Remember searched results as well as matches to avoid repeated checks/alerts.
    seen.update(candidates.keys())
    save_seen(seen)
    print(f"Checked {len(candidates)} indexed results; sent {len(matches)} new alerts.")
    if errors:
        print("Some searches failed:")
        for error in errors:
            print(error)

if __name__ == "__main__":
    main()
