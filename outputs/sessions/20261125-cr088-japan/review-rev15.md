# Fresh-context review: CR-088 revision 15 (branch draft/cr-088)

Reviewer read: AGENTS.md, docs/authority-and-scope.md, CR-088.md in full (with `## Canon tensions` and `## Appendix A`), the storyline lines the CR cites and the paragraphs around each section in its impact notes, plus the matching entries in character_registry.json, character_bible.md, canon_facts.toml, commitments/data/ledger.toml and finance/CR-031-review.md (only to check the rescue figure). I did not read session outputs, decision sheets or git history. I made two light web checks: Harris's tariff, and Kalākaua's decoration (that one was inconclusive). CR line numbers below refer to `book-agent/revision/CR-088.md` as it stands on the branch.

## Verdict

**Not ready for the author's approval yet. The fixes are few and mostly bounded.** The CR's core is strong. It argues Japan's acceptance on Japanese grounds (A2.1–A2.2), and every Edo clause says what each side gains (A1.2). The grievance catalogue has four kinds of grievance and a protected Altai boundary (A5). The agon of A3 has real losers. Kiyotada and his missing key (A5.11, A6.4) work well. The citations I checked are accurate and every protected intent holds.

Three problems stop approval:
1. A3.1 quietly retires approved canon: CR-027's "Oceanian union" and "Prince Komatsu", at L848, in the registry and in the bible. The CR has no canon tension for it and no impact note that removes it.
2. Appendix A contradicts itself on who pays and receives what in two places (grace declarers at an Audit or Call; locked declarers' notes at a Call). It also leaves undefined how a player below zero is recorded and paid, and that is the mechanism the 1928 set piece turns on.
3. One currency-precedence clash in A.3/A.5 decides real payments.

The should-fix items are mostly consistency and history repairs. They also cover a few places where the draft makes the marriage frictionless again: the Ainu cost of 1893–99, the Union's door, and the mission clause of 1919.

## Blockers

**B1. Kalākaua's 1881 proposal contradicts approved canon, with no tension and no impact note.**
- *CR:* A3.1 "The proposal" (line 234): "Here he makes the marriage proposal alone, beyond his instructions, and no federation". D-21 (line 747): "no federation". Impact note at line 550 says only "Add … his declined marriage proposal".
- *Canon:* L848 **[APPROVED — CR-027]**: "proposes an Oceanian union sealed by marrying his niece, the young Kaʻiulani, to Prince Komatsu; the Emperor politely declines." The same appears in character_registry.json (CT-DAVID-KALAKAUA: "proposes an Oceanian union and the Kaʻiulani–Komatsu match"; CT-KAIULANI-CLEGHORN: "proposes her marriage to Prince Komatsu as part of an Oceanian union") and character_bible.md lines 591 and 1102.
- *What is wrong:* the CR retires an approved plot fact (the union) and silently changes the prince's identity, which the CR's own source note says is uncertain ("Higashifushimi Yorihito in most"). This is exactly the case AGENTS.md's canon-tension rule covers. As drafted, an integrator would "add" a proposal that is already on the page and leave "Oceanian union" standing beside "no federation". The CR's reason, "since Hawaii is in the Confederation", is also not obviously right. An Oceanian union is not the historical Asian union, and canon presents it as Victoria's envoy's own vision.
- *Fix:* add a canon tension `T-KAL-1`. Case A keeps the Oceanian union as an envoy's overreach beyond his instructions. Case B is D-21: the marriage only, the union retired. Record the author's D-21 decision under it, and add a `retire_forbidden`/fact entry if needed. Change the impact note for L848, the registry and the bible from "add" to "revise": strike "an Oceanian union", and settle "Prince Komatsu" (keep it, or name the prince the CR's sources support, and say which). Under Case B, also say why the union is dropped in terms of Kalākaua's own motive, not only Hawaii's constitutional status.

**B2. Appendix A contradicts itself on payments to and from declarers who are not the hand's focus.**
- (a) *Grace declarers and the Assay's bad-note payment.* A.5 Audit (line 892): "a declarer still in grace loses only the notes". A.7 (line 940): "A declarer still in grace pays nothing more". But A.6 "A bad note" (line 919): "whenever the declarer is found noten at the end of the hand, the assayer gets the fee back … **plus 1,000 Gold per note** … This covers the Audit, a Call …". If an assayed declarer is still in grace and noten when someone else wins, does the declarer pay the assayer 1,000 per note or not? *Fix:* say which rule governs. The simplest is "the bad-note payment applies only to a declarer whose hand has locked, or who is shown noten at a Call, Confession or presentment".
- (b) *Locked other declarers' notes when a Call ends the hand.* A.5 (line 891): at an Audit "the notes go to the winner as deposits". A.7 "Other Paper declarers" (line 940) sends the Fraud Penalty "to whoever won the Call" and says what happens to the notes only for a declarer in grace ("stay on the table as deposits"). For a locked, noten other declarer at a Call, the rules do not say whether the notes go to the Call's winner, stay as deposits, or are split among the takers. *Fix:* one sentence: "their notes go with the Fraud Penalty, in the same shares".
- (c) *Takers and droppers split the stakes.* A.7 Renewal (line 932): "Only the takers … claim the declarer's notes and collect any Fraud Penalty, each at their share of the doubled stakes." Shares were "fixed now, in equal parts" (line 927). So when one of three callers drops, a third of the notes and of the Fraud Penalty has no owner. The sentence also seems to double the Fraud Penalty, which line 928 forbids ("never the Fraud Penalty of another declarer"). *Fix:* state that the droppers' shares of the notes and of any Fraud Penalty pass to the takers pro rata, and that the Fraud Penalty is never doubled.

**B3. Below-zero accounting is undefined, and the set piece of 1928 depends on it.**
- *CR:* A.8 "Out of Gold" (lines 944–948) converts a Gold-first remainder into Paper at two for one. "Tobi counts only what is on the table" (line 949). "The floor" (line 954): "The loan first brings the borrower's total back to zero … A borrower at −2,000 needs at least 7,000."
- *What is wrong:* nothing says what happens when Gold and Paper both run out mid-payment. Is the shortfall recorded in Gold or in Paper, at one for one or two for one? Does the payee receive the full amount (from the reserve, against the debtor) or only what was physically paid? If the loan "brings the total back to zero", who gets that money: the original creditor, or nobody? A player with 0 Gold and 4,000 Paper who owes 8,000 Gold-first has paid 2,000 Gold-equivalent. Is that player at −6,000 or −12,000, and is the creditor short 6,000? At a real table this is the first argument of the evening. It also decides whether "refuse to print" has any meaning in the 1928 scene (see S10).
- *Fix:* add a short "Shortfall" rule. One coherent option: when both currencies are exhausted, the shortfall is written on the score sheet in Gold against the debtor; the payee is credited in full from the reserve; a rescue loan pays the reserve first. Then reword the floor examples in terms of that rule.

**B4. A.3 and A.5 clash on currency precedence when one Paper declarer deals into another.**
- *CR:* A.3 (line 843): "Paper Riichi wins are paid **Paper first**". A.3 (line 847) puts "the winner's leverage on a Paper declarer's deal-in" under "Gold first, always". A.5 (line 874) on a deal-in: "the declarer pays in Gold first".
- *What is wrong:* if the winner holds a Paper Riichi and the discarder is another Paper declarer, both rules apply, and they decide whether the whole payment or only the leverage han is paid in Gold first. That is a large sum. *Fix:* state the precedence, for example "on a Paper declarer's deal-in the whole payment is Gold first, whatever the winner's declaration". Alternatively, split the payment: the hand's value in the winner's currency, the leverage han in Gold.

## Should fix

**S1. The Marshalls' third condition breaks the CR's founding rule without an answer.** A2.6 condition 3 (line 223), "Freedom for the Hawaiian missions", is a treaty-protected mission on Japanese-held soil. That is exactly what A1.2 item 2 (line 135) says the Republic renounces "with China too" (L762, "policy of no missionaries"), and A1.2 calls it "a pretext" and a "casus belli". The CR notes the irony ("reverses the Treaty of Edo") but gives Pacifica no reason to break its own rule, and gives Japan no grievance at it: G28 (line 431) records only Pacifica's grievance. *Fix:* either reframe the condition as a general religious-freedom and no-expulsion clause that names no mission, matching L804's Catholic precedent as a condition the *Pope* imposed, or keep it and add a Japanese grievance (the navy's southern school or the Home Ministry: "California promised no priests"), with Julian's or Hawaii's reason for paying that price.

**S2. "Only British Columbia … and White Australia … still bar the door, and both are British" ignores canon's Union.** A2.3 item 4 (line 183). L1220: "Roosevelt … while his immigration restrictions make the courtship unreliable". A2.4 (line 189) itself lists "the Union" among the targets of racial-dignity resentment. *Fix:* add the Union's restrictions (and, if wanted, a 1924-style act) to the list of doors still barred, and drop "both are British" or make it "two are British".

**S3. T-AINU-1 Case B removes the loss of 1893–99, and the Act has no Japanese motive.** A5.1 (lines 437–442) and the L1790 impact note (line 554: "while noting the remaining pre-1893 scar"). Canon L739 and L1188 put paddy across the Ishikari and Kamikawa plains from 1893 with the Realm's help. Before the Act, and outside its registered *kotan* trusts afterwards, that settlement still took Ainu ground. The draft's residue is only "the 1870s–92 dispossession". That makes the Hokkaido strand close to frictionless, against the CR's own aim in A2.2 ("an argument and not a brochure"). The draft also never says why the Imperial Diet passes the Act. Sitka's reasons are given, and Japanese reasons are not. *Fix:*
- extend the residue to the 1893–99 settlement and to the non-trust hunting and gathering grounds;
- keep a reduced form of the sufficers' rebuttal at L1790 (the Act protects villages, not the country);
- give the Diet's majority a Japanese reason, for example the Home Ministry's fisheries revenue from managed rivers, Satō's and Nitobe's colonial-policy argument, or answering Sitka's reproach before the 1897 renewal;
- name the losers in Tokyo by bloc.

**S4. History errors marked *Hist.*:**
- (a) A1.2 item 3 (line 138): "a permanent 5 per cent tariff cap" for Harris's treaty of 1858. The 1858 schedule was mostly 20% on imports (35% on liquor, 5% on some goods). The uniform 5% came with the Tariff Convention of 1866. Fix the wording, for example "fixed tariffs that Japan could not change".
- (b) A5.1 (line 438): the 1899 Protection Act "outlawed river salmon fishing, and banned the Ainu language and *iomante*". The salmon bans were earlier Kaitakushi and prefectural measures. The Act itself did not ban the language or *iomante*; those came from other assimilation measures. Re-attribute them.
- (c) A5.2 (line 447): Sōseki (d. 1916) warning against "Honolulu cinema fashions (*moga*)". The word *moga* and Honolulu's talkies (1919–20, L1653) are later than his death. Give the *moga* critique to a 1920s critic.
- (d) A3.3 (line 242): Naitō "studies … at Carquinez rather than MIT". I know of no MIT study by Naitō. He was a Tokyo Imperial University graduate with a study tour of 1916–17. Verify, or drop "rather than MIT".

**S5. The 1881 convention's authority is not stated.** A3.1 (line 233) and C-1881-TOKYO-EMIGRATION (line 600): "the Kingdom of Hawaii's own … binds neither California nor the Confederation". Under the Articles, "The common institutions control defense, the navy, customs, currency and external relations" (L364), and in 1878 Hawaii signed for Pago Pago "on the Confederation's behalf" (L804). *Fix:* say on what authority a member signs with a foreign power. Options: under the member's power over residence (L364, PROPOSED CR-059) with the Council's consent; or signed on the Confederation's behalf with effect limited to Hawaii. Make the ledger entry match.

**S6. Nitobe's fourth point turns into a narrator's verdict.** A2.5 item 4 (line 205): "This is not a prophecy … and the officers of 15 May 1932 … prove it right." A5's own boundary (line 497) says "No grievance is settled on the page by the narrator's verdict", and R4 keeps 1932 out of an actor's knowledge. *Fix:* keep the historian's reading and cut "prove it right". Let the reader make the link. The set piece (line 570) already does this better.

**S7. Kiyotada's reputation needs knowledge and timing checks.**
- (a) A6.4 (line 518): to "Pacifican skeptics (King, Tate's bloc)" he is the officer who "delivered the Tokyo intelligence folder". The British file's folders are the Office's secret (L1709). Tate's bloc, at least, cannot know this. *Fix:* limit that knowledge to those who can have it, or replace it with what the public knows (May 1932).
- (b) A6.4 (line 516) and the set piece of 1 August (line 573) have him "presiding over" or "signing the order that retires" the reserved squadron. L1786 **[APPROVED — CR-085]**: at Hayama in June "the common Navy minister lays the order before the Council himself". That minister is his unnamed predecessor (OPEN, L2047). *Fix:* have him carry out the order that comes into force on 1 August, or have the CR decide that he was the minister in June (which conflicts with "from 1 August").
- (c) Kiyotada has no private cost. His marriage and children are OPEN (line 766), and the registry lists "personal motives" as OPEN. Reading reports on his father's own subordinates (A6.3) is the one tension. Consider letting it cost him something, for example Kashiwagi's court martial and Maria's departure.

**S8. The non-fortification of the Marshalls is attributed to naval limits that contain no such term, and the parity is cited as fact.** A2.6 (lines 218, 221) and C-1919-MARSHALLS (line 598): "cannot be fortified under the naval limits of 1919". C-1919-NAVAL-LIMITS in the ledger has tonnage, parity and disposal terms and no island non-fortification, and its status is PROPOSED. L1403's parity sentence is **[PROPOSED]** too, yet A2.1 item 3 (line 164) and A5.8 (line 473) use it as settled. *Fix:* make non-fortification a term of the Marshalls article itself, or amend C-1919-NAVAL-LIMITS and say so. Tag the parity claims "(PROPOSED in canon)", as A2.1 item 4 already does for L1088.

**S9. The ledger amendment for the Treaty of The Hague is missing.** The impact note at line 547 rewrites L1403's "Pacifica and Japan retain Germany's Pacific islands". That sentence is a `more_quotes` entry of C-1919-HAGUE (ledger.toml line 3301), and its `owes` (line 3280) uses the same words. `ledger.py check` will fail on integration. *Fix:* add C-1919-HAGUE to "Amended commitments" with the new quote and owes. Consider also noting L1336's PROPOSED sentence.

**S10. The 1928 set piece does not match A.8 and S29.** Set piece at line 567: "the attaché left with zero Gold Sticks waiting to see whether Kashevarov will advance a rescue loan (at the Window's 5,000 floor, on the 50% Leash …) or refuse to print."
- Under A.8, Refusal to Print ends the game only for a player **below zero** in total. A player at zero Gold with Paper left simply plays on (line 952).
- A player below zero needs more than the 5,000 floor (line 954).
- Offers come from every rival in turn order (S29, line 951), not from Kashevarov alone.
- The Leash is "all Gold"; "50%" is the interest.
- The scene also never says who declared, who assayed and who called. A renewed Call with three notes, missed and noten, costs at least 24,000 Gold-first (28,000 at Emergency Rate), which almost certainly puts the declarer below zero.

*Fix:* make the attaché below zero in total, then state the floor that applies ("back to zero and 5,000 Gold"). Make the decision the table's, with Kashevarov the rival everyone waits on. Say "the Leash at 50% interest".

**S11. The Maturity Draw lets a locked hand be rebuilt, and A.10 describes it as "completion".** A.7 (lines 933–935): after the draw, "Otherwise, the declarer discards one tile … and lays the remaining thirteen face up, to be judged under Hollow Specie". The discard can be any tile, so:
- a locked hand can change its shape;
- a one-shanten bluffer can *reach tenpai* and collect the doubled tenpai payment;
- a tenpai declarer can switch to a higher-value wait.

A.10 (lines 1013, 1016) speaks only of "completing the hand", and "where a bluff can pay" case (4) omits the draw that only reaches tenpai. *Fix:* decide whether a locked hand must discard the drawn tile (tsumogiri) on a Maturity Draw unless it completes, and whether a grace hand may discard any tile. Then correct A.10's wording ("reaching tenpai", not "completing") and the list of cases.

**S12. Appendix A leaves several standard cases undefined:**
- (a) Pon, chi and kan by a Paper declarer during grace ("the hand is not locked", line 870). Standard riichi forbids calls after riichi; grace is silent, and "the hand must be closed" applies only at declaration.
- (b) Ron on the declaring discard itself. For Gold Riichi the standard rule (stick not paid) applies; for Paper Riichi, does leverage apply to the declaration tile?
- (c) Abortive draws: four riichi (does a Paper Riichi count?), nine terminals, four winds, four kans, triple ron. If any is played, is there a Clearing for Paper declarers?
- (d) "Once per Paper Riichi, any opponent may" Assay (line 905): once in total or once per opponent?
- (e) Renewal "once the Syndicate is formed" (line 928): can a declarer renew against a single caller, and when S16 is off?
- (f) The Assay fee when the assayed declarer is only Audited at a Call against a different declarer ("another player wins", line 918, does not obviously cover a Call).
- (g) The fee when the assayed declarer commits chombo by holding a denied group.

*Fix:* one line each.

**S13. A.10's claims are not quite accurate.**
- (a) "Confession costs the same 4,000 as the Audit, so a noten Paper Riichi pays the same however the hand ends quietly" (line 1014). That holds only for a non-dealer: a dealer confesses 6,000 against a flat 4,000 Audit. And a confessor also pays the ordinary noten payments of the draw (line 896), which an audited declarer does not.
- (b) "Nobody will Call the baron, since a Call against a tenpai hand pays the declarer in Gold" (line 1010) is a non sequitur. A Call targets a Paper declarer, baron or not.
- (c) A.10 never weighs that a *tenpai* Paper Riichi takes back its notes at the Clearing, while a Gold Riichi stick stays on the table (A.1, line 810). Add that to grace's freedom to improve the wait and to the Clearing's 2,000 per note, and one-note Paper Riichi may come close to dominating Gold Riichi for a tenpai hand with spare Paper. Gold Riichi then keeps only ippatsu, payment Gold first, and the leverage risk.

*Fix:* correct (a) and (b). Add (c) to "What only play can settle".

**S14. Brochure prose remains from revisions 2–3.** Several passages still read as catalogue:
- A3.2 (line 238, "deepens a common sobriety toward nature");
- A3.5's "Cinema and *ma*" and "Concert halls" (lines 326–327, "routinely score *taiko*", "a recognizably oceanic voice");
- A3.6 items 3–4 (lines 336–337), with no rival or loser;
- A3.7's bullets after "Who loses" (lines 344–347, "decades before New York accepts trousers on women", "its own rival to Paris couture");
- A3.4's "Civic ritual" (line 312, "Stripped of titles in the cedar bathhouse…");
- the Pacific Modern feature list (lines 244–247).

The agon of revision 9 (D-30) was added beside these passages but did not change them. *Fix:* cut the superlatives and the bold. Give each surviving bullet its holder and its cost, as the "who loses" bullets do, or move them to the beats.

**S15. "Calms the silk belt" goes further than canon.** A5.4 (line 458): "Takahashi's July 1932 yen reset calms the silk belt". L1798 **[PROPOSED — CR-085]**: "The silk districts get no sudden prosperity, because the Union's depression has taken the buyers of raw silk." *Fix:* "eases the debt squeeze but brings no buyers back", or similar.

## Nits

- A2.1 item 2 (line 163): "the Marshall atolls … are cold lands". The Marshalls are tropical. Split the sentence.
- D-22 (line 748) points to "`A2.3` item 5". The rescue figure is item 6.
- D-24 and D-28 say twenty-eight grievances and "G1–G28". The table runs to G29 (D-31).
- G11 (line 414) points to `A6.2` for "Fleet-General and the Kuroda queen". A6.2 does not cover them.
- A6.1 (line 507): "first cousin to Silas's younger daughter" should be half-first cousin. Kiyotada is also Chiyo's nephew by marriage (she is his half-uncle Julian's wife), more exactly than "kinsman-by-marriage".
- A3.6 (line 335) cites the false-account rule to `CR-050`/`CR-051`. It is CR-049 (L242).
- A3.4 (line 288): Chico Hot Springs (Paradise Valley, Park County) is east of the Continental Divide, so in the Union. Glenwood Springs and Ouray are named as settler towns on Ute homeland that "can never be sold" (L665). "Ouray's people" (Uncompahgre) are not the Southern Ute who run Pagosa (line 301).
- The Winter 1926 set piece (line 566) pairs "Glenwood Springs" with a "Pueblo compact commissioner". Glenwood is Ute country.
- A3.3 (line 243): Greene & Greene were Pasadena architects, not "Bay Area timber pioneers". Line 285: Schindler reached Los Angeles in 1920, Neutra in 1925.
- A3.3 (line 271): "the Patrimony, which is paying, gives Ammann the bridge". Say through which arm (the Development Fund?) and whose decision the award is. The Patrimony's board cannot be instructed (CR-083).
- A3.6 item 4 (line 337): an annual series against Ralston College runs past 1910, when "Ralston College goes behind the wall" (L1288).
- A4.2 (line 364): Imamura was bishop of the Hawaii mission. California's Buddhist Mission of North America had its own head.
- A4.4 (line 374): what "Kiyoshi's 1907 rejection" has to do with mixed marriage is unclear. *Nyūfu* means a husband marrying into a house, not "foreign spouses".
- A5.6 and A2.2: the Gen'yōsha is a Fukuoka society. "Kagoshima's grievance" should be "Saigō's cause".
- A2.3 item 4 (line 183): canon has Proclamation Day "about 18 July 1932".
- A1.3 (line 152): 1870 to 1911 is forty-one years.
- A7 (line 534) lists Maybeck and Morgan twice.
- The 1899 set piece (line 571), "Satō Shōsuke, Sitka's fishery commissioner, and Ainu elders", reads as if Satō is Sitka's commissioner. Add "and".
- The Interface table (line 48) says this CR names no food or drink beyond cross-references, but A3.4 has tea, chile, coffee and barley water. These are harmless; adjust the claim.
- Appendix A, small points:
  - A.1 chombo says "no other exchanges … follow" (line 822), while A.4 and A.6 let the other player's win stand.
  - An all-drop Renewal raises honba "by one" (line 932), and "Afterwards" (line 941) may add another.
  - Karaten (line 937) ignores tiles shown face up in others' hands (Open Specie, Assay).
  - Gold Riichi's "at least 1,000 points" (line 804) should read "1,000 Gold".
  - Ranking ties are not addressed.
  - D-36's "One Truth, One Knife" does not appear in the Appendix.
  - The Appendix header says "Revision 13" inside revision 15, and D-36 quotes "revision 14" of the separate rules notes. This is confusing.
- Source notes still marked "to verify": Lava Hot Springs' cession year (1898 agreement, 1902 transfer); the Midway crater; the Golden Gate Park torii; Koga Masao.

## What works

- **A2.1–A2.2.** A Japanese statesman's case made "without one word of gratitude", with a named voice for it and a named voice against it in each era, all anchored in canon. This answers the author's question at its root.
- **A1.2.** Each Edo article with "what Japan gains" and "what the Republic gains". Capability instead of virtue makes Elias credible, and the panels "as a school" are a good idea.
- **A5.7.** Sacramento as the model case: a real grievance, a Japanese remedy won by leverage, and "the residue is a man".
- **The grievance catalogue.** It has four kinds of grievance. The Altai is held as a latent boundary, consistent with L1511, and the closing "Boundaries for the prose" keep the narrator neutral.
- **A3's losers.** Burnham's boulevards, Ōmori against Imamura, the *iemoto* houses, the *benshi*'s strike, the Pueblo that keeps its spring closed, the potters who sign their pots.
- **The Calculated.** Its origin is a challenge evening, and its creed comes from L242 ("a building states what it carries"). This is the best world-building in the CR.
- **Kiyotada and the key** (A5.11, A6.4). A Japanese Navy minister who knows he holds no key and accepts it for the reason of 1907 is a strong, quiet character note.
- **Shōkin-jan's design.** It maps the monetary doctrine onto play closely: cover, hot paper, the Leash, the Poison Pill, refinancing at twice the cost of default. A.10's habit of reasoning in the open and listing what only play can settle is the right one. The noten-penalty table and the A.10 figures (28,000 / 42,000; 4 han; the quarter thresholds) are arithmetically correct.
- **Checked against sources.** The cited canon checked out, including the 1927 rescue figure ($600m committed, $496.9m drawn, finance/CR-031-review.md), L1336's Ka Lōkahi trusts and L1752's consular courts.
