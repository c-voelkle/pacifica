# CR-082 (outline) — Mouths and acres: how Pacifica means to be fed

**Status:** OUTLINE, 21 November 2026. First skeleton for the author. Nothing here is decided except what is marked *canon* or *author*. Figures are MODEL or hand estimates and are labelled.

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
- At the 1920s' rate the Realm passes 100 million about 1960, 150 million about 1972 and half a billion about 2005.
- Half a billion "a hundred years hence" needs only about 2.6% a year. The author's figure is a slowing of the present course.
- So the question does not lie a century off. The first hundred million are the children already born in 1932.

### A2. What canon says about food

- **Land and water:** Powell's irrigation districts by watershed; farms sold by the Land Fund on instalments; the family farm of 80 irrigated or 160 dry acres as a ceiling per household (CR-071). The energy workbook pumps about 2.6–3.6 million acres electrically in 1929.
- **Limits canon set itself:** every Columbia dam is leased from the peoples of its reach and none stands where salmon cannot pass; none at The Dalles, the lower Snake or the Grand Coulee (CR-055). The Thalassia Plan of 1928 reserves watersheds and minimum stream flows, and the Charter of 1932 makes that law.
- **Nitrogen:** electrolytic ammonia on the Columbia and Haber–Bosch on Sacramento Valley gas feed the Central Valley, the Imperial Valley and the Columbia Basin, the crowns' sugar and rice, Korea and the China trade (CR-054).
- **Exports:** California wheat goes to North China's famine in 1876–79; the Northwest sells apples and salmon to Asia and the Union.
- **The sea:** the seal convention, the salmon and halibut treaties (CR-058, CR-070); Heʻeia's and Puʻuloa's fishponds protected.
- **What canon does not say:** how many acres are irrigated, what they yield, what a Pacifican eats, whether the Realm is a net food exporter in any year, or how many people the domain can carry.

### A3. The script (proposal)

`population/provisioning.py`, beside `neighbours.py`. It reads the population run and the energy workbook's pumped acres and feeds nothing back.

- **Demand:** residents × grain-equivalent per head. A diet of meat and dairy needs about three times the grain of a rice diet, so diet is a lever.
- **Supply at home:** irrigated acres × yield, dry acres × yield, range. Levers: Powell's water ceiling, the compacts' and the Charter's reserved flows, the nitrogen path, the family-farm ceiling.
- **Supply elsewhere:** the sea, the crowns, contracts abroad.
- **Outputs:** the surplus or deficit by decade; the year home supply is passed at each growth rate; the same series for Japan (from `neighbours.py`'s pattern), because Japan's deficit is the Concord's business.

*Hand estimate, to be replaced by the script:* the domain's own soil, fully watered and fertilised at the yields of 1930, feeds perhaps 100–150 million. If so, the ceiling falls between 1960 and 1975 at present growth.

### A4. Decisions for Part A

- **F-1.** Build the script with the levers above.
- **F-2.** The diet the Office assumes: the Realm's present diet, or a leaner one.
- **F-3.** Whether the Philippine crown is counted inside the account (its people and its land) or beside it.

## B. The doctrine (sketch)

### B1. Who asks the question, and when

- *Canon:* Powell heads the land and water office (CR-071). The Office of Public Measures publishes the tables from 1888 (CR-027, CR-077). The challenge evening is the Polytechnic's test of a claim (CR-050).
- *Hist.:* Powell told the Irrigation Congress at Los Angeles in 1893 that there was not water enough for the lands already claimed, and was shouted down. In September 1898 Sir William Crookes told the British Association that the world's wheat would fail within a generation unless nitrogen were fixed from the air. Pearl and Reed fitted a ceiling of about 197 million to the Union's census in 1920.
- *Proposal:* three steps.
  1. **Powell's ceiling (1880s).** His office reports how many acres the domain's water can reach. Unlike history's Powell, he is believed, because he holds the office that draws the districts.
  2. **The first table (1890, with the Realm's first census).** The Office sets the population's course beside Powell's acres and prints the year they cross.
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
- **The Union and Canada:** the largest grain surplus on earth lies behind the eastern frontier, and the Union buys four-fifths of its oil abroad, most of it from the Gulf (CR-058). *Question:* whether oil for grain is the continent's bargain, and why the provisioners will not rest on it.

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

From the repository: `population/outputs/canon_by_year.csv` (the table in A1 and the growth rates computed from it, 21 November 2026); `finance/CR-056-dynamics-workbook.md` and `finance/dynamics-design-note.md` (pumped acres); the storyline for A2.
