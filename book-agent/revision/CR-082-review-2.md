# CR-082 revision 2 — fresh-context review

Fresh-context review, 22 November 2026. What the reviewer read:
- `CR-082.md`, all of it, including `## Canon tensions` and `## Decisions`.
- AGENTS.md: protected intent and the current-canon paragraphs.
- `population/outputs/provisioning.md`, all of it, and the `[nitrogen]`, `[nitrogen_supply]` and `[exports]` blocks of `provisioning.toml`.
- The storyline at 91, 687, 748, 774, 923, 1033, 1036, 1038, 1063, 1089, 1116, 1148, 1176, 1263, 1290, 1358–1380, 1445, 1450–1451, 1470, 1504, 1516, 1544, 1614, 1639, 1649 and 1681, and searches for every term in the brief. Line numbers are those of 22 November.
- `CR-082-review.md`, to check Part H; `CR-083.md`, A7–A9, the ledger, T3–T8 and the decisions.
- On `/home/claude/cr081`: the CR-081 outline's guiding principle and Part D (D1–D9), and searches of that branch's storyline and ledger.

The reviewer did not read the session records, `CR-082-outline.md` or any other review file.

**Verdict.** Every figure in A3, the how-firm table and Part F matches the report to its rounding. The doctrine is legible: B3 states the author's principle (D16) in its own words, and F states the aim (D14) as indispensability, not land. Revision 2 has fixed the first draft's worst problem, a Realm twice fed. The CR is **not ready to integrate**, for two reasons:
- CR-081 has already been integrated using revision 2's figures, and those figures rest on four items that are still PROPOSED. Where the approved values differ, they would give other numbers.
- R-1's wheat contract has its only instrument in CR-083, which merges later.

Beyond those two, CR-082 is close. The Chile means (R-7b) contradict the CR's own Pampas line and the model's nitrogen series. R-8 misreads the Tomsk passage. In this CR the sufficers have a true argument, but they win nothing that is approved.

---

## Blockers

**B1. CR-081, already integrated, quotes figures that rest on PROPOSED items.**
- *Passage:* the Status list; A3 ("Works", "Work stock", "Nitrogen as it can be got", "Sales abroad"); B1; T9; the decisions F-1c, F-1d, F-15 and F-16. On CR-081's branch: outline G-1 item 2, G-10 and G-14 item 3, and storyline 1672 and 1688.
- *Problem:* The central case (121% in 1910, 115% in 1932, the margin closing in 1940–42) is built on four PROPOSED items: F-1c revised, F-1d revised, F-15 and F-16. So are the tables' crossings of 1914, 1915, 1920, 1933 and 1938, because §7's home ceiling deducts work stock. The approved values (22 million acres by 1910; 480 thousand tonnes) give the first draft's figures, 204% and 131%. CR-081 has already written revision 2's numbers into its outline and storyline:
  - G-1 quotes the crossings of 1920, 1933 and 1938, the 115% and the year 1940.
  - G-10 rests on "about 3 million tonnes of grain abroad in 1931", which is F-16.
  - G-14 quotes 1938 as the year the granary contracts are timed against.

  If the author keeps any approved value, the merged branch is inconsistent on the day it merges.
- *Fix:* The author decides F-1c, F-1d, F-15 and F-16 before the merge. Under A3's heading "How it counts", add: "The central case and the Office's dates below assume F-1c, F-1d, F-15 and F-16 as revised. CR-081 G-1, G-10 and G-14 quote them." If any of the four is refused, re-run the model and re-check CR-081's three sentences.

**B2. R-1's wheat contract has no instrument until CR-083 merges, and its ledger row is duplicated.**
- *Passage:* E, R-1; L, the row "Prairie wheat contract (R-1)"; the Depends-on list; CR-083 A9 item 2 and CR-083 F.
- *Problem:*
  - CR-083 A9 makes the ten-year floor-price contract part of what Canada is given for losing British Columbia. It exists only as that treaty's article.
  - CR-082 merges with CR-081 now and CR-083 later, so on the merged branch R-1 would name a treaty that canon does not yet contain.
  - The same contract is a ledger row in both CR-082 L and CR-083 F, so `ledger.py check` would meet two rows for one commitment.
  - The review's B4 (a floor price in the winter the Bank refuses to print) went to CR-083. CR-082 does not say that R-1's price and its argument are still unsettled.
- *Fix:* In E, R-1 should read: "The door stays open and the Realm never asks first. Contract and credit come in 1931 by CR-083's treaty with Canada (A9), which also carries the price." Delete the R-1 row from CR-082 L. Add to J: "R-1 is carried out by CR-083; until it merges, no prairie contract is in canon."

---

## Should fix

**S1. Figures stated more firmly than the report allows.**
- A3, item 3: "Without Chile the Realm would sell almost nothing abroad in 1910". The report (§4) gives 1.1 million mouths instead of 2.6, which is less than half, not almost nothing.
- A3, "Sales abroad": "At its height this is about a sixth of the world's wheat trade". The report attributes the sixth to 1929's 4 million tonnes, not to the peak. The comparison also sets grain or its equivalent against wheat alone. It should read: "In 1929 it is about a sixth of the world's wheat trade by weight."
- F-16 gives "7 million in 1917". That is the input. The model can sell only 5.8 million mouths (about 6.1 million tonnes), because capacity binds that year (§4: idle capacity 0.0). Quote the result.
- A3, Japan: "Japan's fields must go on yielding 1% more every year". The report's own people column grows about 1.2% a year in 1920–32. Write "about 1.2%", or drop the figure.
- A1: "the storyline rounds 1932 to 'about 37 million'". 36.2 million does not round to 37. The workbook's residents are about 37.1 million (AGENTS.md, Deseret sheet), and the storyline (1614) follows the workbook. Say that the provisioning model reads the population run, which is about 0.9 million below the workbook in 1932.

**S2. Chile's motive in 1891 contradicts the model's nitrogen series.**
- *Passage:* D, "The motive of 1891"; L, the Chile row (1891–1900).
- *Problem:* D says "the regency needs the nitrate". The report's fields take no nitrogen in 1890 or 1900 and 5 thousand tonnes in 1905 (§4), and the paying crops' share is set at zero in 1900. Long purchase contracts from 1891 therefore buy nitrate that the Realm's fields do not use for fourteen years. The motive also carries no label, though it came from the review and not from the author.
- *Fix:* Label the motive PROPOSED and give 1891 a need the model has. Nitrate is the powder of the mines and the fleet. *Hist.*, general knowledge, to verify: sodium nitrate was the feed of black powder and of nitric acid for explosives. The table makes the fields' need a forecast, and the Strait is the road round. Date the contracts' deliveries to the fields "from about 1900" (F-1b).

**S3. The guarantee of Chile takes sides that the CR says it keeps out of, and the Realm's own ammonia empties it.**
- *Passage:* D, "By 1900 the Realm is Chile's guarantor against a seizure of the nitrate coast or the Strait by any power"; D, "The Pampas (P-4)"; F, "Its points of control … Chile's nitrate".
- *Problems:*
  - "Any power" includes Argentina, so the Realm is inside the frontier quarrel that P-4 says it keeps out of. It also includes Peru and Bolivia, from whom Chile took the nitrate coast in 1879–84 (*Hist.*, general knowledge, to verify: the Tacna–Arica question lasted until 1929). CR-053 already gives Pacifica a Peruvian oil company.
  - In the model the fields take 51 thousand tonnes from Chile in 1920 and nothing from 1925. Meanwhile the Realm's loan is secured on the nitrate duty, about half of Chile's ordinary revenue. In 1930 the Concord joins the nitrogen convention (1544). The provisioners' success ruins the client they bought, and the CR does not say so.
  - F still lists Chile's nitrate as a point of control a century on.
- *Fix:*
  - Write "against a seizure by any power from outside the Americas, and of the Strait as the treaty of 1881 left it (*Hist.*, to verify)".
  - Add to D: "From the 1920s the Columbia's ammonia replaces Chile's nitrate in the Realm's fields. The loan on the duty is the regency's debt to Chile, and Julian's ministers must decide what to do with it." The decision can stay OPEN.
  - In F, replace "Chile's nitrate and the Columbia's ammonia" with "the Columbia's ammonia (Chile's nitrate until about 1920)".

**S4. R-8 misdates the Siberian choice and frames it against the wrong alternative.**
- *Passage:* E, R-8; the storyline at 1445 and 1451, and 1358, 1367 and 1380.
- *Problems:*
  - The vote of 1921 was promised in 1919: "the 1919 bargain is a promised vote" (CR-041). So the choice was made in 1919, not in 1921.
  - Canon's alternative was the Siberian state promised in 1918, not "a client".
  - Victoria's charge at 1445 is that "he has done to Siberia what the Union tried to do to California", and "the storyline gives no verdict". A grain motive written into the cabinet minute gives her a new count. The draft does not say whether she knows of it.
  - CR-081 G-13, which R-8 cites, says the Siberian traffic before 1932 is small and that "the point is the rule, not the tonnage". "Siberia's grain comes by … the Mukden rates" is therefore stated more strongly than CR-081 allows.
  - Canon already has the provisioner's instrument in "the land-and-grain guarantee" (1367, 1380).
- *Fix:* "In 1919 the two figures beside the bargain count Siberia's grain on the railway board's contracts, the half of the land-and-grain guarantee that survives a federal Russia, and not on a frontier to hold. The minute is the cabinet's. Victoria does not read it before 1921 [or: reads it, author to decide], and the storyline still gives no verdict." Add 1358, 1367, 1380, 1445 and 1451 to the impact notes.

**S5. Victoria loses on numbers for twenty years, and nobody beats her.**
- *Passage:* B7, "the sufficers lose the argument on numbers in every decade"; B2.
- *Problem:* The Regent holds the authority from 1887 to 1907, and the run grows 4.1–4.8% a year under her. B7 says who sets the shape of entry. It does not say who wins on its size, so the sufficer regent looks passive or inconsistent.

  Canon supplies an answer. Her own settlement programme fills the interior (687: the Land Fund sells farms on instalments and the passage offices bring settlers). The run also has residents of Japanese origin rising from 0.25 to 1.5 million in 1890–1910.
- *Fix:* Add to B7: "The numbers come from the regency's own settlement programme, which Powell's districts and the Land Fund's sales carry and which the Senate will not stop, and from natural increase. Victoria shapes entry and cannot shrink it." Give the provisioners their answer to the guest-worker programme too: "a class of workers outside citizenship" (1038) is talent the examination never sees.

**S6. The doctrine: the sufficers' best argument is in the model, but not in their mouths, and they win nothing that is approved.**
- *Passage:* B3; F, "Whether it closes" and "What follows"; H, "Literary effect".
- *Problems:*
  - The century table (§8) gives the sufficers an exact and true case. At 0.60% a year of growth, the Realm's own works and the first list of sellers close the century without the Union. Julian's course needs 72% of the world's trade and "holds only while the sellers sell and the sea lanes are open". F states this as the narrator's conclusion. Neither school is given it.
  - Inside CR-082 the sufficers' only win is R-2's refusal, which is PROPOSED. Their other wins are in CR-083 or CR-081, and Giannini's case in CR-081 loses its vote.
  - "Control" of the trade is not squared with canon's self-denials. Canon refuses an embargo on the Union (D15, line 91), and CR-081 G-8 says that "the Concord does not refuse seed, nitrogen or grain to a partner".
  - "Three of the five works are not territorial" is ambiguous.
- *Fix:*
  - In B3, add to the sufficers: "Their figure is the Office's own. At six-tenths of one per cent a year the Realm's works and the first sellers feed it for a century; at Julian's rate it must buy three-quarters of what the world sells."
  - In F, add: "Control means being indispensable, never denying: the Realm refuses food to no partner and embargoes no neighbour in peace."
  - Replace the ambiguous sentence with "Only work 2 needs land the Realm does not hold, and that comes by vote (CR-083)."
  - Approve R-2's detail (see Decisions).

**S7. T9 case B sizes the fields' nitrogen but not CR-054's total.**
- *Passage:* T9; C; the storyline at 1504 ("about 90,000 tonnes of nitrogen"), 1544 and 1148.
- *Problem:* CR-054's figure is the plants' whole output. That output also supplies the crowns' sugar and rice, Korea and the China trade (1504), and since CR-081 G-4 also Manchuria's farmers. Case B gives only the fields' 150–195 thousand tonnes, or the supply ramp's 250–290 thousand. The integrator cannot rewrite 1504 or the workbook from that.

  Two further points:
  - A Realm fixing several hundred thousand tonnes changes the politics of the convention of 1930. *Hist.*, general knowledge, to verify: world fixed-nitrogen output was about 2 million tonnes in 1929.
  - In 1917 the Realm takes 35% of Chile's nitrate while the Entente needs that nitrate for shells. *Hist.*, general knowledge, to verify.
- *Fix:* State the total for 1929 (the fields, plus the crowns, Korea, the China and Manchurian trade, plus industry), or label it "to be sized on integration, MODEL". Add one sentence on 1917: the Entente's shells come first and the Realm's arc furnaces are making explosives. Add 1148 to the impact notes.

**S8. The storage of 1900–1920 is unnamed and may break canon's salmon rule.**
- *Passage:* A3, "Works"; C, "Water"; T2; the report's §1 ("Storage on the Sacramento, the San Joaquin and the Snake from 1900").
- *Problem:* 4.5 million acres are added by 1920 behind dams that canon does not name. T2 states the rule generally: "no dam where salmon cannot pass". Storage on the Sacramento and the San Joaquin blocks salmon unless it has passage. *Hist.*, general knowledge, to verify: Shasta and Friant closed the upper runs. The dams' sites would also need compacts under CR-071.
- *Fix:* Add, labelled PROPOSED or OPEN: "Storage of 1900–1920 is built only where salmon pass or none run (the upper Snake above the falls, the foothill reaches), each site under its compact. The sites and their cost are OPEN for the workbook."

**S9. The impact notes miss passages that this CR changes or settles.**
- 687: "when Powell enters the Republic's service" is OPEN. B1 settles it as "by 1888". Say so, or keep it open with "the report of 1888 is his office's".
- 748: the famine wheat of 1876–79, which A2 cites.
- 774: the Colegio de Santa Fe "trains the surveyors … and the engineers of the acequias". A3's "dry-land farming since 1864" is not in the storyline, so the sentence must be added.
- 1033: Haber refuses Carquinez's chair.
- 1148: the BASF licence of 1913. C's "nitrogen is the first answer of both schools" (1898–99) must end in a German licence fifteen years later. Say so.
- 1614: the "about 37 million" (S1).
- 1358, 1367, 1380, 1445 and 1451: R-8 (S4).
- On the merged branch: 1656, 1672 and 1688 quote this CR's figures (B1).

---

## Minor

**M1.** Status: "the details of R-2 and R-8" is wrong for R-8, which is PROPOSED as a whole. "Dates marked PROPOSED in the text": no date in the text carries the label, so either drop the phrase or label the dates.
**M2.** R-4: "Japan renounces the south" carries no label, and "the south" is undefined. Write "(PROPOSED, for the partners' CR): Japan renounces any southern advance below the Philippine crown". R-4 is APPROVED but rests on line 1681, which is PROPOSED (OPEN-019-06). Say that the approval stands only if that item does. In L the guarantor is "the Concord", whereas 1681's treaty is Pacifica's. Pick one.
**M3.** R-2's "the Senate, the sufficers' house" is not in B3's list of the sufficers. Either add the Senate to B3 or drop the epithet.
**M4.** D: "The Strait also matters to the canal the Realm opens in 1900" is muddled, given 894 and 1112. Write: "Until the canal opens in 1900 the Strait is the Realm's road to the Atlantic, and afterwards its only other one." On the *Itata*: the Companies Act governs treaties of service, not a foreign belligerent's cargo, so write "under the venture licence's rule against private war from Pacifican soil". *Hist.*, general knowledge, to verify: the arms were transferred off the Channel Islands (San Clemente or Catalina), not off San Diego.
**M5.** C and A3 say "Arc nitrogen cannot compete for fertilizer, which is why canon's furnaces are idle in 1919". Canon gives no such reason (1470, 1516). Write "and so they are not turned to fertilizer when the war ends".
**M6.** A3: "Nitrogen with the short wheats is +37% of the +109%" sets a multiplicative gain (1.22 × 1.12) against a total, and calls it "a third". Write: "Nitrogen and the short wheats multiply yields by 1.37 of the whole 2.09."
**M7.** A3, Japan: "it has no colony to fill it" survives, although E already carries the review's S11 wording. Use "no colonial rice on command" in both places. Formosa's rice reaches Japan on long contracts (CR-081 M3).
**M8.** The Depends-on list still has "nations lease and do not sell" for CR-071. The review's M4 doubted it (AGENTS.md: the land of Columbia's nations without a treaty is bought for the Land Fund), and Part H says M4 is worked in. It is not. Write "nations lease their crossings and dam sites".
**M9.** B7: the 1868 treaty's family article is PROPOSED in canon (§14). Say so.
**M10.** B3 calls Keawe a sufficer. His canon arc concerns land, water and industry (CR-020) and has no view on entry. Label it PROPOSED, or write "a sufficer on land and water".
**M11.** The report's opening paragraph says "the century's four works", but §8 has five. That is a model text fix.
**M12.** I, the Nephi set piece: the report's short wheat "was not sown in the driest zone" (§2), and Nephi is a dry-farm station. Either use the drill or fallow there, or give the short wheat to a wetter dry-land station.

---

## The doctrine

- **Legible.** B3 states D16 directly: both schools maximise exceptional engineers and scientists, one by selection and one by numbers as well. F states D14 as indispensability at every step of the trade (seed, nitrogen, machines, credit, ships, ports, storage, information), "not to own its land". Both are clear.
- **Two true arguments.** The provisioners have the same examination on a larger base, plus a fed umbrella that widens the pool. They also have the fact that growth happens under the sufficer regent anyway (S5). The sufficers have schools at the Realm's best for every child. They also have the model's dependence: 72% of the world's trade and the sea lanes. That second argument is in F but has no speaker (S6).
- **Each wins something.**
  - The provisioners win the entry course from 1908, nitrogen, the northern water (P-2) and the granary (CR-081).
  - The sufficers win the shape of entry (B7). Their wins in CR-082 are otherwise PROPOSED (R-2) or outside it (CR-083's Fraser clause and four rivers).
  - The best inversion in the CR is approved: the sufficer intervenes in Chile for yield, which is her own answer to the table. Keep it.
- **Contract, not land.** This holds everywhere except Caledonia, which comes by vote. Say so once (S6). It also needs canon's self-denials stated in F, or "control" reads as a threat to "the giant its neighbours need not fear" (91; CR-083 T8).

## Figures checked

| Figure in CR-082 | Report | Result |
|---|---|---|
| A1 residents and growth (4%, 3.6%, about 2005) | canon_by_year.csv | match; "about 37 million" is not a rounding (S1) |
| A3 land: 13.8, 22.0 and 15.8 million acres; works 13.8, 18.3 and 22 | §1 | match |
| Work stock: 88 of 325 million (27%), 6% by 1925 | §3, toml | match |
| The six innovations, +109%, 1.37, 1.85 and 1.93, 34 and 41 years | §2 | match; "+37% of +109%" (M6) |
| Nitrate: 2.3 and 2.9 million tonnes; 35% cap; ramp of 50, 150, 250 and 290 | toml | match |
| "What it finds" table, 1890–1932 | §§3–4 | every cell matches |
| Items 1–7 (46%, 15–32%, 1905, 1930, 98%, 1940–42, the crossings, 80, 170 and 562 million, 13 times) | §§3, 7 | match; "almost nothing" (S1) |
| Sales abroad: 1.5, 3, 7, 4 and 3 million tonnes; a sixth | toml, §4 | 1917 is input, not result; the sixth is 1929's (S1) |
| Japan table; 5%, 8% and 13%; within 1%; 38 million koku-equivalents | §5 | match; "1% a year" (S1) |
| How-firm table | §9 | match |
| F: 75, 26, 14, 115 (20%), 587; 76%, 72%, 55% and 52%; 95% of 650 million tonnes | §8 | match |

Two century figures are high or doubtful, *Hist.*, general knowledge, to verify. The Pampas at 85 million tonnes looks high for grain and beans without soymeal. The prairies' 45 million tonnes may include canola, which is neither grain nor soybean.

## Literary effect

- **Agency.**
  - Victoria acts in 1891, which is strong. On numbers she is passive (S5).
  - Julian acts from 1908. R-8 gives him a motive he must hide from his mother (S4), and that is where the drama is if the author wants it.
  - Chile acts only as a recipient. Give the junta a decision of its own: it takes the Realm's loan against the Itata's rifles.
- **Conflict.** The tables give mother and son a quarrel with numbers in it, and they fit the drift of 1908–1921. The 1910 table, with the Philippine crown first counted and the century at nineteen times the ceiling, is the right scene for that quarrel.
- **Viewpoint.** The Nephi farmer is good. Powell before the cabinet in 1888 has no one in the room who disbelieves him; give him a respondent, such as the Land Fund's sales or the estates.
- **Irony to use.** The challenge evening of 1898–99 hunts the nitrogen that Haber, who refused Carquinez's chair (1033), will find for Germany. The Realm then buys his licence in 1913 (1148). *Hist.*, general knowledge, to verify: Crookes's address of September 1898 put the wheat crisis about 1931, the decade the model's crossing falls in.
- **Historical people rather than invented ones**, all *Hist.*, general knowledge, to verify:
  - Hilgard (1833–1916; alkali soils at the University of California) is a natural sufficer.
  - Mead (1858–1936) is a natural provisioner. He was State Engineer of Wyoming, worked in Victoria, Australia, in 1907–15 (a bridge to R-4), and became Commissioner of Reclamation in 1924. His failed state colonies at Durham and Delhi give the provisioners a defeat.
  - Hoover ran the Mississippi relief of 1927 (1089), which makes him the man for R-2's drainage compact.
  - For the Office's tabulator of 1890: Hollerith, whose cards are at the Office from 1888 (CR-049).
  - For the dry-land programme: John A. Widtsoe of Utah's agricultural college, author of *Dry-Farming* (1911).
  - For Chile: Jorge Montt, Pedro Montt and the junta's agent Ricardo Trumbull.
  - For a neighbour who does the arithmetic (B6): Nitobe Inazō, Sapporo's agricultural economist.

## Protected intent

Nothing in revision 2 touches Noe Ward's death or a culprit, Julian's styles, the Hawaiian throne, or extermination. The Chile means use no troops. The Mekong, Manchuria and the sellers are reached by contract. The four values are intact.

## Decisions the author must make

| Item | Status | Recommendation |
|---|---|---|
| F-1c revised (13.8, 18.3 and 22 million acres under the works) | PROPOSED | Approve, with S8's salmon and compact condition; needed for B1 |
| F-1d revised / T9 case B at revision 2's size | PROPOSED | Approve, once CR-054's total is stated (S7) |
| F-15 work stock | PROPOSED | Approve; 1910 is sourced, and 1930 and 1940 are to be verified |
| F-16 exports | PROPOSED | Approve with 1917 corrected (S1); CR-081 G-10 depends on it |
| R-7b Chile's means | PROPOSED | Approve with S2 and S3 (the guarantee limited; the 1920s named) |
| R-2 detail (shorter count refused, 1931) | PROPOSED | Approve: it is the sufficers' only win inside this CR |
| R-8 Siberia | PROPOSED | Approve only as recast in S4 (1919, the land-and-grain guarantee, no verdict) |
| B3 names (Hilgard, Mead) | PROPOSED | Approve and register both |
| T11 constant diet | OPEN | Case A, as recommended |
| Gulf compact's date (L) | OPEN | After the flood of 1927, with Hoover, if the author wants a date before the culinary CR |
| New Zealand guarantee's date and party (L) | OPEN | Decide with OPEN-019-06 (M2) |
| Unregistered: the tabulator of 1890, the head of the Santa Fe programme, Balmaceda | — | Hollerith (canon), Widtsoe (*Hist.*), and register Balmaceda |

## Checks run

- `python3 book-agent/revision/lint_canon.py --only book-agent/revision/CR-082.md`: "Canon lint clean: 1 file checked."
- `python3 book-agent/revision/cr_facts.py preview book-agent/revision/CR-082.md`: "CR-082.md: no fact changes declared." The CR declares none, which is correct now that T4 has moved. A clean preview therefore checks nothing. The prose passages in S9 have to be worked by hand.
- `python3 -B -m pytest -p no:cacheprovider population/tests/test_provisioning.py`: 12 passed, run read-only.
- Every figure in A3, E and F was checked by hand against `provisioning.md` and the toml (table above).
- CR-083: nothing of its material is left half-present in CR-082 except R-1's contract (B2). T3–T8, Caledonia and the northern water's text are wholly in CR-083. CR-082 keeps only work 2's count and cross-references, and these agree (26 and 12 million mouths; 45 and 20 km³).

## Not checked

- The session records, `CR-082-outline.md` and other review files, by instruction.
- `change_requests.json`, the character bible, and the registry beyond the Victoria, Julian, Keawe and Powell entries.
- `finance/CR-056-dynamics-workbook.md`, for A2's 2.6–3.6 million pumped acres.
- The `provisioning.py` source, apart from its tests.
- CR-081's storyline beyond the searched passages, and its outline outside the guiding principle and Part D.
- No *Hist.* claim was checked against a source. Every one above is general knowledge, to verify.
