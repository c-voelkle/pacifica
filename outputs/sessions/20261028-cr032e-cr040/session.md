---
session: 20261028-cr032e-cr040
started: 2026-10-28
updated: 2026-10-28
mode: draft
status: paused-for-author
baseline:
  commit: f377d00
independence: separate-agents
---

# Combine CR-032 A and D into one shape, and start a canon CR from it

## Brief

- **Desired outcome:** a revised CR-032 that combines A and D, and the start of a new CR that would bring it into canon.
- **Authorization:** author, 28 October 2026: "a combination of A and D … starts out with Julian's earlier coronation, his Europe tour, and trying to prevent war in Europe … still end up dragging everyone … into World War I, which leads to the Bolshevik Revolution, the Red Terror, and Julian and his Pacifica coalition having to invade and ultimately arrest Lenin, Trotsky, and Stalin. … write up a revised version of CR-032 and start to work out a new CR". Drafting only; no canon edits.
- **Sources of history:** CR-032 (A), CR-032c, CR-032d in `book-agent/revision/alternatives/CR-032/`; canon §§26–32; CR-022, CR-026, CR-039.

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Shape: D's earlier accession and tour, failed July 1914, A's Russian war, Red Terror, arrest of the three leaders | author 2026-10-28 | drafted as CR-032e |
| D2 | decision | The 1904–1905 confrontation with Russia and Kiyoshi's naval battle (as carried in CR-032b from A) belong in CR-040 | author 2026-10-28 | CR-040 revision 3: full Stage 1 passage, indemnity flag, knock-ons, forbidden pattern for "Baltic Fleet"; self-reviewed |
| D3 | decision | R2 renounce; R3 Kahekili c.1916 after daughters; R4 1907; R5 approved in shape; R6, R7 approved; R8 arrested, tried, executed for state crimes; R11 federal Russia; R12 Stalin in Petrograd; R13 Ka Lōkahi keeps ten-year reviews and agrees in 1927 that Japan joins | author 2026-10-28 (second round) | recorded in CR-040 revision 4 |
| D4 | decision | Kiyoshi's death to be defined in this package; not in Siberia | author 2026-10-28 | K1 proposed: Kronstadt, May 1920; Vance holds the Ob |
| D5 | decision | Kiyoshi dies a warrior's death, killing Stalin or on that level; the negotiated surrender was too pacifist | author 2026-10-28 | K1 revision 5: storms the *Petropavlovsk* at Kronstadt, kills Stalin, dies of wounds; R8 for Stalin awaits confirmation |
| D6 | decision | K1 must be realistic and clever: subterfuge or phronesis, then one cut when Stalin lashes out | author 2026-10-28 | K1 revision 6: letters, informant from 1905, interpreter, parley as diversion, public offer, Jigen-ryū cut |
| Q1 | open choice | R1 review findings F1–F7; sharpened R5 text; K1; R8 charges; R12 and R13 mechanisms; R9 Romanovs; R10 Victoria and the Russian war | CR-040 rev 4 | open |

## Outputs

- `book-agent/revision/alternatives/CR-032/CR-032e.md` (scenario) and README row.
- `book-agent/revision/CR-040.md` (canon CR draft: Stage 1 and 2 text drafted, Stages 3 and 4 outlined).

## Handoffs

| ID | To | Task | Output | Status |
| --- | --- | --- | --- | --- |
| H1 | fresh reviewer | Consistency and literary review of both drafts | all findings applied: supersession table, four fact events, fuller impact list, Part VI structure, Silas bargain and motive, Julian's withheld oil sanction, Victoria's act in July 1914, label and history fixes | done |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `cr_facts.py preview CR-040.md` (revision 2, four fact events) | 23 passages in four files; recorded at the end of CR-040 |
| X2 | `lint_canon.py --only` on both drafts | clean |
| X3 | `cr_facts.py preview CR-040.md` (revision 3) | 28 passages in four files, including the five "Baltic Fleet" passages |
| X4 | `cr_facts.py preview` (revision 4) | 33 passages, adding Kiyoshi's death in Siberia; Zimmermann (5 July 1914) and the Gulf ice dates verified; revision 4 self-reviewed |

## Resume here

CR-040 revision 4 records the author's second-round answers. Waiting on: approval of K1 revision 6 (Kiyoshi's stratagem and death at Kronstadt; confirms Stalin is not tried), the sharpened July 1914 text (R5), the F1–F7 fixes, the R13 mechanism, and R9 and R10. Once K1, R5 and F1 are approved, Stages 1 and 2 can be integrated on a branch; Stages 3 and 4 need their storyline text written. Canon is unchanged.
