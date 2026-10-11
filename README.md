# Cypress BDD UI Automation — OrangeHRM

![Cypress](https://img.shields.io/badge/Cypress-UI%20Automation-17202C?logo=cypress&logoColor=white)
![Cucumber](https://img.shields.io/badge/Cucumber-Gherkin%20BDD-23D96C?logo=cucumber&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-Strict-3178C6?logo=typescript&logoColor=white)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

A portfolio-focused QA project for the public [OrangeHRM demo](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login). It combines risk-based manual testing with UI automation built using Cypress, Cucumber/Gherkin, TypeScript step definitions, reusable Page Objects, and GitHub Actions.

> **Environment note:** OrangeHRM's public demo is a shared, third-party environment. Availability, credentials, permissions, and seeded data can change. Automation results should be interpreted from actual test run output, not assumed from the presence of scenarios or workflow files.

## Project at a glance

| Area | Approach |
| --- | --- |
| Application under test | OrangeHRM public demo |
| UI automation | Cypress |
| Scenario format | Cucumber / Gherkin BDD |
| Language | TypeScript |
| Design | Page Object Model, fixtures, reusable step definitions |
| Manual QA | Test plan, scenarios, 38 test cases, defect and execution templates |
| Reports and evidence | Cucumber JSON/HTML reports, failure screenshots, videos where available |
| CI | GitHub Actions |
| Configuration | Environment variables; credentials kept out of source control |

## Test coverage

The project combines manual test design with automated browser scenarios.

- **Authentication:** login page and required-field checks, invalid credentials, and authenticated dashboard workflows when valid demo credentials are configured.
- **PIM employee management:** required-field validation, synthetic employee creation and verification, and Employee List/Search controls.
- **Core navigation:** authenticated navigation to PIM, Leave, Time, and Recruitment.
- **Manual QA:** 38 test cases spanning authentication, PIM, navigation, usability, regression, and security-smoke review.

Credential-dependent scenarios may be marked pending when the username/password configuration is unavailable. Pending or skipped scenarios are not passes. The public demo can change independently of this repository, so review the run summary and evidence when evaluating results.

## Repository structure

```text
cypress-bdd-cucumber-typescript/
├── .github/workflows/cypress.yml
├── cypress/
│   ├── e2e/
│   │   ├── features/
│   │   │   ├── authentication/login.feature
│   │   │   ├── navigation/core-navigation.feature
│   │   │   └── pim/employee-management.feature
│   │   ├── step-definitions/
│   │   │   ├── authentication.steps.ts
│   │   │   ├── navigation.steps.ts
│   │   │   └── pim.steps.ts
│   │   ├── fixtures/employee.json
│   │   ├── pages/LoginPage.ts
│   │   ├── pages/EmployeePage.ts
│   │   └── support/
│   ├── reports/                 # Generated reports, when available
│   └── screenshots/ and videos/ # Failure evidence, when available
├── manual-testing/
│   ├── TEST-PLAN.md
│   ├── TEST-SCENARIOS.md
│   ├── TEST-CASES.csv
│   ├── BUG-REPORTS.md
│   └── TEST-EXECUTION-REPORT.md
├── docs/
│   ├── test-strategy.md
│   ├── TEST-EXECUTION-GUIDE.md
│   ├── TRACEABILITY-MATRIX.md
│   └── defect-lifecycle.md
├── .env.example
├── cypress.config.ts
├── package.json
├── README.md
└── tsconfig.json
```

## Prerequisites

- Node.js 22 or newer
- npm
- Internet access to the public OrangeHRM demo
- An authorized OrangeHRM demo account for authenticated scenarios

## Setup

```bash
npm install
npx cypress install
cp .env.example .env
```

On Windows PowerShell, copy the example with:

```powershell
Copy-Item .env.example .env
```

Update `.env` with the target URL and demo credentials:

```dotenv
CYPRESS_BASE_URL=https://opensource-demo.orangehrmlive.com
CYPRESS_ORANGEHRM_USERNAME=Admin
CYPRESS_ORANGEHRM_PASSWORD=admin123
```

Keep `.env` local; never commit credentials, production/customer data, or sensitive information in test evidence.

## Run tests

```bash
npm test                  # Run the feature suite headlessly
npm run cy:open            # Open the Cypress interactive runner
npm run test:smoke         # Run @smoke scenarios
npm run test:regression    # Run @regression scenarios
npm run test:ci            # Run the CI-targeted Cypress suite
```

Cucumber JSON/HTML reports are configured under `cypress/reports/`. Cypress screenshots on failure and videos are retained when generated. The interactive runner may not create the same Cucumber JSON output as a headless run.

## CI and diagnostics

GitHub Actions runs the Cucumber suite on pushes, pull requests, and manual dispatch. Configure these repository Actions secrets for authenticated coverage:

| Secret / variable | Purpose |
| --- | --- |
| `ORANGEHRM_USERNAME` | Authorized demo username |
| `ORANGEHRM_PASSWORD` | Authorized demo password |
| `ORANGEHRM_BASE_URL` variable (optional) | Overrides the default OrangeHRM demo URL |

The workflow uploads available Cucumber reports, screenshots, and videos as artifacts. Review the Actions run for actual pass/fail/pending counts and evidence; a workflow file by itself is not proof that the suite passed.

## QA documentation

The manual-testing directory contains the planning and evidence templates used to support test design and traceability.

- `TEST-PLAN.md`: scope, approach, environment, risks, and entry/exit criteria.
- `TEST-SCENARIOS.md`: scenario inventory, priorities, and techniques.
- `TEST-CASES.csv`: test steps, expected results, automation mapping, status, actual result, defect, and evidence fields.
- `BUG-REPORTS.md`: defect register and reusable reporting template.
- `TEST-EXECUTION-REPORT.md`: run metadata, results, defects, exit assessment, and remaining risk.
- `docs/TRACEABILITY-MATRIX.md`: links between manual cases and automated scenarios.

Manual cases start as **Not Run** and should be updated only after real execution. A planned case is not a passed case.

## Quality principles

- Prefer meaningful assertions that verify outcomes, not just actions.
- Keep feature scenarios business-readable and focused.
- Reuse Page Objects and shared step definitions for repeated UI behaviour.
- Generate unique synthetic data for record-creation flows.
- Avoid arbitrary waits and brittle assumptions about seeded demo records.
- Distinguish Pass, Fail, Blocked, Skipped, and Not Run.
- Investigate automation and environment failures before reporting a product defect.
- Report only metrics supported by actual execution results.

## Related QA portfolio projects

- [Playwright UI Automation — OrangeHRM](https://github.com/sraagul99/playwright-ui-automation)
- [Postman + Newman API Testing](https://github.com/sraagul99/postman-newman-api-testing)

## Author

**Raagul Sivanathan** · Quality Assurance Engineer

- LinkedIn: [linkedin.com/in/sraagul](https://www.linkedin.com/in/sraagul)
- GitHub: [github.com/sraagul99](https://github.com/sraagul99)

*Independent learning project. OrangeHRM is the application under test; this repository is not affiliated with or endorsed by OrangeHRM.*
