---
session: 20261031-cr043-peace
started: 2026-10-30
updated: 2026-10-31
mode: adopt
status: stopped
baseline:
  commit: fc69d7e
  files:
    book-agent/revision/master_storyline.md: sha256:79790eac4ed14da53d3556665e58a65d18d572215845f004a6c1802855cc706f
    book-agent/revision/change_requests.json: sha256:ebd91eabb09141977b80c63fca954b6208bb840b3de35c063dea54127d2ca2ae
independence: same-agent (drafting and integration combined; self-review only)
---

# How is the war of 1914–18 ended, and who makes the peace?

## Brief

- **Desired outcome:** the defeat, the place and date of the peace and its broker defined (W4); Alsace-Lorraine and Switzerland (W5); the Czech question; the Legion's pay.
- **Authorization:** author, 29–30 October 2026 (see the CR-043 register entry); merge: "You can merge CR-043 and CR-044 now" (31 October 2026).
- **Sources of history:** the 1907 Hague Convention (Article 8 verified by the author); Bryan's record; Kaʻiulani's final illness and Kocher's surgery as supplied and discussed; Neilson and Nock (read for Wilson; neither book treats Bryan's candidacy).

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-10-29 | explore | Author: W4, W5 and the Czechoslovak question |
| 2026-10-30 | draft | Author: "Let's add the suggested structure for the commission as a 'special mediation' under Article 8" |
| 2026-10-31 | adopt | Author: "You can merge CR-043 and CR-044 now" |

## Author decisions and open choices

- D1–D12 = CR-043 P1–P12 (book-agent/revision/CR-043.md).
- Q1: Kaʻiulani's date of death; whether she marries.
- Q2: Germany's regent.
- Q3: Pacifica's secretary-general at The Hague.
- Q4: Janin (F3) and the French money-trail items (F4).
- Q5: Štefánik; Slovak autonomy; Karl's coronation.

## Checks executed

- X1: cr_facts.py apply CR-043 and check; lint_canon.py clean; sync_master_storyline.py --write/--check; validate_character_docs.py; commitments/ledger.py check; population unit tests.
- X2: workbook rebuilt with finance/build/cr043_legion_pay.py and recalculated in LibreOffice (0 formula errors); Story-case comparison in finance/CR-041-workbook.md.

## Round log and stop reason

Integrated on the CR-043 branch and merged as PR #53, before CR-044.

## Resume here

- CR-044 (Omsk, the hostages, *Pele*, Patton) follows in PR #54.
