---
session: 20261031-cr048-rump
started: 2026-10-31
updated: 2026-10-31
mode: adopt
status: stopped
baseline:
  commit: 9aa40f7
  files:
    book-agent/revision/master_storyline.md: sha256:fe64c7058224e77e82a99b6f37d2c75d3a327cfbc4a384c75e01dc4a2c882964
    book-agent/revision/change_requests.json: sha256:90a79982a2ee1881a5287f1555125710c8b824c76d722d30706ca3b0a902b20e
independence: same-agent drafting and integration; one fresh-context review of the storyline passages before merge (fourteen findings, addressed: CR-048.md, Integration review)
---

# What becomes of the rump Confederacy, 1900–1930, and what does it do to the Union?

## Brief

- **Desired outcome:** the home-front arc: the rump's economy, its neighbours' influence and its life; a Black movement that troubles the Union enough to keep scientists choosing Pacifica.
- **Authorization:** author, 31 October 2026: the brainstorm and directions A1–A6; R2, R9, R14 delegated and decided; R12 (the *Tribune*) and R17 (Garvey) approved; R18 (presidents) and Just delegated; departure rates approved; "Ok please integrate the CR with the storyline text, the presidents table, the commitments ledger entries and the character files."
- **Sources of history:** census state tables as recalled (Gibson & Jung 2002, VERIFY); Wikipedia spot check for Georgia; standard histories of Garvey, Du Bois, Just and the readmission acts.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-10-31 | explore | Author: "For the next arc I want to do some brainstorming on the home front" |
| 2026-10-31 | draft | Author: "Yes please go ahead and write this up as CR-048" |
| 2026-10-31 | adopt | Author: "Ok please integrate the CR…" |

## Author decisions and open choices

- D1–D6 = A1–A6; D7 = R1 departure rates; D8 = R2; D9 = R9; D10 = R12; D11 = R14; D12 = R17; D13 = R18; D14 = R11 (Just).
- Q1: Franz Boas and the Act's celebrated dismissal (reaches beyond the rump).
- Q2: workbook follow-through (World sheet rump population, Union and Gulf plus emigrants, Gulf conversion loan).
- Q3: VERIFY the five-state census figures against Working Paper 56.

## Checks executed

- X1: cr_facts.py apply CR-048 and check; lint_canon.py clean; sync_master_storyline.py --write/--check; validate_character_docs.py; commitments/ledger.py check and report; population tests (Neighbours).
- X2: fresh-context review of the storyline passages; fourteen findings addressed.

## Round log and stop reason

Integrated on the CR-048 branch; awaiting the author's merge.

## Resume here

- Merge CR-048 (PR) on the author's word. Then Boas (Q1), the workbook follow-through (Q2) and the census verification (Q3). Note that CR-045, CR-046 and CR-047 exist as project documents but are not in the repository's main branch.
