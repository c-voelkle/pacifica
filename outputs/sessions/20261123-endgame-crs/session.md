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

Revisions on `drafts/cr083-086-endgame`: CR-083 rev 8, CR-084 rev 6, CR-085 rev 3, CR-086 rev 2. The author decided at 20:11: CR-085's `T-M4`, `T-H1`, `T-A1` approved; the annuity band of 15–20 acceptable pending modelling; Australia and New Zealand sign Article I. Four fresh-context reviews ran in separate agents at his request (`CR-083-review-3.md`, `CR-084-review-3.md`, `CR-085-review-2.md`, `CR-086-review-2.md`); each verdict is "one more revision". They were run at the same time, so the later two read CR-084 before its review's fixes.

Next, in merge order: revise each draft against its review. Shared across the four: (1) one account of the annuity tranche (date, order of votes, who objects) in CR-083, CR-084 and CR-086; (2) one calendar for April to 1 August 1932 (when London sees the article, when Hayama agrees it, promulgated and not ratified on 1 August, the Ottawa conference sitting that day); (3) the legal route for striking the Concord's term, with the Senate; (4) custody of the devices and Japan's place in Article I; (5) every APPROVED or "Decided" label that reaches beyond the author's quoted words, which only the author can settle. No fix has been applied since the reviews.
