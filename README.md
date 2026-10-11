# Cypress BDD Automation — OrangeHRM

**Cypress · Cucumber/Gherkin · TypeScript · Manual QA · GitHub Actions**

A practical test engineering project for the public OrangeHRM demo. It combines risk-based manual testing with maintainable Behavior-Driven Development (BDD) UI automation using Cypress, Gherkin feature files, TypeScript step definitions, Page Object Model, test fixtures, and CI.

> **Execution integrity:** Manual cases start as Not Run and should be updated only after real execution. Automation results must be taken from actual local or CI runs. The public demo and its data/UI can change.

## Project objectives

- Design test coverage from observable behavior and risk.
- Document manual tests with reproducible steps, test data, expected results, status, and evidence.
- Express selected stable workflows in readable Gherkin.
- Connect feature files to TypeScript step definitions and reusable page objects.
- Run the suite in GitHub Actions and retain generated reports/evidence.
- Maintain traceability between manual cases, automation scenarios, and defects.

## Technology stack

- Cypress E2E
- Cucumber/Gherkin via @badeball/cypress-cucumber-preprocessor
- TypeScript
- esbuild preprocessor
- Node.js / npm
- GitHub Actions

## Application under test

- **Application:** OrangeHRM Open Source demo
- **URL:** https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- **Initial scope:** Authentication, PIM employee management, and main module navigation
- **Test data:** Synthetic portfolio data only. Never commit credentials or production/customer data.

## Repository structure

    .
    ├── .github/workflows/cypress.yml
    ├── cypress/
    │   ├── e2e/
    │   │   ├── features/
    │   │   │   ├── authentication/login.feature
    │   │   │   ├── pim/employee-management.feature
    │   │   │   └── navigation/core-navigation.feature
    │   │   └── step-definitions/
    │   │       ├── authentication.steps.ts
    │   │       ├── pim.steps.ts
    │   │       └── navigation.steps.ts
    │   ├── fixtures/employee.json
    │   ├── pages/LoginPage.ts
    │   ├── pages/EmployeePage.ts
    │   └── support/
    │       ├── commands.ts
    │       └── e2e.ts
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
    └── tsconfig.json

## Manual QA deliverables

The manual suite contains **38 test cases** across authentication, PIM, navigation, usability, regression, and security-smoke review.

- **TEST-PLAN.md:** objective, scope, approach, environment, entry/exit criteria, risks, and deliverables.
- **TEST-SCENARIOS.md:** scenario inventory with priorities, techniques, and automation links.
- **TEST-CASES.csv:** test case IDs, preconditions, steps, data, expected results, automation mapping, execution status, actual result, defect ID, and evidence link.
- **BUG-REPORTS.md:** defect register (currently no verified defects claimed) and reusable reporting template.
- **TEST-EXECUTION-REPORT.md:** run metadata, status counts, defects, exit assessment, and remaining risk.

Manual execution results are deliberately left as **Not Run** until tests are performed. A planned case is not a passed case.

## BDD automation coverage

### Authentication
- Empty credentials produce required-field validation.
- Invalid credentials produce a visible authentication error.
- Authorized demo user can reach the dashboard when credentials are configured.

### PIM employee management
- Required-field validation on Add Employee.
- Create an employee with unique synthetic values and verify saved details.
- Confirm Employee List and Search controls are available.

### Navigation
- Scenario Outline checks PIM, Leave, Time, and Recruitment module routes for an authenticated user.

The feature files describe behavior; their TypeScript step definitions implement actions/assertions. Page objects centralize selectors/actions. Credential-dependent scenarios short-circuit when credentials are unavailable; Cypress may show them as pending in its summary. Inspect actual result counts rather than interpreting pending/skipped scenarios as passed.

## Local setup

Requires Node.js 22+ and npm.

    npm install
    npx cypress install

Copy .env.example to .env and enter an authorized OrangeHRM demo account. The local .env file is ignored by Git.

    CYPRESS_BASE_URL=https://opensource-demo.orangehrmlive.com
    CYPRESS_ORANGEHRM_USERNAME=your_demo_username
    CYPRESS_ORANGEHRM_PASSWORD=your_demo_password

Never commit real credentials. Do not add secrets to screenshots, CSV test data, bug reports, or source code.

## Run tests

Open Cypress:

    npm run cy:open

Run all feature files headlessly:

    npm test

Run scenarios tagged @smoke:

    npm run test:smoke

Run scenarios tagged @regression:

    npm run test:regression

Cucumber JSON and HTML reports are configured under cypress/reports/. Cypress screenshots on failure and videos are retained as available artifacts. The interactive Cypress runner may not generate the same Cucumber JSON output as a headless run.

## Continuous integration

GitHub Actions runs the Cucumber suite on pushes, pull requests, and manual dispatch. For authenticated coverage, configure these repository Actions secrets:

- ORANGEHRM_USERNAME
- ORANGEHRM_PASSWORD

An optional Actions variable named ORANGEHRM_BASE_URL can override the target URL. The workflow uploads available Cucumber reports, screenshots, and videos.

A workflow file does not prove that tests passed. Review the Actions tab for the actual run status, pass/fail/skip counts, and artifact downloads.

## Traceability and reporting

The traceability matrix maps representative behaviors to manual scenario IDs, case IDs, and Gherkin files. Maintain it as coverage changes.

Triage failures as one of:
- Product behavior that violates an established expectation.
- Automation or locator defect.
- Environment/demo availability issue.
- Test data or credential configuration issue.
- Unclear requirement that needs clarification.

Never report a product defect based on an automation failure alone.

## Quality principles

1. Prefer meaningful assertions that validate results, not just actions.
2. Keep feature scenarios business-readable and focused.
3. Keep locators and shared behavior reusable.
4. Generate unique synthetic test data for record-creation flows.
5. Avoid arbitrary waits and fragile assumptions about seeded demo records.
6. Separate Pass, Fail, Blocked, Skipped, and Not Run.
7. Report only metrics supported by actual execution results.

## Author

**Raagul Sivanathan** · Quality Assurance Engineer

- LinkedIn: https://www.linkedin.com/in/sraagul
- GitHub: https://github.com/sraagul99

*Independent learning project. OrangeHRM is the application under test; this repository is not affiliated with or endorsed by OrangeHRM.*
