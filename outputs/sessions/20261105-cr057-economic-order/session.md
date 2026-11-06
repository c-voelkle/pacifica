---
session: 20261105-cr057-economic-order
started: 2026-11-05
updated: 2026-11-06
mode: integrate
status: integrated
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

Second draft (6 November, 09:18 answers: research path from 0.6%, 35%, diffusion 0.9, champions driven): four separate agents checked it against the author's sources (`growth-sources.md`, `growth-scripts/`). The main revision is that research enters as an elasticity with diminishing returns, not as a constant 35%, so the engine gives about 2.0× (cautious), 2.1× (central) and 2.4× (upper). The storyline's MODEL figure is 2.24×. The note now suggests learning rates and a network premium, and puts two new questions: decision 2a and the target, decision 7.


## The growth engine built (6 November 2026)

After the 10:06 answers (steel 24%, research to 2%; CR-056 on branch `finance/dynamics-layer`, merged into this branch) the engine is built (`finance/build/cr057_growth_engine.py`; note `finance/CR-057-growth-workbook.md`). CR-057 with the engine: 2.23× US at US prices in 1929 (2.24× with the 1913 cover held), residents 36.1m (36.7m) in 1932; the old design gives the same output. Open: adopt the engine; the cover; charge research to the accounts; then iterate energy, re-run population, re-sync the storyline.

## Review applied (6 November 2026, afternoon)

The fresh-context review (`review-growth.md`) found the leak ratio understated (M1) and the stock elasticity inconsistent with the author's 35% (M2), among others; all applied except the iteration loop (S3, open). Rebuilt and iterated: 2.30× US at US prices in 1929, 36.5m at the end of 1932, price level 0.68 in 1929. Population re-run (gap −0.1% in 1932). Next: the author's go-ahead to integrate CR-057 with the re-synced MODEL figures and decision 4's sentence; §34's real-output sentence is a canon decision.

## Resume here

CR-057 is approved and integrated (6 November 2026; author: "I'm happy with the figures, you can integrate CR-057 and keep 'about 37 million'"):
- G1–G17 are in the storyline with coverage comments and local labels;
- the MODEL figures are re-synced: about 2.3 times in 1929, the laboratories, about 2.3 million vehicles, the atomic peak about half a percent;
- §34 is turned round at the author's choice: Pacifica ahead in real output from 1927, the Union ahead in money;
- register entry CR-057 added;
- ledger: C-1880-DEV-FUND revised and nine instruments added;
- character docs: three new dossiers (Calkins, Wang Yongjiang, Hayashi Kyūjirō) and CR-057 notes on Giannini, Baekeland, Tesla, Kashevarov, Takahashi and Zhang Zuolin;
- historical_background and AGENTS are updated;
- all checks are clean.

Branch `draft/cr057-economic-order` (PR #66) carries the CR, both workbooks and the CR-056 merge (PR #65's content). Next, if the author asks:
- find and break the workbook loop through the 1927 Japan rescue, then switch iteration off;
- drive the champions' world shares from the research channel (G8);
- the OPEN items in the register entry.
