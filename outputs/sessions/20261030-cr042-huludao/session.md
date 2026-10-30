---
session: 20261030-cr042-huludao
started: 2026-10-30
updated: 2026-10-30
mode: adopt
status: stopped
baseline:
  commit: 09fc30a
  files:
    book-agent/revision/master_storyline.md: sha256:de45e74c2aea4d05b5b256415bb9606a6a82aaeab49ada1aaa138bbf54538447
    book-agent/revision/change_requests.json: sha256:4c0c89e6ac4e4d44b6af393b269d304970b2b40077c74302b01bc4686367d9d0
independence: same-agent (drafting and integration combined; self-review only)
---

# Should Pacifica own a door at the end of the Chinese line, as Napoleon advised?

## Brief

- **Desired outcome:** a port that keeps Pacifica out of a Japanese doorway, written up as a short CR and integrated.
- **Authorization:** author, 30 October 2026: the split (pledge and option in 1898–99, trust in 1908–10) approved; "Please write this up as a short CR"; "Ok please merge this CR". Japan's reaction and the Victoria–Cixi scenes are out of scope.
- **Sources of history:** CR-041 Appendix B (Napoleon, non-canonical); the earlier session on the CR-041 workbook (PR #51); the Anglo-Pacifican planning note.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-10-30 | explore | Author: "Do you think it makes sense to buy a separate port at the end of the Chinese line" |
| 2026-10-30 | draft | Author: "Please write this up as a short CR" |
| 2026-10-30 | adopt | Author: "Ok please merge this CR" |

## Author decisions and open choices

- D1–D5 = CR-042 H1–H5 (see book-agent/revision/CR-042.md).
- D6 = CR-042 H6: a British and Pacifican syndicate, Britain senior, builds Mukden–Jinzhou–Huludao in 1908–10 (author, 30 Oct 2026; settles Q1).
- Q2: who builds the Harbin–Mukden line.
- Q3: Japan's reaction (off the page).
- Q4: Victoria–Cixi scenes.

## Checks executed

- X1: lint_canon.py clean; cr_facts.py apply CR-042 and check; sync_master_storyline.py --write/--check; validate_character_docs.py; commitments/ledger.py check (176, 0 problems).

## Round log and stop reason

Integrated and merged as PR #52. H6 added afterwards and merged with PR #51 (the CR-041 workbook, rebased on main, plus `finance/build/cr042_huludao.py`).

## Resume here

- The Anglo-Pacifican cold-war arc: settle W1–W4, U4 and T7 (planning note §9–§10), then draft the first follow-on CR (Britain in the Russian war, the K1 amendment for Dzerzhinsky and Stalin, Alash's regiments).
