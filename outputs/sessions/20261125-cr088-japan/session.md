---
session: 20261125-cr088-japan
started: 2026-11-25
updated: 2026-11-27
mode: draft
status: paused-for-author
baseline:
  commit: 5d281dc
independence: fresh-context review of revision 15 by a separate agent (27 November 2026; report `review-rev15.md`); the revisions were written in one context
---

# CR-088: review, plan and revisions toward a draft ready for fresh-context review

## Brief

- **Desired outcome:** `CR-088` brought up to par by the plan of 25 November 2026, 14:36 (seventeen steps in six phases), then a fresh-context review.
- **Authorization:** the author agreed the review's findings and asked for the plan (14:36), then for the mechanical cleanup, the check against `CR-089`, the heading structure and the hand-offs (14:42), the cast and the `CR-089` one-line fix (14:59), and the research steps (15:13). Nothing is approved for integration.

## Author decisions

| ID | Item | Status |
| --- | --- | --- |
| D-17 | The cast (`A7`): five new registered persons, five historical figures in the background | approved, 14:59 |
| D-18 | The Treaty of Edo's sunset is a fixed date in 1870 | approved, 15:13 ("1. a") |
| D-19 | Mixed panels under a Japanese president, 1858–70; the contrast with consular courts explained (`T-EDO-1` Case B) | approved, 15:13 ("2. b - but the sharp contrast needs some explanation") |
| D-20 | The convention of 1881 is Hawaii's own | approved, 15:13 ("3. a") |
| D-21 | Kalākaua's marriage proposal kept as his own initiative | approved, 15:13 ("4. a") |
| D-22 | The 1927 rescue figure as the workbook's, MODEL | approved, 15:13 ("5. agreed") |
| D-23 | Chichibu a bather, no title; patron OPEN | approved, 15:13 ("6. agreed") |
| D-24 | The grievance catalogue as the basis of `A5` | approved, 16:01 ("I approve of the grievances") |
| D-25 | Nitobe Inazō: a rigorous scholar at a Polytechnic challenge evening, about 1900 (`A2.5`); registered | approved, 16:32 ("I approve Nitobe as described") |
| D-26 | Konoe's essay of 1918 as a background voice | approved, 16:32 |
| D-27 | The Marshalls to Japan (`A2.6`): the 1885 gap, 1914, three conditions at The Hague, Nauru carved out | approved, 17:03 |
| D-28 | `A5` rebuilt as the catalogue (step 11) | approved, 18:16 |
| D-29 | Motives in capability terms (step 12) | approved, 18:16 |
| D-30 | The agon in `A3` (step 13) | approved, 17:53 |
| D-31 | Shinto (`A4.5`), the shrine question G29 | approved, 17:53 |
| D-32 | San Francisco's six layers and the engineers' school | approved, 18:16 |
| D-33 | Where the bath takes root | approved, 18:16 |
| D-34 | The Calculated (Keisan-ha), origin, Ammann registered | approved, 18:25 |
| D-35 | Shōkin-jan rebuilt on riichi.wiki's standard rules; choices S1–S10 | superseded by D-36 where it differs |
| D-36 | Shōkin-jan's agreed rules (rule revisions 12–14 and the last pass), `Appendix A` rewritten whole; choices S1–S27; revision 13 adds S28, S29 and the Maturity Draw (S17) | approved as design, 25 Nov 19:41–23:44, 26 Nov 00:14 and 27 Nov 06:30; numbers PROPOSED until play-tested |

## What was done

- Revision 4: `main` (#89, #90) merged into `draft/cr-088`; citations re-pointed; one `## A. The change` with `A1`–`A6`; `T-A1` renamed `T-AINU-1`; `## Interface with CR-089` and `## Hand-offs`; `A2.1` item 4 corrected to `L1220`; cast `A7`.
- `draft/cr-089`: the standalone-merge line points at `CR-088` (commit 2fa17ac); its cast question is struck from OPEN.
- Revision 5: D-17 to D-23 written in; the corrections on `book-agent/revision/CR-088-decisions-rev5.md` made; `T-EDO-1` added; the Perry pattern now catches `L300`. Preflight 0 errors (warnings: five new persons awaiting registry entries at integration; `CR-089` not yet on `main`).
- Research, steps 8 and 9: `research-grievances.md` (twenty-eight grievances, our timeline's humiliations set beside canon, sources) and `research-gains.md` (the ledger of Japan's gains with a Japanese actor for each, the opponents, sources).

- Fresh-context review of revision 15 (27 November): not ready, four blockers, fifteen should-fix, about twenty-five nits (`review-rev15.md`). Author's decisions, 07:29: Kalākaua Case A (canon's Oceanian union and Prince Komatsu kept); the side-payment and shortfall rules as he stated them; Chico in Three Forks County; the rest of the fixes as recommended (D-37).
- Second fresh-context review of revision 16 (27 November): close, not ready; five blockers, fifteen should-fix, about twenty nits; the three worked hands all settle (`review-rev16.md`). Author, 08:53: the recommendations approved, plus the teller's queue for the Bank Run; 09:19: the moratorium on frozen claims and the rule on totals (D-38).
- Revision 17 (27 November): the second round applied. Preflight 0 errors.
- Review of Appendix A alone (27 November, `review-appendix-rev17.md`): close, not playable yet; seven blockers, ten should-fix, two balance problems. Author, 10:57: the mechanical fixes as he worded them, and the balance fixes as revised in his note (paying capacity for a Renewal, half a rescued bank's Gold to its claims, Clearing notes as deposits, settlement in Gold only) (D-39).
- Revision 18 (27 November): the Appendix review's round applied. Preflight 0 errors.
- Revision 16 (27 November): the review's round applied: every blocker, should-fix item and nit. Preflight 0 errors.
- Revision 15 (27 November, 06:41): `T-AINU-1` Case B decided by the author ("Move them in now"); its two fact changes moved into `## Fact changes` (D-7). `preflight.py` fixed to read the registry's `people` (separate commit, with a regression test); its registry warnings now name only the seven persons to be registered. Preflight 0 errors; unit tests pass.
- Revision 14 (27 November, step 16): bookkeeping brought in line with revisions 4–13: impact notes (the preview's one tracked passage, `L300`; Chichibu, the skyline, Shōkin-jan's home, Hawaii's convention), the interface re-checked against `CR-089` revision 10 (no overlap), the ledger (`C-1858-EDO`, `C-1870-JP-ALLIANCE`, `C-1881-TOKYO-EMIGRATION` now `HI`–`JP` only, `C-1906-SEISMIC-CODE`), registry notes for Peirce, Kiyoshi and Kaʻiulani, D-2, D-13, D-14 and D-15 marked superseded where later decisions replaced them, sources extended and four links repaired. Preflight 0 errors; its eight registry warnings are false (preflight reads `characters`, the registry's key is `people`).
- Revision 13 (27 November, 06:30): the Category Knife (S28), the Maturity Draw on a taken Renewal, valued as a ron (S17), the contested Window in turn order (S29); A.10 notes, `A3.6`, the 1928 set piece and D-36 follow. The pasted rule revision 15 was folded in as deltas only, since it was written from the revision 14 note. Preflight 0 errors.
- Revision 12 (26 November, 00:14): `Appendix A` rewritten whole on the agreed Shōkin-jan rules (working note `claude/CR-088-shokin-jan-rev14.md` in the Pacifica project, plus the last pass: the three A.8 polishes, temporary furiten in grace, Renewal doubling only the showdown, Paper Riichi a yaku, S27 printing under the Leash allowed); `A3.6`'s summary, the 1928 set piece and D-36 follow. Preflight 0 errors.
- Revision 6 (step 10): `A2` rebuilt around Japan's own interest (`A2.1`–`A2.4`), Nitobe as `A2.5`; D-3 restated, D-24, D-25. Preflight 0 errors.

## Resume here

- Revision 7: D-25–D-27 written in; `A2.6` the Marshalls; step 11 done: `A5` rebuilt (catalogue G1–G28 in the CR's own numbering, `A5.6`–`A5.12`, boundaries); `A6.4` the key Kiyotada does not hold. Preflight 0 errors.
- Revision 8 (step 12): `A1.2` each article with what the Republic gains by giving it; `A1.3` the alliance as a trade; the Realm's reasons in `A4.2` and `A5.1`. Preflight 0 errors.
- Revision 9 (step 13): rivals and losers in every strand of `A3`, the music corrected, the brochure line made checkable; Shinto as `A4.5` with G29. Preflight 0 errors.
- Revision 10: `A3.3` the six layers, the skyline as a geological map, the engineers' school; `A3.4` the bath by place (nine cases). Preflight 0 errors.
- Revision 11: the Calculated in `A3.3`, Ammann registered; `Appendix A` rebuilt (A.1–A.10), riichi by about 1926 in `A3.6`. Preflight 0 errors.
- Revision 12: Shōkin-jan's `Appendix A` rewritten whole on the agreed rules (D-36, S1–S27). Preflight 0 errors.
- Revision 13: the Category Knife, the Maturity Draw and the contested Window (S28, S17, S29). Preflight 0 errors.
- Revision 14: step 16 done (bookkeeping). Preflight 0 errors.
- Open for the author: the settings still marked Proposed in A.9 (S1–S3, S5, S8–S10, S14, the scale of S19).
- Revision 15: `T-AINU-1` decided, facts moved; preflight's registry check fixed.
- Revision 16: the fresh-context review's round applied (D-37). Preflight 0 errors.
- Revision 17: the second review's round, the teller's queue and the moratorium (D-38). Preflight 0 errors.
- Revision 18: the Appendix review's round (D-39). Preflight 0 errors.
- Revision 20 (27 November, 13:37): S4, S31 and S32 approved; S32 extended to the whole Paper Riichi, closed kans included (D-41). Still Proposed: S14 and the S19 scale.
- Revision 19 (27 November, 12:30): the author approves S1–S3, S5 and S8–S10 (D-40); S14 and the S19 scale stay Proposed for play-testing; S4's core and S31–S32 await his placement.
- Next: the author's approval of CR-088. Still marked Proposed: Shōkin-jan settings S1–S3, S5, S8–S10, S14, the S19 scale, S31, S32.
