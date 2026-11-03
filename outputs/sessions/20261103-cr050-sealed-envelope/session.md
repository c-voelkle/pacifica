---
session: 20261103-cr050-sealed-envelope
started: 2026-11-02
updated: 2026-11-03
mode: integrate
status: integrated-pr-open
baseline:
  commit: 642b605
independence: separate-agents
---

# How Pacifica keeps its atomic lead from fission (1908) to the demonstration (1927), told with justice to the science, believable institutions and the widest lead

## Brief

- **Desired outcome:** the next CR after CR-049, drafted, approved and integrated: the secrecy settlement (CR-049 G1), the light isotope, the magnet halls, Europe's response and the knock-ons of published discoveries.
- **Objective:** the author's three goals (2 November 2026): justice to the scientific achievement; believable competitive institutions and knock-ons; Pacifica's lead in atomic research as wide as possible.
- **Authorization:** Author, 2–3 November 2026, in a claude.ai chat attached to the Pacifica project, using Richard Rhodes's *The Making of the Atomic Bomb* as the reference text. Shape B+C chosen ("A sealed envelope, with competition on the inside"); five rounds of approvals, the last: "Approved. Please do the fresh context check and then proceed with integration." Weapon design stays off the page (CR-049).
- **Sources of history:** CR-049 (project copy and `integrate/cr-049`, PR #59, unmerged at start); the planning ledger `claude/science-engineering-ledger.md`; Rhodes for secrecy, institutions and industry.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-11-02 | explore | Author: discussion of Rhodes; review of CR-049 for blockers |
| 2026-11-03 | draft | Author: "Agreed, please draft the next CR." |
| 2026-11-03 | integrate | Author: "Approved. Please do the fresh context check and then proceed with integration." |

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Shapes B and C: a sealed envelope with competition on the inside | author 2026-11-03 | current |
| D2 | decision | P13 changes; faster understanding of uranium; no radium craze but true noise led by health effects; hide behind greed, staged charity, concessions against the salt; isotope sequence and magnet halls approved | author 2026-11-03 | current |
| D3 | decision | X1, X3, X4; Haas 1907; Hahn 1920; Rutherford outside the wall; R1; Nishina 1922; Langmuir succeeds Hillebrand | author 2026-11-03 | current |
| D4 | decision | S1–S4 secrecy sequence, G3 term, G5 opening, X5 (underwater, site moved south), X6 (late 1913); Julian visits the dying Hillebrand | author 2026-11-03 | current |
| D5 | decision | Breeder sequence and three fusion layers; thorium deferred to a later CR | author 2026-11-03 | current |
| D6 | decision | Millikan and Nagaoka as the two insiders of 1920; Tokyo station 1927/1928/1931/29 April 1932 | author 2026-11-03 | current |
| Q1 | open choice | The walled college's site | draft | closed by D7: Hetch Hetchy (CR-050-R1); terms B2–B5 proposed |
| Q2 | open choice | The desert test's site and exact date (c. 1923–1924) | draft | open |
| Q3 | open choice | Whose name for the split sticks | draft | open |
| Q4 | open choice | Workbook revision: the Atomic sheet still has CR-049's dates (halls from 1912, Tokyo 1925–1927) | integration | open |
| Q5 | open choice | Thorium | author | deferred to a later CR |
| D7 | decision | Hetch Hetchy as the walled college's site ("I like it"); Yerba Buena College renamed, drafter to choose (Humboldt College) and lint with this CR | author 2026-11-03 | current |
| Q6 | open choice | CR-050-R1 B2–B5: the Tuolumne Station, the Me-Wuk compact, Humboldt's Compact of the Tuolumne, Eleanor and Cherry water, Muir | drafter proposal | open |

## Handoffs

| ID | To | Task | Inputs | Withheld | Output | Status |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | Fresh reviewer | Historical fact-check of every claim presented as historical | CR-050.md | the chat and the drafter's reasoning | `outputs/CR-050/review.md` §1 | done; twelve qualifiers applied, no errors |
| H2 | Fresh reviewer | Consistency and literary review of the integrated storyline | AGENTS.md, storyline diff, full storyline, CR-050 canon tensions | the chat, the body of CR-050 and the drafter notes | `outputs/CR-050/review.md` §2 | done; F1–F23 repaired |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `cr_facts.py apply CR-050` | 18 fact changes applied; no stale passages |
| X2 | `lint_canon.py` | clean |
| X3 | `cr_facts.py check` | pass (72 approved fact changes) |
| X4 | `validate_character_docs.py` | pass (nine new dossiers, ten updated) |
| X5 | `commitments/ledger.py check` | pass (196 commitments; Joachimsthal rider amended, Tokyo fuel lease added) |
| X6 | `sync_master_storyline.py --write` / `--check` | pass |

## Round log and stop reason

| Round | Date | What changed | Stop reason |
| --- | --- | --- | --- |
| 1 | 2026-11-03 | CR-050 drafted, approved in five rounds, fact-checked and integrated on `integrate/cr-050`, stacked on PR #59 | Usable integration; Q1–Q4 need the author |

## Resume here

CR-050 and CR-050-R1 (Humboldt College; Hetch Hetchy approved in direction) are integrated on `integrate/cr-050`, PR #60, stacked on `integrate/cr-049` (PR #59); merge #59 first. Open: the college's site (Q1), the desert test's site and date (Q2), whose name for the split sticks (Q3), and a workbook revision for the halls' and the Tokyo station's new dates (Q4). Next CRs still queued from CR-049: how Pacifica mines and buys more uranium; Canada policy (affects Dempster); element names; O4 expeditions; thorium.
