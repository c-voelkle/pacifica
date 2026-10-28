---
session: 20261028-cr039-ledger-findings
started: 2026-10-28
updated: 2026-10-28
mode: integrate
status: complete
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
| D8 | decision | Nanjing, Buchanan–Vallejo/Carson, Querétaro, Urajio signing; Japanese place names after a transfer | author 2026-10-28 (second round) | done |
| D9 | decision | Puʻuloa 1924: options a (tenancy at the Mōʻī's pleasure) and b (reef clause); "the Crown" stays during the regency | author 2026-10-28 (third round) | done |
| Q1 | open choice | Ka Lōkahi on hold for a larger author change; Cuban guarantee; Bread March sentences | CR-039 | open |

## Handoffs

| ID | To | Task | Output | Status |
| --- | --- | --- | --- | --- |
| H1 | fresh reviewer | Integrated storyline diff: consistency, label scope, prose | findings applied; Cuban guarantee and regency-era "Crown" left for the author | done |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | lint_canon (full), cr_facts preview/apply/check | clean |
| X2 | commitments/ledger.py check and unit tests | 165 entries, 0 problems; tests pass |
| X3 | sync_master_storyline --write/--check; validate_character_docs | clean |

## Resume here

CR-039 is integrated and merged into main (author, 28 October 2026: "Go ahead and merge it"). Open: Ka Lōkahi (on hold for a larger change the author is planning), the Cuban guarantee (suggestion: date it to Cuba's formal independence in 1902, when the Gulf Republic exists) and the Bread March sentences.
