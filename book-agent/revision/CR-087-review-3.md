# CR-087 review 3 (fresh context, final, 24 November 2026)

I reviewed `CR-087.md`, revision 5, whole. I read the draft, `AGENTS.md`, the storyline at `L629`, `L632`, `L655`, `L664`, `L727` and its other mentions of Montana, `C-1867-WESTERN-LINE` in the ledger, the CR-087 parts of `population/draw_map_1887.py`, `lewis_crest_strip.geojson`, the last lines of `homelands_1887.md`, the picture `map_1887.png` round Missoula, `CR-071-I-map.md` line 409, `CR-060` N5, and `CR-083` for its cross-references (`A6`, T4, the 08:22 answer). I read no review, proposal or prose-check file and no writer's notes. `preflight.py --draft` gives 0 errors and 0 warnings; `cr_facts.py preview` reports no fact changes declared. I measured the ring with my own read-only script and checked the *Hist.* claims against the draft's own sources and the Newberry atlas's county chronology.

## Verdict

**Ready for the author's approval.** No blocker. The six items under Should fix are each a sentence or two, change no decision, and are worth making before integration; S1 and S2 are worth making before he reads.

## Blockers

None.

## Should fix

**S1. "Everywhere else ignores watersheds"**
- *Passage:* `A2`, The words: "a peace that everywhere else ignores watersheds does not suddenly follow one for its last thirty miles."
- *Problem:* Canon does not ignore watersheds everywhere else: `L629` has "divide crests", `L632` runs the Colorado line "to the divide at Berthoud", `L655` gives the Utes "Colorado west of the divide". The draft's own `A1` runs the line on the divide for the sixty miles from Marias Pass to Flattop, immediately south. The approved reason then rests on a premise that the CR's own line contradicts. "Thirty miles" is also unclear: Flattop's head to the parallel is 10 miles straight and about 11 along the ring's crest; only the divide's own way round by the Livingston Range approaches thirty.
- *Fix:* Keep it as the surveyor's argument and narrow it: the peace takes the front or the crest that can be held and uses a divide only where the divide is that crest; where the two part, at Flattop, it keeps the crest. Drop "everywhere else"; drop the mileage or say whose miles.

**S2. The county line "at the county's making", and how much of it is withdrawn**
- *Passage:* `A2`, The meridian: "a county line drawn in 1867 at the county's making ... the Realm withdraws it as a matter of course."
- *Problem:* (a) `L655` has "western Montana's counties" electing a convention in 1866, so counties exist before 1867. In our history Missoula County dates from 1860 and was re-created by Montana Territory on 2 February 1865; the meridian comes from an exchange with Deer Lodge on 20 November 1867 (Newberry atlas chronology). The author's words are "a county line of 1867", not a county of 1867. (b) Only the part north of about 48°27′ N is east of the treaty line. South of it the same meridian is Missoula's edge against another county of Pacifica, and the redrawn map still shows it. "Withdraws it" reads as the whole line.
- *Fix:* "a county line redrawn in 1867"; "withdrawn north of the point where it crosses the divide". Name the neighbouring county if known.

**S3. The St Mary valley does not cross the parallel inside the old strip**
- *Passage:* `A4`, What the crest line gives up: "On the map as drawn the Belly and St Mary valleys cross the parallel inside the Realm". Also `A1` last bullet ("the easy road into Alberta by the Belly and St Mary valleys") and `T-2` Case A.
- *Problem:* The old strip reached the parallel between about 113.84° and 113.47° W. The Belly (about 113.69°) and the Chief Mountain crossing (about 113.66°) are inside it. The St Mary River crosses the parallel about three miles east of Carway (113.38° W), some six or seven miles east of the meridian, on ground the old map also gave the Union. What the strip held of the St Mary is the upper lake and valley, as `A1`'s second bullet says correctly.
- *Fix:* `A4`: "the Belly valley crosses the parallel inside the Realm, under Chief Mountain". `A1` and `T-2`: "by the Belly valley" and "the upper St Mary and the Belly country".

**S4. `L632` is touched and is not in the impact notes or the tensions**
- *Passage:* `A1` first bullet, `A2` The words, `## B`, `T-1`.
- *Problem:* `L632` says "In Montana it is the mountain front where the Missouri leaves the hills". The draft gives the peace a quoted phrase for this stretch, "the crest of the main range of the Rocky Mountains", which canon does not contain. In northern Montana the mountain front lies east of the Lewis Range, close to the withdrawn meridian, so a reader holding `L632` would take the meridian for canon's line. The draft handles this only by an OPEN item (where the line passes from front to crest) and by `T-1`, which concerns `L629`.
- *Fix:* Add `L632` to `## B` with one clause (the front governs where the Missouri leaves the hills; from Marias Pass north the peace says crest), and either widen `T-1` to name `L632` or add a short `T-3`. Mark the quoted treaty phrase PROPOSED where it stands.

**S5. Labels: one item with two, and an approval gloss wider than the quoted words**
- *Passage:* `L-4` row; `## E` amended commitment "(survey of 1874, PROPOSED)"; `A5` heading; the "PROPOSED by the drafter" list.
- *Problem:* (a) The survey of 1874 is in `L-4`'s APPROVED cell and PROPOSED in `## E`. (b) `L-4`'s gloss ("the peace said 'crest'; the meridian was a county line of 1867 and is withdrawn") is not in the author's quoted words of 10:45, which give: no exchange, the surveyor's loss of about 90 square miles, no revanchist press, "about ten miles" kept, the exact crossing OPEN, the Marias killings and the starving winter unmentioned. The rest comes from the item he answered, which is not quoted. (c) `A2`'s "the particulars are PROPOSED" does not say which; the PROPOSED list omits them (the treaty's quoted phrase, who drew the meridian, the commission's finding for the higher crest, "noticed in Ottawa"), and omits `A4`'s cut line and monuments. (d) `A5` carries no label and has no decision row.
- *Fix:* Quote the answered item's sentence beside the 10:45 words, or cut `L-4`'s gloss to what the words give and cite the item. Give the survey year one label. List `A2`'s particulars under PROPOSED. Give `A5` a label (its first sentence rests on 06:55; the second is `CR-083`'s).

**S6. "The Realm" in 1865–1874, and two meanings of "the map as drawn"**
- *Passage:* `A2` ("the Realm's surveyor", "the Realm withdraws", "the Realm now touches"); `A1`, `A4`, `## B`, `## D`, `T-2`, `L-1` ("the map now shows as the Realm's").
- *Problem:* (a) The Realm begins with the Constitution of 1887; in 1867–74 canon says the Confederation, the Republic or Pacifica. Set pieces drawn from `A2` would inherit the anachronism. (b) "The map as drawn" means the old map in `A1`'s last bullet, `A4` and `L-1`, and the redrawn one in `A1`'s first bullet and `## D`. On this branch the picture no longer shows the strip as the Realm's, so `L-1` and `A4` are now wrong as worded.
- *Fix:* Pacifica or the Confederation before 1887. "`CR-071`'s map" for the old one, "the redrawn map" for the new, throughout.

## Minor

**M1. Process notes in the body.**
- *Passage:* `A3` first bullet ("The author asked at 07:09 ..."), `A3` last bullet ("The drafter's view ..."), `A4` ("The author chose the crest knowing this (08:22)"), `A1` ("This is the drafter's statement").
- *Problem:* House rule: no notes about the drafting in the body.
- *Fix:* Move to the status block or the decision rows; keep the facts.

**M2. *Hist.* claims without an address.**
- *Passage:* `## Sources`, last bullet and "Not verified".
- *Problem:* Mount Cleveland, the tripoint, the Ktunaxa crossing (*Hist.* in `A3`) and Missoula's meridian have no address. "The Union builds one at Chief Mountain in our history" is unmarked and should read "the United States". The Parks Canada page gives 1921 and 1927 and does not say who built the road. The Bigfork page says the Chief Superintendent of Dominion Parks advocated the road by Akamina Pass and the North Fork; it does not mention British Columbia, which is geography.
- *Fix:* Add addresses; for Missoula, https://publications.newberry.org/ahcb/documents/MT_Individual_County_Chronologies.htm (20 November 1867, exchange with Deer Lodge). The North-West Territories existed from 1870, so that "not verified" can be closed with a source. I did not recheck the 8 August account.

**M3. `A2`, What nobody intends, standing alone.**
- *Problem:* Without `CR-083`, Pacifica already borders Canada along British Columbia's whole line from 1871, so the accident noticed in Ottawa has weight only with `CR-083`. The standalone merge check lists `A4` and `A5` and not this bullet.
- *Fix:* Add it to the check, or say only "touches the North-West Territories".

**M4. Wording across sections.**
- `L-5` says "the standstill rule"; `A3` calls it `CR-070`'s land rule. Use one name.
- `## B`: "it loses about 420 square miles ... to the Union" reads as a transfer in 1887; by `A2` the line was withdrawn in 1874 and the county of 1887 never held it. Say that the map of 1887 is corrected.
- `A1`: "its eastern edge is a meridian ... for its whole length" is slightly too strong; the picture shows a jog at the south end.
- `## D`: `map_1887.md` still gives Missoula as made of "Missoula" whole; a footnote there would match `## B`.
- `A2`: "the higher and carries the highest summits of the two" says the same thing twice.

## What holds

- **Geography.** The divide follows the Lewis Range from Marias Pass to Flattop and then the Livingston Range into Canada (National Park Service). Mount Cleveland is the Lewis Range's highest summit and lies on the ring (48.925° N, 113.848° W). The Mokowanis is a branch of the Belly and heads on the crest. The parallel crosses Upper Waterton Lake between the tripoint and the crest. Akamina Pass leads into British Columbia. Chief Mountain, Many Glacier and the Belly lie between the crest and the old meridian.
- **Figures against the map.** My measure of the ring: about 415 square miles west of the meridian and south of the parallel (script 411, atlas 420); the crest meets the parallel at 113.836° W, 10.5 miles from 114.068° W; the old meridian is 27.3 miles from the tripoint; seven hand-placed points, the last beyond the parallel; the ring starts at 48.44° N. 420 and 90 make the 510. `homelands_1887.md` says what `## B` and `## D` report.
- **The picture.** Missoula's north-east edge follows the crest to the parallel; the strip is drawn as the Union's; the faint dotted meridian shows the old line; the county to the east ends in a point on the divide. The caption names CR-087 as a draft.
- **History.** Article 4 of the treaty of 1855 has the quoted words. The advance party found the old monument on the summit on 18 August in the 1874 season. Akamina: advocated in 1915, road to Cameron Lake open in 1927.
- **`A2` as a whole.** With S1 and S2 mended it holds: the peace says crest, a legislature overreaches on paper in 1867, the survey of 1874 has two crests and one phrase, and the only loser is the Union's surveyor. It agrees with `L655` and `L664` (western Montana accedes by charter, 1866–67) and with the ledger's treaty of 1867. No exchange, no revanchist press, no mention of the Marias killings or the starving winter, as the author asked.
- **`CR-083`.** `A6` and T4 say the same: the Union touches Caledonia nowhere, Missoula meets Alberta at Waterton Lake with no road or rail, the Union's border with Canada begins east of it. `A5`'s Burrard sentence matches.
- **Approved items not contradicted:** the crest north of Flattop; surveys only (no road or railway is built); a separate CR with the map change.
- **House rules.** No exclamation marks; citations in form; figures MODEL; OPEN items listed; preflight clean.

## Questions for the author

Needed before approval: none. Two he may wish to settle while approving:
1. Is "the crest of the main range of the Rocky Mountains" to be the peace's wording in canon, or only "crest" with the phrase left PROPOSED (S4)?
2. Does the line run on the divide from Marias Pass to Flattop (the drafter's PROPOSED bullet in `A1`), given that `L632` gives Montana the mountain front?

Can wait: whose country the upper Waterton valley is; a landing and customs officer at Boundary Bay; a CR on treating with the Piegan; the exact point on the parallel (Mount Boswell suggests nearer 113.86° W, about 9.4 miles); which body drew the line of 1867 and on which day.
