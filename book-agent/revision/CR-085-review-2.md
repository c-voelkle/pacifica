Fresh-context review of CR-085, revision 3, 23 November 2026. The reviewer read the draft, AGENTS.md and current canon, and not the writer's notes or earlier reviews.

Tools run first: `lint_canon.py --only` (10 findings, all the five unregistered `CT-` IDs), `preflight.py --draft` (0 errors, 5 warnings, the same five IDs), `cr_facts.py preview --tensions` (three canon passages for T-R3: AGENTS.md:68 and `L1734` twice). Line numbers below are `master_storyline.md` lines (L…) or lines of `CR-085.md` (draft line …).

## Verdict

One more revision. The idea of Part A is strong and fits the ending the author asked for: the coup fails, Japan answers it by proposing a Concord with no date, and the Concord signs the two articles as a union that cannot lapse. The draft is not ready because the legal route for striking the term contradicts canon, the draft's own T-M4 and CR-086; because the list of what T-R3 Case B changes is incomplete and the draft still speaks of a second and third term in several places; because the Kansai station is announced before the Council that is said to agree it; and because the custody sentence and Japan's "party to the monopoly" do not agree with each other or with canon. Parts B to D are close; their problems are figures and a few mechanisms.

## Blockers

**B1. The term is struck by a ruling of the Common Tribunal, and the Senate is bypassed.**
- *Passage:* A4, first row ("The Senate ... loses the power to let the Concord lapse by not acting"); A6 ("the Common Tribunal (`L1602`) rules that the term is a matter of the renewal and within the delegations' competence (PROPOSED)").
- *Problem:* Four conflicts.
  1. `L1604`: "In 1928 she wins two-thirds Senate consent and an Act of Indemnity ... Julian accepts a five-year first term instead of ten, quota review at renewal, Pacifica's delegates chosen half by each chamber and a Polytechnic audit reported to the Senate." The ledger records these as "1928 conditions of consent" (`C-1927-CONCORD`). Removing the term removes a condition on which the Senate consented. That is a question of the Realm's constitution, and canon's forum for it is the Court of the Realm at Monterey ("The constitutional case at Monterey is mooted before judgment", `L1604`), not a Concord body.
  2. `L1602`: "A Common Tribunal of three judges from each side, with alternating chair, decides competences." Canon gives it competences between common and national spheres. The draft has it decide what the Pacifican Senate may vote on, and does not say how three and three divide or who holds the chair in 1932.
  3. The draft against itself: T-M4 Case B says a fourth ministry "forces a full Senate treaty-amendment fight", and A6 calls striking the term "the larger change". The larger change cannot take the lighter route. A6 also has interior senators fight pool entry "on the floor" and Giannini's allies fight the yen reset there, without saying what the floor votes on.
  4. CR-086 D5: the aliʻi seats "make the article their condition for the rest of the season's bills: the British annuities, the renewal without term and the stabilization credits." In CR-086 the renewal without term is a bill before the chambers. In CR-085 the chambers have no vote on it.
  A fifth point is literary and legal at once: this is 1927 again. Julian imposed the Concord unlawfully and Victoria cured it in 1928 on these very conditions. She is alive in 1932 (`L1738`, "ninety-three or ninety-four"), and the draft does not mention her once in Part A.
- *Fix:* Send the striking of the term to the Senate at two-thirds, as an amendment of the conditions of 1928, beside the delegations' ratification. Tate then loses in a vote and not in a ruling; the sufficers' price in CR-086 D5 has something to bite on; and Victoria can decline to speak, or speak once. If the author prefers the Tribunal route, the draft must say why a Concord tribunal can rule on the Senate's competence, list it as a canon tension against `L1604`, and CR-086 D5 must drop "the renewal without term" from the season's bills.

**B2. T-R3 Case B does not list everything it changes, and the draft still assumes a term ending in 1937.**
- *Passage:* draft line 297 ("Passages to revise in this case: `L1734`, `L1595`, the AGENTS.md sentence ..., `C-1932-CONCORD-RENEWAL` in the ledger, and `CR-084`'s reverter clause").
- *Problem:* Canon passages and ledger entries that state or depend on the term and are not in that list:
  - `L1597`: "agreed matters reviewed at every renewal".
  - `L1604`: "quota review at renewal" and "a five-year first term instead of ten".
  - `L1600`: "before 1937", and ledger `C-1928-HAYAMA-ANNEX` (`until = 1937`, open note: "the end of the Concord's second term").
  - Ledger `C-1927-CONCORD` (`renewals`, the conditions of 1928, `can_end`), `C-1927-CONCORD-EXEC` (named under "Amended commitments" at draft line 252 but not in the tension's list) and `C-1927-CONCORD-RESERVES` ("reviewed at every renewal").
  - `character_bible.md` line 128: "Its defeat permits renewal to 1937 and common overseas command"; line 126: "a five-year executive trust"; line 137: "five-year Concord executive term"; line 132 on the Navy portfolio.
  - AGENTS.md line 68 also says "five-year Concord executive term" earlier in the same paragraph.
  The `add_forbidden` pattern (`Japan may refuse in 1937|renewed to 1937|renewal (?:runs|run) to 1937`) does not match the bible's "renewal to 1937", so the linter will stay clean while the bible contradicts the storyline.
  Inside the draft, these still assume terms:
  - B1 item 4: "Through the second term's end in mid-1937".
  - Decisions P-2: "third-term renewal in mid-1937 unlocks Concord Pool entry".
  - Decisions P-4: "a half-built 1937 Kansai 80 MW station" (the language of a stake in a refusal).
  - Decisions P-1: "keeps 65/35 quota to 1937".
  - Section B's heading ("Mid-1937 Pool-Entry Bargain") and T-H1 Case A ("the day the bar lapses in mid-1937").
  - A4 and A6 say "every review" and "first review" without ever fixing the review's month; canon's first term "runs from the provisional application of 1927 to 1932" (`L1595`) and `L1634` puts 29 April 1932 "at the close of the Concord's first term".
- *Fix:* Complete the list under T-R3, widen the forbidden pattern to `renewal to 1937` and `(second|third) term`, correct the five places in the draft, and state the review date.

**B3. The Kansai station is announced on 29 April and agreed in late May.**
- *Passage:* A2 ("At the opening the two crowns announce a second station of the same size for Osaka and Kobe"); A4 table, row "The Kansai station" (Wigner "loses on the date"); C2 ("announced by the two crowns at Tokyo's opening on 29 April 1932 and committed by the Board's charter at the renewal"); draft line 116 (the protocol is "part of what Julian gives for a Concord without term").
- *Problem:* A4 opens: "Each term below has a Pacifican who objects to it and loses", and lists Kansai as a term agreed at Hayama. By then both crowns have announced it to the world, by radiotelephone, a month earlier. Wigner cannot lose at Hayama an argument settled on 29 April, and a station promised before the coup is not a price paid for what Japan offers after it. The authority is also missing: C2 says Pacifican consent comes from "Langmuir's seat and the Council of the Seal", and the Board that commits the station is chartered in May. Nothing says who consented before 29 April. Canon's precedent is Julian announcing Tokyo at the demonstration of 1927 (`L1634`), which was his alone to announce.
- *Fix:* Either move the Works' decision, and Wigner's defeat, to the winter (the Council of the Seal consents before April; Hayama only charters the Board), and take Kansai out of the table of what is traded in May; or have 29 April announce only that a second station will be studied, and let Hayama commit it. The first is better for the story, because A2's point is that the Restoration officers see "a second chain" before they strike.

**B4. Custody of the devices, the Japanese Navy minister and "a party to the monopoly" do not fit together.**
- *Passage:* A4, row 2 ("Custody of the devices stays where it is, with the sovereign and the Council of the Seal and outside the common Navy (PROPOSED; the storyline does not say where custody lies)"); A5 ("Japan renounces nothing, because it is a party to the monopoly and not a power outside it"; "Japan is not told what the Works holds"; "the fleet that would carry the weapon is the common fleet and its minister is now Japanese by law").
- *Problem:*
  1. "Stays where it is" states as existing fact something the same sentence admits canon does not contain. Canon has only: "The design is sealed in the Thalassia archive" (`L1612`), with two keys, the sovereign's and the Polytechnic chief's (CR-050), and a Council of the Seal that is the Works' monthly management council: "the director in the chair, the Chief, a General Staff officer for the Polytechnic's key, an officer of the naval constructor's estate, the Treasury's sealed comptroller" (`L1362`). Nothing gives that Council custody of assembled weapons.
  2. A5 says Japan is inside the monopoly, and in the same paragraph that it builds no separating plant, returns every fuel element, is told nothing of the stock and has no part in custody. Canon's word for that position is "an instrument of dependence" (`L1634`). Japan is the first power to live under Article I's rule, not a holder of what the rule protects.
  3. King's objection is answered by taking the weapon out of the Navy, yet A5 rests Japan's countersignature on the weapon being carried by the common fleet under a Japanese minister. If he is in the chain of delivery he must know something; if he is not, his countersignature promises nothing he controls. The draft has to choose.
  4. "The sovereign" is ambiguous. Julian holds custody as Sovereign of Pacifica or as holder of the Concord's executive. Under a union without term the difference matters for ever.
- *Fix:* State custody as a new fact and decide it in one CR only (CR-086's T-5 already has King before the Council of the Seal on the pledge). A wording that follows canon's precedent: "The devices are held under the two keys of the Thalassia archive, the Sovereign of Pacifica's and the Polytechnic chief's. They are no part of the common Navy's establishment, and the common Navy minister has no key. The common fleet carries a device only on an order under both keys." Then rewrite A5: Japan countersigns as the partner whose fleet would be ordered to carry, which is a real promise, and drop "party to the monopoly" for a plainer sentence: Japan is the one power that has the atom's power by lease and has already given what Article I asks.

## Should fix

**S1. The May timetable has no dates and may not close.** A2 puts the coup "two weeks" after 29 April, so about 15 May. The Council is "late May". Between them: the courts martial open, the court reaches its conclusion with Takahashi and the navy minister, Chichibu carries it at Thalassia, Chiyo carries it "to Takahashi and back", Julian crosses the Pacific (about 3,400 nautical miles from Oʻahu, a week at a cruiser's speed; from memory), and three common ministers assemble. `L1625` says "state business still goes by cable" and the Tokyo voice link is assumed overheard, so Chiyo's errand needs a medium. `L1736` (PROPOSED) has Vance killed "in May at the hands of headquarters guards sympathetic to the Restoration"; the draft never mentions it, yet it would decide whether Julian can leave Thalassia that month. Give four or five dates, or move the Council to early June and keep ratification in July. Set piece 4 also puts Takahashi, seventy-seven, at Thalassia in June facing the common Finance minister; canon's only statement is "Takahashi remains in Tokyo" (`L1597`). Say he travels, or send a deputy.

**S2. Nobody in Japan is named as the author of the largest offer Japan ever makes.** A3 says "the court's conclusion". The draft leaves Inukai's fate open "as canon does", but canon's machinery needs a prime minister ("with Japan's prime minister countersigning", `L1597`) and a Privy Council ("Japan's Emperor ratifies on the Privy Council's conditional advice", `L1593`). A union that "ends only by the agreement of both crowns" is a constitutional act for Japan. Name who advises it (Saionji is in canon at `L1782`), say what the Privy Council attaches, and decide who heads the government. The Diet "votes its quota ... and chooses its sixty delegates in June" with no recorded opposition, weeks after a coup whose manifesto called Thalassia a bakufu. Somebody in the Diet should say that a Concord without term is the bakufu made permanent.

**S3. "None of them is Julian's" is not true of the navy.** A3 claims three Japanese institutions carry the renewal. The second is "Kiyoshi's son hold[ing] the Japanese units of the western squadron loyal" (`L1732`). The western squadron is part of the common Navy, whose executive is Julian's, and Kiyoshi's son knows the day because Maria Kashiwagi "reports what she hears to the Navy General Staff" (`L1677`). Canon's sentence "Emperor Shōwa and the navy stand against them" can carry the claim if the draft says which navy: the home naval establishment in Tokyo as well as the common squadron. As written, a reader who knows `L1732` will object.

**S4. What Japan receives is thinner than the table suggests.** Row by row:
- The Navy seat: `L1597` already says "At least one must be Japanese by law; convention gives Japan the Navy." The gain is a convention made law.
- The yen: canon already gives it ("the adjustable parity it wins at Thalassia", `L1695`).
- Pool entry in 1937: `L1600` bars Japan only "before 1937", so the bar lapses then in any case (see S9).
- Kansai: announced before the coup (B3).
- The piers: CR-084's.
Against this Japan gives up its squadron, its overseas commands and its exit, and the alternating executive is refused "for every review". That last phrase extends `L1734` ("Japan's demand for an alternating executive is refused"), is not listed as a tension, and contradicts the same row's "At each review ... the seats ... are open" and A6's "The argument returns at the first review". The draft says Japan "offers it before it is asked". That can work as the turn, but then the draft should say plainly that Japan's court buys security against its own army and pays in sovereignty, and should give Japan one thing of substance it did not already have. Candidates: a fixed share of the common fleet's building orders now, or a quota-linked voice in the agenda of the Council, or a second Japanese common minister by convention.

**S5. The named objectors.** All five are alive and placed in 1932, with these reservations.
- *Samuel Wilder King* (born 1886; "the Works' naval ordnance officer from 1922", registry): in character and well chosen. Set piece 3 has him argue at Hayama, but `L1651` admits only Julian, the Emperor as host and the common ministers. Give him a forum: the General Staff's paper to the cabinet, or the Council of the Seal. CR-086 T-5 also has King object, to the pledge, before the Council of the Seal, and lose. He loses twice in one summer in two drafts; decide whether that is one argument with two parts.
- *Harlan Tate*: canon says of 1928 "His bloc splits and he abstains" (`L1604`). "Harlan Tate's bloc" in 1932 needs a word on what is left of it. He has no registry ID and no birth year; as "Silas's old adjutant" he may be past sixty-eight, and CR-038 retires senators at sixty-eight. Not checkable from canon; the drafter should check or state his age. CR-084 also uses Tate's bloc as a loser in July.
- *Giannini*: in character (`L1695`: he "answers in the Senate that the money should go to the mortgages"). Whether he is `CT-GIANNINI` is still OPEN (AGENTS.md, CR-057). Across the suite he loses on the granary (canon), the annuities (CR-084), the yen (CR-085) and the credits (CR-086 B1), and wins once (CR-083 A11). Four defeats in one season make him a device.
- *Harris Ryan* (born 1866, the power seat from 1924): placed and in character. He reaches sixty-eight in 1934, which is worth a line since pool entry falls in 1937.
- *Eugene Wigner* (arrives about 1924; "the engineer's brake on Szilárd's haste", `L1637`): in character. What he "gets", the siting rule "inland, on rock, to the Polytechnic's code", is already the rule for Tokyo (`L1634`), so he wins nothing. Give him a real concession, for example a year of Tokyo's operating record before Kansai's pile is loaded.

**S6. The draft contradicts itself on the oil lever.** A1: "The Batavia Compact gives Japanese houses oil of their own ... Only the transports remain." A7 item 7 and the impact note at draft line 213: Julian keeps "common-navy transport and nuclear/oil supply leverage firmly in hand". CR-084 A2a records that the oil lever is spent "knowingly". Correct A7 and the impact note.

**S7. The yen reset's figures and costs (A7).**
- "20–25%" and "±5%" are marked MODEL, but section G lists the modelling as a task not yet done. They are the drafter's estimates with no model behind them; label them PROPOSED or size them. The "25–33%" rise in yen cost is correct arithmetic from them.
- "Because Japan's 35% quota is payable in gold dollars": canon does not say in what money the quota is paid (`L1597`). State it as PROPOSED.
- Cost 2 assumes the rebuilt banks owe gold dollars. `L1589` says "a stabilization agency lends it on to the rebuilt banks", under the government's guarantee; the exchange loss may fall on the agency or the Treasury. Decide which.
- All seven costs fall on Japan, or on Julian's leverage. The reset has Pacifican costs the draft omits: Japanese cloth and consumer goods a fifth cheaper in the Realm's and the Concord's markets, Pacifican machinery a quarter dearer in Japan, and the precedent for the Union and Britain weeks before the conference. Giannini's objection is the only one named.
- Cost 6 and the calendar's 1933 row decide that China "will refuse any tariff renewal in May 1933" and that the banks pay the last instalment. Canon ends in 1932 and says only "no renewal is promised" (`L1706`). Keep these as expectations in 1932.
- `L1746 ("adjustable gold-dollar order")` is cited for the yen; that sentence is about the Union's currency.
- CR-086 B1 states the conference's rule: "A member names its own parity and consults before it changes it." The draft calls `C-1932-ADJUSTABLE-PARITY` "the one parity instrument". Say in one sentence that the yen's band is the Concord's stricter case of the conference's rule.

**S8. Rice (D1) against CR-082 and `population/provisioning.py`.** The three targets agree with the model: 5% of 50.1 is 2.5, 8% of 57.5 is 4.6, 13% of 60.3 is 7.8, giving 68.1 against a need of 68.4 (provisioning.md §5). The mechanisms have five problems.
- The draft adds Hokkaido's whole crop to the increase. For 1910: "Hokkaido paddy ... ~1.5–1.8 million koku ... with Tōhoku selection, Chilean nitrate, and Manchurian bean cake supplying the remaining ~0.7–1.0 million koku to clear +5%". History's 50.1 million koku already contains Hokkaido's historical crop. Only Hokkaido's excess over history counts, and that is perhaps a million koku in 1910 and well under a million in 1932, when Hokkaido historically grew about three million koku in a normal year (from memory; not checked). The draft's own list of unverified items includes "exact Hokkaido paddy acreage by decade".
- D1.3 says "Keeping Japan's ~1.38%/year Meiji growth pace lifts the 1932 domestic crop to ~68.1 million koku". In the model that pace from history's 1920 crop gives 67.8 and leaves a gap of 0.5. From the draft's own 1920 crop (62.1) the same pace gives 73.2. The draft's figures imply growth of about 0.8% a year after 1920. Say which.
- Chilean nitrate on paddy. Nitrate is a poor nitrogen source for flooded rice because it is lost by denitrification (see History checked). Japan's historical paddy fertilisers were fish meal, bean cake and later ammonium sulphate. Put the nitrate on upland crops and mulberry, or drop it and let bean cake and, after 1908, cyanamide and ammonium sulphate carry the 1910 and 1920 figures.
- "Manchurian soybean cake moving at open rates (`CR-081`)" before 1910: CR-081's rate rule belongs to the joint management and the Huludao crop article of 1923 (AGENTS.md summary). Cite what carries the cake in the 1890s.
- "In canon, Pacifica's 1890 food table reverses its Hokkaido advisers' skepticism by 1893" and `C-1893-HOKKAIDO-RICE` "reversing Pacifican advisers' earlier opposition". `L735` says only "Kuroda Kiyotaka's Hokkaido development brings Pacifican advisers north". Canon's advisers never opposed rice; the draft transfers Capron's historical opinion to them without saying it is new. The food table of 1890 is also "read as a limit" under Victoria (`L1020`); the draft should say why a regency of sufficers spends on a partner's rice.
Two smaller points: Noguchi buys the Casale licence in 1921 "(*Hist.*)" in a world where Pacifican ammonia has been licensed "to any firm ... at the same published royalty" (`L863`) since 1915; and early northern rice raises the cost of cold summers (the draft mentions 1931 only as Korea's buffer).

**S9. The pool-entry protocol (B2).** It now gives something real in kind: orders, alumina contracts and majorities on a fixed day. It is still unquantified: "a stated share of the common fleet's and the Concord grid's orders" states nothing. Without a figure or a formula Ryan loses to a promise to agree later. Other gaps:
- `L1600` lets Japan build from 1937 anyway. The protocol's gift is the order book and the price, and B2 should say so.
- "Joint smelting and refining ventures outside Japan": where, and on whose power.
- "`CR-084`'s Bintan bauxite feeds these ventures after 1935": CR-084 C1 makes that bauxite "strictly *additional* tonnage on top of Arkansas bauxite" for the pool, and its ledger note says it "feeds Pacifica's pool". Agree the use with CR-084.
- "The first review found that a promise to lift the bar 'on renewal' gave Japan nothing": this is a reviewer's remark about an earlier revision, and in a draft about "the first review" of 1937 it reads as an event in the story.

**S10. The author's request section and the approval labels.**
- The two quotations of 21 November are in `CR-082.md` (lines 59 and 69) with the same times; verified. The six of 23 November are plausible in wording and timing; the reviewer has no record to check them against.
- T-R3's approval rests on "I agree with your canon changes except for the final one" (19:32). The words do not name the change. The draft says it is "item 3 of section 7 of the planning note", which this review may not read. The list of changes should be quoted in the CR so the approval can be read without the note, and the CR should say which was "the final one" and that nothing in this draft depends on it.
- The status line says T-R3 is "decided by the author"; Decisions P-0 says "APPROVED in direction". Use one.
- "1. Approved" (20:11) is honestly handled: the draft quotes its own question. It covers Navy seat by treaty law, pool entry and the tariff board. It does not cover the Kansai station (which T-A1 Case B bundles in: "and commits the Kansai 80 MW station"), the Joint Materials Board (bundled into T-M4 Case A), the 49% ventures or the dated form of pool entry written in revision 3. The tensions say "Decided" while Decisions P-1, P-2 and P-4 say PROPOSED; the table is the safer statement and the tensions should match it.
- A5 says: "This is what 'co-hegemonic' means in 1932." The word is in quotation marks and appears in none of the author's quoted words. Source it or remove the marks.
- The 19:16 words ("a renunciation agreement and the food order") support A5's direction only; A5 is correctly PROPOSED.

**S11. The sufficers' winter warning (A1).** It is a good frame, with three weaknesses. The sufficers are defined by "rich and few" and the water's limit (`L1020`); why they, rather than the Navy or Tate, count coercive levers needs a sentence (for example: a Realm that buys its bread abroad must not also depend on a partner who can walk away). The Batavia Compact is "initialled June 1932" in CR-084, so in the winter it is a negotiation. And Takahashi in the winter "asks the common Finance minister for fresh dollars" (`L1695`); the adjustable parity is his later answer.

**S12. The reviews are still dates.** The court's reason is to "give its enemies no more dates". A review every five years with "the quota, the seats, the pool shares and the parities" open is a date. The draft should let someone say what a failed review means: the old terms continue. Without that sentence the renewal without term can deadlock in 1937.

**S13. The Tokyo and Kansai stations (C1, C2).** "80 MW" for Tokyo is PROPOSED in canon (`L1634`, `L1869`: "the Tokyo station's size"); the draft treats it as settled and builds Kansai "of the same size". The coal-parity formula has an "agreed Concord discount" that is OPEN, so the tariff is not yet a formula. The Council of the Seal "authorizes" the Board; say who sits on it in 1932 (canon gives its composition for 1917, and the Chief's term ends in 1927). Tokyo Dentō's part is plausible and unverified, as the draft's own Sources admit.

## Minor

- M1. A6 cites `L1595 ("joins co-equal crowns")` for the 65/35 quota; the quota is at `L1597`.
- M2. A3 cites `L1593 ("Diet votes its quota")` for June 1932; that sentence is about 1927.
- M3. C1 cites `L1634 ("station is opened on 29 April 1932")` for ground broken in 1928; the phrase is "Ground is broken in 1928".
- M4. A4: "The four returns of revision 2 stand". A reader of revision 3 has no revision 2; the sentence then lists them, so drop the reference.
- M5. The Joint Materials Board appears in the calendar, the ledger list, T-M4 and P-1, and nowhere in Part A. Describe it once or drop it.
- M6. New instruments use `PAC`, `JP` in some places and `CROWN`, `JP` in others; CR-086 uses `CROWN` for the Concord's acts.
- M7. A5 gives the pledge as "never to use the weapon against a signatory"; CR-086 C1 has "against a signatory that keeps the article".
- M8. D1: "succeeding Zusho Hirotake". Zusho was the college's first president in the 1870s; Satō's immediate predecessor in 1891 was someone else (from memory: Hashiguchi Bunzō). Drop the clause.
- M9. The `add_forbidden` pattern for the rice riots forbids "Rice Riots erupt/break out ... in Japan" in any year and for any cause. CR-082 says only that there are none "from shortage"; riots over price in a year of war purchases stay possible. Narrow the pattern or say there are none.
- M10. D4 gives the Kamchatka Company "a 20-year renewable charter (1927–1947)" inside a paragraph headed "remains PROPOSED"; mark the term itself PROPOSED in the ledger line.
- M11. A6's two figures: "Mouths fed, 0 new in the Realm" is right; "Japan's 62.2 million residents ... are fed by their own crop" overstates a crop "within ~1%" of need plus Formosan and Korean contracts.
- M12. The title of section B and several ledger lines keep "Graduation" and "Mid-1937"; harmless, but they date from the term.

## The PROPOSED items

- **P-0 (renewal without term), the form.** Keep the decision; change the form. Add what happens when a review fails (S12), the Senate's vote (B1), and consider giving each crown a way out that is slow and public (for example denunciation on two reviews' notice, ratified by its own legislature). A union with no exit at all confirms the Restoration charge and gives the next conspirators a better grievance than a date. Case A is not stated at its strongest: it is given only as "five years from a possible dissolution", and the middle course canon itself points to ("a five-year first term instead of ten", `L1604`), a long second term, is not offered. The author has decided, so this is for the record.
- **P-0a, the winter warning.** Keep, with S11.
- **P-0a, Kansai announced on 29 April.** Keep the beat; fix the sequence (B3).
- **P-0a, the proposal comes from Japan's court, carried by Chichibu and Chiyo.** Keep. It uses `L1651` and `L1722` correctly and gives Chiyo the mirror of 1931. Change: name the advisers and the prime minister (S2), give Chiyo a medium and dates (S1).
- **P-0a, the Council in late May.** Change to dated days or early June (S1). Canon sets no month for the annual Council, so nothing forbids May.
- **P-0a, the common Navy minister silent between two loyalties.** Keep. It is the best new character note in the draft and matches `L1597`. He needs a name (OPEN in the draft).
- **P-0a, the named objectors.** Keep King, Ryan and Wigner with S5's changes. Change Tate (state his standing after 1928 and his age). Reduce Giannini's defeats across the suite.
- **P-0a, Julian refused on the home army.** Keep. It is canon's sentence (`L1734`) turned into a refusal with a reason, and the reason is good.
- **P-0a, custody outside the common Navy.** Change as in B4.
- **P-0a, the Common Tribunal's ruling.** Drop, or list as a tension (B1).
- **P-0a, A5.** Keep the two costs ("What it costs Japan", "What it costs the Realm"); they are the most valuable lines in Part A. Change "party to the monopoly" (B4).
- **P-1, Navy seat by law, Materials Board, quota and audit.** Keep the seat. Keep the joint audit and the refusal of an automatic link; `L1595`'s own reason ("because Pacifica pays the larger quota") makes the audit dangerous to Thalassia, and the draft should let someone see that. Describe or drop the Materials Board.
- **P-2, CR-054's four items and pool entry.** Keep Baton Rouge, the 1927 draft and 1928 adoption, and Nagoya and Ōta. Change pool entry as in S9 and correct "third-term renewal".
- **P-3, the yen.** Keep the instrument and the seven costs; change the labels and add the Realm's costs (S7).
- **P-4, financing, the Board, Kansai.** Keep the split financing; it closes `L1634`'s OPEN sensibly and keeps gold at home in 1927–28. Keep the coal-parity idea, which answers the Restoration charge without opening the seal. Change B3, S13.
- **P-5b, rice mechanisms.** Keep the Ainu land cost (it uses `L729`'s own quarrel) and the Korean landlords' grievance. Change the arithmetic and the nitrate (S8).
- **P-6, warnings, cable, Kamchatka.** Keep. The directions of the warnings agree with `L1131` and `L1659`, and the Wusong shore end is a neat use of Fong. Okada's use of the Tokyo machine matches `L1631` ("computes typhoon tracks for Japan's coast").

## Literary effect

The turn is right for the ending asked for, and A3's central sentence earns it: the Concord "should give its enemies no more dates". The two short paragraphs on what Article II costs each side are scenes in waiting. The home army refusal gives Julian a loss with a reason spoken by the other side.

The weakness is that Part A is mostly a term sheet with losers attached. The table's third column names a Pacifican who "objects, and loses" for every row, in the same grammatical slot, and none of them changes anything except Wigner, who is given what he already had. Nobody on the Japanese side is a person except Chiyo and Chichibu, who carry, and the Navy minister, who is silent. The court, the Diet, the army ministry, the Privy Council and the villages have no faces. The men who struck in May had public sympathy in history and have a manifesto in canon; here they vanish after one clause, and the renewal they died to stop becomes permanent without a voice raised in Tokyo. A triumphant ending is stronger if someone the reader respects in Japan pays for it in the open.

Japan "offers it before it is asked" removes the negotiation from the book's last negotiation. That can be the point, but then Julian needs a reaction that costs him something. At present he "accepts" for five returns. A man who was told all winter that "a partner held only by levers is not a partner" and is then handed a partner with no exit should hesitate, and the sufficers who warned him should be heard again in May, not only in the winter.

Victoria's absence is the largest missed chance. The term is hers. A sentence in which she declines to defend it, or defends it once, would tie this CR to `L1604` and to her "one last bargain" (`L1738`).

Parts B to D are dossiers and are written as such; that is acceptable for deferred items. The from-below candidates in F6 are good, especially the Shanghai mill-owner and the Ainu elder; the petty officer "on the morning his carrier does not sail" belongs in Part A.

## History checked

**Confirmed**
- Takahashi Korekiyo: Finance Minister from 13 December 1931, off gold in December 1931, acting Prime Minister 15–26 May 1932. https://en.wikipedia.org/wiki/Takahashi_Korekiyo
- Commercial Pacific Cable Company: 50% Eastern Telegraph, 25% Great Northern, 25% Commercial Cable; Manila–Shanghai cable laid 1906 with *CS Silvertown* (and *CS Store Nordiske*). https://en.wikipedia.org/wiki/Commercial_Pacific_Cable_Company
- Manila Observatory: founded 1865 by the Jesuits, typhoon warnings from 1879, official recognition 1884, Faura its founder. https://en.wikipedia.org/wiki/Manila_Observatory
- Noguchi Shitagau: 26 July 1873 – 15 January 1944; Nihon Chisso Hiryō formed 1908; Casale licence bought 1921. https://en.wikipedia.org/wiki/Shitagau_Noguchi
- Mori Nobuteru: 21 October 1884 – 1 March 1941; founded Nihon Yōdo (later Nihon Denki Kōgyō) and Shōwa Hiryō; ammonium sulphate and aluminium by domestic technology. https://www.ndl.go.jp/portrait/e/datas/580
- Okada Takematsu: 17 August 1874 – 2 September 1956; head of the Central Meteorological Observatory from 1923. https://www.ndl.go.jp/portrait/e/datas/4136
- Hokkaido rice: Nakayama Kyūzō and *Akage* in 1873 at Kitahiroshima; Hokkaido's breeding programmes from 1915. https://www.jstage.jst.go.jp/article/jsbbs/69/3/69_19062/_html/-char/en
- Hokkaido rice: Capron's team judged the island unsuitable for rice; test plots near Sapporo in 1893; *Bōzu* by selection, *Hashiri-bōzu* by crossing in 1913–1925. https://d-arch.ide.go.jp/je_archive/society/wp_je_unu22.html
- Zusho Hirotake was the first president of Sapporo Agricultural College. https://en.wikipedia.org/wiki/Sapporo_Agricultural_College

**Wrong or doubtful**
- "Chaotic ~60% yen drop": doubtful as phrased. The fall was about 30% in the first month; it reached the order of 55–60% only by late 1932 (the later figure from memory). https://www.nber.org/papers/w2683
- Chilean nitrate raising paddy yields: doubtful. Nitrate is "an inefficient source of N for submerged rice culture" because of denitrification. https://oar.icrisat.org/id/eprint/3968/contents
- The draft's two sources disagree on the pioneer's name: the IDE page has "Kyuzo Yamanaka", J-STAGE has Nakayama. Nakayama is right (from memory); cite J-STAGE for the name.
- The Manila Observatory page cited does not give the date 7 July 1879, Algué's directorship from 1897 or the barocyclonometer. They are probably right (from memory) but are not supported by the URL given.
- The same J-STAGE and IDE pages do not give a release year for *Fukoku* or say the agency opposed rice "until" 1893; the IDE page says it retracted its criticism after the 1873 trial and opened test plots in 1893.

**From memory, not checked on the web**
- Showa Fertiliser founded October 1928, ammonium sulphate 1931, first domestic aluminium at Ōmachi in January 1934: consistent with what I know; the draft's source (the-shashi.com) was not opened.
- Satō Shōsuke 1856–1939, first president of Hokkaido Imperial University 1918–1930; Ōmori Fusakichi 1868–1923; the Sanriku tsunami of 15 June 1896; the Emperor's birthday on 29 April; the Diet's extraordinary session of June 1932; Mitsubishi's aircraft works at Nagoya and Nakajima's at Ōta; Hercules Powder's wartime kelp plant at San Diego; Japan's historical paddy fertilisers; Hokkaido's historical crop of about three million koku about 1930.

**Not checked**
- The 1899–1900 landing-rights agreements of Eastern Extension and Great Northern in China (the draft also lists them as unverified).
- Tokyo Dentō's finances in 1927–28; Kansai utilities; Hokkaido paddy area by decade; Hayami and Ruttan's rates (taken from `population/data/provisioning.toml`, which marks them verified).

## The four drafts together

- **CR-086 D5 against CR-085 A6 (contradiction).** CR-086 puts "the renewal without term" among "the season's bills" on which the aliʻi seats set a condition. CR-085 removes it from the Senate by a Tribunal ruling. See B1.
- **CR-086 D5 against CR-085 A5 (contradiction).** CR-085: "The provisioners in Julian's cabinet see this and accept it; the sufficers count it as a gain." CR-086: "The provisioners in the cabinet, Elwood Mead among them, would keep the rule as a practice and not as law", and Mead loses on the form. CR-086 owns Article II; CR-085 should say the provisioners object and point to D5.
- **CR-086 T-5 and CR-085 A4 (double use, and custody decided nowhere).** King loses on the pledge in one and on the Navy seat in the other, in the same weeks. Custody of the devices is proposed in CR-085 and assumed in CR-086. Decide it once.
- **CR-086 B1 and CR-085 A7 (two parity rules).** Compatible, but neither mentions the other. See S7.
- **CR-084 line 50 and CR-085's calendar (timing).** CR-084 says its four Concord treaties are "agreed at Hayama". CR-085's late-May Council lists what it agrees, and they are not there; Britain's cabinet decides only "in the last week of June" (CR-084 B5), and the Batavia Compact is initialled in June. Either the May Council agrees the Concord's position on them or CR-084 should not cite Hayama.
- **Ratification dates.** CR-085: delegations and crowns ratify in "June–July 1932". CR-084's calendar: "July – Aug 1932 ... Concord delegations ratify the Concord instruments at Thalassia". CR-086: the Final Act of 1 August annexes "the renewal of the Concord without term". Agree one month.
- **Bintan bauxite.** CR-084 keeps it as additional tonnage for Pacifica's pool and "respecting the 1937 Hayama Annex bar"; CR-085 B2 feeds it to the 49% joint ventures. See S9.
- **Does CR-085 decide what belongs to CR-084?** No. The piers, the 10° S line and the southern question are recited at A4 ("What Japan is refused"), D4 and draft line 312, and decided nowhere. A1 and A4 lean on the Batavia Compact as already given, which is safe only because CR-084 merges first.
- **Does CR-085 decide what belongs to CR-086?** Mostly not. A5 restates the pledge and Article II in its own words (M7) and adds two consequences that are properly Japan's place: "Japan may embargo no signatory in peace, China included" and the Realm's loss of food as a weapon. The second is a statement about Article II's effect on the Realm and should be worded as CR-086 D5 words it.
- **CR-083.** No contradiction found. Its resale of prairie wheat "to Japan and China" (A11) is consistent with a Japan fed in rice by its own crop, if CR-085 says "rice" where it says "fed".
- **Giannini and Tate** are the standing losers of CR-084, CR-085 and CR-086. See S5.

## Impact notes missing

- `L1736` (Vance's death in May, PROPOSED): not listed. It bears on A1 (the transports are the last lever, and he executed the prohibition) and on the timetable.
- `L1738` and Victoria: the term of 1928 was her settlement. No note, and no line in `character_bible.md` for her.
- `L1754` ("The Concord holds") and `L1756`: the closing summary should say the Concord is without term.
- `L1655` ("Restoration officers attack that future"): listed, but nothing in Part A says what becomes of the betrothal sentence in `L1734` ("The betrothal's marriage can proceed, but Japan may refuse in 1937") once its second half is removed.
- `L1677` and `L1732` on Maria Kashiwagi and Kiyoshi's son: Part A leans on his loyalty as the Navy's claim to the seat; no note says whether he is rewarded, or is the unnamed Navy minister.
- `L1593` and the Privy Council's conditional advice of 1927: what its advice is in 1932.
- `L1597` ("reviewed at every renewal"; "At least one must be Japanese by law; convention gives Japan the Navy"; "The western squadron is reserved ... until the 1932 renewal"): listed for the Navy seat, not for the wording of renewals.
- `L1604` ("five-year first term instead of ten", "quota review at renewal"): listed only for the audit.
- `L1600` ("before 1937") and ledger `C-1928-HAYAMA-ANNEX` (`until = 1937`, "the end of the Concord's second term").
- Ledger `C-1927-CONCORD` (the conditions of 1928, `renewals`, `can_end`) and `C-1927-CONCORD-RESERVES` ("reviewed at every renewal").
- `character_bible.md` lines 126, 128 and 137 (see B2); bible entries for King, Ryan, Wigner and Giannini if their objections stand; the unnamed common ministers.
- AGENTS.md line 68: "five-year Concord executive term", beside the sentence already listed.
- `L1746` and `L1748`: how the yen's instrument sits inside the conference's monetary settlement (S7), and that "Japan and China attend from the standing alliance" while Japan now co-guarantees Article II.
- `L1720`: the note at draft line 213 must be corrected, not only added (S6).
- `L1541` and `L1695`: the Crown's granary "takes ten-year contracts abroad for beans and rice"; if Japan's home crop covers its table rice, say whose rice the granary's contracts and Formosa's long contracts now move.
- `L1625`: listed for 29 April; add the rule that state business goes by cable, for Chiyo's errand.
- `L1634` and `L1869`: the Tokyo station's size is still PROPOSED and open; the draft fixes Kansai to it.
- `historical_background.md`: the reasons for the divergences on Hokkaido rice, the yen and the Manila–Shanghai cable belong there (AGENTS.md, "Mandatory on author approval"); the draft lists the file but not what goes into it.
