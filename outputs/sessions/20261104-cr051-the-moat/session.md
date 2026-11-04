---
session: 20261104-cr051-the-moat
started: 2026-11-03
updated: 2026-11-04
mode: integrate
status: integrated-pr-open
baseline:
  commit: 04155c7
independence: separate-agents
---

# How Pacifica's atomic lead stays as wide and secure as possible from 1908 to 1932, believably

## Brief

- **Desired outcome:** a critical review of the atomic arc (CR-049 to CR-050-R1) against Norris, *Racing for the Bomb*, and Shea (ed.), *Otto Hahn and the Rise of Nuclear Physics*; then the next CR, on the moat, the secret and how Pacifica secures its lead; then its integration.
- **Authorization:** Author, 3 November 2026, in a claude.ai chat attached to the Pacifica project: "make the focus of this one be the moat, the secret and Pacifica secures its lead" (dependence strategy left to a separate CR); eight rounds of approvals, the seventh after a fresh-context review ("Yes please add them as proposed"), the eighth on the power check ("I approve the suggested six fixes for CR-051"). Integration, 4 November 2026: "Ok go ahead and merge CR-051 to main and integrate the changes to the master storyline please."
- **Sources of history:** the review `claude/CR-049-050-atomic-review.md` and the drafting rounds (claude.ai project); the reference texts (OCR'd in the drafting session; not in the repo).

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-11-03 | explore | Author: critical review of CR-049–CR-050-R1 |
| 2026-11-03 | draft | Author: brainstorm and draft the next CR |
| 2026-11-03 | draft | Author: fresh-context review, then the nine points; power check |
| 2026-11-04 | integrate | Author: "merge CR-051 to main and integrate the changes" |

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | The lead rests on the two hard facts and the industry, not on fission staying secret (P1) | 3 Nov | current |
| D2 | decision | Hahn stays in 1920, with his reasons explicit (E5–E6) | 3 Nov | current |
| D3 | decision | Build big (M2) | 3 Nov | current |
| D4 | decision | Sibert as the Chief; Tsingtao; the Birmingham route; two phases; the leadership structure; the Columbia compacts | 3 Nov | current |
| D5 | decision | Fowler's memo; no Fowler–Rutherford marriage; Part II sealed to 1947 | 3 Nov | current |
| D6 | decision | The nine review fixes and all remaining proposals as proposed | 3 Nov | current |
| D7 | decision | The six power fixes (the war's nitrogen power; the Works' dams; the halls the district's largest load, published; Tribune and Tizard evidence) | 3 Nov | current |
| D8 | decision | An energy workbook in its own session (handoff `claude/energy-workbook-handoff.md`) | 3 Nov | done elsewhere (CR-052, unmerged) |
| Q1 | open choice | The Villa question; Chihuahua and Patton's raid | CR-051 C5 | open (military CR) |
| Q2 | open choice | The dependence strategy after 1927 | CR-051 | open (separate CR) |
| Q3 | open choice | Birmingham works' founding date; Senate budget committee; Columbia bands' leaders; the Pit and Feather compacts | CR-051 | open |
| Q4 | open choice | CR-052 CT1–CT2 and CR-055 CT1, CT4 amend CR-051; not applied | other CRs | open |

## Handoffs

| ID | To | Task | Inputs | Withheld | Output | Status |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | fresh-context reviewer | Review CR-051 draft | CR-051, CR-049, CR-050, CR-050-R1, earlier review, both texts | drafting conversation | `outputs/CR-051/review.md` | done (3 Nov) |
| H2 | fresh-context reviewer | Review the integrated prose | storyline and bible diffs, CR-051, AGENTS.md | drafting conversation | `outputs/CR-051/review-integration.md` | see round log |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `cr_facts.py preview` on the draft | 16 fact changes; no stale passages; Hoover already registered as CT-HOOVER |
| X2 | `cr_facts.py apply CR-051` | canon_facts.toml updated; lint clean |
| X3 | `lint_canon.py` | clean after one fix (the first hall's year in Langmuir's dossier) |
| X4 | `validate_character_docs.py` | valid; 225 dossiers |
| X5 | `ledger.py check` | 202 commitments, 0 problems |
| X6 | `sync_master_storyline.py --write/--check` | synchronized |

## Round log and stop reason

- 4 Nov: integrated on `adopt/cr051` (commit 0232da4); fresh-context review of the integrated text requested (H2).

## Resume here

CR-051 integrated on branch `adopt/cr051` and proposed for `main`. Open after it: the military CR for 1899–1917 (Tsingtao in detail, the Villa question), the dependence-strategy CR, CR-052's CT1–CT2 and CR-055's CT1 and CT4 (amendments to CR-051, not applied), the financial workbook's costs for the halls, the feed plant, the Columbia station and the Works' dams.
