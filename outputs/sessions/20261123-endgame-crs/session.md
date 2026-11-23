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

State on 24 November 2026, after the third review round and the model rebuild (the author's message of 23 November, 23:52):

- Branch `drafts/cr083-086-endgame`. Nothing is integrated, `main` is untouched, no integration PR is open.
- The author's six answers of 23:52 are applied: `CR-084` `T-A2` Case B; `CR-086` `T-8` Case B and `T-9` Case B; `CR-083` `T14` and `T15` Case B; the former German Samoa, New Guinea and Nauru are Pacifica's.
- Third-round reviews: `CR-083-review-5.md`, `CR-084-review-5.md`, `CR-085-review-4.md`, `CR-086-review-4.md`. Every verdict is "one more revision". No finding has been applied except one plain error of fact in `CR-084` (Rabaul and Nauru lie north of 10° S).
- Models rebuilt on this branch (`finance/CR-083-086-workbook.md`): `finance/build/cr083_086_endgame.py` is the chain's new last step; the provisioning model has lost the northern water and sizes the prairie contract. Story 0 failed checks, Stress 51. `AGENTS.md`'s paragraph on the financial files is not yet updated; that belongs to integration.

Blockers from the third round, by draft:
- `CR-083`: the refusal over Caledonia is Julian's third by `L1593`, not his second; Caledonia's tranche comes from the far end and relieves nothing, against "the Exchequer needs relief"; the admission clause's rule for a failed year departs from the Gulf's twenty-five consecutive years with no tension listed.
- `CR-084`: Britain decides without asking who else signs, while France reserves; the deadline of 30 June has no force once the April accord carries the suspension.
- `CR-085`: which cabinet makes the offer after 15 May; nobody who can bind Japan is at the Hayama table; what exactly has no term, the union or the executive trust.
- `CR-086`: Article II is both the cabinet's proposal of the winter and the sufficers' condition of July; Julian's "only signature" against "both crowns ratify that day", and who acts for Japan's crown; labels APPROVED in the table and PROPOSED in the body.

Model findings for the author: 17 annuities are 31% of Britain's book only because the third tranche is near-end; the signature tranche is $262m of $375m; the split 5/6/6 and the contract's 1.5 million tonnes are the drafter's proposals; at that size the board's wheat is half of the Realm's own sales abroad.

Next: the author's word on a fourth revision round and on the proposed sizes.
