# Review 3-C — Oregon, the treaty, the Gulf and the Union's war (CR-059, CR-062, CR-063, CR-064)

Fresh-context review, 13 November 2026. Read: AGENTS.md, the canon extract (§§8–13), the four candidates in full, and only the cited rows of CR-068 (G8, G9a, G10, G11, L3, CT4, CT6, CT10, CT11, CT23, CT29 and its §12 blocks), CR-060 (D4–D12, C4–C6, C11, M7, CO4–CO7, A1–A4), CR-065 (E4, E6, P1–P2, L3, M1–M4 and its Mobile, Valley and Chattahoochee passages) and CR-067 (Ord, Naglee, Denver, Hays). Nothing under outputs/sessions/ was read and git log was not run. `lint_canon.py --only` on the four candidates is clean. CR-061 was not on the permitted list, so rows that cite it (CR-062 T3, X2, M5, the S1 table) are unchecked.

Classes: **BLOCKER** (fix before integration), **SHOULD-FIX**, **NOTE**. Each finding says whether it is *author* (needs a decision) or *mechanical*. Line numbers are those of the files as read today.

---

## Blockers

**B1 — CR-059: the recall of 1 October 1861 against the state of war. BLOCKER, author.**
I2 (line 139) and the §10 text (line 598) have the War Department order "every regular on the coast east" on 1 October 1861. W15 (line 130) has Congress recognise a state of war with Pacifica before 6 August 1861, canon §10 has Portland and Vancouver taken in July–September, and canon §10 and W13 have Washington shipping four Iowa regiments *to* the Sound in the same months. A government at war on that coast does not send its only trained troops there to New York while sending raw regiments in to replace them. The order is a historical quotation (OR I.644) from a timeline with no Pacific war. It is load-bearing: the Walla Walla convention (I3) is framed as the regulars "carrying out their own government's order", and Part V calls Idaho load-bearing for the vote (4–6 points). The draft's own note (line 774) lists this as not done. Related and also unresolved: whether Wright marches east with the column (I3; CR-067 says "George Wright's regulars have marched east").

**B2 — CR-064: nothing happens between 8 November 1864 and the armistice. BLOCKER, author.**
The draft stops on election day with Thomas across the Chattahoochee, McPherson on the Georgia Railroad at Decatur, six miles from Atlanta (A9, line 103; step 11, line 233), and a relieving order drafted and suspended only because "Lincoln, a month from the election, will not relieve the general whose army is in contact" (step 12). After 8 November that reason is gone, Lincoln is pushing "last winter operations" at Petersburg and Mobile (canon §11; CR-063 Part VI), and Grant has his replacement named. The draft gives no reason why Atlanta, on two railways, survives four more months. Canon's armistice line and CR-063's December decision ("the western army is stalled before Atlanta") both need it. The draft's note (line 404) admits it. Either write the winter, or mark it **[OPEN]** in the §11 text.

No blocker was found in CR-062 or CR-063.

---

## 1. Internal consistency

### CR-059

1. **SHOULD-FIX, mechanical.** Line 289: "without California the balance is still even". It is not: S2 (line 221), H3 (line 99), line 287 and the §8 text all say parity ended with Minnesota in May 1858 (16 free, 15 slave). Stephens's "already gone" is therefore true by one state; the argument should be that the loss is nine months old and a lead of two is new.
2. **SHOULD-FIX, author.** The Maine motive contradicts the policy rows. P4 (line 84) says assisted passage and the land law "draw emigrants south"; P5 forbids anything aimed at Oregon; Part I says "Washington sees business, not policy". H5 (line 101), line 302 and the §8 text (line 586) say Pacifica's passages "are filling Oregon's valleys" and Oregon's settlers "are arriving on Monterey's tickets". Passages to California do not fill Oregon. The vote survives without Wood and Foster (108–108 fails), but the author's brief was that every changed vote be causally explicit.
3. **SHOULD-FIX, mechanical.** "The convention never meets" (W1 line 117; §10 text line 593) against W11a (line 128), where a convention of 1861 delegates sits at Port Townsend and adopts a constitution, and CR-068's approved §10 sentence saying the same. Say "does not meet at Salem". W11a, W12 and W15 have no sentence in CR-059's own storyline text; W11a is carried by CR-068's block, W15's staged force by none of the four candidates.
4. **SHOULD-FIX, mechanical.** V2 against V3 (lines 155–156): the electorate must be "resident before the armistice of May 1865 and for a year before the vote", yet displaced Unionists and men in Union service vote at Port Townsend. State the exception. The three residence tests (six months, before May 1865, a year) are redundant unless continuity is meant. "Elias's 'concession' on the date" does not say what he conceded.
5. **SHOULD-FIX, author.** W14 (line 132) has Casey holding Port Townsend and also "Cady … Alvord … are the Union's officers at Port Townsend"; who commands is unclear. I2 uses Wright's and the District of Oregon's reports of early 1863 as evidence, although in this timeline that district is Pacifican and Wright's column left in July 1862. CR-064 H3 and its interface row then cite "Halleck refuses coin, March 1863 (I2)" as an event of this timeline. Decide whether it happens, and to whom.
6. **NOTE, mechanical.** Stale passages: the status line (line 3) says the 7 November choices "have not yet been seen by a fresh reviewer", while line 774 records a review of 13 November; CT14 (line 693) still quotes "It transfers Oregon only if Oregon votes for it" as "already in this draft's §12 text" (the text now reads "as Oregon's voters shall choose"); CT15's conflict paragraph quotes superseded wording; line 404 refers to "set piece 6" (the scene list's item 6 is Billy Chinook) and to Colfax's 1865 tour, while V11 has him campaign in August 1866.
7. **NOTE.** V13 (line 166) puts "the Council in San Francisco"; canon §8 seats the Council at Monterey. W4: a relief steamer seized in the flood of December 1861 is released as the price of a renewal voted in May 1862, five months after the flood; the stake can only be precedent, and the text should say so.
8. **NOTE.** The §8 text gives "June 1858 … The Senate passes the bill in May" in an order that reads as May 1859. The §10 text's "resigns his commission in the spring" follows July 1862 and means April 1863.

Fact-change json agrees with the storyline text (all five event patterns match once).

### CR-062

1. **SHOULD-FIX, mechanical.** Decided items still marked open: L1 (line 129, "all OPEN") and Part VI's heading (line 250) against open decision 17 ("the names you suggested are fine"); L2 (line 130, "OPEN … Recommended") against Part VI ("chosen"); Part II's T1 options still "recommended" and "name OPEN".
2. **SHOULD-FIX, mechanical.** The Union signatory has three labels: T1 (line 51) "CR-065 M2 proposes Robert C. Winthrop; PROPOSED"; CR-065 M2 "OPEN"; the §12 text "**[OPEN]** His name".
3. **SHOULD-FIX, mechanical.** A1 and A6 (lines 40, 45) now carry dates and offices (Richmond's convention in April; Pacifica's in mid-May, signed by Elias as Protector; the Amity treaty in the last week of May as his last act). No storyline sentence in CR-062 states any of them; CR-068's block has only "the Republic's armistice is signed in May 1865". The fix note (line 437) still lists the Amity date as "not done".
4. **SHOULD-FIX, mechanical.** Line 223: "Whether Fort Fisher happens in this timeline is CR-063's to decide". It was decided on 12 November (M-a: it does not).
5. **SHOULD-FIX, mechanical.** O5 (line 76) "strikes the no-branch article"; O3 and Part III put the no-branch in the armistice protocol, not in an article. T4 (line 54) fixes $40 million in the treaty while the no-branch lowers it (CR-059 V1); O2 lists T3 and T5 as "written for either result" but not T4. The treaty's price article therefore depends on the protocol too, which sits badly with "the Senate never votes on a conditional cession".
6. **SHOULD-FIX, mechanical.** §12 text (line 299): "Sumner reads Oregon's returns and the article on colour, denounces the clause". "The clause" (Oregon's exclusion clause) has not been named in CR-062's text and reads as the article on colour.
7. **NOTE.** T10a cites "CR-060 CO7, 1878–82"; CO7 is headed 1875–82. The first §12 paragraph says Pacifica's "war advances to Richmond end with the armistice, as it printed in 1863": true to CR-068 G6, but no A-row decides it.
8. **NOTE, author (already flagged by the draft).** How Lincoln in 1867 knows the maxim "a guarantor has a right to come in". The sentence is in the storyline text as fact. CR-068 G10 has him use it already in 1866. The phrase also appears three times in CR-062's own text.

### CR-063

1. **SHOULD-FIX, mechanical.** Order of events at Mobile. Canon's sentences, kept unchanged (line 302), run: lead ship sinks, column breaks, *Tennessee* engages, Farragut is killed. Part VI steps 6–7 (lines 251–252) kill Farragut first and have Buchanan take "*Hartford* … with her admiral dead". The inserted sentence should be placed, or canon's order changed, so both agree.
2. **SHOULD-FIX, author (flagged by the draft, line 454).** Step 5 (line 164): "Logan's workshop goes with the trains", and the trains are captured at the forks with about 1,000 men. Where Logan and Marcus are that morning decides whether either is nearly taken. Both must then get from Johnston's army back across a river the Union holds above Port Hudson to "rebuild capacity in Confederate-held Louisiana" (canon).
3. **NOTE, mechanical.** V3 and step 2 cite "CR-064 C3" for Steele's corps; the row is C4. The repair-pass log (line 526, "about 8,000 stay") is superseded and says so only in one of the two places.
4. **NOTE.** Step 8: *Hartford*'s captain is "senior in the bay"; the squadron's next senior officer is not identified. *Hartford* towed out past Fort Morgan with her bow opened strains belief.

Tables, tensions, json and storyline otherwise agree (15,000 out, 12,500 to Johnston, 16,500 in the works, 15,000 surrendered and paroled; three ironclads plus *New Ironsides*; landing about 6 February, attack about 14 February).

### CR-064

1. **SHOULD-FIX, mechanical.** Decided items treated as open: line 408 "none is decided" (all eighteen are); E4 (line 113) and the §11 text (line 300) "**[OPEN]** Galena's fate" against open decision 10 (she survives, holed, laid up); O3 "The others' posts are OPEN" against open decision 12; C2 and Part III "Rawlins (OPEN)" against open decision 2.
2. **SHOULD-FIX, mechanical.** A. J. Smith: R4 (line 88) "From May"; Part IV (line 200) and open decision 8 "from April"; R4 also says Fort Pillow (12 April) falls before he is in place.
3. **SHOULD-FIX, author.** Where the front is on election day. The summary (line 34) has the armies "face each other across the Chattahoochee"; A10 and CR-065 have them "in contact on the Chattahoochee"; CR-063 has "Johnston on the Chattahoochee". But step 10 puts Thomas across the river and Johnston in works "on the south bank north of Atlanta", and step 11 puts McPherson at Decatur, east of the city. That is Sherman's position of 19–20 July 1864, not a river line.
4. **SHOULD-FIX, mechanical.** O1 (line 120): "Canon moves one Union officer to Pacifica: Sherman … checked 8 November". CR-067, approved on 9 November and cited in CR-059 open decision 16, makes Ord, Naglee, Denver and Stone Pacifican. Ord historically commanded the XIII Corps from June 1863, the corps CR-063 V5 sends to Port Hudson; its commander needs a name that is not his.
5. **SHOULD-FIX, mechanical.** The interface rows (lines 268–269) still read "Conflict to resolve" and "Conflict to flag" on the XIX Corps; CR-065 has resolved both (no XIX Corps; the VI Corps alone).
6. **NOTE.** Resaca is "12–14 May" in A2 and "the historical battle a day early" in step 4; by the draft's own dates it is two days early.

---

## 2. 1865–67 across CR-062, CR-059 and CR-068 (G9a, G10, CT29)

The chronology agrees wherever it is stated:

| Event | CR-062 | CR-059 | CR-068 |
|---|---|---|---|
| Richmond's armistice | April 1865 (A1) | — | not stated in G9a or CT29 |
| Pacifica's armistice | mid-May, Elias as Protector (A1) | "armistice of May 1865" (V2) | May 1865 (G9a, CT29, §12 block) |
| Amity treaty | last week of May, last act as Protector (A6) | — | same (G9a) |
| Protectorship ends | last day of May (A1) | "laid … down in May 1865" (V11) | same |
| Enabling Law | December (A1; Part II) | "life office of 1865" | chambers September–October, Hawaii December |
| Western treaty and Oregon protocol | Washington, December 1865; Vallejo and Sherman | same (open decision 14; Part VI) | Sherman sails in October (G9a) |
| Lincoln's Oregon letter | — | June 1866 (V11) | June 1866 (G10) |
| Pacifica ratifies; charter entrenched | summer 1866 (O6) | summer 1866 (V10) | "that summer" (G10) |
| Oregon's vote | October 1866 | 1 October 1866 | — |
| Certification | December 1866–January 1867 | — | — |
| Alaska signed | early March 1867 | — | — |
| Senate consent; exchange | 9 April 1867; summer | 1867 | spring 1867 |

Findings:

1. **NOTE, mechanical.** A1 attributes "Richmond's convention in April" to "CR-068 G9a, CT29". Neither row states it. CR-065 has Stephens expect an armistice "in a month" from 3 February.
2. **SHOULD-FIX, author.** Authority for the Oregon protocol. It is "a supplement to the 1865 armistice convention", signed in December 1865. The armistice was the Protector's act under Article XIV. In December Elias is Chancellor under Articles that, by CR-068 G9a's own argument, give no lawful basis for what the columns hold. No row says who signs the protocol for Pacifica or under what power. It is the sharpest instance of G9a's "who is bound?" and it goes unused.
3. **SHOULD-FIX, author.** No row places the negotiation of summer–autumn 1865. A1, CR-059 V1 and CR-068 G9a all lean on "Washington's commissioners" at Monterey, unnamed, while the signing is in Washington by the Secretary of State.
4. **NOTE.** Vallejo's office in 1865 is not stated. Canon last shows him as California's President in 1861. A member state's head abroad for four months is worth a clause.
5. **SHOULD-FIX, author. McClellan's motives.** Why he signs the armistice is argued (Part I). Why a "Union man" signs away half the West is not argued in CR-062 at all; the reasons given are the Senate's. Why he holds the treaty sixteen months is argued, but the cost is missing: an executive protocol that puts a United States territory to a vote, and binds the Union to disarm it if the vote goes the Union's way, is the obvious constitutional charge, and Wade and Chandler never make it (S5). CR-062's own question 3 raises it.
6. **SHOULD-FIX, author.** O7's third reason for waiting, "the Senate of the 40th Congress", is asserted. S7 says the alternate 1866 legislatures are unbuilt, so nothing shows that Senate is friendlier.
7. **NOTE.** The Amity treaty a fortnight after the armistice gives the Radicals the speech Part I says McClellan must not hand them. That it was printed since 1863 explains Pacifica; it does not explain why McClellan pays no price.
8. **Sound as written:** why the Senate consents (S4, with the deposit, Russia's signature and the Navy estimate); why Oregon votes as it does (the exclusion hinge, the Idaho trade, entrenchment), subject to B1 and to MODEL shares.
9. **SHOULD-FIX, mechanical.** The same events have storyline sentences in three drafts with different labels: Lincoln's Oregon letter and Elias's answer in CR-059's §12 block (PROPOSED — CR-059) and CR-068's (APPROVED — CR-068); the letter of 1867 in CR-062's (PROPOSED — CR-062) and CR-068's. Choose one home for each before integration. CR-068's bargain paragraph carries both "[APPROVED]" and "[PROPOSED]" on one sentence.

---

## 3. Oregon in CR-059

- **State of war and staged force (W15):** agrees with CR-068 CT4 and G8 and CR-065 P2 and M1. CR-068 has the force "stood down" in the sentence after the November news; W15 and CR-065 say March. Minor.
- **Port Townsend convention (W11a, W12, V5):** agrees with CR-068 CT11. See 1.3 above for "never meets".
- **Electorate and residence:** May 1865 is used consistently (V2; line 343). See 1.4.
- **Lincoln's letter (V11, line 164; §12 text):** agrees with CR-068 G10 and CT6: he grants that the yearly office was laid down in May 1865 as Hawaii asked, and attacks the life office. Line 464 has the letter name "a Providentor for life"; G10 says he does not write the office's name. NOTE.
- **Campaign voices:** Bush is gone from 1866 everywhere. The side against accession is carried by Colfax, Lincoln and a newspaper; Corbett and Dryer are names in a table (Dryer was historically Lincoln's commissioner at Honolulu in 1861–64, which this timeline cannot give him; NOTE). The 40 per cent of Douglas Democrats who vote no have no speaker (the draft admits it, line 774). Who resists Victoria over X2 is also unanswered.
- **Persons misplaced:** Wright and Alvord (1.5); Colfax in 1865 and 1866 (1.6). None other found.

---

## 4. CR-063 and CR-064 against each other, CR-062 and CR-065

Agree: Steele's XV Corps and Blair's division on 17–18 May 1863; McPherson at Jackson in July; 12,500 escapees and 15,000 paroled; Polk on the Alabama flank and no Fort Fisher; Butler's 12,000 in the East (CR-065); the attack in February after Hampton Roads; Indiana's soldiers in October with Thomas on the river.

1. **SHOULD-FIX, author.** The XIII Corps (13,000) is recalled from Port Hudson to Chattanooga in October 1863 (CR-063 V5) and then vanishes. CR-064 A1's 99,000 is the historical figure, which excluded it because it was in the Gulf. The regiments of the never-formed XIX Corps are covered only by CR-065's "not missing men".
2. **Real-history claims that look wrong:**
   - CR-064 A8 and step 8 (lines 102, 230): Allatoona "sixty miles north of Atlanta" and "two months on forty miles of railroad". By the Western and Atlantic's mileage Allatoona is about 40 miles from Atlanta and Dalton about 100; the figures are swapped. Confidence about 85 per cent. The draft lists it as a minor point not done.
   - CR-064 §11 text (line 290): "Four Iowa regiments raised that winter". The 11th and 13th were mustered in the autumn of 1861. Confidence about 80 per cent.
   - CR-062 §12 text and Part IV: "Stoeckl reports from Washington" before the meeting of 16 December 1866. He was in St Petersburg that winter and attended the meeting. Confidence about 85 per cent. A report in person serves as well.
   - CR-059 W14: Alvord in the District of Oregon "from 7 April 1862"; I recall July 1862. Confidence low (about 50 per cent).
   - CR-064 open decision 12 puts A. S. Johnston "commanding in Texas until he resigns in 1861"; that is Twiggs's command and Twiggs's surrender. An alternate-history choice with consequences, not an error.
   - Checked and sound: the 1859 roll-call arithmetic (106–110), 1 October 1866 a Monday, the Alaska dates and price, the gold weights, the wagon arithmetic, Shiloh's strengths, Polk's reinforcement sum (19,646; 73,450), the Vicksburg dates, the *Peterhoff*, Drewry's Bluff, the regular-army dates of McPherson and Thomas.

---

## 5. Canon and protected intent

No breach of protected intent. No undeclared contradiction of the extract was found in CR-063 or CR-064. Points to note:

- CR-062 and CR-059 rely on CR-068 CT29 (the lapse of May 1865), CT4 (state of war) and CT11, and on CR-060 CT1, CT2, CT5 and CT9 (Leadville's ground Pacifican against canon §12 "Leadville stay Union") without tensions of their own. Acceptable only if those drafts integrate together. NOTE.
- CR-059 H7 adds Buchanan's Sausalito demand before the Carson Convention; labelled PROPOSED, no tension entry. NOTE.
- CR-062 S1 gives every ceded district a consent instrument except Colorado's Pacifican side. South Park, the Blue River and California Gulch were organised counties of Colorado Territory in 1861. T10a gives the Union-side districts a vote and these none, against the second head of the Terms of Monterey. SHOULD-FIX, author (with CR-060).

---

## 6. Labels

Covered above: CR-062 L1, L2, T1; CR-064 line 408, E4, O3, C2; the triple-homed Lincoln sentences; CR-068's double label. Also: CR-059 CT9 calls CR-060 CT2 "approved" while CR-062's S1 table calls the same thing "decided" under a PROPOSED row; the drafts' own rule is that decisions settle options and approve nothing. MODEL is used consistently for shares, strengths and amounts.

---

## 7. Literary judgement: the three weakest points

1. **Oregon has no opponent from Oregon.** The case against accession is made by a visiting congressman, a letter from Springfield and an editor. The one Oregonian with a reversal is on the winning side. Elias's "temptation" is three refusals that cost him nothing, because he wins anyway; and two of the six House votes of 1859 turn on a motive that contradicts the policy it is drawn from.
2. **McClellan is furniture.** The man who signs the armistices, cedes the West and keeps a treaty in his safe for sixteen months has no reason of his own on the page, and nobody attacks him for the protocol. The Senate paragraph is a list of one motive per senator. Logan's test is defused by the "better offer", as the draft concedes.
3. **The Atlanta stall is argued by precedent, not shown.** Each hinge is justified by "as McPherson did" or "as before Nashville"; Thomas is wrong at every one; and the campaign simply stops on election day. In CR-063 the Mobile sequence is the best writing in the set, but Logan, whose field it is, is placed nowhere at Vicksburg or at Mobile.

---

## Verdicts

| Draft | Verdict |
|---|---|
| CR-059 | **Not ready.** B1 needs the author; then the Maine motive, the Port Townsend command and the mechanical list. |
| CR-062 | **Ready after mechanical fixes**, provided Lincoln's knowledge of the maxim (S8) is decided or marked OPEN in the text. The protocol's authority, McClellan's motive and the missing constitutional objection are author items that would strengthen it but do not block it. |
| CR-063 | **Ready after mechanical fixes** (the order of Farragut's death; the C3/C4 reference; a commander for the XIII Corps). Logan's and Marcus's whereabouts can stay OPEN if labelled. |
| CR-064 | **Not ready.** B2 needs the author; then the election-day front, the stale OPEN labels, O1 against CR-067 and Allatoona's distance. |
