---
session: 20261112-decision-sheet
started: 2026-11-11
updated: 2026-11-12
mode: draft
status: paused-for-author
baseline:
  commit: ae834bb
independence: same-agent (drafter and reviewer combined; the CR-065 revision is self-reviewed)
---

# Are the unintegrated CRs on `revision/cr059-oregon` ready to be integrated together, and what still has to be decided?

## Brief

- **Desired outcome:** the outstanding recommendations of CR-059, CR-060 and CR-062 to CR-065 decided in one pass, and written into the drafts.
- **Authorization (author, 11–12 November 2026):** asked for a decision sheet ("Yes please"); answered it in the sheet and in chat; approved writing the decisions into the six drafts and the drafter's revision of CR-065 (sheet row 65-REV, "Approve").
- **Out of scope:** approval of any CR as a whole; integration; the carry-over of CR-068 into CR-059, CR-060 and CR-062 beyond the rows named below.

## Finding of 11 November

The set was not ready to integrate together: six drafts unapproved with about fifty canon tensions undecided; CR-068's approved changes not carried into the older drafts; and the storyline text of the drafts written separately for the same paragraphs of §§8–13. Tooling was clean (lint, fact previews, sync, character docs).

## The decision sheet

A Claude Sheets artifact, "Pacifica — decision sheet, CR-059 to CR-065" (private to the author), 166 rows: 19 that only the author could answer, 104 with a recommendation, 9 already decided in CR-061, CR-067 or CR-068, and 34 details that stay OPEN or MODEL. Shared questions were merged into eleven rows (SET-1 to SET-11).

## Author decisions (12 November 2026)

Each draft carries its own list under "Author's decisions of 12 November 2026" and a decision line on each canon tension and open decision. In summary:

| ID | Decision |
| --- | --- |
| D1 | Every recommendation approved except the rows below (114 approvals). |
| D2 | CR-059 CT6: no objection from Victoria to the exclusion clause ("that would read as hypocritical"). |
| D3 | CR-059 CT12: no protest from the Chinese merchants over the Siskiyou bid. |
| D4 | CR-059: W11 dropped; Thayer cut from the scene. |
| D5 | CR-060 A4: southwest Wyoming's residents are attached to Deseret's charter. |
| D6 | CR-062 A1: the armistices stay plain executive conventions; CR-068 changes. |
| D7 | CR-062 L2: option (a), with the draft's names. A5: Logan refuses for a better offer from the Gulf's merchants, its nature to be decided. |
| D8 | Deseret (association 1862, accession 1867) and the new members' representation: amend, as recommended. |
| D9 | Deferred: CR-060 CT7 (the Legion's pay and the Black Hawk War); which set of Vicksburg numbers; CR-059 open decision 17; CR-062 M3 (needs modelling). |
| D10 | Left to the drafter ("I don't care"): CR-059 open decision 11, CR-065 L8 (Chase, included), CR-062 L1. |

## Decisions of the evening of 12 November 2026

| ID | Decision |
| --- | --- |
| D11 | Victoria's price at the blind vote of November 1864 is the end of the renewals: no renewal of the Protectorship after the war, and what follows made by constitutional amendment, ratified by both founding states, with Hawaii's institutions protected ("Yes this works"). She names the form and no office; the life term is Elias's move in 1865. Written into CR-068 as revision 25, which also drops Elias's pledge to lay an armistice before the Assembly. |
| D12 | CR-060 open decision 14: the Union's commercial telegraph traffic passes at Salt Lake and Pacifica reads it quietly. |
| D13 | CR-062 open decision 23 (Sumner denounces the clause and speaks for the treaty) and CR-065 open decision 16 (the gold premium falls on McClellan's election): approved as suggested. |
| D14 | The drafter's readings of CR-059 open decisions 27, 34 and 49 are confirmed. |

## Checks

| ID | Check | Result |
| --- | --- | --- |
| X1 | `lint_canon.py --only` on CR-059, 060, 062, 063, 064, 065, 068 | clean |
| X2 | `tools/session.py end` | canon lint, CR facts, storyline sync and character docs pass |

## Resume here

- **Waiting on the author:** nothing from this session. Still deferred: CR-060 CT7, the Vicksburg numbers, CR-059 open decision 17, CR-062 M3.
- **Done on 12 November (all self-reviewed):** CR-068's pledges of 1864 rewritten (revision 25); CR-068's approved changes written into CR-059 (W11a the Port Townsend convention, W15 the state of war and the staged force, Lincoln's letter of 1866 in V11, Bush out of 1866, the third reason in "Why Elias takes the risk"), CR-060 (the Terms of Monterey and their first reservation in C2, C4, C5 and the Washoe storyline sentence) and CR-062 (T2 and T10 inside the Terms; Lincoln's letter of 1867 in S8 and the §12 text).
- **Next, in order:** (1) a fresh-context review of the whole set (CR-059 to CR-065, CR-067, CR-068), the first since 8 November, with this session's self-reviewed edits named to the reviewer; (2) one merged storyline text for §§8–13, since CR-061, CR-063, CR-065 and CR-068 anchor on the same paragraphs and CR-064 and CR-067 insert after the same §9 sentence; (3) approval of the CRs and integration.
- **Left for those steps:** CR-068's CT26 and CT28 reword CR-063 CT5's "credit (in London)"; whether the Senate follows Lincoln's advice on the Treasury loan goes with CR-062 M3; CR-059's new scene for Lincoln's letter is listed last and belongs early in the campaign.
- **Not done:** CR-061 and CR-067 were not touched (their decisions were already recorded). CR-067's open decisions 4 to 6 and CR-068's waiting items (A13, the occasions of PP6 and PP8) were not on the sheet.
