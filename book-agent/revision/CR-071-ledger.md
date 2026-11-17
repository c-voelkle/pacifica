# CR-071 — Commitments ledger (draft 2, 17 November 2026; entered at integration)

**Status:** DRAFT for the author. These are the entries CR-071 adds to, changes in or ends in `commitments/data/ledger.toml` (outline, "Before integration", item 4). They are written in the ledger's own TOML so that integration can paste them. **They are not in the ledger yet**, and must not be: the ledger's rule is that every `quote` is copied verbatim from `master_storyline.md`, and CR-071's storyline text (`CR-071-storyline.md`, draft 2) is written but not yet integrated. Each entry therefore carries a `quote_draft`, taken word for word from draft 2 of the storyline text. At integration it becomes `quote`, and `ledger.py check` is run.

**Draft 2** follows the fresh-context review against `main` (`CR-071-review-on-main.md`, items 2, 4 and 14) and the storyline text's draft 2:
- every `quote_draft` is now verbatim from the storyline text;
- statuses follow the storyline's labels;
- section numbers are corrected;
- the Baja purchase is split from the Guaymas concession;
- Japan's loan of 1873 is APPROVED, with the Bank of California as the Republic's agent;
- Fort Hall's lease is dated 1881 (renamed C-1881-PORTNEUF-ROW);
- four new entries: the trunk-line charters, Baja's compacts, Salt Lake's charter and the article of supersession's carry-over of Deseret's marriage law (section B, C-1887-CONSTITUTION);
- the ledger quotes that the rewordings of R1 change are listed in section B.

**Checked (17 November 2026, night).** The storyline text was applied to a scratch copy of `main`'s storyline, section A was pasted in and section B's quote changes were made, and then `ledger.py check` was run: 288 commitments, one problem, C-1867-BAJA's status, which section B sets to APPROVED. The scratch copy is not committed.

**Labels.** Each entry's `status` is the storyline's label at its quote: APPROVED where the author approved the decision (cited in `open` or the conditions), PROPOSED where the text is. Figures are MODEL where marked.

**New parties.**

```toml
[[party]]
id = "HOPI"
name = "The Hopi villages (each signing for itself, HP1)"

[[party]]
id = "FORTHALL"
name = "The Shoshone and Bannock of Fort Hall"

[[party]]
id = "NATIONS"
name = "The compact nations of the Realm (the homelands as a class)"

[[party]]
id = "MOUNTAIN"
name = "The Mountain Districts (South Park, the upper Arkansas, the leased San Juan and Gunnison districts, the Front Range districts from 1878–80)"

[[party]]
id = "BAJANATIONS"
name = "The Kumeyaay, Paipai, Kiliwa and Cucapá of Baja"

[[party]]
id = "TRUNKLINES"
name = "The chartered trunk-line companies (the Raton line, the thirty-fifth parallel, the Salt Lake–Snake–Columbia line)"
```

---

## A. New entries

### Before 1887

```toml
[[commitment]]
id = "C-1865-HOPI"
name = "The Hopi agreement (the villages' homeland and the Hopi article of the Navajo treaty)"
kind = "compact"
parties = ["PAC", "HOPI", "NAVAJO"]
from = 1865
owes = [
  {by = "PAC", to = "HOPI", what = "the mesas, fields, springs and grazing entered in the register as the villages' homeland, on a line of named places, with Moenkopi a detached part; no grant or Land Fund sale inside it (HP2, HP6)"},
  {by = "NAVAJO", to = "HOPI", what = "Diné families inside the line stay only by the village's leave (HP3)"},
  {by = "PAC", to = "HOPI", what = "passage to shrines, eagle grounds, salt and the San Francisco Peaks (HP4); no agent, school or mission placed on the mesas unless a village asks (HP5)"},
]
conditions = [
  "each village signs for itself; Pacifica invents no Hopi government (HP1)",
  "First and Second Mesa sign in 1865; Oraibi, with Moenkopi, holds out and signs later (I-57)",
  "disputes go to a board of one Hopi, one Diné and a judge of the confederal court; raids and killings to that court (HP3)",
  "the line is also an article of the Navajo homeland treaty of 1865 (C-1863-NAVAJO)",
]
status = "APPROVED"
cr = "CR-071"
section = 12
quote_draft = "The Hopi villages make their own agreement at Santa Fe in 1865, each for itself."
more_quotes_draft = ["The line between the two homelands is an article of the Navajo treaty too, signed by both."]
open = "HP1–HP7 and I-57 APPROVED. The villages' leaders, the year Oraibi signs and the line in the villages' own names are OPEN."

[[commitment]]
id = "C-1867-BAJA-COMMISSION"
name = "Charter of the Baja commission"
kind = "charter"
parties = ["PAC"]
from = 1867
ended = 1887
ended_by = "the Constitution of the Realm: Baja's two counties replace the commission (CR-071 I-39)"
conditions = [
  "three commissioners appointed by the Council, seated at La Paz (I-54)",
  "a charter copied from the Northern Commission's, with Spanish as a working language (I-54)",
  "the peninsula's nations compacted with the commission in the 1870s (C-1870-BAJA-COMPACTS)",
]
status = "APPROVED"
cr = "CR-071"
section = 13
quote_draft = "Baja is governed from La Paz by a commission chartered by the confederal chambers, three commissioners with Spanish as a working language, until 1887."
open = "I-39, I-54 APPROVED. The commissioners' names are OPEN."

[[commitment]]
id = "C-1870-BAJA-COMPACTS"
name = "The Baja commission's compacts with the Kumeyaay, Paipai, Kiliwa and Cucapá"
kind = "compact"
parties = ["PAC", "BAJANATIONS"]
from = 1870
from_approx = true
owes = [
  {by = "PAC", to = "BAJANATIONS", what = "homelands in their sierras and the delta: the Kumeyaay in the Sierra Juárez, the Paipai at Santa Catarina, the Kiliwa in the San Pedro Mártir, the Cucapá in the delta inside Yuma (I-55, I-56)"},
]
conditions = [
  "made by the Baja commission (C-1867-BAJA-COMMISSION); carried by the Realm from 1887 as compact lands (C-1887-COMPACT-LANDS)",
  "all four are enclaves inside a county's lines (I-72)",
]
status = "APPROVED"
cr = "CR-071"
section = 13
quote_draft = "In the 1870s it makes compacts with the Kumeyaay, Paipai, Kiliwa and Cucapá for homelands in their sierras and the delta."
open = "I-56 APPROVED. Years of each compact not stated. The Cochimí have no homeland unless research shows that enough survived the missions (OPEN)."

[[commitment]]
id = "C-1867-MOUNTAIN-DISTRICTS"
name = "The Mountain Districts' commission"
kind = "charter"
parties = ["PAC", "MOUNTAIN"]
from = 1867
ended = 1887
ended_by = "the Constitution of the Realm: the districts become county ground (CR-071 outline A-1; I-68)"
conditions = [
  "a confederal commission seated at Fairplay, at Leadville from 1879",
  "each district keeps its own miners' code and enters as a district (CR-060 CO7)",
  "from 1873 includes the leased districts of the San Juan and Gunnison (C-1873-SAN-JUAN-LEASE); from 1878–80 the Front Range districts that vote themselves over (§19, CR-060)",
]
status = "APPROVED"
cr = "CR-071"
section = 12
quote_draft = "South Park and the upper Arkansas are governed as districts under a confederal commission at Fairplay, each with its own miners' code, and the districts that later vote themselves over join it."
more_quotes_draft = ["The leased districts of the San Juan and Gunnison join the Mountain Districts' commission, which moves to the new silver town of Leadville in 1879."]
open = "A-1 APPROVED. The commissioners are not named."

[[commitment]]
id = "C-1873-JP-LOAN"
name = "Japan's loan of 1873 (its San Francisco part)"
kind = "loan"
parties = ["JP", "PAC", "SANFRANCISCO"]
from = 1873
owes = [
  {by = "JP", to = "PAC", what = "interest and repayment on the Republic's share of the part placed in San Francisco"},
  {by = "JP", to = "SANFRANCISCO", what = "interest and repayment on the houses' share, Japan's bank being the Bank of California (CR-073 E2, the 1867 precedent)"},
]
conditions = [
  "raised for the commutation of the samurai stipends (CR-071 D, L10)",
  "The Bank of California is the Republic's agent for the loan (CR-073 R10, APPROVED).",
]
status = "APPROVED"
cr = "CR-071"
section = 14
quote_draft = "In 1873 part of Japan's loan for the samurai stipends is placed in San Francisco, with the Bank of California as the Republic's agent."
open = "L10 and decision 6 APPROVED; CR-073 R10 APPROVED. Amount MODEL and small; the split between the Republic's and the houses' shares, rate, term and security not stated (historically a 7% sterling issue in London, to verify)."

[[commitment]]
id = "C-1873-SAN-JUAN-LEASE"
name = "The San Juan lease (Ouray's lease of the mining districts and roads)"
kind = "lease"
parties = ["UTE", "PAC"]
from = 1873
owes = [
  {by = "UTE", to = "PAC", what = "the San Juan mineral belt (Silverton, Ouray, Telluride, Rico) and the Gunnison districts, with their railway and roads, on lease through the Confederation"},
  {by = "PAC", to = "UTE", what = "the rent, paid to the nation; the valleys stay Ute"},
]
conditions = [
  "nothing is ceded (I-68)",
  "the leased districts join the Mountain Districts' commission; they are county ground from 1887 (I-34)",
]
status = "APPROVED"
cr = "CR-071"
section = 13
quote_draft = "In 1873 Ouray negotiates the San Juan lease, which gives the miners their districts and roads and keeps the valleys Ute."
open = "I-68 APPROVED. Rent and term not stated. The Uncompahgre lease at Roc Creek (C-1881-UTE-LEASE) is separate."

[[commitment]]
id = "C-1872-APACHE-MINING-LEASES"
name = "Mining leases in the Apache and Chiricahua countries (Globe, Clifton, Bisbee)"
kind = "lease"
parties = ["APACHE", "PAC"]
from = 1872
from_approx = true
owes = [
  {by = "APACHE", to = "PAC", what = "the Globe and Clifton districts inside the White Mountain line, and Bisbee's copper inside the Chiricahua line, on lease"},
  {by = "PAC", to = "APACHE", what = "a royalty to each nation, as Santa Rita pays the Chihenne (C-1865-SANTA-RITA)"},
]
conditions = [
  "leased ground in no county; its residents attached to the neighbouring county for county business (K-22)",
  "Tombstone lies outside the Chiricahua line and is county ground (I-62)",
]
status = "APPROVED"
cr = "CR-071"
section = 13
quote_draft = "Globe and Clifton are worked on lease inside the Apache country, and Bisbee's copper pays the Chiricahua a royalty."
open = "I-52 and I-62 APPROVED. Years follow our timeline's strikes (Clifton about 1872, Globe 1876, Bisbee 1880) and are placeholders; royalties MODEL."

[[commitment]]
id = "C-1879-TRUNK-CHARTERS"
name = "The trunk-line charters on Land Fund grants"
kind = "charter"
parties = ["PAC", "TRUNKLINES"]
from = 1878
from_approx = true
owes = [
  {by = "PAC", to = "TRUNKLINES", what = "Land Fund grants, ten sections to the mile, in land and not in cash; no grant from a homeland (I-53; outline C5)"},
  {by = "TRUNKLINES", to = "PAC", what = "the lines built: the Raton line to Las Vegas in 1879, the thirty-fifth parallel to the Colorado in 1880–83, the Salt Lake–Snake–Columbia line in 1881–84"},
]
conditions = [
  "chartered by the confederal chambers, not by the members",
  "where a line crosses a homeland the right of way is leased from the nation (C-1881-PORTNEUF-ROW)",
  "the state holds the trunk rights of way (CR-057)",
]
status = "APPROVED"
cr = "CR-071"
section = 13
quote_draft = "The trunk lines are chartered by the confederal chambers on Land Fund grants: the Raton line reaches Las Vegas in 1879, the thirty-fifth-parallel line crosses to the Colorado in 1880–83, and the Salt Lake–Snake–Columbia line is built in 1881–84."
open = "I-53 APPROVED. The companies' names and the grants' acreage are MODEL or OPEN."

[[commitment]]
id = "C-1879-ASSUMPTION"
name = "The Assumption Act"
kind = "law"
parties = ["PAC", "OR", "COLUMBIA", "IDAHO", "MONTANA", "WASHOE", "NM"]
from = 1879
owes = [
  {by = "PAC", to = "OR", what = "the member's debt assumed and its paper guaranteed, with a grant per head; likewise for each member that takes it"},
]
conditions = [
  "offered with the Commission Act; a member takes both or neither (E-3)",
  "the member's treasury audited by the Polytechnic",
  "California and Deseret refuse; their debts pass to the Realm in 1887 (G4)",
  "Oregon, Columbia, Idaho, western Montana, Washoe and New Mexico take it in 1879–80",
]
status = "APPROVED"
cr = "CR-071"
section = 19
quote_draft = "A member that takes them has its debt assumed and its paper guaranteed, and its treasury is audited by the Polytechnic."
more_quotes_draft = ["Oregon, Columbia, Idaho, western Montana, Washoe and New Mexico take it in 1879–80."]
open = "E-3 APPROVED. The debts and the grant per head are MODEL and not yet in the workbook (E2)."

[[commitment]]
id = "C-1879-COMMISSION-ACT"
name = "An Act for the Common Execution of the Laws (the Commission Act)"
kind = "law"
parties = ["PAC", "OR", "COLUMBIA", "IDAHO", "MONTANA", "WASHOE", "NM"]
from = 1879
ended = 1887
ended_by = "the member offices end on 1 August 1887; the Commissioners of the Confederation then in office, and Pacheco, get appointed Senate seats held to sixty-eight (K-11)"
conditions = [
  "each member's chief executive, still elected, is also Commissioner of the Confederation for his member, commissioned by the Providentor in person at Monterey and answering to him for confederal law (E3.1)",
  "member treasurers and auditors examined and posted from outside the member",
  "Hawaii outside the act; California and Deseret refuse it",
]
status = "APPROVED"
cr = "CR-071"
section = 19
quote_draft = "Its governor, still elected, accepts a confederal commission as Commissioner of the Confederation and answers to the Providentor for the common law; each receives his commission from Elias in person at Monterey."
more_quotes_draft = ["The Committee party's papers call it the Collar, and the *Deseret News* takes up the name."]
open = "E3.1, K-11 APPROVED."

[[commitment]]
id = "C-1882-MILITIA"
name = "The Militia Act"
kind = "law"
parties = ["PAC", "OR", "COLUMBIA", "IDAHO", "MONTANA", "WASHOE", "NM", "DESERET", "CAL"]
from = 1882
conditions = [
  "every member militia a reserve of the common army, under the Defense Law before 1887 (E1; Part D, L4)",
  "every commission examined by a board chaired by Sherman, the regulars' and the Auxiliary's with the militias' (E-12, K-2)",
  "the officers who fail kept together as the inland command (E-13)",
  "the Queen's Guard is the Queen's household, not a member militia, and is not caught (E6)",
]
status = "APPROVED"
cr = "CR-071"
section = 19
quote_draft = "The Militia Act of 1882 makes every member militia a reserve of the common army, its officers commissioned by the Confederation and its arms kept in confederal arsenals."
open = "E-1, E-12 (confirmed by the author, 17 November 2026, 23:03) and E-13 APPROVED."

[[commitment]]
id = "C-1881-PORTNEUF-ROW"
name = "The Portneuf right of way through Fort Hall"
kind = "lease"
parties = ["FORTHALL", "PAC"]
from = 1881
owes = [
  {by = "FORTHALL", to = "PAC", what = "the railway's right of way down the Portneuf, leased, not sold"},
  {by = "PAC", to = "FORTHALL", what = "a rent the railway pays"},
]
conditions = ["the precedent for every later crossing of a homeland (I-65)"]
status = "APPROVED"
cr = "CR-071"
section = 13
quote_draft = "In 1881, when the Snake line reaches the reservation, Fort Hall's council refuses to sell the Portneuf right of way and leases it for a rent the railway pays, as every later crossing of a homeland does."
open = "I-65 APPROVED. The year follows the Snake line's (I-53, 1881–84), a story assumption. Rent and term not stated."
```

### From 1887

```toml
[[commitment]]
id = "C-1887-COMPACT-LANDS"
name = "The compact lands under the Constitution of the Realm"
kind = "guarantee"
parties = ["PAC", "NATIONS", "COUNTIES"]
from = 1887
owes = [
  {by = "PAC", to = "NATIONS", what = "the homelands' compacts carried as the Realm's own; a homeland's line, powers and grade are not organic law and change only by compact (I-8; CR-033 A22)"},
  {by = "PAC", to = "NATIONS", what = "one senator for each homeland of a million acres or more, chosen by its own council; one for each league of enclaves that reaches that size (I-70 to I-72)"},
  {by = "PAC", to = "NATIONS", what = "citizenship for a nation's member by registration, without the English test (K-24)"},
  {by = "COUNTIES", to = "NATIONS", what = "a county's board, taxes and courts stop at an enclave's line unless the nation contracts for a service (I4)"},
]
conditions = [
  "a homeland of a million acres or more stands outside the 124 counties; a smaller one is an enclave inside a county's lines beyond its board's reach (I-72)",
  "a member of a nation who lives in a county registers and votes there, and only there (I-9)",
  "residents of leased ground in no county are attached to the neighbouring county for schools, roads, police and the Chamber's roll; the county taxes improvements, not land (K-22)",
  "Alaska's nations choose one senator; Alaska stays under the Northern Commission outside the 124 (I-7, I-32)",
]
can_end = [{who = "NATIONS", how = "a compact changes only with the consent of the nation affected and the Realm"}]
status = "APPROVED"
cr = "CR-071"
section = 21
quote_draft = "Each homeland of a million acres or more chooses one through its own council, as does each league of smaller homelands that reaches that size, and Alaska's nations choose one."
more_quotes_draft = ["Their compacts run to the Realm and change only with the nation's consent.", "A member of a nation becomes a citizen by entering himself on the register, and votes where he lives; those who live on leased ground in no county are on the roll of the county beside it."]
open = "I-7 to I-9, I-70 to I-72, K-22, K-24 APPROVED. An eighth status in CR-021 G (CT5). Leagues formed in 1888: none assumed."

[[commitment]]
id = "C-1888-NATIONS-LADDER"
name = "The nations' ladder (land bought back and the chartered nation)"
kind = "law"
parties = ["PAC", "NATIONS", "COUNTIES"]
from = 1888
from_approx = true
owes = [
  {by = "PAC", to = "NATIONS", what = "first refusal on a nation's own ceded land still in the Land Fund, at the price the Fund paid; additions to a homeland by supplementary compact"},
  {by = "PAC", to = "COUNTIES", what = "the land tax lost to a homeland's addition, paid for ten years from the Land Fund's margin"},
  {by = "PAC", to = "NATIONS", what = "for a chartered nation (five years at the Office's standard): its own trusteeship and the lease fee, a patrimony on the Patrimony's rules, chartered companies and home borrowing with Treasury consent, a court of first instance and police, and its language certified for the tongue vote"},
]
conditions = [
  "an enclave that grows past a million acres leaves its county and chooses its own senator (I-72)",
  "the leak of CR-033 A23 still runs; the Office publishes both columns for every nation",
]
status = "APPROVED"
cr = "CR-071"
section = 25
quote_draft = "A nation may buy back its ceded land still in the Land Fund at the price the Fund paid for it."
more_quotes_draft = ["A nation whose accounts and services meet the Office's standard for five years becomes chartered."]
open = "K-25 APPROVED. The year of the law and which nations climb first are OPEN; 1888 follows the county grades (C-1888-COUNTY-GRADES) as the earliest start. Prices, tax years and the standard's measures MODEL (I-67)."

[[commitment]]
id = "C-1894-SALT-LAKE-CHARTER"
name = "Salt Lake's county charter (the first chartered county)"
kind = "charter"
parties = ["PAC", "COUNTIES"]
from = 1894
conditions = [
  "Salt Lake qualifies in 1893, after five years at the Office's four standards (C-1888-COUNTY-GRADES)",
  "the charter waits a year on the inspectors' test that no congregation may capture a county (CR-037)",
  "the Church's men on the board resign their Church offices to keep it (J2)",
]
status = "APPROVED"
cr = "CR-071"
section = 25
quote_draft = "Salt Lake is chartered in 1894."
more_quotes_draft = ["Salt Lake is the first county to qualify for a charter, in 1893; the people most suspicious of the centre top its tables."]
open = "J2 and CT7 APPROVED. Salt Lake is a county, not a Crown city (§22)."
```

---

## B. Changes to existing entries

| Entry | Change | Why |
|---|---|---|
| **C-1865-PROVIDENTOR** | Remove `lapses_on_death = ["CT-ELIAS"]`; add `ended = 1887`, `ended_by = "the Constitution of the Realm, in force on 1 August 1887; the office has no successor and Elias keeps the style only (CR-071 G-1, G-11)"`. In `more_quotes`, replace "The Providentorship lasts for Elias's life." with "The Providentorship is Elias's alone; it ends with the regency on 1 August 1887, weeks before his death, and neither a later regent nor a county inherits his power." | G-1; storyline A row 1 |
| **C-1865-ENABLING** | `ended_by` add "1 August 1887". In `more_quotes`, replace "Its enabling delegation lapses when the regency begins in 1887; neither a later regent nor a county inherits his power." with the same new sentence. | G1.3; storyline A row 1 |
| **C-1887-TRUCE** | In `more_quotes`, replace "The negotiated pact takes effect; the empire consolidates without a succession war." with "The negotiated pact holds; the empire consolidates without a succession war." | storyline A row 6 |
| **C-1914-ACT-OF-SETTLEMENT** | In `more_quotes`, replace "until 1914 restores Hawaiian-medium education and the Crown's Hawaiian oath and proclamation." with "until 1907 restores …". The entry's ID stays, since stable IDs are not renamed; its name already says 1907. | storyline A row 11; CR-040 |
| **C-1866-UTE**, **C-1863-SHOSHONE-BRIDGER** | In each entry's quotes, replace "The Ute leaders and terms, and Washakie's agreement." with "The other Ute leaders and terms, and Washakie's agreement." (the storyline's §12 OPEN marker is reworded once Ouray is named) | storyline B, §12 l. 603 |
| **C-1874-ORDINANCES** | `ended = 1914` → `ended = 1907` (the Act of Settlement dissolves the Territorial Council; CR-040, `canon_facts.toml` act-of-settlement) | CR-040; F–G CT12 |
| **C-1887-CONSTITUTION** | Add to `conditions`: "in force on 1 August 1887; ratifications cannot be withdrawn (G1.3)"; "the Senate: one senator for each county with a board (Thalassia chooses none), 12 Polytechnic, 8 aliʻi, the homeland seats (C-1887-COMPACT-LANDS) and appointees held to sixty-eight, up to a quarter of the whole"; "Alaska outside the 124"; **"Deseret's marriage and church-property law carried over to persons: a marriage made in the form of a religious community registered with the Realm is valid in every county and church property is held as corporate property, for every registered church, under the Realm's floors (CR-072 P16; CR-071 T3)"**. Add `owes` PAC → CAL: "California a historic land: Spanish entrenched, community property, the Mexican grants as organic law (G6.2)". Add `parties` "CAL", "NATIONS". Add to `more_quotes`: "The Constitution carries the protection over to persons." (CR-072's, already in the storyline) and "Every charter of 1866 carries Elias's article of supersession, so the Constitution enters into force on 1 August 1887 whatever Salt Lake does." | G1.3, G3, G6; I-7, I-70; T3 (the carry-over CR-072 left to CR-071) |
| **C-1887-REGENCY** | Add to `conditions`: "the regency article is drafted at Victoria's instance after she strikes the article of Elias's draft that made her Queen of the Realm (December 1886; CR-071 K-19)" | K-19 |
| **C-1867-BAJA** | **Split.** Rename it "Baja purchase". Remove the Guaymas `owes` line. Set `status = "APPROVED"`, `cr = "CR-071"` and `quote = "As France withdraws, a Baja purchase in 1867, paid over five years, secures the southern flank."`; `more_quotes` stays ("Mexico retains Sonora. Prices, garrisons and firms await audit."); `open` = "term_years is the payment period; the last instalment year and the price are not stated (I-61 APPROVED)." | I-61; review item 4 |
| **C-1867-GUAYMAS** (new, from the split) | `name = "Guaymas railway concession and free port"`, `kind = "concession"`, `parties = ["MX", "PAC"]`, `from = 1867`, `owes = [{ by = "MX", to = "PAC", what = "a Guaymas railway concession and free port" }]`, `status = "PROPOSED"`, `section = 13`, `quote = "A Guaymas railway concession and free port go with it."`, `open = "The year and term of the concession and free port are not stated; CR-057: Guaymas waits on Mexico."` | review item 4 |
| **C-1863-NAVAJO** | Add to `conditions`: "the line by landmarks, not degrees; the southern line north of Beale's road, with an article reserving the strip for 'a road of wagons or of iron', with compensation (I-63)"; "the Hopi article (C-1865-HOPI)"; "the mountain article for Mount Taylor and the Peaks (I-19)". Replace `open`'s "Boundaries not stated" with "Boundaries as Part I, I4a (about 21,300 sq mi as drawn)". Add `more_quotes`: "Barboncito will not have degrees." | I-19, I-63, HP3 |
| **C-1865-APACHE** | Add to `conditions`: "the White Mountain country on the line of 1871, given to the Apache from 1865 (CR-071 I-52, APPROVED)"; "the Chiricahua's country on the line of 1872 (I4a, APPROVED)"; "the Chihenne and Bedonkohe country from the Mimbres to the Gila headwaters and Ojo Caliente (I-66, APPROVED)". `status` stays PROPOSED: the peace as a whole is PROPOSED in canon. Add to `open`: "the countries are APPROVED by CR-071 (storyline: 'The peace gives each people its own country')". | I-52, I-66; review item 11 |
| **C-1866-UTE** | Add to `conditions`: "the Slope and the Parks: Colorado west of the divide with North and Middle Park, about 32,000 sq mi (I-68)". Add `more_quotes`: "Ouray, who grew up at Taos speaking Spanish, comes to the table with Carson." | I-68 |
| **C-1862-LEWISTON-LEASE** | Add to `conditions`: "inside the Nez Perce country on the line of 1855; residents attached to Palouse county for county business (K-22)" | I-47, K-22 |
| **C-1881-UTE-LEASE** | Add to `conditions`: "leased ground in no county (I-68); residents attached to San Juan county for county business (K-22)" | K-22 |
| **C-1866-NM-CHARTER** | Add to `conditions`: "east of Glorieta, San Miguel and Mora adhere by conventions elected on the old franchise in October 1867, Mora narrowly once the Confederation keeps Fort Union and takes over its forage contracts; any resident may declare for the Union within a year and keep his property (A-3)". Add `more_quotes`: "In October 1867 San Miguel and Mora elect conventions on the old franchise to vote on the compact and the charter." | A-3; review item 14 |
| **C-1866-OR-, WA-, ID-, WASHOE-, MT-, NM-, DESERET-CHARTER** | As Parts F–G, T5: add the article of supersession to `conditions`; set `ended = 1887` and `ended_by = "the Constitution of the Realm (CR-071)"`. Add to C-1866-OR-CHARTER's `more_quotes`: "Elias has the charter say what can touch it: a constitution adopted as the Articles are amended, which must carry its protections over or end them with the power they rest on." | K-15 |
| **C-1866-WA-CHARTER** | Add T3's terms: the fishing right carried word for word; compacts carried; the works ended as fulfilled; the name kept by the Olympia circuit | K-16 |
| **C-1866-WASHOE-CHARTER** | Add T3's terms: the 1864 compact's terms carried; the tax cap ends, existing mines on the net-proceeds basis until worked out | K-17 |
| **C-1866-DESERET-CHARTER** | Add T3's terms to `conditions`: "1887: the marriage and church-property law carried as a personal guarantee for every registered church (C-1887-CONSTITUTION; CR-072 P16, CT10); the Nauvoo Legion's place within the Defense Law already common (E1)". Add `more_quotes`: "Deseret's acceptance, after Taylor's death, is its legislature's last act, and Cannon's telegram reaches Thalassia two days before the handover." | T3; the carry-over CR-072 left to CR-071 |
| **CT-RALSTON's entries** | None changes: S7 goes into the registry (CR-071-registry.md); "Ralston brings the San Francisco houses to give their word for it; the Patrimony spends nothing." is not a commitment | — |

## C. At integration

1. Write the storyline text (`CR-071-storyline.md`, draft 2) into `master_storyline.md`. Copy each `quote_draft` as `quote`, and each `more_quotes_draft` as `more_quotes`, checking them against the final wording.
2. Paste section A into `commitments/data/ledger.toml` (Part 4 or a new CR-071 part), apply section B, and run `python3 commitments/ledger.py check`.
3. If the storyline's label at a quote has changed in the final wording, change `status` to match.
