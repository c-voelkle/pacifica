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

The numbers sit in a small standalone script (proposal: `population/china.py`, beside `neighbours.py`). It holds historical baselines and a few levers, so that Parts B and C can read population, output and literacy from one place. It feeds nothing in the financial workbook unless the author asks.

### A1. What canon already sends into China

| Input | When | Canon |
|---|---|---|
| Engineering and credit for steamships and the Kaiping mines | 1870s | §14 |
| The Educational Mission in San Francisco, with naval-academy places | from 1872 | PROPOSED |
| Yung Wing's machinery orders to Carquinez | 1870s | PROPOSED |
| California wheat for the North China famine | 1876–79 | §14 |
| Credit for China's railways and fleet rebuilding on the Kaiping concession | 1880s | §16 |
| The Customs Inspectorate under Pacifican leadership (Fong) | 1885–1929 | §16, §33 |
| The Formosan administration: camphor, the Keelung mines, the customs, the harbour | from 1895 | §25 |
| Credit for a Chinese-owned Manchurian railway and the Hankow–Canton trunk | 1896 | PROPOSED |
| The Boxer indemnity turned into scholarships | 1900s | PROPOSED |
| The Polytechnic of Formosa | 1906 | §26 |
| Huludao: the harbour trust (from 1910), the Mukden line (1908–10), the industrial district (1923) | 1908–23 | CR-042, CR-057 |
| Harbin–Mukden Chinese line | by 1912 | CR-042 |
| Russia renounces its concessions and its share of the Boxer indemnity; the Manchurian railway returns to Chinese management | 1921 | §32 |
| China recovers the Inspectorate, the customs and its tariff | 1928–29 | §33 |
| Fertilizer from Tacoma for South China's rice | from 1929 | §34 |

**What canon does not say:**
- how much of any of this there is;
- what China owns, mines or makes;
- what the Chinese do with the licences.

### A2. Resources

| Resource | History | Pacifican divergence to decide |
|---|---|---|
| **Coal** | output of 8,987,862 tons in 1912, over 23,000,000 tons in 1926 and more than 27,000,000 tons in 1931; in the 1920s and 1930s Chinese-owned mines produced around 20–30% of modern output and Sino-foreign mines perhaps another 30%, and Fushun, run by the Japanese South Manchuria Railway, nearly all the rest | Kaiping on Pacifican credit from the 1870s (canon); Kaiping does not pass to the Anglo-Belgian company in 1900. Fushun stays Chinese, since Manchuria's railway is Chinese-owned. *Proposal:* the Chinese-owned share above half by the 1920s, and output about 1.3–1.5 times history's by 1931 (MODEL) |
| **Iron** | Hanyang (1890–94) and Hanyeping (1908) under Sheng Xuanhuai, indebted to Japan's Yawata works for ore loans | Pacifican credit beside Japan's. *Question:* who finances Hanyeping, and does Daye's ore still go to Japan? |
| **Tungsten and antimony** | China became the world's largest producer of both: tungsten in Jiangxi from the 1910s, antimony in Hunan (dates to verify) | **The strongest material divergence.** Tungsten is the metal of the Realm's lamp filaments, valves and tool steel, and from 1912 its valve works make valves by the hundred thousand (CR-077). *Proposal:* Pacifican demand finds and buys Jiangxi's tungsten about 1905–10 and Hunan's antimony early. This makes two inland provinces rich, contested and wired. Hunan is Mao's province (Part C) |
| **Tin** | Gejiu, Yunnan | Pacifican cans and solder; a smaller case |
| **Oil** | none found before 1939 (Yumen) | none; China buys the trust's lamp oil (canon: the trust's Asian lamp-oil trade) |
| **Camphor** | Formosa's monopoly | under the Pacifican administration from 1895 (canon); film stock (CR-079) and celluloid |
| **Hydropower** | barely used | the AC standard spreads with Pacifican equipment through East Asia (canon). *Question:* any large Chinese hydro before 1932? |

### A3. Infrastructure

| Item | History | Pacifican divergence to decide |
|---|---|---|
| **Railways** | a 10 km line from Tangshan built in 1881, extended to Tianjin in 1888 and Shanhaiguan in 1894; Formosa's 107 km Keelung–Taipei–Hsinchu line of 1887–93; about 9,000 km by 1911; the Nationalists built about 3,600 km in 1928–37 | **Canon's lines:** a Chinese-owned Manchurian railway (instead of the Russian line and the Japanese South Manchuria line), the Hankow–Canton trunk on early credit (history finished it only in 1936), Harbin–Mukden, and Huludao. Formosa's line survives, since the island stays Chinese. *Proposal:* about 11,000–12,000 km by 1911 and 18,000–20,000 km by 1928 (MODEL) |
| **Telegraph** | a Tianjin–Shanghai line opened in December 1882, and lines soon connected all the important cities; the Telegraph Administration under Sheng from 1881–82; Great Northern's coastal cable from 1871 | the mission's telegraphers; the Manila–Keelung–Amoy–Foochow–Shanghai cable (CR-080 C1); fax on the newspapers' wire after 1908–10 (CR-078) |
| **Shipping** | the China Merchants' company (1872) | steamers on Pacifican engineering (canon) |
| **Ports** | Shanghai, Tianjin, Canton and the treaty ports | Huludao (canon), Keelung under its harbour trust (canon); the Customs' lights (*Hist.*: the Marine Department from 1868) |
| **The post** | the Customs' post office from 1896 | the same under Fong |

### A4. Industry

| Item | History | Pacifican divergence to decide |
|---|---|---|
| **Cotton** | the first Chinese mill went into production at the end of 1889; Japanese-owned mills in China had 111,936 spindles in 1913 and 2,485,352 in 1936, while Chinese-owned mills went from 484,192 to 2,919,708 | Japanese mills in China (the annex makes textiles Japan's in the Concord, but China is not a party); Toyoda's looms licensed; electric drive. *Question:* does China's tariff from 1928 (canon) protect its own mills? |
| **Electric power** | Shanghai's first light in 1882; in 1936 China consumed only about 4 kWh per person | Pacifican equipment and credit; Huludao's district. *Proposal:* about 3–5 times history's consumption per person by 1932, concentrated in the treaty ports, Manchuria and the tungsten districts (MODEL) |
| **Machines and electrical goods** | Shanghai's small machine shops | the Commercial Press as maker of character machines (CR-080 D2); Chinese makers beside Japan's for radios and lamps |
| **Chemicals** | Fan Xudong's salt and soda works at Tianjin (1914–17) | — |

### A5. Money and people

| Item | History | Pacifican divergence to decide |
|---|---|---|
| **Customs revenue** | about 14.7 million Haikwan taels in 1885 (*Hist.*, to verify against the Customs returns); about 22 million taels in 1890, from a service of 700 Europeans and 4,000 Chinese; about 36 million in 1911 | Under Fong the revenue is about the same, because the treaty tariff is fixed. What changes is that it is published, Chinese staff rise, and Pacifican credit is secured on it. *Question:* does more of it reach Chinese development and less foreign indemnities, since there is no Shimonoseki indemnity on history's scale? |
| **Indemnities** | Shimonoseki (1895) and the Boxer indemnity (1901) consumed much of the revenue | a moderate indemnity in 1895 (canon); the Boxer indemnity partly turned into scholarships early, and Russia's renounced in 1921 (canon) |
| **Remittances** | Taishan and the Pearl River delta lived on remittances from America | Pacifica has no exclusion act and a charter floor for Chinese residents (canon). *Question:* how large is the Chinese-Pacifican population by 1900 and 1930 (population model)? |
| **Schooling** | the mission recalled in 1881; the examinations abolished in 1905 | the mission continues; the Polytechnic of Formosa (1906); the scholarships. *Proposal:* a Pacifican-trained technical class of a few thousand by 1911 and tens of thousands by 1930 (MODEL) |
| **Population and output** | Maddison found that GDP per capita declined dramatically from 1850 to 1870, then increased slightly from 1870 to 1913; the 1933 benchmark is considered reliable | *Proposal:* the same population path (the famines aside), and output per person about 10–20% above history's by 1932 (MODEL), concentrated in the modern sector, the coast, Manchuria and the mining provinces |

### A6. Information

The Chinese telegraph code (1871), characters on the Customs' cards (CR-080 C3), the Chinese typewriter and fax are the subject of CR-080 Part C. Here they are counted as material: how many terminals, cards and receivers there are by 1932 (MODEL).

### A7. Decisions for Part A (to be put to the author when the draft is complete)

1. The method and the script (A0).
2. Coal: Kaiping kept Chinese, Fushun Chinese, the Chinese-owned share and the output multiple.
3. Tungsten and antimony found and bought early.
4. The railway kilometres in 1911 and 1928.
5. Electric power per person by 1932.
6. Hanyeping's financing.
7. The technical class and the Chinese-Pacifican population.
8. Output per person, about 10–20% above history's by 1932.

## B. The socioeconomic layer (sketch)

- **Famines:** North China in 1876–79 (with canon's relief), 1920–21 and 1928–30. Do railways and relief lower the deaths?
- **Cities:** Shanghai, Tianjin, Canton, Harbin, Huludao; the tungsten towns of Jiangxi and Hunan.
- **The hinterland:** Pomeranz's question; which regions the railways and the Customs pass by.
- **Literacy:** baselines, the mission's and the scholarships' graduates, and the Mass Education Movement.
- **New classes:**
  - engineers;
  - Chinese Pacificans and returnees;
  - compradors and their successors;
  - mine and mill workers;
  - the Customs' Chinese staff.
- **The warlords' fiscal base:** railways, salt and the provinces' mines.
- **Opium:** history's suppression campaign of 1906–17, and Pacifica's rule (CR-076).

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
- Kaiping passing to the Anglo-Belgian company in 1900, which canon does not mention;
- Fushun's ownership;
- whether Hoover, a Pacifican in canon, was ever Kaiping's engineer as he was in history.

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
- Electricity history: Tan, *Recharging China* ([OAPEN](https://library.oapen.org/bitstream/handle/20.500.12657/49455/9781501758966.pdf?sequence=1)).
