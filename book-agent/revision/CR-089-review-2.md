# CR-089 review 2 (fresh context, 25 November 2026)

I reviewed `CR-089.md`, revision 5, whole, including its `## Canon tensions`. I read `AGENTS.md` (its "Fresh-context review" section and the summaries of approved CRs) and `docs/authority-and-scope.md`. I read every storyline line the draft cites, each with the lines around it: `L51`, `L81`, `L99`, `L333`, `L667`, `L701`, `L739`, `L745`, `L762`, `L783`, `L796`, `L850`, `L855`, `L887`, `L922`, `L937`, `L939`, `L1028`–`L1030`, `L1036`, `L1080`, `L1129`, `L1220`, `L1306`, `L1322`, `L1344`, `L1365`, `L1553`, `L1702`, `L1704`, `L1737`, `L1786`, `L1892`, `L2041`. I grepped the storyline for the names and CRs the draft relies on (Longyu, Chiyo, the Educational Mission, the China Merchants' line, trade tests, guilds, Tate, the earthquake, boycotts, Puyi, the Honolulu cables, the Confederal Court) and read what I found, among them `L832`, `L1141`, `L1237`, `L1258`, `L1325`, `L1338`, `L1346`–`L1348`, `L1403`, `L1556`, `L1561`, `L1752`, `L1766`, `L1890` and `L1792`. I read the registry entries for Keawe, Chiyo, Hoover, Kaʻiulani (Cleghorn), Longyu, Szilárd, Satori Kato, Hilgard, Mead, Harlan Tate and Satō Shōsuke; `CR-037.md`'s E7 row; `CR-071-H-resistance.md` H6.4; and `population/outputs/provisioning.md` §3 and §8 to see whether the century's plan already counts the sea. I read `CR-089-review.md` only to check its items. I did not read anything under `outputs/sessions/`, any writer's notes, or the git log. *Hist.* claims were checked from general knowledge only; I made no web lookups, and I say where a claim is wrong and where it is merely unverified.

**Preflight.** `preflight.py --draft` exits 0 with 0 errors and 10 warnings: the nine new registry IDs (Takaki, Ah Bing, Kodani, Shima, Akiyama, Ikeda, Takamine, Lee Kum Sheung, Wu Yunchu), which land with integration, and "CR-088 (first cited on line 57) has no file and no register entry". Line 57 is the author's own words, quoted; nothing rests on CR-088. All ten are expected and harmless. `cr_facts.py preview` reports 12 fact changes, no canon passage that would still state an old value, and a clean lint over 4 files; its 33 findings in the draft are all "unknown character ID" for the same nine people. **Patterns.** A read-only script ran the three `add_event` patterns against the draft, the two quoted storyline sentences in `## B` and `master_storyline.md`. `takaki-beriberi-trial` matches `A7` and `## B`'s *Tsukuba* sentence (1884). `bing-cherry-oregon` matches `## B`'s Ah Bing sentence and three draft passages through "cherry of 1875"; its first pattern, "Bing cherry … in", matches nothing anywhere. `ikeda-umami` matches `A4` and `## B`'s Ikeda clause ("names its taste umami in 1908") and `A13` ("umami, 1908"). None of the three matches anything in the current storyline, so none over-matches canon.

## Verdict

**Nearly ready; no blocker.** Revision 5 answers the first review almost entirely. The agon now has losers who pay: the Napa growers, the borrowed-name shippers, the cold-store syndicate, the pot school's masters, the oyster imitators, the Fujian house and the cookhouse cook who asks for his name and is fired. The Chinese kitchens make choices with stakes (`C5`, `C9`, `C12`, `C14`). The rough kitchens are in canon's spirit: "The Realm's transparency is the cooks' distrust made into rules" turns the publishing habit into a product of vice rather than virtue, and that answers the central-plan worry. What remains is a set of mostly one-sentence corrections. Four contradict canon: the boycotts (S2), where the farmed sea first appears (S4), the Educational Mission's men in the 1890s (S5) and the cooks' nightly drink (S9). Two get history wrong: the Madrid Agreement (S3) and Takamine's whiskey (S8). Two leave the palace cooks and the moving ranking unclear (S6, S7), and S1 corrects the status block's claim that every approved block now has a home in the storyline. Nothing touches protected intent, CR-037's examination by number or CR-022's 1906.

## The first review's items

- **S1** (storyline homes): **partly answered.** `## B` now places most blocks, but not all, although the status block says it does (S1 below).
- **S2** (*Tsukuba* patterns): **answered.** The pattern matches `## B`'s sentence and `A7`.
- **S3** (the *Tsukuba*'s record): **answered.** Shinagawa to Shinagawa, 14 mild cases, no deaths, and Takaki in Tokyo at the receiving end of the cable. The cable is possible in canon: `L832` ("The San Francisco–Oʻahu cable opens in 1879"), and from there it goes on by British wires (`L1141`).
- **S4** (who examines a master cook): **answered** (option a, approved 11:43).
- **S5** (the quarrel over rice and 1906): **answered.** `A3` follows H6.4 item 5, `C5` now has a cost, and `C9` sits after Tate's board in the autumn of 1906 (`L1220`, `L1237`).
- **S6** (losers): **answered.** `A9` now names who lost each fight, and one fight (health claims) is never settled.
- **S7** (Chinese agency): **answered** for the Chinese strand (Ah Bing's choice, Lee and Wu registered, `C5`, `C9`, `C11`–`C14`). Not taken up for the Filipino and Hawaiian cooks (Could fix).
- **S8** (Akiyama and Escoffier): **answered.**
- **S9** (1911 as a model; county Commissioners): **answered.**
- **S10** (the earthquake): **answered.**
- **S11** (which paper prints the sea): **answered**, but see S4 below on "first appears".
- **S12** ("the Realm" before 1887): **answered**, except one stray use (Could fix).
- **S13** (labels and the decision table): **answered.**
- **S14** (Takamine's roof): **answered**, but the station needs a date (S8 below).
- **Minor list:** all answered, except the redundancy item. `A10` item 11 still restates `A4`'s tasting (Could fix).

## Blockers

None.

## Should fix

**S1. The status block says every approved block has a home in the storyline; several still have none**
- *Passage:* status block ("every approved block now has a home in the storyline (`## B`)"); `## B` as a whole.
- *Problem:* `## B` now places `A1`, `A2`, `A6`, `A7`, the story facts of `A9`, Ikeda, Akiyama, Takamine, Lee, Wu and the palace cooks. These approved blocks have no sentence anywhere in it:
  - `A3`'s regional kitchens (direction approved, 06:58); there is only an "optional" clause at `L783`;
  - `A4`'s rough kitchens and the fellowships abroad (D-33, approved as direction 11:43); only Akiyama is placed;
  - `A5`'s two schools;
  - `A10` (approved in direction, 09:56) and `A11` (11:00);
  - `A12` items 1–3 and 5: Yuan Mei's book, the Cantonese-Western houses, the moving ranking and the camp cooks, all approved at 12:00.

  An integrator following `## B` would leave the core of the author's 06:58 request out of canon.
- *Fix:* Add one paragraph in section 25 beside `L1036`: the regional kitchens, the fellowships, the two schools, the Cantonese-Western houses, the camp cooks and Yuan Mei as the test's second book. Add one in section 33: the moving ranking, the two powders, the frozen course and the snowball. If the author would rather leave dishes and desserts to the beats, say so in `## B` and correct the status line.

**S2. Canon has boycotts, and Wu's raw material was Ajinomoto's too**
- *Passage:* `A12` item 7 ("In canon there is no boycott of the kind (`CR-081`), so he sells on price and on the Chinese cook's loyalty to a Chinese maker"; "makes glutamate from wheat gluten without the Japanese process").
- *Problem:* Canon has no boycott of Japan in 1919 or 1931 (`L1403`, `L1766`), but it has short ones: in 1915 "the boycott of 1915 is short" (`L1338`), and after Jinan in May 1928 "a short boycott answers it" (`L1561`). In 1930 Japan accepts the end of its consular courts "for an end to the boycotts" (`L1752`). The draft's statement is wrong as worded. On the history: Ajinomoto's own process was the acid hydrolysis of wheat gluten. Wu's achievement was to work the process out for himself, outside Ajinomoto's patents. He did not use a different raw material.
- *Fix:* "Canon's boycotts are short (1915, 1928), so he sells mainly on price and on loyalty." The boycott of May 1928 could be the season his sales jump in the Realm's Chinatowns, with some of the gain lost when it ends. That is a stake of the kind the author asked for. Reword the process: "by an acid hydrolysis of wheat gluten worked out on his own, outside Ajinomoto's patents (to verify)".

**S3. The Madrid Agreement on indications of source has no register, and China was not a party**
- *Passage:* `A6`, Abroad ("Foreign houses register their own places under it in the Realm, Lee Kum Sheung's among the first"); `A12` item 6 ("Lee's house registers Nanshui and Macao as its places under the Madrid Agreement").
- *Problem:* The Madrid Agreement of 1891 for the repression of false indications of source requires its parties to seize goods bearing a false indication. It creates no register of places. International registration belongs to the separate Madrid Agreement on marks, also of 1891, which registers trade marks, not places. Qing China was a party to neither. Lee's house also left Nanshui after the fire of 1902, so a registration of "Nanshui" that year needs a reason.
- *Fix:* Foreign places and houses enter the Realm's own register of marks under the Marks Act, on reciprocity or on the producer's application. The Madrid Agreement binds the Realm only to stop false indications at its customs. "Lee's house registers its mark under the Realm's act, with Macao as its place."

**S4. The farmed sea does not "first appear" in 1932**
- *Passage:* `A2` ("The farmed sea first appears in the Office's papers in July 1932, in a supplement to the century's plan").
- *Problem:* The plan of 1930 already "farms the sea, with kelp and shellfish beside Japan's kombu growers" (`L1702`). In `provisioning.md` §8 the century's figure counts Work 5's central case: "The Realm's own works feed 89.0 million (home and the farmed sea)". The 81% in `A1`'s first column therefore already includes the sea on `CR-082`'s whole-diet figure.
- *Fix:* "The century's plan of 1930 already counts the farmed sea on `CR-082`'s whole-diet figure; the supplement of July 1932 is the first paper to print it on two lines."

**S5. The Educational Mission's men are in China in the 1890s, and the Fujian galleys do not follow from them**
- *Passage:* `A12` item 1 ("An English version is made at San Francisco in the 1890s by graduates of the Educational Mission"); `A12` item 4 ("In canon most of the Chinese naval mission's graduates go to the China Merchants' Pacific line from 1880 … Its galleys are Fujianese"); `## B`, `L796` ("one clause on the Fujian galley cooks").
- *Problem:* Canon puts the mission's men in China: "By 1894 the mission's men, in their early thirties, work in Li's and Sheng's offices" (`L762`). The line runs from 1880 and is "officered by the mission's naval graduates by the 1890s", not from 1880. The mission's boys were mostly Cantonese (*Hist.*). The officers' origin therefore says nothing about who cooked in the galleys. The Fujianese claim rests on Shanghai's dock houses (Swislocki p. 167), not on the line. `## B` puts the clause beside France's war of 1884 (`L796`), while the line itself is at `L762`.
- *Fix:* Give the translation to someone who is in San Francisco in the 1890s, such as the line's officers in port, the consulate's interpreters or Chinese Pacifican graduates of the Polytechnic (PROPOSED). Make the Fujianese galleys a separate PROPOSED claim, without the "in canon" link. Move `## B`'s clause to `L762`.

**S6. The palace cooks: when they leave, at whose invitation, and what the deposit asks of them**
- *Passage:* `A12` item 8 ("when the Imperial Household cuts its kitchens after the abdication … accept the Hawaiian Crown's invitation, carried by Kaʻiulani … refuse to deposit their methods under `T-METHOD-1`"); `C12` ("the steward asks them for their recipes under the deposit rule").
- *Problem:*
  - (a) *When.* Under the Articles of Favourable Treatment the court kept the Forbidden City, its household and its kitchens until Feng's men drove Puyi out on 5 November 1924 (`L1556`). Fangshan (1925; that date holds) was founded by cooks released then. No event in 1912 cut the kitchens. Canon has a better one: Longyu, whom Kaʻiulani served, "dies in February 1913" (`L1325`), and her household is dispersed.
  - (b) *Whose invitation.* Since 1907 the Hawaiian Crown is Julian's. The friendship with Longyu is Victoria's: the third term "is Victoria's" (`L1322`), and "Victoria writes to Longyu until Longyu dies" (`L1325`). Victoria is not at Thalassia. The draft does not say who invites or why the cooks join Julian's court rather than Victoria's household.
  - (c) *The deposit.* `T-METHOD-1` deposits "a master's dish" as it enters the guild register. The palace cooks are not masters and belong to no guild, so a court steward has no rule under which to demand their recipes. Their refusal costs them something only if the deposit is the price of something they want.
- *Fix:* Bring them to Thalassia in 1913, after Longyu's death, as her own kitchen's cooks. A second wave after November 1924 is possible if wanted. Name the inviter: Victoria, through Kaʻiulani, with Julian's court as the kitchen, or Julian himself. Rewrite `C12` so that the steward offers them the register and its honour at state dinners on the register's terms, and they refuse what it costs.

**S7. The moving ranking borrows Shanghai's politics and disagrees with itself on dates**
- *Passage:* `A3`, Neighbourhoods ("The press estate's restaurant lists, from the 1900s"); `A12` item 3 ("In the 1890s the Sam Yup banquet houses … stand first. After 1912 a Peking house … and the first Sichuan house become the places where a Republican official must be seen to banquet … By the late 1920s the Cantonese houses are back on top"); `A12` item 8 ("closes in 1921, when the lists move to the Cantonese houses and the officials go home").
- *Problem:*
  - (a) The lists begin in the 1900s but rank the 1890s.
  - (b) The Cantonese houses return to the top in 1921 in one item and in the late 1920s in the other.
  - (c) Shanghai's guidebooks moved with Shanghai's politics. San Francisco has a consulate and students, not a Republican officialdom that "must be seen" at a banquet.

  The Realm's ranking should move with the Realm's Chinese politics. Canon supplies the moments: Sun at Thalassia (`L1322`), Chiang's mission of 1923 (`L1553`), the split of 1927 and the Canton reconciliation of January 1932.
- *Fix:* Start the lists in the 1890s (the press estate is chartered in 1887) or start the ranking in the 1900s. Pick one date for the Cantonese return. Tie the Peking house's years of fashion to the Realm's own visitors and exiles.

**S8. Takamine's koji whiskey: the wrong losers, and a station without a date**
- *Passage:* `A9` item 7 ("in the Realm the Sacramento malt distillers object to it before the Spirit Stores' buyers, who will not list a spirit no one has asked for, and it never sells"; "comes to the station as a fellow in about 1890").
- *Problem:* Takamine's process replaced malt in the mash with koji. It made ordinary whiskey for the distiller's own label. In Peoria the Whiskey Trust backed him, and the men who fought him were the maltsters (*Hist.*; the fire's year, 1891, is the usual account and unverified). "Malt distillers" and "a spirit no one has asked for" misread the case. Nobody at a Spirit Store counter can tell which mash made the whiskey, and `CR-076`'s label states strength, not process. Separately, the Realm's fermentation station is dated only by Japan's of 1904 (`A9` item 7). A fellow who arrives about 1890 needs a station that exists by then.
- *Fix:* Either let the process win in the Realm's distilleries and let the maltsters lose, which is the historical loser and the kind of loss S6 asked for. Or make it fail for a reason inside `CR-076`: the duty is about five-sixths of the Stores' price, so the distillers keep too little of the saving to retool. Date the station (PROPOSED, for example with the agricultural college in the late 1880s).

**S9. The cooks' nightly drink quietly amends `CR-076`**
- *Passage:* `A4`, The kitchens are rough ("Drink is forbidden on the line by Escoffier's rule and by the Realm's … and the cooks drink together after service").
- *Problem:* `L887` is settled canon: "The cup belongs to a thing done … Someone who drinks alone or by day is understood to be in trouble … an officer or examined official loses the post." As written, a nightly cup with no deed is a neutral custom of the trade, and that is an unlisted exception to `CR-076`. The author wants a rough trade, and canon can give one without the exception.
- *Fix:* Make the nightly drink the trade's known breach, with its price. The Realm reads a brigade that drinks after every service as men in trouble, the hotels sack a cook found with drink in him at the next service, and a hall's examined cook loses the post. The licit cups are the guild's dinner and the night of a proving. This is harsher than the present sentence and stays inside canon.

**S10. Small contradictions across `A`, `C`, `E` and the tensions**
- *Passage:* `## E` ("Ah Bing … Seth Lewelling's Manchurian foreman") against `C2` ("The boat home (Kwangtung and Portland …)"); `C13` ("Three powders and a pot") against `A4` ("two powders, Japan's and Wu Yunchu's"); `T-METHOD-1` and `A11` item 7 (a home baker's line in a register of "a master's dish").
- *Problem:* Ah Bing cannot both be from Manchuria and go home to Kwangtung; the accounts differ, so choose one. There are two powders. A home baker is not a master, so her cake has no reason to be in the guild's register, and her empty line needs one.
- *Fix:* Choose Ah Bing's home and mark it "to verify". Retitle `C13` "Two powders and a pot". Say how the cake reaches the register, for example through the growers' recipe contest, or because a guild master serves it and names her as its inventor.

## Could fix

- **"A Confederal Court ruling of about 1904"** (`A9` item 1). After 1887 the court is the Court (`L937`, "The Court's constitutional chamber"). "The Confederal Court" ends with the members.
- **Yuan Mei's rule is inverted** (`A5`: "the shopping is more than half the cooking"). Yuan Mei gives a fine meal's credit six parts to the cook and four to the buyer. Say "four parts in ten". His sins are fairly summarised, but "drinking before the dishes are tasted" is closer to "drinking so much that the taste is dulled", and "following fashion" is closer to "following the set banquet formulas".
- **Cacao "from the Philippine crown"** for chocolate makers of 1852 and 1868 (`A11` item 6). The crown dates from 1907. Write "from the Philippines, under the Philippine crown from 1907".
- **"The Realm has the same houses … from the 1870s"** (`A12` item 2). Write "Pacifica".
- **The Truckee ice harvest** (`A9` item 1). Historically the Sierra's commercial harvest ran into the 1920s, so its end about 1910 is the divergence. Say so beside the *Hist.* tag.
- **Marks that cross county lines.** Delta rice, Willamette cherries and "Basque lamb from the interior" span several counties. Say who draws a line across counties (each board for its part, the Commissioners certifying jointly) or confine the first marks to one county each.
- **The Marks Act covers content as well as origin.** The oyster case (`A12` item 6) and the date label (`A9` item 2) are statements of content. `A6`'s heading "Origin, not method" holds, but say that the act covers every statement on a label.
- **`C9`'s "as the rule allows".** No fair rule about a cook's name beside an entry is stated. Add it to `A10`: an entry may carry its cook's name beside the house's.
- **The press estate's list and the railway contract** (`A10` item 8). A state-shareholding estate's ranking that ends a contract reads like regulation. Say that the clause is the railway's own contract term.
- **Wine at state dinners.** The Hayama dinner is Japan's table. For the Realm's own state dinners (`A5`) and the guild dinner, say when the cup is poured, so that `CR-076`'s "thing done" governs.
- **When the trade test begins, and who its "masters" are.** `A12` item 5 says "open to them from its start", and `A9` item 3 says "women are among the test's masters from the start". Date the start (with the congress in 1895, or earlier), and say whether "masters" means examiners or cooks who passed.
- **Filipino and Hawaiian cooks** still have dishes and no choices (the tail of the first review's S7). One clause would do. A Manila cook might refuse the French brigade's stations at Thalassia, or a Hawaiian fishpond keeper might refuse to sell to the abalone day's houses.
- **Chinese agency through agents.** The two registered Chinese makers act from Macao and Shanghai through agents, and in `C13` the agency is Ajinomoto's. Let the Chinese grocers' change of supplier be `C13`'s decision. Or consider registering Chin Lung (historical, now background), who would give the Delta a Chinese Pacifican opposite Shima.
- **Scope.** The "most exclusive table in the Realm" (`A12` item 8), houses "more luxurious than the Western hotels'" (`A12` item 3) and `C14`'s marble lean toward the prestige-destination CR (D-26). Keep the rivalry and the ranking here, and leave the clientele and the luxury to that CR.
- **Redundancy.** `A10` item 11 still restates `A4`'s tasting and `C4`. A cross-reference is enough.
- **The dead pattern.** `bing-cherry-oregon`'s first pattern matches nothing anywhere. Drop it, or fit it to the storyline sentence. The second pattern, "cherry of", is generic. It is safe today, but it would catch any later "cherry of 18xx".
- **The palace cooks' approval.** The author's words at 12:00 are "could be cool". D-34 records them as APPROVED. "Approved in direction" would be the exact reading, and the particulars are already PROPOSED.

## What works

- **The rough kitchens.** `A4`'s brigades that despise one another, the spoiled stocks, the stolen recipes and the line "The Realm's transparency is the cooks' distrust made into rules" give the author the cutthroat arena he asked for without making the Realm's institutions the cooks' virtue. Private prejudice is placed where `CR-037` E7 allows it: guild dinners, hotels that will not hire women. The Polytechnic's test, which E7 binds, stays examined by number with examiners from another county (`L855`).
- **Losers who pay.** The Napa growers lose a third of their price and take twenty years to make their own mark worth anything. Two shipping houses fail. The pot school loses the halls it trained, and then loses again to Wu. The cookhouse cook in `C9` asks for his name and is fired the next week. The Fujian owner in `C14` changes nothing and loses his tables. None of these is a consolation.
- **The quarrel over rice.** "The judging table is a second front, not a peace", with the men of the Feather in the crowd and a blind tasting that is never quite blind. This is H6.4 item 5 written as a scene. `C5` (the mother does not enter again) and `C9` (autumn 1906, after Tate's board) carry the cost.
- **`A1`, `A2` and the tensions.** The four causes, the spending-not-land footnote, dairy as the reason for keeping the first column, and the sea's two lines that are never added together are unchanged and sound. `T-DIET-2` Case A leaves `L1702` and `L1892` intact, so Mead's case and Article II's irony survive.
- **`A7`.** The corrected *Tsukuba* record is right. The arithmetic of "three years off and the Concord forty-three" holds. The cable from Honolulu is possible on canon's cable of 1879 (`L832`).
- **The cast.** The nine registrations are historical people, as the author prefers, and no invented chef is named. The Chinese share (three of nine, with the unnamed Chinese cooks carrying four set pieces) is now roughly in proportion.
- ***Hist.* claims of revision 5 that hold** (general knowledge, not looked up):
  - Yuan Mei's *Suiyuan shidan* (1792), and that he collected recipes rather than cooked;
  - Lee Kum Sheung's oyster sauce at Nanshui (1888) and the move to Macao after the fire of 1902;
  - Wu Yunchu (1891–1953), Tianchu (1923) and the Buddha's-hand mark;
  - Fangshan (1925), founded by palace cooks released after 1924;
  - the Truckee ice harvest as a real industry;
  - Takamine (1854–1922), Takadiastase (1894) licensed to Parke-Davis, and Peoria;
  - the chiffon cake (Harry Baker, Los Angeles, 1927, sold in 1947);
  - the Cantonese egg tart of the 1920s, from Guangzhou's department stores, and the Macao tart of 1989;
  - Escoffier's dates;
  - Ikeda (1864–1936) and umami (1908);
  - Akiyama (1888–1974; Europe 1909–13);
  - the *Ryūjō* and *Tsukuba* figures;
  - the Capron mission's Ishikari cannery (1877);
  - rice as Hawaii's second crop in the 1880s.
- ***Hist.* claims I could not verify**, all plausible: Wu's patents abroad from 1926; the Fourth Avenue fire of 1899 and the "Fire God eats Western food" headline, which rest on Swislocki pp. 97–99; the Japanese chefs' judgment and Wang Dingjiu's phrase; Lee Kum Sheung's personal dates; the year of the Peoria fire; Chin Lung "before" Shima.
- **House rules.** Citations are in form, labels follow the decision table, the PROPOSED list matches the table, OPEN items are listed, and preflight is clean.
