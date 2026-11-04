---
session: 20261103-cr052-energy-workbook
started: 2026-11-03
updated: 2026-11-04
mode: draft
status: merging
baseline:
  commit: 04155c7
  files:
    finance/Pacifica_financial_model_1846-1932.xlsx: sha256:22266bad58ee60da888c9b8de9bcd2c964498a5427d6b453b1f6a5a46f6120b2
independence: separate-agents (fresh-context reviewer for CR-052)
---

# Build the energy workbook the handoff specifies and add it to the repository

## Brief

- **Desired outcome:** a power generation and consumption workbook, like the financial workbook, that tracks every source of power and its uses and correlates with the financial workbook.
- **Authorization:** author, 3 November 2026: "create a power generation and power consumption workbook similar to the financial workbook …"; then, with `claude/energy-workbook-handoff.md`: "Can you make this energy workbook according to the specifications outlined here and then add it to the project repository?" The master storyline and the financial workbook are out of scope (no edits).
- **Sources:** the handoff; project docs CR-051, CR-051 power check, CR-020, the science-engineering ledger; the financial workbook at the baseline SHA. census.gov and USGS PDFs unreachable.

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Build the workbook to the handoff and add it to the repository. | author message 2026-11-03 | current |
| D2 | decision | CT3 A, B and C approved ("with the greatest believable haste in finding the Los Angeles basin giants"); California the most motorized place on earth (CT5 amended); explore a Max case of maximal energy use. | author messages 2026-11-03 | current |
| D3 | decision | Narrowed Max into Story (M1, M6, M7 Boulder only, M8, M9); M2 to finance via the investment share; M3/M4 reworked as CR-054; CR-053 concessions; CT6 Hilo on the hydro board; Ryan in the power seat from 1924 | author messages 2026-11-04 | current |
| D4 | decision | CR-054 amounts, division of labour and storyline sentences; CR-055 R0 in full (early river, four purposes, McNary and Chief Joseph) | author messages 2026-11-04 | current |
| D5 | decision | CT9: Ryan replaces Steinmetz (successor seat and the halls' supply); CR-054 A6: join the nitrogen convention, stay out of the aluminium cartel; paperwork consolidated with newer statements replacing older; hydrogenation with fewer barrels; workbook consistent with itself and the story; report before merging or rebuilding finance | author message 2026-11-04 16:29 | current |
| D6 | decision | CR-054 A6 means the European cartel; Northwest capacity added to keep both the line and the mill boilers; CT1 wording amended at integration; CT2 approved (adapt); Max and Stress side effects accepted; rebuild the financial workbook and report before merging | author message 2026-11-04 17:07 | current |
| D7 | decision | The 1932 compact a price floor; the extra residents accepted (about 37 million in 1932 at integration); the `inv_share` path adopted with `ind_src` = 1; CR-053 amounts approved; CR-055 CT4 adapt to canon; rebuild both workbooks and merge PR #61 | author message 2026-11-04 18:29 | current |
| Q1 | open choice | W1, F1–F4, F10, F12; `halls_after`; CR-053 entitlement form and ledger entries; CR-055 R1–R9 open items; the industrial-output derivation (`ind_src` = 2); a world oil-price response; CR-052–055 integration into the storyline | `CR-052.md`, `finance/CR-052-workbook.md`, `CR-053.md`, `CR-055.md` | open |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | LibreOffice recalculation, Story and Stress | 22,633 formulas, 0 errors in both |
| X2 | Workbook Checks sheet, tests 1–9 | Story: 7 fails 1900–23, 1925–26, 1932; 6 fails 1916; 4 fails 1932. Stress: 2 (1922), 6 (9 years before 1927), 9 (1923–27) |
| X3 | Sensitivity runs (mid-Columbia chain, main-line electrification, Gulf crude, Realm coal ×4, Asian sales, Works' dams +30%, industrial weight 0.7 and 1.0) | in `energy/CR-052-workbook.md` |
| X4 | Fresh-context review (separate agent) | `outputs/CR-052/review.md`; five MUST FIX applied in the second build |
| X5 | Second fresh-context review (separate agent) of the third build | `outputs/CR-052/review-2.md`; three MUST FIX applied in the fourth build (field-model oil, Kettleman 1923, no double counting in Max) |
| X6 | LibreOffice recalculation, fourth build, three cases | 23,722 formulas, 0 errors in each |
| X7 | Eleventh build: LibreOffice recalculation, three cases | 28,765 formulas, 0 errors in each; Story and Max pass every check in every year; Stress fails 3 (1876–1916), 2 (1922), 9 (1923–24) |
| X8 | Reproduction from the committed inputs (tenth build, before the changes) | finance import identical; rebuilt workbook equal cell by cell to the committed one |
| X9 | `lint_canon.py --only` on CR-052–055 | clean except the expected unknown ID CT-HARRIS-RYAN (registered at integration) |
| X10 | Twelfth energy build and the financial workbook's energy link, iterated to a fixed point | energy 29,029 formulas, finance 54,321, 0 errors; energy outputs unchanged on the last pass; Story: no check fails in either workbook |
| X11 | Fresh-context review of the finance build (separate agent) | results table and switches confirmed; five errors found (residents do rise; GDP decomposition; CR-053 stakes financed twice; net-exports flows; Stress and SHA statements) and all corrected; the finance series the energy workbook reads are unchanged by the fixes |

## Resume here

The author's decisions of 4 November evening are applied (compact a price floor; extra residents accepted; `inv_share` adopted with `ind_src` = 1; CR-053 amounts; CR-055 CT4 adapt), both workbooks rebuilt to a fixed point (no Story check fails in either), and PR #61 merged into `main` on the author's instruction. CR-052–CR-055 remain PROPOSED decision records with their approvals noted; nothing in the master storyline is changed. Next: integrate CR-052–055 into the storyline (the population "about 37 million", the CT1 wording, CT9's two Steinmetz sentences, Ryan's registry entry, the Hawaiian hydro board, CR-054's and CR-055's sentences) and register them in `change_requests.json`; the financial workbook's CR-054/055 champions and CR-051 costs.
