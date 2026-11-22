# CR-081 and CR-082: final integration check (fresh context, 22 November 2026)

Branch `drafts/cr081-082-integration`, against `501791d`. Concentrates on CR-082. Line numbers are the current `master_storyline.md`.

## Verdict

**Ready to merge after the six Should-fix items. No blockers.** All five checks are clean (`lint_canon.py`, `cr_facts.py check` with 258 facts, `ledger.py check` with 332 commitments, `validate_character_docs.py`, `sync_master_storyline.py --check`). Every APPROVED CR-082 decision that belongs in canon is carried. No CR-083 work, prairie contract or Caledonia passage appears in the prose. Protected intent is intact. The two CRs agree on the tables, Manchuria, Siberian grain, entry and families, the granary and nitrogen. The faults are of three kinds:
- one phrase that turns the Chile loan round, so the Realm seems to owe Chile;
- MODEL figures written under APPROVED labels;
- one hidden dependency on CR-083 in the century's figures.

## Blockers

None.

## Should fix

**S1. 1560: the Chile loan reads backwards.** "the loan on the duty remains the regency's debt to Chile" makes Pacifica the debtor. Line 1129 and ledger row `C-1891-CHILE-NITRATE` both have Chile owing the Realm. CR-082 D has the same phrase, but the storyline must not contradict itself. Replace the sentence with:
> **[APPROVED — CR-082]** From the 1920s the Columbia's ammonia replaces Chile's nitrate in the Realm's fields, and the regency's loan to Chile is left secured on a duty the Realm's own fields no longer pay. **[OPEN — CR-082]** What Julian's ministers do with the loan.

After that, update `more_quotes` in `C-1891-CHILE-NITRATE` and rerun `ledger.py check`. This also gives the scene its point: the Realm's own ammonia weakens the security of its own loan.

**S2. 1018, 1256 and 1672: MODEL figures under APPROVED labels.** The register labels the crossings (1914, 1915, 1920, 1933, 1938) and the century's figures as MODEL. In the prose they sit under APPROVED. At 1018 the 1.5% (an approved story assumption) is also labelled MODEL, while Julian's 2% at 1256 is labelled APPROVED. Exact fixes:
- **1018.** Change "It shows the Realm passing what its soil and sea can feed in 1914, and she draws" to "It shows the Realm passing what its soil and sea can feed within a generation, and she draws". Replace the closing MODEL sentence with:
  > **[APPROVED — CR-082]** The regency's tables let growth fall over a century to 1.5% a year, on the Realm's own diet held constant. **[MODEL — CR-082]** The table of 1890 starts from growth of about 4% a year and puts the crossing in 1914.
- **1256.** Replace the last sentence with:
  > The table of 1910, the first to count the Philippine crown, moves the crossing back, and mother and son read it together and quarrel over its century. **[MODEL — CR-082]** It puts the crossing in 1920 and the century's need at nineteen times the home ceiling.
- **1672.** Open the paragraph with "**[APPROVED — CR-082]** The programme's yields keep moving the Office's crossing back, and Julian's table of 1930 looks a century ahead. **[MODEL — CR-082]** The table of 1920 puts the crossing at 1933 and the table of 1930 at 1938." Keep "Julian's table of 1930 has … thirteen times the home ceiling." under that MODEL label. Restore "**[APPROVED — CR-082]**" before "The provisioners' plan for that century". Put "**[MODEL — CR-082]**" in front of "It closes only by buying…" and restore "**[APPROVED — CR-082]**" before "The sufficers answer". If the 0.6% is kept (see S3), it should also be marked MODEL.

**S3. 1672: the century's figures rest on CR-083.** "About three-quarters" and "six-tenths of one per cent" come from `provisioning.md` §8, which counts work 2, the northern water (26.2 million mouths). That work is CR-083's and not in canon. Without it the model gives about 81% bought (473 of 587 million mouths) and a fitting rate of about 0.40% (`slowing_that_fits` on 252.3 million, computed for this check). The prose never names the northern water, so nothing leaks in words, but the numbers already assume it. Choose one:
- **(a)** Make the prose true without CR-083: "It closes only by buying three-quarters or more of what the world's grain sellers sell abroad" and "at about half of one per cent a year". Leave the register and AGENTS.md as they are, since they are restored when CR-083 merges.
- **(b)** Keep the figures and add a line to CR-082 J: "1672's three-quarters and 0.6% include CR-083's work 2; without it, about four-fifths and 0.4%."

I recommend (a).

**S4. 1256: a PROPOSED treaty article under APPROVED.** In "He lifts the entry course and adds families under the 1868 treaty's article, read as spouses and children", the family-emigration article of 1868 is PROPOSED in canon (752). CR-082 B7 and CR-081 D9 B1 both say so. Replace it with:
> He lifts the entry course and adds families, read as spouses and children. **[PROPOSED]** They come under the 1868 treaty's family article. **[APPROVED — CR-082]** Under Victoria the two figures…

**S5. Keawe is missing from the sufficers.** CR-082 B3, the register and AGENTS.md all name "later Keawe, a sufficer on land and water". No storyline passage does. Giving him the sufficers' answer at 1672 also gives that answer a speaker. Change "The sufficers answer with the Office's own figure:" to:
> The sufficers, Keawe among them on land and water, answer with the Office's own figure:

**S6. 1129: the junta's choice is hollow.** The prose holds the rifles first and only then says "The junta makes its own choice: it takes the Realm's loan and recognition in place of the rifles." By that point the rifles are already gone, so the junta is choosing nothing. Replace the three sentences from "When the Congress's agents load rifles…" to "…in place of the rifles." with:
> When the Congress's agents load rifles off the Channel Islands for the *Itata*, the Realm holds them under the venture licence's rule against private war from Pacifican soil, and its minister puts a choice to the junta at Iquique: fight on without the rifles, or take recognition as a belligerent and a loan and accept an armistice before the last battles. The junta makes its own choice and takes the loan. Balmaceda leaves Chile alive.

This keeps every element of R-7b.

## Minor

- **M1. 691.** "Powell is in the Republic's service by 1888." reads like an edit memo. Suggested: "**[APPROVED — CR-082]** He is in the Republic's service by 1888, the year his office reports how much land the domain's water can reach."
- **M2. 778.** The 1890s sentence sits before the 1878 eclipse. Move "**[APPROVED — CR-082]** From the 1890s it is the nexus of the Realm's dry-land farming programme." to the end of the paragraph, as "From the 1890s the Colegio is the nexus…".
- **M3. 1166.** "only about a twentieth of the crop land feeds work stock" is 5%; the model gives 6%. Use "about one acre in sixteen".
- **M4. 1672.** "between a sixth and a third above its residents" misses the model's 15–32%. Use "between a seventh and a third".
- **M5. 1052.** "which adds workers without adding residents" contradicts 1046 (residence after six years and a trade test). Use "which adds workers without adding residents until a worker earns residence".
- **M6. 1166 and the bible.** "Utah's agricultural college" sits in a canon where the member is Deseret (778: "Deseret's university"). Consider "Deseret's agricultural college at Logan". The storyline already mixes the two names, so this is the author's call.
- **M7. 1129 and 1166.** "yield is the sufficer's own answer" appears twice, in the singular and then the plural. Cut it at 1129: "The fields' need is the table's forecast."
- **M8. 1352.** "In 1917 the Entente's shells come first" is cryptic. Use "In 1917 Chile's nitrate goes first to the Entente's shells".
- **M9. 1447.** The APPROVED sentence calls the railway board's grain contracts "the half of the land-and-grain guarantee". That guarantee is PROPOSED at 1422 (CR-041), and its railway half is PROPOSED at 1409 (CR-030). The author approved this wording (R-8 as recast), so no change is required. Note that it hardens two PROPOSED premises.
- **M10. 1100. Julian's motive is missing.** Nothing says why he asks for the shorter count. A candidate for the author (a proposal, not canon): "to bring the Gulf's acres and people under the crown sooner".
- **M11. Character summaries (1766, 1778, 1788).** They carry none of CR-082. For example, at Victoria: "A sufficer, she asks the Office for the table of 1890 and shapes an entry she cannot shrink." At Julian: "A provisioner, he reads the tables as a target." At Keawe: "a sufficer on land and water."
- **M12. Open items (after 1883).** There is no CR-082 item. Suggested:
  > 38. **CR-082:** whether Victoria reads the Siberian minute of 1919 before 1921; the storage sites of 1900–1920 and their cost; what Julian's ministers do with Chile's loan; New Zealand's and Australia's guarantee dates (OPEN-019-06); Japan's yields, Hokkaido and any southern renunciation (the partners' CR); the Realm's diet and the farmed sea's measure (a culinary CR).
- **M13. Approved but not in the prose.** R-5 (the Mekong last, Mindanao first) and F-1e/F-10 (the sea's own line in the table) are absent. Optional addition at 1672: "Of the sellers the Mekong comes last, after Mindanao and the Philippine crown's own frontier."
- **M14. 1672.** "a thriftier table stays out of the Office's tables" points to a CR still to come. Use "the Office keeps the Realm's present table in its figures".
- **M15. 1256.** The paragraph jumps to the table of 1910 just before the paragraph on November 1908. Consider placing it after the November 1908 paragraphs.
- **M16. Ledger.**
  - `C-1915-ENTENTE-GRAIN` lists FR as a party with no obligation. Either add `{ by = "FR", to = "PAC", what = "repayment of its share" }` or drop FR (the storyline says "London owes").
  - The `open` note of CR-081's `C-1929-SOYBEAN-COMPACT` ("Settles CR-082 L's date (OPEN there)") is stale: CR-082 L now gives 1929.
- **M17. `provisioning.md` §1 (line 26, generated by `provisioning.py`).** "Storage on the Sacramento, the San Joaquin and the Snake from 1900" contradicts F-1c as revised and CR-055 (the background notes that Shasta and Friant closed those runs). Use "Storage from 1900 only where salmon pass or none run (the upper Snake above the falls, the foothill reaches)".
- **M18. CR-082.md T9 and K.** They say CR-054's sentence and the finance workbook are revised "on integration". The sentence was revised; the workbook was deferred, as AGENTS.md says. Make the record say the workbook was deferred.

## Literary effect

- **Powell (1018).** Has agency and an opponent: he is believed over the Land Fund's sales office.
- **Victoria (1018, 1052).** Has a motive and a defeat she cannot undo ("shapes entry and cannot shrink it"). In Chile she is only "Victoria's government"; she would be stronger as the Regent who chooses.
- **Julian (1256, 1100).** The quarrel over the table of 1910 is the best new scene. His Senate request of 1931 lacks a motive (M10).
- **The junta (1129).** Its agency is nominal until S6 is applied.
- **The two schools (1020, 1672).** Clearly argued but expository. With S5 the sufficers' answer at 1672 gets a voice. The sufficers win in the Gulf refusal (1100) and in Giannini's case (1695).
- **CR-081 and CR-082 together.** The granary scene (1695) and the Manchurian plot (1720) carry the grain-trade aim dramatically. 1672 states it as cabinet doctrine and keeps CR-075's "never stated".

## Checked

- The five canon checks, all clean.
- The full storyline diff against `501791d`, with each CR-082 insertion read in its paragraph and section (691, 778, 1017–1020, 1052, 1100, 1127–1129, 1165–1168, 1255–1256, 1352, 1447, 1560, 1672, 1752, and summary line 115).
- CR-082.md in full, including the decisions table and canon tensions T1, T2, T9 and T11 (taken as author decisions).
- CR-081-outline's guiding principle and Part D (G-1 to G-14, D9).
- CR-082's register entry, ledger rows and AGENTS.md paragraph; the CR-082 sections of the character bible and historical background; the registry's IDs and count (362).
- Every figure against `provisioning.md` §§2–9.
- One recomputation with `provisioning.py`: the slowing rate without work 2 (S3).
- Authority dates (the regency 1887–1907, Julian from November 1907).
- Protected intent; CR-058 (never embargo), CR-075 (never stated), CR-055 (salmon), CR-054 (Japan's own nitrogen), CR-039 and CR-048 (the Gulf's tests), and CR-041 (Siberia 1919–21).
- Label restoration after each inserted passage, which holds everywhere.
- A search for CR-083 material (prairie, Caledonia, northern water, plebiscite) in the storyline, ledger and bible.

## Not checked

- The CR-081 passages beyond where they touch CR-082 (already reviewed).
- `outputs/sessions/`, `CR-082-outline.md`, and every review and verification file (excluded by instruction).
- The finance and energy workbooks, which are not updated for CR-082.
- `provisioning.toml`'s sources, and the *Hist.* claims marked "to verify".
- `canon_facts.toml` beyond what `cr_facts.py check` verifies.
- `approved_change_index.md`.

## Fixes applied (22 November 2026)

- **S1–S6:** applied as worded above; for S3, option (a), with a note in CR-082 J that F's 76% and B3's 0.6% include CR-083's work 2. The ledger's `C-1891-CHILE-NITRATE` second quote follows S1, and CR-082 D uses the same wording.
- **Minor:** M1, M2, M3, M4, M5, M7, M8, M11, M12, M13, M14, M15 (Julian's tables now follow the November 1909 paragraph), M16 (France dropped from `C-1915-ENTENTE-GRAIN`; the soybean compact's note updated), M17 (the toml's storage text, report regenerated) and M18 applied. M6: "Deseret's agricultural college at Logan" in the storyline; the historical note in the bible keeps Utah's. M9 needs no change. M10 (Julian's motive for the shorter count) is not invented: it is added to the storyline's open items for the author.
