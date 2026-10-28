---
session: 20261028-adopt-cr033-036
started: 2026-10-28
updated: 2026-10-28
mode: integrate
status: complete
baseline:
  commit: 9e46405
independence: separate-agents
---

# Adoption of CR-033 to CR-036

## Brief

- **Desired outcome:** check that CR-033 to CR-036 are complete, run the models, merge the four CRs in order and update the documentation.
- **Authorization:** author, 28 October 2026: "Let's first merge the crs that we have created in this thread. First, check if they are all complete. If so, run the models first and make sure everything checks out. Then merge 33, 34, 35, and 36 in that order and update all the relevant documentation."

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Approve the Polytechnic wave sizes (12/120 in 1858 … 90/1,400 in 1875) and apply CR-034 A24 (skilled entry from 1856) now | author 2026-10-28 | done |
| D2 | decision | Storyline population figures follow the workbook; CR-015's 1895 range is replaced | author 2026-10-28 | done |
| D3 | decision | CR-033 A18: "helps pay for" | author 2026-10-28 | done |
| D4 | decision | Merge CR-033, 034, 035, 036 in order and update the documentation | author 2026-10-28 | done |
| Q1 | open choice | Local OPEN items kept in the register: CR-033 A9 terms; royalty share; Japanese students' origin; the bishop; Julian's test | register `open` lists | open |
| Q2 | open choice | Ledger findings 1–12 | `commitments/README.md` | open |

## Handoffs

| ID | To | Task | Output | Status |
| --- | --- | --- | --- | --- |
| H1 | fresh reviewer | Integrated storyline: consistency, chronology, labels, literary effect | findings applied | done |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | Workbook with skilled entry from 1856, Paths C re-iterated to convergence | 51,127 formulas, 0 errors; Story 0 failed checks; Stress 11 (unchanged) |
| X2 | Population model scripts and tests | regenerated; 11 tests pass |
| X3 | lint_canon, cr_facts check, sync --check, character validator, ledger check | clean; 165 commitments |
| X4 | book-agent revision tests, commitments tests | pass |

## Resume here

CR-033 to CR-037 are adopted (CR-037 on 28 October, with the county rule). CR-038 (retirement at 68, Vallejo College, inspectors, scholarships, county halls, results-based pride, trades congress, guest-worker background) is a draft awaiting the author: confirm the reading of the county-hall sentence, the names, and the list of posted grants. A Crown-affiliated party is on hold. Ledger findings 1–12 still await the author.
