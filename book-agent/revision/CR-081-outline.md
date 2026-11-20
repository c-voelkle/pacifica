# CR-081 (outline) — China's other century: materials, society and politics (1860–1932)

**Status:** OUTLINE, 20 November 2026. Part A (the material layer) is in first draft below; Parts B and C are sketched. Nothing is decided beyond what is marked *canon*.

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

## C. The political timeline (sketch)

Built on A and B. It starts from CR-080 D0's table (1860–1928) and the decided X-8:
- Self-Strengthening with a partner;
- the late Qing reforms;
- 1911;
- Yuan Shikai;
- the warlords;
- no May Fourth outrage;
- the Nationalists' model;
- land;
- Mao.

## Canon tensions

None yet. Part A's proposals stay inside canon. The ones to watch are:
- Kaiping's refinancing in 1900–01 by Hoover (a Pacifican in canon; history's Kaiping engineer from 1899), which canon does not mention;
- Fushun's ownership;
- an end date for the Formosan administration after 1932 (no tension if it falls after 1932);
- whether canon's §14 and §16 inputs (PROPOSED) are approved with this CR.

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
