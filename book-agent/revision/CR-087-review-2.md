# CR-087 review 2 (fresh context, 24 November 2026)

I reviewed `book-agent/revision/CR-087.md`, revision 3, in a fresh context. I read the draft in full, `AGENTS.md`, lines 629, 632 and 727 of `master_storyline.md`, the entry `C-1867-WESTERN-LINE` in `commitments/data/ledger.toml`, the map commit `bd1b453` (the change to `population/draw_map_1887.py` and to `population/outputs/homelands_1887.md`), `population/data/counties/lewis_crest_strip.geojson`, the picture `population/outputs/map_1887.png` around Missoula, and from `CR-083.md` only the passages that name this CR (its header, `A6`, `A11`, `T4`). For context I also opened row N5 of `CR-060.md` and line 409 of `CR-071-I-map.md`, which the draft cites. I read no earlier review, no planning file and no session record.

Scripts: `preflight.py --draft` reports 0 errors and 0 warnings; `cr_facts.py preview` reports no fact changes declared. I ran no script under `population/`. With my own read-only measurement of the geojson ring (shapely, the script's flat formula): the ring is valid; clipped to the meridian at 113.4663° W and the parallel it holds 415 square miles, which agrees with the script's 411 for the part inside the county; its west edge crosses 49° N at 113.8364° W, which is 10.51 miles from 114.068° W. The draft's two figures from the map therefore stand as the script's measure.

Web checks made today: the treaty of 1855, article 4 (Washington State University's text of the treaty); the boundary survey of 1874 (Manitoba Historical Society, "Markers on the Forty-Ninth"; Wikipedia, "Boundary Commission Trail"); the Akamina road of 1915 (the Bigfork Eagle article the draft cites); Mount Boswell and Campbell Mountain (Wikipedia). I did not recheck the Parks Canada page on the Akamina Parkway or the Geological Survey papers.

## Verdict

One more revision. The line, the map change and the agreement with `CR-083` hold. The reason given for the line (`A2`, decision L-4) does not: the bargain it describes is no bargain, and the loser it names has won.

## Blockers

**B1. The exchange in `A2` gives the Union nothing it did not already have, and the named loser gained.**
- *Passage:* `A2`, "The survey": "The Union gives way, and gets something for it: the meridian strip. ... The Realm gives up the strip east of the crest, some 420 square miles, for the crest itself." And "The loser": "The Union's surveyor, who files a protest that the divide was the natural line and is overruled by a commission that wants to go home."
- *Problem:* Three things do not fit together.
  1. The draft's own words of the peace are "the crest of the main range of the Rocky Mountains". Both candidate crests, the Lewis and the Livingston, lie west of the meridian at 113°28′ W. On either reading of the phrase the strip east of the Lewis crest is the Union's by the treaty. The Realm's only title to it is a county line of 1867 that the draft itself calls "a legislature's line" which "follows nothing on the ground" and which the Union "had protested since". So the Realm pays with ground it never held under the peace, and the Union concedes the trough for nothing. A commissioner would see that.
  2. The outcome hands the Union about 411 square miles, the St Mary country and the one easy road north, against about 90 square miles of trough with no pass and no mineral. A protest by the Union's surveyor, and a revanchist press that takes it up in the 1890s, are hard to credit when his side came out four to one ahead. The party that lost something real is the Realm (the county's ground, the road at Chief Mountain) or the Piegan, who are not asked.
  3. The draft does not say whose legislature drew the meridian in 1867, the year of the exchange, or why it ran a county across the mountains onto the Blackfeet's side against the words of a peace two years old. Without that, the meridian is our timeline's county line showing through.
  A smaller point follows from the first: if the commission of 1874 trades territory, it amends the treaty and needs a ratifier on each side; if it only reads the phrase, it does not.
- *Fix:* Choose one of two accounts and write `A2` on it.
  - (a) *The meridian is the peace's own provisional line.* The negotiators of 1865 did not know the country north of Marias Pass, so the peace ran the last stretch "due north to the forty-ninth parallel" from the point where the divide was known, "until surveyed", and the county of 1867 simply followed the treaty. In 1874 the surveyors replace a line nobody can find on the ground with a crest. Then the exchange is real, both sides give something, and the loser is on the Realm's side: Missoula County, or the Realm's surveyor who wanted the St Mary grass and the Chief Mountain road and is overruled by a commission that wants to go home. The protest and the press of the 1890s move to the Realm, or are dropped. A protocol of 1874 then needs a line in `## E` (who signs, who ratifies).
  - (b) *The words stand and there is no exchange.* The peace says "crest of the main range"; the county line of 1867 is a Pacifican overreach, explained in one sentence, and is withdrawn in 1874 as a matter of course. The only contest is which crest. The Union yields the trough because its own treaty of 1855 and the height of the Lewis summits argue for it. Then the Union's surveyor can stay as the loser, but his loss is the 90 square miles and the principle, and the draft should say so plainly and delete "gets something for it".
  Either way, delete the sentence "That argues for one line and not for the eastern one" or finish its thought; as it stands it concedes that the first argument does not decide the matter and then moves on.

## Should fix

**S1. Missoula's eastern edge is described wrongly.**
- *Passage:* `A1`, second bullet: "North of about 48°27′ N its eastern edge leaves the divide and runs due north along a meridian".
- *Problem:* On the picture the meridian is Missoula's eastern edge for its whole length, from about 47° N to the parallel. South of about 48°27′ N the ground between the meridian and the divide is drawn as Silver Bow County (our timeline's Deer Lodge panhandle), which narrows to a point where the divide crosses the meridian. Missoula's edge never follows the divide. After the redrawing, the Realm's counties along the line are Silver Bow up to that point and Missoula from there north.
- *Fix:* Say that the Realm's outer line follows the divide to about 48°27′ N, where Silver Bow County ends in a point, and that north of it Missoula ran on along its meridian. Check the sentence proposed for `L629` and the note for `CR-071` against this.

**S2. The script's report line gives an area that is not the county's.**
- *Passage:* `draw_map_1887.py`, the new `report.append`: "the county is 17,022 sq mi as drawn"; `B`, "is about 19,070 square miles (MODEL)".
- *Problem:* 17,022 is the county less the Flathead homeland (1,813 square miles in the same file), as `## D` says and the report line does not. A reader of `homelands_1887.md` gets a county 2,000 square miles smaller than the draft's impact note states, with no explanation there.
- *Fix:* Add "outside the Flathead homeland" to the report line, and in `B` give the figure by one named measure (the atlas's, or the script's 18,835 with the homeland).

**S3. Historical claims are sourced to a review file and not in the draft.**
- *Passage:* `## Sources`, last bullet: "Confirmed by the reviewer, with sources in `CR-087-review.md`"; `A3`: "(*Hist.*, from memory)".
- *Problem:* The house rule is that a claim marked *Hist.* has its source with it. The treaty of 1855, the date in 1874, the tripoint, Mount Cleveland, the Marias, the winter of 1883–84 and the Ktunaxa have no address in the draft, and a later reader may not be given the review. "From memory" also contradicts the same bullet, which lists the Ktunaxa hunts as confirmed, while Piikani use of the trough is listed as not verified but is stated flatly in `A3`.
- *Fix:* Put the addresses in `## Sources`. Mark the Piikani sentence "to verify" and remove "from memory".

**S4. The date of 1874 has two versions in the sources.**
- *Passage:* `A2`: "the survey of the 49th parallel closes at the divide, on 18 August (*Hist.*)".
- *Problem:* The Manitoba Historical Society's account has the advance party find the monument of the earlier survey on the summit on 18 August; the Wikipedia article on the Commission's trail has the last marker placed on 8 August at Waterton Lake. The draft's wording is defensible but the set piece on Flattop depends on the season's calendar.
- *Fix:* Say "reaches the monument on the divide on 18 August" and note the other date under `## Sources`.

**S5. "Partly surveyed" for the Akamina road is not in the source.**
- *Passage:* `A4`: "It is advocated, partly surveyed and not built, as in history."
- *Problem:* The cited article says the superintendent of Dominion parks proposed the link in 1915 and that there is little evidence Canada pursued its part. It supports "advocated" and "not built" only.
- *Fix:* "Advocated and not built, as in history", or source the survey.

## Minor

**M1. Seven points, not eight.**
- *Passage:* `## D`: "eight points placed by hand"; the geojson's `note` says the same.
- *Problem:* After the last vertex taken from the atlas (113.841° W, 48.8559° N) the ring has seven hand-placed vertices, and the seventh is at 49.02° N, beyond the parallel.
- *Fix:* "Seven points, the last beyond the parallel", in both places (the note can wait for the next change to the file).

**M2. The crossing point may lie a mile or so further west.**
- *Passage:* `A1`: "about ten miles (the review measures 10.3)"; `## D`: "113.836° W, 10.5 miles".
- *Problem:* Mount Boswell, on the lake's east shore, is at about 113.866° W and one kilometre north of the parallel, with Miche Wabun Peak five kilometres to its south-east. If the watershed between the lake and the North Fork of the Belly runs over Boswell's south ridge, the crest meets the parallel nearer 113.86° W and the border is about nine miles. That is inside the draft's stated error and the point is OPEN, so nothing is wrong; but three figures (ten, 10.3, 10.5) for an unsettled point read as more precision than there is.
- *Fix:* Keep "about ten miles" in the prose and say once that 10.5 is the hand-drawn ring's figure. The other hand points agree with Mount Cleveland (48.925° N, 113.848° W) and the ridge by Stoney Indian Pass to within about a mile.

**M3. "Past the head of the Belly River".**
- *Passage:* `A1`, fourth bullet.
- *Problem:* The Belly heads under Ahern Peak, south of the point where the divide leaves the range. North of that point the crest's east side drains to the Mokowanis, a branch of the Belly.
- *Fix:* "Past the head of the Mokowanis, a branch of the Belly".

**M4. Citations not in the house form.**
- *Passage:* `A3`: "(line 727 of master_storyline.md; `CR-070`)"; `B`: "line 409 of CR-071-I-map.md"; `A3` and `B`: `L629` without a phrase.
- *Problem:* The form is `L727 ("grants nothing")`. Line 727 does carry the quoted words.
- *Fix:* Write `L727 ("the land office grants nothing")` and give `L629` its phrase each time.

**M5. Events of our timeline stated as events of the story.**
- *Passage:* `A3`: "after the killings on the Marias in 1870 or the starving winter of 1883–84".
- *Problem:* Canon does not say either happens. Baker's column of 1870 marched from Fort Ellis by Fort Shaw; in this canon the Gallatin valley is the Realm's.
- *Fix:* "After events such as our timeline's killings on the Marias (1870) or starving winter (1883–84), if they happen here", or leave both to the later CR.

**M6. The code.**
- *Passage:* `draw_map_1887.py`, the lines added in `main()`.
- *Problem:* `sqmi` is a number inside the loop above and is rebound as a function below it. Nothing breaks, because the loop has finished, but the name now means two things in one function. The picture's caption still reads "CR-071 Part I, draft 12 (17 November 2026)" and does not say that the map carries `CR-087`.
- *Fix:* Name the function `sq_miles`; add "with CR-087's Lewis crest" to the caption at the next run.

**M7. "The range's highest summits".**
- *Passage:* `A2`: "the eastern crest, which is the higher and carries the range's highest summits".
- *Problem:* Two ranges are being compared.
- *Fix:* "Carries the highest summits of the two".

**M8. North-West Territories.**
- *Passage:* `## Sources`, "Not verified: ... whether the country north of the parallel was part of the North-West Territories in 1874".
- *Problem:* In our timeline it was, from 1870; the district of Alberta dates from 1882. Whether this canon's Canada follows is `CR-083`'s matter.
- *Fix:* Move it to the confirmed list with a source, and write "the North-West Territories".

## What holds

- **The geography.** The divide on the Lewis Range from Marias Pass to Flattop and then on the Livingston Range; the trough through the Waterton valley and the lake; Mount Cleveland on the eastern crest; the tripoint at 114°04′ W; Akamina Pass on the divide north of the parallel, so that a road over it crosses a corner of British Columbia to reach the North Fork; Chief Mountain, the Belly and the St Mary all east of the crest. The vertices taken from the atlas pass Triple Divide Peak and Logan Pass where they should.
- **The treaty of 1855.** Article 4 runs the Blackfoot line north to the parallel, west along it to the main range and south along the range, as quoted.
- **The figures.** 411 square miles and 10.5 miles are what the ring gives. 27 miles for the old border is right for a meridian at 113.466° W. About 420 by the atlas's measure against 411 by the script's is a difference of two per cent and is explained in `## D`.
- **The code change.** It is sixteen lines, it touches only Missoula, and it is in the right place: after the homelands' pass, whose twelve-kilometre smoothing would otherwise remove the tapering trough. The ground taken off is computed from the county before that pass and added to the Union's side, so the picture shows it grey with our timeline's meridian still dotted through it, which is what a reader needs. The docstring's sentence is accurate. The ring's overhang east of the meridian and north of the parallel leaves no sliver in the picture.
- **Agreement with `CR-083`.** `A6` there says Missoula reaches past the divide to the Lewis crest and meets Alberta at Waterton Lake with no road or rail, that the Union touches Caledonia nowhere and that its border with Canada begins east of the lake; `A11` and `T4` say the same. Nothing in this draft contradicts it. "A few miles" in `T4` against "about ten" here is loose and harmless.
- **The approved items.** The draft does not contradict the Lewis crest (07:19, 08:22) or "road surveys only" (07:19). The status line and the standalone merge check say honestly what is approved, what is the drafter's and what waits on `CR-083`.
- **The tensions.** T-1 and T-2 put both cases fairly, and Case B in each is the better: a crest in place of a meridian across mountains, and a border that makes `CR-083`'s map true.
- **`A3`.** It answers the author's question of 07:09 without closing it, and "nobody tells the Piegan either thing in 1874" is the strongest sentence in the draft.
- **House rules.** Plain prose, no exclamation marks, figures labelled MODEL, additions labelled PROPOSED, quotations from canon exact at L629 and L632.

## Questions for the author

1. Under the peace of 1865, was the last stretch a meridian until surveyed (B1, account a) or "the crest of the main range" from the start (account b)? The first makes the Realm the loser of 1874, the second the Union.
2. Should the revanchist press of the 1890s have this paper at all, if the Union came out ahead?
3. Do the killings on the Marias and the starving winter happen in this history? `A3` assumes so in passing.
4. Is "about ten miles" enough for the storyline, with the exact point left OPEN, or do you want it read from a topographic map before integration?
