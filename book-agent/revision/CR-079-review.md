# CR-079 — fresh-context review

**Verdict.** The sound, television and music parts are well built and mostly agree with CR-077 and CR-078. The CR is **not ready to integrate**. T1 case C was added late and never carried into the rest of the text: Part C, P-2, P-8, the set pieces, the Registry and the Fact changes still read as if film begins with Dickson in 1895. Three canon facts are broken: Kolchak's government, Kalākaua's purse and the 1878 weekly. And the one succession canon says "matters in 1932" has no appointing authority. There are also about a dozen factual and wording fixes, most of them one line each.

---

## Blockers

**B1. Case C is missing from the Registry and Fact changes.**
- *Passage:* T1 "Cost: two new people, Muybridge (born 1830; dies 1904) and Le Prince"; the header "New people are kept to six, three of them optional"; Part M; `## Fact changes`.
- *Problem:* Muybridge and Le Prince are in neither Part M nor the JSON. T1 has no ```json block, which AGENTS.md ("Canon tensions") requires. Its fact changes (C1 moves from 1895 to 1889–90, and the storyline's "from 1895 W. K. L. Dickson ... gives it moving pictures", para 446) are not copied into Fact changes, even though the author decided C. The `add_event` list has no entry for projected film. The header's count of six new people is out of date: there are now eight, three of them optional.
- *Fix:* Add to Part M:
  - Eadweard Muybridge (CT-EADWEARD-MUYBRIDGE, born 9 April 1830 at Kingston upon Thames; dies 1904);
  - Louis Le Prince (CT-LOUIS-LE-PRINCE, born 28 August 1841 at Metz).

  Add to the JSON:
  ```json
  {"add_person": {"id": "CT-EADWEARD-MUYBRIDGE", "aliases": ["Eadweard Muybridge", "Muybridge"], "born": 1830}},
  {"add_person": {"id": "CT-LOUIS-LE-PRINCE", "aliases": ["Louis Le Prince", "Le Prince"], "born": 1841}}
  ```
  Also add an `add_event` for projected film (1889–90), with a pattern on the revised para 446 sentence (use `retire_forbidden` if the 1895 sentence is linter-protected). Change the header to "eight, three of them optional". Add the power timeline (CR-015) to "Depends on".

**B2. The rest of the CR still treats Dickson's 1895 camera as the start of film.**
- *Passages:*
  - Part 0: "From 1895 onward: W. K. L. Dickson ... gives the press seat moving pictures";
  - P-2: "the film unit, from 1895 (Dickson)";
  - Part C's Dickson paragraph: "comes to San Francisco in 1895 with a portable camera";
  - P-8: "Here Dickson's camera, the Latham loop ... and Lauste's track are licensed at one royalty from the start";
  - set piece 1: "1895: Dickson unpacks his camera at San Francisco".
- *Problem:* Under case C the press seat has projected film from 1889–90 on Le Prince's camera. The CR never says who runs the film unit from 1889 to 1895, or how Le Prince (fifty-four in 1895) and Dickson divide the work afterwards. As written, the Realm has two founders of its film and no one in charge.
- *Fix:*
  - Mark Part 0's 1895 line "amended by T1 C".
  - P-2: "the film unit, from 1888–89 (Le Prince; Dickson from 1895)".
  - P-8: "Le Prince's camera and projector, Dickson's Biograph-type camera, the Latham loop and Lauste's track".
  - Split the roles in one sentence. For example, Le Prince keeps the camera and projector works and Dickson runs production, the newsreel and sound. Le Prince retires at sixty-eight in 1909 under CR-038.
  - Replace set piece 1 with "1889–90: the first projected film at San Francisco". Dickson's arrival can stay as a minor beat.

**B3. There is no "Kolchak's government" in canon.**
- *Passage:* P-10 (a): "He is at Omsk in 1918–19 buying radio for Kolchak's government."
- *Problem:* CR-041 (AGENTS.md) says the Omsk coup of 18 November 1918 fails in a night, the Directory survives and Kolchak is a minister, later federal Russia's navy minister. The historical fact (Zworykin worked for Kolchak's government in 1919; [Wikipedia](https://en.wikipedia.org/wiki/Vladimir_K._Zworykin)) has to be translated into canon.
- *Fix:* "buying radio for the Directory's war and marine ministry (Kolchak's ministry) at Omsk". Kashevarov's Reserve Bank office at Omsk (CR-045) would be a natural recruiter.

**B4. Case C's money and agents in 1878 and 1887 break canon.**
- *Passages:* "Here Kalākaua, minister of the image, and the weekly pay for it" (1878); "Here the press seat's agents bring him to San Francisco instead" (1887).
- *Problems:*
  - The six-language weekly does not exist in 1878. Hearst makes it in 1887 (para 446), and the power timeline's weekly belongs to the 1887–1900 programme.
  - The bible says Kalākaua is "her minister of the image and envoy, never controller of the purse" (CT-DAVID-KALAKAUA).
  - In May 1887, when Le Prince left New York for Leeds ([Wikipedia](https://en.wikipedia.org/wiki/Louis_Le_Prince)), the press seat barely exists. Hearst took the *Examiner* in March 1887, and the Constitution and the estates begin on 1 August 1887.
- *Fix:*
  - 1878: "Kalākaua commissions it and the Queen's government pays (or the Laboratory of Light, Electricity and Matter)."
  - 1887: "Kalākaua's office brings him to San Francisco, and the press estate takes over his contract in August 1887."
  - The *Hist.* note also needs a word on whose horses Muybridge photographs, since Stanford is not in canon.

**B5. The 1931 succession has no appointing authority, and the "only seat" claim is unverified.**
- *Passage:* P-3: "Hearst reaches sixty-eight ... The press seat is the only one of the five to change hands in the last two years before 1932."
- *Problems:*
  - Canon gives the procedure: the named holders keep office for life, "after which the Regent appoints with Senate consent" (para 435). In 1931 that power is Julian's, as sovereign. The CR never says who chooses Lippmann, or why. This is the one choice the bible flags: "The successors' choice matters in 1932."
  - The "only one" claim cannot be checked against canon, which leaves the successors open: "Seats pass to successors such as Baekeland, Doheny, Giannini and Montgomery" (para 446). Baekeland was born on 14 November 1863. If he took the champions' seat from Doheny in 1924, he also reaches sixty-eight in November 1931.
- *Fix:* Add one line: "Julian appoints Lippmann with the Senate's consent in May 1931", with the motive (for example, he wants a critic of spectacle at the press seat during the 1931 crisis, or the reverse). Delete the "only one" sentence, or check every seat holder's birth year first.

---

## Fixes

**F1. Lippmann was not at Harvard in 1913.**
- *Passage:* "Hearst hires him from Harvard in 1913."
- *Problem:* Lippmann took his B.A. in 1909. *A Preface to Politics* came out in 1913, and he helped found *The New Republic* in 1914 ([Britannica](https://www.britannica.com/biography/Walter-Lippmann)). In 1910–13 he was a journalist and political secretary in Boston, New York and Schenectady.
- *Fix:* "Hearst hires him from New York in 1913, after *A Preface to Politics*." He is twenty-four, which is worth stating.
- *Also:* "when Julian's information is canon's weakness (§36)" misquotes canon. The line is "its confidence in its own information remains a weakness", and it describes Pacifica, not Julian (CR-078 §0). Quote it correctly.

**F2. Jensen's patent date, the crowd size and the public-address date.**
- *Passages:* "their patent was filed in 1911"; "a crowd of about 100,000"; "a public-address set in 1913".
- *Problems:*
  - The Pridham–Jensen moving-coil patent (US 1,105,924) was filed on 20 August 1913 and granted on 4 August 1914 ([Google Patents](https://patents.google.com/patent/US1105924)). The company was founded at Napa in 1911, and the speaker was built in 1915 ([Wikipedia](https://en.wikipedia.org/wiki/Peter_L._Jensen)).
  - Wikipedia gives 75,000 for the crowd of 24 December 1915, and [other accounts](https://cfuttrup.com/dpc/inventor.htm) also say 75,000. Write "75,000–100,000".
  - In 1909 Jensen's employer was the Poulsen Wireless company (Federal Telegraph from 1911).
  - P-4 also moves the planning note's own working date for public address (§4 C6, "about 1915", which §9's "What it moves" assumes) to 1913. T4 corrects only the *Hist.* column.
- *Fix:* Correct the *Hist.* lines. Add to T4: "the Pacifican date also moves from about 1915 to 1913."

**F3. Families cannot listen through a loudspeaker in 1913.**
- *Passage:* Part I: "Families listen together through the loudspeaker from 1913."
- *Problem:* Valve receivers become household goods only "from about 1914" (CR-077; storyline para 530), and the planning note §9 says "valve sets from about 1915". A crystal set cannot drive a loudspeaker. The 1913 date also contradicts P-5's "from about 1915".
- *Fix:* "from about 1915. Before that, the loudspeaker is heard in halls, theatres and squares."

**F4. The air school did not teach languages in CR-078, and Kalākaua did not revive Hawaiian.**
- *Passages:*
  - P-12: "the air school's Hawaiian lessons follow in 1916 (CR-078)";
  - P-17: "The air school's language lessons, broadcast from 1915–18 (CR-078), prepare listeners for the language examinations";
  - P-17: "The language Kalākaua revived".
- *Problems:*
  - CR-078 I3 broadcasts the *examination lessons* in English and Spanish, then Hawaiian, Japanese, Tagalog and Cantonese. Those are lessons given in each language, not lessons that teach it. P-17's tongue-vote mechanism rests on a function CR-078 never approved.
  - Kalākaua revived hula and chant (bible, CT-DAVID-KALAKAUA). Hawaiian was a living language, and Victoria funds the Hawaiian-language schools (bible, CT-KAIULANI).
- *Fix:* Make it new canon under CR-079: "From 1916 the air school adds hours that teach Hawaiian (and the other listed tongues) for the certification." Change "The language Kalākaua revived" to "the language of the Society's schools".

**F5. The date of "Confederation Day", and who owns Elias's cylinders.**
- *Passage:* P-19 and set piece 2: "from 31 July 1913 the founder's recorded voice is broadcast each Confederation Day."
- *Problems:*
  - No Confederation Day appears in the supplied canon.
  - 31 July is Lā Hoʻihoʻi Ea. Canon dates the 1889 rising by it (para 440: "On 30 July 1889, the eve of Lā Hoʻihoʻi Ea"). Elias's voice on the Hawaiian restoration day would be a provocation the CR does not mean.
  - The Realm's own date is 1 August, when the Constitution began in 1887.
  - The CR never says who holds Elias's cylinders or who consents to broadcasting them. That decides whether set piece 2 shows Victoria's helplessness, or a decision Julian made over her.
- *Fix:* Choose 1 August, or an existing holiday, and check the full storyline. Add one sentence on ownership and consent. For example, Victoria holds the cylinders, Julian asks for the copies, she agrees, and she then switches the set off. That puts a choice into the Julian–Victoria drift and explains the July 1913 timing a year before Julian's own broadcast.

**F6. Victoria's age in set piece 7.**
- *Passage:* "1931: the first television pictures at Honolulu, and Victoria, ninety-three, watches them."
- *Problem:* She was born on 1 November 1838 (bible, CT-KAIULANI), so she is ninety-three only from 1 November 1931.
- *Fix:* Date the Honolulu service to November–December 1931, or write "ninety-two".

**F7. Tape needs a different base, and three *Hist.* notes need correcting.**
- *Passages:* P-6: "Baekeland's works coat a plastic film with iron oxide"; "*Hist.*: Carlson and Carpenter at the US Naval Research Laboratory, 1921"; "the bias added, 1941".
- *Problems:*
  - Bakelite is a brittle thermoset and cannot be made into tape. Pfleumer used paper (1928) and BASF used cellulose acetate (1935).
  - The Naval Research Laboratory opened in 1923. Carlson and Carpenter's patent (US 1,640,881, filed 26 March 1921 at Washington) used high-frequency bias to receive radio telegraph on a telegraphone ([Google Patents](https://patents.google.com/patent/US1640881)). That supports the cipher-room use, so the CR should say so.
  - Weber rediscovered bias at the RRG in 1940. Camras's 1941 rediscovery was American ([Wikipedia, Tape bias](https://en.wikipedia.org/wiki/Tape_bias)).
  - CR-078 places the San Diego laboratory only in 1924–26 (PROPOSED). P-6 needs it in 1921, so state that it exists by then.
- *Fix:* "coat cellulose acetate film from the press estate's film-stock works with iron oxide." Correct the three *Hist.* notes. Add "(the laboratory exists by 1921)".

**F8. Kekuku's school dates.**
- *Passage:* "about 1885–89, at the Kamehameha School".
- *Problem:* The Kamehameha School for Boys opened in 1887. Wikipedia dates the discovery to 1889, at that school ([Wikipedia](https://en.wikipedia.org/wiki/Joseph_Kekuku)). Kekuku died at Morristown, New Jersey, which is irrelevant here.
- *Fix:* "about 1889". Canon reduces Pauahi's eventual holdings (bible, CT-KAIULANI), so confirm that the school still opens in 1887.

**F9. Jazz may come from the Gulf, not the Union.**
- *Passage:* P-13: "Jazz comes from the Union by record and over the air."
- *Problem:* New Orleans holds in 1863 (CR-059–070). CR-054 names Baton Rouge as a possible Gulf Republic refinery site, which puts Louisiana in the Gulf Republic. If so, jazz's first home is a partner country, not the Union.
- *Fix:* "from the Gulf Republic and the Union's cities." Beauchamp, born in Coleman County, Texas, is a Gulf Republic citizen by birth, so record that in his registry note.

**F10. Two lines contradict open licensing.**
- *Passages:*
  - P-9: "Sound comes to the Realm's cinemas a decade before the world's";
  - P-20: "Its television waits for Pacifican licences, since Zworykin and Farnsworth are both in the Realm."
- *Problem:* P-8 licenses sound film abroad at one royalty, and P-20 has the Union making talkies from about 1922. Under CR-057 a licence is never withheld.
- *Fix:* "a decade before history's"; "the Union's television runs on Pacifican licences from 1930–31, beside its own mechanical sets (*Hist.*: Jenkins, 1928)". The second clause also keeps §3's line that the analogue road is the Union's.

**F11. An unlisted canon tension, and gaps in the ledger.**
- *Passages:* P-2: "the state holds shares in it ... It owns: ... the film unit ... Farnsworth's television"; Part L: "1912 or 1913, as an article of the Wireless Act".
- *Problems:*
  - Storyline para 188 (CR-057) says "Competitive steel, motor, chemical, electrical, film, aluminium and aircraft firms carry no state stake." A state-shared estate that owns a film unit and a television company needs a tension entry.
  - The Wireless Act is 1911 and is already in the ledger. "1912 or 1913" is not a date.
  - P-2 creates a charter (the press estate, 1887), and P-1 and P-3 settle an estate headship (1887–1931, then 1931). AGENTS.md requires ledger entries for charters and life offices.
- *Fix:*
  - Add T9: case A, the press estate's film and television are estate businesses beside private studios, and para 188 is amended to "film firms other than the press estate's"; case B, the film unit is spun off as a private firm and the estate keeps only the newsreel.
  - Fix P-16's date: either the 1911 Act carries the article, or an amending act of 1913 gets its own ledger entry.
  - Add ledger rows for the press estate's charter (1887) and the 1931 succession.

**F12. The T1 test overstates what existed in 1888–89.**
- *Passage:* "Every part of the plan existed in 1888–89 ...: Le Prince's camera, the celluloid base, perforated strips and projection of photographed motion."
- *Problem:* The zoopraxiscope projected images painted or traced from photographs. Le Prince's projected films "were never presented to anyone outside his immediate circle" ([Wikipedia](https://en.wikipedia.org/wiki/Louis_Le_Prince)). The missing part was an intermittent projector that could move celluloid through the gate safely, and the risk list leaves it out.
- *Fix:* "projection of motion drawn from photographs (the zoopraxiscope)". Add the intermittent projector as the first risk. This makes 1890 the date of short open-air subjects rather than a standing cinema, which suits the newsreel.

**F13. Victoria's silence has no stated reason.**
- *Passages:* P-18 (a) and Part G.
- *Problem:* A queen who in 1873 "speaks to the men in Hawaiian" refuses the microphone through 1914, 1918, 1921 and 1928, and the text gives no reason. Without one, her refusal reads as passivity. Her two set pieces (2 and 7) show her only reacting: she switches a set off, and she watches.
- *Fix:* Add one line of motive. For example, her voice belongs to the cylinder and to Elias, or she will not let the press seat edit her. Give her one active decision in the CR: the T7 rule (the Office films and the press estate distributes) can be hers, made in 1913–14 while she still holds an executive role. In set piece 7, let her watch the Office's tables drawn as charts, which is her own work on the new medium.

---

## Notes

1. **Hearst and Lippmann.** Hearst holds the seat for forty-four years with no conflict on the page except the spiked story of 1919 (CR-050). *Public Opinion* criticizes exactly the spectacle Hearst sells. One scene where Hearst hires or keeps his own critic, or where Lippmann's rule-bound newsroom argues with the *Examiner*, would give P-1 and P-3 a dramatic cost. This is optional.
2. **The 1870s cylinder.** Elias's cylinder of Victoria's voice dates from the late 1870s, the tinfoil era, and tinfoil cannot be kept or replayed reliably. P-19 copies Elias's cylinders electrically in 1913. One *Hist.* line would cover both: say the Laboratory recorded on wax early (*Hist.*: Bell's Volta Laboratory, wax, 1881–86). The underlying fact is CR-027's (PROPOSED).
3. **The two sets of six languages.** The weekly's six (English, French, German, Spanish, Japanese, Chinese; power timeline) are not the air's six (English, Spanish, Hawaiian, Japanese, Tagalog, Cantonese; CR-078). P-9 and Part I say "six tongues" without saying which. P-9 also leaves out Cantonese films at San Francisco. "titles in kanji and Chinese" should read "Japanese and Chinese titles".
4. **An ambiguous reference in P-10.** "The partners' CR inherits him (T6)" follows the Takayanagi sentence. Write "inherits Takayanagi; Zworykin's move is T6".
5. **Muybridge's past.** He killed Harry Larkyns in 1874 and was acquitted in 1875. The Queen's government funding him in 1878 is texture a scene could use. Stanford's absence also needs whoever owns the horses.
6. **Edison in case C.** With projected film shown in Chicago's music halls in the 1890s, Edison launching the peephole Kinetoscope in 1894 needs half a line, for example "a parlour novelty in the Union".
7. **Le Prince's family.** His son Adolphe, his assistant, stays unregistered. Le Prince not vanishing removes a historical mystery. That is acceptable, but say so in the *Hist.* note.
8. **Style.** These read as Claudisms:
   - "What history lacked was one buyer ... The press seat is that buyer." (T1)
   - "Their quarrel ... is a quarrel inside one house, between print and air." (P-2)
   - "The newsreels show her face, and the Realm never hears her." (P-18)
   - "The Prosperity Party buys the most, and the table says so." (P-16)
   - "a book the Office of Public Measures could have commissioned" (P-3)
   - "Here the mainland is the Realm." (P-12)
   - "The funding never stops." (T1)
   - "It belongs to none of them" (Part E), repeated in Part I.

   State each fact plainly. For example: "The Prosperity Party buys the most air time; the Office's table shows it."
9. **Checked and correct:**
   - every age except Victoria's 1931 age (F6): Hearst 23 in 1887 and 68 on 29 April 1931; Lippmann 41 in 1931; Zworykin 30–31 in 1919; Jensen 23 in 1909; Beauchamp 26 in 1925; Le Prince 45 in 1887;
   - the sound delay at twenty miles (about 94 seconds; para 337 "about twenty miles off");
   - Lauste's biography and the 1906 patent with Haines and Pletts ([Wikipedia](https://en.wikipedia.org/wiki/Eugene_Augustin_Lauste));
   - Dickson's credit of the Latham loop to Lauste ([Wikipedia](https://en.wikipedia.org/wiki/Latham_loop));
   - Le Prince's dates; Takayanagi, 25 December 1926; W6XAO, December 1931; Kekuku's death on 16 January 1932;
   - the CR-078 dependencies: the arc stations of 1910–12, broadcasting in 1912, Thalassia and Honolulu on Oʻahu, and the air school's language dates.
