# Cypress BDD Automation — OrangeHRM

**Cypress · Cucumber/Gherkin · TypeScript · Manual QA · GitHub Actions**

A practical test engineering project for the OrangeHRM public demo. It combines structured manual testing with Behavior-Driven Development (BDD) UI automation using Cypress, Gherkin feature files, TypeScript step definitions, reusable page objects, and continuous integration.

> **Execution integrity:** Test plans and test cases are not evidence of execution. Manual cases start as **Not Run** and should be updated only after running them. Automated outcomes must be taken from actual CI or local test results. The public demo and its data/UI can change.

## Project goals

- Design and document risk-based manual tests.
- Express selected behaviors in readable Gherkin.
- Connect feature files to maintainable TypeScript step definitions.
- Reuse page objects, fixtures, commands, and configuration.
- Run automated scenarios in GitHub Actions and preserve useful evidence.
- Maintain traceability between requirements, manual cases, automation, and defects.

## Application under test

- **Application:** OrangeHRM Open Source demo
- **URL:** https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- **Initial scope:** Authentication, PIM employee management, and core module navigation
- **Test data:** Synthetic portfolio data only. Never commit credentials or production/customer data.

## Repository areas

- `cypress/e2e/features/` — Gherkin feature files.
- `cypress/e2e/step-definitions/` — TypeScript step implementations.
- `cypress/pages/` — Page Object Model.
- `cypress/fixtures/` — Synthetic test data.
- `manual-testing/` — Test plan, scenarios, detailed CSV cases, defects, and execution reporting.
- `docs/` — Test strategy, traceability, and defect lifecycle.
- `.github/workflows/` — CI configuration.

## Local setup

Requires Node.js 20+ and npm.

```bash
npm install
npx cypress install
```

Copy `.env.example` to `.env` and set credentials for an authorized OrangeHRM demo account. Never commit `.env`.

```bash
npm run cy:open
npm test
```

Credential-dependent scenarios should be marked/skipped when authorized credentials are unavailable; don't hard-code credentials in source control.

## Manual QA deliverables

The manual test suite includes a test plan, prioritized scenarios, detailed test cases with execution status fields, a defect-reporting template, and an execution-summary template. Record environment, browser, date, actual behavior, evidence, and defect references when executing cases.

## Automation quality standards

- Gherkin describes observable behavior, not implementation details.
- Step definitions reuse common actions and avoid duplicate wording.
- Assertions verify the expected application state, not merely that a click occurred.
- Test data is synthetic and unique where possible.
- Credentials are configured through environment variables or CI secrets.
- CI failures are triaged into application defects, automation defects, and environment issues.

## Author

**Raagul Sivanathan** · Quality Assurance Engineer

- LinkedIn: https://www.linkedin.com/in/sraagul
- GitHub: https://github.com/sraagul99

*Independent learning project. OrangeHRM is the application under test; this repository is not affiliated with or endorsed by OrangeHRM.*
