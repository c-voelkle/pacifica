# CR-071 — Commitments ledger (drafted 17 November 2026; entered at integration)

**Status:** DRAFT for the author. These are the entries CR-071 adds to, changes in or ends in `commitments/data/ledger.toml` (outline, "Before integration", item 4). They are written in the ledger's own TOML so that integration can paste them. **They are not in the ledger yet**, and must not be: the ledger's rule is that every `quote` is copied verbatim from `master_storyline.md`, and CR-071's storyline text is not written (item 2). Each entry below therefore carries a `quote_draft`, the sentence the storyline is expected to say; at integration it becomes `quote` once the storyline's final wording is in, and `ledger.py check` is run.

**Labels.** Every new entry is `status = "PROPOSED"` until the author approves this list; the decisions behind each are cited in `cr` and `open`. Figures are MODEL where marked.

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
  {by = "PAC", to = "HOPI", what = "passage to shrines, eagle grounds, salt and the San Francisco Peaks (HP4); no agent, school or mission placed on the mesas (HP5)"},
]
conditions = [
  "each village signs for itself; Pacifica invents no Hopi government (HP1)",
  "disputes go to a board of one Hopi, one Diné and a judge of the confederal court; raids and killings to that court (HP3)",
  "the line is also an article of the Navajo homeland treaty of 1865 (C-1863-NAVAJO)",
]
status = "PROPOSED"
cr = "CR-071"
section = 12
quote_draft = "The Hopi villages make their own agreement at Santa Fe in 1865, each for itself, and their mesas enter the register as a homeland."
open = "The villages' leaders, Oraibi's year and the line in the villages' own names (I-57) are OPEN."

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
  "the peninsula's nations compacted with the commission in the 1870s (I-56)",
]
status = "PROPOSED"
cr = "CR-071"
section = 13
quote_draft = "A commission on the Northern Commission's model governs Baja from La Paz until 1887."
open = "The commissioners' names are OPEN (I-54)."

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
  "from 1873 includes the leased districts of the San Juan and Gunnison (C-1873-SAN-JUAN-LEASE); from 1878–80 the Front Range districts that vote themselves over",
]
status = "PROPOSED"
cr = "CR-071"
section = 12
quote_draft = "South Park and the upper Arkansas enter as districts under a confederal commission at Fairplay."
open = "The commissioners are not named."

[[commitment]]
id = "C-1873-JP-LOAN"
name = "Japan's loan of 1873 (its San Francisco part)"
kind = "loan"
parties = ["JP", "SANFRANCISCO"]
from = 1873
owes = [
  {by = "JP", to = "SANFRANCISCO", what = "interest and repayment on the part of the 1873 loan placed in San Francisco, with the Bank of California as agent"},
]
conditions = [
  "raised for the commutation of the samurai stipends (CR-071 D, L10)",
]
status = "PROPOSED"
cr = "CR-071"
section = 14
quote_draft = "Part of Japan's loan of 1873 for the samurai stipends is placed in San Francisco."
open = "Amount MODEL and small; rate, term and security not stated (historically a 7% sterling issue in London, to verify). CR-073 expects this entry."

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
  "replaces our timeline's Brunot cession: nothing is ceded (I-68)",
  "the leased districts are county ground from 1887 (I-34)",
]
status = "PROPOSED"
cr = "CR-071"
section = 15
quote_draft = "In 1873 Ouray negotiates the San Juan lease, which gives the miners their districts and roads and keeps the valleys Ute."
open = "Rent and term not stated. The Uncompahgre lease at Roc Creek (C-1881-UTE-LEASE) is separate."

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
  "California and Deseret refuse; their debts pass to the Realm in 1887 (G4)",
  "Oregon, Columbia, Idaho, western Montana, Washoe and New Mexico take it in 1879–80",
]
status = "PROPOSED"
cr = "CR-071"
section = 15
quote_draft = "In 1879 the Confederation assumes the debts of the members that accept its commission."
open = "The debts and the grant per head are MODEL and not yet in the workbook (E2)."

[[commitment]]
id = "C-1879-COMMISSION-ACT"
name = "An Act for the Common Execution of the Laws (the Commission Act)"
kind = "law"
parties = ["PAC", "OR", "COLUMBIA", "IDAHO", "MONTANA", "WASHOE", "NM"]
from = 1879
ended = 1887
ended_by = "the member offices end on 1 August 1887; the Commissioners in office get appointed Senate seats held to sixty-eight (K-11)"
conditions = [
  "each member's chief executive is also Commissioner of the Confederation for his member, confirmed by the Providentor and answering to him for confederal law (E3.1)",
  "member treasurers and auditors examined and posted from outside the member",
  "Hawaii outside the act; California and Deseret refuse it",
]
status = "PROPOSED"
cr = "CR-071"
section = 15
quote_draft = "From 1879 the governors who accept it are also Commissioners of the Confederation; their opponents call it the Collar."

[[commitment]]
id = "C-1882-MILITIA"
name = "The Militia Act"
kind = "law"
parties = ["PAC", "OR", "COLUMBIA", "IDAHO", "MONTANA", "WASHOE", "NM", "DESERET", "CAL"]
from = 1882
conditions = [
  "every member militia placed under the Defense Law before 1887 (E1; Part D, L4)",
  "the Queen's Guard is the Queen's household, not a member militia, and is not caught (E6)",
]
status = "PROPOSED"
cr = "CR-071"
section = 16
quote_draft = "The Militia Act of 1882 places every member militia under the Defense Law."

[[commitment]]
id = "C-1878-PORTNEUF-ROW"
name = "The Portneuf right of way through Fort Hall"
kind = "lease"
parties = ["FORTHALL", "PAC"]
from = 1878
from_approx = true
owes = [
  {by = "FORTHALL", to = "PAC", what = "the railway's right of way down the Portneuf, leased, not sold"},
  {by = "PAC", to = "FORTHALL", what = "a rent the railway pays"},
]
conditions = ["the precedent for every crossing of a homeland (I-65)"]
status = "PROPOSED"
cr = "CR-071"
section = 15
quote_draft = "Fort Hall's council refuses to sell the Portneuf right of way and leases it for a rent the railway pays."
open = "Year: the Salt Lake–Snake line is built in 1881–84 (I-53); 1878 is a placeholder for the council's refusal, to settle."

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
status = "PROPOSED"
cr = "CR-071"
section = 15
quote_draft = "Globe and Clifton are worked on lease inside the Apache country, and Bisbee's copper pays the Chiricahua a royalty."
open = "Years follow our timeline's strikes (Clifton about 1872, Globe 1876, Bisbee 1880) and are placeholders; royalties MODEL."
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
status = "PROPOSED"
cr = "CR-071"
section = 21
quote_draft = "Each homeland of a million acres or more chooses a senator through its own council."
open = "An eighth status in CR-021 G (CT5). Leagues formed in 1888: none assumed. Where a citizen living inside a large homeland is on the Chamber's roll is OPEN (recommended: the neighbouring county's)."

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
status = "PROPOSED"
cr = "CR-071"
section = 25
quote_draft = "A nation may buy back its ceded land from the Land Fund at the price the Fund paid, and after five years at the Office's standard becomes its own trustee."
open = "Year of enactment not settled; 1888 follows the county grades (C-1888-COUNTY-GRADES). Prices, tax years and the standard's measures MODEL (I-67)."
```

---

## B. Changes to existing entries

| Entry | Change | Why |
|---|---|---|
| **C-1865-PROVIDENTOR** | Remove `lapses_on_death = ["CT-ELIAS"]`; add `ended = 1887`, `ended_by = "the Constitution of the Realm, in force on 1 August 1887; the office has no successor and Elias keeps the style only (CR-071 G-1, G-11)"` | G-1: the office ends weeks before his death |
| **C-1887-CONSTITUTION** | Add to `conditions`: "in force on 1 August 1887; ratifications cannot be withdrawn (G1.3)"; "the Senate: 123 county senators (Thalassia chooses none), 12 Polytechnic, 8 aliʻi, the homeland seats (C-1887-COMPACT-LANDS) and appointees held to sixty-eight, up to a quarter of the whole"; "Alaska outside the 124". Add `owes` PAC → CAL: "California a historic land: Spanish entrenched, community property, the Mexican grants as organic law (G6.2)". Add `parties` "CAL", "NATIONS" | G1.3, G3, G6; I-7, I-70 |
| **C-1887-REGENCY** | Add to `conditions`: "the regency article is drafted at Victoria's instance after she strikes the article of Elias's draft that made her Queen of the Realm (December 1886; CR-071 K-19)" | K-19 |
| **C-1865-ENABLING** | `ended_by` add "1 August 1887" | G1.3 |
| **C-1867-BAJA** | `status` PROPOSED → APPROVED; `cr = "CR-071"` | I-61 |
| **C-1863-NAVAJO** | Add to `conditions`: "the line by landmarks, not degrees; the southern line north of Beale's road, with an article reserving the strip for 'a road of wagons or of iron', with compensation (I-63)"; "the Hopi article (C-1865-HOPI)"; "the mountain article for Mount Taylor and the Peaks (I-19)". Replace `open`'s "Boundaries not stated" with "Boundaries as Part I, I4a (about 21,300 sq mi as drawn)" | I-19, I-63, HP3 |
| **C-1865-APACHE** | Add to `conditions`: "the White Mountain country on the line of 1871, given to the Apache from 1865 (I-52)"; "the Chiricahua's country on the line of 1872 (I4a)"; "the Chihenne and Bedonkohe country from the Mimbres to the Gila headwaters and Ojo Caliente (I-66)" | I-52, I-66 |
| **C-1866-UTE** | Add to `conditions`: "the Slope and the Parks: Colorado west of the divide with North and Middle Park, about 32,000 sq mi (I-68)"; `open` add "Ouray at the table with Carson (I-68)" | I-68 |
| **C-1862-LEWISTON-LEASE** | Add to `conditions`: "inside the Nez Perce country on the line of 1855; residents attached to Palouse county for county business (K-22)" | I-47, K-22 |
| **C-1881-UTE-LEASE** | Add to `conditions`: "leased ground in no county (I-68); residents attached to San Juan county for county business (K-22)" | K-22 |
| **C-1866-OR-, WA-, ID-, WASHOE-, MT-, NM-, DESERET-CHARTER** | As Parts F–G, T5: the article of supersession added to `conditions`; `ended = 1887`, `ended_by = "the Constitution of the Realm (CR-071)"` | K-15 |
| **C-1866-WA-CHARTER** | Add T3's terms: the fishing right carried word for word; compacts carried; the works ended as fulfilled; the name kept by the Olympia circuit | K-16 |
| **C-1866-WASHOE-CHARTER** | Add T3's terms: the 1864 compact's terms carried; the tax cap ends, existing mines on the net-proceeds basis until worked out | K-17 |

**One discrepancy found, not CR-071's.** C-1874-ORDINANCES has `ended = 1914`, but canon dates the Act of Settlement that dissolves the Territorial Council to 1907 (CR-040; `canon_facts.toml` act-of-settlement). CR-071 follows 1907 (F–G CT12). The entry's year should be corrected at integration, or by CR-040's own follow-up if `ledger.py check` does not already catch it.

## C. At integration

1. Write the storyline text (item 2), then copy each `quote_draft` as `quote` from the final wording.
2. Paste section A into `commitments/data/ledger.toml` (Part 4 or a new CR-071 part), apply section B, and run `python3 commitments/ledger.py check`.
3. Change `status` to the storyline's label at each quote.
