---
session: 20261105-cr057-economic-order
started: 2026-11-05
updated: 2026-11-06
mode: draft
status: paused-for-author
baseline:
  commit: 961ebae
  files:
    book-agent/revision/master_storyline.md: sha256:3ce6bfa4792fc3a7ad04ad21271b9ffce07f8c22e136c7f9cfb0f64c38b092d6
    book-agent/revision/change_requests.json: sha256:2fb5ac084dcbdd354809e3253f336b5af9b381e1d99e0c56a11890d2f6e8a577
independence: separate-agents
---

# How Pacifica's economic system can be made rigorous enough to survive its hardest critic

## Brief

- **Desired outcome:** a reading guide to Mises's *Human Action* for Pacifica's economy; a review that runs Mises's objections against the design; then a CR carrying the author's decisions and the follow-up proposals.
- **Authorization:** Author, 5 November 2026, in a claude.ai session attached to the Pacifica project:
  - "I'm trying to tighten the economic system in Pacifica and make it more rigorous."
  - The review note ("Yes that would indeed be helpful").
  - The MR-01 direction (falling prices; state capitalism on the contemporary Chinese model).
  - The fifteen decisions of 11:42.
  - "Yes please draft it with the proposed solutions to 03, 08, 09, 11 (specify which zones abroad would work particularly well to Pacifica's advantage), and 12 (maybe make it optional but tax deductible up to a certain yearly amount like Switzerland's Säule 3a)".
  - Not authorized: storyline, register or workbook changes.
- **Sources of history:** the author's copies of Mises, *Human Action* (Scholar's Edition) and Mankiw, *Macroeconomics* (12th ed.), read in the session and not in the repo. Two separate agents digested the Mises sections; every quotation in the review was checked verbatim by script. The claude.ai project doc `claude/CR-056-dynamics-workbook.md` (the dynamics layer, not yet in this repo) was read for consistency.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-11-05 | explore | Author: which Mises chapters matter for Pacifica's economy |
| 2026-11-05 | draft | Author: the review note (`outputs/research/20261105-mises-review/Mises-review.md`) |
| 2026-11-05 | draft | Author: decisions on MR-01 to MR-15; "please draft it" (CR-057) |

## Author decisions and open choices

| ID | Status | Detail |
| --- | --- | --- |
| D1 | decided | MR-01 to MR-15, as recorded in CR-057 A and the review's part I |
| D2 | decided | The Fund's default (15:52): leased public land, half the guest-worker levy, nothing spent before 1910 and 3% from then (CR-057 C, CT12) |
| D3 | decided | Second round (16:21): B's ratios and guards; Elias writes the charter; widen the rent base first; D's customers; open patents and auctions from the start; five districts abroad, Huludao and Mariveles as scenes; F's caps; the income tax a war measure; G1–G12 and the refusal scene (CR-057 A2) |
| Q1 | open | CR-057 A2's suggestions (PROPOSED), the revised G2, G5, G8, G10 and the new G13–G16, CT13 and CT14; previously: CR-057 B to F (the reserve compact's ratio and guard; the Fund as a sovereign wealth fund; the river's customers; open patents, auctions and districts; the provident account) and the G wording |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `lint_canon.py --only CR-057.md` | clean |
| X2 | `cr_facts.py preview CR-057.md` and `--tensions` | no fact changes declared; no tension carries fact changes |
| X3 | Fresh-context review (separate agent; `review.md`) | 7 must-fix, 11 should-fix, 14 notes; all applied, F32 partly |
| X4 | Second fresh-context review of the third draft (separate agent; `review-2.md`) | 3 must-fix, 29 should-fix, 11 notes; all applied in the fourth draft |

## Growth design note (6 November 2026)

The workbook rebuild of 5 November (`finance/CR-057-workbook.md`) left Pacifica about a fifth poorer. A decomposition of the old model (CR-057 off) showed that the base path gives about 1.5× the Union. The Development Fund's 30% non-depreciating return gives most of the rest (to 2.37×). The author asked for a believable path to the old 2.4× and approved a growth engine built on research, diffusion, learning curves, selection, ordinary capital and income from abroad: "Yes that sounds much more accurate". `finance/CR-057-growth-design-note.md` (G1–G8) awaits the author's decisions (its §7). No rebuild until approved.

## Resume here

CR-057 (fourth draft: A2 and the second review applied) is drafted (PROPOSED) on branch `draft/cr057-economic-order` and awaits the author's decisions on B–F and the G wording. A fresh-context review is filed in `outputs/sessions/20261105-cr057-economic-order/review.md` (F1–F32) and its findings are applied in the second draft. Nothing in the storyline, register, ledger or workbooks is changed. After approval:
- integrate G into the storyline with coverage comments;
- add the register entry and the ledger instruments (I);
- run sync and the checks;
- then the workbook builds in H's order (money block, saving account, the Fund, wages and prices, the energy loads, auctions).

The dynamics workbook (CR-056) lives in the claude.ai project and is not yet in this repo; check its status before H4.
