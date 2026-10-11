# Test Traceability Matrix

This matrix links representative behavior to manual test cases and executable Gherkin scenarios. A listed feature file indicates implementation coverage, not a claim that the scenario has passed.

| Behavior / requirement | Manual scenario | Manual case | Gherkin automation | Notes |
|---|---|---|---|---|
| Login page is available | ORH-AUTH-S01 | ORH-AUTH-001 | login.feature, empty/invalid login scenarios start here | Manual page-load check |
| Empty login is rejected | ORH-AUTH-S02 | ORH-AUTH-002 | login.feature — empty login | Negative/validation |
| Invalid credentials are rejected | ORH-AUTH-S03 | ORH-AUTH-003 | login.feature — invalid credentials | Requires live demo behavior to remain consistent |
| Authorized user reaches dashboard | ORH-AUTH-S04 | ORH-AUTH-004 | login.feature — authorized user | Requires credentials in local environment or CI secrets |
| Employee list is accessible | ORH-PIM-S01 | ORH-PIM-001 | employee-management.feature — Employee List | Authenticated |
| Add Employee form loads | ORH-PIM-S02 | ORH-PIM-002 | employee-management.feature — validation/create | Authenticated |
| Required employee data is validated | ORH-PIM-S03 | ORH-PIM-003 | employee-management.feature — required fields | Authenticated |
| Employee can be created | ORH-PIM-S04 | ORH-PIM-004 | employee-management.feature — create employee | Uses synthetic unique data |
| Saved employee values are correct | ORH-PIM-S05 | ORH-PIM-005 | employee-management.feature — saved details | Authenticated |
| Core module navigation works | ORH-NAV-S02–S05 | ORH-NAV-002–005 | core-navigation.feature — Scenario Outline | PIM / Leave / Time / Recruitment |
| Password remains masked | ORH-AUTH-S05 | ORH-AUTH-005 | — | Manual/security-smoke coverage |
| Search and pagination behave consistently | ORH-PIM-S06–S14 | ORH-PIM-006–014 | — | Candidates for later automation after reviewing demo data/behavior |

## How to maintain traceability

1. Assign a stable ID to new manual cases.
2. Record the related scenario ID in the CSV notes or a matrix row.
3. Add a Gherkin scenario only where automation provides value and the behavior is stable enough to assert.
4. When requirements change, review manual expectations and their linked feature scenarios together.
5. Keep test status and execution evidence in the execution report, not in this static mapping.
