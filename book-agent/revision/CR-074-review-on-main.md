# CR-074 — Fresh-context review of the integration on `integrate/cr074` (18 November 2026)

**Base:** `main` at 2ad4016; reviewed `integrate/cr074` at fa8a49b (e040d84 integration, 22892d1 model rows). **Independence:** fresh context; read AGENTS.md, `CR-074.md` (draft 7) and the diffs and surrounding canon only. `CR-074-review.md` and the session record were not read. Nothing in the repo was modified.

**Verdict:** Not ready to merge as is; close to ready. The integration is faithful to Part N almost word for word, every ledger quote is verbatim with the correct label, and all five mechanical checks pass. Four blockers, all small text fixes. One adds a chronology error in §6. One puts approved text under a `[MODEL]` label in §19. One narrates T9's PROPOSED naturalization rule as APPROVED. One mentions the Calamba evictions of 1890–91 in an 1888 passage. Twelve should-fix items follow: mostly knock-on effects across files (the family farm's size, CR-037 E7, the Miwok guide, the Philippine Council), a misleading 1894 sentence, label choices that need the author's confirmation, and the model's warrant timing. **4 blockers, 12 should-fix, 15 nits.**

## M. Mechanical checks

All were run on `integrate/cr074` at fa8a49b, and none changed the working tree (`git status` clean afterwards).

| Check | Result |
|---|---|
| `python3 commitments/ledger.py check` | 300 commitments checked, 0 problems (exit 0) |
| `python3 book-agent/revision/lint_canon.py` | Canon lint clean: 4 files checked (exit 0) |
| `python3 book-agent/revision/cr_facts.py check` | Register and facts file agree, 204 approved fact changes (exit 0) |
| `python3 book-agent/revision/sync_master_storyline.py --check` | Index synchronized; approved CR IDs referenced (exit 0) |
| `python3 book-agent/revision/validate_character_docs.py` | Valid: all canonical IDs, links and 250 legacy profiles agree (exit 0) |

These scripts live in `book-agent/revision/` and `commitments/`, not in `tools/`.

**Own check of the ten CR-074 ledger entries.** I located every `quote` and `more_quotes` entry in the storyline and took the last label before it in the same paragraph:
- Each quote occurs exactly once.
- Each label matches `status`: APPROVED — CR-071 for C-1854's main quote, APPROVED — CR-074 for all the others.
- The C-1878-LETTERS quote ends just before `[MODEL]`, so it passes; see B2 for the consequence.

**Workbook.** E247–E250 in `finance/Pacifica_financial_model_1846-1932.xlsx` match the build script and the note:
- E247: 10,000 × $1.39 = $0.0139m
- E248: 500 × $360 = $0.18m
- E249: −350 × 55 × $3.50 = −$0.067m
- E250: 2,500 × $360 × ½ × 2.5 × 1% = $0.011m

The workbook's SHA-256 equals the one in the note.

## Blockers

1. **§6, l. 248–250: the Crabb insertion moves the Hawaiian annexation crisis to 1857.** L. 248 now ends with "…and the Mexicans shoot him at Caborca" (April 1857). The next paragraph, l. 250, still opens "At the same time the Hawaiian government hears rumors of further American adventurers…" and ends "Kamehameha III dies in December 1854". "At the same time" now points at 1857, which contradicts the paragraph's own date. **Fix** (l. 250): "At the same time" → "In 1854, while Walker's men are tried, the Hawaiian government hears rumors…". The alternative is to move the Crabb sentence after the 1856 material. The base-text edit is the smaller change.

2. **§19, l. 819: `[MODEL]` takes over approved canon.** The text reads "In the spring and summer of 1878 about a dozen armed sealers and whalers **[MODEL]** sail under letters of marque and bring a handful of Russian supply ships to the prize courts …; Russia answers with its Volunteer Fleet. At Keelung in the spring of 1885 … a company lands to guard the coal company's miners. **[APPROVED — CR-071]**…". A label applies until the next label in the paragraph. The letters' sailing, the prize courts, the Volunteer Fleet and the Keelung landing (D-5, D-6, APPROVED) are therefore all labelled MODEL. Only the number of ships is MODEL (C4). **Fix:** "In the spring and summer of 1878 armed sealers and whalers sail under letters of marque and bring a handful of Russian supply ships to the prize courts at San Francisco and Honolulu, and a few men make fortunes; Russia answers with its Volunteer Fleet. At Keelung in the spring of 1885, after Ferry's fall, a company lands to guard the coal company's miners. **[MODEL]** About a dozen ships hold letters in 1878. **[APPROVED — CR-071]** Some thousands have served…". Then change the C-1878-LETTERS quote (ledger l. 6236 ff.) to "In the spring and summer of 1878 armed sealers and whalers sail under letters of marque".

3. **§19, l. 819: T9's PROPOSED rule is narrated as APPROVED.** The text reads "On his way to China in 1859 he swears allegiance to the Republic at San Francisco, so that no American consul can touch his trade, and the company serves under the Pacifican consul's licence…", all under **[APPROVED — CR-074]**. CR-074 is explicit on this point:
   - C2: "That an oath is enough is PROPOSED here: canon leaves the exact naturalization rules OPEN (§4)".
   - T9: "PROPOSED".
   - The register's `open` list: "Pacifica's naturalization rule (T9, PROPOSED)".
   - The registry and bible profile also flag it.

   The "so that" clause settles §4's **[OPEN]** naturalization rule under an approved label. **Fix:** "On his way to China in 1859 he swears allegiance to the Republic at San Francisco. **[PROPOSED — CR-074]** The oath alone makes him a Pacifican, so that no American consul can touch his trade. **[APPROVED — CR-074]** The company serves under the Pacifican consul's licence, paid by the taotai Wu Xu and the banker Yang Fang. Its first assault…"

4. **§25, l. 947: the Calamba evictions are mentioned in 1888, before they happen.** The 1888 paragraph says "In the Philippines the Council charters companies of the islands' men, whose warrants are paid in the friar land, and the families evicted at Calamba have first claim." The evictions are of 1890–91 (F8; storyline l. 1062: "the land board's evictions at Calamba in 1890–91"), and the reader meets them 115 lines later. **Fix:**
   - At l. 947, end the sentence at "…whose warrants are paid in the friar land."
   - At l. 1062, inside the CR-074 Borneo block after the New Calamba sentence, add: "Tenants evicted at Calamba who serve in the Philippine companies have first claim on the friar-land warrants."
   - The C-1888-COMPANIES-ACT condition text can stay; it is not a quote.

## Should fix

5. **§25, l. 1009 (1894): wrong belligerents, and the sentence sits next to OPEN-1.** The text reads "The companies serving both sides stand down from armed duty under the Act." No company serves Japan: CR-074 F has "Not partners: Japan after 1875". The companies affected are China's Customs companies and Korea's guard. Two smaller problems:
   - The sentence comes after the armistice, so it reads as hindsight.
   - It directly follows "Queen Min survives and Gojong does not flee…", so "the guard at Seoul keeps to the palace" hints at the company's part in her survival, which is OPEN-1.

   The paragraph is unlabelled base text, so the sentence cannot move earlier inside it without shifting the label. **Fix:** remove it from l. 1009 and add a new paragraph after that one: "**[APPROVED — CR-074]** Through the war the companies serving China and Korea stand down from armed duty under the Act. Fong's revenue cruisers keep to the customs, and the guard at Seoul keeps to the palace." The ledger's `more_quotes` for C-1888-CAPITULATION-KOREA stays verbatim.

6. **The family farm's size (E2) is not recorded consistently.** E2 and the Fact changes section make "80 irrigated or 160 dry acres" the family farm, a new canon fact, and AGENTS.md l. 141 states it. Elsewhere it is missing or contradicted:
   - The storyline never states it (l. 945: "and ten years a whole farm").
   - C-1887-LABOUR (ledger l. 6152 ff.) is unchanged.
   - C-1888-COMPANIES-ACT, `open` (l. 6214), says "Acres MODEL".

   **Fix:**
   - l. 945: "…and ten years a whole farm, the family farm of eighty irrigated acres or a hundred and sixty dry that the labour law allows a household."
   - Ledger l. 6214: "The acreage of the half and whole farm APPROVED (CR-074 E2, the family farm); scale MODEL."
   - C-1887-LABOUR: add "the family farm is 80 irrigated or 160 dry acres (CR-074 E2)".

7. **The amendment of CR-037 E7 (T5, D-24, R-3) is not carried into CR-037's own record or the storyline.** Storyline l. 956 (CR-037, APPROVED): from 1888 the Office publishes "for every chartered body … how appointments and promotions compare with the examination lists". Raised companies are chartered by the Office (I1), so without qualification that rule reaches them. Neither `CR-037.md` nor the CR-037 entry in `change_requests.json` notes the exception. **Fix:** at l. 947, after "…preach under arms", add "The Office's appointment tables do not count whom a raised company takes, since it rules no one at home." Also add a one-line amendment note ("E7 amended by CR-074 D14, 18 November 2026") to the CR-037 register entry or decision record.

8. **Labels: Part N's PROPOSED labels became APPROVED without comment, and one detail has no decision behind it.** Part N labels every passage **[PROPOSED — CR-074]**, and its §4 note says "The clause on Ynitia and his men is PROPOSED — CR-074". The integration uses APPROVED throughout. For most passages the decisions table supports this (D-1 to D-37). Two points remain:
   - Part C's heading is "dates APPROVED; details PROPOSED unless marked". C1's first holders ("Sealers on the Mexican islands under Mexico's permit, Okhotsk whalers, guano men on the equatorial islands and traders bound for Hakodate…", l. 248) were **[PROPOSED — CR-071]** and are covered by no D-item. Only Crabb is (D-30).
   - "Local labels retained" in the status line needs confirming as "labels follow the decisions table, not Part N's draft labels".

   **Fix:** l. 248: "<!-- CR-074: the first licences and Crabb --> **[PROPOSED — CR-074]** Sealers on the Mexican islands … take out the first licences. **[APPROVED — CR-074]** In 1857, when the Republic refuses Henry Crabb…". Ask the author to confirm the rest. The C-1854 `more_quotes` (Crabb) keeps APPROVED.

9. **AGENTS.md l. 141 and CR-074 K3 settle the Miwok guide's people, which the registry keeps open.** AGENTS says "the Coast Miwok are distinct from the Sierra Miwok of Elias's guide". The registry's CT-MIWOK-GUIDE (registry l. 1125 ff.) says "The character's exact people (Miwok or Yokuts) … remain open", and storyline unresolved item 6 (l. 1687) has "Miwok/Yokuts collaborators". The storyline itself (l. 203, 231) says only "a Miwok guide". **Fix** (AGENTS l. 141): "the Coast Miwok of Olompali are distinct from the people of Elias's Mokelumne guide (CT-MIWOK-GUIDE, Miwok or Yokuts, OPEN) and must not be merged with them". Make the same change in K3 if CR-074.md is revised.

10. **§26, l. 1144 and §25, l. 947: "the old Council" and "the Council" are ambiguous.** The text reads "the Philippine crown takes over the islands' companies from the old Council". It comes one paragraph after "The Act dissolves the Territorial Council" (Hawaii, l. 1142), and AGENTS calls that body "the appointed Council". The body meant is the Philippine Council (l. 722, F8). **Fix:** l. 1144: "…from the Philippine Council"; l. 947: "In the Philippines the Philippine Council charters companies…". Ledger C-1888-COMPANIES-ACT already says "the Philippine Council".

11. **Model, E249: warrants are redeemed from 1888, but the first can be earned only in 1893.** The row runs 1888–1932 at 350 a year. A warrant is earned by five years' service under the Act (E1), and service before 1888 under licence earned none: C8 says farms were "bought with pay and prize money". Only the wound and death rider (E3) yields warrants before 1893. 350 a year from 1888 gives about 9,450 by 1914, which matches F's 9,000 only because of the five extra years. **Fix:** either start E249 in 1893 and raise `cp_warrants` to about 410 to keep F's 9,000 by 1914 (×27 vs ×22 years), or state the assumption (pre-1888 service counted, or the wound rider) in the lever note and `finance/CR-074-workbook.md`. Effect: about $0.3m.

12. **Model: the workbook departs from CR-074's Model section without a recorded decision.** The Model section asks for:
   - the prize money of 1878 and 1914, and the hosts' pay, "as income from abroad";
   - the home half "as a deposit liability";
   - the warrant men in the population model.

   The workbook adds none of these. It models only the home half's net interest, and it adds Ward's bequest, which the section does not list. The note's reasons are sound: these are private income, and the men are too few to move the population. But the CR still says otherwise. **Fix:** update `CR-074.md` § Model to match what was built, citing the 12:02 authorization, or record the author's acceptance in the workbook note.

## Nits

13. **§4, l. 182:** Part N and R-33 fold Ynitia into the Olompali sentence; the integration appends a separate sentence after "The losses leave Elias…", so the paragraph steps back to the battle after the reflection. This is defensible, since a mid-sentence label would put CR-074 over canon text. Tighten "whose men hold the ground beside the Republic's men under their own leader" ("headman" and "their own leader" overlap) to "…headman of the Coast Miwok of Olompali, and his men hold their own ground beside the Republic's."
14. **§8, l. 336:** "answers as Marcy answers" → "answers as Marcy has answered". Marcy's reply (28 July 1856) comes before the Confederation is in force in November. Add "and does not accede" so that the 1919 accession (l. 1266) has its setup: "…it will keep the rules on neutral goods and blockade, and does not accede; it will give up letters of marque when…".
15. **§19, l. 819, the will:** "fifty thousand taels for his Chinese wife" introduces a wife the storyline has never mentioned → "for his wife Changmei, Yang Fang's daughter". "sets the money against Harry's share" → "sets the Chinese money the steamers cost against Harry's share of the estate".
16. **§19, l. 819:** "serves on under its own captain beside Gordon's Chinese" → "serves on under its own captain and Gordon's orders" (C2: "serves under Gordon's orders by its articles").
17. **§19, l. 819:** the CR-071 summary says "a company guards the Keelung coal in 1884–85", and four sentences later CR-074 says "At Keelung in the spring of 1885 … a company lands". This is not a contradiction (licensed late 1884, C5) but reads as one. Also "a company lands to guard the coal company's miners" uses "company" in both senses in one clause → "…a company lands to guard the miners of the Chinese–Pacifican coal company". The CR-074 comment "(T6)" sits after the amended sentence instead of before it.
18. **§19, l. 819:** CR-071's PROPOSED "and lend sergeants to the army mission" was dropped, and Part N does not restore it. R-22 (C3, approved under D-4) keeps the sergeants, discharged and enlisted in the mission. Optional: "…in 1875 Japanese sergeants take their place; sergeants who join the army mission are discharged from the companies first."
19. **§25, l. 1062 (Borneo):** Part N places the block "after Unsan"; the integration splits CR-029's paragraph at New Calamba. That is a better hook, but the paragraph now runs to 1899 and then returns to "When cholera returns in 1888". Mat Salleh is first "a Sugut chief" and named only in the next sentence → "orders the village of Mat Salleh, a Sugut chief, burned". The "because" in "buys that land by compact … because it holds its coast by the Sultan's lease and its interior only by compact" is odd for a site on Marudu Bay, which is coast. Suggest "…before it grants it, as it must for any land beyond its stations."
20. **History (Borneo):** the company's burning of Mat Salleh's village was on 29 August 1895, at Jambongan (Wikipedia, "Mat Salleh Rebellion"). The storyline's refusal of 1894 is a divergence the author may keep, but 1895 would anchor it to the real order. The "to verify" in `historical_background.md` (the rising's end) can be closed: sources give 1903 or 1905. Mat Salleh's death was 31 January 1900 (some sources give 1 February). The Palatan meeting was on 19 April 1898, and Cowie was managing director: both correct as used.
21. **§25, l. 1011:** "and never the camphor frontier" → "and never serves on the camphor frontier against the mountain peoples" (F3).
22. **§30, l. 1266:** "and gives up the letters of marque it issued in 1914" (the letters lapsed with the war) → "and gives up privateering for good, five years after Julian's letters".
23. **§26, l. 1144:** the Hawaiian clause ("The restored Hawaiian legislature passes an act of its own for Hawaiian companies") sits in the Philippine paragraph. It belongs at the end of the Act of Settlement paragraph, l. 1142, after the CR-072 sentence.
24. **§28, l. 1212 / C-1914-LETTERS:** APPROVED letters "the next day" hang on a declaration of 23 August that sits under **[PROPOSED — CR-040]**. AGENTS.md and the register turn this into "from 24 August 1914". Add an `open` note: "dated from the declaration of 23 August, PROPOSED — CR-040".
25. **Ledger C-1856-PARIS-NOTE (l. 6217):** `owes = [{ by = "PAC", to = "PAC" …}]` is a self-obligation. Name the beneficiaries ("partners and neutrals") in `what`, or use `conditions` only. C-1888-CAPITULATION-KOREA has no `until` though F2 gives 1905; this is correct while the storyline is silent, and an optional §26 clause would let the ledger end it: "Korean officers it trained take over the king's guard when Japan takes its agreed military rights."
26. **Workbook:** the `cp_tael_usd` label says Shanghai tael, but its note says "About $1.39 to the Haikwan tael". $1.39 is the Shanghai tael; the Haikwan tael was worth more. "Ten thousand taels in gold" could also be read as ten thousand taels' weight of gold, about fifteen times the modelled value. If the storyline means value, write "ten thousand taels' worth in gold" (l. 819, and the registry/bible). The note shows 1887 domestic taxes falling by $0.02m with no event in that year, more than the 1868 bequest itself; say why (iteration?). Events "Story status" reads "Approved" for E247–E250 but "Proposed" for E246 and earlier; AGENTS says the column is not a canon label, so align it or say why.
27. **Character bible, CR-074 notes:** CT-LI-HONGZHANG's "for reasons the Chronicler gives fairly (the amnesty policy, Taicang's feigned surrender, the leaders' demands)" is not in CR-074. Ward's marriage to Changmei (registry/bible) is historical but appears only in the background note. CT-CALEB's "his name is read at each year's review" conflicts with K4 and K7, where the roll opens with the dead and Caleb's name is on the colour → "his name, among the living of 1846, is on the colour of Olompali carried at each year's review".
28. **Registry, CR-074 request record:** `updated_ids` lists CT-LI-HONGZHANG, CT-LOGAN-TURNER, CT-FONG, CT-CALEB and CT-SILAS-CLAIMANT, but none of those registry entries changed; only the bible notes did. Either say "bible notes only" in `limits`, or follow whatever CR-071's record does.
29. **Storyline header, l. 103:** "North Borneo holds its interior only by compact" → "the Pacifican Borneo company holds North Borneo's interior only by compact".
30. **Storyline §25, l. 945:** approved items that have no storyline text yet: D-9 (nurses from 1888), D-13 / D13 (acts of state), I8 (the review), K7 (Caleb's colour) and B6 (1907: the conventions signed, the reservation kept). None is required, and nothing contradicts them. Listing them here so their absence is deliberate.
31. **Fidelity check, no finding:**
   - D-14 (Siberia's line guard) has no storyline text; the CR-044 line guard at Omsk is untouched.
   - OPEN-1 is not narrated, apart from the juxtaposition in item 5.
   - The numbers agree across storyline, ledger, registry, bible, background, AGENTS.md, the register and the workbook note: Korea first in 1888 and China second (autumn); Formosa from 1895; Philippine crown companies from 1907; accession at The Hague in 1919; Ward 1831–1862, shot 21 September, died 22 September 1862.
   - Historical anchors used in the text that I checked and found sound: the Declaration's terms, Marcy (28 July 1856), Seward (1861), Dobroflot (1878), Convention VII of 1907, Keelung (August 1884; the port held October 1884 – June 1885), Hakodate (Enomoto October 1868, Kuroda June 1869), the Kaitakushi and tondenhei dates, Burgevine (4 January 1863), Gordon (March 1863) and Suzhou (4–6 December 1863).
