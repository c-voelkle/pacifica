---
session: 20261106-cr058-north-america
started: 2026-11-05
updated: 2026-11-06
mode: integrate
status: integrated
baseline:
  commit: 961ebae
independence: separate-agents
---

# Pacifica's relations with its North American neighbours, the Union's fuel, and Villa

## Brief

- **Desired outcome:** a strategy for Pacifica's relations with Canada and Mexico that keeps them from lining up with the Union and draws them into Pacifica's orbit; then who fuels the Union; then the Villa question and Patton's raid; then a CR and its integration.
- **Authorization:** Author, 5–6 November 2026, in a claude.ai chat attached to the Pacifica project: the brief ("help them stand against the Union as much as possible"); approvals of NA-1 to NA-13 (NA-10, NA-14 to NA-16 not taken), NA-12a to NA-12h, MX-1 to MX-7 (pending a fresh check) and MX-10 to MX-12, DH-1 to DH-4, IR-1 (IR-2 to IR-5 approved and deferred); the southern command's location delegated; "Just do the final fresh context check and then integrate it to main."
- **Sources of history:** Macfarlane, *Natural Allies* (2023), supplied by the author (not in the repo); CR-058.md in the claude.ai project; four fresh-context fact checks with web sources.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-11-05 | explore | Author: brainstorm Pacifica's relations with North America |
| 2026-11-06 | draft | Author: "Please write it into CR-058" |
| 2026-11-06 | integrate | Author: "do the final fresh context check and then integrate it to main" |

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | NA-1 to NA-9, NA-11, NA-13 as recorded in CR-058 | 5–6 Nov | current |
| D2 | decision | NA-12a to NA-12h: Standard a refinery without crude; Gulf crude mostly to the Union; Huasteca contracts; never embargo; Guffey; the 55% ceiling; the Caribbean understanding | 6 Nov | current |
| D3 | decision | MX-1 to MX-7, MX-10 to MX-12; the southern command at Tucson (delegated) | 6 Nov | current |
| D4 | decision | DH-1 to DH-4; IR-1, with IR-2 to IR-5 deferred to the confrontation CR | 6 Nov | current |
| Q1 | open choice | Storyline item 36 (the CR's open decisions) and Lago in 1925 (PROPOSED) | CR-058 | open |
| D5 | decision | DH-5: Doheny takes Turner's champions' seat about 1907–1924 after the Senate (about 1896–1907); recorded as CR-058-R1 | 6 Nov | current |

## Handoffs

| ID | To | Task | Inputs | Withheld | Output | Status |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | fresh-context reviewer | Fact-check Part IV (22 claims) | the claims | drafting conversation | folded into CR-058 | done |
| H2 | two fresh-context reviewers | Fact-check Parts I–III (51 claims) | the claims | drafting conversation | folded into CR-058 | done |
| H3 | fresh-context reviewer | Final review: remaining anchors and internal consistency | CR-058 draft | drafting conversation | 22 fixes, applied | done |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `cr_facts.py preview` on CR-058 | no fact changes declared |
| X2 | `lint_canon.py` | clean |
| X3 | `validate_character_docs.py` | valid; 229 dossiers (CT-FREDERICK-FUNSTON, CT-PANCHO-VILLA, CT-CHARLES-CAMSELL added; CT-DOHENY and CT-GEORGE-PATTON updated) |
| X4 | `commitments/ledger.py check` | 0 problems; 12 new commitments, 3 new parties |
| X5 | `sync_master_storyline.py --write`, `--check` | synchronized |
| X6 | pytest (revision and commitments tests) | 43 passed |

No fresh-context review of the integrated prose was run; the final review covered the CR draft.

## Resume here

- CR-058 integrated on `adopt/cr058` and merged to `main`.
- Next: the Anglo-Pacifican confrontation CR (it should carry IR-2 to IR-5, the Irish lever); a Union fuel row and Huasteca in the financial workbook; storyline item 36.
- CR-058-R1 (Doheny among the Five) integrated on `adopt/cr058-r1` and merged to `main`; CT10 settled. Lago in 1925 stays PROPOSED; Doheny's successor in 1924 is open.
