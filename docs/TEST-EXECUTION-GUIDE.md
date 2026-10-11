# Test Execution Guide

## Manual execution

1. Read manual-testing/TEST-PLAN.md and review the selected scope.
2. Record application URL, date/time, OS, browser/version, and account role.
3. Run cases from manual-testing/TEST-CASES.csv in the selected order.
4. For every executed case, record the actual result and one of the approved statuses.
5. Attach evidence for failures and any result where a screenshot/log adds value.
6. Create a defect using manual-testing/BUG-REPORTS.md only after reproducing the discrepancy.
7. Complete manual-testing/TEST-EXECUTION-REPORT.md for the run.

## Cypress-Cucumber execution

- Install dependencies with npm install.
- Copy .env.example to .env and add authorized test credentials locally if authenticated coverage is needed.
- Run npm test for the full suite.
- Run npm run test:smoke for scenarios tagged @smoke.
- Run npm run test:regression for scenarios tagged @regression.
- Review console output, generated Cucumber reports, screenshots, and videos.
- In CI, inspect the workflow run and download its artifacts.

## Classify failures before filing defects

| Failure category | Examples | Action |
|---|---|---|
| Product behavior | Reproducible mismatch against an approved expectation | Report defect with clear steps and evidence |
| Automation | Stale locator, incorrect assertion, test data bug | Fix test code; retain root cause notes if useful |
| Environment | Demo outage, slow response, external dependency | Record environment evidence; rerun when stable |
| Configuration | Missing or invalid credential, wrong base URL | Correct local/CI configuration without committing secrets |
| Ambiguous expectation | No requirement describes the observed behavior | Seek clarification before asserting a product defect |

## Execution integrity

A script that has been committed is not evidence of a passing scenario. A green job may still include skipped/pending scenarios. Record counts and statuses from the real run, and keep Not Run, Blocked, Skipped, Fail, and Pass distinct.
