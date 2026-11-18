---
session: 20261118-cr075-war-aims
started: 2026-11-18
updated: 2026-11-18
mode: draft
status: paused-for-author
baseline:
  commit: bf2d899
independence: same-agent (outline only; no review yet)
---

# What did the Republic go to war for in 1861, and why did California and Hawaii agree?

## Brief

- **Desired outcome:** an outline for CR-075, filled part by part afterwards, as with CR-071.
- **Origin:** CR-068 CT3 ("amend, with reservations"; author, 11 November 2026) and CR-068's open list, item 5: the war aims of 1861 and California's reasons are underdetermined; a new CR is to settle them.
- **Authorization:** author, 18 November 2026, 13:05: "Yes that's a good item. Let's proceed according to the suggested plan" (outline first: the aims, each government's reasons, how they tie to the 1865 terms, the schoolbook formula; then part by part).
- **Branch:** `drafts/cr075-war-aims` from `main` at bf2d899.

## What was done

- `book-agent/revision/CR-075-outline.md`: Parts 0 (canon), A (the gap), B (design rules), C (five aims of 1861), D (Elias's sealed estimate), E (California's own reasons and price), F (Hawaii cross-check), G (aims to peace table), H (schoolbook candidates), I (on the page), J (deferred items it can carry); canon tensions CT1–CT3; fact changes none; research R1–R5.
- `lint_canon.py --only` clean; `cr_facts.py preview`: no fact changes declared.

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | The next CR is the war aims of 1861 and California's reasons; outline first | author, 18 November 2026, 13:05 | current |
| D2 | decision | Add a section on the key players in Pacifica and their agency; answer "how does he know?" alongside the plan, within this CR | author, 18 November 2026, 13:20 | current |
| D3 | decision | C-1 the five aims stand; C-2 preamble public in July 1861; C-3 "on the Pacific slope"; C-4 Burch himself speaks for the expansionists | author, 18 November 2026, 16:19 | current |
| D4 | decision | E-1 the May 1861 note approved; E-2 California's price (a); E-3 a Californian renewal at risk in May 1862; E-4 real historical figures, Burch and one other for the Union side (Starr King proposed); E-5 Beale's public letter used | author, 18 November 2026, 16:19 | current |
| D5 | decision | D-1 to D-7 approved: the closed sitting as a challenge evening; the 21 players (Starr King confirmed for E-4); the new roles for Broderick and the Calculation Office; D7's errors traced as recommended; the fallback in 1861 and 1864; who hears the plan; Sherman first comes in 1853 as a banker | author, 18 November 2026, 16:29 | current |
| D6 | decision | B-1 rules stand; F-1 no new Hawaiian aim; F-2 approved; G-1 table complete; CT1 amend (B); CT2 adapt (A); CT3 amend | author, 18 November 2026, 16:45 | current |
| D7 | decision | J-2 approved: no separate revision of CR-065; impact notes at integration | author, 18 November 2026, 17:11 | current |
| D8 | decision | Part C: C-5 to C-11 approved (preamble text; Pacific slope; east of the mountains; Burch in the Confederal Assembly, Boonslick link; Vallejo on the pledge of 1848; promise to treat in 1861; each resolution names its object) | author, 18 November 2026, 17:26 | current |
| D9 | decision | Part E: E-6 to E-12 approved; Starr King in the pulpit only; San Pasqual used (no conflict) | author, 18 November 2026, 17:43 | current |
| D10 | decision | D-8 to D-13 and F-3 to F-7 approved as recommended | author, 18 November 2026, 19:28 | current |
| D11 | decision | Hawaii's island aim: the first object's island clause, the sealed minute, the chain of 1856–1867 (Parts C, F, G); G-2 decided | author, 18 November 2026, 19:58 | current |
| Q1 | open choice | H-1 (deferred until C–G are drafted) | outline | open |

## Revision of 13:20

- Part D rebuilt: D-a the closed sitting as a challenge evening with Sherman as respondent; D-b fifteen players (P1–P15) with what each knows, their own interest and where they act on their own; D-c the estimate (D1–D7) with a *how does he know* column. B8 added; C7 corrected (the invited guard at Salt Lake, 1862, without a vote); I1 and R6 added. Working copy of Part D: `part-D-draft1.md`.

## Research, 18 November 2026

- 14:15: the author supplied seven texts; plan in `research-plan.md`.
- 14:52: four more (Kuykendall II, Lavender on Ralston, Williams on Broderick, Thompson on Beale); pass 1, the keyword sweep of all eleven, in `research-pass1-sweep.md` (122 queries; reading guide, matrix, clusters, year windows, locations, silences). Texts, extraction and snippets stay outside the repository.
- 15:07: the author said go for pass 2. Close reading done; notes in `research-notes/` (README with findings, four note files). Nothing in the outline changed yet; the findings are proposals.
- 15:20: Johannsen supplied; passes 1 and 2 run on it (the sweep now covers twelve texts; notes in `research-notes/O-oregon.md`).
- 15:24: pass 3 (canon checks) done: `research-pass3-canon-check.md`. No tracked fact contradicted; three wordings to refine (B1–B3); Sherman's 1847–49 Monterey years do not exist in Pacifica (recommended: he first comes in 1853).
- 15:33: author: make the three wording fixes, then write the findings into Parts C–F. Fixes on `housekeeping/cr075-wordings` (from `main`; checks clean; PR to be opened by the author, the CLI is not logged in). Findings written into the outline's Parts C–F and CT2; new questions C-4, D-7, E-5, F-2.
- 15:49: PR #77 (`housekeeping/cr075-wordings`) opened and squash-merged on the author's word (`2f65358`).
- 15:56: pass 6 (page references) done: `research-pass6-citation-check.md`. 258 citations; one spelling corrected; five over-long quotes in the notes paraphrased.

## Resume here

- Part C drafted in full: `book-agent/revision/CR-075-C-aims.md` (preamble draft text, the five objects, the price and the promise to treat, Burch's motion, the rule that each resolution names its object). Open: C-5 to C-11.
- Part C's C-5 to C-11 approved (17:26). Part E drafted in full: `book-agent/revision/CR-075-E-california.md` (Baker's note of May 1861, California's price as an article of the war resolution, Beale's letter to Andrés Pico, Starr King, the renewal of May 1862). Open: E-6 to E-12.
- Part E's E-6 to E-12 approved (17:43; Starr King in the pulpit only); historical facts checked on the web (the treaties of 1852, Starr King's dates, Beale at San Pasqual, the flood of 1862). Part D drafted in full: `book-agent/revision/CR-075-D-plan-and-people.md` (two closed sittings in late June, the estimate part by part, Sherman's case, the errors traced). Open: D-8 to D-13.
- D-8 to D-13 left open by the author (19:13). Part F drafted in full: `book-agent/revision/CR-075-F-hawaii.md` (Victoria's argument, Wyllie's guarantee answered by Vallejo's 1848, the kingdom divided, Hawaii as the keeper of the aims at each renewal). Open: F-3 to F-7, and D-8 to D-13.
- D-8 to D-13 and F-3 to F-7 approved as recommended (19:28): the extra year is an error nobody saw (paper money); Marcus's Casey call reasonable; Ralston's rule recorded in 1861 and applied in 1862; whalers' safe-conduct a CR note only; the Hawaiian press from autumn 1861; Lot's refusal from December 1863. Part G drafted in full: `book-agent/revision/CR-075-G-aims-to-peace.md` (the chain of instruments; the B4 test item by item; the guano islands missed by G-1, G-2; the empty parks paid for, G-3). Open: G-2 to G-6.
- Hawaii's own power (author, 19:47–19:58): the island chain 1856–1867 made explicit (Part F, F5; historical facts checked on the web: Nihoa/Laysan/Lisianski 1857, Johnston 1858, the Honolulu-based guano trade, the *St. Mary's* from Panama, Midway 1859/1867, Palmyra 1859/1862); the first object gains an island clause and Hawaii a sealed minute (Part C, C1.5, C3.1); G-2 decided (Part G). The author's planning note: the hidden aim is Pacific hegemony, not stated in 1861. OPEN: the *Palestine*'s port of departure.
- The promise (author, 20:37): on their honeymoon in November 1858, in the rain, Elias promises Victoria Johnston back; the sealed minute of 1861 is that promise made binding; after the exchange in 1867 the *Kalama* raises the flag on Kalama Island again (Part F, F5.6; Part C, C1.5). The *Palestine* sails from Honolulu (story assumption), with no Pacifican institution involved; a confederal rule of 1859 closes the gap, and Brooks breaks it at Midway.
- Next: the author's answers on G-3 to G-6; then H (the schoolbook formula), I, J, then the fresh-context review.
- The outline waits for the author's answers to its questions and tensions. Recommended order: C (the aims), then E (California), then D, H, the rest.
- Nothing is integrated; `main` is untouched.
