# OrangeHRM Manual Test Plan

## Document control

| Field | Value |
|---|---|
| Project | Cypress BDD Cucumber TypeScript — OrangeHRM |
| Document | Manual Test Plan |
| Owner | Raagul Sivanathan |
| Version | 1.0 |
| Status | Planned — complete execution fields during real test runs |
| Application URL | https://opensource-demo.orangehrmlive.com/web/index.php/auth/login |

## 1. Objective

Assess the externally observable behavior of selected OrangeHRM workflows using risk-based manual testing. Confirm that expected behavior, field validation, navigation, and common user journeys work as intended. Record reproducible defects and evidence without assuming root cause.

## 2. Test scope

### In scope
- Authentication page rendering, empty credentials, invalid credentials, and valid sign-in when an authorized account is available.
- PIM employee list and Add Employee flows, field validation, creation, record details, search, filters, pagination, and cancellation.
- Core navigation to Dashboard, PIM, Leave, Time, and Recruitment.
- Usability and responsive-layout observations on selected screens.
- Regression checks for the main authentication and employee workflows.
- Test case execution, defect reporting, retesting, and traceability to automation scenarios.

### Out of scope
- Penetration testing, load testing, performance certification, and exhaustive accessibility certification.
- Testing production systems, real employee data, or any environment for which the tester lacks authorization.
- Assuming the demo application's current behavior is a contractual requirement; confirm expected behavior against approved requirements where available.

## 3. Test approach

Use risk-based testing with a combination of:
- Functional testing for normal user workflows.
- Negative testing for invalid or incomplete data.
- Equivalence partitioning where input categories are known.
- Boundary-value analysis based on constraints confirmed in the UI or approved requirements.
- Exploratory testing for usability, ambiguous feedback, and data consistency.
- Smoke testing to confirm core routes and pages are available.
- Regression testing after a relevant code or configuration change.

Automate stable, repeatable, high-value regression scenarios. Keep exploratory checks, visual judgment, and scenarios requiring human evaluation as manual activities.

## 4. Environment and test data

Record these details for each execution:
- Date/time and time zone.
- Application URL and any visible build/version.
- Operating system and browser/version.
- Account role (never record password).
- Network/demo availability.
- Tester and test run identifier.

Use synthetic values and unique identifiers for employee creation. Do not use real personal information. Remove only test records you created and only when deletion is permitted.

## 5. Entry criteria

- Target demo is reachable.
- Scope and test cases have been reviewed.
- Browser and execution environment are recorded.
- Authorized credentials are available for authenticated scenarios.
- Test data is synthetic and approved for the demo environment.

## 6. Exit criteria

- Executed cases have accurate Pass, Fail, Blocked, or Not Applicable statuses.
- Not Run cases remain clearly distinguished from executed cases.
- Failures have reproducible steps and evidence; relevant defect IDs are recorded.
- Blocked tests have an explicit reason.
- Retests and related regression checks are recorded.
- The execution summary identifies residual risk and untested areas.

## 7. Severity and priority

Severity describes the impact of a defect. Priority describes urgency of resolution. Use the project's agreed definitions and business impact; do not mechanically derive one from the other.

## 8. Deliverables

- TEST-SCENARIOS.md — coverage inventory and risk priorities.
- TEST-CASES.csv — detailed case-level steps and traceability.
- TEST-EXECUTION-REPORT.md — per-run result summary.
- BUG-REPORTS.md — defect register and reporting template.
- docs/TRACEABILITY-MATRIX.md — requirement/scenario/manual/automation mapping.

## 9. Risks and assumptions

| Risk / assumption | Response |
|---|---|
| Public demo is unavailable or changed | Record the observed environment and mark impacted cases Blocked or update them after review |
| Seeded data changes | Avoid assuming fixed record counts; use unique test data where possible |
| Credentials change | Request authorized current credentials; never store secrets in the repository |
| UI selectors change | Re-check expected behavior, capture evidence, and distinguish automation issues from product defects |
| The demo may not represent production | State this limitation in all conclusions |

## 10. Reporting rule

Never report a case as passed based only on its expected result or on the presence of an automation script. Record the observed result after execution and attach evidence where useful.
