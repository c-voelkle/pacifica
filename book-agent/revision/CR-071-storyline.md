# CR-071 — Storyline text (draft 3, 18 November 2026)

**Status:** DRAFT for the author (outline, "Before integration", item 2). This is the text to be written into `master_storyline.md` at integration. CR-072 and CR-073 are now on `main` (PR #74, merged into this branch), so the anchors quote the storyline and give its line numbers as of `main` at 586ca26. Labels are those the text will carry in the storyline:
- **[APPROVED — CR-071]** where the author has approved the decision;
- **[PROPOSED — CR-071]** for details inside it;
- **[OPEN]** for what is not decided.

Comparisons with our timeline stay out of the prose; they are in the parts and go to `historical_background.md`. Each block names its source decisions in a hidden coverage comment, as the storyline does. Where a block is inserted inside a canon paragraph, the label of the canon text that follows it is repeated, so that no canon sentence falls under CR-071's label.

**Draft 3** (18 November 2026) adds Part H's settler bargain (H6–H7, approved by the author on 18 November with the revisions of 06:27 and 06:36):
- the Feather River case in place of Rock Springs and Hells Canyon;
- the labour article;
- the convention that each people is kept in order by its own;
- Silas's oath at Sacramento;
- the trades and the soldiers in the Party;
- the Pacific Companies' first generation (dates APPROVED, details PROPOSED pending CR-074);
- the labour law and the Companies Act of 1888;
- "the slack years after 1873" (E-2a).

**Draft 2** applied the fresh-context review against `main` of 17 November 2026 (`CR-071-review-on-main.md`) and the author's decision of 23:03 that Sherman chairs the board of 1882 (E-12, confirmed). It makes these changes:
- the ratification is told once, after CR-072's paragraph;
- Salt Lake is no longer "ordinary";
- the Baja purchase is split from Guaymas;
- the §19 and §25 blocks are put in order with CR-072's text, and the grant machinery is moved to §12;
- the Mountain Districts sentence is corrected, and the 1880 survey is commissioned by the Superintendency;
- labels are fixed;
- the §14 and §5 blocks are placed in reading order;
- Sherman's refusal of 1884 (E-14) and the article of supersession in 1866 (K-15, T4), approved but not yet written, are added.

**Fact changes.** The text states the fifteen tracked facts of the outline's `## Fact changes` in the wording their patterns catch (checked with `cr_facts.py preview`).

---

## A. Rewordings of current canon (section R1)

| # | Where (main, 586ca26) | Now | Becomes |
|---|---|---|---|
| 1 | §12, l. 572 | "The Providentorship lasts for Elias's life. Its enabling delegation lapses when the regency begins in 1887; neither a later regent nor a county inherits his power." | "The Providentorship is Elias's alone; it ends with the regency on 1 August 1887, weeks before his death, and neither a later regent nor a county inherits his power." Both ledger quotes change with it (ledger draft, B). |
| 2 | §21, l. 827 | "Elias's life office ends with him." | "Elias's life office has no successor; he lays it down when the regency begins." |
| 3 | §13, l. 631 | "As France withdraws, a Baja purchase in 1867, paid over five years, a Guaymas railway concession and free port secure the southern flank. Mexico retains Sonora." | "**[APPROVED — CR-071]** As France withdraws, a Baja purchase in 1867, paid over five years, secures the southern flank. **[PROPOSED]** A Guaymas railway concession and free port go with it. Mexico retains Sonora." "Prices, garrisons and firms await audit" stays. The Guaymas clause keeps its PROPOSED label (CR-057: "Guaymas waits on Mexico"); the ledger entry is split the same way. |
| 4 | §19, l. 777 (CR-072) | "**[PROPOSED — CR-072]** Soberanes, back from Vladivostok, sees what the Party is …" | "**[PROPOSED — CR-072]** Soberanes sees what the Party is …". He has just come back in CR-071's memorandum paragraph, which now precedes this one. |
| 5 | §14, l. 671 (CR-072) | "Kido Takayoshi, who governs by rescript, watches …" | "Kido, who governs by rescript, watches …". CR-071's block before it introduces him by his full name. |
| 6 | §21, l. 838 | "The negotiated pact takes effect; the empire consolidates without a succession war." | "The negotiated pact holds; the empire consolidates without a succession war." The ledger quote in C-1887-TRUCE changes with it. |
| 7 | §22, l. 848 | "Victoria’s standing combines the founder’s widowhood, …" (curly apostrophes on `main`) | "Victoria’s standing combines her marriage to the founder, and from August his widowhood, …" |
| 8 | §22, l. 850 | "Portland, Seattle and Salt Lake remain ordinary counties, with the Church steering a coherent Deseret Senate bloc." | "Portland, Seattle and Salt Lake remain counties, not Crown cities, with the Church steering a coherent Deseret Senate bloc." This is CT7 (APPROVED, 17 November, 13:14), here in the storyline as in CR-021. |
| 9 | §22, l. 848 | Sherman's sentence after "Sherman supports constitutional military allegiance rather than personal rule." | as given below the table |
| 10 | §23, l. 856 | "As natural guardian she could claim a regency;" | "As natural guardian she could contest the regency;" |
| 11 | §25, l. 910 | "until 1914 restores Hawaiian-medium education" | "until 1907 restores Hawaiian-medium education". A leftover of CR-040, which dates the Act of Settlement to 1907 (§26); the ledger quote in C-1914-ACT-OF-SETTLEMENT changes with it. |

**Row 9 in full.** On `main`, Sherman's sentence in §22 reads: "His proposed June 1884 refusal of political power and February 1891 death remain working uses of his historical chronology." It becomes: "**[APPROVED — CR-071]** Sherman refused the state in June 1884. **[PROPOSED]** Sherman's death in February 1891 remains a working use of his historical chronology." Sherman's refusal is now told in §19 (E-14).

| 12 | §15, l. 703 | "Rock Springs in 1885 and Hells Canyon in 1887 occur on Pacifican soil and receive prompt prosecution." | removed; the paragraph ends with the new sentence in B (§15) |
| 13 | §20, l. 931 | "Union critics answer with the Chinese massacres," | "Union critics answer with the Feather River," |
| 14 | §25, l. 914 | "In 1888 selective skilled and sponsored-family immigration replaces the open door." | "In 1888 selective skilled and sponsored-family immigration replaces the open door, as the labour article promised: the Realm admits labour by examination, sponsorship or guest contract, never on a broker's debt." |

CR-021's own passages (R1 items 8–13 of Parts F–G) are amended in `CR-021.md` at integration, not here.

**Order of canon paragraphs.** The storyline draft moves two canon paragraphs; neither changes its words except as in rows 4 and 5.
- **§19:** CR-022's l. 775 ("The examinations reach the officer corps in mid-career …") moves to after CR-072's l. 777, so that the order runs memorandum and Collar (1878–80), the Party taken by the examined (about 1880), the examinations in the officer corps, the Militia Act (1882), and the survey (1880–86).
- **§14:** the last sentence of l. 669, "The Iwakura Mission's San Francisco landfall in 1872 puts Japan's officials inside this industrial world.", becomes its own paragraph after CR-071's 1871 block.

---

## B. New text, in storyline order

### §5, l. 218: split the paragraph after "…without changing their working language." and insert (K-18)

> <!-- CR-071: the capital at Sacramento --> **[APPROVED — CR-071]** The legislature moves to Sacramento in December 1849, to the gateway of the registered gravels, and sits there through the flood of January 1850. Monterey, the republic's first capital, keeps the courts, and in 1856 the Confederation makes it its seat.

The rest of l. 218, from "The election of 1850 strengthens merchants …", follows as its own paragraph, unlabelled as before. The squatters' quarrel at Sacramento comes in that paragraph, in August, so the block no longer mentions it.

### §5, l. 238: after "…without making them subordinate to Elias." (H7.8)

> <!-- CR-071: the venture licence --> **[APPROVED — CR-071]** In 1854 the Republic answers Walker with a law of its own: no one may make war abroad from its soil, and a venture abroad needs the Republic's licence and bond. **[PROPOSED — CR-071]** Sealers, whalers, guano men and traders take out the first licences.

### §12, after l. 568 ("…legally hollowing out the states.") and before CR-072's l. 570 (C1)

> <!-- CR-071: the grant machinery --> **[APPROVED — CR-071]** The grants come with terms. A county board petitions the Superintendency for a water grant, a railway subsidy or Development Fund credit; it signs away the works' accounts to confederal audit, their route to confederal consent, any member tax on them and its own forum to the Confederal Court, and it gets money no member could give it. The accounts are published each year beside the next county's. By 1871 most interior boards spend more confederal money than member money, and their supervisors look to Monterey. Nothing is taken from the members; everything new goes round them.

### §12, after l. 582 ("**[PROPOSED — CR-060]** In the Rockies the line follows what each side can hold …") (A-1, I-68)

> <!-- CR-071: the Utes' alliance and the Mountain Districts --> **[APPROVED — CR-071]** The Utes come to the peace having earned their terms. Ute guides led the column up the San Luis Valley in 1863, and through the winters of 1863–65 the Ute bands held the passes against the Union's Colorado volunteers. The mountain districts never become a member. South Park and the upper Arkansas are governed as districts under a confederal commission at Fairplay, each with its own miners' code, and the districts that later vote themselves over join it. **[OPEN]** Whether the massacre at Sand Creek happens.

### §12, l. 585: after "…No Navajo walks to the Pecos." insert (I-63, HP1–HP7, I-57)

> <!-- CR-071: the Diné line and the Hopi --> **[APPROVED — CR-071]** Barboncito will not have degrees. The treaty draws the homeland by landmarks: the Puerco of the West, named springs and Ojo del Oso. Its southern line runs north of Beale's wagon road, and an article reserves the strip along the road for a road of wagons or of iron, with compensation. A mountain article keeps the summits of Mount Taylor and the San Francisco Peaks inside the line. The Hopi villages make their own agreement at Santa Fe in 1865, each for itself. Their mesas enter the register as a homeland inside the Diné country, with Moenkopi apart, and no agent, school or mission goes onto them unless a village asks. The line between the two homelands is an article of the Navajo treaty too, signed by both. Oraibi, with its farming village at Moenkopi, holds out and signs later. **[OPEN]** The villages' leaders and the year Oraibi signs.

The canon text that follows takes its label again: "**[APPROVED — CR-061]** East of the armistice line at Glorieta …".

### §12, l. 585: before "Mangas dies in his own country …" insert (I-52, I-66)

> **[APPROVED — CR-071]** The peace gives each people its own country: the White Mountain country to its bands, the Chiricahua mountains and valleys to the Sonora line to Cochise's people, and to the Chihenne and Bedonkohe the country from the Mimbres to the Gila's headwaters and Ojo Caliente. No settler has to be moved off any of it. **[APPROVED — CR-061]**

The sentence about Mangas follows under the label repeated at the end of the block. In canon the Apache peace stays **[PROPOSED]** as a whole, with its scouts, agents and convention; the countries are the part the author has approved (I-52: "given to Apache country from 1865"). The ledger marks the same split.

### §12, l. 600: after "…calls it a charter no cabinet can touch." insert (K-15; F–G T1, T4)

> <!-- CR-071: the article of supersession --> **[APPROVED — CR-071]** Elias has the charter say what can touch it: a constitution adopted as the Articles are amended, which must carry its protections over or end them with the power they rest on. Every charter of 1866 carries the same article. **[PROPOSED — CR-059]**

The canon text that follows ("The charter's Native article …") keeps CR-059's label through the repeated tag. F–G T4 had this sentence as PROPOSED; K-15 (APPROVED, 16 November) makes the article canon, so it carries the approved label. The ratification block in §21 relies on it.

### §12, l. 603: replace "**[OPEN]** The Ute leaders and terms, and Washakie's agreement." with (I-68)

> **[APPROVED — CR-071]** Ouray, who grew up at Taos speaking Spanish, comes to the table with Carson. The Utes keep Colorado west of the divide, with North and Middle Park. **[OPEN]** The other Ute leaders and terms, and Washakie's agreement.

### §12, after l. 615 ("**[PROPOSED — CR-061]** Until the exchange the armistice line at Glorieta holds …") (A-3)

> <!-- CR-071: San Miguel and Mora adhere --> **[APPROVED — CR-071]** The land east of Glorieta passes by the treaty, and for a year any resident may declare for the Union and keep his property. In October 1867 San Miguel and Mora elect conventions on the old franchise to vote on the compact and the charter. Las Vegas adheres by a wide margin. Mora has been fed for five years by Fort Union's forage contracts, and adheres narrowly once the Confederation keeps the fort and takes over the contracts. Manuel Chaves, who led the Union's New Mexicans against the carretas, speaks against at Las Vegas and stays.

### §13, after l. 631 (the whole paragraph, ending "…Prices, garrisons and firms await audit.") (I-39, I-54, I-56)

> <!-- CR-071: the Baja commission --> **[APPROVED — CR-071]** Baja is governed from La Paz by a commission chartered by the confederal chambers, three commissioners with Spanish as a working language, until 1887. In the 1870s it makes compacts with the Kumeyaay, Paipai, Kiliwa and Cucapá for homelands in their sierras and the delta. **[OPEN]** The commissioners' names.

### §13, after the Baja block (C5, I-53, I-65, C2, I-52, I-62, I-68, B2)

> <!-- CR-071: the settlement programme --> **[APPROVED — CR-071]** The interior is filled while the members are emptied. John Wesley Powell heads the land and water office, and his irrigation districts are drawn by watershed. The passage offices bring settlers from Europe and Asia to farms sold by the Land Fund on instalments. The trunk lines are chartered by the confederal chambers on Land Fund grants: the Raton line reaches Las Vegas in 1879, the thirty-fifth-parallel line crosses to the Colorado in 1880–83, and the Salt Lake–Snake–Columbia line is built in 1881–84. The settlers owe their farm to the Land Fund, their water to the district and their passage to a confederal office, not to the member's legislature. **[PROPOSED — CR-071]** Hans Mattson runs the passage offices. **[OPEN]** The programme's scale, and when Powell enters the Republic's service.
>
> <!-- CR-071: the first quarrel, and the leases --> **[APPROVED — CR-071]** The first quarrel is Oregon's. The Chinese floor of its charter has brought Chinese Pacificans into the Rogue valley, and in 1869 the Breckinridge men of Jackson and Josephine carry a Land Act through the legislature. It bars Land Fund sales to anyone the old constitution would have barred and lays a member tax on assisted settlers' instalments. In 1870 the Confederal Court strikes it down: the Land Fund's title is confederal, the floor protects a citizen of another member, and no member tax lies on a confederal grant. Oregon keeps its power over residence until 1887.
>
> **[APPROVED — CR-071]** Where a line or a mine crosses a homeland, the nation leases and does not sell. In 1873 Ouray negotiates the San Juan lease, which gives the miners their districts and roads and keeps the valleys Ute. The leased districts of the San Juan and Gunnison join the Mountain Districts' commission, which moves to the new silver town of Leadville in 1879. Globe and Clifton are worked on lease inside the Apache country, and Bisbee's copper pays the Chiricahua a royalty. In 1881, when the Snake line reaches the reservation, Fort Hall's council refuses to sell the Portneuf right of way and leases it for a rent the railway pays, as every later crossing of a homeland does.

### §14, after l. 665 (CR-070, "the northern wire") (I-69)

> <!-- CR-071: Dall --> **[APPROVED — CR-071]** In 1885 William Healey Dall, the naturalist of the telegraph survey, succeeds Davidson at the head of the Northern Commission at forty.

### §14, l. 669: after "…eventual independence from the system expensive." insert; the paragraph's last sentence follows as its own paragraph (Part D, D2, L10)

> <!-- CR-071: the abolition of the domains, watched --> **[APPROVED — CR-071]** Kido Takayoshi and Itō Hirobumi have read the Articles of 1856 through Hamada Hikozō at Nagasaki and concluded that Japan cannot afford a confederation whose members keep their own militia and a veto. Part of the alliance's credit lets Tokyo promise to take the domains' debts and paper money. Elias has the accounts, and he watches the abolition of the domains in August 1871 as an underwriter, not a spectator: the registers returned first, the guard assembled before the announcement, the lords brought to the capital and given rank for office, the new prefectures named for rivers and mountains.

Then: "The Iwakura Mission's San Francisco landfall in 1872 puts Japan's officials inside this industrial world." (own paragraph, unlabelled as before), then CR-072's l. 671 as amended in A row 5.

### §14, l. 673 (CR-073): before "In 1874 his bank is the Republic's agent for the Spanish government's loan …" insert (L10, decision 6; CR-073 R10)

> <!-- CR-071: Japan's loan of 1873 --> **[APPROVED — CR-071]** In 1873 part of Japan's loan for the samurai stipends is placed in San Francisco, with the Bank of California as the Republic's agent. **[APPROVED — CR-073]**

The CR-073 sentence that follows ("In 1874 his bank is …") keeps its label through the repeated tag. This completes CR-073 R10, which left the Japanese part to CR-071.

### §15, l. 703: A row 12, and at the end of the paragraph, after "…has become daily experience." (H-17, H7.3)

> **[APPROVED — CR-071]** In 1886 a mob drives Chinese families off their district farms on the Feather; the Confederal Court convicts the ringleaders, and the district restores the families to their land.

### §19, after l. 773 (CR-037, "Soberanes guards the machinery against patrons as well as factions") (Part D decision 9; E3; B3, B4)

> <!-- CR-071: the memorandum, the assumption and the Collar --> **[APPROVED — CR-071]** In the winter of 1878–79, back from Vladivostok, Soberanes writes Elias a memorandum on what Japan has shown: money first, then the men, then the armed men, then the map, then the vote. Victoria reads it. The slack years after 1873 and falling prices have put the members' railway and road bonds into arrears, while the Reserve Bank carried the coast's largest private bank through August 1875. Now the Confederation offers to take the members' debts.
>
> **[APPROVED — CR-071]** The Assumption Act of 1879 goes to each member legislature with *An Act for the Common Execution of the Laws*, to be taken together or refused together. A member that takes them has its debt assumed and its paper guaranteed, and its treasury is audited by the Polytechnic. Its treasurer and auditor are examined and posted from outside. Its governor, still elected, accepts a confederal commission as Commissioner of the Confederation and answers to the Providentor for the common law; each receives his commission from Elias in person at Monterey. The Committee party's papers call it the Collar, and the *Deseret News* takes up the name. Oregon, Columbia, Idaho, western Montana, Washoe and New Mexico take it in 1879–80. California, which does not need rescuing, refuses, and so does Deseret, whose Church will not open its books to Carquinez's auditors. Hawaii, under its Territorial Council, is not asked. Through the 1870s and 1880s the members adopt California's codes one after another on Party majorities.

Then CR-072's l. 777 (as amended in A row 4), then:

> <!-- CR-071: the trades and the soldiers come into the Party --> **[APPROVED — CR-071]** The Party takes in the trades as well. In the slack year of 1877 Denis Kearney draws crowds to the sandlot and loses them when work comes back; his anger has no crash to ride. From about 1880 Frank Roney, an Irish moulder who despises Kearney's methods, builds the Party's trades side. Hiring goes through the trades, not the brokers, and the ticket runs on *Eight hours and the same wage*, which the Realm's own works keep. To the settler the same wage means no one can undercut him; to the Chinese workman it means equal treatment, and the trades admit everyone who earns it. The Party enrols the soldiers too: in the interior its lodges are largely veterans of 1861–65 and men home from the companies abroad.

Then CR-022's l. 775, then:

> <!-- CR-071: the Militia Act, Sherman's board and his refusal --> **[APPROVED — CR-071]** The Militia Act of 1882 makes every member militia a reserve of the common army, its officers commissioned by the Confederation and its arms kept in confederal arsenals. Sherman chairs the board that examines every commission, the militias' with the regulars' and the Auxiliary's, and keeps the commissions out of the Party's hands. Elias accepts it as Sherman's price: rank is no longer a reward the Party can give, no Party committee stands in the chain of command, and no serving officer stands on the Party's ticket in a county he commands. At his request, with Elias's consent, the officers who fail are kept together as a command of their own, the inland command. From 1882 to 1885 the Auxiliary's veteran battalions pass to the interior garrisons and come under the inland command, and Silas commands on the Sierra line. In June 1884 men of the old army, and Prosperity men who do not trust the Queen's influence or the Japanese naval party, offer Sherman the state after the founder. He answers that he will not take it.
>
> <!-- CR-071: the survey --> **[APPROVED — CR-071]** In 1880 the Superintendency commissions a survey of water districts, stations and land values, headed by Theodore Judah, on whose tables the Patrimony's Development Fund lends. Its second purpose is the map of counties that will replace the members, and it is known to Elias, Soberanes and Judah. Ralston, who sees every sheet the Fund lends on, works it out and says nothing. The census of 1880 is printed again by the survey's districts with a provisional map of about 130 districts in 1884, and every confederal table from then on is printed by district. The second map, the 124 in 1886, is argued over seat by seat inside the Party's county committees. Where two towns want the seat, the railway station decides, and the loser receives the court, the school or the hall.
>
> <!-- CR-071: the Pacific Companies' first generation --> **[APPROVED — CR-071]** By 1887 the Pacific Companies have served abroad for a generation under the venture licence. The first company is raised at Shanghai in 1860 and serves until 1863. Veterans of 1861–65 serve in Japan between 1866 and 1875. In the war of 1878 the Republic issues letters of marque, a company guards the Keelung coal in 1884–85, and from 1885 Pacificans serve in the Customs' preventive service. **[PROPOSED — CR-071]** The Shanghai company is Frederick Townsend Ward's: Pacifican officers and sergeants over Chinese ranks. It holds the city; Ward is killed at Cixi in September 1862. In December 1863 Li Hongzhang has the Taiping princes who surrendered at Suzhou put to death, and the company refuses further service, because its articles forbid any part in killing prisoners. In Japan the companies survey and guard Kuroda's Hokkaido and lend sergeants to the army mission. In 1878 armed sealers and whalers take Russian supply ships in the Okhotsk, and the prize courts at San Francisco and Honolulu make the first fortunes. **[APPROVED — CR-071]** Some thousands have served, and hundreds have bought farms in the interior with what they brought home. They served beside Chinese and Japanese comrades, and they are the settlers least ready to hate them.

### §21, l. 825: after "…establish her record before she becomes regent." (H-17, H7.3; F1–F3, K-5, K-6, F-2)

> <!-- CR-071: the Feather River --> **[APPROVED — CR-071]** The irrigation counties have seen what a confederal title is worth. In February 1886 a night mob on the Feather burns the packing sheds of Chinese families who bought their district farms from the Land Fund, and puts the families on a river barge. The district holds its water by confederal grant, so the ringleaders are tried before the Confederal Court, not by a county jury, and convicted. The district restores the families to their land, damages are levied on the rioters' property, and the followers who pay their share are amnestied. **[PROPOSED — CR-071]** No one is killed.
> <!-- CR-071: the triggers --> **[APPROVED — CR-071]** Two events of 1885–86 make the constitution urgent while the founder lives. In 1885 California's legislature resolves against a war with Britain over Port Hamilton; the resolution has no force and is printed in London. In the water decision of October 1886 the Confederal Court, on Henry Miller's appeal in his riparian suit against a confederal district on the Kern, holds that a confederal grant does not extinguish a private water right held under a member's law, and every district in California now holds its water only until the next suit. The court that convicted the Feather rioters cannot protect the settlers' own rivers. The Party runs on the decision in every irrigation county and in November narrowly takes California's legislature from the Committee party. Romualdo Pacheco, home from Manila, is chosen President of California.

### §21, l. 827: replace "A regency article names Victoria, Queen of Hawaii, Regent of the Realm until an Act of Settlement establishes the Crown, and Julian Heir of the Realm. Elias's life office ends with him." with (K-19; A row 2)

> A regency article names Victoria, Queen of Hawaii, Regent of the Realm until an Act of Settlement establishes the Crown, and Julian Heir of the Realm. **[APPROVED — CR-071]** In December 1886 Elias's draft makes Victoria Queen of the Realm. She strikes the article and has Soberanes draft the regency in its place. A crown for her, she tells Elias, would pass through her to Julian and decide between his sons while he is dying; the members' men took a life Providentor, not a king; the Confederation still carries the ordinances that stretched her lease; and power held for a crown not yet settled is the older Hawaiian form. Elias's life office has no successor; he lays it down when the regency begins.

### §21, after CR-072's l. 831 ("…their senators sit as a bloc.") (G6, H-1, K-9, E-15, G-3, G-4, K-15)

> <!-- CR-071: the ratifications --> **[APPROVED — CR-071]** Pacheco settles California's terms with the Regent-designate at Thalassia in the winter of 1886–87, on the island where he went to school. He takes home the historic-land clause, Spanish entrenched, community property kept and the Mexican grants as organic law, and he knowingly signs away the power through which California could have excluded the Chinese. The bill goes to the confederal chambers in January 1887 and passes by two-thirds in April. In May Reginaldo del Valle, born in the Republic, carries it through California's senate, where a riparian amendment fails by one vote and the ratification passes by three. Ralston brings the San Francisco houses to give their word for it; the Patrimony spends nothing. Every charter of 1866 carries Elias's article of supersession, so the Constitution enters into force on 1 August 1887 whatever Salt Lake does. Deseret's acceptance, after Taylor's death, is its legislature's last act, and Cannon's telegram reaches Thalassia two days before the handover. Elias reads it himself.

### §21, after the ratification block (H-15, H-16, H7.1, H7.2)

> <!-- CR-071: the settlers' price --> **[APPROVED — CR-071]** The settlers of the interior are paid as well, in rules they can see kept. The Constitution's labour article holds four rules: no labour bound by debt, penal contract or a broker's ticket; the same wage for the same work, whoever does it; a day of rest in seven, on the day of the worker's faith; and the eight-hour day on the Realm's works and in its chartered undertakings. A convention of the regency answers the fear of native rule: each people is kept in order by its own, the interior by the inland command and its reserve and Hawaii by the Queen's Guard, never by the naval party. The promise of a law for the companies goes with the article: a school, land for service and treaties for service abroad. Silas says nothing through the campaign.

### §21, after l. 836 ("…they answer to the ruler, not the Chamber.") (G2, G4, K-11, I-7, I-8, I-70 to I-72, K-22, K-24)

> <!-- CR-071: the members' men, the Senate's other seats, Alaska and the homelands --> **[APPROVED — CR-071]** On 1 August 1887 the member offices end. The governors who hold the confederal commission that day, and Pacheco, receive appointed Senate seats held to sixty-eight. The member legislatures are dissolved, and their men may stand for the new county boards. California's capitol at Sacramento becomes the inland command's headquarters, Salem's a county hall and Olympia's the courthouse of the Court of the Realm's Columbia circuit. Thalassia, governed by the Crown without a board, chooses no senator. Each homeland of a million acres or more chooses one through its own council, as does each league of smaller homelands that reaches that size, and Alaska's nations choose one. Alaska stays a territory under the Northern Commission, outside the 124, and Baja's two counties replace its commission. The homelands are not counties. A homeland of a million acres or more stands outside the 124, and a smaller one lies inside a county's lines beyond its board's reach. Their compacts run to the Realm and change only with the nation's consent. A member of a nation becomes a citizen by entering himself on the register, and votes where he lives; those who live on leased ground in no county are on the roll of the county beside it.

"County boards choose one senator each." (l. 836) stands unchanged: the other seats are in this block under its own label.

### §21, l. 838: before "In August 1887 Elias dies." insert, and apply A row 6 (G1.3, R-1, G4, B-1, B-2)

> <!-- CR-071: the handover --> **[APPROVED — CR-071]** On 1 August 1887 the regency begins at Thalassia, and the states end with it. Elias, too weak to stand long, watches Victoria take the oath. Her first act as Regent is to sign the commissions of the 124 county Commissioners from the list he approved; they take up their counties in 1888, when the first boards are elected. Silas, Kiyoshi and Soberanes take their commissions from her hand and sit for the first time in the Regency Council. A week later Silas takes the oath again at Sacramento, in California's old capitol, now the inland command's headquarters, before its officers. He keeps the title of Providentor as a style, with no office and no seat. Twice a constitution of members has stood in his way: in 1860 it stopped him, when Hawaii withheld its assent to Washoe, and in 1864 the vote of twelve to six kept him by a single Californian. It could stop anyone after him, and the examined men he has trained since 1879 still serve under governors the members elect. **[PROPOSED — CR-071]** Elias's words that day are not recorded.

B-2 (APPROVED) requires the look-back. The draft names the two votes by what happened, and does not explain them.

### §22, l. 848 and l. 850: A rows 7, 8 and 9 only.

### §23, after l. 858 ("She dies in the autumn of 1888 …") (H-11, H-13, H-14)

> <!-- CR-071: the Honolulu rising of 1889 --> **[APPROVED — CR-071]** On 30 July 1889, the eve of Lā Hoʻihoʻi Ea, Robert Wilcox, home from the military academy at Turin, occupies the grounds of Aliʻiōlani Hale with a hundred-odd men. He demands that the Territorial Council be dissolved and the kingdom's legislature restored. They rise in the Queen's name against the Territorial Council. Kiyoshi's naval party offers marines and the Commissioner for Honolulu offers the reserve; the Regent refuses both, because each people is kept in order by its own. She sends the Queen's Guard over the Pali under Samuel Nowlein, with Kalākaua answerable for its loyalty, and her terms ahead of it. Wilcox refuses them. The Guard takes the grounds that afternoon and seven of the rising are killed. The Regent rides into Honolulu that night. The kingdom's Supreme Court tries Wilcox for treason, and a Hawaiian jury acquits him in 1890; the Regent accepts the verdict and says that the Act that establishes the Crown will end the Council. The loyalists sing of the seven; the Realm's press notes that no marine landed. Wilcox dies in 1903, before the union is put to the Hawaiian people.

### §24, after l. 867 ("…rather than as guardian obliged to surrender office on the boy's majority.") (G-8, R-2, K-12)

> <!-- CR-071: the interim --> **[APPROVED — CR-071]** Until the first Senate and Chamber sit in 1888, the Confederal Council and Assembly sit on as the Realm's chambers under the Regent, and the old county boards carry on in their old counties. The Council consents to the Chancellor the Regent appoints, and the Senate confirms him at its first sitting. The interim chambers' first act, early in 1888, is the Franchise Law; the first county boards are elected on it in the spring and choose the first Senate. **[OPEN]** The first Chancellor.

### §25, after l. 887 ("Victoria and Soberanes consolidate through examinations, finance and published comparisons.") (J1, J3)

> <!-- CR-071: the first Commissioners --> **[APPROVED — CR-071]** The first Commissioners arrive in 1888 from the examined men of 1879–87, each outside his home county and posted by the record of his works, not his marks. On the Rio Grande a Californio Commissioner hears complaints in the plaza as the alcaldes did and publishes the accounts in both languages, and in his third year the county's school passes are the best in the old New Mexico. At Hilo a Commissioner who has passed the Hawaiian examination speaks English to the Queen's people and takes their petitions through an interpreter, and Victoria recalls him early in 1889. Ordinary people notice less: the sheriff stays, the school examiner is a stranger, the courthouse changes its seal, and the tax bill loses the member's line. In Oregon the exclusion law has lapsed with the member, and the first Black family to buy a Willamette farm in 1888 does so without anyone saying why it can. **[OPEN]** The Commissioners' names.

### §25, after the first Commissioners block (H6.4, H7.2, H7.4, H7.8)

> <!-- CR-071: the labour law, the settlers' arenas and the Companies Act --> **[APPROVED — CR-071]** The labour law of 1888 fills in the article: county wage boards on the Realm's benchmarks, the working day outside the Realm's works, and the guest workers' rules. Every child is in school until fourteen, on a family farm as anywhere else. The Land Fund sells no household more than a family farm, a rule that binds the great buyers as much as anyone. The Development Fund lends to the districts' co-operatives, so that a settler can meet a harder-working neighbour with machines rather than hours, and the Polytechnic's farm stations teach the high-value crops to all who come. Honour has arenas outside the examination hall: the militia's commission, which carries the third vote; the counties' contest for the excellence of their works; and the counties' festivals of marksmen and riders. **[PROPOSED — CR-071]** The Companies Act of 1888 makes the companies a system: a school at Sacramento under the inland command's officers, a Land Fund warrant for every five years served, treaties of service with the partners, and a company's commission counted for the third vote.

### §25, after l. 897 (CR-037, "the county rule and its limits") (J2)

> <!-- CR-071: the first receivership and the first charter --> **[APPROVED — CR-071]** The first receivership is of an owners' board. In July 1892 the Regent declares a disorder in Coeur d'Alene, where the mine owners' lockout has met the miners' union with dynamite and rifles. The board is suspended and a commission enforces the labour code against both sides: it tries the men who blew up the Frisco mill and the guards who fired into the crowd, and hands the county back in 1895. Salt Lake is the first county to qualify for a charter, in 1893; the people most suspicious of the centre top its tables. The charter waits a year on the inspectors' test that no congregation may capture a county, and the Church's men on the board resign their Church offices to keep it. Salt Lake is chartered in 1894.

### §25, after l. 934 (CR-033, "Native Californian recovery and the leakage of land") (K-25, I-70, I-71)

> <!-- CR-071: the nations' ladder --> **[APPROVED — CR-071]** The nations have a ladder of their own. A nation may buy back its ceded land still in the Land Fund at the price the Fund paid for it. Its purchases join the homeland by a supplementary compact, and the county is paid its lost land tax for ten years; a homeland that grows past a million acres leaves its county. A nation whose accounts and services meet the Office's standard for five years becomes chartered. It is then its own trustee and keeps the lease fee the Realm has always taken. It holds its royalties in a patrimony of its own, may charter companies and borrow at home with the Treasury's consent, and keeps a court of first instance and its own police. It may have its language certified, so that its citizens who pass in it cast a tongue vote. The leak of land through long leases still runs, and the Office prints both columns for every nation. **[OPEN]** The year of the ladder's law; which nations climb first.

---

## C. Coverage and checks

- **Reviews.**
  - Self-review in the drafting session (17 November 2026).
  - Fresh-context review against `main` after CR-072 and CR-073 (17 November 2026, `CR-071-review-on-main.md`): four blockers and eleven should-fix items. All are applied in draft 2 except where section D says otherwise.
  - A short second fresh-context check of draft 2's placements is recorded in the review file.
- **Coverage comments:** `<!-- CR-071: … -->` as above. The register entry lists CR-071's sections §5, §12, §13, §14, §19, §21, §22, §23, §24, §25.
- **After integration:** run `sync_master_storyline.py --write` and `--check`, then `ledger.py check` once the ledger's quotes (`CR-071-ledger.md`) are copied from this text's final wording.
- **Other canon at integration:** in AGENTS.md, "Sherman's fate after 1865 stays OPEN" becomes "Sherman's career to 1887 is CR-071's (E-12 to E-14: the board of 1882, the inland command, his refusal of 1884); his fate after 1887 stays OPEN". AGENTS.md also gets CR-071's "Current canon" paragraph and the new identity count.
- **Not written here, and OPEN in canon:**
  - the names of the first Commissioners, the Baja commissioners and the first Chancellor;
  - when Powell enters Pacifican service;
  - the Apache bands of 1865 beyond the three named;
  - the year Oraibi signs, and the Hopi leaders;
  - when Nowlein takes the Guard;
  - Sand Creek;
  - the counties' changes after 1887;
  - the Cochimí.

## D. Review findings not applied as suggested

- **Appointed seats (review item 13).** Pacheco is not redundant beside the Commissioners. California refused the Commission Act, so he holds no commission, and K-11 (APPROVED) names "the Commissioners of the Confederation in office on 1 August 1887 and Pacheco". The text now says that; Deseret's executive, who holds no commission either, gets no seat.
- **The handover's look-back (item 15).** It is not cut, because B-2 (APPROVED) requires it. It now names the two votes by what happened and keeps out of the past perfect where it can.
- **The Apache countries (item 11).** They keep **[APPROVED — CR-071]**, because I-52 approves them from 1865. The rest of the peace stays **[PROPOSED]** in canon and in C-1865-APACHE, and the label after the block is repeated so that the Mangas sentence keeps CR-061's.
