---
session: 20261102-cr049-nomos
started: 2026-11-02
updated: 2026-11-02
mode: adopt
status: paused-for-author
baseline:
  commit: 3296de3
independence: separate-agents
---

# Approve the suggested parts of CR-049, fix the tone, cut the invented cast and add the Babbage and Boole anchors

## Brief

- **Desired outcome:** CR-049 recorded as approved in part, with the atomic branch returned.
- **Authorization:** Author, 2 November 2026: "Ok let‘s first approve the suggested sections and fix the tone in I. I want less of the invented scientists and mathematicians for sure. Maybe just one or two if absolutely necessary for the plot’s development. Also add the Babbage and Boole anchors." The suggested sections came from the review in the same chat: approve N, E and I once the tone is fixed, T1 Case A, C1 with Babbage and Boole anchors; return S1/S2; rework P1 and the expeditions. Integration (storyline prose, facts, characters) is out of scope until the author asks.

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Approve N1–N3, E1–E4, I1–I2 (T1 Case A), C1 | author 2026-11-02 | current |
| D2 | decision | Fix the tone (legal-brief hedging) | author 2026-11-02 | current |
| D3 | decision | One or two invented scientists at most; five cut. Liang Wenqi and Mele Kealoha are the drafter's PROPOSED choice within the limit (P1) | author 2026-11-02 | current |
| D4 | decision | Babbage and Boole anchors added to C1 | author 2026-11-02 | current |
| D5 | decision | Keep Liang and Mele (P1 approved); rework the atomic branch, requirements 1–5 | author 2026-11-02 | current |
| Q1 | open choice | Integration of the approved groups | — | open |
| Q2 | open choice | O4: expedition episodes with real danger | review | open |
| D6 | decision | Approve the atomic rework, requirements 1–5 (S1, S2) | author 2026-11-02 | current |
| Q3 | open choice | Requirements 6–7 and G1: when the programme goes secret, under whose authority, the Five | author question 2026-11-02 | open |
| D7 | decision | Peirce replaces Liang, Japan at seventeen; atomic estate seat under Hillebrand (dates and history to propose) | author 2026-11-02 | current |
| D8 | decision | Watkins dropped; Kate Layne (Curran, Brandegee) follows up Niépce; Kamakau approved; the Light and Matter Works named | author 2026-11-02 | current |
| Q5 | open choice | F1 dates (1883, 1887) and G1 secrecy design | drafter proposal | open |
| Q6 | open choice | Requirement 6: brainstorm on consequences after 1892 | author 2026-11-02 | open |
| Q4 | open choice | Names of the two new elements | rework round | open |

## Handoffs

| ID | To | Task | Inputs | Withheld | Output | Status |
| --- | --- | --- | --- | --- | --- | --- |
| H2 | Fresh reviewer | Atomic rework: mechanisms, requirements 1–5, history, canon, safety, labels | CR-049.md, AGENTS.md, background sections, storyline passages | drafter's reasoning and the chat | `outputs/CR-049/review.md` (round 3) | done; F10–F19 repaired |
| H1 | Fresh reviewer | Consistency, tone, cast, anchors, payload | CR-049.md, AGENTS.md, affected storyline passages, background section | drafter's reasoning and the chat | `outputs/CR-049/review.md` (round 2) | done; F1–F9 repaired |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `sync_master_storyline.py --write` / `--check` | pass |
| X2 | `cr_facts.py check` | pass (34 approved fact changes; CR-049 facts deferred) |
| X3 | `cr_facts.py preview --tensions CR-049.md` | all payloads parse; only findings are the two unregistered IDs, expected until integration |
| X4 | `lint_canon.py` | clean, 4 files |
| X5 | `validate_character_docs.py` | pass |
| X6 | `commitments/ledger.py check` | 188 commitments, 0 problems |

## Resume here

CR-049: N, E, I, C1, P1/P2 (Peirce, Kate Layne, Kamakau), S1/S2 and the Light and Matter Works' seat approved; integration pending. Proposed: the Works' dates and the G1 secrecy settlement. Now brainstorming requirement 6 (the world after 1892); then element names, O4.
