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

## Open author choices

| ID | Question |
| --- | --- |
| Q1 | CR-060 open decision 14: the drafter suggests the Union's commercial telegraph traffic passes at Salt Lake and Pacifica reads it quietly. |
| Q2 | CR-062 open decision 23: the drafter's suggestion for Sumner's speech. |
| Q3 | CR-065 open decision 16: the drafter suggests the gold premium falls on McClellan's election. |
| Q4 | CR-068: what replaces Victoria's price of November 1864 now that the armistices are executive (suggestion: a pledge to consult the Council). The rows are not rewritten until this is answered. |
| Q5 | The drafter's readings of "Approve" on rows without a recommendation: CR-059 open decisions 27 (yes), 34 (yes) and 49 (all three scenes; P6 stays "never stated"). |

## Checks

| ID | Check | Result |
| --- | --- | --- |
| X1 | `lint_canon.py --only` on CR-059, 060, 062, 063, 064, 065, 068 | clean |
| X2 | `tools/session.py end` | canon lint, CR facts, storyline sync and character docs pass |

## Resume here

- **Waiting on the author:** Q1 to Q5.
- **Then, in order:** (1) rewrite CR-068's pledges of 1864 (its open item 4 lists the rows); (2) carry CR-068's approved changes into CR-059 (Baker, Bush out of 1866, the Port Townsend convention, Lincoln's letter of 1866) and the rest of CR-060 and CR-062; (3) a fresh-context review of the whole set, the first since 8 November; (4) one merged storyline text for §§8–13, since CR-061, CR-063, CR-065 and CR-068 anchor on the same paragraphs and CR-064 and CR-067 insert after the same §9 sentence; (5) approval of the CRs and integration.
- **Not done:** CR-061 and CR-067 were not touched (their decisions were already recorded). CR-067's open decisions 4 to 6 and CR-068's waiting items (A13, the occasions of PP6 and PP8) were not on the sheet.
