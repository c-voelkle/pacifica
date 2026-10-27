# CR-033 (draft) — Settlement, Native recovery and the shape of Pacifica's population

**Status:** PROPOSED draft, 27 October 2026, revised after one fresh-context review. Not adopted: no storyline, register, character or workbook file is changed by this draft. CR-033 is the next free number (CR-032 is used by the separate alternative timelines).
**Basis:** author decisions of 27 October 2026, made while reviewing the population model (`population/README.md`; outputs in `population/outputs/`).

## Author decisions

> Let's divide up that stream. I think most of it would be coming from the Americas and Europe then Japan, then China (Japan would canonically have much higher rates of emigration to Pacifica in this timeline, China also, but not as high as Japan), with Filipino immigration mostly after 1914.

> 1: disease without mass killing. 2: yes, [the sheet's 1846 Californians] include native population. 3: if it can be realistically explained through believable counterfactuals in the alternate timeline, including such as have not yet been made explicit in the canon, I like the 1.2m figure better for 1861. 4: I think a predominance of Japanese immigration also in absolute terms makes more sense for the picture shown in the storyline. It is explained not just by redirected historical emigration flows but also by emigration flows increased by changed circumstances in the alternate timeline.

> I approve the candidate explanations in the population README. I think the 1865 figure should rise. I think the population should continue to rise generously after 1915 too — that's when Pacifica becomes a really attractive place to live. I think the native population should also be modeled as growing after the initial dip. This is explained by fair treatment and generally superior quality of life compared to the historical timeline.

The README explanations the author approved:
- The light foreign-miner licences keep Sonoran, Chilean, Peruvian and Chinese miners.
- Assisted passage for women and families turns sojourners into settlers.
- Secure land titles and a stable republic.
- A Pacific-facing republic draws arrivals from Australia and Chile directly.
- Americans keep moving west to an independent but open California.

## Decisions

| ID | Decision | Label |
|---|---|---|
| A1 | The gold rush settles rather than passes through, by the five approved explanations above. | APPROVED direction |
| A2 | The Confederation counts about 1.2 million people in 1861 and about 1.7 million in 1865 (DEM-01, revised). | MODEL |
| A3 | How land titles become secure. | OPEN (unresolved items 6 and 7; no new item) |
| A4 | No campaign of extermination against Native Californians. Introduced disease reduces them to about two-thirds of their 1848 number by the mid-1880s. Fair treatment and a better quality of life then bring steady growth: about 180,000 by 1932. | APPROVED direction; figures MODEL |
| A5 | The legal form of Native Californian homelands and claims, and the Republic's obligations to Indigenous polities. | OPEN (unresolved items 4, 6, 7; unchanged) |
| A6 | Japanese immigration predominates over Chinese in absolute terms from the 1900s. It comes from redirected flows and from emigration increased by the alternate timeline's circumstances. Filipino migration is mostly after 1914. | APPROVED direction |
| A7 | Tying A6 to the 1907 compact's family immigration (§26, APPROVED — CR-022), and to Japan's lack of a settler outlet in Korea and Manchuria. | PROPOSED |
| A8 | By 1932, Japanese-origin Pacificans number about 3.9 million and Chinese-origin about 3.6 million. | MODEL |
| A9 | After 1915 the population keeps rising generously, and core Pacifica counts about 30 million people by 1932. | APPROVED direction; figure MODEL |
| A10 | The model's health and fertility paths: life expectancy converging to the world's best (New Zealand) by about 1910, and fertility to Canada's. | MODEL (population/data/rates.toml) |
| A11 | Native Hawaiians: no change. Canon already has the decline into the 1880s and the turn about 1895 (§20, §23); the model reproduces it, with a low of about 42,000 in 1895 and about 67,000 by 1932. | Existing canon; figures MODEL |

## Proposed storyline text

Each insertion is a new paragraph, shown with the existing passage it follows or precedes, quoted exactly. Comparisons with our timeline stay in these notes and in `historical_background.md`, not in the story.

### End of §8, before the heading "# PART II — The struggle for North America (1861–1867)" (A1–A3)

> **[PROPOSED — CR-033]** The gold rush has settled rather than passed through. The light licences keep the Sonoran, Chilean, Peruvian and Chinese miners whom the American miners wanted taxed out. Assisted passage brings women and families. As titles are confirmed, by means still **[OPEN]**, more miners buy land and stay. Pacific shipping brings Australians and Chileans as well as Americans moving west. By 1861 the Confederation counts about 1.2 million people **[MODEL]**. Measles, smallpox and malaria meanwhile sweep the Native villages of California.

### §25, after the paragraph ending "…giving county oligarchies reason to fight through their senators." (A4–A5)

> **[PROPOSED — CR-033]** Native Californians, reduced by disease to perhaps two-thirds of their number at the gold discoveries, begin to recover in the 1880s. With fair treatment and better living conditions their villages grow again, and by 1932 they number about 180,000 **[MODEL]**. What homelands and claims the Republic recognises remains **[OPEN]**.

### §26, after the paragraph ending "…family immigration and civic equality for Japanese Pacificans." (A6–A8)

> **[PROPOSED — CR-033]** With families now admitted, Korea independent, Manchuria Chinese and Japan's eastern holdings drawing few settlers, Japanese emigrants increasingly choose Pacifica. Within a decade Japanese arrivals overtake Chinese, and by 1932 Japanese-origin Pacificans outnumber Chinese-origin ones, about 3.9 against 3.6 million **[MODEL]**. Filipino migration stays small until the Philippine crown joins Julian's, and grows after it.

### §33, before the paragraph beginning "Shared infrastructure, technical education and investment also lift the partners." (A9–A10)

> **[PROPOSED — CR-033]** Pacifica itself keeps growing fast. Its public health ranks with the best in the world, families stay large and immigrants keep coming. By 1932 core Pacifica, Hawaii included and the Philippine crown and the Gulf not, counts about 30 million people **[MODEL]**, though critics note that selective entry flatters the bureau's figures.

## Fact changes

```json
[
  {"add_forbidden": {"pattern": "(?<!\\bto )(?:wages|declares|orders|launches|waged|declared|ordered|launched) (?:a |its )?(?:war|campaign) of extermination",
                     "message": "No campaign of extermination against Native Californians (CR-033)"}}
]
```

The rule catches an actor declaring, ordering, launching or waging such a campaign. It lets through refusals ("wages no …", "refuses to wage …") and demands short of a campaign, such as squatters' papers calling for one, which can stay in the story as conflict. Tested on both kinds of sentence. No person's dates change. The population figures are MODEL estimates and do not go into `canon_facts.toml`.

## Impact notes

- **Storyline:** four new paragraphs (end of §8, §25, §26, §33), each with a hidden CR-033 coverage comment. No existing sentence changes, and each insertion sits in the section whose dates it covers. The §5 licence compromise, the 1888 selective-entry law (§25) and the Hapa passages (§15, §26) are unchanged and consistent.
- **Dependency:** the §5 promise of a Miwok homeland (PROPOSED — CR-028) is compatible with A4 but not required by it.
- **Historical background:** on adoption, add the divergences to `historical_background.md`, with our-timeline anchors and sources:
  - our timeline's punitive 1850 Foreign Miners' Tax and the departure of Latin American miners;
  - the Native Californian decline (Madley 2016);
  - Japanese emigration and colonial settlement (MOFA 1985; Discover Nikkei);
  - the New Zealand and Canadian benchmarks.
- **Assumptions:** DEM-01 in `war_base_assumptions.md` already reads about 1.2m (1861) and 1.7m (1865).
- **Character documents:** none affected.
- **Financial workbook:** unchanged. It differs from the model on Native Hawaiians and Native Californians (the sheet grows both with everyone), on the origin of its talent stream, and on growth after 1915. These belong in the workbook change list, not this CR.
- **Review:** one fresh-context review (consistency and literary effect) was run on the first draft. This revision acts on its findings:
  - the Japanese paragraph is tied to the 1907 compact and moved to §26;
  - Japan's eastern holdings are acknowledged;
  - the Filipino timing is aligned with the crown's union;
  - the comparisons with our timeline are removed from the prose;
  - the paragraphs are placed in their sections' time spans;
  - the 1852 date (workbook-only) is dropped from the prose;
  - the land-titles question points to the existing OPEN items;
  - the forbidden rule is narrowed;
  - the 1932 perimeter is stated, and a counterweight added.

## Open choices for the author

- How land titles become secure (unresolved items 6 and 7).
- Whether the Native Californian turn in the 1880s should hang on a named event, such as a public-health law or a homelands settlement. Canon gives none, and the model's dates are MODEL.
- Whether the population figures (1861, 1932, Japanese and Chinese) belong in the storyline or only in these notes.
- The model's 1895 total, about 6.8m, sits just above the CR-015 range of 4–6.5m. Raise the range, or accept the overshoot as a consequence of A1–A2.
