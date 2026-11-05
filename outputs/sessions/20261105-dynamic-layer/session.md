---
session: 20261105-dynamic-layer
started: 2026-11-05
updated: 2026-11-05
mode: draft
status: paused-for-author
baseline:
  commit: 961ebae
  files:
    finance/Pacifica_financial_model_1846-1932.xlsx: sha256:cba70b3147a71cc9c0a4b977eeae3bca5de69313255723b167d5dc398c87059e
    energy/Pacifica_energy_model_1846-1932.xlsx: sha256:89807a6664a2beebc3056f289f8cef17467c2955b2438fbb9d98778acd8dfc17
independence: same-agent (design only; the build gets a separate reviewer)
---

# A switchable dynamic layer for the financial workbook: the second- and third-order effects of Pacifica's investments

## Brief

- **Desired outcome:** a `dyn_on` layer on top of the accounting baseline that turns physical investment into productivity, prices, wages, hours and household life, with a "life in Pacifica" table for the storyline.
- **Authorization:** author, 5 November 2026: "Can you please build the model described here?" (the handoff of 5 November). The handoff's method requires a design note approved by the author before building. No canon change.
- **Sources:** the handoff; `finance/investment-share-note.md` v2; `finance/CR-051-054-055-workbook.md`; `finance/CR-052-workbook.md`; `energy/CR-052-workbook.md`; the workbooks' formulas.

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| Q1–Q12 | open choice | See `finance/dynamics-design-note.md` §8 | raised in session | open |

## Round log and stop reason

| Round | Date | What changed | Stop reason |
| --- | --- | --- | --- |
| 1 | 2026-11-05 | Design note `finance/dynamics-design-note.md` | Blocked on Q1–Q12 (the channel choice is the author's) |

## Resume here

Design note written on branch `finance/dynamics-layer`; nothing built. Next: on the author's answers to Q1–Q12, write `finance/build/cr056_dynamics.py` (§9 of the note), add the energy exports, run the `dyn_on` = 0 identity test against `cba70b31…`, then the four recalculations, the review and the PR.
