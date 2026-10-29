---
session: 20261029-cr041-plan-c
started: 2026-10-29
updated: 2026-10-29
mode: adopt              # history: explore → draft → adopt
status: paused-for-author
baseline:
  commit: 14a16f3
  files:
    book-agent/revision/master_storyline.md: sha256:525dbd45a00d6b041d181ab0b830196dd14b62be75e4eadf9ef1bebee4af0c07 (before this session's note)
    book-agent/revision/change_requests.json: sha256:f0fbc38c4cf67b64e2a098084a6952ad38725e0657339adf7240b57430e314d0
independence: same-agent (planning, drafting and verification by one agent; the author decided each item; no fresh-context review yet — the CR is a decision record, not prose)
---

# How should the Russian war of 1918–1920 actually be fought, and who signs for Russia?

## Brief

- **Desired outcome:** a re-planned Russian war for CR-040 Stages 3–4 that uses the enemy's year without an army, names the Russian partner, keeps the approved 1920 sequence, and gives Julian's drift from Victoria his own signature.
- **Objective:** Julian's effective power by 1932 (a Russia that owes Pacifica its survival, credit and borders) with the literary aim of an honest betrayal.
- **Authorization:** author, 29 October 2026: "I approve of C" (the eighteen-month plan with a maximal 1918); "Bring them into the new CR and let's decide on all of them right now"; "For N10 I would like a Hawaiian name. For N13 b."; "I approve. You can add it into the CR just like that (the more detailed version of shape C). Pacifica keeps the oil from Emba and should get favorable conditions in Baku as well"; "Can you add this to the repo as a new branch and then carry out the merge sequence?" Out of scope: integration of the storyline prose (Stages 3–4 and CR-041 together), which the author has not yet authorised as a prose revision in this session.
- **Sources of history:** the planning correspondence (CR-041.md Appendix B, non-canonical); CR-040 and its Stage 3–4 draft; web checks of 29 October 2026; the author's supplied PDFs (Amanzholova 1997 ×2, Amanzholova 2003, Sabol 2003 preview) and the Alash-Orda Sbornik dokumentov (1929/1992) — all cited in historical_background.md §CR-041.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-10-29 | explore | Author: "discuss this scenario from the perspective of a professional military strategist" |
| 2026-10-29 | draft | Author: "write this up as a new change request" |
| 2026-10-29 | adopt | Author: "add this to the repo as a new branch and then carry out the merge sequence" |

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Plan C adopted: one summer to seize (1918), one winter to strangle, the Russians take Moscow in the second winter | author 2026-10-29 | current |
| D2 | decision | S1–S9 and N1–N16 as recorded in CR-041.md §1 | author 2026-10-29 | current |
| D3 | decision | N6: Siberia enters federal Russia by the Tomsk Duma's vote of 1921, promised to Wrangel in 1919; Alash unasked | author 2026-10-29 | current |
| D4 | decision | Oil: Emba kept; Grozny and Maikop from Wrangel's government; Baku shared with Britain | author 2026-10-29 | current |
| Q1 | open choice | Which Ukraine (Hetmanate or Directory) and the Black Sea coast | raised in session | open |
| Q2 | open choice | Bessarabia; Kars–Ardahan–Batum | raised in session | open |
| Q3 | open choice | What Alash keeps inside Russia after 1921; its regiments | raised in session | open |
| Q4 | open choice | Authorise the prose integration of CR-040 Stages 3–4 and CR-041 together | this record | open |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `python3 tools/session.py start --topic cr041` | pass (main current, no unmerged branches) |
| X2 | `sync_master_storyline.py --write` then `--check` | pass |
| X3 | `lint_canon.py` | clean, 4 files |
| X4 | `cr_facts.py check` | pass (CR-041 facts deferred; register facts empty) |
| X5 | `cr_facts.py preview book-agent/revision/CR-041.md` | 12 passages in 4 files to revise at integration (recorded in CR-041.md) |
| X6 | `validate_character_docs.py` | pass |
| X7 | `commitments/ledger.py check` | 171 commitments, 0 problems |
| X8 | `python3 -m unittest discover -s book-agent/revision/tests` | 19 tests OK |

## Round log and stop reason

| Round | Date | What changed | Stop reason |
| --- | --- | --- | --- |
| 1 | 2026-10-29 | CR-041.md decision record; register entry (approved_directions_integration_pending); CR-040 register note; storyline integration note; AGENTS.md paragraph; historical_background §CR-041; provisional timeline 1918–1922 and Kiyoshi entries | Usable decision record adopted; blocked on Q4 (prose integration) and Q1–Q3 |

## Resume here

CR-041 is adopted as a decision record on `adopt/cr041`; canon's Siberian war prose still stands. Next action: with the author's authorisation (Q4), integrate CR-040 Stages 3–4 and CR-041 together on one branch — apply the Stage 3–4 passages from `review/cr040-stage3-4` with CR-041's supersessions, then `cr_facts.py apply` for both CRs, revise the 12 listed passages, update the ledger (July 1918 treaty, Kazan escrow, oil concessions, the 1919 promise, the 1921 vote), the character files and the fresh-context review. Stale: the Stage 3–4 draft's Ob battle, Omsk's fall, the unilateral 10 September recognition and the torn-treaty mechanism of R10.
