# Defect Lifecycle

Statuses vary between teams; adapt the names below to the project's actual workflow.

1. **New** — reproducible observation documented with expected/actual behavior.
2. **Triaged** — validity, impact, severity, priority, and ownership reviewed.
3. **In Progress** — investigation or implementation underway.
4. **Ready for Retest** — fix is available in a known environment.
5. **Retest** — original reproduction steps and related regression cases executed.
6. **Closed** — acceptance criteria are met and evidence supports closure.
7. **Reopened** — issue persists or recurs after a fix attempt.
8. **Deferred / Rejected / Duplicate** — used with explicit rationale.

## Severity vs. priority

- **Severity** describes impact on functionality, users, data, or risk.
- **Priority** describes how urgently a fix should be addressed.

Assess both using product context. A high-severity defect is not automatically the highest priority in every project, and vice versa.

## Triage questions

- Is the behavior inconsistent with a requirement or established expectation?
- Can it be reproduced in the stated environment?
- Does the issue affect one user, a role, a workflow, or all users?
- Is data lost, corrupted, exposed, or incorrectly persisted?
- Is there a safe workaround?
- Is the failure caused by the product, test code, credentials, or the public demo environment?

## Retest and closure

Retest against the proposed fix, preserve evidence, and run associated regression checks. Close a defect only when the expected behavior is verified. If the issue remains, document actual behavior and reopen it using the team's process.
