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

State on 24 November 2026, after integration stage 2 (this block supersedes the ones below):

- The author approved all five CRs at 13:08 ("All the CRs are approved and can be integrated."), chose one integration branch and one pull request (13:15) and parallel writers with reconciliation (13:37).
- Branch `integrate/cr083-087-endgame`, cut from `drafts/cr083-086-endgame`. Commit `83e27fa` integrates CR-083 to CR-087 in one pass: the four writers' storyline edits were merged paragraph by paragraph, so there is no commit per CR. `main` is untouched until the pull request is merged.
- Done: storyline (sections 8 to 37, the overview lines and closing items 39 to 42); five register entries with facts applied; ledger (24 new parties, 32 new commitments, 46 amended, plus the Lewis crest on `C-1867-WESTERN-LINE`); 28 new people in the registry and bible (390), notes on existing people in the bible's CR-083 to CR-087 section; historical background; AGENTS.md; amendment notes on `CR-054.md`, `CR-058.md`, `CR-070.md`, `CR-082.md` and their register entries. `preflight.py --integration`: 7 of 7.
- Not done, and listed in the drafts and writers' notes: the finance, energy and population workbooks for the new figures (annuity tranches, the yen, the stations, Hokkaido, the prairie contract); the decision records CR-084 lists for annotation (`CR-019`, `CR-021`, `CR-022`, `CR-029`, `CR-040`, `CR-052`, `CR-053`, `CR-057`, `CR-074`, `CR-077`, `CR-081`); sources still "from memory" in the historical background.
- Next: apply the fresh-context review of the integrated prose (`/tmp/work/integ/integration-review.md`, to be copied into `book-agent/revision/CR-083-087-integration-review.md`), then open the pull request to `main`.

State on 24 November 2026, after the fifth revision round (the author's answers of 08:22):

- Branch `drafts/cr083-086-endgame`. Nothing is integrated, `main` is untouched, no integration PR is open.
- Current revisions, all passing preflight: `CR-083` 16, `CR-084` 15, `CR-085` 12, `CR-086` 10, `CR-087` 6. The fifth-round reviews, of earlier revisions, are `CR-083-review-7.md`, `CR-084-review-7.md`, `CR-085-review-6.md`, `CR-086-review-6.md` and `CR-087-review-2.md`; every verdict is "one more revision", and none of their findings is applied yet. The finding common to three of them is the calendar of July 1932: what the Emperor ratifies about 16 July, what is signed after it, and when the chambers and delegations vote.
- Decided on 24 November: 00:12 (Inukai, Hayama 12–15 June, the union without term, consecutive years, the split 2/4/11, wheat at 1.0 million tonnes, the third refusal); 07:19 (the Lewis crest, road surveys only, `CR-087`); 07:27 (the yards' share below capital ships, the Columbia half in power, the drafter's additions of the should-fix round); 07:31 and 07:37 (Kaʻiulani as common Foreign minister, signing seated, nothing said of 1919); 08:22 (the crest line confirmed knowing the map; the Emperor signs in mid-July on one advice; Proclamation after the annuity bill; London notices and accepts what the retrenchment is paid in).
- Added to `CR-083` after revision 13 and not reviewed: the King's representative at Victoria from January to July, and the vote of 16 April on final terms published about 25 March (author, 08:58); the Governor is John Buchan, appointed 1930 in this timeline (author, 09:02; the year is PROPOSED).
- The county map is redrawn on this branch for `CR-087` (revision 3; author, 09:10): `population/data/counties/lewis_crest_strip.geojson` is taken off Missoula in `population/draw_map_1887.py`. Run it with the atlas's `output` folder as its argument.
- `CR-083-086-calendar.md` (author, 10:10: "I approve A-K with Victoria in the final scene.") is the one calendar for April to autumn 1932. Its eleven decisions are applied to `CR-083` to `CR-086` and close the calendar findings of the fifth reviews. The author's answers of 10:45 on `CR-083-087-remaining-proposal.md` (sent in the second assistant's wording, and quoted in each draft as sent) are applied too: Buchan in February and his appointment, citizenship and the vote in Caledonia, the quota's default, Kiyoshi's son as Navy minister from July, the British committee, "in peace", Chiyo, the Emperor's reason, and the reason for the Lewis crest (`CR-087` revision 4). Still to do, none of it needing a decision: body labels brought into line with the decision rows, drafting notes out of the bodies, Kaʻiulani's set piece in London, registry entries for Mori Kaku and Hiranuma, the older prose in `CR-084` and `CR-085`, the reviews' minor items; then one narrow fresh-context review. Done since: labels, drafting notes, minor items and registry (revisions 14, 12, 9, 8 and 4), and the narrow review in two files, `CR-083-086-calendar-review.md` and `CR-083-087-labels-review.md`. The author answered their five questions at 11:21 (the exchange on 1 August; the guarantee signed at Victoria on Proclamation Day, in effect on signature, on full powers carrying Tokyo's mandate; Tate's cap as a condition of the Senate's consent; the yards' share fixed to 1942; London's Chiefs of Staff told in late July of the Act) and their findings are applied: `CR-083` 15, `CR-084` 13, `CR-085` 10, `CR-086` 9, `CR-087` 5. Since then the drafting notes were swept and the older prose of `CR-084` (`B2` to `B4`, `C1`; revision 14) and `CR-085` (`A7`, `B1`, `C1`, `C2`, Part D; revision 11) restyled, with a before-and-after content check by a separate reader (`CR-084-085-prose-check.md`) whose findings are applied. The final whole reviews of 24 November (`CR-083-review-8.md`, `CR-084-review-8.md`, `CR-085-review-7.md`, `CR-086-review-7.md`, `CR-087-review-3.md`) say: `CR-087` ready for approval; the other four ready once their blockers are fixed (five blockers in all, each a term stated two ways). The author answered at 12:06 and the final pass is applied: `CR-083` 16, `CR-084` 15, `CR-085` 12, `CR-086` 10, `CR-087` 6, all passing preflight. Each draft's last decision row says which of the final review's items were not done (minor items; in `CR-085` the impact notes for the decisions of 24 November; in `CR-086` the question whether Belgium accedes). At 13:08 the author approved all five for integration ("All the CRs are approved and can be integrated"), approved `CR-087`'s phrase for the peace of 1865, and left Belgium's accession to a future Postwar Europe CR; `CR-085`'s impact notes and calendar now carry the decisions of 24 November. Revisions as approved: `CR-083` 16, `CR-084` 15, `CR-085` 13, `CR-086` 11, `CR-087` 7. Integration began at 13:15 on the author's word "one" (one branch, one pull request for all five): branch `integrate/cr083-087-endgame`, cut from the drafts branch. Stage 1 is committed: section 36 of the storyline carries `CR-085`'s May to July 1932 (the renewal to 1937 is replaced), and `L629` and `L632` carry `CR-087`. Still to do, in order: section 37 (`CR-083`'s 1932, `CR-084`, `CR-086`, the Final Act and the last image); the earlier storyline passages each draft lists under its impact notes; the register entries with their fact changes and `cr_facts.py apply`; the ledger; the registry and character bible; `AGENTS.md`; `preflight.py --integration`; a fresh review of the integrated prose; the pull request. No register entry exists yet, so the canon checks pass only because nothing has been declared. 
- Each draft lists at the end of `## Decisions` what the fifth round did and did not do with the fourth review's findings.
- Models (`finance/CR-083-086-workbook.md`): Story 0 failed checks, Stress 51. The memo row E263 names France among the stabilization credits and is to be corrected at the next rebuild.

Not done:
- Registry entries and fact changes for Mori Kaku and Hiranuma Kiichirō (`CR-085`).
- The older prose of `CR-084` `B2` to `B4` and `C1` and of `CR-085` Parts B to D; the reviews' Minor items.
- `AGENTS.md`'s paragraph on the financial files; that belongs to integration.

Next: the map redraw for `CR-087` if the author wants it; a fifth fresh-context review; then the registry commit and integration on his word.
