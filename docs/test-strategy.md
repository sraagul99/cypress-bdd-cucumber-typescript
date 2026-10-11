# Test Strategy — OrangeHRM

## 1. Purpose

Use risk-based manual testing and Cypress-Cucumber BDD automation to evaluate selected workflows in the public OrangeHRM demo. This is a portfolio exercise: observations must be tied to the specific demo state and must not be generalized to a production deployment.

## 2. Testing model

Manual and automated testing serve complementary purposes.

| Activity | Primary purpose | Execution approach |
|---|---|---|
| Manual functional testing | Explore workflows, inputs, state changes, and expected behavior | Follow TEST-CASES.csv; capture actual results and evidence |
| Exploratory / usability | Assess clarity, layout, focus, feedback, and unexpected behavior | Time-boxed investigation; record charter and findings |
| BDD automation | Repeat stable, high-value user journeys with deterministic assertions | Gherkin feature + TypeScript steps + page objects |
| Regression | Detect unintended changes in stable behavior | Execute relevant tagged automation and manual cases |
| Defect verification | Verify that a reported behavior is fixed | Reproduce, retest, then execute related regression checks |

Do not automate a manual scenario merely to increase the automated test count. Prioritize scenarios that are stable, repeatable, and valuable to run after change.

## 3. Scope

- Authentication form validation and invalid credentials; valid sign-in when authorized credentials are configured.
- PIM employee form validation, employee creation, employee details, and employee-list availability.
- Main navigation routes for PIM, Leave, Time, and Recruitment.
- Manual search, pagination, data-boundary, usability, and responsive checks.

Out of scope: penetration testing, load testing, production-data testing, and full certification of the application.

## 4. Test design

Apply:
- Risk-based prioritization by impact, likelihood, and user frequency.
- Equivalence partitioning when input categories are known.
- Boundary-value analysis only where a field limit is confirmed by an approved requirement or observable application constraint.
- State-transition checks across login and record-creation flows.
- Positive and negative tests for both normal and invalid user input.
- Exploratory testing where requirements are unclear or judgment is needed.

## 5. Automation architecture

- **Feature files:** describe observable behavior in Gherkin.
- **Step definitions:** implement Gherkin steps using Cypress commands and assertions.
- **Page Object Model:** centralizes page locators and actions.
- **Fixtures:** hold synthetic test-data prefixes.
- **Environment configuration:** isolates the target URL and credentials.
- **Tags:** classify smoke, negative, regression, and credential-dependent scenarios.
- **CI artifacts:** preserve available Gherkin reports, screenshots, and videos.

Keep steps declarative. Avoid placing long implementation detail into Gherkin, repeating locators across scenarios, arbitrary waits, and assertions that check only that an element was clicked.

## 6. Entry and exit criteria

### Entry
- Target application is reachable.
- Scope, expected behavior, and test data are understood.
- Authorized demo credentials are available for authenticated scenarios.
- Browser and environment are recorded.

### Exit
- Executed manual cases contain actual results and statuses.
- Failures have reproducible evidence and defect references where appropriate.
- Blocked and skipped tests remain distinct from Pass.
- Automation failures are triaged as product, test-code, or environment failures.
- Residual risk and untested coverage are described in the execution report.

## 7. Risks

| Risk | Mitigation |
|---|---|
| Public demo is unstable or changed | Record environment and timestamp; mark affected testing Blocked where justified |
| Credentials unavailable | Keep credentials outside source control and identify authenticated scenarios as skipped |
| Test data already exists | Generate unique synthetic names and identifiers |
| Locators change | Diagnose the failure and update locators only after verifying current behavior |
| Test creates persistent data | Use synthetic records and remove only records created by the tester if permitted |
| False confidence from green CI | Review scenario counts, pending/skipped scenarios, and actual evidence; CI is not product certification |

## 8. Defect triage

Before logging a product defect, verify that the expected behavior is justified, reproduce the discrepancy, and rule out environment and automation problems. The defect report must distinguish observed facts from hypotheses.

## 9. Metrics

Report counts from actual execution only:
- Manual cases planned / executed / Pass / Fail / Blocked / Not Run.
- Gherkin scenarios discovered / passed / failed / skipped.
- Defects by severity and state.
- Requirement and scenario coverage.
- Main blockers, unstable tests, and residual risk.

Do not calculate a pass rate using skipped or Not Run cases as passing tests.
