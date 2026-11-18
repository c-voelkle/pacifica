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
| Q1 | open choice | B-1, D-1 to D-7, F-1, F-2, G-1, H-1, J-2; CT1–CT3; the Union-side figure for E-4 (Starr King proposed) | outline | open |

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

- Next: confirm Starr King (E-4); the D questions; then draft Part C in full.
- The outline waits for the author's answers to its questions and tensions. Recommended order: C (the aims), then E (California), then D, H, the rest.
- Nothing is integrated; `main` is untouched.
