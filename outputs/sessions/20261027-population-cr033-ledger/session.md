---
session: 20261027-population-cr033-ledger
started: 2026-10-27
updated: 2026-10-27
mode: draft
status: paused-for-author
baseline:
  commit: 490bd49
independence: separate-agents
---

# Population model steps 2–3, CR-033 and the commitments ledger

## Brief

- **Desired outcome:** the population model with canon divergence factors; draft CR-033 for the canon changes; a workbook change list; the commitments ledger.
- **Authorization:** the author's decisions of 27 October 2026, recorded in `population/README.md` (decisions 1–6) and `book-agent/revision/drafts/CR-033-draft.md` (A1–A23). CR-033 is a draft and is not adopted. The workbook is not changed.

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Native Californians: disease without mass killing, then growth; the policy must pay for the Republic, not be charity | author 2026-10-27 | current |
| D3 | decision | Apply the change list to the workbook and test the Land Fund; widen Events beyond row 174 | author 2026-10-27 | done |
| D2 | decision | Land Fund, land warrants, register as title, grant confirmation, three-part compact, loss of land through leases (CR-033 A17–A23) | author 2026-10-27 "I approve of these decisions" | current |
| Q1 | open choice | CR-033 open choices (prices, annuity terms, boundaries, grant deadline; 1895 range; population figures in prose) | CR-033 draft | open |
| Q2 | open choice | Ledger findings 1–12 (Puʻuloa expiry 1924, Tokyo compact vs Concord, China "defense treaty", etc.) | `commitments/README.md` | open |

## Handoffs

| ID | To | Task | Output | Status |
| --- | --- | --- | --- | --- |
| H1 | fresh reviewer | CR-033 rev 3 consistency and literary effect | findings applied (draft impact notes) | done |
| H2 | four extraction agents | ledger entries by storyline range | merged into `commitments/data/ledger.toml`; quotes checked | done |
| H3 | this session | workbook edits per `population/workbook_change_list.md`; Land Fund costing (L1); Events to row 400 | `finance/CR-033-workbook.md` | done |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | lint_canon (full and --only CR-033), cr_facts preview | clean |
| X2 | commitments/ledger.py check | 164 entries, 0 problems |
| X3 | population and commitments unit tests | pass |
| X4 | LibreOffice recalculation of the 23 Oct workbook against saved Excel values | 63,415 cells identical |
| X5 | Revised workbook: recalculation, Checks | 51,127 formulas, 0 errors; Story 0 problems, Stress 11 (was 17) |
| X7 | Sale price tied to land values (author 27 Oct): sensitivities | finance/CR-033-workbook.md |
| X6 | Land Fund totals recomputed by hand (annuities, sales, survey, police) | agree |

## Resume here

Author to decide CR-033 adoption and the open choices, including A18 (the margin covers about 47% of assisted passage at the land-value price) and the 1932 population (32.6m in the workbook). Ledger findings 1–12 await the author.
