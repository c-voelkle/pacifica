---
session: 20261108-cr066-elias-before-california
started: 2026-11-08
updated: 2026-11-08
mode: adopt
status: paused-for-author
baseline:
  commit: 221ed91
independence: separate-agents
---

# Write up Elias's childhood, father, the Colonel and Kit Carson as a CR

## Brief

- **Desired outcome:** a draft CR carrying the 28 October brainstorm ("Elias's life and languages") into canon form, which had never been integrated.
- **Authorization:** author, 8 November 2026: "Yes please write this up as a cr - missouri birth and mother is ok; the colonel's backstory also goes in - as well as what he learns from the guy and the books Elias saves: numa and lycurgus as I recalled it. Carson and his volunteers again cross paths with Elias's men in a fateful way during the Civil War in New Mexico." Earlier, 28 October: the Colonel's river warning is "too on the nose"; the Taos Rebellion is his end and "helps explain Elias' vendetta against the Union"; Elias speaks English, French, Spanish and some Hawaiian. Out of scope: integration into canon.
- **Sources of history:** the 28 October chat; CR-061 (draft, PR #69, commit 4acee99), whose C11 already carries the author's canon that Elias read to Carson as a boy and drafts the 1862–63 crossing.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-10-28 | explore | Author: "Let's continue brainstorming for now" |
| 2026-11-08 | draft | Author: "write this up as a cr" |
| 2026-11-08 | adopt | Author: "Reuben is the right name. The changes to cr-061 are approved. Elias does not choose the crossing place. If there's nothing else open, go ahead and integrate it." |

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Missouri birth; Anglo mother (not the Nuevomexicana alternative) | author 2026-11-08 | current |
| D2 | decision | The Colonel's backstory, what Elias learns from him, and the volume with Lycurgus and Numa go in | author 2026-11-08 | current |
| D3 | decision | The Colonel dies in the Taos Rebellion; it feeds Elias's enmity to the Union; no on-the-nose river warning | author 2026-10-28 | current |
| D4 | decision | Carson and his volunteers cross Elias's men fatefully in New Mexico in the Civil War | author 2026-11-08 | current (realised through CR-061 C11 plus CR-066 EB-22–25) |
| Q1 | open choice | Father's name: Reuben (recommended) or Silas (CT1) | CR-066 | open |
| Q2 | open choice | CR-066 open decisions 2–12 | CR-066 | open |

## Handoffs

| ID | To | Task | Inputs | Withheld for independence | Output | Status |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | fresh-context reviewer | consistency, history, literary effect | CR-066, AGENTS.md, canon §§1–4, §10 excerpt, bible entries, CR-061 draft | the brainstorm chat, this record | 4 blockers, 13 should-fix, 6 consider; applied (CR-066 Review section) | done |

## Checks

- X1 `cr_facts.py preview` and `--tensions`: clean except CT1's expected AGENTS.md hit.
- X2 `lint_canon.py --only CR-066.md`: clean (before and after the review fixes).
- X3 Interface with CR-061 (PR #69): CT4 asks C11 for "the boy who read to him by the fire" and a November 1862 resignation.

## Resume here

- CR-066 Parts A–D integrated and merged to main (#71); Part E (Taos, December 1862) waits for CR-061 and is written into its §10 text at CR-061's integration, with the `taos-1847-amnesty` event and the compact's ledger article.
- CR-061 draft (PR #69) carries the approved CT4 changes: "the boy who read to him by the fire", resignation November 1862; its registry note should use CT-KIT-CARSON.
- Still OPEN: the mother's and the Colonel's names; the Bible's rescue (Missouri exemption law).
