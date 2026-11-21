# CR-082 (outline) — Mouths and acres: how Pacifica means to be fed

**Status:** OUTLINE, 21 November 2026. Part A's decisions F-1 to F-3 are decided (author, 17:59) and the script is built. At 18:16 the author asked for a central case in solid numbers that counts concerted yield research on land and at sea; A3 is that case. Nothing else is decided except what is marked *canon* or *author*. Figures are MODEL.

**Number:** CR-082. CR-081 (China, `drafts/cr081-china`, PR #83, not merged) waits on it; CR-080 (the partners) stays parked behind CR-081.

**Why now.** The review of CR-081 found that Pacifica's China policy has no stated purpose of its own. The author's answer is that the purpose has to come from a question the leadership asks about itself, and that the question is food.

**Read with:** CR-033 (the Land Fund, the population), CR-071 (Powell's office, the settlement programme, the family farm), CR-054 and CR-055 (nitrogen, the Columbia), CR-057 (the Patrimony, licensing), CR-075 (the war aims), CR-077 (the Office to 1932), `population/` (the cohort model).

## The author's request

> Historically the great powers and Japans scramble for China made sense from those countries perspectives. […] Yet Pacifica does something completely different seemingly only for China's benefit. What explains this and why is the payoff for Pacifica as the most technologically advanced country not more visible? In other words what is the point of Pacifica's China policy? (21 November 2026, 16:27)
>
> Its domain is mostly water, right, and arid land. And so it looks across the Pacific and it sees this giant rice bowl that's capable of supporting not just tens of millions of people, but literally billions. And it's weird if it doesn't think that, you know, it wants some of that. (16:46)
>
> a country with eminently foresighted leadership will not think in terms of feeding only the 37 million they have today, especially if their population was only like 3 million less than a hundred years ago. They will be thinking about how half a billion Pacificans will be fed a hundred years hence. This concern needs to guide China policy explicitly. (17:09)
>
> I don't think it makes sense to continue on the China CR without it (17:24)
>
> Start with the script. The Office has to assume the same diet, but not the same growth rate as in the early years. The Philippine crown is counted after Julian's accession. (17:59)
>
> This is very important information and it clearly needs to influence Pacifica's decisions from the 1880s onwards. One thing Pacifica would do anyway is to dedicate a significant amount of R&D towards increasing the yield, both on land and at sea. The first step is to define the central case in terms of solid and reliable numbers that take into account Pacifica's concerted efforts to maximize yields in dry areas (the Santa Fe University is the key nexus here). Then we can determine the correct slowing and assess the appropriate strategic positioning regarding the food producers. (18:16)

**Author's premise (17:09), taken as the brief:** the leadership plans for half a billion Pacificans a century ahead, and that plan guides foreign policy explicitly.

## Method

Three parts in order, as in CR-081. Part B is drafted once Part A's account is decided, and Part C once B is.

1. **The account (A):** people against food, decade by decade, from the models. The author's working rule applies: open values come from what the model allows, not from a figure fixed in advance.
2. **The doctrine (B):** who states the question, when, and how it binds decisions.
3. **The instruments (C):** what Pacifica does at home, at sea, in its crowns and abroad.

Part D lists what changes in other CRs. Part E lists candidate scenes. No prose is drafted yet.

## Reference works (proposal)

1. **John Wesley Powell, *Report on the Lands of the Arid Region of the United States* (1878).** The statement that water, not land, limits the West; irrigation districts by watershed; the 80-acre irrigated farm. Canon already has Powell at the head of the land and water office (CR-071). With it: Donald Worster, *A River Running West* (2001).
2. **F. H. King, *Farmers of Forty Centuries* (1911).** A soil scientist's tour of China, Korea and Japan in 1909, asking how the same fields fed so many for so long. It is the rice bowl seen by exactly the kind of man Pacifica would send.
3. **Vaclav Smil, *Enriching the Earth* (2001).** Crookes's wheat warning of 1898, Haber and Bosch, and what fixed nitrogen did to carrying capacity.
4. **Warren S. Thompson, *Danger Spots in World Population* (1929).** A demographer's argument, written in canon's last years, about crowded Japan and China beside the empty lands of the Pacific.

**Useful for single parts:** Pearl and Reed's logistic projection of the Union's population (*PNAS*, 1920); E. M. East, *Mankind at the Crossroads* (1923); David Wolff on the Manchurian soybean; Michael Adas, *The Burma Delta* (1974); the census irrigation volumes of 1890–1930.

## A. The account (first sketch)

### A1. What the population model already says

From `population/outputs/canon_by_year.csv` (MODEL; the storyline rounds 1932 to "about 37 million", the Philippine crown not counted):

| Year | Residents | Of Chinese origin | Of Japanese origin |
|---|---|---|---|
| 1861 | 1.2 million | 0.14 | 0.01 |
| 1880 | 4.3 | 0.54 | 0.10 |
| 1900 | 10.0 | 1.35 | 0.64 |
| 1920 | 23.9 | 3.14 | 2.93 |
| 1932 | 36.2 | 4.73 | 5.60 |

- Growth is about 4% a year from 1900 to 1932 and about 3.6% a year in the 1920s.
- Unslowed, that rate reaches half a billion about 2005. The author's "hundred years hence" is therefore already a slowing course, and A3 builds it that way.

### A2. What canon says about food

- **Land and water:** Powell's irrigation districts by watershed; farms sold by the Land Fund on instalments; the family farm of 80 irrigated or 160 dry acres as a ceiling per household (CR-071). The energy workbook pumps about 2.6–3.6 million acres electrically in 1929.
- **Limits canon set itself:** every Columbia dam is leased from the peoples of its reach and none stands where salmon cannot pass; none at The Dalles, the lower Snake or the Grand Coulee (CR-055). The Thalassia Plan of 1928 reserves watersheds and minimum stream flows, and the Charter of 1932 makes that law.
- **Nitrogen:** electrolytic ammonia on the Columbia and Haber–Bosch on Sacramento Valley gas feed the Central Valley, the Imperial Valley and the Columbia Basin, the crowns' sugar and rice, Korea and the China trade (CR-054).
- **Exports:** California wheat goes to North China's famine in 1876–79; the Northwest sells apples and salmon to Asia and the Union.
- **The sea:** the seal convention, the salmon and halibut treaties (CR-058, CR-070); Heʻeia's and Puʻuloa's fishponds protected.
- **What canon does not say:** how many acres are irrigated, what they yield, what a Pacifican eats, whether the Realm is a net food exporter in any year, or how many people the domain can carry.

### A3. The central case (MODEL)

`population/provisioning.py`, with `data/provisioning.toml`; the full report is `population/outputs/provisioning.md`. It reads the canon run and feeds nothing back.

**How it counts**
- **Diet (author):** the Realm's present diet, held constant. Our timeline's Union used about 2.1 acres of crop land a head for its own food and fibre in 1910–34, and that is the measure.
- **Land (census, our timeline):** irrigated acres by state in 1929 and the totals of 1889–1929, cut to canon's frontier; 13.8 million irrigated acres there in 1929. The ceiling is the 1940 census's irrigable area in enterprises, 22 million acres, with dry land at 1.2 times its 1929 extent, 15.8 million.
- **Canon's farmers:** canon has about three times history's people on the same land, so they work history's acres a head until the ceilings stop them. They reach the irrigated ceiling about 1910.
- **Concerted research (author, 18:16):** one rule. In year *t* the Realm farms as our timeline farmed the same land in year *t* + lead, and the lead grows from nothing in 1880 to thirty years in 1930. The measure is a verified series, Washington's dry-farmed wheat: flat at about 19 bushels an acre from 1900 to 1929, then 1.37 times that in the 1940s, 1.63 in the 1950s, 1.81 around 1960 and 2.13 around 1970. *Hist.:* dry-farm research began with Utah's Nephi substation in 1903, and its gains reached the fields a generation later. *Canon:* the Colegio de Santa Fe has taught acequia irrigation and dry-land farming since 1864 and Deseret's university measures water (CR-036 D13, D14). So the Realm's yields are history's until about 1915, 1.37 times history's in 1920 and 1.81 times in 1930.
- **The sea:** our timeline's Pacific landings at their peak of 1936 (the Pacific states' 1.9 billion pounds, verified, and Alaska's), reached by 1930 and counted as animal food that needs no crop land.
- **The Philippine crown (author):** counted from 1908, as its own ledger on its own diet. It roughly feeds itself.

**What it finds**

| Year | Residents | Canon's farmers, history's yields | With research | With the sea (central case) | Share fed |
|---|---|---|---|---|---|
| 1880 | 4.3 million | 6.6 | 6.6 | 6.8 | 160% |
| 1900 | 10.0 | 18.0 | 18.5 | 20.3 | 204% |
| 1910 | 16.0 | 22.1 | 22.3 | 24.9 | 155% |
| 1920 | 23.9 | 22.1 | 30.2 | 33.6 | 140% |
| 1930 | 34.3 | 22.1 | 39.9 | 44.1 | 129% |
| 1932 | 36.2 | 22.1 | 42.4 | 46.6 | 129% |

1. **Without research the Realm outgrows its own soil in 1918.** Land runs out about 1910; after that only yields can add food.
2. **With research and the sea it still feeds itself in 1932, with about three-tenths to spare,** and it has been a food exporter since about 1870. The research is what keeps it one.
3. **The margin closes fast.** On the Office's course the Realm outgrows soil and sea about 1940 if yields stay at 1932's, and about 1944 if they go on up history's ladder.
4. **Each table moves the date back by about a decade and no more.** The tables of 1890 and 1900 put the crossing at 1923–24, the table of 1920 at 1929, the table of 1930 at 1938.
5. **The century is out of reach of research.** The table of 1930 has about 438 million in the Realm a century on (the slowing is still to be decided). On the present diet they need ten times the home ceiling at 1930's yields, and eight times at history's yields of 1966–75.
6. **The case asks canon for two things it does not yet have.** About 22 million irrigated acres by 1910, against history's 13.8 million in 1929. And nitrogen: about 170 thousand tonnes a year by 1920 and 375 thousand by 1930, where CR-054 makes 90 thousand in 1929 and sends half to farms. With nitrogen as canon now has it, the central case feeds 37.5 million in 1932, barely more than the residents.

**How firm it is**

| If | Fed in 1932 | Share of residents |
|---|---|---|
| The lead in 1930 is 20 years | 35.8 million | 99% |
| It is 25 years | 40.9 | 113% |
| It is 35 years | 50.8 | 141% |
| Research lifts dry land only | 31.8 | 88% |
| There is no sea | 42.4 | 117% |

The lead is the one judgement in the case. Everything else that carries weight is a census or crop-reporting figure, except the items below.

**Corrections.** The skeleton's hand estimate (100–150 million fed at home) assumed something near a rice diet and was wrong. The first run of the script put the crossing at 1922; it gave yields a flat 30% for nitrogen and nothing for research. The central case above replaces both.

**Still weak, and listed in the report:** the same yield ladder is applied to irrigated land for want of a verified irrigated series; an irrigated acre is counted as two average acres and a dry one as 0.8 (MODEL); the dry-land series before 1929 and the part-state shares are estimates; the nitrogen response is canon's own figure from CR-056; Alaska's landings are recalled; fishponds, hatcheries, range and pasture are not counted; the Japan series is not built.

### A4. Decisions for Part A

- **F-1. DECIDED (author, 21 November 2026, 17:59):** build the script. Built.
- **F-2. DECIDED (author, 17:59):** the Office assumes the same diet, and a rate of growth slower than the early years'.
- **F-3. DECIDED (author, 17:59):** the Philippine crown is counted after Julian's accession (from 1908).
- **F-1a.** The central case's lead: thirty years by 1930 (recommended), or twenty-five. It decides whether the Realm exports food in 1932.
- **F-1b.** The rate at which the Office lets growth slow (now 1.5% a century on). The author takes this up next (18:16).
- **F-1c.** Canon's irrigated area: about 22 million acres by 1910. A line for the storyline, with Powell's office.
- **F-1d.** Canon's nitrogen: CR-054's 90 thousand tonnes in 1929 against the 375 thousand the case needs. Either CR-054's figure is raised (a canon tension for CR-054, to be drafted), or the lead is shorter.
- **F-1e.** The sea: whether canon reaches history's peak landings by 1930, and what research adds beyond the catch (fishponds, hatcheries), which is not yet counted.

## B. The doctrine (sketch)

### B1. Who asks the question, and when

- *Canon:* Powell heads the land and water office (CR-071). The Colegio de Santa Fe (1864) teaches acequia irrigation and dry-land farming, and Deseret's university is where the arid world learns irrigation (CR-036 D13, D14); the author names Santa Fe the nexus of the yield research (18:16). The Office of Public Measures publishes the tables from 1888 (CR-027, CR-077). The challenge evening is the Polytechnic's test of a claim (CR-050).
- *Hist.:* Powell told the Irrigation Congress at Los Angeles in 1893 that there was not water enough for the lands already claimed, and was shouted down. In September 1898 Sir William Crookes told the British Association that the world's wheat would fail within a generation unless nitrogen were fixed from the air. Pearl and Reed fitted a ceiling of about 197 million to the Union's census in 1920.
- *Proposal:* three steps.
  1. **Powell's ceiling (1880s).** By A3 it is about 22 million irrigable acres, and canon's farmers reach it about 1910. His office reports how many acres the domain's water can reach. Unlike history's Powell, he is believed, because he holds the office that draws the districts.
  2. **The first table (1890, with the Realm's first census).** The Office sets the population's course beside Powell's acres and prints the year they cross. By A3 the table of 1890 puts the crossing at 1923; research then moves it back about a decade with each table.
  3. **The revision every ten years** (1900, 1910, 1920, 1930), laid before the Senate with the census.
- The revisions fall beside decisions canon already has: the wire to Manila and Tokyo (1889–92); Liaodong, the Huludao option and the Gulf's founding (1898–1900); Julian's first years and Huludao's trust (1909–10); Harbin (1921); the Concord's renewal and the Charter (1932).

### B2. The two answers

The table does not say what to do. Two schools read it, and the author's premise makes the first the governing one:

- **The provisioners.** Numbers are power. The Realm is the smallest of the great powers and will be outgrown by its partner and its rivals unless it grows, so the half-billion must be fed, and the acres found.
- **The sufficers.** The domain carries what its water carries. Entry is already selective; let it be more so, and let the Realm be rich and few. This is the line that runs from Powell to Keawe's Charter.

Each has canon behind it: the Party's *Things work* and the settlement programme on one side, the compacts, the reserved flows and selective entry on the other. Which men and women hold each view is a decision (F-6).

### B3. The rule

*Proposal:* from the first table, every treaty, loan, lease and holding abroad is laid before the cabinet with two figures beside its price: the mouths it feeds or the people it brings, and by what year.

### B4. Stated or unstated

- *Canon:* "The Republic's further purpose in the Pacific is never stated" (CR-075). Pacifica never states anything false (CR-049).
- *Proposal:* the table is public, like every table of the Office. The conclusions drawn from it for China, Japan and the Gulf are cabinet minutes. The neighbours can do the arithmetic, and some do.

### B5. Decisions for Part B

- **F-4.** The three steps and their dates.
- **F-5.** Whether Elias leaves the question to Victoria in 1887 as a charge, or it arises in the offices under her.
- **F-6.** The two schools and who leads each.
- **F-7.** The rule of two figures.
- **F-8.** Public table, unstated conclusions (canon tension 1).

## C. The instruments (sketch)

Each line gives what canon has, the gap and the question.

### C1. At home: water, acres, yield

| Instrument | Canon | Question |
|---|---|---|
| Water | Powell's districts; Boulder Canyon (1926); the Columbia without the Grand Coulee; reserved flows | How much water the compacts and the Charter leave for fields (canon tension 2) |
| Nitrogen | the Columbia's ammonia; Sacramento gas | Whether the challenge evening takes up Crookes's warning in 1898–99, and nitrogen becomes the provisioners' first answer |
| Phosphate and potash | the guano islands (1867, 1871) | *Hist.:* the western phosphate field and Searles Lake's potash lie inside the domain (to verify dates) |
| Method | Asian farmers in the irrigation districts (CR-071 H-17) | Whether the Polytechnic sends its own King to the rice bowl, and paddy rice comes to the Sacramento Valley early (*Hist.:* 1912, to verify) |
| The farm | 80 irrigated acres per household | Whether a ceiling made for settlers suits a country that must feed cities |

### C2. The sea

"Its domain is mostly water" (author). Canon has the treaties and the fishponds. *Question:* how far the Office counts the sea, which gives protein and not bread, and whether the fishpond becomes a method as the paddy does.

### C3. The crowns and the protégé

- **Hawaii:** sugar, rice and taro on little land.
- **The Philippine crown:** about a million Filipinos already live in the Realm (MODEL). Its own land and people are F-3's question.
- **The Gulf Republic:** the nearest rain-fed farmland on the continent, an ally whose admission tests cannot pass before the 1960s (canon). *Question:* whether the provisioners read those tests differently from the men who wrote them.
- **The Union and Canada:** the largest grain surplus on earth lies behind the eastern frontier, and the Union buys four-fifths of its oil abroad, most of it from the Gulf (CR-058). *Question:* whether oil for grain is the continent's bargain, and why the provisioners will not rest on it. By A3 the Realm needs none before about 1940; the question is what it secures before then.

### C4. Other people's surplus land

*Proposal:* the doctrine ranks foreign land by its surplus, not its size. China proper feeds itself and little more; in the 1920s it bought rice and flour abroad (to verify).

| Land | What it yields | Canon's hold | Rival claimant |
|---|---|---|---|
| Manchuria | soybeans, bean cake, wheat | Huludao's port, trust and district; Chinese railways | China's own settlers; Japan |
| Formosa | rice, sugar | the administration since 1895 | Japan, by contract; China, by right |
| Korea | rice | a guarantee; fertilizer sales | Japan |
| The Amur and Siberia | wheat, in time | the alliance of 1922 | Russia; Japan's sphere |
| The rice deltas (Siam, Cochinchina, Burma) | the world's rice exports | none | France, Britain |
| Australia and New Zealand | wheat, meat, wool | none | Britain; closed to Asian settlers |

**The forms a claim can take,** from light to heavy: a purchase contract; a claim on revenue through credit; a lease by compact to a land company; an administration; a cession.

**Two limits from canon and arithmetic.**
- The Realm takes no acre without a compact, at home or abroad (CR-033, CR-070, CR-074's Act).
- The Realm imports people. It has none to settle abroad, so settlement colonies, the form Japan and Europe chose, are closed to it by its own numbers. Its claim is on the crop, and on the people who come.

### C5. People

Where the half-billion come from: births, and ships from Japan, China and the Philippines. About three in ten residents are of Asian origin in 1932 (MODEL). *Questions:* whether the doctrine sets a course for entry as it does for acres; how it meets the interior settlers' grievance (CR-071 H6); and whether Hawaii, which keeps its own entry rules, is bound by it.

### C6. Decisions for Part C

- **F-9.** The home instruments, and the challenge evening on nitrogen.
- **F-10.** The sea's place in the account.
- **F-11.** The Gulf, the Union and Canada in the account.
- **F-12.** The ranking of foreign surplus land.
- **F-13.** The heaviest form of claim the Realm allows itself in each land (the author's open question of 16:46: trade, hold or settle).
- **F-14.** Entry policy under the doctrine.

## D. What it changes elsewhere (to be decided there)

- **CR-081, China.** A8's aim ("a strong, successful China aligned with Pacifica, at minimal cost to Japan") gains Pacifica's own object. Formosa's published end date (A8.12), the Manchurian settlement left to Chinese land offices (S-4), the farm bank (S-5) and the famine and flood works (S-1), which add Chinese mouths, are each read again against the table.
- **Japan and the Concord.** In canon Korea is independent and Formosa is Chinese, so Japan has no colonial rice. *Hist.:* the rice riots of 1918 led to the colonial rice plans of 1920. Japan's deficit is therefore worse than history's, and the bean cake, the fertilizer and Formosa's rice all pass through Pacifican hands. The Hayama annex divides industries; nothing divides surplus land.
- **Britain.** The dominions hold the Pacific's empty farmland and keep Asian settlers out, while three in ten Pacificans are of Asian origin. This belongs to the confrontation CR.
- **The Gulf.** The admission tests (CR-039).
- **Home.** Keawe's Charter of 1932 becomes the sufficers' law, passed in the year of the fifth table.

## E. On the page (candidates, not drafted)

1. Powell before the chambers with his acres.
2. The challenge evening on the wheat warning.
3. Victoria with the table of 1900, in the months of the Liaodong negotiation.
4. The table of 1930 beside the Charter, with Keawe and the Industrial Board (canon's scene of 1932).

## Canon tensions

1. **The unstated purpose (B4).** Canon: "The Republic's further purpose in the Pacific is never stated" (CR-075). *Case A, canon kept:* the table is public and the purpose is still never stated; the reader infers it from decisions. *Case B, canon amended:* the purpose is stated in a document of the regency. No fact changes. *Recommendation:* case A.
2. **Water for fields against reserved water (C1).** Canon: no dam at the Grand Coulee, the lower Snake or The Dalles, and none where salmon cannot pass (CR-055); minimum stream flows (CR-036, the Thalassia Plan). The strongest provisioning plan would dam and divert more. *Case A, canon kept:* the limits stand, and the foreign instruments exist because of them. *Case B, canon amended:* one limit is given up. No fact changes drafted. *Recommendation:* case A; it is the doctrine's motive.
3. **The giant its neighbours need not fear (C3, C4).** Canon: Pacifica "coordinates nothing" in North America (CR-058). A doctrine that counts the Gulf's and the Union's farmland strains it. *Case A:* the account counts them and policy does not act on it before 1932. *Case B:* policy acts. *Recommendation:* case A, to be reopened by the author.

Watch item: CR-081 is not on `main`. Its A8.12, S-1, S-4 and S-5 are named in Part D as dependencies, not as canon.

## Fact changes

none

## Sources

Stated from general knowledge and to verify before any figure or date is used: Powell at the Irrigation Congress (October 1893); Crookes's address (September 1898) and its date for the wheat failure; Pearl and Reed's ceiling (1920); King's journey (1909) and book (1911); California's first commercial rice (1912); the rice riots of 1918 and the plan of 1920; China's rice and flour imports in the 1920s; the western phosphate field and Searles Lake; the grain-equivalent ratio between diets.

Read for the script on 21 November 2026 (details and status of each series in `population/data/provisioning.toml`): USDA NASS, Washington Field Office, all wheat, yield per acre 1879–1975; Utah Agricultural Experiment Station Bulletin 222 (the Nephi dry-farm substation, founded 1903); the Fish and Wildlife Service's release of 20 June 1941 (the Pacific states' catch); Census of Irrigation 1940, summary tables (the 19 states' irrigated area 1889–1939 and irrigable area in enterprises); Census of Agriculture 1935, vol. III, Table 7 (area irrigated by state, 1929); a table of crop land used per head, 1910–50 (collections.lib.utah.edu, id 1134612; the report's title to verify); the Philippine censuses of 1903, 1918 and 1939; the Library of Congress country study for the Philippines' cultivated area.

From the repository: `population/outputs/canon_by_year.csv` (the table in A1 and the growth rates computed from it, 21 November 2026); `population/outputs/provisioning.md` (A3); `finance/CR-056-dynamics-workbook.md` and `finance/dynamics-design-note.md` (pumped acres); the storyline for A2.
