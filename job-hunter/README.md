# Sri Lanka QA Job Hunter

A small scheduled job-search assistant that checks publicly indexed LinkedIn job listings and recruiter posts for Sri Lankan QA/testing opportunities, filters obvious junior/training roles, and sends new matches to Telegram.

## What it does

- Searches Google News RSS for public web results scoped to LinkedIn jobs and posts.
- Looks for QA/testing roles and Sri Lankan location signals.
- Excludes results mentioning intern, trainee, graduate, junior, entry-level, associate, apprentice, or fresher.
- Flags clear experience/seniority signals; otherwise marks a non-junior QA title as a **potential match** so you can verify the 3+ years requirement.
- Deduplicates results using `seen_jobs.json`.
- Runs hourly via GitHub Actions and sends alerts to Telegram.

## Important limitations

This is a public-search approach, not a LinkedIn account scraper. It cannot see private posts, closed groups, every LinkedIn listing, or results that search engines do not index. Search snippets can be incomplete, and the filters may miss or misclassify opportunities. Review each listing before applying. A direct LinkedIn URL is used when Google News redirects to one; otherwise the message may contain the Google News result URL.

## Enable free Telegram notifications

1. In Telegram, open **@BotFather**, send `/newbot`, and follow its steps.
2. Copy the bot token. Keep it private.
3. Open your new bot and press **Start**.
4. To obtain your chat ID, open this URL in a browser after messaging the bot, replacing `YOUR_BOT_TOKEN` with the token:
   `https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates`
   Find `"chat":{"id": ...}` in the response. Do not share the token publicly.
5. In this GitHub repository, open **Settings → Secrets and variables → Actions → New repository secret**. Add:
   - `TELEGRAM_BOT_TOKEN` = your bot token
   - `TELEGRAM_CHAT_ID` = your chat ID
6. Open **Actions**, select **Sri Lanka QA Job Hunter**, and run **Run workflow** once to test it.

## Schedule

The workflow runs hourly. GitHub scheduled workflows can start late during busy periods, and public RSS search results are not guaranteed to refresh hourly. You can also run the workflow manually from the Actions tab.

## Required GitHub Actions permissions

The workflow uses `contents: write` only to save `seen_jobs.json`, preventing the same result from being alerted repeatedly. It does not need access to your LinkedIn account or password.
