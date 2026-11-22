# CR-081 — verification of the grain review's fixes (22 November 2026)

What I read on 22 November 2026, in `/home/claude/cr081`: the AGENTS.md sections "Fresh-context review" and "Protected intent" and the CR-081 paragraph; `CR-081-grain-review.md`; `git diff 1b4f080 580ab82` for the storyline, ledger, register, generated index, AGENTS.md, outline and A-series; the storyline paragraphs around every changed passage (lines 1209, 1272, 1299, 1610, 1656, 1672, 1688, 1693, 1697), the summary at line 113, the Huludao pledge at 1073, the 1868 treaty at 750, the indemnity at 1128 and the Patrimony at 89, 890 and 967; searches for oath, Kiyoshi, Nishina, Pacific Companies, Fong, indemnity, granary, Patrimony, Senate, Zhang Xueliang, Huludao and Rossby; outline D5, D6 and D9; A-series §11; and, read-only, `provisioning.md` §§3, 7 and 8, with §4 for G-10's export figure. I did not read session records or `CR-081-provisioning-review.md`.

## Verdict

**Ready with minor fixes.** All 22 items are applied, and the storyline wording matches the review's. One fix brings in a new conflict and needs the author's decision before merge: the Senate's vote on the granary (problem 1). The rest are wording and record fixes.

## Items

| Item | Result |
|---|---|
| B1 | Applied. Kiyoshi, Nishina, Nagaoka, Victoria and the Companies' officers are clear (Japan and the crowns are excepted, and only entrants are bound). AGENTS.md leaves out "pay or rank". Line 113 still says "the exclusive oath" (problem 5). |
| B2 | Applied with a problem. The wording is the review's, but the Senate directing the Patrimony's reserves conflicts with CR-027 (line 967) and the Patrimony's charter (line 890) (problem 1). "The Industrial Board stands with him" now appears twice in one paragraph (problem 2). |
| B3 | Applied: "only" removed. |
| S1 | Applied, word for word. |
| S2 | Applied. Mukden and Nanjing rows extended; wheat-credit and granary rows added. One unsourced detail (problem 9). |
| S3 | Applied, word for word, in the storyline and the ledger. |
| S4 | Applied, word for word; the ledger's parties are now CN and ESTATES. |
| S5 | Applied, word for word. |
| S6 | Applied (option 2), chosen by the writer under the author's general instruction. "They" can be read as the soundings (problem 3). Not in the register's D9 entry (problem 10). |
| S7 | Applied, word for word. D9 records case A for family entry. D9 and G-11 put the 1868 article in §16; it is in §14 (problem 8). |
| S8 | Applied, word for word. "His mother's" follows a sentence about Tang (problem 4). The year 1899 matches the ledger row `C-1899-LIAODONG-PLEDGE`. |
| S9 | Applied: the merge order is in the register's open list and in AGENTS.md. The optional sentence was left out. |
| S10 | Applied in G-2, G-10 and G-14. G-1's new figures are inconsistent with each other (problem 6). |
| M1 | Applied; the labels are correct. |
| M2 | Applied. |
| M3 | Applied in the storyline and the ledger. |
| M4 | Applied for G-4, G-7 and G-12. The §16 reference in G-11 is still wrong (problem 8). |
| M5 | Applied. The revision date is in the later "Revised on 22 November 2026" clause, not in the parenthesis; that is acceptable. |
| M6 | Applied. |
| M7 | Applied with a problem. Nothing in the A-series changed, and D9 sends the rice figures to Hsiao Table 2.5, which is wheat flour (problem 7). |
| M8 | Applied in the register's D9 entry. |
| M9 | Applied as a note under G-13. |

## Changed passages

- **Labels.** Every inserted or changed sentence sits under **[APPROVED — CR-081]**. The text that follows keeps its own label: CR-040 after line 1209, CR-081 at 1272 and 1299, [OPEN] at 1610, CR-057 before "Japan's army officers count the district" at 1656, CR-057 at 1672 and [PROPOSED] at 1697.
- **Ledger.** All six rows agree with the storyline on quotes, parties, terms and sections: Mukden §32; Nanjing, Huludao crop and soybean compact §33; wheat credit and granary §34.
- **Figures.**
  - G-1 item 2 and G-14: 1920, 1933, 1938; 115%; 1940 (§§3, 7). Agree.
  - G-2: 5.0 Mt, 4.8 million mouths, "about 1930" (§8). Agrees.
  - G-10: "about 3 Mt" in 1931. Agrees: 3.3 and 2.7 million mouths × 1.05 t (§4) gives about 3.1 Mt. "About an eighth" holds, as 0.41/3.1 ≈ 0.13. 15 million bushels are 450,000 short tons, about 0.41 Mt.
- **Canon.** One new conflict, the granary's authority (problem 1). No conflict found for the oath, Kiyoshi, Nishina, the Pacific Companies, Fong, the indemnity, Zhang Xueliang, Huludao or Rossby.
- **Protected intent** holds: Noe Ward is untouched; Julian is never President; the oath excepts the crowns, so no throne question arises; and food stays out of the 1931 threat.

## Remaining problems and replacement wording

1. **The granary's authority (line 1672; ledger `C-1932-GRANARY-CONTRACTS`; register; AGENTS.md).** CR-027 has "The Crown does not touch their charters, appointments or the Patrimony", and the charter (line 890) has the board investing and paying three per cent into the budget. A Senate vote that directs the Patrimony's reserves breaks both. The review left the decider to the author; D9 integrated the Senate anyway. The author should choose.
   - *Case A* (recommended; it keeps the Senate scene and settles the 3% question as spending): replace "to be filled by the Patrimony from its own reserves without new issue" with "to be paid for from the Patrimony's three per cent without new issue".
   - *Case B*: replace "Julian asks the Senate for a Crown's granary" with "Julian asks the Patrimony's board for a Crown's granary", and "and the Senate votes the granary" with "and the board, which the Crown cannot direct, votes the granary as an investment".
   - Either way, update the ledger quotes and its open note, and the "voted by the Senate" lines in the register and AGENTS.md.
2. **Line 1672, repetition.** Replace "Giannini answers that the money should go to the mortgages, the Industrial Board stands with him, and" with "Giannini answers that the money should go to the mortgages, the Industrial Board again with him, and". Update the ledger's `more_quotes` to match.
3. **Line 1610.** Replace "so that they can be tried on" with "so that the forecasts can be tried on".
4. **Line 1272.** Replace "The option at Huludao, his mother's of 1899," with "The option at Huludao, Victoria's of 1899,".
5. **Line 113.** Replace "under the exclusive oath, the Crown's granary filled in the slump" with "with the Crown's oath for entrants, the Crown's granary voted in the slump" (or "bought" under problem 1 case B).
6. **G-1 item 1 and A-series §11.** 2.4 Mt at 40% of the crop implies a crop of about 6 Mt in 1926, above the new series (5.3–5.4 Mt by 1929–30). After "(about 2.4 million tonnes)" add: "which at 40% implies a crop near 6 million tonnes, above the research note's series; to reconcile against Sun's tables". The upper-bound conclusion still holds.
7. **D9, M7.** Replace "to verify against Hsiao, Table 2.5" with "to verify against Hsiao's rice import table (Table 2.5 is wheat flour)".
8. **G-11 and D9.** Replace "storyline §16" and "(§16, PROPOSED)" with "§14".
9. **Ledger `C-1931-CHINA-WHEAT-CREDIT`, open.** Replace "(our timeline's loan: 4%, three instalments 1934–36)" with "(our timeline's loan: 4%, A-series §11; three instalments 1934–36, general knowledge, to verify)".
10. **Register, D9 entry.** Add before "Outline-only": "the trial forecasts wait on soundings the Weather Office asks of the Customs at Huludao and Shanghai; the Huludao option is Victoria's of 1899; the crop estimate is undated; the 1868 article's families are read as spouses and children (case A)." Then run `sync_master_storyline.py --write` and `--check`.

## Checks run (in `/home/claude/cr081`)

- `lint_canon.py`: "Canon lint clean: 4 files checked."
- `commitments/ledger.py check`: "327 commitments checked, 0 problem(s)."
- `sync_master_storyline.py --check`: synchronized.
- `cr_facts.py check`: the register and facts file agree (254 approved fact changes).
- `lint_canon.py --only book-agent/revision/CR-081-outline.md`: one finding, the known false one at the Sherman 1891 line (849).

## Not checked

- The character bible and registry, including the oath against the Chinese Pacificans already serving.
- The financial workbook.
- CR-082 and whether R-1's wheat contract needs the granary's text once merged.
- The sources in the author's research note (Hsiao, Sun, Prodöhl, Cheng), which I did not fetch.
- `provisioning.md` beyond §§3, 4, 7 and 8.
- The session record in the diff.
