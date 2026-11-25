# CR-089 review 3 (fresh context, canon check, 25 November 2026)

I reviewed `CR-089.md`, revision 8, whole, including its `## Canon tensions` and `## Decisions`. I read `AGENTS.md` (its "Fresh-context review" section and the summaries of approved CRs) and `docs/authority-and-scope.md`. I read every storyline line the draft cites, each with the lines around it: `L51`, `L81`, `L99`, `L333`, `L667`, `L701`, `L739`, `L745`, `L762`, `L783`, `L796`, `L850`, `L855`, `L887`, `L922`, `L937`, `L1028`, `L1036`, `L1080`, `L1129`, `L1220`, `L1306`, `L1322`, `L1325`, `L1338`, `L1344`, `L1365`, `L1553`, `L1556`, `L1561`, `L1702`, `L1704`, `L1737`, `L1752`, `L1786`, `L1892`, `L2041`. I grepped the storyline for the names, years and institutions the draft relies on and read what I found, among them `L43`, `L236`–`L257` (the State Assay Office), `L324` and `L327` (women's and families' passages), `L735`–`L741` (Sitka and Alaska), `L747` (the alliance of 1870–71), `L755` (the diamond field, 1872), `L941`, `L984` (the Realm card and the operators' complaint of 1898), `L1024` (the county halls), `L1032` (the Spirits Act and the halls), `L1141`, `L1250`–`L1258` (Chiyo), `L1354` and `L1401` (Hoover's food administration), `L1617`, `L1657`, `L1729`–`L1735` (the slump), `L1784` and `L1900`. I read `CR-037.md`'s decision table (E1–E11), `CR-038.md`'s F8 and F9, `CR-057.md`'s part E, `CR-076.md`'s A4, D7 and G4, and the registry entries for Keawe, Hoover, Mead, Hilgard, Satori Kato, Satō Shōsuke, Kaʻiulani (both IDs), Chiyo, Longyu, Harlan Tate, Szilárd and Julian. I read the two earlier reviews only to check whether review 2's items were answered. I did not read anything under `outputs/sessions/`, any writer's notes, or the git log or history. *Hist.* claims were checked from general knowledge, with a few web searches where the brief asked (named below); I say where a claim is wrong and where it is only unverified.

**Preflight.** `preflight.py --draft` exits 0 with 0 errors and 10 warnings: the nine new registry IDs (Takaki, Ah Bing, Kodani, Shima, Akiyama, Ikeda, Takamine, Lee Kum Sheung, Wu Yunchu), which land with integration, and "CR-088 (first cited on line 62) has no file and no register entry". Line 62 is the author's own words, quoted; nothing rests on CR-088. All ten are the expected warnings. `cr_facts.py preview` reports 12 fact changes, no canon passage that would still state an old value, and a clean lint over 4 files; its 33 findings in the draft are all "unknown character ID" for the same nine people. **Patterns.** A read-only script ran the three `add_event` patterns against the draft, against the two sentences `## B` quotes for integration, and against `master_storyline.md`. `takaki-beriberi-trial` matches `A7` (line 191) and `## B`'s *Tsukuba* sentence (1884). `bing-cherry-oregon` matches `## B`'s Ah Bing sentence ("whose name is on the cherry of 1875"), which is its only occurrence in the draft; the dead pattern of revision 5 is gone. `ikeda-umami` matches `A4` and `## B`'s Ikeda clause ("names its taste umami in 1908") and `A15` ("umami, 1908"). None of the three matches anything in the current storyline, so none over-matches canon.

## Verdict

**Nearly ready; no blocker.** Review 2's items are all answered. Case C of `T-MARK-1` is the right choice for this Realm, and `A6` is mostly written in canon's own terms: a label is a statement, nothing is reserved, the Assay Office tests on complaint, and the register of results puts quality where the agon already puts it. The losers pay (the Napa syndicate, the borrowed-name shippers). What remains is a set of corrections, most of them one or two sentences:

- Four points in the rewritten `A6` and `T-MARK-1`: the act's legal root (S1), a boundary question that Case C moves rather than removes (S2), two accounts of the reciprocity clauses that disagree (S3), and a title that still promises marks of origin (S4).
- Four contradictions of canon in `A13` and `A14`:
  - the county halls' date and their kitchens (S5);
  - the trades congress and the Cantonese guild as placers of cooks (S6);
  - the "bachelors' table" running to 1865 (S7);
  - Japanese restaurant dates taken from our timeline, where the Realm's Japanese population is a hundred times larger (S8).
- Three smaller points: the palace cooks' price (S9), the fermentation station's institution (S10) and two integration homes on summary lines (S11).

Nothing touches protected intent, `CR-037`'s examination by number, `CR-022`'s 1906, the boycott dates or the dates of the Chinese court.

## Review 2's items

- **S1** (storyline homes): **answered.** `## B` now has paragraphs in sections 25 and 33. Two of the new homes sit on summary lines (S11 below).
- **S2** (boycotts; Wu's process): **answered.** "Canon's boycotts are short", with `L1338`, `L1561` and `L1752`, and the raw material is Ajinomoto's.
- **S3** (the Madrid Agreement): **answered.** The Madrid register is gone. Lee's house registers its trademark "with Macao stated as its place".
- **S4** (the farmed sea "first appears"): **answered** in `A2`.
- **S5** (the mission's men; the Fujian galleys): **answered.** The consulate's interpreters and Chinese Pacifican Polytechnic graduates now make the translation, the galleys are PROPOSED, and `## B` puts the clause at `L762`.
- **S6** (the palace cooks): **answered.** They leave in 1913, after Longyu's death (`L1325`; the registry gives 22 February 1913), at Victoria's request through Kaʻiulani, and the steward offers what the register offers. The offer still misstates the price (S9 below).
- **S7** (the ranking): **answered.** The lists run from the 1890s, the Cantonese houses are first again "by 1928" in both items, and the palace house's years are tied to Sun at Thalassia. One word is wrong (Could fix: "legation").
- **S8** (Takamine): **answered.** The koji process wins, the maltsters lose, and the station is dated from Hilgard's work of the 1880s. The station's institution is a new problem (S10).
- **S9** (the nightly drink): **answered** as the trade's known breach, with its price, inside `L887`.
- **S10** (small contradictions): **answered.** Ah Bing's home province is left uncertain, `C13` is "Two powders and a pot", and the cake reaches the register through a guild master's naming.
- **Minor list:** all answered: the Court after 1887; Yuan Mei's four parts in ten; the cacao; "Pacifica" in `A12` item 2; the Truckee; the fair's name rule; the railways' own contract term; the cups at state dinners; the test from 1895; the Manila and fishpond choices; the grocers' decision in `C13`; the scope words; the redundancy; the dead pattern; "approved in direction". The items on marks crossing county lines and the Marks Act's content are moot under Case C. A few stray uses of "the Realm" before 1887 remain (Could fix).

## Blockers

None.

## Should fix

**S1. The Truth of Labels Act rests on the wrong act of 1866, and "no inspector in the cellar" meets the gaugers of `CR-076`**
- *Passage:* `A6`, The act ("extends the principle of the Measures Act of 1866, which already holds the assay standard by which strength is measured: a label is a statement, and a false statement about a good is fraud"); `T-MARK-1` Case C item 1 ("A false statement is fraud under the principle of 1866"); `A6`, Who enforces it ("There is no subsidy, no quota and no inspector in the cellar").
- *Problem:*
  - The Measures Act of 1866 "takes only what is confederal: the customs duty on imported spirits and opium, licensed importers, and the assay standard" (`L667`). It contains no label and no principle of fraud. The label is in the members' own acts of 1866–67 ("a label on every bottle with the Assay Office's strength, the floor and the life offices' figures", `L667`) and in the Spirits Act of 1888 ("From 1888 the label carries the Office's figures", `L1032`).
  - The principle the draft wants is `CR-076` A4: "Never false … its label says only what the figures show."
  - Canon also has inspectors at the source of one class of goods: "every still is licensed and sealed by the Assay Office, and the gaugers are rotated and paid by the Republic" (`L667`).
- *Fix:*
  - Root the act in `CR-076` A4 and the label of the members' acts and the Spirits Act. For example: "extends to every good the rule of the drink label of 1866–67 and 1888, that a label says only what is true (`CR-076` A4), with the Assay Office's standard as the measure".
  - Write "no inspector in the cellar beyond the gaugers at the licensed stills (`CR-076`)".
  - Correct `T-MARK-1` item 1 to match.

**S2. Case C removes the franchise, not the boundary: someone must still say what "Napa" means**
- *Passage:* `A6`, Place to the field ("every word must be true of all of it"); No district belongs to anyone ("No body draws a district's line, and there is nothing to fight over at a boundary"); `T-MARK-1` Case C item 3 ("There are no boundary fights, because there is no franchise to fight over").
- *Problem:* If "Napa" must be true of all the fruit, a court that hears a complaint has to decide where Napa ends. Is it the county, the valley floor, or the watershed that includes Pope Valley? Is "Russian River" the river's basin or its valley? There is no franchise to win, but there will be cases, and each ruling draws a line. As written, the draft promises that this never happens. The Napa syndicate's fight in `A6` and `C6` is about a franchise, so it does not test the claim.
- *Fix:* Give place-names a public reference that already exists in canon. County names mean the county's lines. Valley and river names mean the watershed as drawn on the land and water office's maps, since Powell's districts are "drawn by watershed" (`L701`). Below that (ranch, vineyard, slope), the name means whatever the maker's title deed shows. Then say plainly that the fights are over whether a statement is true, decided by the courts on complaint against that map, and that nobody gains a right by winning one. One case would make the point: a Pope Valley grower who writes "Napa Valley" and loses.

**S3. The reciprocity clauses: two accounts that disagree, and a citation of `CR-085` that does not hold**
- *Passage:* `A6`, Abroad ("reciprocity clauses in its own commercial treaties … Japan's are the first (PROPOSED)"); `T-MARK-1` Case C item 7 ("(the Concord's and Japan's first, `CR-085`)").
- *Problem:*
  - The act is of 1897. The Concord dates from 1927, so its clause cannot come first, and `CR-085` (the renewal of 1932) has no such clause.
  - Canon's instruments with Japan are the alliance of 1870–71 (`L747`), the compact of 1887 and its renewals of 1897, 1907 and 1917 (`L1617`, `L1220`), and the Concord of 1927.
  - `CR-076` G4 already proposes "the label standard (Hayama, 1928; PROPOSED)" for the Concord.
- *Fix:* Write one account in both places. For example: "Japan's first, in the compact's renewal of 1897 (PROPOSED), carried into the Concord's label standard at Hayama in 1928 (`CR-076` G4, PROPOSED)". Drop the citation of `CR-085`. Japan joined the Paris Convention, which has its own article on false indications, in 1899 (*Hist.*, to verify), which would give Tokyo a reason to agree.

**S4. Leftover language of marks**
- *Passage:* the title ("the cooks' agon, the marks of origin and the farmed sea's measure"); `T-MARK-1`, Why Case C is better ("(PROPOSED, in place of `A6`'s Napa fight)"); `## Decisions` D-22 (the set pieces "`C1`–`C14`" APPROVED at 12:51).
- *Problem:*
  - The title still promises the French-style marks the author rejected at 13:36.
  - "In place of `A6`'s Napa fight" refers to the marks version. `A6`'s Napa fight is now this same fight.
  - D-22 approved `C6` at 12:51, before revision 8 rewrote it as the refused petition.

  Nothing else in the file contradicts Case C. "Syndicate" now refers only to the Napa petitioners and the butter corner. "County board" appears only as the body that refuses the petition. "Madrid" appears only as left OPEN, and "marks" only as trademarks or in the record of earlier revisions.
- *Fix:* Retitle (for example "… the cooks' agon, the truth of labels and the farmed sea's measure"). Strike "in place of `A6`'s Napa fight". Mark `C6` in D-22 as "rewritten under D-35 (13:36); the new text PROPOSED".

**S5. The county halls open in the 1890s, and canon gives them no kitchens**
- *Passage:* `A13` period 3 ("The county halls from 1888 cook for hundreds a day and publish what each plate costs (`CR-038`)"); `A10` item 4 ("in the county halls from 1888"); `A14` stage 4 ("The halls' kitchen managers … become the trade's largest employers"; losers: "The small eating houses, undersold by the halls"); `## B` ("one clause at `L51` on the halls' published cost per plate").
- *Problem:*
  - Canon dates the halls to the 1890s: "In the 1890s every county opens a hall for all its residents, with sick and burial funds, interpreters, night classes, notices of work and the county's tables on the wall" (`L1024`; `CR-038` F8, "From the 1890s").
  - `CR-076`'s Spirits Act of 1888 sends money to "the halls" and gives them a coffee counter (`L1032`), but that is not an opening date.
  - Neither CR gives the halls a kitchen that feeds hundreds a day. Mass catering by a chartered county body, large enough to be the trade's largest employer and to undersell private eating houses, is a new premise attributed to `CR-038`. It also raises a question `CR-057` would ask: are the meals paid for by the measures grants, which pay for halls that meet the minimum? If they are, the eating houses lose to a subsidy, not to the halls' method.
- *Fix:*
  - Date the halls' kitchens from the 1890s and mark them PROPOSED as an addition to `CR-038` F8.
  - Say that meals are sold at cost from the halls' published accounts, with no grant in the price, so that they undersell by scale and by the card (`A14` stage 4), which is a fair fight.
  - Move `## B`'s clause from `L51` (a summary line, S11) to `L1024`.

**S6. Neither the trades congress nor a guild may place cooks in the halls**
- *Passage:* `A14`, The guilds ("The halls, the commissaries and the trades congress's register take the placing of cooks"; the Cantonese guild "runs a private school for the trade test, places its members in the halls and commissaries").
- *Problem:*
  - `CR-038` F9's first caution says the congress "never controls hiring, training or pay: no closed shop, hiring hall or gang of its own". Canon says "The contractors still hire, train and pay" (`L1080`). A register that "takes the placing of cooks" is a hiring hall.
  - The county halls are chartered, so `CR-037` binds them. Appointments follow the examination (E2, E5), and the passed-over and kinship tests apply (E10). A Cantonese guild that places its members in the halls is the kind of capture E1 exists to stop. It is also a capture by one origin, which the author has said the story must not turn into (`AGENTS.md`, CR-033 to CR-036).
  - "A private school for the trade test" contradicts `A4` ("no school teaches cookery").
- *Fix:*
  - "The halls and commissaries hire from the congress's register of passed cooks, by number and by the posted results."
  - "The Cantonese guild coaches its members for the written paper and recommends them, as `L855` lets any guild do, and its members win more of the halls' posts than any other guild's because more of them pass."

  The guild keeps its strength, and the halls keep their examination.

**S7. The bachelors' table cannot last to 1865: canon pays women's and families' passages from 1852**
- *Passage:* `A13` period 1 ("The bachelors' table (1846–1865). A city of single men eats out"); period 2 ("The peace brings families and the trunk lines (`L701`)").
- *Problem:*
  - "From 1852 the Superintendency pays the passage of single women with a contract of employment and of whole families" (`L324`, PROPOSED — CR-034).
  - "Elias makes women's immigration his own priority: a country of single men is a camp, not a republic" (`L327`, APPROVED — CR-034).
  - The passages continue after 1855 (`L384`), and the families come through the 1850s and 1860s.

  Canon's Pacifica ends the bachelor city earlier and on purpose, and that is one of its differences from our timeline.
- *Fix:* Make period 1 "The bachelors' table (1846–about 1855)", ending with the assisted passages and Elias's priority. Let period 2 begin with "the families the passages bring". Noah Brooks's "cosmopolitan fare" of 1868 can stay as our timeline's description of a city that, in canon, already had households.

**S8. Japanese restaurant dates and the cross-over houses are taken from a timeline with almost no Japanese and with Exclusion**
- *Passage:* `A13` period 2 ("Japanese restaurants follow, first cooking Western food and then their own (*Hist.*: Kame in Los Angeles, 1885, Western food; the Yamato in San Francisco, 1887, the first to serve Japanese food)"); period 5 ("Japanese cooks open Cantonese-style houses … (*Hist.*: some sixty Japanese-owned 'chop suey' houses in Los Angeles by 1927)").
- *Problem:*
  - The Realm has about 34,750 Japanese-origin residents in 1870 and 106,733 in 1880 (`population/outputs/workbook_changes.md`, MODEL), beside the Wakamatsu colony and the earlier emigration scheme (`L783`). Our timeline had a few dozen. Japanese eating houses that cook for Japanese customers belong in the Realm's 1860s and 1870s, not after 1885. Kame cooked Western food because Los Angeles had almost no Japanese to feed.
  - In our timeline the Japanese-owned chop suey houses also filled a trade that Exclusion had thinned. The Realm has no Exclusion and 4.8 million Chinese residents (`A12`), so the cross-over needs another cause or should be cut.
- *Fix:* Date Japanese eating houses in San Francisco, Honolulu and the Wakamatsu country from the 1860s, cooking for Japanese customers first. Keep Kame and the Yamato as *Hist.* comparisons. For period 5, either give the cross-over a cause of the Realm's own (each kitchen chasing the other's clerk lunch trade, as `A10` item 5 and `A12` item 2 already say) or keep the Los Angeles figure only as a comparison.

**S9. The palace cooks are offered the title "at the price of" a deposit the title does not require; and Thalassia has more than three kitchens**
- *Passage:* `A12` item 8 ("their dishes printed on the state dinner menus under their own names, and the title of master if they sit the trade test, at the price of depositing their methods under `T-METHOD-1`"; "the three kitchens fight over the state dinners for twenty years"); `A3`, Manila ("Its cooks at Thalassia refuse the French brigade's stations and cook the crown's own dinners"); `## B` ("the court's three kitchens").
- *Problem:*
  - The master's title is the Polytechnic's trade test, and nothing in `A4` makes the test cost a deposit.
  - The deposit is the price of a named dish in the guild's register (`T-METHOD-1` Case A; the naming rule, `A10`).
  - `A3` puts a Manila kitchen at the same court, so there are four kitchens, not three.
- *Fix:* "Their names on the menus are the register's, at the price of depositing their methods; the title is open to them by the test, which costs them nothing but the test." Their refusal is then of the names, and the title stays open. Write "the court's kitchens" or "four kitchens", and say which of them cooks the Hawaiian Crown's dinners (`A11` item 8).

**S10. "The agricultural college" is not an institution in canon, and `CR-057`'s one royalty covers Polytechnic patents**
- *Passage:* `A9` item 3 ("the agricultural college's station (item 7)"); item 7 ("A fermentation station at the agricultural college, grown out of Hilgard's wine work … so what he finds there is licensed at the one royalty (`CR-057`)").
- *Problem:* Canon's only named agricultural college is Deseret's at Logan (`L1184`). Berkeley appears only as a seismograph and a doctorate. `CR-057` E licenses "every patent it [the Polytechnic] holds". If the station is outside the Polytechnic, the open licence does not follow, and Takadiastase being "the station's and the Realm's" rests on nothing.
- *Fix:* "The Polytechnic's agricultural school and its fermentation station (PROPOSED), grown out of Hilgard's wine work of the 1880s". The one royalty then applies by `CR-057`'s own rule.

**S11. Two integration homes are summary lines, not story prose**
- *Passage:* `## B` ("one clause at `L51` on the halls' published cost per plate"; "One clause at `L81` on the cold chain and the common-carrier cars").
- *Problem:* `L51` ("**CR-038 integration:**") and `L81` ("**CR-052 integration:**") are lines in the storyline's list of integrations, which summarises each CR. They are not the narrative. An integrator who writes there leaves the prose unchanged, and `AGENTS.md` asks for "the actual narrative prose".
- *Fix:* Put the halls' clause at `L1024` (S5). Put the cold chain and the common-carrier cars beside the trunk lines' charters at `L701` (for the duty) or in section 25 near `L1036` (for the 1900s machines), next to the `L1737` sentence that already carries the refrigerators.

## Could fix

- **Oven thermostats** (`A14` stage 3, "*Hist.*: oven thermostats from about 1915"). This is right for gas ovens: the Lorain regulator of 1915 and Meacham's thermostatic gas-oven patents. Thermostats in electric ovens came later, in the 1920s. Since the Realm's kitchens are electric, say which oven you mean, or date the electric thermostat separately as a divergence.
- **Kelp meal before the kelp harvest** (`A5`, `A7` item 2: "harvested wild kelp meal in the interior's dairy and livestock feed keep endemic goitre down a generation early"). Canon has kelp harvested by machine only from the wartime plant at San Diego (`L1704`). Either date the kelp meal from about 1915, so that the goitre effect rests on kombu stock and sea fish before then, or say it is cut by hand before the war.
- **"Its curry" in 1884** (`A7` item 1). Takaki's ration of 1884 is barley, meat, fish, milk and vegetables. `A10` item 3 dates navy curry to "about 1908". "The ration comes ashore" is enough for 1884.
- **Ah Bing's thirty years** (`C2`: "a wife he has not seen in thirty years"). Born about 1848 (`A15`, `## E`), he would have married at about eleven. "Twenty years" or "since he was a young man" avoids it.
- **"The Realm" before 1887:** `A3`, the quarrel over rice ("In the Realm the same grievance belongs to the settlers of the interior in the 1880s"); `A4`, Abroad ("from the 1880s … bound to cook in the Realm"); `A6`, Abroad ("Kikkoman's in 1879" registered "in the Realm"; it was in California); `A9` item 7 ("Realm breweries", beside 1879). Write "Pacifica" or "California".
- **"The Republic's legation"** (`A12` item 3). A legation sits at Thalassia. The San Francisco house would be the consulate's table.
- **A boycott inside the Realm** (`A12` item 7, "the boycott of May 1928 doubles Tianchu's sales in the Chinatowns"). Canon's boycott of 1928 is China's (`L1561`). Chinese Pacificans boycotting Japanese goods, sold in part by Japanese Pacifican grocers, in the year after the Concord, is a new event with a cost of its own. Mark it PROPOSED and give it one line of consequence.
- **The porters' complaint of 1912** (`A14` stage 4). In canon the complaint of 1898 was answered by the Office's school and a year's wage from the concessionaires (`L984`). Say what the Senate's committee answers in 1912. The porters can still fail the test, but the reader should see canon's pattern applied and see it fall short.
- **The Realm card** (`A14` stage 4, "keep each recipe on a card … filed on the Realm card"). The Realm card is the Office's punched card (`L984`), and the county halls are Hollerith's company's customers. Say that the halls' costs and yields are tabulated on it. A recipe is not filed on it.
- **Kona under two rules** (`A6`): the cooperative's private brand under "Brands are private", and "Kona's coffee" under "The crowns and the nations". Say which rule governs, or that the brand sits inside the Hawaiian Crown's label law.
- **"Blind-panel scores"** (`A6`, register of results). Say who sits the panels: the fairs' juries, the press estate's tasters, or both.
- **`T-MARK-1` has Cases A and C and no B.** Say that Case B was withdrawn, or reletter.
- **Order of the approvals** (status block). 13:36 is listed before 12:51 and 12:00.
- **The American-Russian Commercial Company** (`A13` period 1). The claim is right (below). In a San Francisco that is not American, the company's name could note that its founders were Americans, or the draft could simply say "the San Francisco ice company".
- **Literary.** Victoria's request for Longyu's cooks comes in the year she "blames Julian for backing a man without an army while her friend's house fell" (`L1325`). The draft does not use this. The cooks could arrive as her reproach, and Julian's yes as his answer to it, at no cost to canon. `A14`'s guilds also have no scene. One candidate set piece would carry them: the French guild's refusal of the thermometer, or the porters' complaint of 1912.
- **Outside this CR:** `CT-CHIYO`'s registry profile says "Kiyoshi arranges her marriage to Julian in 1915". Canon has November 1907 (`L1258`, `CR-040`). This is for the author, not for this draft.

## What works

- **Case C.** "Nothing is reserved; every statement is checked" is the Realm's habit applied to food: measure, publish, examine, no exclusive rights (`CR-057` E). The Napa syndicate, which wanted "a monopoly rent", gets neither the line nor the premium. A decade later the register puts its members below Sonoma growers, and `C6` ends on a founder who finds his wine ninth. The shippers who lose "Burgundy" are real losers. The small grower's weakness is stated as the price and left unsolved.
- **Lee's oyster sauce and Wu's powder under the same act.** Both were always cases of content, so they fit Case C without change. The Assay Office's finding of no oyster, and its passing of Tianchu against Ajinomoto's expectation, show the act cutting both ways.
- **`A13` against canon's dates.** Apart from S5, S7 and S8, the chronology holds:
  - the *Tsukuba* at Honolulu in 1884;
  - the Feather River sheds in February 1886 (`L922`);
  - the trunk lines of 1879–84 (`L701`);
  - the earthquake of 1906 (`L1365`) and Tate's board in the autumn of 1906 (`L1220`);
  - Longyu's death in February 1913 (`L1325`);
  - the war from 1914 and the Russian campaign to 1920–22;
  - Hoover as Pacifica's food administrator in the war (`L1354`);
  - the slump with its foreclosures (`L1731`);
  - the table of 1930 (`L1702`) and Hayama in June 1932 (`L1786`).

  The Court decides after 1887 and the Confederal Court before it, as canon has them (`L922`, `L937`). The diamond field is 1872 (`L755`).
- **`A14`'s winners and losers.** Every stage has a named loser, and several are the author's "obsessives": the all-round cooks who will not work a station, the garde-manger whose cold room becomes a machine room, the French guild that becomes "the most coveted dinner on the coast and no power over anyone's career". The table answers the author's request for an engineering dynamic without making it a march of progress.
- **The master's title.** It is examined by number by examiners from another county (`L855`, `CR-037` E3–E4), registered by the congress (`L1080`), and leaves the guild only its dinner and its prejudice. That keeps the private prejudice where `CR-037` E7 allows it.
- **Tensions and figures.** `T-DIET-2` Case A leaves `L1702` and `L1892` intact. The two columns' figures match `provisioning.md` and the margin of about 1940–42. Population by origin matches `workbook_changes.md` (4.84, 5.77 and 0.97 million in 1932, 31% on the model).
- ***Hist.* claims the brief asked about:**
  - **Correct:**
    - Sitka and Kodiak ice shipped to San Francisco by the American-Russian Commercial Company from the early 1850s (web search: the Alutiiq Museum's entry on ice and accounts of Woody Island's ice houses; "to verify" can go);
    - Kame, Los Angeles, 1885, the first Japanese-owned business in what became Little Tokyo (web search: the Little Tokyo Historical Society's marker of 2022 confirms the date and the claim; that it served Western food is general knowledge and Rath's);
    - Fred Harvey's first house, at Topeka on the Santa Fe, 1876;
    - Childs, New York, 1889, with white-tiled rooms;
    - Fannie Farmer's *Boston Cooking-School Cook Book*, 1896, with level measures;
    - Taylor's *Principles of Scientific Management*, 1911;
    - Christine Frederick's *The New Housekeeping*, 1913;
    - oven thermostats about 1915, for gas ovens (Could fix);
    - Germany's must-weight classes in the wine law of 1971 (Oechsle measurement and the older terms predate it, which the draft's "fixed in law only" allows);
    - the American viticultural areas' 85% rule;
    - Noah Brooks on San Francisco's restaurants, 1868.
  - **Unverified, plausible and sourced to the books listed:**
    - the Yamato, San Francisco, 1887, as the first house to serve Japanese food (Rath);
    - "some sixty" Japanese-owned chop suey houses in Los Angeles by 1927 (Rath);
    - the Imperial Navy's ration control from 1890 and the army's reform from 1920 (Cwiertka pp. 71–79). I could not confirm the year 1890. Takaki's own reforms date from 1884–85.
  - **Wrong:** none.
- **House rules.** Citations are in form. The PROPOSED list matches the decision table except for `C6` (S4). OPEN items are listed, preflight is clean, and the three patterns match only what they should.
