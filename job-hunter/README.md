# Sri Lanka QA Job Hunter

A small scheduled job-search assistant that checks publicly indexed LinkedIn job listings and recruiter posts for Sri Lankan QA/testing opportunities, filters obvious junior/training roles, and emails new matches to your chosen address using Gmail SMTP.

## What it does

- Searches Google News RSS for public web results scoped to LinkedIn jobs and posts.
- Looks for QA/testing roles and Sri Lankan location signals.
- Excludes results mentioning intern, trainee, graduate, junior, entry-level, associate, apprentice, or fresher.
- Flags clear experience/seniority signals; otherwise marks a non-junior QA title as a **potential match** so you can verify the 3+ years requirement.
- Deduplicates results using `seen_jobs.json`.
- Runs hourly via GitHub Actions and sends alerts to Telegram.

## Important limitations

This is a public-search approach, not a LinkedIn account scraper. It cannot see private posts, closed groups, every LinkedIn listing, or results that search engines do not index. Search snippets can be incomplete, and the filters may miss or misclassify opportunities. Review each listing before applying. A direct LinkedIn URL is used when Google News redirects to one; otherwise the message may contain the Google News result URL.

## Enable free email notifications

The job hunter sends email using Gmail's free SMTP service. The destination can be any valid email address, including Outlook, but the sending account must be a Gmail account.

1. Choose a Gmail account to send alerts from.
2. Turn on 2-Step Verification for that Gmail account.
3. Create a Google **App Password** from your Google Account security settings. Use this app password only for this automation; do not use your normal Gmail password.
4. In this GitHub repository, open **Settings → Secrets and variables → Actions → New repository secret** and add:
   - `EMAIL_TO` = the email address that should receive job alerts
   - `EMAIL_SENDER` = the Gmail address sending the alerts
   - `EMAIL_APP_PASSWORD` = the Google App Password
5. Open **Actions**, select **Sri Lanka QA Job Hunter**, and choose **Run workflow** to test it.

Never put an app password in source code, a public issue, or a chat message. If Google does not offer App Passwords for your account, use a different supported sender account or another email provider's SMTP settings.

## Schedule

The workflow runs hourly. GitHub scheduled workflows can start late during busy periods, and public RSS search results are not guaranteed to refresh hourly. You can also run the workflow manually from the Actions tab.

## Required GitHub Actions permissions

The workflow uses `contents: write` only to save `seen_jobs.json`, preventing the same result from being alerted repeatedly. It does not need access to your LinkedIn account or password.
