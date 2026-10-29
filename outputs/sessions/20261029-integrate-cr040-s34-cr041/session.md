---
session: 20261029-integrate-cr040-s34-cr041
started: 2026-10-29
updated: 2026-10-29
mode: adopt
status: active
baseline:
  commit: 1d4ae02
  files:
    book-agent/revision/master_storyline.md: sha256:525dbd45a00d6b041d181ab0b830196dd14b62be75e4eadf9ef1bebee4af0c07
    book-agent/revision/change_requests.json: sha256:de8e1047512ba871525f98850cc6240059b22d793ef8d99efba74372b20281be
independence: separate-agents (integration by one agent; the fresh-context review by a second agent given only the candidate §31–§32, the neighbouring canon §28–§30 and §33–§37, and AGENTS.md)
---

# Integrate CR-040 Stages 3–4 and CR-041 into the master storyline together

## Brief

- **Desired outcome:** the Russian war of 1918–1922 written into `master_storyline.md` as a record of the alternate-historical facts, with the ledger, facts file, character files and background updated, so that a new beats.json can later be generated from it.
- **Objective:** the approved sequence (CR-040 R6–R11, K1; CR-041 S1–S9, N1–N16) embodied as what happens, with labels preserved.
- **Authorization:** author, 29 October 2026: "I would say go ahead and integrate. We leave the Ukraine and other open sectors for a follow-up CR." Also: "the master_storyline file is not actually the 'book' but only an outline … a meticulous record of the alternate-historical facts and not as the actual novel."
- **Sources of history:** `CR-040.md` (R6–R13, K1), the Stage 3–4 draft on `review/cr040-stage3-4`, `CR-041.md`, the session record `20261029-cr041-plan-c`.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-10-29 | adopt | Author: "go ahead and integrate" |

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Integrate CR-040 Stages 3–4 and CR-041 together now | author 2026-10-29 | current |
| D2 | decision | Ukraine, Bessarabia and the Turkish frontier go to a follow-up CR | author 2026-10-29 | current |
| D3 | decision | The master storyline is the factual outline for a future beats.json, not the novel | author 2026-10-29 | current (recorded in AGENTS.md) |
| Q1 | open choice | Which Ukraine, the Black Sea coast, Bessarabia, Kars–Ardahan–Batum | carried from CR-041 | open |
| Q2 | open choice | The hostages' names; the Kotelnich commander; Lenin's capture day; Kiyoshi's sword and poem; who attends the Romanov burial; monarchy or republic | carried from CR-040/041 | open |

## Handoffs

| ID | To | Task | Inputs (paths and IDs) | Withheld for independence | Output | Status |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | Fresh reviewer (separate agent) | Consistency, literary and plausibility review of §31–§32 | candidate §31–§32; canon §28–§30 and §33–§37; AGENTS.md | CR files, drafts, the integrator's notes | findings F1–Fn below | see Review judgments |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `tools/session.py start --topic integrate` | pass |
| X2 | `cr_facts.py apply CR-041` (4 forbidden patterns, incl. CR-040's deferred Kiyoshi pattern) | applied; all listed passages revised |
| X3 | `lint_canon.py` | clean, 4 files |
| X4 | `cr_facts.py check` | pass (13 approved fact changes) |
| X5 | `sync_master_storyline.py --write` / `--check` | pass |
| X6 | `validate_character_docs.py` | pass (171 dossiers: 3 updated, 9 new historical persons) |
| X7 | `commitments/ledger.py check` | 174 commitments, 0 problems (3 new: C-1918-SIB-TREATY, C-1918-EMBA, C-1919-WRANGEL-VOTE; 8 revised) |
| X8 | revision and commitments unit tests | OK |
| X9 | `lint_canon.py --only` on the candidate before review | clean |

## Review judgments

(filled after H1)

## Round log and stop reason

| Round | Date | What changed | Stop reason |
| --- | --- | --- | --- |
| 1 | 2026-10-29 | §31 rewritten and §32 revised under CR-040 Stages 3–4 + CR-041; §25, §28, §30, §33, §35, §37, trajectories and unresolved item 23 from the review branch; register, facts, ledger, characters, background, AGENTS.md | awaiting H1 |

## Resume here

Integration complete on `integrate/cr040-stage3-4-cr041` pending the fresh-context review's findings and the merge. Next: the follow-up CR for Ukraine and the southern sectors (Q1); then the OPEN character details (Q2). Stale: everything in the Stage 3–4 draft that CR-041 superseded (Ob battle, Omsk's fall, unilateral recognition, torn treaty).
