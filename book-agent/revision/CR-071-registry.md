# CR-071 — Character registry and bible (draft 2, 17 November 2026; entered at integration)

**Status:** DRAFT for the author (outline, "Before integration", item 5). New people get registry entries and `add_person` facts **together, at integration**, so that every ID the facts file names is in `character_registry.json`; then `validate_character_docs.py`. Nothing below is in the registry yet. Proposed IDs are written without their `CT-` prefix, as CR-073 writes its proposed entries, so that the linter does not read them as unknown IDs; the prefix is added at integration. Life dates are historical (Hist.) unless the row says the story changes them.

**Draft 2** (after the fresh-context review against `main`, `CR-071-review-on-main.md`) does four things:
- marks CR-072's people as in the registry;
- adds rows for Sherman (E-12 to E-14, confirmed by the author on 17 November 2026 at 23:03), Silas, Davidson, Manuel Chaves and Hikozō;
- brings Victoria's four reasons into line with the storyline text;
- records that Fair, Victorio and Deady's seat have no storyline text yet.

## A. New people

| Proposed ID (CT- added at integration) | Person | Nature | CR-071 role | Life (Hist.) and what changes |
|---|---|---|---|---|
| REGINALDO-DEL-VALLE | Reginaldo Francisco del Valle | historical, alternate career | Born in the Republic (1854); defeats the English-only records bill of 1880–81; president pro tempore of California's senate; carries the ratification in May 1887, narrowly (G6.3–G6.5); sits for a Los Angeles county or among the appointed from 1888; lives into Julian's Senate fights | 1854–1938, unchanged |
| JAMES-FAIR | James Graham Fair | historical, alternate career | One of the Bonanza four; chosen by Washoe's legislature for the Confederal Council in 1881; leads Washoe's opponents of the act, four of nine (H-6, W-1) | 1831–1894, unchanged. CR-073 proposes one BONANZA-FIRM entry for Mackay, Fair, Flood and O'Brien; CR-071 needs Fair on his own. **Recommendation:** Fair gets his own entry, linked to BONANZA-FIRM |
| ROBERT-WILCOX | Robert William Wilcox | historical, alternate career | Leads the Honolulu rising of 30 July 1889 at Aliʻiōlani Hale; put down by the Queen's Guard, seven killed; acquitted by a Hawaiian jury in 1890 (H-11) | 1855–1903, unchanged (H-14); the 1907 campaign passes to others, possibly his widow Theresa |
| SAMUEL-NOWLEIN | Samuel Nowlein | historical, alternate career | Commands the Queen's Guard in 1889 (H-13) | c. 1851–1905 (to verify). When he succeeds Moehonua is OPEN |
| JOHN-WESLEY-POWELL | John Wesley Powell | historical, alternate career | Heads the land and water office; his arid-lands plan of 1878 (irrigation districts by watershed) is policy, and its rule draws the counties (I-65, E4) | 1834–1902. When he enters Pacifican service is OPEN |
| HANS-MATTSON | Hans Mattson | historical, alternate career ("an emigration agent such as") | Runs the passage offices of the interior settlement programme (I-65, Part C) | 1832–1893. Named as a type: the author may keep him or replace him with another agent |
| OURAY | Ouray | historical, alternate career | Grew up at Taos speaking Spanish; comes to the 1866 table with Carson; in 1873 negotiates the San Juan lease in place of the Brunot cession (I-68) | c. 1833–1880. His death in 1880 is not changed by CR-071 and stays as historically unless a later CR changes it |
| WILLIAM-HEALEY-DALL | William Healey Dall | historical, alternate career | Naturalist of the telegraph expedition (1865–68), stays with the line when the Confederation buys it in 1868 (PROPOSED); succeeds Davidson at the head of the Northern Commission in 1885, at forty (I-69) | 1845–1927, unchanged |
| HENRY-MILLER | Henry Miller (of Miller & Lux) | historical, alternate career | The riparian plaintiff of *Lux v. Kern River District* (working name), the water decision of October 1886 (K-6, F3); his partner Charles Lux dies in March 1887 (Hist.) | 1827–1916, unchanged |
| VICTORIO | Victorio | historical, alternate career | With no removal there is no Victorio's war; he may sit on the council that spends the Santa Rita royalty (I-66) | c. 1825–1880 historically, killed at Tres Castillos. **His death is OPEN here**: the war that killed him does not happen |

**People CR-072 brought in** are in the registry since its integration on `main` (17 November 2026): CT-JOHN-TAYLOR, CT-GEORGE-Q-CANNON, CT-THEODORE-JUDAH, CT-DAVID-BRODERICK. CR-071 adds nothing to their entries except the amendments in B (Cannon's telegram; Judah's survey under the Superintendency).

**Entries without storyline text yet.** Fair (H-6, W-1), Victorio (I-66) and Deady's seat on the Court (H-4) are not in the storyline text of draft 2. Their registry entries and amendments go in with it as recorded decisions; the storyline mentions them when Part H's text is written (outline, Fact changes: H's `add_event` records wait for it).

**Named only, no entry:** Charles Lux; Ōkubo and Saigō (Part D's comparison, not the Chronicler's); Kido Takayoshi and Itō Hirobumi, who are named in §14 (CR-072 already names Kido without an entry; an entry for both is the next CR's to give, if they come back); Theresa Wilcox; the first Commissioners, the Baja commissioners and the first Chancellor (OPEN).

## B. Existing entries to amend

| ID | Add |
|---|---|
| CT-ELIAS | Lays the Providentorship down on 1 August 1887, weeks before his death, and keeps the style only, with no seat (G-1, G-11). In December 1886 his draft of the Constitution makes Victoria Queen of the Realm; she strikes it (K-19). The Commission Act of 1879; the commissions confirmed in person at Monterey (E3.1). |
| CT-KAIULANI (Victoria) | Declines the Realm's crown in December 1886 and has the regency article drafted in its place, for four reasons, as the storyline gives them: a crown for her would decide between the founder's sons while he is dying; the members' men took a life Providentor, not a king; the Realm still carries the ordinances that stretched her lease; power held for a crown not yet settled is the older Hawaiian form (K-19, G1.3a). Takes the oath at Thalassia on 1 August 1887 in Elias's presence and signs the 124 commissions as her first act (G-1, R-1). Receives Pacheco at Thalassia in the winter of 1886–87 (G6.2). Refuses the naval party's marines in July 1889 and sends the Queen's Guard (H-11). |
| CT-SOBERANES | Drafts the bill of 1887 and, at Victoria's instance, the regency article (K-19); makes the Californios' case to Pacheco (G6.2); takes the Polytechnic's commission from the Regent on 1 August 1887 (G4). |
| CT-ROMUALDO-PACHECO | Home from Manila about 1885; President of California from November 1886, chosen by the legislature in joint session (R-3); brought in by Manila, the Californios' arithmetic and Victoria, and takes home the historic-land clause (G6.2); signs away exclusion with his eyes open (G-10a); an appointed Senate seat held to sixty-eight and precedence at Monterey (G4). Dies 1899 (Hist.). |
| CT-MATTHEW-DEADY | Reads the article of supersession for the Realm; a seat on the Court of the Realm, 1887–1892 (H-4). |
| CT-KIT-CARSON | At the Ute table of 1866 with Ouray (I-68). |
| CT-BARBONCITO | Will not have degrees: the Diné line is drawn by landmarks, with the road article north of Beale's road (I-63). |
| CT-COCHISE | Dies in 1874 and is buried in secret in the Dragoons, inside his people's country (I-62, as historically). |
| CT-SHERMAN | Chairs the board that examines every commission under the Militia Act of 1882, militias', regulars' and Auxiliary's, and keeps them out of the Party's hands; at his request the officers who fail form the inland command (E-12, E-13). In June 1884 refuses the state after the founder, offered by men of the old army and some Prosperity men (E-14). Backs constitutional allegiance at the Truce (canon). His fate after 1887 stays OPEN. |
| CT-SILAS-CLAIMANT | Fails the mathematics before Sherman's board in 1882 (CR-022's failure, dated; K-2); the failed officers kept together as the inland command; commands on the Sierra line, 1882–85 (E-13). |
| CT-GEORGE-DAVIDSON | Succeeded at the head of the Northern Commission by William Healey Dall in 1885 (I-69). |
| CT-MANUEL-CHAVES | Speaks against adherence at Las Vegas in October 1867 and stays (A-3). Distinct from CT-JOSE-FRANCISCO-CHAVES, who publishes the protest of 1866. |
| CT-HECO | Kido and Itō read the Articles of 1856 through him at Nagasaki (Part D, D2). |
| CT-THEODORE-JUDAH | Heads the survey of 1880, commissioned by the Superintendency, on whose tables the Development Fund lends; draws the provisional map of 1884 and the 124 of 1886 (E4; CR-072 P12). |
| CT-GEORGE-Q-CANNON | His telegram reaches Thalassia two days before the handover, and Elias reads it himself (G-4). |
| CT-RALSTON | As CR-073 S7: 1886–87, as chairman of the Patrimony brings the San Francisco houses to accept the Constitution (E-15). Sees the second purpose of Judah's survey, whose sheets the Fund lends on, and keeps the secret (E-16, as worded in draft 2: the Superintendency commissions the survey, so the Patrimony spends nothing; CR-057). |

## C. Fact entries to add at integration

Added to CR-071's register `"facts"` with the registry entries above, not before:

```json
[
 {"add_person": {"id": "REGINALDO-DEL-VALLE", "aliases": ["Reginaldo del Valle", "del Valle"], "born": 1854, "died": 1938}},
 {"add_person": {"id": "JAMES-FAIR", "aliases": ["James G. Fair", "James Fair"], "born": 1831, "died": 1894}},
 {"add_person": {"id": "ROBERT-WILCOX", "aliases": ["Robert Wilcox", "Wilcox"], "born": 1855, "died": 1903}},
 {"add_person": {"id": "SAMUEL-NOWLEIN", "aliases": ["Samuel Nowlein", "Nowlein"], "born": 1851, "born_approx": true}},
 {"add_person": {"id": "JOHN-WESLEY-POWELL", "aliases": ["John Wesley Powell"], "born": 1834, "died": 1902}},
 {"add_person": {"id": "HANS-MATTSON", "aliases": ["Hans Mattson"], "born": 1832, "died": 1893}},
 {"add_person": {"id": "OURAY", "aliases": ["Ouray"], "born": 1833, "born_approx": true, "died": 1880}},
 {"add_person": {"id": "WILLIAM-HEALEY-DALL", "aliases": ["William Healey Dall", "Dall"], "born": 1845, "died": 1927}},
 {"add_person": {"id": "HENRY-MILLER", "aliases": ["Henry Miller"], "born": 1827, "died": 1916}},
 {"add_person": {"id": "VICTORIO", "aliases": ["Victorio"], "born": 1825, "born_approx": true}},
 {"add_person": {"id": "CT-ROMUALDO-PACHECO", "aliases": ["Romualdo Pacheco", "Pacheco"], "born": 1831, "died": 1899}}
]
```

Notes: the IDs take their `CT-` prefix at integration. Pacheco is in the registry but has no entry in `canon_facts.toml` yet, so his dates are an `add_person`. Nowlein's birth year is to verify. "Dall" and "Wilcox" as bare aliases are checked against the registry for collisions before entry (AGENTS.md: keep aliases specific). Ouray's death stays 1880 unless the author changes it; Victorio's has no date because the war that ended it does not happen.

## D. At integration

1. Add section A's entries to `character_registry.json` and their bible sections to `character_bible.md`; apply section B.
2. Add section C to the register entry's `"facts"`; run `cr_facts.py apply CR-071` and `lint_canon.py`.
3. Run `validate_character_docs.py`.
