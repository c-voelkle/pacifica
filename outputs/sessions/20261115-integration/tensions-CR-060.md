## Canon tensions

### §12, the line in Colorado (amends the H5 Colorado segment, CT9); after the sentence fixing the line

<!-- CR-060 -->
> **[PROPOSED — CR-060]** In the Rockies the line follows what each side can hold, not the water. In Montana it is the mountain front where the Missouri leaves the hills, so that Helena, Virginia City and Bannack are Pacifican and Fort Benton the Union's river post. In Colorado it runs from the Sangre de Cristo crest across the Arkansas above Cañon City and along South Park's east rim to the divide at Berthoud: the Western Slope, the parks, South Park and the upper Arkansas are Pacifican, held from the San Luis Valley in summer and by the snow in winter; Denver, Boulder, Clear Creek and Gilpin — twenty-five thousand people and the regiment that fought at Glorieta — stay with the Union, because they can be neither taken nor fed. The Colorado article lets any mountain mining district vote itself over, binds Pacifica to supply and coin it either way and binds the Union to transit through Denver.

### §19 (the 1870s), beside the Uncompahgre lease of 1881

<!-- CR-060 -->
> **[PROPOSED — CR-060]** The Front Range comes over the way Deseret and Washoe came. Its gold fails in the refractory ores of 1864–67, its statehood is refused, and from 1868 a Pacifican smelter at the head of the Arkansas buys Gilpin's and Clear Creek's ores in coin. Pacifica's narrow gauge comes up from Santa Fe through the San Luis Valley and over Poncha Pass, and when Leadville's silver is struck in 1877 it is on Pacifica's side of the crest. Clear Creek and Gilpin vote themselves over in 1878–79 under the article, Boulder's mountain districts in 1880, and the survey of 1880–82 fixes the line along the foot of the mountains: Denver, Cañon City, Pueblo and Trinidad on the Union's side at the foot of another power's range. The Union's newspapers call it the theft of Colorado. **[OPEN]** What becomes of the Union's Colorado, Denver and the plains; the author's preferred answer is that it is attached to Kansas in the 1880s, and that the page may say *Denver, Kansas*.

### CT1 — Deseret: association in 1862, accession in 1867 (CR-015 H2 and H3; §10; registry CT-ELIAS; ledger C-1862-DESERET)

**Current:** §10 dates Deseret's accession as a confederate state to late 1862–1863, with its militia placed within the Defense Law at accession; CR-015 H2 marks the entry date APPROVED and makes Lee "the private price of accession"; H3 gives "full confederate statehood on the Hawaiian precedent"; the CT-ELIAS profile repeats the date; ledger C-1862-DESERET records an accession compact from 1862.

**Adapted (canon kept):** accession comes in late 1862–63 by the legislature's vote. Then either the Protector annexes a state by an emergency act, against canon's own condition ("no annexation by emergency decree", §9; "not emergency annexation", §10), or the confederal chambers and both founding states ratify a polygamous member state in wartime, months before the 1864–65 Assembly struggle. Lee remains the price. CR-059's Oregon campaign then runs beside a Mormon member state, which costs votes among Oregon's Protestants (CR-059 L5).

**Amended (this draft):** working articles in December 1862 and the Compact of Association on 24 July 1863 (D5, as amended on 13 November 2026); accession by the legislature's vote in December 1866 and on exchange in 1867 (D12). The 1862–63 date survives as the date of the bargain, and Lee becomes the price of the Compact. Text to revise: the §10 paragraph (draft above), the CT-ELIAS sentence in the character bible and the registry, CR-015 §1 and H2–H3 by note, ledger C-1862-DESERET. **Knock-on in CR-059 (draft):** Part V's route table and Part VI's offers table call Deseret a member in 1862–66; both become "associated (1862), member on exchange".

**Recommendation:** amend. It is what canon's Article XIV wording already demands, it gives Elias a reason (D11) instead of an exception, and it hands CR-059 the lever of holding the vote until after Oregon's.

```json
[
  {"add_event": {"id": "deseret-working-articles", "year": 1862, "patterns": ["In December (?P<year>1[89]\\d\\d), while Elias is at Santa Fe, his commissioners"]}},
  {"add_event": {"id": "deseret-compact-of-association", "year": 1863, "patterns": ["Compact of Association (?:of |in )?(?:24 )?(?:July )?(?P<year>1[89]\\d\\d)", "by the Humboldt road in July (?P<year>1[89]\\d\\d)"]}},
  {"add_event": {"id": "deseret-accession", "year": 1867, "patterns": ["Deseret (?:becomes a member state|accedes)[^.;]{0,60}in (?:late )?(?P<year>1[89]\\d\\d)"]}}
]
```
**Decision (author, 12 November 2026):** amend. Association in December 1862; accession by vote in December 1866 and on the exchange of 1867. **Amended again (author, 13 November 2026):** the association is in two steps, working articles in December 1862 and the Compact signed by Elias and Young at Salt Lake on 24 July 1863 (D5), so that he signs it in person ("Yes that's perfect I think").

### CT2 — Nevada is never admitted (CR-015 H4, APPROVED; §10; CR-059 CT9)

**Current:** H4 has the Union admit Nevada on 31 October 1864 for Lincoln's votes and sign it away months later; §10 repeats it.

**Adapted (canon kept):** the admission happens. But canon also has Washoe retaken in 1863–1864, and admission needed a convention and a vote held under federal authority (Hist.: the second convention met in July 1864 and the constitution was approved in September; to verify). The retaking would have to wait until after September 1864, against canon's own date. And the 1867 treaty would cede a state of the Union, against the plan's first principle and CR-059's "no state is ceded".

**Amended (this draft):** the first constitution fails in January 1864 (Hist.); the Enabling Act of March 1864 is Lincoln's lock; Pacifica retakes Washoe in the spring and the act is a dead letter (C3–C10). Text to revise: one §10 sentence (draft above); H4 by note. CR-059 CT9 already raises this.

**Recommendation:** amend. It turns Nevada from a convenience (a state admitted for its votes) into the sharpest move in the Elias–Lincoln agon: Lincoln uses the argument the House refused Oregon in 1859, admit to bind, and Elias answers by making the convention impossible.

```json
[
  {"add_forbidden": {"pattern": "(?:Washington|the Union|Congress|Lincoln) (?:still )?admits Nevada|Nevada (?:is|was) admitted (?:to|into|as)", "message": "CR-060 C3–C10: Nevada is never a state of the Union; its first constitution fails in January 1864, Pacifica retakes Washoe in spring 1864 and the Enabling Act is a dead letter", "kind": "fact"}}
]
```
**Decision (author, 12 November 2026):** amend. Nevada is never admitted (the author had already said so in CR-068 CT10: "Nevada does not become a state, as in CR-060").

### CT3 — The Missouri route "cut in wartime" (CR-015 H4) and Fort Benton's two-way trade

**Current:** western Montana is "supplied by Pacifica; the Missouri route to Fort Benton is cut in wartime."
**Adapted (recommended):** cut for military supply (the Lakota wars, the June-rise season, Halleck's regiments; CR-059 Part V); civilian steamers still trade both ways (M6). One clause in H4 by note; §10 does not state it.
**Amended:** none needed. Fact changes: none.
**Decision (author, 12 November 2026):** adapt.

### CT4 — "Washoe is retaken in 1863–1864" (§10; ledger C-1860-CARSON)

**Adapted (recommended):** the sentence is kept verbatim, since the ledger quotes it. The garrison is cut off from December 1862 and the retaking falls in the spring of 1864, inside canon's range. Fact changes: none.
**Decision (author, 12 November 2026):** adapt.

### CT5 — Bear River is not a Pacifican atrocity (§10 "Bear River becomes a Pacifican atrocity in January 1863 under a local commander"; CR-015 H6 APPROVED "Bear River is committed under a local Pacifican commander … One stain and one success make the friendship doctrine a choice rather than a given"; CR-059 I7 "the price of the Snake road"; §25 "Union critics answer with Bear River")

**Current:** a Pacifican massacre at Bear River in January 1863, unexplained and without consequence for its commander.
**Adapted:** keep the massacre, with a mechanism (a reserve officer who exceeds written orders) and a reckoning (inquiry, dismissal, compensation in the Box Elder compact). This keeps canon's sentence and costs a scene of Pacifica prosecuting its own, two years before it writes that into the Apache peace.
**Amended (decided):** the column marches with warrants and written orders, fights a limited action at the ravine and leaves the camp untouched (D8); the Box Elder compact opens the road (D9); the stain the doctrine needs moves to the Owyhee country in 1865–66, where miners' companies do what Connor's volunteers did and Pacifica prosecutes them (M8–M10). CR-015 H6's "one stain and one success" stands with the stain renamed; CR-059 I7's "price of the Snake road" becomes the compact's annuities; §25's rejoinder becomes the Owyhee. The reasons: Pacifica has no volunteer regiments to send (CR-033, APPROVED), prosecutes settler massacres by 1865 (CR-015 H6, APPROVED), is renewing the Protectorship before Hawaii's legislature that spring and asking Oregon for consent before title; a massacre under its flag is the one thing all three forbid. The historical causes (Cache Valley's settlement, the Snake road, the 1862–63 killings, the warrants) are kept; only the flag and the orders change.
**Decision (author, 8 November 2026): amend** — "Let's go with the recommended proposal. Owyhee country and prosecution of the miners is the better 'stain'." Fact changes: the §10 sentence is replaced (no entry in `canon_facts.toml` tracks it; the draft's own protection of the 1863 date is withdrawn below); CR-015 H6's second bullet and CR-059 I7 are revised at integration; the Owyhee hangings are dated 1866 (Fact changes).

### CT6 — Representation of the new members (§10 OPEN)

Shared with CR-059 CT8: Washoe, Deseret and western Montana each need a Council delegation and Assembly seats, and the same 1887 knock-on applies. **Recommendation:** decide once, in CR-059 open decision 18. Fact changes: none.
**Decision (author, 12 November 2026):** amend, with CR-059 CT8: a Council delegation for each new member, equal with the others, and Assembly seats by population.

### CT7 — The Nauvoo Legion's pay and the Black Hawk War (D7, N6; protected intent; added by the set review, 8 November 2026)
**Current:** the protected intent "Pacifica wages no campaign of extermination" (AGENTS.md); CR-059 N5 ("No volunteer companies; force only under confederal command") and this draft's N1 ("no volunteer companies"). D7 as drafted puts the Legion on confederal pay in gold under Deseret's own command, and N6 lets it fight the Black Hawk War of 1865–67 as Deseret's militia. Historically that war included the Circleville killings of Paiute captives in April 1866 (Hist.; to verify).
**Case A, the draft as written:** Pacifica pays a militia that conducts its own Ute and Paiute war, Circleville included. Gold from Monterey then pays for exactly what N1 and CR-059 N5 forbid, and the protected intent is worked round rather than kept.
**Case B, recommended:** confederal pay covers road duty only (escorts, stations, the mail and the telegraph). Any operation against the Utes is under confederal command, with the Native agreements' rules (N1: killings tried in confederal courts with Native testimony), and the Legion takes part only under that command. A Legion company acting on its own account is off confederal pay and answerable in the confederal court, which gives Circleville, if it happens, a prosecution rather than a payroll.
**Recommendation:** B, author to decide. It keeps the protected intent without a special exception and gives N6 a real test of D7. Fact changes: none.
**Decision (author, 12 November 2026):** deferred. Until it is decided, the Legion's pay and the Black Hawk War stay out of the storyline text.
**Decision (author, 15 November 2026):** "I suggest Nauvoo is paid by Pacifica only if Pacifica gets something worth the pay in return (i.e. their deployment has to happen at some decisive moment where it wins something big for Pacifica that it otherwise would not have gotten)." Road duty and the muster against Black Hawk are the Compact's common defence and unpaid; the paid deployment is Bannack in 1864 (M11, approved by the author the same day). Case B's rules hold: no operation against a nation is paid, and a Legion company acting on its own account is answerable in the confederal court.
**Decision (author, 13 November 2026):** "The Legion can be bound to the common defense while a separate treaty and hatchet burial agreement is reached with Black Hawk that prevents the war from getting out of hand." The Compact's clause stands (D5), and the war is stopped by an agreement with Black Hawk (N6). The agreement's date, place and terms in N6 are the drafter's and PROPOSED. ~~**Still open:** the Legion's pay (D7).~~ Decided 15 November 2026 (above).

### CT8 — What "Washoe" covers, and the Salt Lake column's road (D4; CR-015 H2; C-1860-CARSON; added by the set review, 8 November 2026)
**Current:** CR-015 H2 has Pacifica's telegraph and road reach Carson Valley in July–October 1861; the Carson Convention (C-1860-CARSON) recognizes American sovereignty over Washoe in exchange for property guarantees and transit rights. D4 sends the column "by Honey Lake and the Humboldt, north of Union Washoe". Historically Honey Lake was disputed between California and Nevada Territory (the "Sagebrush War" of 1863; Hist.; to verify), and the Humboldt road ran through Nevada Territory's north.
**Route (a), define "Washoe" against Nevada Territory's bounds:** canon's "Washoe" is the district the Carson Convention covered (the Carson, Washoe and Truckee valleys and the Comstock), not the whole of the Territory. The Honey Lake valley is Pacifica's, as California claimed, and the Humboldt road crosses the Territory's unoccupied north far from Carson and Fort Churchill. Nye protests the passage and has no force to stop it. D4 then reads "by Honey Lake and the Humboldt, north of Carson".
**Route (b), by the Carson road with Washoe's consent:** the column marches by the road H2 has already built to Carson Valley, under the Convention's transit rights, which Pacifica reads as covering a garrison bound for an associated state; Nye and Washoe's legislature consent because Washoe lives on California's road (S3). Nye's consent then becomes a scene, and the Union can call it a breach of the Convention.
**Recommendation:** (a), author to decide: it leaves Washoe untouched until 1864, which C2's restraint needs, at the price of defining the word once. Fact changes: none.
**Decision (author, 12 November 2026):** route (a). "Washoe" is the district the Carson Convention covered; the column goes by Honey Lake and the Humboldt, north of Carson.

---

