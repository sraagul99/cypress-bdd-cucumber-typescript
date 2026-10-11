# Defect Register and Reporting Standard

## Current register

No OrangeHRM application defects are asserted in this repository yet. Add an entry below only after reproducing an issue on the current demo and documenting evidence.

| Defect ID | Summary | Severity | Priority | Environment | Status | Evidence |
|---|---|---|---|---|---|---|
| — | No verified defects recorded yet | — | — | — | — | — |

## Defect report template

### Title
[Module] Concise, observable failure

### Environment
- Date/time and time zone:
- Application URL/version:
- Browser/version and OS:
- Account role (no password):
- Related manual case / feature scenario:

### Preconditions
1. [State required to reproduce]

### Steps to reproduce
1. [Action]
2. [Action]
3. [Action]

### Expected result
[Behavior grounded in a requirement or agreed product behavior]

### Actual result
[What occurred, with concrete messages/data; do not guess root cause]

### Classification
- Severity: Critical / High / Medium / Low
- Priority: P1 / P2 / P3 / P4
- Reproducibility: Always / Intermittent / Once
- Type: Functional / Validation / UI / Data / Compatibility / Security / Automation / Environment

### Evidence
- Screenshot/video:
- Sanitized console/network evidence:
- Test data used (synthetic only):
- Related test ID and execution run:

### Triage / retest history
- Owner/status:
- Fix version:
- Retest result and date:
- Regression coverage:

## Reporting standard

Write defects so another engineer can reproduce the observed behavior without a verbal explanation. Separate facts from hypotheses. Distinguish a product defect from test-code defects, demo-environment instability, and unavailable credentials.
