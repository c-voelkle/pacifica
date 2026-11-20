# CR-081 (outline) — China's other century: materials, society and politics (1860–1932)

**Status:** OUTLINE, 20 November 2026. Parts A and B are decided (A7, B10); Part C (the political timeline) is in first draft with decisions P-1 to P-22. Nothing in Part C is decided beyond what is marked *canon*.

**Number:** CR-081. CR-080 (the partners' CR) is parked; its China part shrinks to what Japan, Korea and Russia need from China.

**Method (author, 13:41):** three layers in order. Parts B and C are drafted only once Part A is decided.
1. **The material layer:** technologies and resources, and how much of each.
2. **The socioeconomic layer.**
3. **The political timeline** on top of both.

**Read with:** CR-080 outline (frame, D0); CR-015 and CR-021 (the Customs, Formosa); CR-042 (Huludao); CR-057 (licensing, credit); CR-074 (Ward, the Companies); CR-077 and CR-078 (cards, wire, fax).

## The author's request

> Before we discuss China's political changes in isolation, I think we need to go at least two layers deeper and try to get a handle on the material changes. The kinds of technologies and resources that are available, and how much. Then the socioeconomic changes. Only on top of that does it make sense to develop the alternative political timeline. (20 November 2026, 13:41)
>
> Yes and please suggest three or four historical reference works that would help us to get a deeper understanding. (13:46)

**Decided earlier (CR-080 X-8, 13:31):** no communism in China without the Soviets. Mao is a nationalist and a rising leader.

## Reference works

1. **The Cambridge History of China, vols. 10–13** (Late Ch'ing and Republican China), above all Albert Feuerwerker's two economic chapters, also reprinted together as *The Chinese Economy, 1870–1949* (1995). This is the standard frame for every layer.
2. **Thomas G. Rawski, *Economic Growth in Prewar China* (1989).** The quantitative case that China's modern sector grew fast before 1937. Its series are the baselines for Part A.
3. **Albert Feuerwerker, *China's Early Industrialization: Sheng Hsuan-huai (1844–1916) and Mandarin Enterprise* (1958).** The China Merchants' company, the telegraph, the cotton mills and Hanyeping, all through one man. These are the enterprises Pacifican credit would touch first.
4. **Kenneth Pomeranz, *The Making of a Hinterland* (1993).** Inland North China, 1853–1937: what happens to the regions the railways and the treaty ports pass by. It is the corrective to a coastal story.

**Useful for single parts:**
- Tim Wright, *Coal Mining in China's Economy and Society, 1895–1937*;
- Ying Jia Tan, *Recharging China in War and Revolution, 1882–1955* (2021, open access), on electricity;
- Thomas Mullaney, *The Chinese Typewriter* (2017), on characters and machines.

## A. The material layer (first draft)

### A0. The method

Each item gets three things:
- **a historical series:** the anchor years and a source;
- **canon's change:** what canon already alters;
- **a proposed Pacifican series:** stated as a multiple or a shift of the historical one, labelled MODEL.

The historical series, read from the four reference works with page citations, are in `CR-081-A-series.md`; its section 9 says how they change the proposals below.

The numbers sit in a small standalone script (proposal: `population/china.py`, beside `neighbours.py`). It holds historical baselines and a few levers, so that Parts B and C can read population, output and literacy from one place. It feeds nothing in the financial workbook unless the author asks.

### A1. What canon already sends into China

| Input | When | Canon |
|---|---|---|
| Engineering and credit for steamships and the Kaiping mines | 1870s | §14, PROPOSED |
| The Educational Mission in San Francisco, with naval-academy places | from 1872 | PROPOSED |
| Yung Wing's machinery orders to Carquinez | 1870s | PROPOSED |
| California wheat for the North China famine | 1876–79 | §14, PROPOSED |
| A Keelung coal concession to a Chinese–Pacifican company, with railway and fleet-rebuilding credit | 1884–85 | §16, PROPOSED |
| The Customs Inspectorate under Pacifican leadership (Fong) | 1885–1929 | §16, §33 |
| The Formosan administration: camphor, the Keelung mines, the customs, the harbour; its receipts pay the indemnity, Japan, Pacifica's fee and then the province | from 1895 | §25 |
| Credit for a Chinese-owned Manchurian railway and the Hankow–Canton trunk | 1896 | PROPOSED |
| The Boxer indemnity turned into scholarships | 1900s | PROPOSED |
| The Polytechnic of Formosa | 1906 | §26 |
| Huludao: the harbour trust (from 1910), the Mukden line (1908–10), the industrial district (1923) | 1908–23 | CR-042, CR-057 |
| Harbin–Mukden Chinese line | by 1912 | CR-042 |
| Russia renounces its concessions and its share of the Boxer indemnity; the Manchurian railway returns to Chinese management | 1921 | §32, PROPOSED (CR-031) |
| The Manchurian line Chinese with Japanese running rights | from 1899 | §25 |
| Sibert's survey for a Chinese-owned Huai conservancy | 1914 | §28 (CR-051) |
| Shandong returned to China; the Tsingtao anchorage leased to Pacifica | 1919 | §30 |
| The Treaty of Nanjing: the Concord guarantees China's frontiers; China guarantees the Manchurian transit and its joint management | 1928 | CR-039 |
| The Formosan administration becomes a Concord affair with a Japanese deputy | 1928 | §33, PROPOSED |
| China recovers the Inspectorate, the customs and its tariff | 1928–29 | §33 |
| Fertilizer from Tacoma for South China's rice | from 1929 | §34 |
| The Republic's trade dollar for Asia, an outlet for Comstock silver | 1872 | CR-073 |

**What canon does not say:**
- how much of any of this there is;
- what China owns, mines or makes;
- what the Chinese do with the licences.

### A2. Resources

| Resource | History | Pacifican divergence to decide |
|---|---|---|
| **Coal** | output of 8,987,862 tons in 1912, over 23,000,000 tons in 1926 and more than 27,000,000 tons in 1931. Modern mines were 93% foreign-controlled in 1913, 78% in 1928 and 66% in 1936 (CE 119). Kaiping passed in 1900–01 to the Anglo-Belgian Chinese Engineering and Mining Company, with Hoover as its engineer, and formed Kailan with the Chinese Luanzhou company in 1912; Fushun was run by the Japanese South Manchuria Railway | Kaiping on Pacifican credit from the 1870s (§14, PROPOSED). In 1900–01 Hoover, a Pacifican in canon, refinances Kaiping on Pacifican credit instead of transferring it. Fushun stays Chinese, since Manchuria's railway is Chinese. The Shandong mines go to a Sino-Japanese company after 1919. *Proposal:* about 70–80% of modern output Chinese-owned by 1928; output about 1.2–1.4 times history's by 1931, following railway freight and the modern sector (MODEL). Keelung's coal is counted with Formosa |
| **Iron** | Hanyang began production in 1894, several years before Yawata, but its pig iron cost Ch.$48.50 a ton in 1919 against Benxi's Ch.$22.00 in 1915, mostly through the cost of hauling coke from Pingxiang (CE 147). Japanese funds were lent against Daye ore from 1904; Hanyeping (1908) under Sheng Xuanhuai fell into debt to its Japanese lenders, the pretext for the Twenty-One Demands' Hanyeping clause | Pacifican credit beside Japan's. *Question:* who finances Hanyeping, who fixes its costs, and does Daye's ore still go to Japan? |
| **Tungsten and antimony** | China became the world's largest producer of both. Hunan's antimony: the Tai Shing company under the Hunan Bureau of Mines (1897), the Wah Chang (Huachang) company with its Changsha refinery (1908), regulus exports from 3 tons (1908) to about 6,000 (1915). Jiangxi's tungsten from the 1910s (start date unconfirmed), dug by small miners and taxed by the province. K. C. Li (born Changsha 1892) traded it from New York from 1916 | Pacifica has its own tungsten (Atolia from 1904–05, the world's largest producer in the First World War; Pine Creek from 1916) and Japan has Korea's Sangdong (1916). China's tungsten and antimony are therefore an export trade for China, not a security need for the partners. *Proposal:* Chinese-owned mining and refining, sold to every buyer; K. C. Li, a historical person, carries the strand (Part B). Hunan is Mao's province (Part C) |
| **Tin** | Gejiu, Yunnan | Pacifican cans and solder; a smaller case |
| **Oil** | Formosa: the Qing hired American drillers at Chuhuangkeng in 1877; mainland China's first well at Yanchang, Shaanxi, 1907; Yumen 1939 | small; China buys the trust's lamp oil (canon). Formosa's oil is not among the administration's specified revenues (§25), so it is the province's |
| **Camphor** | Formosa's monopoly | under the Pacifican administration from 1895 (canon); film stock (CR-079) and celluloid |
| **Hydropower** | barely used | the AC standard spreads with Pacifican equipment through East Asia (canon). *Question:* any large Chinese hydro before 1932? |

### A3. Infrastructure

| Item | History | Pacifican divergence to decide |
|---|---|---|
| **Railways** | a 10 km line from Tangshan built in 1881, extended to Tianjin in 1888 and Shanhaiguan in 1894; Formosa's 107 km Keelung–Taipei–Hsinchu line of 1887–93; 9,618 km before 1912; about 3,400 km built in China proper in 1928–37 (CE 152) | **Canon's lines:** the Manchurian railway Chinese with Japanese running rights (§25), Harbin–Mukden and Huludao–Mukden (CR-042); PROPOSED: credit in 1896 for the Hankow–Canton trunk (history finished it only in 1936). Formosa's line survives, since the island stays Chinese. *Proposal:* about 11,000–12,000 km by 1911; about 14,000–15,000 km by 1927; about 16,000–17,000 km by 1932 at Nanjing's pace on the recovered tariff (MODEL). History: 9,618 km before 1912, about 13,000 km by 1927, 20,746 km of track in 1936 |
| **Telegraph** | a Tianjin–Shanghai line opened in December 1882, and lines soon connected all the important cities; the Telegraph Administration under Sheng from 1881–82; Great Northern's coastal cable from 1871 | the mission's telegraphers; the Manila–Keelung–Amoy–Foochow–Shanghai cable (CR-080 C1); fax on the newspapers' wire after 1908–10 (CR-078) |
| **Shipping** | the China Merchants' company (1872): 33 ships in 1877 and only 30 in 1914, while Japan's NYK grew from 51 to 93; no Chinese officer in 1885; two steamers to Honolulu and San Francisco in 1880–81, the scheme then suspended | steamers on Pacifican engineering (canon). *Proposal:* a Chinese Pacific line, Shanghai–Honolulu–San Francisco from 1880, officered from the mission's naval graduates by the 1890s (decision 9). From 1898 it competes with Japan's Tōyō Kisen Kaisha, which historically ran the same route, and with Pacifican shipowners |
| **Ports** | Shanghai, Tianjin, Canton and the treaty ports | Huludao (canon), Keelung under its harbour trust (canon); the Customs' lights (*Hist.*: the Marine Department from 1868) |
| **The post** | the Customs' post office from 1896 | the same under Fong |

### A4. Industry

| Item | History | Pacifican divergence to decide |
|---|---|---|
| **Cotton** | the first Chinese mill went into production at the end of 1889; Japanese-owned mills in China had 111,936 spindles in 1913 and 2,485,352 in 1936, while Chinese-owned mills went from 484,192 to 2,919,708 | By 1933 Chinese-owned mills made 71% of the yarn but only 39% of the cloth. Japanese mills in China (the annex makes textiles Japan's in the Concord, but China is not a party); Toyoda's looms licensed; electric drive. *Question:* does China's tariff from 1928 (canon) protect its own mills? |
| **Electric power** | Shanghai's first light in 1882; in 1936 China consumed only about 4 kWh per person | Pacifican equipment and credit; Huludao's district. *Proposal:* about 2–3 times history's use per person by 1932, about 5–7 kWh a head against Pacifica's 2,600, concentrated in the treaty ports and Manchuria (MODEL). History grew 14% a year in 1914–36, and foreign utilities still held 55% of output in 1936. The Shanghai Settlement's municipal plant, the largest single plant, was sold in April 1929 for 81 million taels to American and Foreign Power; who buys it in canon is a question (decision 5) |
| **Machines and electrical goods** | Shanghai's small machine shops | the Commercial Press as maker of character machines (CR-080 D2); Huludao's district makes coke, cement and rolling stock (CR-057). Whether Japan makes the radios and lamps waits on CR-080 X-3 |
| **Chemicals** | Fan Xudong's salt and soda works at Tianjin (1914–17) | — |
| **Steel** | 0.03 Mt in 1933 against Japan's 3.2 Mt; pig iron 0.5 Mt against 1.4 Mt (R 75) | *Question:* how much steel China makes by 1932 (decision 14) |

### A5. Money and people

| Item | History | Pacifican divergence to decide |
|---|---|---|
| **Customs revenue** | about 14.7 million Haikwan taels in 1885 (*Hist.*, to verify against the Customs returns); about 22 million taels in 1890, from a service of 700 Europeans and 4,000 Chinese; about 36 million in 1911 | Under Fong the revenue is about the same, because the treaty tariff is fixed. What changes is that it is published, Chinese staff rise, and Pacifican credit is secured on it. In the early 1890s the customs were a quarter of the centre's 89 million taels, and railways got half a million of its spending (CE 76). *Question:* does more of it reach Chinese development and less foreign indemnities, since there is no Shimonoseki indemnity on history's scale? |
| **Indemnities** | Shimonoseki (1895) and the Boxer indemnity (1901) consumed much of the revenue | a moderate indemnity in 1895 (canon); the Boxer indemnity partly turned into scholarships early, and Russia's renounced in 1921 (canon) |
| **Remittances** | Taishan and the Pearl River delta lived on remittances from America | Pacifica has no exclusion act and a charter floor for Chinese residents (canon). *Question:* how large is the Chinese-Pacifican population by 1900 and 1930 (population model)? |
| **Schooling** | the mission recalled in 1881; the examinations abolished in 1905 | the mission continues; the Polytechnic of Formosa (1906); the scholarships. *Proposal:* a Pacifican-trained technical class of a few thousand by 1911 and tens of thousands by 1930 (MODEL) |
| **Population and output** | Maddison found that GDP per capita declined from 1850 to 1870, then increased slightly from 1870 to 1913; the 1933 benchmark is considered reliable. GDP in 1933 was 29.88 billion yuan, the modern sector about 4.7% of it in 1933 prices (Liu and Yeh, CE 95) | *Proposal:* the same population path (the famines aside). Doubling the modern sector adds about 5%. *Proposal:* output per person 5–10% above Rawski's path by 1932 (MODEL), from a modern sector about twice history's and one to three points from agriculture. The waterworks (decision 10) are argued on floods and famine: Huang-Yun's losses are 0.2–0.3% of China's GDP |
| **Silver** | China was on silver. The gold–silver ratio rose from about 16 in the early 1870s to 39 in 1902, so loans in gold cost China more in its own money each year; silver fell again in 1929–31. Kemmerer's commission proposed a gradual gold standard in November 1929; China left silver in 1935 | Canon's trade dollar for Asia (CR-073) and Comstock silver put Pacifica on both sides. *Question:* in what money Pacifica lends, and whether China links to Pacifica's money in 1929 (decision 11) |

### A6. Information

The Chinese telegraph code (1871), characters on the Customs' cards (CR-080 C3), the Chinese typewriter and fax are the subject of CR-080 Part C. Here they are counted as material: how many terminals, cards and receivers there are by 1932 (MODEL).

### A7. Decisions for Part A

**DECIDED (author, 20 November 2026, 15:55):** all fifteen recommendations in A8 are approved.

1. The method and the script (A0), with levers for railways, coal ownership, power, waterworks, the price of silver, Formosa and migration to Manchuria, and a Japan series beside China's.
2. Coal: Kaiping and Fushun Chinese, the Chinese-owned share and the output multiple.
3. Tungsten and antimony as China's export trade.
4. The railway kilometres in 1911, 1927 and 1932.
5. Electric power per person by 1932, and who owns Shanghai's plant after 1929.
6. Hanyeping from 1904.
7. The technical class and the Chinese-Pacifican population.
8. Output per person by 1932.
9. The China Merchants' Pacific line from 1880.
10. The waterworks of the Yellow River and the Grand Canal from 1891.
11. Silver: the money of Pacifican loans and China's link to Pacifica's money.
12. Formosa to 1932.
13. Shandong's railway and mines after 1919.
14. Steel.
15. Agriculture and food: soybeans, cotton seed, silk, fertilizer, and grain capacity in the famines of 1920–21 and 1928–30.

**For Parts B and C:** the treaty ports and extraterritoriality; Britain's position; opium revenue and its suppression; the warlords' revenue and the railways as their prize; labour terms in Pacifican credit; migration from Shandong and Hebei to Manchuria; Korea's rice and the Yalu crossing; the 1913 Reorganisation Loan and the salt revenue.

### A8. The 1932 target and the decisions measured against it (approved 20 November 2026)

**The author's aim (20 November 2026):** a strong, successful China aligned with Pacifica, at minimal cost to Japan.

**The target in 1932 (MODEL where numeric)**
- China is solvent and governed. It has recovered its customs and tariff (canon, 1928–29), owns most of its railways, mines and utilities, and services its debt.
- China is still poor beside Japan. In the mid-1930s Japan's output per person was about 31% of the United States level and China's about 10%. With China 5–10% above Rawski's path and Japan faster in canon, China stays between a quarter and a third of Japan.
- Pacifica lends, trains and sets the standards. China owns. Japan sells manufactures and buys coal, ore and food under long contracts.
- Alignment rests on interest: credit, the Chinese Pacificans, the scholars, the standards and the Concord's guarantee of China's frontiers (Treaty of Nanjing). Pacifican ownership is kept to what canon already holds: the Formosan administration (as credit security, a Concord affair with a Japanese deputy from 1928, PROPOSED), the Huludao trust until its bonds are paid, and the Tsingtao anchorage. China resents these, and canon says so.

**Japan's position in China in canon:**
- Manchuria, Dalian and Port Arthur stay Chinese (CR-042). Japan has running rights on the Manchurian line (§25) and, from 1928, its joint management (Treaty of Nanjing, CR-039).
- Shandong returns to China and Pacifica keeps the Tsingtao anchorage (§30).
- Japan receives a share of the Formosan receipts (§25) and, from 1928, the deputy (PROPOSED).
- Victoria blocks the worst of the Twenty-One Demands (CR-040, PROPOSED).
- Japan's other gains (Urajio, Enkaishū and Karafuto in 1899, the Kamchatka protectorate, the Transbaikal sphere, Korea's economic predominance) were taken from Russia, not given for China.

**Where this proposal still costs Japan:** its cotton goods and mills in China after the tariff of 1928, Hanyeping ore at a reviewed price instead of a captive one, and the San Francisco route. The recommendations below turn the rest of Japan's interests into contracts.

| # | Decision | Recommendation | Pacifica | China | Japan |
|---|---|---|---|---|---|
| 1 | Method and script | Yes, with the levers in A7 and a Japan series, so that the ratio to Japan is computed | numbers in one place | — | — |
| 2 | Coal | Kaiping refinanced by Hoover on Pacifican credit in 1900–01 instead of transferred; Fushun Chinese; 70–80% of modern output Chinese-owned by 1928; output 1.2–1.4 times history's by 1931; Fushun and Kailan coal sold to Japan on long contracts | credit repaid | owns its fuel | coal on contract, without owning mines |
| 3 | Tungsten and antimony | Chinese-owned mining and refining (Hunan's Huachang company, 1908), sold to every buyer; K. C. Li as the trader | a second source beside Atolia | export earnings for Hunan and Jiangxi | a second source beside Sangdong |
| 4 | Railways | 11,000–12,000 km by 1911; 14,000–15,000 km by 1927; 16,000–17,000 km by 1932. Chinese state lines. Loans secured on the customs; after 1928–29 Nanjing keeps their service a first charge on the recovered customs. No lending to factions in Peking in 1916–28 (history's Nishihara loans of 1917–18, 145 million yen to Duan Qirui, discredited the borrower). Rails from Hanyang, locomotives from Pacifica (the Hayama annex) and Huludao's works | rails and locomotives | unity and grain carriage | transit on the Manchurian line |
| 5 | Electricity | 2–3 times history's use per person, about 5–7 kWh a head; Chinese municipal and provincial utilities. Shanghai's Settlement plant, sold in history to American and Foreign Power in 1929, goes to a Chinese municipal company on Pacifican bonds (needs the ratepayers' vote) | generating plant | power for its mills | — |
| 6 | Hanyeping | From 1904, Pacifican credit for Pingxiang's coke and its haulage, so Hanyeping can service its Japanese loans; the Daye ore contract to Yawata stays, with a price review. The Twenty-One Demands' Hanyeping group then has nothing to demand | a bank's return | keeps its works and makes its rails | keeps its ore |
| 7 | Technical class and Chinese Pacificans | A few thousand Pacifican-trained engineers and officials by 1911, tens of thousands by 1930. Japan keeps training China's lawyers and doctors; officers train at Whampoa on Pacifican money (§33, PROPOSED). The Chinese-Pacifican population comes from the population model; it depends on the family-emigration article of 1868 (PROPOSED) | the alignment's carriers | its modern cadres | its own Chinese alumni |
| 8 | Output per person | 5–10% above Rawski's path by 1932 | a larger customer | the gain | a larger market |
| 9 | The China Merchants' Pacific line | Yes, from 1880, officered by the mission's naval graduates by the 1890s; Hawaii keeps its own entry rules. It costs Japan's Tōyō Kisen line (from 1898) and Pacifican shipowners some of the trade | remittances and passengers | a merchant marine | a competitor on one route |
| 10 | Waterworks | Yes, from 1891, when the Qing put the Yellow River dikes on the localities: a Chinese conservancy board with Pacifican engineers, paid from the customs surplus under Fong and, after 1901, Pacifica's own share of the Boxer indemnity; Sibert's Huai survey of 1914 (§28) continues it. Land reclaimed from the canal lakes (more than 500 square miles, P 214) is sold or taxed to repay part | floods and famine relief that show what the alignment does | fewer floods and famines in the North China plain | — |
| 11 | Silver | Pacifica lends in silver (taels or trade dollars) for works paid for in China and in gold only for imported equipment, carrying the silver risk it can bear as a silver producer. In 1929 a Pacifican commission takes Kemmerer's place and proposes a gold-exchange standard linked to Pacifica's dollar | silver's outlet; China in its money area | debt that does not grow with silver's fall | — (Japan's own yen area is not extended to China) |
| 12 | Formosa | Within canon to 1932; a published date for ending the administration once the indemnity and loans are paid, after 1932. Formosan sugar and rice sold to Japan on long contracts | credit security | a date for recovery | sugar and rice, and the deputy |
| 13 | Shandong after 1919 | History's settlement of 1922: China buys back the railway with Japanese treasury-note credit and a Japanese traffic manager until it is repaid; the German mines go to a Sino-Japanese company | the anchorage only | its province and railway | a mining stake and a creditor's place |
| 14 | Steel | Hanyang made efficient for rails and a second works on Manchurian ore and Huludao coke; about 0.3–0.5 Mt of steel by 1932 against history's 0.03 (MODEL) | equipment | its own rails and bridges | fewer steel sales to China |
| 15 | Agriculture and food | Decided in Part B with the famines; Part A counts the railways' grain capacity and fertilizer | — | — | soybeans and bean cake through Huludao (canon) |

**Tradeoffs that cannot be avoided**
1. **Cotton.** China's tariff from 1928 hits Japan's cotton goods and its mills in China. This is Japan's largest cost. How far it is softened depends on what the partners' CR gives Japan (CR-080 X-3, undecided).
2. **Formosa.** Pacifican control remains China's grievance to 1932. Japan's deputy and its share of the receipts make it a shared asset, and Formosan sugar sold to Japan competes with Hawaiian and Philippine sugar.
3. **Recovery and alignment.** China will press on Formosa, Huludao and Tsingtao. Pacifica keeps China aligned by credit, contracts and the guarantee, not by those holdings.
4. **Speed and debt.** Faster building on loans secured on the customs loads the customs and invites a backlash against the lender, as the railway loans did in 1911. The revised railway path is slower after 1911 for this reason.
5. **Silver.** Loans in silver put the risk on Pacifica; loans in gold put it on China.
6. **Britain.** Kaiping kept Chinese, Fong in place of Hart and a large Pacifican creditor share all come at Britain's expense. Britain's answer belongs to Part C.
7. **Japan's army.** Its material interest is the Manchurian corridor and its transit, which canon secures. Canon already counts Huludao's customs among the officers' grievances and has the Manchurian plot stopped in 1931. A stronger China does not prevent the plot, and this CR leaves it as canon has it.
8. **Hawaii.** A Chinese Pacific line and a growing Chinese-Pacifican population touch the Hawaiian crown's concern for its own people. Hawaii keeps control of its entry rules, and the story does not become about one diaspora (CR-037).
9. **Coast and interior.** The waterworks earn no cash. Their money comes from the customs surplus and the indemnity share that could otherwise build railways.

## B. The socioeconomic layer (draft, revised after the technology review)

Built on Part A as decided and on the technologies canon already gives Pacifica: CR-052 (electricity, hydro, motor vehicles), CR-077 (cards, the Office's methods, cipher), CR-078 (wire, the warnings compact, wireless and broadcasting) and CR-079 (film, newsreels, records, sound film). Each item gives the historical baseline with its source, what canon and Part A change, and a proposal (MODEL where numeric). Abbreviations as in `CR-081-A-series.md` (CE, FS, R, P); outside sources at the end of this part. Decisions are numbered S-1 to S-16 to keep them apart from the section numbers. The fresh-context review is `CR-081-B-review.md`.

### B0. What Part A and canon's technology already decide

- Railways about 11,000–12,000 km by 1911 and 14,000–15,000 km by 1927 (A8.4); the Yellow River and Grand Canal works from 1891 and Sibert's Huai survey of 1914 (A8.10); output per person 5–10% above Rawski's path (A8.8); loans for works paid in China are in silver (A8.11).
- Formosa stays Chinese under the Pacifican administration (§25). It is counted in China's figures below and is China's showcase province for schools, power and radio.
- **How technology reaches China.** Not as Pacifica's own installations but through Chinese owners and five channels: the Customs under Fong (lights, telegraph, statistics), the railways, Huludao's district (CR-057), the Formosan administration, and the Chinese Pacificans. Japan is a sixth channel if CR-080 X-3 gives it consumer electronics (undecided).
- **Scale.** China has card and relay installations only, none of CR-077's stored-program machines: about 20–40 by 1932 at the Customs, the Post Office, the railways, the Bank of China, Huludao and the Formosan administration, under Hollerith's licence (MODEL). Nothing of the Works, no radio location and no cipher machine appears in China.

### B1. Disasters, warnings and population

| Disaster | History | Pacifican divergence and proposal |
|---|---|---|
| North China famine, 1876–79 | 9.5–13 million dead, most in Shanxi | California wheat and Chinese-Pacifican committees (§14, PROPOSED); no inland telegraph before 1881 and no railway into Shanxi. *About a million fewer deaths* |
| Boxer drought, 1898–1901 | the drought fed the Boxer rising | *As history* |
| Manchurian plague, 1910–11 | about 60,000 dead; Wu Lien-teh's quarantine at the railway centres and the Mukden conference of 1911 | in canon the Manchurian lines are Chinese, so one railway administration runs the quarantine by telegraph from the first cases. *About 40,000 dead*; Wu Lien-teh is the historical person |
| North China famine, 1920–21 | about 30 million affected, 0.5 million dead; relief by Chinese charities, the provinces and international committees; Red Cross engineers built motor roads as famine work | railways at about 13,000–14,000 km, the conservancy, newsreels of the famine shown in Pacifica (CR-079). *About 0.2–0.3 million dead* |
| Swatow typhoon, 2 August 1922 | 50,000–60,000 dead, perhaps more; a storm surge at night; warnings that day sent shipping to shelter | China's ports in the warnings compact (S-14): warnings by the Customs' telegraph from 1897 and by radio from about 1912, with evacuation of the low-lying villages. A night surge limits what warning can do. *About a third fewer deaths* |
| Northwest famine, 1928–30 | 6–10 million dead (Shaanxi about 3 million, Gansu 2.5–3 million); about 4 million refugees to Manchuria. The Longhai line reached Lingbao in 1927, Tongguan in 1931 and Xi'an in 1934 | the Longhai line reaches Xi'an by 1927, inside A8.4's path; trucks from Mariveles and Pacifica on famine roads reach part of Gansu beyond the railhead (a few hundred tons a day). The wire shortens the delay and raises money abroad, but transport and the war are the limits. *About 3–5 million dead* |
| Yangtze–Huai flood, 1931 | estimates from 422,499 to about 4 million; Buck's survey found 150,000 drowned and that this was less than a quarter of deaths in the first 100 days; the Lindberghs flew the aerial survey | gauge readings by telegraph (the Customs kept river and tide gauges), radio warnings, the Huai works partly built after 1914, relief by rail, river and air. *About 0.2–0.3 million dead*, depending on how much of the Huai works stands by 1931 (MODEL) |

Effect on population: about 4–8 million more people in 1932, under 2% of 500 million; Part A's "same population path" holds.

### B2. Cities

- History: cities over 50,000 held about 16.8 million people about 1900 (4–5%) and 27.3 million in 1938 (5–6%); the six largest grew 2–7% a year in the 1930s (CE 92).
- *Proposal:* about 6–7% in large cities by 1932 (MODEL). The fastest growers are Shanghai's media and electrical trades (studios, record pressing, radio assembly), Huludao and its district (CR-042, CR-057), the Manchurian railway towns, Harbin (CR-040, CR-042) and Changsha with its antimony refineries. The mining settlements of Hunan and Jiangxi stay small.

### B3. The village: land, credit, prices and pumps

| Item | History | Proposal |
|---|---|---|
| Tenure | 1934–35, 1.75 million farm families in 16 provinces: owners 47.6%, owner-tenants 20.8%, tenants 15.8% (CE 141) | unchanged except where S-6 applies |
| Land register | no complete cadastre; the land tax rested on old registers | **S-6:** in each district a Pacifican-financed work serves, an air-photographed cadastral survey and a card register of plots and tenancies; the same register carries the land tax |
| Rent | the Land Law of 1930 limits rent to 37.5% of the main crop; not enforced (CE 141) | **S-6:** the limit enforced where the register exists (canon's precedent: Komuch's credit conditional on its land law, CR-041) |
| Credit | loans from merchants 25%, landlords 24%, well-to-do farmers 18%, banks 2.4%, cooperatives 2.6% (CE 144); the Famine Relief Commission's credit societies in Hebei grew from 8 to 561 in 1923–27 | **S-5:** a Chinese farm bank lends to credit cooperatives from 1923 on the customs surplus and Pacifican silver credit; about ten times the Commission's Hebei societies by 1932 (MODEL); repayments and remittances move through the Post Office's money orders |
| Prices | per-person consumption rose about 0.5–0.6% a year, 1914/18–1931/36 (R 341); Rawski's case that information integrated markets (R 58) | **S-16:** a daily market report on the air from the mid-1920s (grain, cotton, soybeans, silk at Shanghai, Hankow, Tianjin and Huludao), read unaltered. Per-person consumption about 1.0% a year (MODEL); the report helps cash-crop districts, not Gansu |
| Pumps and power | village electricity negligible at A8.5's 5–7 kWh a head; in history Japan's farmers turned to electric pumps in the Taishō era and Formosa's to motor pumps in the 1930s | **S-16:** electric pumping where a grid passes (Huludao's district, the Shanghai delta, Formosa) and oil-engine pumps in the Pearl River delta; soybeans and bean cake through Huludao (canon); Tacoma's fertilizer from 1929 (canon) |
| Wages | Kailan's underground real wage index 100 in 1920, 209 in 1931 (R 310) | rising with the modern sector |

### B4. Labour

- History: 1,076,000 factory workers in 1933 (R 72); 12 million in handicrafts (CE 94); young women and children a large share in the mills (CE 118). The May Thirtieth movement of 1925 began in Shanghai's Japanese-owned mills, after a Chinese worker was shot on 15 May.
- Part A doubles the modern sector: about 2 million factory and mine workers by 1932 (MODEL).
- **S-7:** every Pacifican-financed work, mine and utility carries a labour article: wages paid directly to the worker and shown on payrolls the Office's methods can audit; no labour bound by debt or a contractor; no worker under fourteen. Japanese mills in China are not bound by it.

### B5. Migration

- **To Manchuria:** about 25 million journeys from Shandong and Hebei between the 1890s and 1937; nearly 500,000 a year; two-thirds returned; net over 8 million. **S-4:** about the same flow, organised by railway land offices with notices in the press and on the air; more of it settles (net 10–12 million, MODEL); the 1928–30 refugees move on the railway's trains.
- **To Pacifica:** canon counts about 4.8 million Chinese-origin Pacificans of some 37 million in 1932, against 5.8 million of Japanese origin (§26, MODEL — CR-057, CR-059). History's comparison: Hawaii had 18,254 Chinese in 1884 (22.6%) and restricted entry from 1886; 25,767 in 1900. **S-2:** accept canon's figure; Hawaii keeps its own entry rules.
- **To Japan:** about 8,000 Chinese students in Japan in late 1905 (history); Japan's school beside the Polytechnic from 1928 (§33).

### B6. Remittances and the south

- History: overseas remittances Ch.$114 million in 1903 and 316 million in 1930, about equal to foreign loan service and foreign firms' profits (69 and 35 million in 1903, 111 and 227 million in 1930; CE 179).
- **Route:** San Francisco–Oʻahu–Guam–Manila on Victoria's cable (CR-078), then the British Hong Kong cable or the Manila–Amoy–Shanghai cable (CR-080 C1, undecided). Telegraphic transfers through Pacifican and Chinese-Pacifican banks displace part of the letter-shop trade, so families in Taishan and Amoy are paid in days. That makes remittances a buffer in famine and slump.
- **S-3:** remittances about twice history's by 1929 (MODEL), concentrated in Guangdong and Fujian. Their value in yuan rises in 1929–31 as silver falls; their volume dips in 1930–32 as guest-worker contracts lapse and part of the slump's cost goes home to Canton (canon).
- **People:** Chin Gee Hee (1844–1929), a Taishan man who made his fortune in Seattle and in 1906 founded the Sun Ning Railway with about $2.75 million raised mostly from emigrants, is the historical person for remittances turned into works. In canon Seattle is Pacifican (Columbia), so he is a Chinese Pacifican. *Optional*, one addition to the cast.

### B7. Schooling, literacy, reach and language

| Item | History | Proposal |
|---|---|---|
| Literacy | Buck in the 1930s: 45% of males over seven had some schooling and 30% were literate (R 58); women's literacy far lower (Buck's figure not confirmed) | **S-8:** about 40% of males literate by the early 1930s, carried by schools and the primer, since radio teaches pronunciation and motivation, not characters; women about 5% (MODEL), to be measured by the 1931–32 census |
| Reach | radio from January 1923 (Osborn's station, Shanghai, about 500 sets sold in days); the first Chinese-run station at Harbin, October 1926, under Zhang Zuolin's patronage; Nanjing's Central Broadcasting Station, 1928, a party organ. Japan had 1.2 million radio subscribers in May 1932 | **S-8:** a second measure beside literacy: about 10–15% of Chinese see a newsreel or hear a broadcast at least monthly by 1932 (MODEL); about 0.5–1 million private sets, mostly in Shanghai, Canton, Manchuria and Formosa, plus 20,000–50,000 public listening points in county offices, schools and market towns |
| Language | the phonetic alphabet (zhuyin) promulgated 1918; Chao's national-pronunciation records, 1921; Gwoyeu Romatzyh adopted 1928 | sound film (1919–20) and the Cantonese air school (1918, CR-079) build a Cantonese public sphere tied to Pacifica; guoyu records and radio pull the other way. Y. R. Chao stays in the historical notes |
| Mass education | James Yen's Mass Education Movement (1923), a primer of about a thousand characters, the Ding county experiment from 1926; Nanjing ordered 1.5 million primers in 1929 | **S-8:** Pacifican support on China's terms: paper and presses at the one royalty for the primer, lantern slides and film for Ding county, and the movement's lessons on the market-report stations (S-12) |
| Cinema | Mingxing (1922); the first Chinese sound film, *Sing-Song Girl Red Peony*, 15 March 1931; Lai Man-wai filmed Sun Yat-sen and the Northern Expedition | Chinese studios and record pressing come about a decade earlier, at the one royalty; Shanghai's and Canton's studios make newsreels of famine, floods and the Expedition. Lai Man-wai stays in the historical notes |

### B8. Opium

- History: the edict of 1906 and the Ten Years' Agreement of 1907; Indian imports almost stopped by 1917; the warlords revived the poppy (Liu Xiang's 21st Army: opium 13.6 of 31.3 million yuan of revenue in 1930, R 18).
- Canon: Pacifican merchants may still carry opium; strict duty collection (§16, PROPOSED); the Spirit Stores at home (CR-076).
- **S-9:** the customs enforce the 1907 schedule, and their card returns make diversion visible; Formosa runs stores on the Realm's model; the poppy's revival is smaller where the railways and Nanjing reach (MODEL). No ban on Pacifican merchants.

### B9. Armies: the material base for Part C

- Armies about 500,000 in the late Qing, 1.5 million in 1913, 2 million in 1928, 2.23 million in 1935; military spending about 800 million yuan in 1928 (R 35). At that ratio each 500,000 soldiers cost about 200 million yuan a year, about a third of canon's doubled remittances.
- The material prizes of warlord politics are the railways and rolling stock, the telegraph offices (warlord politics ran on public circular telegrams printed in the papers) and, from the 1920s, the transmitters, trucks and aircraft.
- The number of soldiers and the cipher question (whether Pacifica's cipher room reads Peking, the warlords or Nanjing, and whether it stops after 1928) are Part C's.

### B10. Decisions for Part B

**DECIDED (author, 20 November 2026, 17:18):** S-1 to S-16 approved. S-17 and S-18 approved as proposed (17:25). Notes: S-3, the author asks whether remittances are taxed (answered in S-17); S-8, the author asks about women's employment, operators and programmers (answered in S-18); S-12, no ownership but influence and gravity; S-15, Chin Gee Hee and remittances turned into works approved.

| # | Decision | Recommendation |
|---|---|---|
| S-1 | Disaster deaths | 1876–79 about a million fewer; 1910–11 plague about 40,000; 1920–21 0.2–0.3 million; Swatow 1922 about a third fewer; 1928–30 3–5 million (Longhai to Xi'an by 1927, trucks beyond); 1931 flood 0.2–0.3 million |
| S-2 | Chinese Pacificans | Canon's 4.8 million in 1932; Hawaii keeps its own entry rules |
| S-3 | Remittances | About twice history's by 1929, sent by wire; up in yuan and down in volume in 1930–32 |
| S-4 | Manchuria | About the same flow, more settled (net 10–12 million); railway land offices |
| S-5 | Rural credit | A farm bank and credit cooperatives from 1923; Post Office money orders |
| S-6 | Land register and rent | Air-photographed cadastre and card register in works districts; the 37.5% limit and the land tax on it |
| S-7 | Labour | The labour article, with audited payrolls |
| S-8 | Literacy and reach | Men about 40%, women about 5%; reach 10–15% monthly; 0.5–1 million sets and 20,000–50,000 listening points; Yen's movement supported on China's terms |
| S-9 | Opium | The 1907 schedule enforced by the customs; stores on Formosa; no merchant ban |
| S-10 | Cities and living standards | About 6–7% in large cities; consumption about 1.0% a year |
| S-11 | Census | The customs' statistical office tabulates a census of Nanjing's provinces in 1931–32, the first counted Chinese census; it feeds the population script (A0). Depends on CR-080 C3 (cards at the Customs, undecided) |
| S-12 | Chinese broadcasting | Chinese state stations under the Ministry of Communications on Pacifican transmitters at the one royalty, no Pacifican ownership; Pacifican credit for them carries a public-service article (the market report, Yen's lessons, flood and storm warnings). *Author:* no ownership, but influence and gravity: the standard, the equipment, the training of engineers and announcers, programme exchange and the air school's example draw Chinese broadcasting toward Pacifica without a share in it |
| S-13 | Film | Chinese studios and record pressing at the one royalty; China may set a quota or censorship board for foreign films |
| S-14 | Warnings | China's ports join the 1897 warnings compact through the Customs' lights and telegraph, and by radio from about 1912 |
| S-15 | People | Yen carries literacy and radio, Fong statistics, Sheng the telegraph; Chin Gee Hee (approved) carries remittances turned into works: a Chinese Pacifican of Seattle who builds the Sun Ning Railway in Taishan from 1906 with emigrants' money |
| S-16 | Agriculture and food | The market report; electric and oil-engine pumping where power exists; soybeans through Huludao; Tacoma's fertilizer from 1929 |
| S-17 | Remittance tax (approved) | No tax on remittances at either end. Pacifica taxes income where it is earned (the War Revenue Act of 1915), and the employer levy on guest workers (from 1890) falls on employers, not on wages sent home; a tax on the sending would fall on the poorest earners and break the guest-worker contract's promise of wage protection. China competes for the business instead of taxing it: the Post Office's money orders and the banks' telegraphic transfers at a published fee, against the letter shops. The money reaches the state indirectly, through the customs on what remittance families buy and through the deposits it brings to Chinese banks. *Alternatives:* a small Chinese stamp duty on telegraphic transfers, which would push the trade back to the letter shops and Hong Kong; or a Pacifican charge on transfers abroad, which would contradict the guest-worker contract |
| S-18 | Women's employment (approved) | Canon's practice carries to China through its channels. The Realm examined the women its dial displaced for the computing rooms (1898), runs the halls with examined women operators and has Sophia Levy as its first order-writer (CR-077, CR-050). *Proposal (MODEL):* (1) China's 20–40 card installations (B0) are staffed by examined women operators from the 1910s, the first cadre trained at the Office's school from among Chinese-Pacifican women; by 1932 a few thousand card operators and a few dozen order-writers who set up the card-programmed calculators at the Customs, the Post Office, the railways and the census of 1931–32 (S-11); (2) women operators in the telephone exchanges of Shanghai, Canton, Huludao and Formosa and women announcers on the state stations; (3) the labour article (S-7) carries the same wage for the same work (CR-071) into Pacifican-financed mills, where young women are a large share (CE 118); (4) the Polytechnic of Formosa and the Pacifican scholarships admit women on the same examination from the start (CR-037: the examination, never a quota). About 10,000–20,000 women in offices, exchanges, card rooms and stations by 1932, beside about 600,000–700,000 in the mills (history had about 520,000 textile workers of both sexes in 1933, CE 99) |

**For Part C:** women's place in the Nationalists' programme and in the 1931–32 census's results; the cipher question; the number of soldiers; the treaty ports and extraterritoriality; Britain's position and the 1913 Reorganisation Loan; Korea's rice and the Yalu crossing.

**Tradeoffs that cannot be avoided**
1. **Rent and the Nationalists' base.** Enforcing the limit where the register exists takes income from landlords, who are much of the Nationalists' rural support. Not enforcing it leaves Mao his issue (Part C).
2. **The labour article and Japan's mills.** Japan's mills in China are not bound by it, and labour unrest starts there, as in 1925.
3. **Japan's receivers and China's tariff.** If CR-080 X-3 gives Japan consumer electronics, China's radio, record and telephone boom is Japan's largest new market and the cheapest offset to its cotton loss (A8, tradeoff 1). It works against Chinese makers at Shanghai and Huludao and against the tariff of 1928. Part B does not assume either answer.
4. **A party station and Pacifica's own rule.** Pacifica gives no wavelength to a party (CR-079). Nanjing's central station was a party organ; equipping it breaks the rule, and refusing offends Nanjing. S-12's state stations are the middle course and may not satisfy the party.
5. **Pacifican films and Chinese censorship.** The Realm's films fill the Pacific's screens (CR-079). A quota or a ban on a film that insults China (history's *Welcome Danger* protest at Shanghai in February 1930) is the price of S-13.
6. **South and north, Cantonese and guoyu.** Remittances, the Pacific line and Cantonese film and radio enrich and bind Guangdong and Fujian to Pacifica, while guoyu radio and records bind the nation to Nanjing. The south's money is also the base of a southern government (Part C).
7. **Literacy, reach and nationalism.** More readers and listeners strengthen the demand to recover Formosa, Huludao and Tsingtao; reach grows faster than literacy.
8. **Radio in Manchuria.** Chinese broadcasting at Mukden and Huludao joins Huludao's customs among the Japanese officers' grievances (canon); the 1931 plot is still stopped.
9. **Relief and the warlords.** Rail and truck relief works only while the lines' owners let grain pass, as in 1920–21 and not in 1928–30.
10. **Women in offices.** Women in the card rooms, exchanges and stations come first from Chinese-Pacifican and mission-school families; their visibility is contested at home in the way it was in history's treaty ports, and it ties women's careers in China to Pacifican institutions.
11. **The Chinese Pacificans.** At about 13% of residents they are larger than any Chinese community abroad in history; the story must not become about one diaspora (CR-037), and Hawaii's concern for its own people stands.

**Sources outside the four books (Part B), checked 20 November 2026**
- Famines: Wikipedia, *Northern Chinese Famine of 1876–1879*, *Chinese famine of 1920–1921*, *Chinese famine of 1928–1930* (citing Lillian Li, 2007); DisasterHistory.org; Pierre Fuller, *Famine Relief in Warlord China* (2019); a newspaper report on the Red Cross famine roads (Utah Digital Newspapers).
- Manchurian plague: Wikipedia, *Manchurian plague*; Wu Lien-teh, *First Report of the North Manchurian Plague Prevention Service* (1913).
- Swatow typhoon: Wikipedia, *1922 Shantou typhoon* (citing *Monthly Weather Review*, August 1922); *Evening Star* and *Manawatu Herald*, August 1922.
- 1931 flood: Wikipedia, *1931 China floods*; Guinness World Records.
- Storm signals: Hong Kong Observatory (Zikawei's flag signals from 1884); *Nature* (1884) on Dechevrens and the Customs' observers; customs gauge records (Woosung from 1880; Hankow gauge in the Customs' 1919 survey).
- Longhai railway: Wikipedia, *Longhai railway*.
- Radio: Wikipedia, *Radio Corporation of China*, *Broadcasting Corporation of China*, *Radio in China*; Radiomuseum, *Radio history of Shanghai*; NHK Monthly Report (1.2 million subscribers, May 1932).
- Language: Wikipedia, *Yuen Ren Chao*, *Gwoyeu Romatzyh*; Zhou Enlai's summary on the phonetic alphabet (pinyin.info).
- Film: Wikipedia, *Sing-Song Girl Red Peony*, *History of cinema of China*, *Lai Man-Wai*; University of Washington News on *Welcome Danger* (2014).
- Chin Gee Hee: Wikipedia, *Chin Gee Hee* and *Sun Ning Railway Company*; HistoryLink essay 23547.
- Pumps: Tsuru, "Irrigation pumps in late colonial Taiwan", *Modern Asian Studies* (2023); Jinnouchi, *Electric irrigation and local society* (UNU, 1983).
- Circular telegrams: Rong Wu, "The making of 'public opinion'", *Modern Asian Studies* (2023).
- Philippine Chinese: Wikipedia, *Chinese Filipinos*.
- Migration, Hawaii, cooperatives, Land Law, Yen, opium, May Thirtieth: as in the first draft (Gottschang and Lary; FRUS 1885 and 1906; ILO 1934; Taiwan Today; Wikipedia; Britannica).
- Women's education: Ginling College (founded 1913, opened 1915), the first institution in China to grant women bachelor's degrees (Wikipedia, *Ginling College*); China's first official women students abroad, to Japanese girls' schools in 1905 (Heidelberg University repository); the Shanghai Women's Commercial and Savings Bank, founded by Chinese women (*Evening Post*, 2 May 1927).
- Remittances: Harris on the remittance firms and the Post Office (*Journal of Asian Studies*, 2014; Illinois dissertation); Benton and Liu, *Dear China* (2018). No source found for a tax on remittances in this period.
- Not confirmed and not used as figures: Buck's women's literacy figure; electric irrigation at Wujin; national cooperative counts for 1931–35; motor-road kilometres for 1921 and 1927; a 1936 ban on Cantonese films.

## C. The political timeline (draft)

Built on Parts A and B as decided and on canon's turning points. Each period gives canon with its label, the historical baseline (*Hist.*, sources at the end of this part) and the proposals, which are measured against the 1932 target in A8: a strong, solvent China aligned with Pacifica, at minimal cost to Japan. Decisions are numbered P-1 to P-22. Part C answers CR-080's questions D0.1–D0.6 and the items Parts A and B left for it; D0.7 (the Chinese Pacificans) was answered by S-2, S-3 and S-15, and P-3 and P-21 add their politics.

### C0. What canon, Part A and Part B already decide

**Canon's fixed points** (§ numbers are the storyline's):
- 1860–63: Ward's company holds Shanghai and leaves the Qing's service after Suzhou (CR-074).
- About 1878–80: Korea's first Western treaty is with Pacifica, through Li Hongzhang's mediation (§14).
- 1884–85: the Keelung squadron without a battle; a Chinese–Pacifican coal company; railway and fleet-rebuilding credit (§16, PROPOSED).
- 1885: the Customs Inspectorate under Fong by China's appointment, with Li's backing (§16).
- 1894–95: the armistice. Korea is independent and neutral, the indemnity moderate, no mainland is ceded, Formosa stays Chinese under the Revenue Convention, and "the Qing retain solvency" (§25).
- 1898–99: Liaodong stays Chinese through Victoria's negotiation with Cixi; China recovers the Amur's north bank and pledges the Liaodong Gulf coast to no power (§25, CR-042).
- After 1898: Honolulu and San Francisco shelter reformers and revolutionaries; a limited Boxer relief contingent withdraws promptly and turns its indemnity into scholarships (§25, PROPOSED).
- 1909: the Huludao trust under a Qing commission; Xu Shichang as viceroy (§27, CR-042, PROPOSED).
- 1911–12: the Qing falls and Julian backs Sun (§27). PROPOSED: Sun tours Pacifica's Chinese communities, becomes provisional president, yields to Yuan, loses the Second Revolution of 1913 and lives in exile in Honolulu.
- 1915: Victoria blocks the worst of the Twenty-One Demands (§28, CR-040, PROPOSED).
- 1915–16: Yuan's monarchy; Julian leaves him to his fate. PROPOSED: Pacifica funds Sun in Canton while working with Zhang Zuolin (§29).
- 1918: a Chinese brigade guards the Manchurian line, "since Peking's price is that Chinese soldiers guard it" (§31, CR-041, PROPOSED).
- 1919: Shandong returned to China at The Hague (§30, CR-043).
- 1921: the Treaty of Harbin, signed in a Chinese city. Russia's extraterritorial rights, concessions and indemnity share are renounced, and Mongolia returns to Chinese suzerainty under its own Mongol government (§32, CR-031, PROPOSED). By 1922 the settlement is a standing alliance of Pacifica, Japan, China and federal Russia (§32, CR-040 R11, APPROVED).
- 1920s: Whampoa on Pacifican money without a Soviet bargain; Sun dies in 1925 and Chiang succeeds him; the Northern Expedition; Julian obtains Japan's withdrawal at Jinan; Japanese officers kill Zhang Zuolin in June 1928 and Zhang Xueliang joins Nanjing (§33, PROPOSED). The Treaty of Nanjing with the Concord returns the customs and the tariff in 1928–29 (§33, CR-039, APPROVED).
- 1931: the Manchurian plot is stopped, no client state is made, and Puyi remains in Tianjin (§35).
- No Soviet state survives 1920 and there is no communism in China; Mao is a nationalist (CR-080 X-8).

**Rules from Parts A and B that become political rules**
- **Works, not factions.** No Pacifican lending to factions in Peking in 1916–28 (A8.4). Loans go to Chinese-owned works with published accounts and the labour article (S-7).
- **State, not party.** Pacifican transmitters go to state stations (S-12).
- **No ownership beyond canon's holdings** (A8): influence comes from credit, standards, schools, the Chinese Pacificans and the guarantee.

**What this means for the timeline.** Canon has Pacifica choose a Chinese leader twice, Sun in 1911 and Nanjing in 1928. Between those dates it deals with whoever holds Peking, the provinces and Manchuria, through revenue, works and people. The decisions below keep to that.

### C1. 1860–1894: Self-Strengthening with a partner (D0.1, D0.2)

- *Hist.:* the Educational Mission sent 120 boys to New England from 1872, and the Qing recalled it in 1881, partly because it thought the boys too Americanised. Its men included Tang Shaoyi (Columbia, class of 1882), Liang Dunyan (Yale), Liang Cheng (Phillips Academy, then Amherst) and Zhan Tianyou (Yale, 1881).
- *Canon:* the mission studies in San Francisco with naval-academy places and is not recalled (PROPOSED; CR-080 D0.1). By 1894 its men are in their early thirties and serve the telegraph, Kaiping, the China Merchants' line (its Pacific line from 1880, A8.9) and the customs.

**P-1. The partner before 1894.** *Proposal:* Pacifica's partner is Li Hongzhang's Beiyang administration and Sheng Xuanhuai's enterprises, not the court and not the provinces at large. Li mediates Korea's treaty and backs Fong (canon). The mission's men work in Li's and Sheng's offices: the telegraph administration from 1881, the coal and steamship companies, the Tianjin schools. Victoria's friendship with Cixi belongs to 1898–99 and does not reach the arsenals.

**P-2. The fleet credit of 1885.** Pacifica has been Japan's ally since 1870–71 (§14). *Proposal:* the fleet-rebuilding credit of 1885 (canon, PROPOSED) is lent in money. China buys its cruisers in Britain and Germany as in history, and no Pacifican yard builds and no Pacifican officer serves in a Chinese warship. The mission's naval graduates go mainly to the merchant line. This is why the Beiyang fleet loses in 1894 as canon requires, and why Japan does not read the credit as arming its enemy.

### C2. 1895–1901: a milder defeat, the reformers and the Boxers

- *Hist.:* the Hundred Days of reform (June–September 1898) ended in Cixi's coup. Kang Youwei founded the Baohuanghui (Chinese Empire Reform Association) at Victoria, British Columbia, on 20 July 1899, with Liang Qichao as vice-president; its chapters spread through the Americas, and at one time most of Honolulu's Chinese supported it. Sun had founded the Xingzhonghui at Honolulu on 24 November 1894. In 1900 the southern viceroys kept their provinces out of the court's war (the Southeast Mutual Protection).
- *Canon:* the armistice and the Revenue Convention leave the Qing solvent; Germany still takes Kiaochow, and Pacifica takes nothing (§25). Russia enters Manchuria during the Boxer rising (§26, PROPOSED).

**P-3. The reformers in exile.** *Proposal:* the Hundred Days fail as in history, because the court is unchanged. Pacifica gives Kang, Liang and Sun's men asylum and the right to organise among the Chinese Pacificans, but no arms, no credit and no ships for risings, and Victoria tells Cixi so. Her friendship with Cixi protects the exiles' lives, not their plans. The Baohuanghui and Sun's society both grow fastest in San Francisco and Honolulu, so that by 1905 the two rival Chinese parties abroad are largely Pacifican-based and compete for the same remittance money (S-3).

**The Boxers.** Canon's contingent guards the legations, withdraws early, and Pacifica's indemnity share goes to scholarships and, after 1901, to the conservancy (A8.10). No decision is needed here.

### C3. 1901–1911: the New Policies with more money, and the fall (D0.3)

- *Hist.:*
  - the examinations were abolished in 1905;
  - in May 1906 an edict put the whole customs service under a Revenue Council, with Tieliang as superintendent and Tang Shaoyi as associate minister;
  - Xu Shichang was the first viceroy of the Three Eastern Provinces (1907–09);
  - in 1908 the court set a nine-year programme for a constitution;
  - the provincial assemblies were elected in 1909 by about 1.7 million registered voters, 0.42% of the population, and the National Assembly met in 1910;
  - the cabinet of 8 May 1911 had thirteen members, eight of them Manchu, one Mongol and four Han, seven from the imperial clan, and the provincial assemblies' federation protested at once;
  - on 9 May 1911 Sheng Xuanhuai nationalised the trunk railways, and on 20 May he signed the Huguang loan with the four-power consortium of British, French, German and American banks;
  - the Sichuan Railway Protection League formed on 17 June, and troops sent from Hubei to suppress it gave the Wuchang garrison its chance on 10 October.
- *Canon and Parts A–B:* more revenue (a moderate indemnity, a published customs), more railways (11,000–12,000 km by 1911, A8.4), a Chinese Manchuria, the Polytechnic of Formosa (1906) and the mission's men in office.

**P-4. Why the Qing still falls.** Canon fixes the fall. *Proposal:* the New Policies go further in money, railways and trained men, and the court still fails politically, as in history: the princes' cabinet of May 1911 alienates the constitutionalists, and the railway nationalisation sets Sichuan alight. Pacifica is not in the Huguang consortium, because its rule is to lend to Chinese-owned lines on the customs with no foreign management (A8.4), so the crisis of 1911 is not Pacifica's. The mission's men are divided, as they were in history: Tang Shaoyi serves Yuan in the negotiations of 1911–12, and Liang Dunyan, foreign minister in the princes' cabinet, stays a monarchist.

**P-5. The customs in the revolution.** *Hist.:* in January 1912 the diplomatic body made the Inspector-General the trustee of all customs revenue, deposited in foreign banks at Shanghai for the loan service, so that he released the surplus only to the government the powers recognised. *Proposal:* Fong does the same, because the customs secure the loans Pacifica's savers hold. Pacifica recognises the Republic on the abdication (12 February 1912), not a person, and so the trusteeship that serves the Republic in 1912 serves Yuan from March. This is Fong's divided duty again: Julian backs Sun, and Fong's revenue goes to Peking.

### C4. 1912–1916: Yuan, the loans and the Demands

- *Hist.:* Tang Shaoyi was the Republic's first premier from 13 March to 27 June 1912 and resigned over Yuan's disregard for the cabinet and the law. The Kuomintang won the elections of 1912–13; Song Jiaoren, who was to lead the cabinet, was shot at Shanghai station on 20 March 1913. On 18 March 1913 Wilson withdrew his government's support from the American bankers in the consortium. On 26 April 1913 Yuan signed the £25 million Reorganisation Loan with the British, French, German, Russian and Japanese banks without the parliament's consent, secured on the salt revenue under a foreign-inspected salt administration. The Second Revolution of July 1913 was crushed in about two months; Yuan banned the Kuomintang in November 1913 and dissolved the parliament in January 1914. In 1915 Japan's ultimatum of 7 May forced acceptance of the modified Demands on 25 May, and 9 May became a day of national humiliation and the occasion of a boycott.

**P-6. The Reorganisation Loan.** *Proposal:* Pacifica stays out and says why: it does not lend to arm a president against an elected parliament. With the Union's bankers also out, Britain leads the five-power loan and its salt inspectorate. Japan, not yet in the Concord, takes its share. Britain gains a second foreign-run revenue in China beside Fong's customs, and Japan finances the man Pacifica's candidate is fighting. This is the first instance of canon's criticism of Julian's bargains in China.

**P-7. Tang Shaoyi.** D0.1 asks which of the mission's men matter. *Proposal:* Tang Shaoyi is the one addition to the cast from the mission, because three of his historical posts touch Pacifica. In 1906 he is the associate minister to whom Fong reports. In 1912 he is premier and resigns. In 1929, as in history, he heads Zhongshan, the county Nanjing makes a model county; in canon it is the first county where the card register and the rent limit (S-6), the farm bank (S-5) and the labour article all apply. Zhan Tianyou (the Peking–Kalgan line, 1905–09, and the Canton–Hankow line after 1912; died at Hankou in April 1919), Liang Cheng (the scholarships) and Liang Dunyan stay in the historical notes.

**P-8. The Twenty-One Demands.** In canon Japan holds no lease in Manchuria or Shandong, and Hanyeping's debt is serviced on Pacifican credit (A8.6). *Proposal:* what Japan still obtains in 1915 is commercial: residence, leasing of land for business and mining rights for Japanese along the Manchurian line, and the Daye ore contract (A8.6). Victoria's intervention removes the fifth group of advisers and police and any ultimatum. There is no 9 May, and the boycott of 1915 is short.

### C5. 1916–1923: warlords, war, The Hague and Harbin

- *Hist.:*
  - Yuan died in June 1916;
  - the Manchu restoration of 1–12 July 1917, in which Liang Dunyan served as Zhang Xun's foreign minister;
  - China declared war on Germany on 14 August 1917; some 140,000 Chinese labourers served the British and French armies;
  - Sun's Constitutional Protection government at Canton from 1917;
  - Xu Shichang, the only civilian president of the warlord years, from 10 October 1918 to 2 June 1922;
  - the Nishihara loans of 1917–18 to Duan Qirui (A8.4);
  - the Zhili–Anhui war of July 1920 and the first Zhili–Fengtian war of 1922;
  - Hunan's provincial constitution, promulgated on 1 January 1922;
  - Chen Jiongming's federalism in Guangdong and his attack on Sun on 16 June 1922.
- *Canon:* the Chinese brigade (1918), Shandong at The Hague (1919), the Treaty of Harbin (1921), the standing alliance (1922), Huludao opened (1914, PROPOSED) and its industrial district under Wang Yongjiang (1923, CR-057).

**P-9. Who signs for China.** *Proposal:* the recognised government in Peking signs, and the southern government joins China's delegation. At The Hague in 1919 China sends one delegation with Canton's men in it, as the Paris delegation had in history, and Pacifica asks for that. Xu Shichang's government signs the Treaty of Harbin in 1921 with Zhang Zuolin's consent for Manchuria. The standing alliance binds the government of China, which passes from Peking to Nanjing in 1928. Xu, who chartered Huludao in 1909, is president when China joins the alliance, so the Huludao link of CR-042 carries through.

**P-10. No May Fourth outrage.** *Proposal:* the New Culture movement and the student unions still form. With Shandong returned, the students' anger turns to the Anfu clique's loans and to the treaty system that remains: extraterritoriality, the concessions and the two foreign-run revenues, Fong's customs and Britain's salt. "Abolish the unequal treaties", which the Nationalists took up in 1924, becomes the movement's cry five years earlier. *Hist.:* there were significant boycotts of Japanese goods in 1908, 1909, 1915, 1919, 1925 and 1928, and then almost continuously from 1931 (Gerth, after Remer). In canon the boycotts of 1915 and 1928 are short and those of 1919 and 1931 do not happen. That is the political return to Japan for the cotton tariff of 1928 (A8, tradeoff 1).

**P-11. The federalists and the south.** *Proposal:* Pacifica gives federalism no political support; canon has it fund Sun's line, which is unification. Its works rule makes it deal with provincial governments, though, and in practice that rewards Hunan under its constitution and Chen Jiongming's Guangdong, which publish accounts and accept the labour article. This is a quarrel with Sun before 1922. Mao takes part in Hunan's self-government movement of 1920, as in history.

**P-12. The Canton customs, 1923.** *Hist.:* in December 1923 Sun threatened to seize the Canton customs surplus, and foreign warships gathered at Canton to stop him. His government cited the precedent of 1919–20, when part of the surplus had been released to the south. *Proposal:* Fong proposes a works account. The surplus collected at the southern ports is held under published accounts for works in the provinces where it is collected (the Canton–Hankow line's southern section, the Pearl River works, the Swatow warnings, S-14) and paid to contractors, never to armies. Peking protests, Sun accepts because his province gets the works, and no warships are needed. Britain resents a Pacifican Inspector-General deciding what the powers decided in history. The formula is the precedent for the Nationalists' own finances (P-14).

### C6. 1923–1928: the Nationalists' model and the Expedition (D0.4, D0.5, D0.6)

- *Hist.:*
  - Chiang Kai-shek led Sun's military mission to Moscow from 2 September to 29 November 1923;
  - the Kuomintang's first congress (Canton, 20–30 January 1924) reorganised it on the Soviet model, declared that there was no restriction of sex in political activities and set up a Central Women's Bureau;
  - Whampoa opened on 16 June 1924;
  - Sun died on 12 March 1925;
  - the May Thirtieth shooting of 1925 and the Canton–Hong Kong strike and boycott (June 1925 to October 1926; at Shakee on 23 June 1925 British and French troops fired on the marchers);
  - Mao was acting head of the Nationalists' propaganda department from October 1925 to May 1926 and director of the sixth session of the Peasant Movement Training Institute in 1926;
  - the Northern Expedition began on 9 July 1926;
  - the British concessions at Hankou and Jiujiang were returned by agreement in February and March 1927;
  - Mao's report on the Hunan peasant movement (March 1927);
  - the Jinan incident of 3 May 1928, the killing of Zhang Zuolin on 4 June, and Zhang Xueliang's change of flag on 29 December 1928.

**P-13. Chiang's mission of 1923.** *Proposal:* Sun sends Chiang to Pacifica instead of Moscow, for about three months in 1923: to the Companies' school at Sacramento, the Polytechnic, a county board and the Party's machine. He comes back with a plan for Whampoa and a view of how an examined party governs.

**P-14. The Nationalists' model (D0.4).** *Proposal:* the Kuomintang takes three things from the Prosperity Party and refuses one.
- *It takes:*
  - examined cadres: party schools whose examinations qualify for posts;
  - published accounts of the party's and Canton's finances, with T. V. Soong's Central Bank at Canton (1924, as in history) and the works account of P-12 as models;
  - its own wire and press, under the Wireless rule of S-12.
- *It refuses* the open ballot. Sun's three stages stay, and tutelage means one party without elections until a constitution.
- *Whampoa:* its instructors are Chinese officers trained in Pacifica (Chinese Pacificans from the Sacramento school and the mission's sons) under private contract. No Pacific Company serves it, because the Companies serve China only by treaty with the recognised government (CR-074).
- *The money:* Pacifica's money for Whampoa (canon) is indirect, through the Chinese Pacificans' subscriptions and the works account, which frees Canton's own revenue for the school.
- *The result* is a party that publishes its accounts and examines its cadres but rules without voters, with the tension that brings to the warlords and later to its own officers.

**P-15. Labour in 1925.** *Proposal:* the May Thirtieth movement and the Canton–Hong Kong strike happen, led by the Nationalists' labour bureau and the seamen's union, since there is no Communist party. They are aimed at Britain and at the Japanese mills where the shooting began (B4). The strike committee exempts the China Merchants' Pacific line and Pacifican firms that carry the labour article, so the boycott moves Hong Kong's trade to Canton, Chinese ships and Pacifica's. Britain pays most of the cost; Japan's mills pay some.

**P-16. The split of 1927, without communists.** *Proposal:* the Nationalists still split in 1927, over land and labour. The left at Wuhan (Wang Jingwei, the peasant and labour bureaus) stands against Chiang at Nanjing with the Shanghai bankers and officers whose families own land. *Hist.:* on 21 May 1927 officers at Changsha turned on the Hunan peasant associations. In canon the associations are dissolved and their leaders dismissed, not hunted down, and there is no Shanghai massacre because there is no Communist party to purge. Wuhan rejoins Nanjing later in 1927, as in history. Land stays the party's open question, and the rent limit of 1930 (S-6) is its answer on paper.

**P-17. Land (D0.5).** S-6 has already decided the practice: the rent limit is enforced where a Pacifican-financed register exists. *Proposal:* Pacifica asks nothing of Nanjing's land law as a whole, unlike Komuch (CR-041), because China's land is China's and the Concord does not guarantee China's government, only its frontiers. The conditions sit in the works contracts district by district. By 1932 the districts with a register are the showcase, and the rest of China is the argument.

**P-18. Mao Zedong (D0.6).** *Hist.:* he graduated from Hunan's First Normal School in 1918, founded the *Xiang River Review* in 1919, argued for Hunan's self-government in 1920 and was elected an alternate member of the Nationalists' Central Executive Committee in 1924. *Proposal:*
- 1921–24: no Communist party to found; he joins the Nationalists in Hunan.
- 1925–27: propaganda and the peasant institute as in history; his Hunan report of 1927 is a Nationalist document, and he is on Wuhan's side in the split.
- 1928–31: out of favour in Nanjing, he goes back to Hunan to run the register and the rent limit in the works districts along the Canton–Hankow line, and the census of 1931–32 (S-11) prints his districts' tables.
- 1932, aged thirty-eight: a member of the Central Executive Committee and head of the party's peasant department, the leading voice for enforcing the rent limit everywhere, against Nanjing's officers and bankers. He is a rising leader and not yet a successor to Chiang.

### C7. 1928–1932: Nanjing with the customs

- *Hist.:*
  - the disbandment conference of January 1929 meant to cut the armies outside Manchuria to sixty-five divisions of 11,000 men, about 715,000, within a limit of 800,000, and failed;
  - the Central Plains war of May–November 1930 against Yan Xishan, Feng Yuxiang and Li Zongren was decided when Zhang Xueliang declared for Chiang on 18 September 1930;
  - Nanjing's mandate of 28 December 1929 declared extraterritoriality abolished from 1 January 1930; Britain and the Union agreed to treat that date as the start of a gradual abolition, and the negotiations of 1931 were broken off after Mukden;
  - Weihaiwei was returned on 1 October 1930;
  - Hu Hanmin was put under house arrest on 28 February 1931; the National People's Convention met in May 1931, and the Provisional Constitution of the tutelage period was promulgated on 1 June 1931;
  - an opposition government formed at Canton in May 1931 under Wang Jingwei and Eugene Chen; in January 1932 Wang and Chiang agreed to lead together, Wang as premier from 28 January;
  - the Civil Code, promulgated in 1929–30, gave daughters equal inheritance.
- *Canon:* the customs and tariff recovered; the Formosan administration a Concord affair with a Japanese deputy (PROPOSED); the Huludao trust until its bonds are paid; the 1931 plot stopped.

**P-19. Soldiers.** *Hist.:* about 2 million under arms in 1928 and 2.23 million in 1935 (B9). *Proposal (MODEL):* about 1.7–1.9 million in 1928 and 1.3–1.5 million by 1932. Fewer famine refugees join the armies (S-1), and more men find work in the modern sector and the Manchurian settlement (S-4). The disbandment of 1929 partly works because the recovered customs pay discharged soldiers through the works: railway building, the conservancy and the land offices, under the labour article. The Central Plains war still happens, because it is about power, and Zhang Xueliang still decides it.

**P-20. Extraterritoriality and the concessions.** *Proposal:* the Concord's crowns, Pacifica and Japan together, renounce their consular jurisdiction from 1 January 1930, answering Nanjing's mandate on its own date. For a term of years (proposal: ten) the International Settlement at Shanghai and the Manchurian line's joint-management zone keep mixed courts with foreign assessors. Without Mukden, Britain and the Union sign their treaties in 1932. The concessions follow history (Hankou and Jiujiang in 1927, Weihaiwei in 1930); the Shanghai Settlement and the French Concession remain in 1932; Pacifica keeps only the Tsingtao anchorage (canon). *Alternative:* Pacifica renounces alone and Japan keeps its courts until a treaty of its own, which singles Japan out and gives its officers another grievance.

**P-21. Canton in 1931.** Remittances, the Pacific line and Cantonese film and radio make Guangdong the richest base outside Nanjing's control (B, tradeoff 6). *Proposal:* Pacifica recognises only Nanjing, a party to the Treaty of Nanjing; the customs pay Nanjing; remittances stay untouched and untaxed (S-17). Without Mukden the reconciliation of January 1932 needs another cause, and the 1931 flood and Nanjing's finances supply it: Wang becomes premier and Chiang keeps the army, as in history.

### C8. Questions carried from CR-080 and Parts A and B

**P-22. The cipher question.** The cipher room never reads a partner's traffic (CR-077 D-6: Germany 1914–18 and the Reds and Whites 1918–20 are read, Japan never). *Proposal:* it never reads any Chinese government, before or after China joins the standing alliance in 1922, and it reads no warlord. Pacifica's picture of China comes from the customs returns, the Chinese Pacificans and the open circular telegrams of warlord politics. That is why Feng Yuxiang's coup of October 1924 and the killing of Zhang Zuolin in 1928 (canon: the officers Thalassia does not see coming) surprise it. *Alternative:* read the factions' military traffic in Manchuria in 1918–22 for Siberian security, which breaks the partner rule with Zhang Zuolin.

**Other items, with recommendations (decided with P-22's table below)**
- **The party station (S-12, B tradeoff 4).** Pacifican transmitters go only to the Ministry of Communications' stations. Nanjing's party station of 1928 is equipped elsewhere, and the state stations carry the party's hour at a published rate, on the Wireless Act's model of 1913, though under tutelage there is no other party to buy time.
- **Women in the Nationalists' programme and the census.** The programme follows history: equality in the 1924 manifesto, the Women's Bureau, and the Civil Code's equal inheritance. The census of 1931–32 (S-11), set up and run largely by the women operators and order-writers of S-18, prints for the first time county tables of women's literacy (about 5%, S-8), schooling, employment and age at marriage. The Women's Bureau uses them in its demands on the school law of 1932.
- **Britain's position (A8, tradeoff 6).** Britain keeps Hong Kong, its Yangtze trade, the salt inspectorate of 1913 and the lien on the Mukden–Huludao line (canon). It bears most of the nationalist anger of 1925–27 and turns to treaty revision from 1926–27, as in history. Its retreat after 1927 (canon) makes it give way faster in China, Hong Kong excepted. Pacifica does not bid for British holdings.
- **Korea's rice and the Yalu.** *Hist.:* Japan's rice imports from Korea grew from 2.79 million koku a year in 1919–23 to 6.65 million in 1929–33 under the rice plan of 1920. In canon Korea is independent, so the rice comes by contract on Japanese credit, and the Korean farmers in Manchuria are Korea's citizens, not Japan's subjects. A dispute like Wanbaoshan (July 1931) becomes a Sino-Korean matter for the guarantors of 1894, and Japan's army loses a pretext. The Yalu crossing and the Antung–Mukden link belong to CR-080 Part E. *Recommendation:* a Chinese line with Japanese transit rights, under the Treaty of Nanjing's transit guarantee like the Harbin line.
- **The south as a rival base** is P-21; the treaty ports are P-20.
- **Mongolia and Tibet.** Mongolia is canon's (Chinese suzerainty under its own government, 1921); its government after the Bogd Khan's death in 1924 stays OPEN. Tibet follows history and is outside this CR.

### C9. Decisions for Part C

| # | Decision | Recommendation |
|---|---|---|
| P-1 | The partner before 1894 | Li Hongzhang's Beiyang administration and Sheng's enterprises; the mission's men in their offices |
| P-2 | The fleet credit of 1885 | Lent in money; no Pacifican-built warships or Pacifican officers in Chinese warships; the mission's naval men to the merchant line |
| P-3 | The reformers in exile | Asylum and freedom to organise for Kang, Liang and Sun's men; no arms or credit for risings; both parties grow among the Chinese Pacificans |
| P-4 | The fall of the Qing | As history: the princes' cabinet and the Sichuan railway; Pacifica outside the Huguang consortium; the mission's men divided |
| P-5 | The customs in 1911–12 | Fong as trustee for the loan service; the surplus to the recognised government; Pacifica recognises the Republic on the abdication |
| P-6 | The Reorganisation Loan | Pacifica stays out and says why; Britain leads and runs the salt inspectorate; Japan takes its share |
| P-7 | Tang Shaoyi | Added to the cast: the Revenue Council (1906), premier (1912), the Zhongshan model county (1929) as the showcase of S-5, S-6 and S-7 |
| P-8 | The Twenty-One Demands | Only commercial rights along the Manchurian line and the Daye contract; no fifth group, no ultimatum, no 9 May |
| P-9 | Who signs for China | Peking signs, with Canton in China's delegation at The Hague; Xu Shichang's government signs at Harbin; the alliance passes to Nanjing |
| P-10 | No May Fourth outrage | The students turn on the Anfu loans and the treaty system, Fong's customs included; boycotts of Japan in 1915 and 1928 short, none in 1919 or 1931 |
| P-11 | The federalists | No political support; works contracts with provinces that publish accounts, which favours Hunan and Guangdong |
| P-12 | The Canton customs, 1923 | A published works account for the southern ports' surplus, paid to contractors; no warships |
| P-13 | Chiang's mission of 1923 | To Pacifica instead of Moscow |
| P-14 | The Nationalists' model | Examined cadres, published accounts, own wire; tutelage without elections; Whampoa's instructors Pacifican-trained Chinese under private contract; Pacifican money indirect |
| P-15 | Labour in 1925 | May Thirtieth and the Canton–Hong Kong strike led by the Nationalists' labour bureau and the seamen's union; aimed at Britain and the Japanese mills |
| P-16 | The split of 1927 | Over land and labour, without a massacre; Wuhan rejoins Nanjing |
| P-17 | Land | No condition on Nanjing's land law; conditions in the works contracts district by district (S-6) |
| P-18 | Mao | Nationalist from the start; the peasant work of 1925–27; the Hunan register 1928–31; in 1932 head of the peasant department and on the Central Executive Committee, not yet a successor |
| P-19 | Soldiers | About 1.7–1.9 million in 1928, 1.3–1.5 million by 1932 (MODEL); demobilisation through the works; the Central Plains war still fought |
| P-20 | Extraterritoriality | Pacifica and Japan renounce together from 1 January 1930, with mixed courts for ten years at Shanghai and in the railway zone; Britain and the Union sign in 1932 |
| P-21 | Canton in 1931 | Recognition of Nanjing only; remittances untouched; Wang and Chiang reconcile in January 1932 for internal reasons |
| P-22 | The cipher question | No Chinese government and no warlord read at any time; open sources only |
| — | The party station, women and the census, Britain, Korea's rice and the Yalu, Mongolia and Tibet | As in C8 |

**Tradeoffs that cannot be avoided**
1. **Neutral revenue and the chosen leader.** The trusteeship that protects Pacifica's savers (P-5) pays Yuan in 1912–16 and Peking's factions until 1928, while Julian backs Sun. Canon's criticism of Julian's bargains starts here.
2. **Staying out of the 1913 loan.** It keeps Pacifica's hands clean and gives Britain the salt and Japan a creditor's place with Yuan.
3. **The students' target.** Without Shandong, nationalism turns on the treaty system, and Fong's customs is part of it. Pacifica becomes a target before Japan does, and the recovery of 1928–29 is its answer.
4. **A party that publishes its accounts and has no voters.** The Prosperity Party model gives the Nationalists discipline and credit, and the open ballot that Pacifica made its own in 1911 is the part they refuse. Pacifica's example is a standing reproach to tutelage.
5. **Works contracts as politics.** Conditions district by district (P-11, P-17) reward the provinces and districts that accept them, so Pacifica's money takes sides in the provinces without saying so.
6. **Land.** The 1927 split and Mao's career both come from the rent question, and enforcing it only in the works districts leaves the rest of China to the landlords and Mao his issue.
7. **Extraterritoriality.** Renouncing with Japan costs Japan its consular courts outside the railway zone and adds to its officers' grievances. Holding out with Japan would keep China's main grievance against both crowns.
8. **The cipher rule.** Reading no Chinese government keeps faith with an ally and leaves Pacifica blind to coups, as canon already has it in 1928.
9. **Britain.** Most of the political cost of a nationalist China aligned with Pacifica falls on Britain: the customs, the 1925 boycott, the concessions. Britain's retreat after 1927 in canon absorbs it, but London keeps the record (as it does at Tomsk, CR-044).
10. **Canton.** Pacifica's remittances, line and films build the south that challenges Nanjing in 1931 (B, tradeoff 6), and recognising only Nanjing limits what it can do there.

**Sources outside the four books (Part C), checked 20 November 2026**
- Educational Mission and its men: Wikipedia, *Tang Shaoyi*, *Liang Cheng*, *Liang Dunyan*, *Zhan Tianyou*, *Boxer Indemnity Scholarship*; Phillips Academy, *Chinese students at Andover: Liang Cheng*; FRUS 1908 (the indemnity remission).
- Reformers and revolutionaries abroad: Wikipedia, *Chinese Empire Reform Association* and *Revive China Society*; Hong Kong government photo archive (Xingzhonghui, Honolulu, 24 November 1894); University of Hawaiʻi ScholarSpace.
- The Revenue Council of 1906: FRUS 1906 (Rockhill's dispatches); Hansard, Lords, 28 May 1906; *The Spectator*, 19 May 1906.
- Late Qing reforms: Wikipedia, *1909 Chinese provincial elections*, *Advisory Council (Qing dynasty)*, *Cabinet of Prince Qing*; Chinese Culture (chiculture.org.hk) on the 1911 cabinet.
- 1911: Wikipedia, *Railway Protection Movement*, *Wuchang Uprising*; Toyo Bunko, Ichiko Chūzō on the Sichuan movement.
- Customs trusteeship: FRUS 1913 and 1915 (the bankers' commission of 30 January 1912); FRUS 1926; Wikipedia, *Francis Aglen*.
- 1912–16: Wikipedia, *Reorganisation loan affair*, *Second Revolution*, *China Consortium*, *National Protection War*; Cambridge, *Modern Asian Studies* on British policy and the loan; Wilson's statement of 18 March 1913 (Teaching American History); FRUS 1913; Papers Past (March 1913).
- 1916–23: Wikipedia, *Xu Shichang*, *Zhang Xun*, *China during World War I*, *Chinese Labour Corps*, *Zhili–Anhui War*, *First Zhili–Fengtian War*, *1924 Beijing Coup*, *Hunan Provincial Constitution*, *Chen Jiongming*; Cambridge on Chinese federalism; Guoqi Xu, *Strangers on the Western Front* (review, Project MUSE).
- Canton customs, 1923: FRUS 1923 (vol. 1, the naval demonstration at Canton); Papers Past (December 1923).
- Boycotts: Karl Gerth, "Consumption as resistance" (DIJ Tokyo), citing Remer, *A Study of Chinese Boycotts* (1933).
- 1923–28: Eugene Wu on Chiang's mission to Moscow (Project MUSE); Wikipedia, *1st National Congress of the Kuomintang*, *Whampoa Military Academy*, *Canton–Hong Kong strike*, *Shakee Massacre*, *Northern Expedition*, *1928 in China*; Britannica, *Mao Zedong*; Wikipedia, *Peasant Movement Training Institute*; Guangzhou education bureau on Mao's propaganda post; Hansard 1927 and the Hong Kong record on the Hankou and Jiujiang agreements; Chinese Culture on the flag change of 1928.
- 1928–32: FRUS 1929 (the disbandment conferences); Wikipedia, *Central Plains War*; FRUS 1929–31 and Hansard (extraterritoriality); Hansard 1930 and Papers Past (Weihaiwei); *American Political Science Review* (1931) on the convention and constitution; Wang Ke-wen on Hu Hanmin; Cambridge, *Modern Asian Studies*, on the Wang–Chiang cooperation; Wikipedia, *Wang Jingwei*.
- Women: Papers Past (1929 and 1932) on the inheritance principle and the Civil Code; Simonian (Toulouse) on the Civil Code; Taiwan Today on the 1924 platform; Ma, *Studies on Asia*, on the Central Women's Bureau.
- Zhongshan model county: Viana, *International Journal of Asian Studies* (2015); Zhongshan government history pages; China Daily (Zhuhai).
- Korea's rice: *Japanese Research in Business History* 39 (2022); Keio discussion paper 198.
- Not confirmed and not used as facts: the reasons for the mission's recall beyond "too Americanised"; Zhan Tianyou's part in the inter-Allied railway board of 1919; the share of women among the 1931 convention's delegates; the makers of Nanjing's transmitters.

## Canon tensions

None yet. Part A's proposals stay inside canon. The ones to watch are:
- Kaiping's refinancing in 1900–01 by Hoover (a Pacifican in canon; history's Kaiping engineer from 1899), which canon does not mention;
- Fushun's ownership;
- an end date for the Formosan administration after 1932 (no tension if it falls after 1932);
- whether canon's §14 and §16 inputs (PROPOSED) are approved with this CR;
- Part C's watch items, none a conflict with canon: Chiang's mission of 1923 to Pacifica (P-13); the works account for the Canton customs (P-12), which canon does not mention; the Concord's renunciation of extraterritoriality in 1930 (P-20), which canon neither states nor excludes; Tang Shaoyi as a new cast member (P-7); canon's "Pacifica funds Sun in Canton" read as indirect money (P-14).

## Fact changes

None at outline stage.

## Sources

- Rawski, *Economic Growth in Prewar China*: [University of California Press, via BHC](https://thebhc.org/bibliography/abstract/4505918/2NST6GSW).
- Feuerwerker, *China's Early Industrialization*: [De Gruyter](https://www.degruyterbrill.com/document/doi/10.4159/harvard.9780674333734/html).
- Pomeranz, *The Making of a Hinterland*: [UC Press](https://www.ucpress.edu/books/the-making-of-a-hinterland/hardcover).
- Feuerwerker, *The Chinese Economy, 1870–1949* (Cambridge History chapters): [University of Michigan Press](https://press.umich.edu/Books/T/The-Chinese-Economy-1870-1949).
- Coal output 1912–1931: [Evening Post, 1936, via Papers Past](https://dynamic-rsnz.natlib.govt.nz/newspapers/EP19360811.2.131.8); ownership shares: [Modern Asian Studies](https://core-cms.cambridgecore.org/core/journals/modern-asian-studies/article/entrepreneurs-politicians-and-the-chinese-coal-industry-18951937/396CB87F423497ACFB8A34DABB14C250).
- Railways: [Wikipedia, History of rail transport in China](https://en.wikipedia.org/wiki/History_of_rail_transport_in_China).
- Cotton spindles 1913 and 1936: [Nichibun repository](https://nichibun.repo.nii.ac.jp/record/3225/files/kosh_007__67__61_78__67_84.pdf).
- Electricity per person, 1936: [Chen and Sun, 1948](https://search.isc.ac/inventory/49/1492792.htm).
- Customs revenue and staff, 1890: [Vincent, via Litres](https://litres.com/book/ethel-gwendoline-vincent/newfoundland-to-cochin-china-34282504/read/page-17); telegraph 1882: [Hong Kong in texts](https://hkintexts.histsyn.com/page/1005569).
- Maddison's China estimates: [University of Bayreuth exhibition](https://eh-exhibition.uni-bayreuth.de/en/cs/China-2/index.html).
- Series with page citations from Feuerwerker (both books), Rawski and Pomeranz: `CR-081-A-series.md`.
- Electricity history: Tan, *Recharging China* ([OAPEN](https://library.oapen.org/bitstream/handle/20.500.12657/49455/9781501758966.pdf?sequence=1)).
