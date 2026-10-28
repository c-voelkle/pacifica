---
session: 20261028-cr039-ledger-findings
started: 2026-10-28
updated: 2026-10-28
mode: integrate
status: paused-for-author
baseline:
  commit: 06fd9b8
independence: separate-agents
---

# CR-039: the ledger findings of 27 October 2026

## Brief

- **Desired outcome:** apply the author's answers to the twelve commitments-ledger findings and give proposals where the author asked a question.
- **Authorization:** author, 28 October 2026, answering each finding in `commitments/README.md` (quoted in `book-agent/revision/CR-039.md`).

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Concord replaces the 1887 compact (finding 2) | author 2026-10-28 | done |
| D2 | decision | Gulf compact at the Republic's founding, with the canal's opening (1900); sets the admission tests (finding 5) | author 2026-10-28 | done |
| D3 | decision | Concord first term 1927–1932 (finding 6) | author 2026-10-28 | done |
| D4 | decision | Protectorship renewed in 1864 (finding 9) | author 2026-10-28 | done |
| D5 | decision | "the state", not "the Crown", for the 1876 tobacco company (finding 10) | author 2026-10-28 | done, with §19 knock-on |
| D6 | decision | Silas's death (winter 1912) into canon_facts (finding 11) | author 2026-10-28 | done |
| D7 | decision | Waite, Association treaties, Truce signing approved (finding 12) | author 2026-10-28 | done |
| Q1 | open choice | P1 Puʻuloa 1924; P2 China's defense treaty; P3 Ka Lōkahi used twice; P4 Buchanan–Vallejo/Carson; P5 Querétaro; P6 1905 signing place; Cuban guarantee | CR-039 | open |

## Handoffs

| ID | To | Task | Output | Status |
| --- | --- | --- | --- | --- |
| H1 | fresh reviewer | Integrated storyline diff: consistency, label scope, prose | see Checks | done |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | lint_canon (full), cr_facts preview/apply/check | clean |
| X2 | commitments/ledger.py check and unit tests | 165 entries, 0 problems; tests pass |
| X3 | sync_master_storyline --write/--check; validate_character_docs | clean |

## Resume here

Author to answer CR-039 P1–P6 (Puʻuloa 1924, China's defense treaty, the double use of Ka Lōkahi, Buchanan–Vallejo/Carson, Querétaro, the 1905 signing place) and the Cuban guarantee. The branch `adopt/cr039` holds the integrated decisions.
