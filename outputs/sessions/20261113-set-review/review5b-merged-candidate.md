# Review 5b — merged candidate, §§8–13 (fresh context)

**Reviewer:** independent, fresh context, 13 November 2026. Read: `AGENTS.md`; the whole candidate `merged-storyline-8-13.md` (382 lines); current canon for the same sections (`/home/claude/review/canon_sections_8-13.md`); only the `## Canon tensions` sections of CR-059 to CR-065, CR-067 and CR-068. Not read: any other session file, any decision table, git history. Nothing was edited.

**Checks run:** `lint_canon.py --only` on the candidate is clean (1 file). A comparison of `commitments/data/ledger.toml` quotes against the candidate finds eight quotes that canon carries and the candidate no longer does (item D-1).

**Conventions.** `L123` is the line number in the candidate, followed by the first words of the paragraph or sentence. Class: **BLOCKER** (must be fixed before integration), **SHOULD-FIX**, **NOTE**. Kind: *mech* (mechanical, no decision needed) or *author* (needs the author's decision). Departures that a draft's Canon tensions section declares (Deseret 1862/1867, Nevada never admitted, Bear River, the Colorado line, Thomas in the West, Atlanta "untaken", the lapse of May 1865, the writ of 1871, Victoria supporting the controls, London repaid in 1859, and the rest) are treated as proposals and are not reported as regressions.

**Verdict in one line:** needs another pass. §10 is furthest from ready, then §12 and §11; §8, §9 and §13 are ready after mechanical fixes. Details at the end.

---

## A. Chronology and order

### §8

- **A-1. L70 "California's Oregon policy is commerce and nothing else."** SHOULD-FIX, mech. The paragraph follows the Utah War and the Fraser rush (L67, 1857–58) and goes back to 1848–1855. It belongs before L67 or should open with its date.
- **A-2. L72 "In June 1858 it elects Whiteaker … The Senate passes the bill in May."** SHOULD-FIX, mech. June, then May, with no year; the reader takes it for May 1859. Say "had passed the bill in May 1858", or reverse the two sentences. The same May is used again at L74 ("the free states took the Senate's lead only in May") without saying what happened then.
- **A-3. L79 "In 1858 the Carquinez school publishes two results"** and L82–L91 (1855–1864). NOTE, author. After the House vote of February 1859 the text returns to 1855–58 and then runs to 1864. This is canon's order; the new Oregon paragraphs make the jump more visible. Moving L70–L76 to just before L93 (Comstock, 1859) would put the vote in order.
- **A-4. L48 "He supports Victoria's restraint at Washoe in 1860."** NOTE, mech (canon). Used fifty lines before the Washoe crisis is told (L98–L100).
- **A-5. L65 "They marry in November 1858"**. NOTE, mech (canon). "They" follows a paragraph whose last named pair is Victoria and Wyllie.
- **A-6. L76 "When the commercial articles of 1848 come up for renewal, Buchanan's negotiators ask…"** against L72 (the chargé "opens talks to renew" in February 1859) and L102 (the Carson Convention "renews … the commercial articles of 1848, which had run out that year"). NOTE, author. Three statements about one renewal; the reader cannot tell whether the talks of 1859 failed over Sausalito and were then folded into Carson, though the Sausalito storehouse is in the renewal of 1860.

### §9

- **A-7. L128 "The offer of release and investigation is Lincoln's own"**. **BLOCKER**, mech for the move, author for the sequence. The reply asks Washington "to let Oregon's convention meet with both armies withdrawn" and to protect "the inhabitants of the Columbia", and the Council reasons from "the Columbia and the Sound". Oregon's convention and the Enabling Act of 2 March 1861 are first introduced at L138 in §10; the invasion is first told at L134. The Enabling Act predates Sumter and belongs in §8 or at the head of §9. The order of offer, reply, Baker's passports and the fall of Astoria is also unclear: L126 (canon) puts the offer after "a July offensive" and "in exchange for withdrawal"; L128 has Baker ask for his passports and only then "After Astoria falls". Either the offer comes after troops are in Oregon (then say so) or before (then "withdrawal" and "both armies withdrawn" need a referent).
- **A-8. L118 "from July 1862 he is its general in chief"** NOTE, mech. A forward statement that L199 repeats in its place.

### §10 (headed 1861–1862; runs to 1867)

- **A-9. The section as a whole.** **BLOCKER**, author. Order of the paragraphs by date: L134–L136 Columbia 1861; L138 March 1861 to 1862; L140–L144 winter 1861 to summer 1862; L147 October 1861 to "by 1864" and later; L149 winter 1863–64; L151 undated finance; L154 July 1861 to July 1863; L157–L165 winter 1861–62 to November 1862; L168 December 1862; L170–L174 January to spring 1863; L176 1863 to spring 1864; L179 January 1863; L181 winter 1865–66; L183 April 1865; L186 January 1863 to 1865; L188 1863 to winter 1866–67; L190 December 1865 to summer 1866. Canon already carried the Southwest to 1866 here, but in three short paragraphs; at this length the reader cannot hold the calendar. The author should decide between sub-heads by theatre inside §10 (the Columbia; the Basin and Deseret; the Rio Grande; the nations) and moving everything after mid-1863 into §11 and §12.
- **A-10. L138 "The Oregon Enabling Act of 2 March 1861"**. SHOULD-FIX, mech. Goes back to before Sumter after two paragraphs on the campaign (see A-7). Within the paragraph "subject to the compact's court" precedes the sentence that makes Deady that court.
- **A-11. L147 "In October 1861, with Portland fallen"**. SHOULD-FIX, mech. Follows the turret ship's action of summer 1862 (L142–L144) and goes back nine months; it then runs on to the Walla Walla convention of July 1862, Idaho Territory (1863), "by 1864" and a successor governor's accounts. Break at "Lewiston stands". "Mullan resigns his commission in the spring" has no year.
- **A-12. L149 "In the winter of 1863–1864 Washington calls Oregon's displaced Unionists"**. SHOULD-FIX, mech. Placed between 1862 material and the Deseret paragraph that begins in July 1861. It belongs with Washoe 1864 and the Terms of Monterey.
- **A-13. L151 "The second undertaking sustains the gains"**. NOTE, mech (canon). The "three connected undertakings" were announced at L35, more than a hundred lines and a war earlier.
- **A-14. L154 "Southwestern and interior expansion follows"**. SHOULD-FIX, mech. One paragraph from July 1861 to the peace. The signing of 24 July 1863 is told ("he and Young sign the Compact"), then the Compact's terms, then "and Young signs" again, then Lee, then "He gives up one man, at the signing", then back to the spring of 1863 ("Lincoln's governor had left by Fort Bridger in the spring of 1863"). Needs three paragraphs: 1861–62, the articles of December 1862, the Compact.
- **A-15. L168 "In December 1862, on his way to Texas, Elias rides up from Santa Fe to Taos"**. SHOULD-FIX, mech. First appearance of Elias in New Mexico; the text never says that he left Monterey or arrived. "on his way to Texas" uses a journey first introduced at L205 (§11). "The amnesty becomes an article of the Rio Grande compact" uses a compact first introduced at L186.
- **A-16. L176 "Idaho's mining districts turn toward the Northwest in 1863"**. **BLOCKER**, mech. One paragraph holds Montana 1863–64 and Washoe 1863–64 and tells Washoe out of order: retaking (spring 1864), then "Through 1863", then August 1863, January 1864, March 1864, September 1863 ("the Council adopted it in September"), then the retaking again. It also uses the Terms of Monterey ("In August 1863 Pacifica prints that it asks no state of the Union…") before they are introduced at L213. Break at "Pacifica retakes Washoe" and tell it once in order. See also B-8 and D-1.
- **A-17. L179 "In January 1863 the road's commander marches"**; **L181 "The Owyhee country"** (1865–66); **L183 "In April 1865"**; **L186 "In January 1863"**. SHOULD-FIX, mech. From spring 1864 back to January 1863, forward to 1866, back to 1865, back to January 1863. L181 and L183 are later than the armistice told in §12.
- **A-18. L186 "signs when the Sunset articles are read in the plaza"** and **L188 "the Sunset road's customs"**. SHOULD-FIX, mech. Neither "Sunset articles" nor "Sunset road" is defined anywhere in the candidate. From CR-068 CT24 they are the San Antonio terms of February 1863 (L172) and the southern road; L172 must name them.
- **A-19. L186 "In Navajo country the government chooses a different course."** SHOULD-FIX, author. See D-6.
- **A-20. L190 "the cabinet promulgates it … January 1866"; "cross the armistice line"**. NOTE, mech. The armistice and the cabinet of the Enabling Law are first told in §12.

### §11

- **A-21. L201 "Pacifica's credit to Richmond, lent on the terms printed in Texas"**. SHOULD-FIX, mech. The printing in Texas is told at L207 (February 1863). "Farragut will not take his ships into a bay…" refers to Mobile Bay one sentence before Mobile is named.
- **A-22. L203 "He meets Logan in a New Orleans repair yard"**. SHOULD-FIX, mech. The CR-067 sentence inserted before it ends "answer to the Protector through him", so "He" now reads as the acting chief or the Protector. Write "Marcus meets Logan".
- **A-23. L207 "In the spring of 1862 Elias proposes a general armistice"**. **BLOCKER**, mech for the split, author for the cuts. The paragraph follows Vicksburg preparations and the Texas scene of early 1863 (L203–L205) and goes back to spring 1862. It then holds eight events to May 1863 and ends "In the spring Pacifica's government prints its terms of passage", after May. The armistice offer and the widened credit belong before L201's Matamoros sentence, which depends on them. See H.
- **A-24. L209 "Steele's corps bridging the river"**. NOTE, mech. Steele is introduced at L216.
- **A-25. L216 "In Monterey, Sherman drills the Republic's reserves. Frederick Steele … in December 1862"**. SHOULD-FIX, mech. After the Terms of Monterey and *Two Houses* (to early 1864) the text returns to December 1862, runs to March 1864, and ends with "The raid on Meridian he planned for February", before March.
- **A-26. L226 "On 15 May 1862 Rodgers takes Galena"**. SHOULD-FIX, mech. Two years back, between Marcus's return in 1864 and the Atlanta campaign. It belongs after L194 (Virginia destroyed on 11 May 1862).
- **A-27. L229 → L231 → L234 → L236 → L238.** SHOULD-FIX, author. Atlanta from May to December 1864; back to Mobile in summer 1864; back to July–October in the Valley; forward to December–February; then L238 "In the East the armies fight from the Peninsula to the Wilderness", which reaches back to 1862. L229 uses "On election day", "the ships go to Mobile" and "the coming armistice" before the election (L271), the Mobile decision (L236) and McClellan's programme (L275) are told. L236 has "Lincoln, beaten at the polls".
- **A-28. L236 "re-embarks the Dauphin Island troops … The order to ignore mines"**. SHOULD-FIX, mech. No landing on Dauphin Island and no such order have been told. "Logan's denser mine field" and "the new row's torpedoes" likewise.
- **A-29. L240–L248** (Victoria 1863, indium 1863, Peirce 1863). NOTE, author. Canon's order; it now follows February 1865.

### §12

- **A-30. L264 "In the 1864–1865 consolidation struggle"**. **BLOCKER**, mech for the move, author to confirm. This paragraph tells Lincoln's offer of spring 1864, the blind vote of November 1864, the arrival of the news of Lincoln's defeat, the dissolution, the winter election and the stand-down of March 1865 "when McClellan's inaugural shows that he will treat". The Union's summer and election are told afterwards (L269 "By August", L271, L273, L275). L266 (canon) then announces "Lincoln loses the election of 1864" before L269–L271 narrate it. The blind vote depends on the reader not yet knowing more than the Council does; it should follow L271 or L273. Inside the paragraph "After Lincoln's refusal in February" follows the offer of "spring 1864".
- **A-31. L271 "In September the State Department publishes"**. NOTE, mech. Placed after 11 October.
- **A-32. L273 "In December Lincoln asks … in January the amendment fails … In December he names Chase … On 3 February … east of Atlanta in November … His annual message of December 1864"**. SHOULD-FIX, mech. December, January, December, February, November, December. Also "which McClellan will grant within two months, and the conference fails over separation. His last operations fail": "His" reads as McClellan's.
- **A-33. L284 "He reads his pledge of 1864 against himself"**. SHOULD-FIX, mech. At L264 the end of the renewals is "Hawaii's condition" on its seven votes; Elias's own pledge there is to resign if he falls short. Say "the condition he accepted in 1864".
- **A-34. L286 "Marcus seeks defensible gains"**. NOTE, mech. Canon paragraph now standing between the lapse (L284) and the bargain (L288), which read as one movement.
- **A-35. L288 "the two members of the mission party"**. NOTE, mech. Not introduced in §§8–13.
- **A-36. L298 "The Western line is agreed in the 1865 peace"**. SHOULD-FIX, mech. The line's content (L298, L301) is told before the treaty is signed (L304). L304 should come first.
- **A-37. L307 "Lincoln, a private citizen at Springfield"**. NOTE, mech. His going home is told at L324.
- **A-38. L307 "the exclusion article … the Native article's rule on testimony … The Chinese floor … Nesmith … the returns commission"**. SHOULD-FIX, mech. Five things used and never introduced. The reader is told that the Chinese floor and the Native article "nearly cost him the south" without being told what either is.
- **A-39. L307 "Pacifica's Articles leave residence to the member states, as Hawaii demanded in 1856"**. SHOULD-FIX, mech. L54 does not say this. CR-059 CT4 was decided "amend" (residence, land tenure and the franchise named as member powers); the amendment is not in the candidate's §8.
- **A-40. L317 "They are too late."** NOTE, mech. A good break, but L317 and L319 start without a label (F-3).

### §13

- **A-41. L351, last sentence: "Free navigation of the Mississippi is Pacifica's condition for guaranteeing the treaty of the spring of 1871."** **BLOCKER**, mech. It is appended to the paragraph about the Treaty of Washington and the Stikine grant, where "the treaty of the spring of 1871" reads as Britain's treaty. It belongs in L345 beside "Richmond restores free Mississippi navigation; Pacifica guarantees Confederate independence."
- **A-42. L353, last two sentences: "Lincoln dies at Springfield in November 1872."** SHOULD-FIX, mech. Appended after the railway strike of 1877. Put it after "Greeley defeats Grant in 1872, then dies before the electors meet" or with L357.
- **A-43. L341 "The same convention ends the scalp bounties"**. NOTE, mech. No convention has been named in the paragraph, only "a customs post agreed with Mexico".

---

## B. Repetition (which telling should stay)

| # | Event | Told at | Keep |
|---|---|---|---|
| B-1 | Lincoln's offer of 1861 and Elias's reply | L126 "Washington eventually offers…"; L128 "The offer of release…" | L128. Cut L126 from "Washington eventually offers" to the end. SHOULD-FIX, mech (CR-068 CT13 decided "amend") |
| B-2 | The War Department's order to the posts east of the Cascades, October 1861 | L147 "In October 1861…"; L154 "that October the posts east of the Cascades…" | L147; L154 a clause. SHOULD-FIX, mech |
| B-3 | The Iowa regiments | L140 "Candidate changed assignments are the 11th and 13th Iowa"; L147 "sends its Iowa regiments to Casey"; L199 "Four Iowa regiments raised that autumn" | One statement, at L147. SHOULD-FIX, author (L140 still calls it open) |
| B-4 | Whiteaker | L138 "They choose Whiteaker…"; next sentence "John Whiteaker negotiates…" | Merge; first name at first mention. NOTE, mech |
| B-5 | Compact of Association signed | L154 "he and Young sign the Compact"; "…and Young signs" | Once, after the terms. SHOULD-FIX, mech |
| B-6 | John D. Lee | L154 "Brigham Young surrenders John D. Lee in 1863"; "He gives up one man, at the signing" | Merge into one sentence. SHOULD-FIX, mech |
| B-7 | Fort Garland | L174 "take Fort Garland's herd … a written convention"; "Fort Garland falls … in 1863 without an assault: in May its Colorado garrison goes home" | The second, shortened; "in 1863 … in May" is one date twice. NOTE, mech |
| B-8 | Washoe's failed constitution and the second convention | L176 "after a winter in which its own convention's constitution failed and a spring in which Congress called a second"; later "In January 1864 Washoe's voters reject… In March Congress passes" | The dated telling. BLOCKER with A-16, mech |
| B-9 | Terms of Monterey and the Council's adoption | L176 "In August 1863 Pacifica prints…"; "the Council adopted it in September"; L213 | L213. L176 a back-reference once §10 and §11 are in order. SHOULD-FIX, mech |
| B-10 | Victoria's conditions on the third renewal | L176 "Victoria writes Hawaii's conditions…"; L264 "Victoria uses it to win her conditions for the third renewal" | One, at L176 with the Washoe conditions, and L264 gives only her means (Lincoln's offer). SHOULD-FIX, mech |
| B-11 | Pablo de la Guerra introduced | L186 "his commissioner, Pablo de la Guerra"; "Elias's commissioner, Pablo de la Guerra" | First. NOTE, mech |
| B-12 | Navajo treaty of 1865 | L186 "in 1865 a treaty recognizes a homeland and avoids the Long Walk"; L188 "the Navajo homeland treaty of 1865… No Navajo walks to the Pecos" | L188. NOTE, author (CR-061 CT3 kept the split deliberately) |
| B-13 | Abolition of peonage | L190 "Pacifica abolishes New Mexico's debt peonage … by 1866, facing a short Hispano revolt"; then the ordinance and the revolt in full | The full telling; the canon sentence is its summary. NOTE, mech |
| B-14 | Scalp bounties | L188 "followed by a Mexican convention ending scalp bounties"; "The end of the bounties is the price Mangas asks"; L341 "The same convention ends the scalp bounties" | L188 for the price, L341 for the instrument. NOTE, mech |
| B-15 | Pensacola | L201 "The Union occupies the evacuated Pensacola navy yard in May 1862"; "has already emptied Pensacola"; "A brigade stays to hold Pensacola"; "The Union keeps a squadron and a garrison at Pensacola" | Two of the four. SHOULD-FIX, mech |
| B-16 | Sherman refuses the Southern assignment | L203; L207 "Elias keeps Sherman as Inspector-General after Sherman refuses" | L203, with the keeping added there. NOTE, mech |
| B-17 | Elias's journey to Texas | L168 "on his way to Texas"; L186 "on the road to Texas with Elias"; "after he leaves for Texas"; L205 "Early in 1863 Elias goes to Texas"; L207 "In Texas, in February 1863" | L205 as the telling; see H-1. SHOULD-FIX, author |
| B-18 | San Antonio, February 1863 | L172 (convention); L205 ("to settle the Arizona renunciation and the Matamoros supply terms"); L207 (credit terms printed) | One paragraph. SHOULD-FIX, author |
| B-19 | "the South is not conquered and the Pacific taken next" | L128 (seventh reason); L207 (Honolulu) | Both may stay if the second is marked as his own words repeated. NOTE, author |
| B-20 | Johnston driven from Jackson, July 1863; the escaped men | L211 "Grant drives Johnston out of Jackson"; L216 "McPherson drives Johnston's relief army, stronger by the men who escaped the city, out of Jackson in July" | L211 with McPherson's name. SHOULD-FIX, mech |
| B-21 | Early before Washington | L234; L238 "in July 1864 Early's raid reaches Fort Stevens"; L269 "Early at the gates of Washington" | L234. Cut L238's sentence. SHOULD-FIX, mech |
| B-22 | Overland losses | L238 "more than sixty thousand men in six weeks"; L269 "sixty thousand casualties in six weeks" | L269. SHOULD-FIX, mech |
| B-23 | Atlanta untaken | L229 "On election day Atlanta is untaken"; L269 "Atlanta does not fall"; L271 "in contact with Johnston before Atlanta" | L229 and one clause in §12. NOTE, mech |
| B-24 | McPherson's death; Mobile and Petersburg in February | L229; L236–L238; L273 "His last operations fail: east of Atlanta in November, where McPherson is killed, and in February at Petersburg and at Mobile" | L229 and L236; L273 a clause without the detail. SHOULD-FIX, mech |
| B-25 | Lincoln's defeat | L236; L264; L266; L271 | L271. Cut L266's sentence. BLOCKER with A-30 |
| B-26 | McClellan takes office, March 1865 | L264; L275 "takes the oath on 4 March 1865"; L275 "After taking office in March 1865" | First sentence of L275. SHOULD-FIX, mech |
| B-27 | Pacifica's armistice | L275 "signs executive armistice conventions … during March–June"; L278 "signed in mid-May 1865"; L284 "is signed in May 1865" | L278. SHOULD-FIX, mech |
| B-28 | Treaty of Amity and Commerce | L278 "in the last week of May he signs the Treaty of Amity and Commerce"; L282 "A Pacifica–Confederate Treaty of Amity and Commerce in spring 1865" | L278; L282 keeps only the recognition by Britain, France and McClellan. SHOULD-FIX, mech |
| B-29 | The Enabling Law | L284 (heads laid in July); L288 (bargain, votes, ratification, in force 1 December); L290 "In 1865 Elias secures the Enabling Law"; L292 "The guarantees become protected provisions" | L288; L290 reduced to what the office is. SHOULD-FIX, mech |
| B-30 | Treaty of December 1865 and "the full powers of the office the Enabling Law created" | L288; L304; L307 | L304. SHOULD-FIX, mech |
| B-31 | The line in Montana and Colorado | L298; L301 | L301 (see C-1). BLOCKER |
| B-32 | Evacuation of Port Townsend | L304; L312 "The surviving Puget Sound enclave is evacuated under the treaty"; L319 "Port Townsend's garrison sails" | L304 (term) and L319 (act). SHOULD-FIX, mech |
| B-33 | Fort Union's evacuation | L304; L322 "the Fort Union garrison marches out … and Fort Union is evacuated in 1867" | L322, one clause. NOTE, mech (the merge notes say it is told once; inside L322 it is told twice) |
| B-34 | Oregon's choice recorded | L307 last sentence; L315 first sentence | L315. NOTE, mech |
| B-35 | Vendor credit | L312 "$40 million … through 1872"; L315 "a payment spread over six years"; L319 | L312. NOTE, mech |
| B-36 | Lincoln's letters of 1866 and 1867 | L307; L319; L324 "are told above" | L307 and L319; cut the pointer (E-1). BLOCKER, mech |
| B-37 | Free navigation and the guarantee of 1871 | L345; L351 | L345 (A-41). BLOCKER, mech |
| B-38 | Halleck as general in chief | L118; L199 | L199. NOTE, mech |

---

## C. Contradictions inside the candidate

### 1861

- **C-1. L128 "the first armoured ship completed is stationed at Honolulu"** against **L142 "The first operational Ericsson turret ship helps secure the lower Columbia"**. SHOULD-FIX, author. L106 also says Pacifica already has "some armored warships" at Sumter. One of the three needs a qualifier.
- **C-2. Offer, reply and invasion** (A-7). L126 "in exchange for withdrawal" and L128 "both armies withdrawn" suppose Pacifican troops in Oregon; L128's "After Astoria falls" puts the fall after Baker has asked for his passports. SHOULD-FIX, author.
- **C-3. L126 "Elias demands broader strategic guarantees and protection for collaborators"** against **L128**, whose three demands are the renunciation of search, amnesty and habeas corpus for the Columbia's inhabitants, and Oregon's convention. SHOULD-FIX, mech (cut L126's version).
- **C-4. L136 "Union troops preserve a northern anchorage and interior concentration, giving later reinforcements somewhere to arrive"** against **L147**, where the interior posts are ordered out in October 1861 and the reinforcements go to the Sound. NOTE, mech (CR-059 CT3 adapts: the concentration is Fort Walla Walla and ends in July 1862; the sentence should say so).
- **C-5. L140 "[OPEN] These are planned allocations, not audited strengths or sailing schedules"** against **L147** and **L199 "Four Iowa regiments raised that autumn are on the Panama road to the Sound"** (5 April 1862). SHOULD-FIX, author. A fact in two places and an open question in a third. L199 also has them still on the road six months after the order of October 1861; "that autumn" has no year.
- **C-6. State of war.** L128 (Congress recognizes it before 6 August) is consistent with L120, L298 ("ended by the war") and L304. No finding.
- **C-7. Port Townsend.** L136, L149, L213, L264, L271, L304, L319 agree. L157 calls the enclave "besieged"; L140 says it "ties down Pacifican troops". NOTE.

### 1862–63: Elias's journey

- **C-8. The calendar holds:** Santa Fe and Taos in December (L154, L168, L186), on the road in January (L186), San Antonio in February (L172, L207), Monterey late in April (L207), Honolulu in May (L207), Salt Lake on 24 July (L154), Box Elder afterwards (L179), the Terms in August (L213). It matches CR-068 CT24. Two gaps: L172 never says that Elias is at San Antonio or who signs for Pacifica, and nothing says how he reached Santa Fe. SHOULD-FIX, mech.
- **C-9. L154 "The articles … promise nothing against the Union's law"** against **"Lincoln's governor had left by Fort Bridger in the spring of 1863, under the articles"**. NOTE, author. If the articles do nothing against the Union's law, the governor does not leave "under" them.
- **C-10. L154 "Fort Churchill's regulars go by the Salt Lake road the next summer"** and **L176 "Nye's volunteers at Fort Churchill"**. Consistent, but the change of garrison is never stated. NOTE, mech.
- **C-11. L207 "its undertaking to end peonage in New Mexico"** in a paper published in reply to a letter of January 1863; the compact that carries the clause is signed "In the spring" (L186). NOTE, mech (CR-068 CT15 says "declared purpose"; use that).
- **C-12. L172 "a fugitive who crosses from Texas is not sent back"** (APPROVED, CR-061, February 1863) against **L357 "Pacifica enforces a fugitive agreement with Richmond from 1871–1872"**, under which "a fugitive held for return" exists by autumn 1871. SHOULD-FIX, author. The reversal is nowhere acknowledged, and Lincoln's opinion (L357) rests the case on the terms of passage of 1863, which L207 says were printed "for men leaving the Union's draft", and not on the San Antonio article, which is the instrument in point. Either the association treaties of 1871–72 expressly end the San Antonio article, or counsel cite it.
- **C-13. L207 "the Republic makes no condition about slavery"** against L172's free-soil articles. Not a contradiction (a loan's conditions; a road's law), but the two sit 35 lines apart with no link. NOTE.

### Deseret, Washoe

- **C-14. Deseret.** Articles of December 1862, Compact of 24 July 1863, vote of December 1866, membership on the exchange of 1867 (L154, L310) agree with each other and with L176 and L179. No finding beyond C-9.
- **C-15. L176 "Pacifica retakes Washoe … after a winter in which its own convention's constitution failed"**. SHOULD-FIX, mech. "its own" attaches to Pacifica; it is Washoe's convention.
- **C-16. L176 conditions of the third renewal** (no annexation, Carson's guarantees, entry at Hawaii's ports; Washoe's own choice refused) against **L310 "Washoe elects a convention in 1866 that approves its charter of accession"**. Consistent. "Carson's guarantees" in a section full of Kit Carson should read "the Carson Convention's". NOTE, mech.
- **C-17. L298 "American owners in Nevada"**. NOTE, mech. Everywhere else the candidate says Washoe, and there is no State of Nevada.

### The Union's war, 1862–65

- **C-18. L236 "where Polk's army stands while Johnston holds the Chattahoochee"** (December 1864) against **L229 "He reaches the Chattahoochee in September and turns Johnston out of his lines north of the river … The army winters in its lines from Decatur to the river"**. SHOULD-FIX, mech. By December Thomas is across the river and east of Atlanta. L269 "Johnston still stands in front of Atlanta" in August is loose for the same reason: L229 has him on the Allatoona heights in July.
- **C-19. Thomas and McPherson.** L216, L229, L271 and L273 agree: Thomas from March 1864, McPherson from 10 November, killed on 22 November, Thomas again. No finding.
- **C-20. L196 "until the autumn every one is needed at Charleston or on the James"** and **L236 "*New Ironsides* comes down from Charleston"** against **L226 "[OPEN] Whether the Charleston and Wassaw operations occur"**. NOTE, author.
- **C-21. Mobile.** L201 ("no Union army comes to the Gulf for two and a half years", from July 1862), L231 and L236 (January–February 1865) agree. See A-28.
- **C-22. The election.** New York 33, Pennsylvania 26, New Jersey 7, Indiana 13, Illinois 16, Connecticut 6, New Hampshire 5, Delaware 3, Kentucky 11 make 120; 223 electors without the Pacific coast leave 103. Consistent with L271 and CR-065 CT4.
- **C-23. L264 "on terms it printed two years ago"** (winter 1864–65) against **L213** (August 1863) and **L269 "printed a year ago"** (September 1864). SHOULD-FIX, mech. It is about a year and a half.
- **C-24. L264 "After Lincoln's refusal in February he makes no statement"** against the two sentences before it, in which he answers Lincoln's spring offer by reminding the merchants and by the sugar contract. NOTE, author.

### The blind vote, 1865

- **C-25. The Council.** Eighteen members; twelve to six in November 1864 (five of California's nine, seven of Hawaii's); thirteen to five in 1865 with Hawaii seven to two. Consistent.
- **C-26. L275 "during March–June"** against **L278 "signed in mid-May 1865, some weeks after Richmond's … by Elias as Protector"** and **L284** (the office expires on 31 May). SHOULD-FIX, mech. No Pacifican armistice can be signed in June by the Protector.
- **C-27. L278 "Pacifica's war advances to Richmond end with the armistice, as it printed in 1863"** against **L207**, where the condition is published in spring 1862 and the credit's terms are printed in February 1863. NOTE, mech.
- **C-28. L213 "Its recognition of the government at Richmond … waits on no armistice"** against L278 and L282, where formal recognition comes by a treaty signed a fortnight after the armistice. NOTE, author. Not false, but the reader will ask why it waited.
- **C-29. L278 the armistice's public term (no military mission, no arms)** followed in the same sentence by the Treaty of Amity, and **L282 "Wartime alliance clauses … remain [OPEN]"**. SHOULD-FIX, mech. CR-062 CT3 was decided: replace L282's sentence with "The treaty carries no military clause; its exact drafting remains [OPEN]." Not applied.
- **C-30. L288 "the list of provisions the cabinet may not legislate around"** against **L290 "The cabinet may legislate around specified provisions, but the Hawaiian crown, Kuhina Nui and local institutions are protected."** SHOULD-FIX, mech. Two descriptions of one instrument that read as opposites.

### The treaty, Oregon, Alaska, the Senate

- **C-31. L298 "Colorado's Western Slope, North and Middle Park and the San Luis Valley are Pacifican; Denver, the Front Range, Pikes Peak and Leadville stay Union"** against **L301 "the Western Slope, the parks, South Park and the upper Arkansas are Pacifican"**. **BLOCKER**, mech. Leadville is on the upper Arkansas; South Park is in one list and not the other. CR-060's Canon tensions section declares the amendment of the Colorado segment, so canon's sentence must be cut or rewritten; it also names Leadville twelve years before the place exists.
- **C-32. L310 "The Western Slope has no settlers to vote … reserves the Slope and the Parks as a Ute homeland"** against **L301 "The Colorado article lets any mountain mining district vote itself over"** with the parks and South Park Pacifican. NOTE, author. Mining districts inside a homeland "whose ground the Republic may lease only for the Utes".
- **C-33. L319 "the Treasury's statement of what Pacifica will pay for the West and for Alaska"**. SHOULD-FIX, author. Pacifica pays Russia for Alaska (L317); the Union's Treasury has nothing to state about it.
- **C-34. L319 "the charters of Washington Territory …"**. NOTE, mech. No charter for Washington Territory is told; L138 has only "The Puget Sound counties sign a parallel compact".
- **C-35. L312 "offers a separate Treasury loan"** and **L319**, where Lincoln advises the Senate "to take the purchase money and refuse the separate loan". SHOULD-FIX, author. What the Senate does with the loan is not told, and L312 goes on "Elias … becomes creditor to the United States".
- **C-36. L307 "In July the Treasury publishes the customs houses a Union Oregon would face."** NOTE, mech. Whose Treasury.
- **C-37. L317 "Elias refused even an American guarantee, because a guarantor has a right to come in"** and **L319 "because a creditor, like a guarantor, has a right to come in"**. NOTE, author. Lincoln quotes a phrase that the candidate presents as a private assurance to Gorchakov; if it has been public since 1848, say so once.
- **C-38. Dates.** Treaty in the third week of December 1865; Oregon's vote October 1866; Deseret December 1866; the Tsar's meeting 16 December 1866 (old style); St Petersburg early March 1867; consent 9 April; exchange in the summer. Consistent across L288, L304, L307, L310, L315–L322.

### After 1867

- **C-39. Lincoln.** L307 (1866), L319 (1867), L324 (1869), L357 (opinion, autumn 1871), L353 (dies November 1872) agree.
- **C-40. L357 "the override his ministers have prepared under the enabling law, to which Sherman had objected"**. NOTE, mech. What Sherman objected to, and when, is not told; the clause is the remnant of canon's sentence.
- **C-41. L341 "rifles for the Republic's army"**. NOTE, mech. Here "the Republic" is Mexico. Throughout the CR-068 passages "the Republic" is the Confederation after 1856 (L128, L207, L213, L284, L324, L357), while L54 keeps California as a republic inside it. The author should settle one name for the common state between 1856 and 1887.

---

## D. Leftover canon now false or redundant; stale OPEN and PROPOSED markers

- **D-1. Ledger quotes.** SHOULD-FIX, mech; one is a BLOCKER. Eight sentences that `commitments/data/ledger.toml` quotes are gone: the bondholders' warning of 1860; "Washoe is retaken in 1863–1864."; the two Deseret accession sentences; the Matamoros supply sentence; "In Navajo country the government chooses a different course: a treaty recognizes a homeland and avoids the Long Walk."; "Lot supports the bargain…"; the travel-paper sentence. Seven follow from decided tensions and need the ledger changed at integration. **The Washoe sentence is a BLOCKER:** CR-060 CT4 was decided "adapt … the sentence is kept verbatim, since the ledger quotes it", and the merge rewrote it as "Pacifica retakes Washoe in the spring of 1864" (L176).
- **D-2. L126**, from "Washington eventually offers" to the end. Superseded by L128 (B-1, C-3).
- **D-3. L130 "in the proposed office of Inspector-General"** against L207 "Elias keeps Sherman as Inspector-General" (APPROVED). SHOULD-FIX, mech.
- **D-4. L138 "[OPEN] Local officeholders, succession, compacts, boundaries and accession dates."** SHOULD-FIX, mech. The same paragraph now names Whiteaker and Deady and describes the compacts; L307 dates the accession.
- **D-5. L140 "Candidate changed assignments are…"** See C-5.
- **D-6. L186 "[APPROVED — CR-015] In Navajo country the government chooses a different course."** SHOULD-FIX, author. In canon the sentence answered "Bear River becomes a Pacifican atrocity". CR-061 CT3 kept it verbatim; CR-060 CT5 then removed the atrocity. It now follows the Pueblos' agreement and is different from nothing.
- **D-7. L176 "[OPEN] Exact forces, routes and accession instruments"**. NOTE, mech. L310 gives the instruments.
- **D-8. L190 "[PROPOSED] Religious toleration and civic protection demand actions that cost the new state support among its own settlers."** NOTE, author. No "new state" is in view at the end of the New Mexico paragraph.
- **D-9. L201 "suffers an initial failure"** with "No further Union attempt on New Orleans occurs before 1870"; **"[OPEN] Exact obstruction, ship placement…"** beside the dated barrier of 11 April. NOTE, mech.
- **D-10. L226 "The consequences of the altered armored fleet continue along the Atlantic and Gulf coasts."** NOTE, mech. A topic sentence for canon's paragraph, now followed by a single action of May 1862.
- **D-11. L238 "In the East the armies fight from the Peninsula to the Wilderness."** SHOULD-FIX, mech. A summary of three years in the middle of February 1865, and the two sentences after it repeat L234 and L269.
- **D-12. L240 "His principle of broad civic incorporation increasingly coexists with ruthless military punishment."** NOTE, author. With Bear River no longer a Pacifican atrocity, the candidate shows no such punishment between 1861 and 1865 except Lee's hanging.
- **D-13. L264 "[OPEN] Exact dissolution and election dates…"** beside the dated vote and the announced dissolution. NOTE, mech.
- **D-14. L266 "The war's political decision comes when Lincoln loses the election of 1864."** SHOULD-FIX, mech (A-30).
- **D-15. L275 "Sherman's brother John in the Senate provides a possible negotiating channel."** SHOULD-FIX, mech. William Sherman signs the treaty (L304) and John votes on it (L319); nothing is "possible" any longer.
- **D-16. L282** (C-29); **L290, L292** (B-29, C-30).
- **D-17. L298**: the Colorado sentence (C-31); **"surveys remain [PROPOSED]"** beside L319 "the surveyors take the field".
- **D-18. L312 "[PROPOSED] The surviving Puget Sound enclave is evacuated under the treaty"** and **"The price, payment schedule and loan capacity require financial testing"** beside L319, where the first instalment lies counted in the Subtreasury. SHOULD-FIX, mech.
- **D-19. L122 "Naval purchases and equipment still depend on foreign credit"** and **L326 "foreign credit and diplomacy"**. NOTE, mech. CR-068 CT26 lists both for a word on whose credit, after L39's repayment of London in 1859. Not applied.
- **D-20. L124 "[OPEN] … late May is the working activation date"** against L207 ("in the last week of the term") and L284 ("on the last day of that month the Protectorship expires"). NOTE, author. The new text treats the date as fixed.
- **D-21. L172 "[PROPOSED] Richmond renounces its Arizona claim"** against L205 "[APPROVED — CR-022] … to settle the Arizona renunciation". NOTE, author (kept by CR-061 CT5; the label conflict remains).
- **D-22. L54** lacks the member powers that CR-059 CT4 added (A-39).

---

## E. Memo language

New material (to fix before integration):

- **E-1. L324 "His letters to Oregon in 1866 and to the Senate in 1867 are told above."** **BLOCKER**, mech. An editor's pointer.
- **E-2. L3 "Status: CANDIDATE…"** and **L360–L382 "Notes on the merge"**. **BLOCKER**, mech. Not storyline; they must not travel with the text.
- **E-3. L181 "The Owyhee country is where the friendship doctrine fails before it holds."** SHOULD-FIX, mech. "The friendship doctrine" is a planning term that §§8–13 never introduce; the sentence is an argument about the story.
- **E-4. L154 "The regiments that might have come back to Utah were to be raised in California."** SHOULD-FIX, mech. An explanation from real history.
- **E-5. L234 "The Gulf has no corps to send north, because the Union never took New Orleans."** and **L201 "Without a Union New Orleans base there is no Red River campaign in 1864."** SHOULD-FIX, mech. The second names a campaign that does not happen.
- **E-6. L186 "the campaign the Union would have made"; "avoids the Long Walk"**. NOTE, mech.
- **E-7. L76 "Hughes of Indiana and Stephens make the right argument"; L72 "Elias could have held the note for a month and did not."** NOTE, author. The narrator judges; the second also leaves Elias's motive unstated at the hinge of the Oregon story.
- **E-8. L216 "Grant has the strategy and no one in the West to carry it out."** and **L273 "He leaves his successor not a ruin but a choice made plain: separation, or more war."** NOTE, author. Theses, the second in a "not X but Y" turn.
- **E-9. L264 "It is the argument of continuity that the Union has just refused its president."** NOTE, author.

Canon's own memo language, now sitting beside the denser prose (NOTE, author, outside these nine drafts): "on the working calendar/timetable/chronology" (L31, L33, L124, L126, L134, L142); L106 "recorded as scenario estimates in the historical and planning files rather than asserted here"; L122 "is a planning estimate"; L140; L142 "requires a capacity audit"; L151 "must not be silently placed in the early war"; L194 "is the working additional outcome"; L196 "the historical Monitor"; L201 "its historical breakthrough", "form the working mechanism", "by assertion"; L226 "the historical failures do not become additional Confederate victories merely because"; L231 "the historical August 1864 attack is delayed"; L238 "rather than a Pacifican field army overrunning the East"; L255 "The historical Lot"; L257 "in our history"; L282 "within this selected postwar structure"; L338, L355 "await audit"; and the character notes at L222–L224 and L328.

---

## F. Labels

- **F-1. Two labels in one sentence.** L211 "…its guns and **[MODEL]** about fifteen thousand men, whom Grant paroles; **[PROPOSED — CR-063]** much of the mobile Confederate army survives." L188 "…brings his son-in-law Cochise to the table, and **[PROPOSED]** an Apache peace in 1865…" (an APPROVED CR-061 sentence that turns PROPOSED at its comma). SHOULD-FIX, mech.
- **F-2. Label repeated with no change.** L157 and L159; L186 (PROPOSED CR-061 twice running); L201 (CR-063 three times); L236 (CR-063 four times); L273 (CR-065 twice, adjacent). NOTE, mech.
- **F-3. Paragraphs of new material with no label at their head.** L72, L74, L76 (CR-059); L211 (CR-063); L317, L319 (CR-062). Unlabelled text in this document reads as settled canon. SHOULD-FIX, mech.
- **F-4. Material under another CR's label.** L307: Lincoln's Oregon letter and Elias's answer (CR-068) inside [PROPOSED — CR-059]. L319: Lincoln's letter to the Senate (CR-068) inside CR-062's paragraph. L273: the attack of 22 November (CR-064) and the annual message (CR-068) under [PROPOSED — CR-065]. L176: Hawaii's control of entry (CR-068 CT8) under [PROPOSED — CR-060]. L264: canon's "Elias uses the dissolution provision…" under [APPROVED — CR-068] and canon's "He campaigns on security…" under [PROPOSED — CR-065]. L324 then calls the two letters APPROVED. SHOULD-FIX, author.
- **F-5. APPROVED sentences that rest on PROPOSED ones beside them.** SHOULD-FIX, author.
  - L128 [APPROVED — CR-068]: "Oregon's convention" and the Columbia rest on L138 [PROPOSED — CR-059].
  - L149 [APPROVED — CR-068]: the delegates of 1861 rest on L138.
  - L186 [APPROVED — CR-061] "The Pueblos make their own agreement" and the Cubero signing "with Elias's commissioner, Pablo de la Guerra" rest on the PROPOSED compact and on a commissioner introduced in a PROPOSED sentence.
  - L190 [APPROVED — CR-061] "The captive article brings the compact's unwilling clause forward" and "the Taos article has settled its account with 1847" rest on L186 [PROPOSED — CR-061] and L168 [PROPOSED — CR-066].
  - L207 [APPROVED — CR-068]: the order against slaving raids and the peonage undertaking rest on L186.
  - L264 [APPROVED — CR-068]: "once Washoe is retaken that spring" rests on L176 [PROPOSED — CR-060]; "when McClellan's inaugural shows that he will treat" on L275 [PROPOSED — CR-065].
  - L284 and L288 [APPROVED — CR-068]: the armistice of May rests on L278 [PROPOSED — CR-062]; "Deseret, Oregon's compact" on CR-059 and CR-060.
  - L324 [APPROVED — CR-068]: see F-4.
  - L357 [APPROVED — CR-068]: stands on its own CR's L207.
- **F-6. L168 [PROPOSED — CR-066].** NOTE, author. `AGENTS.md` records CR-066 Part E as "approved and integrated with CR-061". The label disagrees.
- **F-7. Coverage comments.** Every new CR whose label appears in a section has a hidden comment with its ID somewhere in that section; none is missing by ID. They are not always adjacent: the CR-068 material at L307 and L319 has none beside it, and the CR-061 text at L170–L174 hangs on the comment at L156 with CR-066's comment between. NOTE, mech.

---

## G. Protected intent

No breach found.

- **"Pacifica wages no campaign of extermination."** Kept. Bear River (L179) is a limited action with warrants and orders "not to touch the lodges", and "the column does not follow". The Owyhee killing (L181) is done by a miners' company and Pacifica hangs its leaders. The Legion's orders in 1865 (L183) forbid carrying the war into the canyons and the war ends by treaty in a season. No Navajo campaign is made (L186). Watch-points, all NOTE, author: L159 "Pacifica's own Apache war begins on its own road" is a war the text never describes between July 1862 and the truce of winter 1862–63; L183 depends on the Legion's pay (CR-060 CT7, still open) staying out of the text, as it does; L207 has the government publish its record with the nations against Mankato while L98 (Pyramid Lake, 1860) stands in the same document, which a hostile reader inside the story would use; D-12.
- **Noe Kaʻanoe Ward; Julian never President; no throne abeyance.** Not touched. L255 keeps the Kuhina Nui and names Victoria heir. "Major Julian St. Clair" (L224) is another man.

---

## H. Literary effect of the whole

### Where the reader loses the thread

- **H-1. Where is Elias?** His journey of November 1862 to August 1863 is the spine of the middle of the war and is told in nine places in two sections, never in order: L154, L168, L172, L174, L179, L186, L205, L207, L213. The reader meets him at Taos before knowing he left Monterey, learns at L205 that he "goes to Texas" after having twice been told he was on the road there, and finds him at Salt Lake (L154) a hundred lines before Honolulu (L207). One paragraph that walks the journey once, with the theatre paragraphs referring to it, would carry more than all nine.
- **H-2. §10** (A-9). Four theatres, each told from 1861 to its end, laid end to end under a heading that says 1861–1862.
- **H-3. §11** runs 1862, 1863, spring 1862, 1863, December 1862, 1864, May 1862, 1864, February 1865, 1863. The CR-064 paragraphs are each clear and each restart the clock.
- **H-4. §12's opening** (A-30). The best device in the candidate, a vote taken before the news can arrive, is told before the reader has been through the election whose result is being awaited.
- **H-5. L201, L207, L264, L307, L319** each hold a year or more of separate actions in one paragraph of 400 to 700 words.
- **H-6. Names without introductions:** Nesmith, Deady's "returns commission", the Sunset articles, the mission party, the Chinese floor, the Native article, "the heads" (L213, used before the six sentences are called that), "the friendship doctrine", Lot Smith, Arny.
- **H-7. The Emancipation Proclamation is never named.** L207's hidden comment lists "the Proclamation"; the prose says only that "In January 1863 Lincoln answers a memorial from San Francisco's coloured citizens in a public letter", without what he says. The account of the nations then answers a charge the reader has not heard, and Hawaii's legislature puts the renewal over for a reason the reader must guess.

### Victoria's assents: which could be a clause

Keep at length: 1860 (L100); 1861 (L124); the Deady order as the price of the renewal of 1862 (L138), which is the best of them because it turns on one steamer; the condition of November 1864 (L264); the summer of 1865 (L288); the exclusion article in San Francisco (L307).

Cut to a clause or cut: L128 "Hawaii's delegation obtains that the first armoured ship completed is stationed at Honolulu" (and see C-1); L176's list of conditions or L264's repetition of it (B-10); L147 "Hawaii's legislature renews it each year"; L317 "Victoria will not have it otherwise", which is an assent asserted with no scene behind it; L357 "Victoria supports the controls", which is a reversal of canon (declared, CR-068 CT25) stated in four words and deserves either a reason or nothing. L304's "At Victoria's insistence, the family of the Hawaiian sailor killed in 1861 keeps its own claim" is already a clause and is the right size.

### The Lincoln–Elias exchanges: which could be a clause

There are about seventeen: L104, L115, L128 (two), L149, L176, L207 (three), L213 (three), L264, L271, L273, L307, L319, L324, L357. The ones that carry the contest are L128 (the offer laid before the Council, with the offer to stand down), L213 (the Terms and *Two Houses*), L264 (the offer of 1864 used by Victoria), L307 (Oregon, where Elias concedes the point) and L357 (the opinion of 1871, where he acts on it).

Cut to a clause: the State Department circular of 1862 (L207); the January 1863 letter as it stands (L207), unless H-7 is fixed, in which case it becomes one of the main ones; the terms of passage and Lincoln's letter on the draft (L207), keeping only the clause that L357 needs; Lincoln's public letter of autumn 1863 (L213), which can be folded into his refusal of early 1864; the captured correspondence (L271), to which nobody responds; the annual message of December 1864 (L273); the school readers (L324). L115's sentence on Seward and L324's meeting of 1869 are already the right size.

### The three passages most in need of rewriting

1. **L176** (Montana and Washoe). Two subjects, the central event told three times out of order, a forward reference to the Terms, a wrong antecedent and a dropped ledger sentence.
2. **L207** (the CR-068 omnibus for 1862–63). Eight exchanges in one paragraph, starting a year before the paragraph above it, with the one that matters most (January 1863) left opaque.
3. **L264** (Lincoln's offer, the blind vote, the dissolution, the campaign, the stand-down). Three labels, two canon sentences stitched in, a year compressed, and the whole placed before the election it waits on.

Close behind: L154 (Deseret), L186–L190 (a label every second sentence), L201.

### The three that work best

1. **L161–L165**, the second Valverde and the fall of Santa Fe. Every move has a cause the reader can see, Canby is a competent opponent, and Carson's resignation closes it on a person.
2. **L168**, Taos. One paragraph, one choice with a cost ("Elias gives up the trial he wants"), and it pays off at L190 when Taos does not rise.
3. **L288**, the bargain of summer 1865. The division inside Hawaii is real, Sherman's objection "is not answered", and Victoria's last clause leaves the question open as the author asked.

Also sound: L74–L76 (the House vote, dense but earned by John Sherman's line at L319), L205 (canon), and the endings of L304 ("McClellan puts the signed text in his safe") and L307 (the stuffed box voided on Pacifica's own complaint).

---

## Verdict

**Needs another pass.** The facts of the nine drafts fit together better than the page shows: the calendars of 1862–63, the Council's votes, the electoral count, and the dates from the armistice to the exchange of 1867 are consistent. What is not ready is the order of telling and the seams with canon.

**Blockers (9):** A-7 (the reply of 1861 uses Oregon's convention and the invasion before they are told); A-9 (§10's order); A-16 with B-8 and D-1 (the Washoe paragraph and its ledger sentence); A-23 (L207); A-30 with B-25 (the blind vote before the election); C-31 (the Colorado line stated two ways); A-41 (the river sentence in the wrong paragraph); E-1 (the pointer "told above"); E-2 (status line and merge notes). Seven are mechanical; A-9 and the cuts in A-23 need the author.

**By section, furthest from ready first:**

- **§10** needs restructuring, an author's decision on its shape, and the Washoe and Deseret paragraphs rewritten.
- **§12** needs its first third reordered and canon's summary sentences (L266, L275, L282, L290, L292, L298, L312) cut against the new detail.
- **§11** needs reordering by date and L207 split; its individual paragraphs are sound.
- **§9** is ready once L126 is cut and the offer's sequence is settled.
- **§8** is ready after mechanical fixes (A-1, A-2, A-39).
- **§13** is ready after mechanical fixes (A-41, A-42) and the author's decision on C-12.
