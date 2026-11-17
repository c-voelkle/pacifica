# CR-071 — Fresh-context review against `main` after CR-072 and CR-073 (17 November 2026)

**Base:** `main` at 586ca26 (CR-072 and CR-073 integrated, PR #74), with CR-071's documents brought over from `drafts/cr071-073-counties` (a local branch, not pushed). **Independence:** one separate reviewer given only the candidate texts (`CR-071-storyline.md`, `-ledger.md`, `-registry.md`, the outline's fact changes), the affected canon on `main` (§§5, 12–26 and the header notes; the ledger entries CR-071 changes), the CR's canon-tensions sections and AGENTS.md. The drafter's mechanical checks are listed separately (section M). Each blocker was checked again against `main` before this was written down.

**Verdict:** not yet ready. Four blockers, all mechanical or about placement, none needing a new decision except possibly 12 (Sherman). After the fixes, one more run of `lint_canon.py`, `ledger.py check` and the sync should be enough. A second review is needed only if the §19 and §25 reordering is large.

## M. Mechanical checks (drafter)

- `lint_canon.py` (canon and the eleven CR-071 files) is clean, `cr_facts.py check` agrees, and the sync is current. The fact preview finds one canon passage to change, §12 l. 572 "The Providentorship lasts for Elias's life.", which R1 item 1 covers.
- Every quoted anchor exists exactly once on `main`. §22's anchor uses curly apostrophes on `main`, so copy it as it stands. Table A's line numbers and the ordinals "fifth paragraph" and "last paragraph" in §21 are out of date because CR-072 inserted l. 831.
- **Japan's loan of 1873.** It is approved twice: CR-071 L10 and decision 6, and CR-073 R10 (the Bank of California as the Republic's agent). The storyline still labels it **[PROPOSED — CR-071]**, and C-1873-JP-LOAN has `status = "PROPOSED"`. It should be APPROVED. Add the Spanish loan entry's condition: "The Bank of California is the Republic's agent for the loan (CR-073 R10, APPROVED)".
- **Deseret's charter (T3).** CR-071-ledger.md ends C-1866-DESERET-CHARTER, but nothing records that its marriage and church-property law carries over to the Constitution of 1887 as a personal guarantee for every registered church (CR-072 P16; CR-072's ledger note leaves this to CR-071). Add a condition to C-1887-CONSTITUTION, and the T3 terms to the charter's row, as for Columbia and Washoe.
- **Leftovers on `main`, which can be fixed in the same pass:** §25 l. 910 "until 1914" (CR-040's 1907), and C-1874-ORDINANCES `ended = 1914`.

## Blockers

1. **The ratification is told twice (§21).** CR-071's ratification block goes after l. 829, directly before CR-072's l. 831. Both paragraphs then narrate the interior legislatures carried, Taylor resisting until 25 July 1887 and Cannon bringing the Church in. Cannon is also named before l. 831 introduces him. **Fix:** place the block after l. 831. Cut "John Taylor will not accept it and dies on 25 July; George Q. Cannon brings the Church in," and "The interior legislatures ratify on their grants in May and June." Keep Deseret's legislature's last act and Cannon's telegram.
2. **Ledger quotes that `ledger.py check` would fail.**
   - R1 item 1 removes "The Providentorship lasts for Elias's life." and "Its enabling delegation lapses …", which are `more_quotes` of C-1865-PROVIDENTOR (l. 1092) and C-1865-ENABLING (l. 1075). Replace both quotes with the new sentence.
   - The Baja block goes in after "Mexico retains Sonora." and splits C-1867-BAJA's quote. Place it after the whole paragraph.
   - These `quote_draft`s don't match the drafted text: C-1879-ASSUMPTION, C-1879-COMMISSION-ACT, C-1882-MILITIA, C-1867-BAJA-COMMISSION, C-1865-HOPI, C-1878-PORTNEUF-ROW and C-1888-NATIONS-LADDER.
   - C-1872-APACHE-MINING-LEASES has no storyline sentence. Write one or drop the entry.
   - The ledger draft's header still says the storyline is not written.
3. **Salt Lake is still "ordinary" in the storyline (§22 l. 850).** CT7's approved amendment ("stay counties, not Crown cities") is entered only for CR-021.md. The storyline's own "Portland, Seattle and Salt Lake remain ordinary counties" contradicts the charter of 1894. **Fix:** add a row to table A.
4. **The Baja row would also approve Guaymas (A row 8; l. 631; ledger C-1867-BAJA).** The sentence that becomes **[APPROVED — CR-071]** also carries "a Guaymas railway concession and free port", against CR-057's "Guaymas waits on Mexico". **Fix:** split the sentence: the Baja purchase becomes APPROVED and Guaymas stays **[PROPOSED]**. Split the ledger entry the same way.

## Should fix

5. **Mountain Districts (§12 Ute block; l. 582, 799).** South Park and the upper Arkansas are Pacifican by the 1865 line; the districts that vote themselves over are the Front Range ones (1878–80). Suggested: "The mountain districts never become a member: South Park and the upper Arkansas are governed as districts under a confederal commission at Fairplay, each with its own miners' code, and the districts that later vote themselves over join it."
6. **The grant machinery is told twice (§13 first paragraph; l. 568, 570).** It retells l. 568, and CR-072's l. 570 now depends on it. **Fix:** move it into §12 in place of l. 568's last sentence, before l. 570.
7. **§19's order (l. 775, 777).**
   - Two paragraphs in a row now open with Soberanes "back from Vladivostok".
   - The text runs to 1886 and then returns to CR-072's "About 1880".
   - Row 9 names the Militia Act inside a CR-022 sentence before the Act is introduced.
   - Suggested order: the memorandum and the Collar (1878–80), then l. 777 (cut "back from Vladivostok"), then l. 775, then the Militia Act, then the survey. Drop row 9, or label it CR-071.
8. **Who commissions the 1880 survey.** "The Patrimony's Development Fund commissions" conflicts with CR-057 (l. 806: the Patrimony "spends nothing for thirty years"; the Fund lends beside private capital). **Fix:** "the Superintendency commissions …", with Ralston, who sees the maps, working it out.
9. **§25 order (l. 889–900).** The receivership block (1892–95) is inserted before CR-072's 1888 paragraph. It also relies on the rule that no congregation may capture a county, which l. 897 (CR-037, from 1890) introduces only later. **Fix:** move both paragraphs after l. 897 or l. 900.
10. **§14 placements.**
    - The Japan block calls him plain "Kido" before CR-072's l. 671 introduces Kido Takayoshi, and puts 1871 after the Iwakura landfall of 1872. **Fix:** insert it before the Iwakura sentence and write the full names; shorten l. 671 to "Kido, who governs by rescript …".
    - The Ouray and Dall block splits CR-070's Alaska run (l. 661–665). **Fix:** put Ouray with the Ute material; put Dall after l. 665, as "the naturalist of the telegraph survey".
11. **Labels.**
    - The Apache countries are labelled APPROVED inside a peace still PROPOSED (l. 585; C-1865-APACHE).
    - The Hopi leaders and Oraibi, and the ladder law's year and which nations climb first, should be **[OPEN]**, as section C and the ledger have them.
    - Split Mattson (**[PROPOSED]**) from the programme's scale (**[OPEN]**).
    - "The Rogue valley farmer's name" refers to no farmer in the text.
    - R1 row 3 adds approved decisions without a CR-071 label.
12. **Sherman after 1865 (AGENTS.md: "Sherman's fate after 1865 stays OPEN").** He chairs the board of examination in 1882 under an APPROVED label, but no decision, tension or registry row records it. Label it PROPOSED, or record it as the author's decision. Add registry rows for Sherman, Silas (the Sierra line, 1882–85) and Davidson (succeeded 1885).
13. **The appointed Senate seats.** The storyline gives them to "the members' executives … and Pacheco"; the ledger gives them to "the Commissioners in office". Pacheco is a member executive, and Deseret's executive is in or out depending on which wording wins. "That day" has no antecedent. **Fix:** "The Commissioners of the Confederation in office on 1 August 1887, and Pacheco, …", or "every member executive, Pacheco among them".
14. **Ledger gaps.**
    - Section numbers are stale: San Juan lease 15→14; Assumption, Commission Act and Militia →19; Portneuf →13.
    - Missing entries: the trunk-line charters on Land Fund grants; the Baja nations' compacts; San Miguel and Mora's adherence of 1867 and Fort Union's contracts (amend C-1866-NM-CHARTER); possibly Salt Lake's charter of 1894.
    - Date the Fort Hall lease in the text and match it in `from`.
15. **Memo-like handover sentence (§21).** "The founder's lesson of 1860 … had nowhere to serve while the members held the offices." is the narrator explaining. Cut it or give it to Elias watching the oath. Replace "The Providentorship ends with the regency on 1 August 1887, and the states end with it." with "With it the Providentorship and the states end."

## Minor

- **§5:** the move to Sacramento in December 1849 follows a paragraph that already runs to 1851; insert it before "The election of 1850 …".
- **The Apache sentence:** place it before "Mangas dies …".
- **Wilcox block:** "against the Territorial Council"; "The Regent rides into Honolulu".
- **Survey:** "its second purpose, the map of counties that will replace the members"; "In 1884" is said twice.
- **Wording:**
  - "make the constitution urgent while the founder lives".
  - "elected for two terms by wards that follow the old county lines" is unclear.
  - "123 county senators" and "the Slope is Colorado west of the divide" read as glosses.
- **Two Chaveses at Las Vegas** (Manuel; José Francisco at l. 587): tell them apart. Add registry rows for Manuel Chaves and Hikozō.
- **Registry:**
  - Victoria's "four reasons" don't match the storyline's ("a life Providentor, not a king").
  - Fair, Victorio and Deady's seat have no storyline text yet.
  - The note on CR-072's people is out of date.
  - The fact-changes header still assigns Cannon's and Taylor's `add_person` entries to CR-071.

## Confirmed fine

- Every anchor exists. The fifteen fact patterns match the drafted wording.
- Consistent with CR-072 and CR-073:
  - Judah's survey and his death in 1890;
  - Broderick stepping aside about 1880;
  - the Committee party;
  - Ralston as the Patrimony's chairman from 1880, "the Patrimony spends nothing", and S7;
  - the August 1875 discount.
- Dates and ages hold: Taylor (25 July 1887), Dall at forty in 1885, Pacheco, Salt Lake's five years (1888–92) and its qualifying in 1893.
- Sacramento as the inland command's seat (l. 850). Oregon's exclusion lapsing. Commissioners serving outside their home counties.
- Protected intent untouched.

## Outcome (17 November 2026, night)

The author confirmed E-12 at 23:03 ("Yes sherman should chair it, that is my decision") and asked for the blockers, the should-fix items and the minor fixes to be applied. `main` (CR-072 and CR-073, #74) was merged into `drafts/cr071-073-counties`. Applied in `CR-071-storyline.md` draft 2, `CR-071-ledger.md` draft 2, `CR-071-registry.md` draft 2, the outline and Part E:

| # | Outcome |
|---|---|
| 1 | **Fixed.** The ratification block sits after CR-072's l. 831; Taylor's and Cannon's resistance and the interior legislatures are told once, by CR-072. |
| 2 | **Fixed.** Every `quote_draft` is verbatim from the storyline text. Section B replaces the quotes that R1 changes: Providentor, Enabling, Truce, Act of Settlement, and also Ute/Shoshone-Bridger, which the scratch run found. The Apache leases have their sentence (§13). Ledger header updated. Checked on a scratch integration: `ledger.py check` reports 288 commitments and one problem, C-1867-BAJA's status, which section B sets. |
| 3 | **Fixed.** A row 8: "remain counties, not Crown cities". |
| 4 | **Fixed.** A row 3 splits the Baja purchase (APPROVED) from Guaymas (PROPOSED); the ledger entry is split into C-1867-BAJA and C-1867-GUAYMAS. The Baja commission block goes after the whole paragraph. |
| 5 | **Fixed** as suggested. |
| 6 | **Fixed.** The grant machinery moves to §12 after l. 568, before CR-072's l. 570. |
| 7 | **Fixed.** Order: memorandum and Collar; l. 777 without "back from Vladivostok"; l. 775; the Militia Act; the survey. Row 9 dropped. |
| 8 | **Fixed.** The Superintendency commissions the survey and the Fund lends on its tables. E-16's mechanism is amended in Part E; Ralston still sees the second purpose and keeps the secret. |
| 9 | **Fixed.** The receivership and Salt Lake go after l. 897; the nations' ladder goes after l. 934, beside CR-033's leakage of land. |
| 10 | **Fixed.** The 1871 block comes before the Iwakura sentence, with full names, and CR-072's line is shortened. Japan's loan of 1873 goes into CR-073's paragraph before the Spanish loan. Dall comes after l. 665. Ouray's lease moves to §13 with the other leases. |
| 11 | **Fixed** (Hopi, ladder, Mattson, Rogue farmer, R1 row 3), except the Apache countries, which keep APPROVED as I-52 approves them (storyline D). |
| 12 | **Settled by the author** (E-12 confirmed). Registry rows for Sherman, Silas and Davidson; AGENTS.md's "Sherman's fate after 1865 stays OPEN" is amended at integration (storyline C). |
| 13 | **Fixed per K-11:** "The Commissioners of the Confederation then in office, and Pacheco". Pacheco is not redundant, because California refused the Commission Act. |
| 14 | **Fixed:** section numbers; new entries for the trunk-line charters, Baja's compacts and Salt Lake's charter; San Miguel and Mora in C-1866-NM-CHARTER; Fort Hall dated 1881 (C-1881-PORTNEUF-ROW). |
| 15 | **Kept and rewritten**, because B-2 (APPROVED) requires the look-back. It names the two votes by what happened; "With it the Providentorship and the states end." |
| M | **My own checks:** Japan's loan is APPROVED, with the Bank of California as the Republic's agent; Deseret's marriage law is carried over in C-1887-CONSTITUTION and C-1866-DESERET-CHARTER (T3); the 1914 leftovers are corrected (A row 10; C-1874-ORDINANCES). |
| Minor | **All applied:** §5 split; the Apache sentence before Mangas; Wilcox; the survey's wording; the triggers sentence; ward wording cut; glosses recast; Manuel Chaves distinguished; Victoria's reasons; the registry notes; the fact-changes header. Hikozō and Manuel Chaves already had entries (CT-HECO, CT-MANUEL-CHAVES), and amendments were added. |
| Added | **Two approved decisions without storyline text are now written:** the article of supersession in 1866 (K-15, F–G T4; §12) and Sherman's refusal of June 1884 (E-14; §19). |

## Second fresh-context check (17 November 2026, night)

A separate reviewer was given only the scratch integration of draft 2 (§§5, 12–14, 19, 21–25), the outline's canon tensions and AGENTS.md. It found no blockers and seven should-fix items, all local; the verdict was "ready to integrate once the seven should-fix items are done". Applied:

1. **The Baja commission.** It is "chartered by the confederal chambers". The Northern Commission is not met until §14.
2. **The three senses of Commissioner.** The governors who hold the confederal commission get the Senate seats. The 124 county Commissioners, commissioned on 1 August 1887, take up their counties in 1888, when the first boards are elected.
3. **The look-back.** It now matches the Collar (from 1879 the examined serve under elected governors) and the vote of 1864 ("kept him by a single Californian"). "The Chronicler gives the day and the room" becomes "Elias's words that day are not recorded."
4. **Sherman's §22 sentence** (A row 9): the refusal is APPROVED, and the death in 1891 stays PROPOSED.
5. **Hawaii and the Collar:** "Hawaii, under its Territorial Council, is not asked."
6. **Monterey in 1849:** "Monterey, the republic's first capital, keeps the courts, and in 1856 the Confederation makes it its seat" (K-18).
7. **Victoria's reasons** are her argument to Elias; "the Confederation", not "the Realm", in 1886.

Minor items applied:
- Hawaii's ratification is cut from CR-071's block (canon l. 829 tells it).
- The leagues are cut from the ladder (§21 tells them).
- "The states end with it" (the Providentorship's end is told by A rows 1–2); "the title of Providentor as a style".
- California's legislature taken "from the Committee party" (CR-073).
- "the inland command" named.
- "their old counties".
- "The Utes come to the peace having earned their terms".
- Leadville "the new silver town".
- Powell's year marked OPEN.

Minor items not applied:
- The order of canon's own §13 paragraphs (Baja before Juárez) is canon's.
- The survey stays after the Militia Act on purpose: the memorandum's order is "the armed men, then the map".
- Labels in the storyline are scoped to the paragraph, as throughout canon, so the unlabelled canon paragraphs after a CR-071 block do not inherit its label.

**Scratch integration re-run on the final drafts:** `lint_canon.py` clean; `ledger.py check` 288 commitments, 0 problems (with section B applied); `sync_master_storyline.py --check` synchronized.
