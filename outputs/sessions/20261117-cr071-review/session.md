---
session: 20261117-cr071-review
started: 2026-11-17
updated: 2026-11-17
mode: review
status: done
baseline:
  commit: 586ca26
independence: two fresh-context reviewers given only candidate text, affected canon on main, the CR's canon tensions and AGENTS.md. The first reviewed the CR-071 drafts against main; the second reviewed a scratch integration of draft 2. The revision itself is by the drafter.
---

# CR-071 reviewed against `main` after CR-072 and CR-073

## Brief

- **Author, 17 November 2026, 21:51:** "Can you do a fresh context review of CR-071 and see if it's ready to be integrated?" (after integrating CR-072 and CR-073, #74).
- **Author, 23:03:** "Yes sherman should chair it, that is my decision" (E-12 confirmed); asked what to do about the blockers.
- **Author, 23:07:** "Yes apply with the should fix and other small fixes please".

## What was done

- **Review.** Fresh-context review of the CR-071 storyline, ledger, registry and facts drafts against `main` at 586ca26. It found four blockers, eleven should-fix items and several minor ones (`book-agent/revision/CR-071-review-on-main.md`), plus the drafter's mechanical checks.
- **Merge.** `main` merged into `drafts/cr071-073-counties`; CR-072 and CR-073 take `main`'s integrated documents.
- **Drafts revised.**
  - `CR-071-storyline.md` draft 2: eleven rewordings, two moved canon paragraphs and twenty-nine new paragraphs, anchored to `main`.
  - `CR-071-ledger.md` draft 2: verbatim quotes, statuses by label, the Baja/Guaymas split, four new entries, the T3 carry-over, and the quote changes caused by R1.
  - `CR-071-registry.md` draft 2: Sherman, Silas, Davidson, Manuel Chaves, Hikozō, Judah and Cannon amendments.
  - Part E: E-12 confirmed; E-16's mechanism amended so that the Superintendency commissions the survey, as CR-057 requires.
  - Outline: the "Before integration" items updated.
- **Scratch integration** (in `/tmp`, not committed). The storyline text was applied to a copy of `main`'s storyline and section A and the quote changes to a copy of the ledger. `lint_canon.py` was clean; `ledger.py check` reported 288 commitments and one expected problem (C-1867-BAJA's status, which section B sets).
- **Second fresh-context check** of the scratch integration's sections 5, 12–14, 19 and 21–25: see the review file.

## Checks at the end

- `lint_canon.py --only` on the twelve CR-071 files is clean. `cr_facts.py preview` on the outline finds the one expected passage (§12 l. 572). The canon checks on the branch are unchanged.

## Resume here

- CR-071 is ready for integration on `main` in the K-1 order, once the author says to integrate.
- Integration follows each draft's "At integration" sections:
  1. the storyline text, then `sync_master_storyline.py`;
  2. the register entry with the outline's fact changes, then `cr_facts.py apply CR-071` (the `add_person` facts go with the registry entries);
  3. the ledger's A and B, then `ledger.py check`;
  4. the registry and bible, then `validate_character_docs.py`;
  5. `historical_background.md`, CR-021.md's R1 items 8–13, and AGENTS.md (Sherman's line, the "Current canon" paragraph, the identity count).
- The scratch script that applied the storyline text (`/tmp/sim/apply.py`) is not in the repo. The integration should apply the same operations by hand or re-create the script.
