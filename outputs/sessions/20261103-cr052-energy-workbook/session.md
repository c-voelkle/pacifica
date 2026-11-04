---
session: 20261103-cr052-energy-workbook
started: 2026-11-03
updated: 2026-11-04
mode: draft
status: building
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
| Q1 | open choice | W1, F1–F4, F10, F12; CT1, CT2, CT4; `halls_after`; CR-053 open items; CR-055 R1–R9 open items | `CR-052.md`, `CR-053.md`, `CR-055.md` | open |
| Q2 | open choice | CR-054 A6: confirm "the aluminium pool" meant the European cartel, not the Concord pool | `CR-054.md` | open |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | LibreOffice recalculation, Story and Stress | 22,633 formulas, 0 errors in both |
| X2 | Workbook Checks sheet, tests 1–9 | Story: 7 fails 1900–23, 1925–26, 1932; 6 fails 1916; 4 fails 1932. Stress: 2 (1922), 6 (9 years before 1927), 9 (1923–27) |
| X3 | Sensitivity runs (mid-Columbia chain, main-line electrification, Gulf crude, Realm coal ×4, Asian sales, Works' dams +30%, industrial weight 0.7 and 1.0) | in `energy/CR-052-workbook.md` |
| X4 | Fresh-context review (separate agent) | `outputs/CR-052/review.md`; five MUST FIX applied in the second build |
| X5 | Second fresh-context review (separate agent) of the third build | `outputs/CR-052/review-2.md`; three MUST FIX applied in the fourth build (field-model oil, Kettleman 1923, no double counting in Max) |
| X6 | LibreOffice recalculation, fourth build, three cases | 23,722 formulas, 0 errors in each |

## Resume here

The CR-051 integration (branch `adopt/cr051`, not yet on `main` when this was written) is merged into this branch. Paperwork consolidated (4 Nov): CR-052 sixth draft, CR-054 A6 recorded, CR-055 R3 and CT1 aligned with the integrated CR-051. Next: the eleventh workbook build (the line used, the hydrogenation works resized, the diffusion plant of 1930–32, stale notes), then the figures in CR-052–055, the README and the workbook note refreshed from it, and a report to the author before merging PR #61 or rebuilding the financial workbook.
