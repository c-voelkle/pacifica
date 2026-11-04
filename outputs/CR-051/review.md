# CR-051 — fresh-context review (3 November 2026)

Independent reviewer, given CR-051, CR-049, CR-050, CR-050-R1, the earlier atomic review and both reference texts; no access to the drafting conversation.

# CR-051 review: the industrial lead, the secret and the arc's weak points

## Verdict

CR-051 makes the right strategic move. Basing the lead on two hard facts plus an industrial plant, instead of on fission staying secret, answers the review's main objection, and most of its sources are used honestly: 41 of the 47 citations I checked are correct. What still fails sits in three places:

- **The production model contradicts itself.** Weapon-grade output starts before the second stage exists, and the feed plant's benefit is overstated against Norris.
- **The 1924 test cannot be both announced in true words and misread abroad as chemical**, given what Europe already knows by then.
- **The 1947 seal has no binding mechanism.** Canon ties the bonds and both compacts to a term ending in November 1928.

Several leftovers from earlier rounds also need sweeping up: status labels that no longer match the register, an O'Shaughnessy paragraph that puts the Chief in charge before he exists, and a contradiction in Rutherford's timeline. None of this touches the approved direction. All of it can be fixed with small edits.

---

## MUST FIX

**1. M2 table: weapon-grade output before the second stage exists.**
- The Scale bullets say a second stage of smaller halls is needed "to finish the product", and the table dates that stage to 1923.
- Yet the same table shows "first weapon-grade product" in 1921 (about 8 kg) and about 2 kg a month in 1922.
- At Y-12 the Alpha tracks only partly enriched. Weapon grade needed the Beta stage (Norris p. 202).
- The scale text also says twice Y-12 is "reached by 1925", but the table says 1924.
- **Fix:** bring a small Beta stage forward to 1920–21, or relabel the 1921–22 output as partly enriched and push the first weapon-grade material to 1922–23. The test device can still be ready at the end of 1923. Align 1924 and 1925.

**2. M1: "The halls' output rises several times over" overstates what Norris supports.**
- Norris says the S-50 product was "slightly enriched" and gave "a significant increase in efficiency" as feed (pp. 364–365, 367).
- Little Boy's 64 kg came only after K-25's roughly 23 per cent product went into Y-12 (p. 367).
- The same paragraph says S-50 was "built in 66 days". Norris says one-third of the plant was complete after 66 days, enough to begin preliminary operations, and the plant "had not been fully completed" when it was scrapped (pp. 366–367).
- **Fix:** say the columns raise output "by perhaps a fifth to a half". If the M2 rates are to stand, either make the thermal-diffusion plant a long cascade at a very large steam cost (S-50 needed the K-25 powerhouse, p. 365; that plant was 238 MW, p. 206), or bring M4's gaseous diffusion in as feed earlier. Then re-derive M2 (see item 12).

**3. S5/S6: Europe cannot plausibly read the 1924 statement as a chemical explosive.**
- By May 1924 Europe has had fission since 1920 and neutron multiplication since 1921.
- It has the 1922 *Tribune* story about a Station that will "blow a battleship out of the water".
- It has an SIS file.
- The Light and Matter Works, an atomic firm, then announces "an explosive of a new kind and very great power", seen as far as Gerlach and recorded on seismographs. Yet Tizard's file stays closed, and T2's memo appears later for no stated reason.
- **Fix:** let the statement reopen Tizard's file and prompt Fowler's memo. Disbelief then rests on the second hard fact, which is what P1 wants. Lindemann argues that the separation factory is impossible, so the shot must have been a large chemical charge or a publicity stunt. The Treasury declines on that advice. This also gives T2 its trigger.

**4. L2 (approved, 1947): the canon tensions are not listed and there is no binding mechanism.**
- CR-050 S3: the bond holds "for its term", which ends in November 1928.
- CR-050-R1 B4: the Compact of the Tuolumne runs "to November 1928, renewable", and clause 10 gives Ralston College an exit right.
- CR-050-R1 B3: the Me-Wuk lease runs "for the seal's term".
- CR-050 S3 also uses the "promised opening" as the defence against a Fuchs-type idealist. Extending the secret to 1947 removes it at the moment Szilard is pressing for an end.
- The tension section (T5) mentions only G5.
- **Fix:** list these tensions. Add a 1927 re-bonding: Part II is a new deposit with new signatures, a pensioned exit for anyone who refuses, and the renewal of the Compact and the Me-Wuk lease. Make Szilard's and Victoria's reactions explicit.

**5. C2: superseded chronology.** "Under the Chief he builds" the survey line and railway of 1908–13, the tunnel and spur, and Eleanor–Cherry. The Chief arrives in 1917, and the phase table rightly puts O'Shaughnessy under Hillebrand in that period. **Fix:** "Under Hillebrand (1908–17), and then under the Chief, he builds…"

---

## SHOULD FIX

**6. Labels and IDs left over from earlier rounds.**
- The C3 heading says "(PROPOSED)"; the register says APPROVED.
- The S7 heading says "(PROPOSED; site OPEN)" and its Power subsection says "(PROPOSED)"; the register says APPROVED.
- The status line still says "second round", and line 7 still says the Chief's identity is OPEN.
- The C1 identity paragraph still says "(outside the texts, to verify)".
- The canon-tension IDs T1 and T2 collide with the decision IDs T1 (signposts) and T2 (the memo), and they run T1, T2, T8, T9, T10, T3 and so on.
- The fact pattern `pacifica-record-part-two-sealed` has no `(?P<year>…)` group, unlike every other pattern. It may fail `cr_facts.py`.
- The heading "S1–S7" omits S8.

**7. Rutherford is inconsistent.**
- E5 cites his 1913 proposal to leave nuclear theory to the next generation (Stuewer p. 22). E6 has him publish a nuclear-structure model in 1912 that becomes Europe's textbook prohibition. One has to go, or be reframed, for example: having published his model, he declares nuclear theory settled.
- The T1 table and S4 (1922) turn "moonshine" into a verdict on "power from the atom". CR-050's integration note limits it to power from fusion. It also cuts against T1's own target conclusion, "power one day", and is hard to believe once Europe has measured multiplication in 1921. Restrict it to fusion, or to "a bomb is moonshine".

**8. Hoover: a canon tension that is not listed.**
- Canon (CR-020 B5 and B6, CR-021 I7) has Hoover running the 1927 flood relief, issuing the June 1931 moratorium, and fronting the 1932 Union rescue.
- C3 puts him at the head of the ore office from 1920 with no end date, and in the sealed record in 1926.
- **Fix:** give him an exit, for example to public office about 1925–27, and list the tension. An inner-circle man who becomes a public figure is also good drama.

**9. Other tensions missing from the list.**
- CR-050-R1 B4 ("the cut-off of December 1908 shows how quickly they can stop") and CR-050 X4 both depend on the cut-off that E2 replaces.
- CR-050 U1 says the light-isotope lead "lasts until … the mid-1920s". The E1 table has Bohr reaching it in 1920–21, and the CR's T6 covers only K1.
- The review's §6 question goes unanswered: once actino-uranium is a live question in 1920–21, Dempster's survey published without uranium becomes a conspicuous gap. Say what Dempster answers when he is asked.

**10. E4 and the nomos.** Pacifica co-published the transuranic error of 1902–07 (CR-049). A Nobel Prize for that error, which the Works knows to be false, and possibly with Pacifican co-nominees, strains the corrections custom and the rule "never a false word". **Fix:** one sentence in which Hillebrand withdraws his group from consideration "pending verification", which is true, and the prize goes to Paris alone.

**11. The plutonium route.** The "two hard facts" framing ignores element 94. Europe's piles could reach a weapon without industrial separation. Canon gives Europe heavy hydrogen through Dempster's published survey (CR-050 X2), and Norsk Hydro already runs large electrolysis plants. T1 or L3 should say why Europe has no pile and no element 94 before 1932: the graphite error, no heavy-water production, and element 94 unknown outside the wall.

**12. The M2 rates (MODEL) and power.**
- Y-12 had about 8 kg of *enriched* uranium by Christmas 1944. It reached 64 kg by July 1945 only with K-25 feed (Norris pp. 364, 367).
- 7–10 kg a month of weapon-grade material from 1920s halls on thermal-diffusion feed means matching or beating Y-12's 1945 performance per unit with 1920s vacuum and valve technology.
- **Fix:** either take about 4–6 kg a month as the central case (three devices and the test still fit by 1927), or add the feed described in item 2.
- On power, twice Y-12's electrical draw in 1924 is probably a large share of the Pacific coast's generating capacity of the period. Compute it before relying on the halls "hiding" in the electrochemical district.

**13. C1, Sibert.**
- (a) The CR has him building the Atlantic locks "from 1889", at 29. Historically he took over Gatun at 47. **Fix:** he joins in 1889 and commands the Atlantic division from about 1895.
- (b) The register calls him "chief engineer at the siege"; the body says he "commands the Pacifican engineers in the combined siege". Kamio commanded the siege, and Japanese engineers would not serve under him. Use the body's wording throughout.
- (c) "Pacifica keeps at Tsingtao on lease (canon §30)": the lease comes from the 1919 settlement. In 1915–17 it is occupation.

**14. C5.**
- "German warships are interned at Honolulu" contradicts a Pacifica at war from 23 August 1914. Internment is what a neutral does; historically SMS *Geier* was interned there by the then-neutral United States in November 1914. Here the ships would be captured or would stay away.
- In the Villa question, the historical rail transit started in Texas (Eagle Pass), and Texas belongs to the Gulf Republic in canon. The Gulf is party to the decision.

**15. C6 and Ralston College admissions.** "Who is admitted to the inner circle: the Works' director" conflicts with Compact clause 2: Ralston College nominates its own people, and Carquinez can veto only on the bond. Add "subject to Compact clause 2".

**16. The Columbia station is outside the secrecy design.** S1–S3 rebuild the valley's secret only. The Columbia station also holds secrets:
- the piles and the chemistry of element 94;
- a construction force of thousands;
- the existing towns of White Bluffs and Hanford, which have to be bought out.

It needs a line in S3 (population and attrition) and in S5 (what SIS could learn there).

---

## NOTE

**Citations to correct.**
- Sengier is not on Norris p. 192 (Murray Hill only). He appears on pp. 179, 183 and 325–326.
- "Lectured each other on why a bomb was beyond any nation": Badash pp. 174–175 says they *assumed* no other country could do it and lectured each other on the technical problems.
- The Cameron p. 196 "safety valve" quote is Egerton's note of what Bohr said ("as it were").
- The 1912 opening of the Kaiser Wilhelm Institute is in Shea p. 13, so it is not "outside the texts".
- "My reputation is made; yours is at stake" is Lawrence's retort to Groves (p. 205).

**Qualifiers for claims from outside the texts.**
- **Comstock silver:** about 7,000 t in total (LBMA). Norris's 14,700 tons are short tons, about 13,300 t, so the ratio is about 1.9 times. Say "nearly twice", not "more than twice".
- **Hoover at Tientsin:** he "helped build" the barricades and organized food and water, rather than "organized the barricades".
- **Rock Island:** about 12 miles below Wenatchee, built 1930–33 with two fish ladders and a third added in 1936. It is about 80 river miles above White Bluffs, not 90.
- **Paneth:** in Prague from 1913, Hamburg 1919, Berlin 1922, which matches the CR. But his radioactivity textbook with Hevesy dates from 1923. "Whose own textbook teaches it" needs an earlier textbook in this timeline, or a different source.
- **Tizard:** at the DSIR as Assistant Secretary from 1920 is correct. But he and Lindemann were close friends in the 1920s; their rivalry belongs to the 1930s.
- **Smohalla:** his teaching forbade ploughing and digging. Wanapum took seasonal wage work (HistoryLink). Reword the passage to say the compact never asks them to dig or build.
- **King:** historically correct (1910 graduate, resigned in 1924, governor 1953–57). In this timeline he would not attend Annapolis.
- **Correct as stated:** Ruff's uranium hexafluoride (1909, with Heinzelmann), the copper slump (26¢ in 1918 to 11.6¢ in August 1921), the siege of Tsingtao, and O'Shaughnessy's Hawaii work (1899–1906) and City Engineer dates (1912–32).

**Other.**
- L3: 1933–35 is 5–7 years, which is not "inside the range" of the historical 4–5 years. Say "comparable".
- "Churchill … watches the column of water": a sitting Chancellor in mid-Pacific in autumn 1927 needs canon confirmation. Otherwise make it the newsreel.
- M3: a Pacifican Mint holding "a few thousand tons" of silver needs a monetary reason under canon's gold standard. Norris's figure of 6,000 tons for Y-12's first request (p. 202) makes the quantity itself credible.
- "A second Hawaiian … besides Hillebrand": Hillebrand is Honolulu-born but not Native Hawaiian. The phrase is ambiguous.
- S1 gives no date for when the outer college leaves the valley, which matters because R1's valley opened in 1911 with both circles.

---

## Citations checked and found correct

**Norris**
- p. 192 (Murray Hill)
- pp. 202–203 (825 acres; 14,700 tons; copper shortage; silver recovered)
- pp. 203–205 (first racetrack failure; more than 90 per cent splattered)
- p. 206 (K-25's own power plant, because TVA power "might be subject to interruption")
- pp. 215–216 (three California sites failed)
- pp. 224–226 (Argonne; 504 tubes; plateau five miles from the river)
- p. 246 (Los Alamos growth)
- pp. 255–256 (Condon's colloquia, Greenglass, "wiring diagram")
- p. 286 (Alsos indicators)
- pp. 326–327 (uranium not scarce; vanadium tailings)
- p. 336 (oxide only; radium tailings kept by the seller)
- pp. 336–337 (the special fund)
- pp. 339–341 (State Department bypassed; Acheson; Maclean)
- p. 362 ("within half an hour")
- p. 363 (39–60 kg; Little Boy 64 kg)
- p. 364 (200 g; 8 kg by Christmas; Parsons)
- p. 365 ("Add a third method and combine them")
- pp. 368–369 (iodine-131)
- p. 371 (couriers; Gable Mountain vaults)
- pp. 401–402 and 406–407 (Trinity evacuation plan and cover story)
- p. 436 (Smyth Report)
- p. 470 (material for about thirty weapons)
- pp. 475 and 480 (Groves's forecast; low-grade ores)

**Shea volume**
- Shea p. 5 (Giesel's radium at $5 a milligram in 1903)
- Shea pp. 10–12 (Meitner's restrictions; first paid post 1912; von Baeyer)
- Stuewer p. 22 (Rutherford 1913; the war's toll), pp. 28–30 (satellite model; uranium paradox; nuclear electrons "pervaded physics")
- Kargon pp. 75–77 and 81 ("a billion", "a new world for man", "bust up", "birth cries")
- Weart p. 101 (Fermi's Nobel), pp. 112–113 ("laws" softened to "experience")
- Krafft pp. 137–139 (Bohr in November 1938; Heisenberg's "what" and "why"), notes p. 162 (radium–beryllium neutrons)
- Badash p. 168 (Knöfler; "German radium"), pp. 169–170 (gas warfare; tours in Berlin)
- Berninger pp. 213–214 (re-checking the 1914 measurements; actino-uranium hypothesis)

## Sources
- [Uranhexafluorid (dewiki)](https://dewiki.de/Lexikon/Uranhexafluorid)
- [Friedrich Paneth (Wikipedia)](https://en.wikipedia.org/wiki/Friedrich_Paneth)
- [Henry Tizard (Wikipedia)](https://en.wikipedia.org/wiki/Henry_Tizard)
- [Sibert, Alabama Authors](https://www.lib.ua.edu/Alabama_Authors/?p=2176)
- [Michael O'Shaughnessy (Wikipedia)](https://en.wikipedia.org/wiki/Michael_O%27Shaughnessy)
- [LBMA: Comstock and the end of the European silver standard](https://www.lbma.org.uk/alchemist/alchemist-107/comstock-and-the-end-of-the-european-silver-standard)
- [US House History: Samuel Wilder King](https://history.house.gov/People/Detail/16344)
- [HistoryLink: Rock Island Dam](https://historylink.org/file/21173)
- [HistoryLink: Wanapum after Smohalla](https://historylink.org/File/9524)
- [Siege of Tsingtao (Wikipedia)](https://en.wikipedia.org/wiki/Siege_of_Tsingtao)
- [SMS Geier incident (Wikipedia)](https://en.wikipedia.org/wiki/SMS_Geier_incident)
- [FRED: copper prices, New York](https://fred.stlouisfed.org/data/M0415BUS000NYM267NNBR)
- [Hoover Library blog: Tientsin 1900](https://hoover.blogs.archives.gov/2021/06/02/the-most-interesting-but-largely-forgotten-siege-and-bombardment-of-the-age)
- [Finest Hour: Lindemann and Churchill](https://winstonchurchill.org/publications/finest-hour/finest-hour-195/the-professor-and-the-prime-ministerfrederick-lindemann-and-winston-churchill/)