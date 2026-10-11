# Manual Test Scenario Catalogue

Priorities: **P1** = critical journey / high risk; **P2** = important functional coverage; **P3** = lower-risk, usability, or additional regression coverage.

| Scenario ID | Module | Scenario | Priority | Technique | Automation link |
|---|---|---|---|---|---|
| ORH-AUTH-S01 | Authentication | Verify login page loads with required controls | P1 | Smoke | Manual |
| ORH-AUTH-S02 | Authentication | Submit empty credentials and inspect validation | P1 | Negative / validation | login.feature |
| ORH-AUTH-S03 | Authentication | Submit invalid credentials | P1 | Negative | login.feature |
| ORH-AUTH-S04 | Authentication | Sign in with an authorized demo account | P1 | Positive / state transition | login.feature |
| ORH-AUTH-S05 | Authentication | Verify password field masks typed values | P2 | UI / security smoke | Manual |
| ORH-AUTH-S06 | Authentication | Check keyboard focus order on login form | P2 | Exploratory / accessibility smoke | Manual |
| ORH-AUTH-S07 | Authentication | Refresh login page and confirm it remains usable | P3 | Compatibility | Manual |
| ORH-PIM-S01 | PIM | Open Employee List | P1 | Smoke | employee-management.feature |
| ORH-PIM-S02 | PIM | Open Add Employee form | P1 | Functional | employee-management.feature |
| ORH-PIM-S03 | PIM | Submit employee form with required data missing | P1 | Negative / validation | employee-management.feature |
| ORH-PIM-S04 | PIM | Create an employee with unique valid test data | P1 | Positive | employee-management.feature |
| ORH-PIM-S05 | PIM | Verify saved employee details match input | P1 | Data validation | employee-management.feature |
| ORH-PIM-S06 | PIM | Search for an existing employee | P2 | Functional | Manual |
| ORH-PIM-S07 | PIM | Search for a nonexistent employee | P2 | Negative | Manual |
| ORH-PIM-S08 | PIM | Clear search criteria and repeat search | P3 | Functional / regression | Manual |
| ORH-PIM-S09 | PIM | Confirm duplicate employee identifier validation | P2 | Negative / data integrity | Manual |
| ORH-PIM-S10 | PIM | Check whitespace-only name values | P2 | Boundary / validation | Manual |
| ORH-PIM-S11 | PIM | Examine long-name handling against observed constraints | P3 | Boundary-value analysis | Manual |
| ORH-PIM-S12 | PIM | Cancel Add Employee without saving | P3 | State transition | Manual |
| ORH-PIM-S13 | PIM | Open an existing employee's details from results | P2 | Functional / data integrity | Manual |
| ORH-PIM-S14 | PIM | Verify pagination when multiple pages exist | P3 | Functional | Manual |
| ORH-PIM-S15 | PIM | Check employee ID format and boundary rules | P2 | Boundary / validation | Manual |
| ORH-NAV-S01 | Navigation | Open Dashboard after login | P1 | Smoke | login.feature |
| ORH-NAV-S02 | Navigation | Open PIM from the main menu | P1 | Smoke | core-navigation.feature |
| ORH-NAV-S03 | Navigation | Open Leave from the main menu | P2 | Smoke | core-navigation.feature |
| ORH-NAV-S04 | Navigation | Open Time from the main menu | P2 | Smoke | core-navigation.feature |
| ORH-NAV-S05 | Navigation | Open Recruitment from the main menu | P2 | Smoke | core-navigation.feature |
| ORH-UX-S01 | Usability | Check labels and required indicators on employee form | P2 | Exploratory | Manual |
| ORH-UX-S02 | Usability | Check clarity and proximity of validation feedback | P2 | Exploratory | Manual |
| ORH-UX-S03 | Usability | Inspect page layout at desktop viewport | P3 | Visual | Manual |
| ORH-UX-S04 | Usability | Inspect usability at narrower viewport | P3 | Responsive / exploratory | Manual |
| ORH-UX-S05 | Usability | Check loading/disabled states and repeated submission feedback | P3 | Exploratory | Manual |
| ORH-REG-S01 | Regression | Confirm rejected login does not open authenticated pages | P1 | Regression | login.feature |
| ORH-REG-S02 | Regression | Verify a newly created employee remains searchable | P1 | Regression | Candidate |
| ORH-REG-S03 | Regression | Navigate between Dashboard and PIM | P2 | Regression | core-navigation.feature |
| ORH-REG-S04 | Regression | Confirm search criteria do not corrupt subsequent searches | P2 | Regression | Manual |
| ORH-SEC-S01 | Security smoke | Confirm password text is masked in the UI | P1 | Security smoke | Manual |
| ORH-SEC-S02 | Security smoke | Ensure credentials are not committed or exposed in test logs | P1 | Repository/config review | Manual review |

## Coverage guidance

A scenario describes a behavioral objective. Detailed steps, expected results, test data, and run status belong in TEST-CASES.csv. Scenario priorities can change after risk analysis and after product requirements are clarified. Automation links identify implemented Gherkin coverage or future candidates; they are not claims of a passing result.
