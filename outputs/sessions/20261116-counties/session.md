---
session: 20261116-counties
started: 2026-11-16
updated: 2026-11-16
mode: drafting
status: paused-for-author
baseline:
  commit: 28b7263
independence: self-review only (the consistency check of 16 November was done in the drafting session); no fresh-context review yet
---

# CR-071 (counties), CR-072 (the Prosperity Party), CR-073 (Ralston): drafting

## Brief

- **Author, 16 November 2026:** implement the consistency check's fixes; then "From now on let's only work in the repo please". The drafts were moved from the claude.ai project to this repo; the project copies are superseded and no longer updated.
- **Branch:** `drafts/cr071-073-counties`, from `main` at 28b7263. Nothing is integrated; `main` is untouched.

## What was done

- **Files** (all in `book-agent/revision/`): `CR-071-outline.md`, `CR-071-D-meiji.md`, `CR-071-E-preparation.md`, `CR-071-FG-triggers-act.md`, `CR-071-H-resistance.md`, `CR-071-consistency-check.md`, `CR-072-party.md` (draft 8), `CR-073-ralston.md` (draft 3, as approved on 15 November).
- **Consistency check** (`CR-071-consistency-check.md`, section E): every point fixed or decided; decisions K-1 to K-15 approved, with D-8, E-17, R-1 and R-2.
- **Checked against `main`:** the member list (nine members from 1867, eight legislatures; Arizona is New Mexico's Arizona county); the entrenched charters of 1866 (K-15: an article of supersession, F–G section T); the Act of Settlement in 1907, the regency 1887–1907 and the Senate dispute of 1910–1911 (CR-040). The earlier drafts had drawn these from stale project snapshots of CR-021, CR-022, CR-027 and the storyline of 28 October.
- **Part H** (draft 2): H-1 to H-12 approved, including the Honolulu rising of 30 July 1889 (H4) and the comparison with Meiji (H5).

## Checks at the end

`lint_canon.py --only` clean on every draft except one false positive in `CR-072-party.md` line 45 ("Taylor resists until he dies on 25 July 1887" read as Elias's death). Canon checks clean (no canon files changed).

## Part I, steps 1 and 2 (16 November, afternoon)

- **Author:** "Please merge main in ... Then go ahead and start with steps 1 and 2." `main` (7b2cb15, CR-057 with the Deseret sheet) merged into the branch; canon checks clean.
- **Step 1, the historical baseline:** `population/counties_1887.py` builds `population/outputs/counties_1887.csv` and `counties_1887.md` from `population/data/counties/` (the Newberry atlas's counties of 1 August 1887, CC0; county census totals from the counties' Wikipedia articles, checked against the state totals in `census.toml`). 233 mainland counties lie wholly or partly on Pacifica's side; about 2.29 million people in 1887 in our timeline, 1.10 million of them in California.
- **Step 2, the regional split (MODEL, not decided):** four variants in section 2 of `counties_1887.md`. The population model has no regions; California's share of the 5.84 million of 1887 runs from 77% (interior as in history) to 47% (every region in proportion).
- **Found on the way:** Baja California (purchase of 1867, PROPOSED in §16) is in neither the strawman nor the model; the line in Montana, Wyoming and Colorado needed county assignments (`overrides.toml`, `[pacifica_share]`, guesses for the split counties).
- **Not done:** county seats; maps (the atlas's geometry is available as topology in `localgeohistoryproject/county-boundaries-topology`, CC0, and can be rebuilt); 1880 sums for Colorado, Montana and Oregon do not close (444, 170, 100); three 1890 figures unverified.

## Resume here

- **Part I is drafted as `book-agent/revision/CR-071-I-map.md` (draft 1).** Decisions I-1 to I-9 carry the author's words of 16 November: 124 stays; Baja counts; Bozeman is Pacifican; the settlement programme is part of the hollowing; Asian settlers also in the interior; the drawing rules; Alaska stays under the Northern Commission outside the 124 (CT3); the homelands are compact lands, not counties, with a few Senate voices, and a member living in a county votes only where he is registered (CT5).
- **Approved (author, 16 November, 14:58):** the allocation (I-10); six homeland seats as grouped (I-11); Deseret's counties (I-12); Salt Lake City split from its valley (I-13). Draft 2 of Part I has Deseret at nine counties and New Mexico with the Diné country drawn.
- **Approved (author, 16 November, 15:05):** Park City and Coalville with Weber (I-14); a Pecos county from Deseret's spare, so New Mexico has ten (I-15); a thirty-fifth-parallel railway by 1887 (I-16); New Mexico's names (I-17). The pool has no spare county left.
- **Decided (author, 16 November, 15:17):** the transcontinental route stays Pacifica's; Gallup and the other European settlements stay in the counties (I-18).
- **Approved (author, 16 November, 15:19):** the mountains (I-19): Mount Taylor's and the Peaks' summits and northern slopes inside the Diné country, Hesperus and Blanca under a mountain article.
- **Approved (author, 16 November, 15:22):** the Hopi terms HP1 to HP7 (I-20).
- **California drawn (draft 1, PROPOSED):** 43 counties (12 merged away, 3 new: Carquinez, Santa Ana, Mojave). The map so far is machine-readable: `population/data/counties/map_1887.toml`, checked and tabulated by `population/map_1887.py` -> `outputs/map_1887.md` (62 of 124 drawn).
- **Approved (author, 16 November, 15:57, "I approve all thirteen"):** I-21 to I-33 in Part I: California's people moved off the historical shares, Mojave, California's names; renaming only where the map forces it; Snohomish into Skagit; the test for large homelands; the Snake railway; the multiples as working figures; Springer; Pecos English; the Jicarilla; a seventh homeland seat for Alaska's nations; Oregon and Columbia.
- **Idaho, western Montana, Washoe and the Rockies drawn (draft 1, PROPOSED):** twenty counties; 109 of 124 drawn; one county spare.
- **Approved (author, 16 November, 16:06):** the Slope's mining districts as county ground leased from the Utes (I-34); the spare county held until Arizona is drawn (I-35).
- **Approved (author, 16 November, 16:08):** Walker kept; Three Forks (I-36).
- **Arizona (eight) and Baja (two) drawn (draft 1, PROPOSED):** 118 of 124; Hawaii's five and Thalassia remain, no spare.
- **Approved (author, 16 November, 16:22):** I-37 to I-40 (San Pedro and the Chiricahua lease; Spanish for Pima and Baja; a Baja commission 1867-87 on the Alaska model; Arizona's large homelands).
- **Hawaii (five) and Thalassia drawn (draft 1, PROPOSED). All 124 are drawn** (`population/outputs/map_1887.md`; Part I draft 4, section I6).
- **Approved (author, 16 November, 16:31):** I-41 to I-45 (Hawaii's five; Thalassia's lines; Kalaupapa; the Hawaiian examination; Idaho's, Washoe's and the Rockies' counties). Every county of the 124 is now approved.
- **Map drawn** on the author's request: `population/outputs/map_1887.png` (`population/draw_map_1887.py`; needs the atlas's topology, cloned outside the repo, plus shapely and pyshp).
- **Owed:** sources for Salt Lake City's share of its valley and for the Diné population of 1887.
- **Author, 16 November, 17:18:** the awkwardly shaped counties are acceptable; asked for a suggestion of the homelands' borders and why California's homelands were not on the map (they were enclaves by I-8 and had been left off the drawing; now marked).
- **Author, 16 November, 17:35:** supplied Royce's *Indian Land Cessions* (PDF, not copied into the repo) and asked for definitive borders with no county divided by a homeland, and whether Spokane should be split.
- **Homelands redrawn (draft 2, PROPOSED):** `population/data/counties/homelands_1887.toml` (lines from Royce's boundary texts where read; Nez Perce 1855 and Uinta 1861 still from memory), Part I section I4a, `population/outputs/homelands_1887.md` (areas and the county adjustments), and the map. `draw_map_1887.py` now cuts counties to the homelands and reassigns detached pieces. Spokane is not divided (the Okanogan country goes to Big Bend); the Globe district goes to Salt River; Tombstone lies outside the Chiricahua line.
- **Author, 16 November, 18:26:** asked for a legibility pass on the map before any further adjustment (labels with a white outline, above the lines, never overlapping, as on Google Maps). Done in `population/draw_map_1887.py`: every name has a white halo and is placed by a collision check; names that fit nowhere get a number and a key (one so far); tiny counties in the insets get a leader line; a Puget Sound inset was added.
- **Approved (author, 16 November, 19:16):** I-46 to I-49 (the homeland rule; the Nez Perce line of 1855 with Lewiston on lease; the Uinta valley large; Yakama, Klamath and Fort Hall stay large).
- **California's tracts drawn (PROPOSED):** eighteen treaties, nineteen tracts, Royce's numbers 273-309, traced by eye from his plate CXIV (`homelands_1887.toml`, `[[tract]]`; `outputs/homelands_1887.md`; Part I section I4a; the map). About 10,400 sq mi as drawn.
- **Approved (author, 16 November, 20:43):** the nineteen tracts as a working version (I-50); the Cosumnes tract is section 8's Miwok homeland, one of the first or signed seven months early (I-51).
- **Approved (author, 16 November, 20:50):** the Apache country on the line of 1871, Globe and Clifton inside on lease, the Gila's valley floor in Gila county; for canon, the border "is given to Apache country from 1865 and the settlers don't have to be driven out or anything" (I-52; note in Part I section I4a, to be carried into section 15 at integration). He also asked why the Diné and Hopi labels both stood in a square and why the homelands had three colours: the square was Royce's 1882 box of degrees used as a placeholder, against HP2. Now the Hopi country is sketched by named places with Moenkopi detached, the Diné name stands outside it, and all homelands have one colour (Part I draft 9; map draft 9). The Hopi line stays OPEN.
- **Waiting for the author:** the Apache line. The assistant's suggestion: the White Mountain order's line of 1871 (the mountains from the Rim to the crest north of the Gila, to New Mexico's line), Globe and Clifton on lease inside it, the Gila's valley floor left to Gila county.
- **Next for the homelands:** check the Nez Perce and Uinta texts on the scan's page images; outline the other enclaves; move the counties' people to match.
- **Next:** G3's table replaced by I6's; the outline's Part I, CT3 and CT5 updated; the settlement programme written into Part C and costed; the Baja commission (I-39) and the three assumed railways given dates; then a fresh-context review of Part I. Maps can be drawn from the atlas's topology (`localgeohistoryproject/county-boundaries-topology`, CC0). Then G3 recounted, the outline's I and CT3/CT5 updated, and the programme written into Part C and costed.
- **Corrected in this session:** Thalassia is on Kāneʻohe Bay, not in California; the allocation tables now count it apart.
- Then Parts A, B, C and J; storyline text, fact changes, ledger (Japan's loan of 1873; the seven charter entries, F–G section T5), registry lines, model rows; a fresh-context review; integration in the K-1 order. CR-057 is now on `main` (PR #73), so CR-073 and CR-072 integrate on `main` as it stands.
- Still open in CR-071: D decision 9 ("ready for approval"), the Guard's commander and Wilcox's later life (H4), CT4's Columbia and Washoe rows in the outline.
- On `main`, for a later CR or review branch: the leftover "until 1914" in §25's languages paragraph (should follow CR-040's 1907); AGENTS.md's "A Crown-affiliated party is on hold" (CR-038), which CR-072 supersedes at integration.
