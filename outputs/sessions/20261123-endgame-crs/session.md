---
session: 20261123-endgame-crs
started: 2026-11-23
updated: 2026-11-23
mode: draft
status: paused-for-author
baseline:
  commit: 5b85ce5
independence: same-agent (one writer revised all four drafts; no review was run)
---

# Revise CR-083 to CR-086 so that they build toward the Final Act of Thalassia

## Brief

- **Desired outcome:** the four endgame drafts revised to the fifth version of `book-agent/revision/planning/endgame-suite-allocation.md`, each passing `preflight.py --draft`.
- **Authorization:** the author's handoff note of 23 November 2026 ("Can you execute these instructions please", 19:44) and his answers of 19:55: no newer CR-083 exists; Canada signs Article I; `L1754` is kept; CR-086's title is confirmed; merge PR #87 and run the workflow on this branch. Nothing is approved for integration; `main` was touched only by merging PR #87 at his instruction.

## Author decisions and open choices

| ID | Item | Status |
| --- | --- | --- |
| D1 | No newer CR-083 than revision 7 | decided, 19:55 |
| D2 | Canada signs Article I for itself | decided, 19:55 |
| D3 | `L1754` kept as it is | decided, 19:55 |
| D4 | CR-086's title: "The Final Act of Thalassia: the renunciation and the food order" | decided, 19:55 |
| D5 | PR #87 merged (squash, d0d2c93); the draft workflow runs on this branch | done |
| Q1 | CR-085: `T-M4`, `T-H1`, `T-A1` were marked decided in revision 2 without his words; now shown as recommendations | open |
| Q2 | CR-084: the combined annuity band of 15–20 for Caledonia, the retrenchment and the renunciation | open |
| Q3 | Fresh-context reviews of the four drafts | run at the author's request, 20:11; all four say one more revision |
| Q4 | Whether Australia and New Zealand sign Article I on Canada's footing | open |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `preflight.py --draft` on CR-083, CR-084, CR-085, CR-086 | exit 0 for each (warnings: people not yet in the registry; IDs that sibling drafts introduce) |
| X2 | `cr_facts.py preview CR-086.md` | flags `L1758`, the clause tension 6 cuts |
| X3 | GitHub workflow "Pacifica — preflight CR drafts" on 283782e | success |
| X4 | `tools/session.py end` | canon checks pass |

## Resume here

State on 24 November 2026, after the third revision round (the author's "Please do that", 23 November, 23:36):

- Branch `drafts/cr083-086-endgame`. Nothing is integrated, `main` is untouched, no integration PR is open.
- Revised against the second-round reviews and passing preflight: `CR-083` revision 10, `CR-084` revision 8, `CR-085` revision 5, `CR-086` revision 4. None of these revisions has been reviewed in a fresh context.
- Each draft quotes the items of the author's answer sheet of 23:11 that concern it, and lists at the end of `## Decisions` the review findings it does not yet address.

Questions put to the author and not decided by the drafter:

1. `CR-084` `T-A2`: the cancelled annuities come from the end of the schedule (approved, item 84-8), which gives Britain no yearly relief. Alternative: take the third tranche from the near end.
2. `CR-086` `T-8`: Article II as worded does not forbid what the Realm did in 1919. Alternative: a fourth undertaking against making food or credit conditional on a concession.
3. `CR-086` `T-9`: what Julian does on 1 August (three cases).
4. `CR-083` `T-15`: whether the first wave of compacts is ratified by Proclamation Day or ratifications run on under the standstill rule. Also `T14`, the reading of `L892`.
5. `CR-084` `C3`: who holds the former German Samoa, New Guinea and Nauru after 1919, which decides the annex of existing stations south of 10° S.

Next, when he has answered: apply the answers; a third fresh-context review in merge order (`CR-083` and `CR-084`, then `CR-085`, then `CR-086`); then the workbook tasks and the registry commit. Integration only on his word.
