# Second fresh-context review, B: CR-060, CR-061 and CR-067 (13 November 2026)

Reviewer: a separate agent context given only AGENTS.md, the three drafts, the canon extract of §§8–13, named rows of neighbouring drafts and a list of earlier findings to verify. It did not see the session records, the earlier reports or CR-068-record.md. Points marked "(my knowledge)" or "my estimate" are the reviewer's own. Line numbers are those of commit 77feb3e.

## Verdict

CR-061 and CR-067 are close to ready; CR-060 is not. The two-step Deseret story is carried through the rows, but a stale fact block and stale prose still say December 1862, and the travellers' court jurisdiction is incoherent as written. The main obstacle is that the Washoe "mandate" postdates the operation it is supposed to authorise.

## Blockers

1. **CR-060 CT1 fact block and "Amended" paragraph still date the Compact to December 1862 (L311, L317).**
   - Stale: L311 "the Compact of Association in December 1862 (D5)"; L317 `"deseret-compact-of-association", "year": 1862` with pattern `In December … Pacifica and the State of Deseret sign`.
   - Current: decision line L321 and D5 (L60), "Salt Lake, 24 July 1863".
   - Why: `cr_facts.py apply` would register 1862 and lint the true date as an error.
   - Fix: split into `deseret-working-articles` (1862) and `deseret-compact-of-association` (1863), and rewrite L311. Also drop "if CT1 is amended" at L394.

2. **CR-060 Part II, Bear River (L189), still has the Compact before January 1863.**
   - Stale: "The Compact promises safe passage on Pacifica's roads, and a month later the road is bloody".
   - Current: D5, where only the articles exist in January 1863.
   - Fix: "The December articles promise…".

3. **The travellers' court: the January warrants and "of any date" cannot both stand (CR-060 D5 L60, D8 L63, D9 L64, Part II L185).**
   - D8: the court issues warrants in January 1863 for "the emigrant killings of 1862 on the Snake and the Bannack miners killed … in January 1863".
   - D5: what the Compact "adds to the articles is three words … *of any date*", and Lee is reached only by them.
   - Why: if the December article already reaches killings from before December 1862, it is already retroactive and the added words add nothing. If it is prospective, the 1862 warrants are void.
   - Fix: limit the January warrants to the January killings, as the §10 text (L275) already does. Let the 1862 killers be surrendered at Box Elder on 30 July under the words added on the 24th.
   - Also state what gives a Deseret–Pacifica court reach over Shoshone who signed nothing, on a road north of Deseret, before Box Elder.

4. **Washoe's mandate comes after the march (CR-060 C5–C6 L77–78; CR-067 A1 L59; CR-068 G8 L300).**
   - C6: Hawaii's assent to the third renewal "serves as the Council's mandate for the retaking".
   - C5: he moves "as soon as the Sierra roads open", "the week one is called", "eight months after" August 1863, so about April 1864.
   - CR-068 G8: the assent "falls due in the spring (working date late May)", and Lincoln's offer is published "in the weeks of the enabling acts, in time to reach Honolulu before the renewal".
   - Why: news of an act of 21 March cannot reach Honolulu and return as a mandate before a march in April. A member legislature's renewal is also not the "new Council resolution" A1 requires.
   - Fix (a): a Council resolution of autumn 1863 adopts the Terms' first reservation as standing authority, and Victoria's conditions are the price at the renewal after the fact.
   - Fix (b): move the march to May and date the renewal before it. Then align all three drafts.

5. **CR-060 Part II (L183) still credits Hays with the Pyramid Lake peace.**
   - Stale: "He sends Hays, who has made one Great Basin peace already".
   - Current: D4 (L58), "the peace that followed was not his making".
   - Fix: "who has fought one Great Basin war and did not make its peace".

## Should fix

1. **What Young gets in December (D5a against D5b, L184).** The articles omit "protection from federal enforcement", the one thing he asked for in July 1862, yet L184 says "Young gets protection". Harding leaves in spring 1863 (D10) with nothing promised. State that the articles are silent or interim on enforcement and expire, so Elias has something to withhold in July.

2. **"Will not bind the Republic to the Nauvoo Legion … before he has seen it" (D5)** contradicts articles that already make the Legion and Lot Smith's cavalry the road guard. Distinguish road guard for Deseret (articles) from mutual defence (Compact).

3. **§10 text L265 pre-empts CT7.** It has the Legion guard the road "under its own command", against N1 and CR-059 N5 ("force only under confederal command"). Use neutral wording until CT7 is decided.

4. **§10 text L265 order.** "Lincoln's governor leaves by Fort Bridger in the spring" follows the July 1863 signing and reads as 1864. Say "in the spring of 1863, under the articles".

5. **Who acts for the Protector (CR-067 B2–B3, CR-061 C12, CR-060 D4/D5/D8).**
   - Elias is at Monterey about four weeks between November 1862 and late August 1863, with no wire to Santa Fe, Texas or Salt Lake.
   - CR-061 says only "the cabinet governs"; CR-067 has the Staff issue "the Protector's orders" under an acting chief of unstated rank; Marcus is abroad.
   - No row says who authorised Denver's signature in December, the Bear River orders ("on Monterey's instructions"), or the two-step design itself.
   - Add a CR-067 row on delegation, and say in D5/D8 that Denver acts on instructions Elias left in November.

6. **Travel times.**
   - Monterey to Salt Lake by Honey Lake is about 1,100 miles (my estimate; the draft gives 700–800 "from California", "to measure").
   - Late June to about 20 July, and 31 July to the last days of August, both need about 40 miles a day.
   - The drafts' own speeds are 15 (trains) and 26 (frontier). There is no margin for the 24 July parade.
   - State relay coach or light escort on the station line (S2), or leave Monterey about 15 June.

7. **Marcus from mid-1864.** CR-067 B3 has him resume "his place at the Staff" at Monterey; B7 (L80) has him command the Columbia; CR-068 G9a has him at Monterey in June 1865 while Naglee asks for orders. Choose one.

8. **Stale OPEN in the §12 text (L289):** "the representation of the new members" was decided on 12 November (CT6).

9. **Fort Bridger.** D4 posts a company there in October; U3, R1 and Part I say December 1862.

10. **CR-061 storyline has no sentence for C0a,** the spring 1862 resolution. It also says the column "leaves Fort Yuma" in April (L455) where C1 says "leaves southern California on 13 April".

11. **CR-061, 1865 instruments.** CR-067 A1 says that after 31 May 1865 the Council "votes each operation". N3, N4 and M1–M2 (the Navajo treaty, Apache peace, Paso del Norte convention and Juárez credit) carry no month and no Council vote.

12. **"Why the Compact is lawful" (L187)** argues in the draft's own voice that the agreement is "what operations require", while A1 says the operation had no mandate. Recast it as Elias's case.

13. **CR-059 N-G against CR-060 N8.** "Paulina holds out" of the Paiute peace of 1865–66, but N8 lists Paulina as a candidate signatory in 1866.

14. **CR-068 G4 (L243):** "Elias has been home from Texas since March" contradicts CT24 and CR-061 C12 (late April).

## Minor

- D4a and open decision 14: traffic passes "under the Compact" from October 1862; the articles do not list the telegraph.
- CR-061 K8: "riding up from Santa Fe on his way to Texas" reads against C12's order (Taos first, Santa Fe at the turn of the year).
- CR-060 D5 and L265 say "Elias is at Santa Fe" for all of December; C12 has him on the river and at Taos until late in the month.
- Part I table lists Camp Floyd twice; R4 cites "R4–N8" (should be N7); two sections are lettered C.
- The impact preview says "5 fact change(s)"; the list has seven.
- M8 says the company was "armed by their own district" and also by "men Pacifica's supply system armed".
- CR-067 L23 and L12 still say "Deseret's accession" as a description of canon; update at integration.
- Self-review question 2 in CR-060 still asks about "an anti-Mormon commander".

## Earlier findings: status

- Legion "on Pacifica's pay" in storyline text: gone; D7 and N6 are marked held. See Should fix 3 for the command clause.
- "Connor's camp": gone.
- "Washoe to choose for itself" granted: gone (L270 has it asked and refused).
- Enabling Act told twice: gone.
- Hays credited with the peace: **survives**, CR-060 L183.
- Denver absent: gone (D4, D5).
- Stale OPEN flags: Marcus and Montana gone; representation **survives**, L289.
- "Deseret's accession" in 1862 in CR-067: gone from B6; remains only where canon is described.
- Naglee against Wright: gone.
- Marcus in two places, spring 1864: gone, but see Should fix 7 for mid-1864 onward.
- Elias home in May or renewal "in his absence": gone from the three drafts; a variant survives in CR-068 L243.

Left for the author:

- **Deseret's ratification:** still open and accurately described. A5 states the rule with no dated row. CR-062 O6 has Pacifica ratify the treaty in summer 1866, before Deseret's December charter exists; the chambers, California and Hawaii must then ratify a polygamous member by April 1867.
- **South Park and the upper Arkansas:** still open. No post, no charter row, and absent from CR-062's table.
- **Owyhee court at Boise:** still open. M9 uses "the circuit court of M4", which sits only for "districts that sign", while CR-059 I8 has the Union's territorial government sitting at Boise.
- **Denver and Ord:** still open.
  - CR-067 L43 rests Denver's fitness on "his years with the Indian Office and in Kansas".
  - L41 rests Ord's on campaigns as a US officer.
  - Research task 2 says candidates "must have come as a civilian".
  - The same applies to Beale's "superintendent of Indian affairs for California 1852–54" (CR-060 D4).
- **CR-068's account of the nations:** mostly sound. The rule of July 1862 and the December talks are dated in CR-061. The "order of December 1862 forbidding slaving expeditions" is not: K4 is a compact clause signed in spring 1863, and N2 says only "K4 gives him that first". Add a dated order to N2.

## Literary effect

1. **The July signing has no stake.** By then Young has the garrison, the gold market and Harding gone. Give Elias something to withhold, such as an expiry on the articles or the enforcement pledge, so that Lee is a price and not a courtesy.
2. **The Salt Lake grievance is silent for eighteen months.** Have it put to Elias at Honolulu in May 1863. His ride to sign a defence compact a month later is then a defiance, and Victoria's "no annexation" of 1864 has a visible cause.
3. **The Protector passes within a few days' ride of Fort Churchill twice.** Nye can cut the wire but never tries for the man. Stage the attempt or give Nye's reason (his garrison eats California's flour).
4. **Bear River's choice belongs to no named person.** Elias is unreachable, so say whether Denver, Beale or Hays wrote "no attack on the lodges". The doctrine's first test needs an author.
5. **Five garrisons march out with arms and colours** (Walla Walla, Fort Craig, Fort Garland, Fort Churchill, Fort Union). Let Fort Churchill differ: Washoe men who split, or a wire cut.
6. **Lee's surrender has no resistance.** The Legion parades while one of its own is handed over, and the trial's jury is OPEN. A possible acquittal, or a murmur in the ranks, would cost Young something on the page.

## What I did not check

- CR-061's fact-change JSON, research tasks and process notes.
- CR-060's Colorado rows (CO1–CO9) beyond the charter question.
- CR-063 and CR-064 beyond Marcus's dates and Vicksburg.
- CR-062 beyond the listed rows.
- The character bible, `character_registry.json` (one grep only) and `ledger.toml` beyond C-1862-DESERET.
- No linter or script was run.
- Distances are the reviewer's own estimates. Historical dates were not verified.
