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

On `drafts/cr083-086-endgame`: CR-083 rev 9, CR-084 rev 7, CR-085 rev 4, CR-086 rev 3, each revised against its fresh-context review of 23 November (`CR-083-review-3.md`, `CR-084-review-3.md`, `CR-085-review-2.md`, `CR-086-review-2.md`) at the author's instruction of 20:25. All blockers were addressed; each draft lists the review findings not yet addressed at the end of its `## Decisions`. The four now share one calendar (stated in CR-086 `E1`), one account of the annuities (CR-084 `B1`: three dated tranches from the end of the schedule), one rule for the Senate's consent (CR-084 `T-S1`), and one statement of custody (CR-086 `T-5`).

The author answered the approvals list in full at 23:11 and 23:14 (`book-agent/revision/planning/endgame-approvals-to-confirm.md`); all 29 items are approved and recorded in the drafts with his words. Harlan Tate is pegged to a birth about 1866 (PROPOSED). Nothing is approved for integration.

Next: a second fresh-context review of the revised drafts if the author wants one; workbook sizing (the annuity band and its split, Great Bear's tonnage, the wheat contract's band); the review findings each draft lists as not yet addressed; then the author's decision to integrate, in merge order. History was web-checked only in part; several dates are from memory and are marked so.
