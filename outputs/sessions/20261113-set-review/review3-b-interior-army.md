# Review 3-B — CR-060 (interior), CR-061 (Rio Grande), CR-067 (army)

Fresh-context review, 13 November 2026. Read: AGENTS.md, the canon extract (§§8–13), CR-060, CR-061 (to line 640 in full; open decisions and research tasks skimmed; its self-review section not read), CR-067, and only the cited rows of CR-068 (G6/G7/G9a text, CT8, CT10, CT15, CT16, CT23, CT24, CT29), CR-059 and CR-062 (grep only). Nothing under `outputs/sessions/` was read. `cr_facts.py preview` was run read-only on the three drafts. Historical checks are from my own knowledge, with confidence marked; none was checked against a source.

Classes: **BLOCKER** (fix before integration), **SHOULD-FIX**, **NOTE**. "Author" = needs an author decision; "mechanical" = can be fixed without one.

---

## 1. Blockers

**B1 — CR-060 D5 and §10 text: the Legion clause deepens CT7 while CT7 is deferred. BLOCKER, author.**
CT7 (line 365–370) is deferred and its decision line says the Legion's pay and the Black Hawk War stay out of the storyline. The pay was struck, but the 13 November rewrite of D5 (line 60) adds that Young "binds the Legion to the common defence of the roads and the valley, under its own officers", and the §10 text (line 265) carries it: "binds Lot Smith's cavalry and the Nauvoo Legion to the common defence of the roads and the valley". That makes the Legion's defence of "the valley" a treaty obligation of the Compact, under Deseret's own command, from July 1863 to 1867, which covers the Black Hawk War years (N6, Circleville). It contradicts N1 ("no volunteer companies") and CR-059 N5 as quoted in CT7 ("force only under confederal command"), and it is the protected-intent exposure CT7 was opened for, now reached by a different clause. Either the clause is cut back to the articles' "road guard" until CT7 is decided, or CT7 is decided first.

**B2 — CR-061 C0a: the Rio Grande resolution authorises the wrong war. BLOCKER, author (wording), then mechanical.**
C0a (line 49) has the Council vote, before 13 April 1862, "to clear the Confederate invasion from the road and hold the valley". The same draft says a Confederate army in New Mexico "is a partner's venture" (line 170), that "Richmond and Monterey are partners, and neither commander has orders to fight the other" (C5), and that at Mesilla "neither side has orders to fight" (C7, line 214). The campaign the resolution has to cover is against Canby: the second Valverde, Fort Craig, Santa Fe, Taos, Fort Garland. As worded the resolution orders the fight C7 says nobody ordered and does not mention the Union. In addition: the row has no Status cell (two cells in a three-column table); C0a is cited nowhere else in CR-061 and is absent from its storyline text; and news of Glorieta (26–28 March) cannot have reached Monterey before a vote taken before 13 April, so the Council votes while Sibley holds Santa Fe. CR-067 A1 rests on this row.

**B3 — CR-060 CO4 and the §12 Colorado text: the named crest puts South Park on the wrong side. BLOCKER, mechanical once the author confirms the intended line (open decision 16).**
CO4 (line 119) and the storyline block (line 298) run the 1865 line "over Poncha Pass and along the Mosquito and Front Range crests (Kenosha and Ute passes)" and make South Park Pacifican. The Mosquito Range is the west wall of South Park, between it and the upper Arkansas; a line on its crest leaves South Park to the Union. Kenosha and Ute passes are on South Park's east rim (Kenosha/Tarryall/Puma Hills), which is the line the result needs. High confidence. The text would enter canon as a boundary.

**B4 — CR-060: four load-bearing items are still "to confirm" and are written into the storyline text and into CR-067/CR-068 as fact. BLOCKER for integration, author (confirmation only).**
D4a (the Union closes its wire in April 1864), D8 (no warrants for 1862 because the articles are not retroactive), D9 (the 1862 killers surrendered under "of any date"), C5 (the September 1863 resolution as Washoe's mandate) each read "drafter's suggestion … raised no objection; to confirm". The §10 text states all four without qualification (lines 270, 275); CR-067 A1 and CR-068 G6/line 322 repeat two of them with the same caveat. AGENTS.md: do not mistake an assistant suggestion for approved canon.

---

## 2. CR-060 — internal consistency

| # | Where | Finding | Class |
|---|---|---|---|
| 1 | Fact changes, lines 432, 448–459 | Text and pasted preview say "five fact changes"; the block has seven, and the CT1 block has three, not the "2 change(s)" shown. A fresh run gives 7 and 3, lint clean. The pasted output is stale | SHOULD-FIX, mechanical |
| 2 | Ledger, lines 384 and 395 | The Compact is entered twice: new C-1862-DESERET-COMPACT and C-1862-DESERET "renamed the Compact of Association". One instrument, two entries. Also dated from 1862 although the Compact is of July 1863 and the articles lapse on its signing | SHOULD-FIX, mechanical |
| 3 | D5(a) vs open decision 11 | D5 has Jefferson Hunt sign the December articles "for the Republic"; open decision 11 leaves "whether Hunt rides as Deseret's man or the Republic's" open | SHOULD-FIX, author |
| 4 | D9 and §10 text vs open decision 2 | D9 and the text have the killers "given up to the travellers' court by their own people"; open decision 2 still asks "whether the killers are surrendered at Box Elder or tried in their absence" | SHOULD-FIX, mechanical |
| 5 | C5 and §10 text vs open decision 4 | Text decides who marches (volunteers who will not stay; Nye); decision 4 says "who marches stays open" | NOTE, mechanical |
| 6 | Line 498 | "Not done, because they need the author: Elias's calendar for the winter of 1862–63 (who signs the Compact), the resolution for the Salt Lake and Washoe operations" is stale: both are now written in. The other three items it lists (Deseret's ratification vote, South Park's charter, the Owyhee court's jurisdiction) appear nowhere in "Open decisions" | SHOULD-FIX, mechanical; the three items author |
| 7 | Self-review, lines 550, 564, 566 | "No fresh-context reviewer has seen the draft" (line 498 cites one); question 2 still asks about "an anti-Mormon commander"; question 4 about "Victoria's question about Bear River". All superseded | SHOULD-FIX, mechanical |
| 8 | Part III, line 214 | Sherman accepts the crossing "because it ends a garrison's slow starvation"; C1 and line 203 have the garrison eating California's flour | SHOULD-FIX, mechanical |
| 9 | §10 text, line 270 | "after a winter in which Lincoln tried to make it a state": the winter's constitution was the territorial convention's (C3); Lincoln's act is March (C4). The distinction matters, because the Terms' reservation is triggered only by Congress | SHOULD-FIX, mechanical |
| 10 | D4a, open decision 14 | Union traffic passes "under the Compact" from October 1862; the Compact is of July 1863. Should read the articles, then the Compact | NOTE, mechanical |
| 11 | Structure | The §12 and §19 storyline blocks (lines 295–303) sit under "## Canon tensions"; CT9 sits after "Financial and population models" (line 424). CT9 has no json block and no decision line in the form the others have | SHOULD-FIX, mechanical |
| 12 | R4 | "(R4–N8)": the Ute agreement is N7; N8 is the Owyhee Paiute | NOTE, mechanical |
| 13 | Part I table, lines 165–166 | Camp Floyd appears in two rows | NOTE, mechanical |
| 14 | Fact pattern `washoe-retaken-spring` | Neither pattern matches the storyline sentence ("Pacifica retakes it in the spring of 1864"), so the date is unprotected | NOTE, mechanical |
| 15 | M8 vs Part IV | M8: the company is "armed by their own district" and also "men Pacifica's supply system armed". Pick one | NOTE, mechanical |
| 16 | §10 text | "The articles run for a year" against D5's "until the Compact is signed, or to the end of 1863" | NOTE, mechanical |
| 17 | C6 | "her conditions for what is done with Washoe afterwards" lists Hawaii's control of entry at its own ports, which is not about Washoe | NOTE, mechanical |
| 18 | D5 "none within a day's ride of the city" | Camp Floyd is put at forty miles, which is a day's ride | NOTE, mechanical |

---

## 3. Deseret (task item 2)

**Statements checked across D4–D9, CT1, the CT1 fact block, the ledger note, Part II and the §10/§12 text.** They agree on: working articles, December 1862, signed by commissioners while Elias is in New Mexico; what the articles cover (passage, supply, wheat for gold, three named posts, Legion and Lot Smith as road guard, the travellers' court); no pledge in the articles; the Compact at Salt Lake on 24 July 1863, signed by both principals; the pledge given in person; the Legion bound to common defence; "of any date"; Lee surrendered at the signing and hanged in the autumn; Bear River a limited action with warrants only for January 1863; Box Elder on 30 July with Elias present and Beale signing; accession by vote in December 1866 and on exchange in 1867. CR-067 B6 and CR-068 (line 384, CT24) say the same. The exceptions are items 2, 3, 4, 10 and 16 above, B1, and these:

- **D5 vs CR-061 C12. NOTE, mechanical.** D5: "Elias is at Santa Fe" in December 1862. C12 has him on the river in early December, at Taos in mid-December and at Santa Fe "at the turn of the year". "In New Mexico" is safe.
- **The pledge is also unmandated, and neither CR says so. SHOULD-FIX, author.** See 5.2 below.

**Logic: Young.**
- **Lincoln's word reaches Young before he signs. SHOULD-FIX, author.** CR-068 line 384 dates Lincoln's assurance through Stenhouse to 7 June 1863 and says it "comes too late". On CR-060's new calendar the Compact is not signed until 24 July, so Young has the assurance in hand for six weeks and still pays Lee, the Legion and "of any date" for a pledge against an enforcement Lincoln has just disclaimed. CR-060 never mentions Stenhouse (only research task 7). Young needs a stated reason to disbelieve Lincoln, or "too late" must change. The Gettysburg and Vicksburg news the draft already brings to Salt Lake that week could supply it (a winning Union will enforce later), but the draft does not use it that way.
- **What the pledge adds is thin as stated. NOTE, author.** From October 1862 Pacifica is at war with the Union and holds every former federal post in Utah, Fort Bridger included; Harding leaves in the spring "under the articles". Young is described as left "seven months with a garrison on his road and no promise", but no federal force exists within a thousand miles. The pledge's real content is the peace (Pacifica will not hand Deseret back). Saying so would make the seven months' wait credible.
- **"Of any date" is wider than the bargain. NOTE, author.** The words expose every Mountain Meadows participant and, as accessories, Young's own circle, yet "he gives up one man … the others are not found". An understood limit, or Young's reason for trusting there will be no second warrant, is missing. Self-review question 5 (ex post facto; a confederal court trying an 1857 crime committed in United States territory) is still unanswered, and open decision 10 leaves court, judge and jury open. The court sits at Salt Lake, a city Pacifican soldiers enter unarmed and by invitation; who holds and hangs Lee there is not said.

**Logic: Elias.**
- **Absence. SHOULD-FIX, author.** On the merged calendar he leaves Monterey in November 1862 and is at the capital for about a week (late April to 5 May) and five days (10–15 June) before the last days of August 1863: some ten days in ten months, in wartime, as Protector. From 15 June to late August he is beyond the wire, since D4a routes Monterey's traffic by courier. CR-061 C12 defends only the first six months ("his opponents in Monterey say so less kindly"). Camp Boise (July 1863) and the Northwest fall in the second absence. Who acts for him is not stated in any of the three drafts.
- **The articles of December were authorised from where? NOTE.** Elias leaves Monterey in November, weeks after the column arrives in October; the wire west of Salt Lake runs through Nye's Washoe and S2 allows only summer trains on the Humboldt. So the articles' text and Bear River (January) are Denver's and Hays's decisions without Monterey. That suits "written orders", but the draft should say the articles were settled before he left or that Denver had powers.
- **Six days. NOTE, author.** The three words are added at Elias's demand on 24 July; by 30 July Beale has the bands agreeing to surrender men "named for the emigrant killings of 1862". D8 says no warrants were ever issued for 1862, so nobody has named them. The 1862 killings (the Snake) are also outside Deseret, so Deseret's consent cannot found the jurisdiction; only the bands' own compact can.

**Bear River.**
- **Plausibility of "nobody in the camp is killed". NOTE, medium confidence.** Historically the lodges stood in the ravine that was the fighting position. A morning's fight there with dozens of dead on both sides and no one in the camp hurt needs the ground stated (the men come out to the bank; the lodges are upstream).
- **Days. NOTE.** "Hays marches on 24–29 January": five days in deep snow is feasible from the Bear River crossing post, not for infantry from Camp Floyd (forty miles beyond Salt Lake). Name the post.
- **Protected intent.** D8, D9 and M8–M10 keep it: a limited action under written orders; a massacre by miners that Pacifica prosecutes. No breach, apart from B1.

**The itinerary, 1862–63.**

| Leg | Dates | Check |
|---|---|---|
| Monterey–Yuma–Tucson–Mesilla–Taos | November to mid-December 1862 | About 1,450–1,500 miles in about six weeks: stage pace through an Apache war and past the Fort Craig lines. Feasible, no slack |
| Santa Fe–San Antonio | First days of January to early February | About 950 miles in about 30 days. Feasible |
| San Antonio–Mesilla–Yuma–Monterey | Late February to late April | Feasible |
| Monterey, then Honolulu | News about 2 May; sails "at once" (CR-061 C12) or about 5 May (CR-068 CT24); speaks about 20 May | Agrees within three days. NOTE, mechanical |
| Honolulu–Monterey | Last week of May to about 10 June | Feasible by steamer |
| Monterey–Salt Lake | About 15 June to about 20 July, "about five weeks" | Agrees in CR-060 D5 and CR-068 CT24 |
| Box Elder–Monterey | 30 July to "the last days of August" | **Does not agree with the outward leg.** Five weeks from 30 July is 3 September; even crediting Box Elder's sixty miles it is about 1 September. Every draft dates the Terms to August. SHOULD-FIX, mechanical: either the road is shorter than five weeks or the Terms are printed in the first days of September |

Also: "relay coach" at five weeks for the road is wagon pace (about 28 miles a day on roughly 950–1,000 miles from Monterey; Part V's "700–800 miles" is measured from an unnamed California base). A relay coach would take two to three weeks, which would cure the return leg. NOTE.

CR-061 C12 and CR-068 CT24 agree with CR-060 on every date except the two noted.

---

## 4. Washoe, 1863–64 (task item 3)

CR-060 (C2, C4–C6, D4a, §10 text), CR-067 A1/B7 and CR-068 (G6, G7, CT8, CT10, CT23, line 322) agree on: Terms printed August 1863 with the first reservation; Council adoption in September 1863 as the mandate; Enabling Act March 1864; retaking in April under Marcus with about 1,500 and no fight; garrison out armed and unparoled; the wire cut in April 1864; four conditions asked and three granted at the May 1864 renewal. No contradiction found between the three drafts.

- **The mandate's logic. SHOULD-FIX, author (part of B4).** Hawaii's delegation votes for the Terms "because they bind him", and that vote is then the "standing authority" for crossing into territory Pacifica recognised as American at Carson. CR-067 A1's own rule is that a new theatre "needs a new resolution"; a declaratory adoption seven months earlier is the weakest reading of it. Victoria, who stopped Washoe in 1860, would see that she had signed a blank cheque. C6 and A1 instead make her "no annexation" answer the 1862 garrison. If the September vote is to stand as the mandate, her recognition of what she voted for belongs in C6.
- **The telegraph, internally. SHOULD-FIX, mechanical.** D4a: after April 1864 "Deseret's wire runs from Salt Lake west". Pacifica holds Fort Bridger and South Pass (R1), so the wire east of Salt Lake to the line is also in its hands, and the gap a rider must cross is not Denver–Salt Lake.
- **The telegraph, historically. SHOULD-FIX, medium-high confidence.** The transcontinental line of 1861 ran by Fort Kearny, Julesburg, Fort Laramie, South Pass and Fort Bridger to Salt Lake; Denver had a branch from Julesburg from 1863. A Union wire cut "west of the divide" ends near South Pass, not at Denver, and the 500-mile mountain ride in CR-060 D4a and CR-068 line 322 (result on the 15th) is unnecessary. The line was a private company's; "the War Department stops carrying traffic" needs an order closing it. D4a's own route west ("by Carson and Fort Churchill") is right.
- **Gettysburg and Vicksburg. NOTE.** D5 has "Vicksburg's surrender"; canon §11 has Pemberton withdraw and Grant capture the city, with dates OPEN. CR-068 CT10 already flags both battles as assumed. Use "the fall of Vicksburg".

---

## 5. CR-067 A1 against the operations (task item 4)

1. **Rio Grande column, 1862.** Has a resolution (C0a), which fails as worded: B2. Fort Garland (March–May 1863) is in Colorado Territory since 1861; "hold the valley" covers it only if the San Luis Valley is read as the upper Rio Grande. One clause in C0a would settle it. NOTE, author.
2. **Salt Lake road, October 1862.** No resolution, by design, and all three drafts say so. But A1 calls it "an invited guard on a road and not a theatre", and the same unmandated command then (a) fights the Bear River action in January 1863, with dozens of dead, and (b) carries Elias's pledge of 24 July 1863 that the Republic "will not suffer the Union's law to be enforced in Deseret by arms", which is a new commitment of the army and arguably a change of war aim. Part II says outright that Elias gets the Legion "without asking Hawaii or the Assembly for a vote". A1 lists "three interior operations" and is silent on both. D9 then says Victoria "has nothing to ask about Bear River" in May 1863, which sits badly beside A1's statement that she and Sherman held the garrison needed a vote. **SHOULD-FIX, author:** either the Compact goes to the Council (the September 1863 session is available) or A1 names the pledge and Bear River as part of the same grievance.
3. **Washoe, 1864.** Satisfies the rule only on the reading discussed in section 4.
4. **Idaho and Montana.** Camp Boise (July 1863), the circuit courts and mounted police are not mentioned in A1; CR-059 contains no resolution for them (grep). Presumably the 1861 Northwest resolution. NOTE.
5. **1865.** CR-067 A1 and CR-068 CT29/G9a agree: armistice in May, the Protectorship expires on the last day of May, Chancellor until the Enabling Law in December. CR-061 A1 agrees. One gap: the Navajo treaty, the Apache peace and the Paso del Norte convention are all "1865"/"late 1865"; none of the drafts says under which office they are signed, in the months CR-068 line 349 describes as having "no lawful government" for the interior. NOTE, author.

**CR-067's own consistency.**
- Lines 3, 32 and 154 still say the open offices "stay OPEN" and that candidates "enter the registry only if the author chooses them"; Stone, Alden, Naglee, Denver, Pico, Johnson, Watkins and Kalākaua are approved in the same file. The registry row for Hays still reads "(CT1, if amended)". SHOULD-FIX, mechanical.
- A1: a full stop is missing before "**How the three interior operations**"; the Status cell does not cover the 13 November additions. NOTE, mechanical.
- Candidates table, Denver row, "Alternative" cell reads "Marcus's Washoe force of 1864 (CR-060 C5)", which is not an alternative. NOTE, mechanical.
- B7 Status column mixes "PROPOSED" (Great Basin, with an approved commander) and "PROPOSED; commander approved" (California). Ord's rank of brigadier appears only in the registry table. NOTE, mechanical.
- B6 cites CR-060 D7 for the Legion entering the Defense Law at accession; D7 is held. Cite D12 and canon §10. NOTE, mechanical.
- The §11 storyline sentence leaves the acting chief unnamed although Stone is approved. NOTE, author's choice.

---

## 6. Canon and protected intent (task item 5)

Declared departures (CR-060 CT1–CT9; CR-061 CT1–CT8; CR-067 CT1–CT2) cover what I found against the extract, with these exceptions:

- **Colorado never becomes a state in 1876 (CR-060 CO6–CO8).** Canon §13 has "a disputed Hayes election"; historically Colorado's three electors decided it. Research task 6 notes the altered fact but no tension is raised. NOTE, author (the Union's map is already different, so it may only need a line).
- **CR-061 Part IV, line 407** still argues from "CR-015 H6 … sets Bear River beside the Navajo treaty", which CR-060 CT5 and CR-061's own CT8 note have replaced with the Owyhee. SHOULD-FIX, mechanical.
- **CR-061 §10 text, line 478:** "The Chiricahua take passage money … and Pacifica takes the old copper mine on a lease that pays them a royalty." N4 and ledger C-1865-SANTA-RITA pay the royalty to the Chihenne, whom N5 distinguishes from Cochise's Chiricahua. SHOULD-FIX, mechanical.
- **Protected intent.** Bear River (D8), the Navajo (N2–N3: no campaign, by choice), the Apache war (C6's limits; peace in 1865), the Mescalero (the Union's campaign, not Pacifica's) and the Owyhee (private killers, prosecuted) do not breach "no campaign of extermination". The only exposure is B1.

---

## 7. Labels (task item 6)

- CR-060: B4 (suggestions written as fact); items 3, 4, 5 of section 2 (decided in the tables, open in the list); CO8 is "PROPOSED (author-endorsed beat)" in the table and [OPEN] in the §19 text.
- CR-061: its storyline rule (line 448) is that a passage is [APPROVED — CR-061] only if every row it rests on is approved. Two passages break it: the compact's opening and signing (line 476) rest on K1, PROPOSED; Connelly's withdrawal to Las Vegas (line 461) rests on F2, PROPOSED. SHOULD-FIX, mechanical. M1's Status is "APPROVED (CT4)" while its text still says "lending from 1865 is PROPOSED (CT4)". NOTE, mechanical. C0a has no Status (B2).
- CR-061 registry, line 597: Lubbock "signs Texas's resolution at San Antonio"; C8 has the session and the signature at Austin. NOTE, mechanical.
- CR-061 M1 has Juárez at Paso del Norte "from August 1865"; the §13 text says "from the autumn of 1865". NOTE, mechanical.
- CR-067: as listed in section 5.

---

## 8. Historical plausibility (task item 7)

| Claim | Where | Assessment | Confidence |
|---|---|---|---|
| Line on "the Mosquito … crest" with South Park Pacifican | CR-060 CO4, §12 text | Wrong range (B3) | High |
| The Union's wire "ends at Denver" | CR-060 D4a; CR-068 322 | The line ran by South Pass and Fort Bridger (section 4) | Medium-high |
| January 1862: the convention "elects Brigham Young governor" | CR-060 D1, §10 text | The convention of 20–23 January wrote the constitution; Young was elected governor at the election of 3 March 1862. SHOULD-FIX, mechanical | Medium-high |
| "the Soda Springs agreement with Pocatello's bands" | CR-060 D9, N2, registry | Pocatello signed the Box Elder treaty of 30 July 1863; Soda Springs (14 October) was with mixed Bannock and Shoshone bands under other leaders. SHOULD-FIX | Medium |
| Sagwitch and Bear Hunter sign Box Elder | D9 | Bear Hunter died at Bear River historically and Sagwitch did not sign; both are consistent divergences here | — |
| Beale as commissioner in 1862 | D4 | Historically Lincoln's surveyor general of California and Nevada 1861–64; the draft's own research task 5 notes it. A stated reason he is Pacifica's man is still owed | High (fact) |
| "Santa Fe taken on 23 March" 1862 | CR-061 line 172, 182 (Boatner) | Confederates entered about 10–13 March. Not in storyline text. NOTE | Medium |
| Hunter left Tucson "4 May 1862" | CR-061 C5 (Colton) | I recall 14 May. NOTE | Low-medium |
| "in 1861 Pico's ill health made him decline … a Native Cavalry battalion" | CR-061 C3 (Pitt) | The battalion was raised in 1863; the offer and refusal are of that year. NOTE | Medium |
| Blanca Peak "inside Pacifica" | CR-061 N3 | It stands on the Sangre de Cristo crest, which is the line until the 1880–82 survey. NOTE | High |
| Nevada: first constitution rejected January 1864; Enabling Acts for Nevada and Colorado 21 March 1864 | CR-060 C3–C4 | Correct | High |
| Camp Floyd abandoned July 1861; Morrill Act July 1862; Harding arrives July 1862; Plummer hanged 10 January 1864; Box Elder 30 July, Fort Bridger 2 July, Ruby Valley 1 October, Soda Springs 14 October 1863; Hill's smelter 1868; rails at Cheyenne 1867 and Denver 1870 | CR-060 | Correct as dated | High |
| Glorieta, Valverde, Apache Pass, West's commission, Mangas's death, Reily at Irish Bend, the Texas called session of February 1863, Juárez at Paso del Norte, Connelly's death, Carson's and Josefa's deaths | CR-061 | Correct as dated | High |
| Stone, Naglee, Denver, Alden, Dominis, Kalākaua, Pico, Ord career facts | CR-067 | Consistent with what I know. Ord was a serving U.S. officer in California from 1847, so he does not fit the draft's own "came as a civilian" filter and needs his divergence stated | Medium-high |
| "the first time in the West that a court hangs white men for killing Native people on Native testimony" | CR-060 M9 | Unverifiable from memory; already flagged "to verify". Keep it out of the storyline until checked | — |

---

## 9. Verdicts

- **CR-060: not ready.** Two author decisions (B1 the Legion clause against CT7; B4 confirmation of the four suggestions) and one boundary error in storyline text (B3). After those, the remainder is mechanical apart from the Stenhouse timing, the unmandated pledge and Elias's absence, which the author should see before integration.
- **CR-061: ready after mechanical fixes and one author wording decision** (B2, the resolution's object and status, and its place in the storyline). The rest is labels and three stale or mismatched sentences.
- **CR-067: ready after mechanical fixes,** on condition that A1 follows whatever is decided for B2, B4 (the Washoe mandate) and the Salt Lake pledge; its stale "OPEN" statements must be removed first.
