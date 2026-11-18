# CR-075 research plan: scanning the seven texts

Author supplied, 18 November 2026, 14:15. The texts stay outside the repository (`/home/claude/research/`); the repository gets only notes with page references, paraphrase and quotes under fifteen words.

## The texts

| Key | Book | Form | Size | Strongest for |
|---|---|---|---|---|
| ELL | Ellison, *California and the Nation, 1850–1869* (1927) | PDF, 284 pp., OCR fair | 95k words | California's grievances against Washington; the Pacific Republic movement of 1860–61; the war's finance on the coast (legal tender, the Specific Contract Act) |
| RICH | Richards, *The California Gold Rush and the Coming of the Civil War* (2007) | EPUB | 103k words | Gwin and the Chivalry, Broderick, Terry; the Southern plan for California |
| WAITE | Waite, *West of Slavery* (2021) | PDF, 393 pp. | 163k words | The South's Pacific ambitions; secessionists in southern California; Confederate Arizona; the Pacific Republic seen from the South |
| SHER | *The Sherman Letters* (ed. Thorndike, 1894) | PDF, 440 pp. | 125k words | What W. T. Sherman knew and thought, 1853–1865: San Francisco banking and the Vigilance Committee of 1856, Louisiana 1859–61, his forecast of a long war; what John told him of Congress |
| HUNT | Hunt, *The Army of the Pacific* (1951) | PDF, 470 pp. | 128k words | The Union's forces on the coast in 1861: Sumner, Wright, Casey, the posts, the volunteers, the navy's ships; Fort Churchill, Camp Floyd, Utah |
| ROS | Rosenus, *General Vallejo and the Advent of the Americans* (1995) | PDF, 316 pp. | 108k words | Vallejo's character, his view of Americans, 1846–1850s; thin on 1861 (ten hits) |
| JONES | Jones, *Blue and Gray Diplomacy* (2010) | EPUB | 175k words | Seward's foreign-war memorandum, belligerency, neutrality, blockade and search, the *Trent*, mediation |

## Passes

### Pass 0 — Preparation (done, 14:20)
Text extracted with page breaks kept (PDFs) and chapter breaks (EPUBs), so every note can carry a page or chapter reference.

### Pass 1 — Keyword sweep (all seven, mechanical)
One query list per outline item, run across all texts, giving a hit table with pages. It shows where to read and where the books are silent. Queries by item:
- **C1, D2, G** (the coast's garrisons and squadron): Vancouver, Steilacoom, Port Townsend, San Juan, Alcatraz, Benicia, Mare Island, Sumner, Wright, Casey, *Lancaster*, *Saranac*, squadron, Panama.
- **C2, E2** (the treaty of 1848 as a leash; belligerency): belligerent, insurgent, pirates, privateer, neutral, proclamation, blockade, search, deserters, Prize Cases, Seward circular.
- **C3, CT2** (search at sea): visit and search, *Trent*, Wilkes, neutral rights, Declaration of Paris.
- **E1, E4** (the lock; the Americans in California): Pacific Republic, secession, Chivalry, Gwin, Weller, Burch, Scott, Lane, Union men, Douglas Democrats, Knights of the Golden Circle, Los Angeles, Visalia.
- **E3** (San Francisco's money): treasure, specie, steamer, legal tender, greenbacks, Specific Contract Act, Comstock, Washoe, New York.
- **E5, E7** (opposition, renewals, cost): legislature 1861, 1862, taxes, militia, volunteers, enlistment.
- **E6** (a price for California): federal neglect, mail, overland, Pacific railroad, Indian war debts, land titles.
- **D-b** (the players): every player's name, with spelling variants.
- **D1, D5** (the sequence; the Union's calendar): long war, Scott, Anaconda, election, Peace Democrats, Copperheads.
- **D3** (the interior follows its supplies): Sacramento trade, freighting, Salt Lake, Mormons, Idaho, Clearwater, Oro Fino, mines, supply.
- **D4** (the coin): as E3, plus gold premium, suspension.

### Pass 2 — Close reading of the core chapters
Read whole chapters, not only the hits, wherever Pass 1 shows a run of hits, because the argument of a chapter is what supplies motive and the hits only supply facts. Provisional list, to be fixed after Pass 1:
- ELL: the chapters on secession, the Pacific Republic and California in the war; the chapters on mail, roads and the railroad (California's grievances).
- RICH: the chapters from Broderick's rise to his death and the epilogue on 1860–61.
- WAITE: the chapters on the secession winter and the war in the Far West.
- SHER: every letter from 1853 to the end of 1861; then 1862–65 for his forecasts and judgments of the generals.
- HUNT: the opening chapters (the department in 1860–61, Sumner's command, the withdrawals) and the chapters on Oregon and Washington, Nevada and Utah.
- ROS: the 1846 chapters (Vallejo's view of the Americans), the 1850s and whatever there is of 1861.
- JONES: the chapters on the spring of 1861 (Seward, recognition, neutrality, blockade), the *Trent*, and the mediation of 1862.

Notes go into one file per outline item, each note in the same form: item; claim (paraphrased); source and page; a quote under fifteen words if the wording matters; what it means for Pacifica (fits canon, a divergence to note, or a correction).

### Pass 3 — Checking canon
The books can confirm or correct facts already in canon and marked "Hist.; to verify" in CR-059 to CR-069 and CR-068's sources list (for example Sherman's path before 1853, Halleck's California career, the Pacific squadron's ships and the Clearwater discoveries). Output: a list of confirmations and corrections, each with its page, and a fact change wherever a correction touches canon.

### Pass 4 — The players
One page per player in D-b: what the record shows they knew in 1861, their own interests, a sample of their voice (short quotes), and what that suggests for their part in the closed sitting. Sherman, Vallejo, Broderick, Gwin (absent in canon so far) and the Union's coast commanders are well covered; Huntington, Ralston, Judah, Beale, Hunt, Wyllie and Victoria are covered thinly or not at all (see Gaps).

### Pass 5 — Back into the outline
Revise Parts C, D, E and CT2 with what the passes found. Every historical claim the outline relies on gets a page reference. The research and the reasons for each divergence go into a draft section for `historical_background.md`, as AGENTS.md requires.

### Pass 6 — Checking the citations
Every page reference is checked mechanically against the extracted text (the cited words must be on the cited page), and every quote counted under fifteen words. A fresh-context review of the revised parts follows later, as usual.

## Gaps these seven books will not fill

- **Hawaii in 1861** (Part F; Victoria, Wyllie, Honolulu as a news harbour): Kuykendall, *The Hawaiian Kingdom*, vol. 2.
- **Huntington, Ralston, Beale, Broderick in detail** (D-b): Lavender, *The Great Persuader*; Lavender, *Nothing Seemed Impossible* (already supplied for CR-073); Thompson, *Edward F. Beale and the American West*; Williams, *David C. Broderick*; Quinn, *The Rivals*.
- **The Pacific squadron's ships and stations** (C1): the Official Records of the Union and Confederate Navies, series I, vol. 1; Hunt may be enough.
- **Vallejo in 1861** (E2, P8): Rosenus is thin here; his *Recuerdos* and correspondence are in the Bancroft Library.

What none of these cover stays a story assumption, labelled as such.
