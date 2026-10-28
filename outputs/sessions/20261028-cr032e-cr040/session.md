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
| Q1 | open choice | R1–R13 of CR-040 (Silas route, heir's birth, accession year, July causes, hostages, arrests, court and sentence, Romanovs, Victoria, federal Russia vs Siberia, Stalin, Ka Lōkahi) | CR-040 | open |

## Outputs

- `book-agent/revision/alternatives/CR-032/CR-032e.md` (scenario) and README row.
- `book-agent/revision/CR-040.md` (canon CR draft: Stage 1 and 2 text drafted, Stages 3 and 4 outlined).

## Handoffs

| ID | To | Task | Output | Status |
| --- | --- | --- | --- | --- |
| H1 | fresh reviewer | Consistency and literary review of both drafts | findings applied where clear | see below |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `cr_facts.py preview CR-040.md` | 1 finding (AGENTS.md accession sentence); storyline forms not matched by the pattern listed by hand |
| X2 | `lint_canon.py --only` on both drafts | clean |

## Resume here

Waiting for the author's answers to CR-040's R-items. Stage 1 (the crown of 1907) needs R2–R4 before integration; Stage 2 (the tour and July 1914) needs R5. Stages 3 and 4 are outlines until R6–R12 are answered. Canon is unchanged.
