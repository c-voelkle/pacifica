# Fresh-context review: CR-088 revision 16 (branch draft/cr-088)

Reviewer context: fresh. Read only AGENTS.md, docs/authority-and-scope.md, CR-088.md (whole), the cited and affected lines of master_storyline.md, and entries in character_registry.json, ledger.toml and map_1887.toml. I checked every `L#### ("phrase")` citation by script: each phrase is on its cited line. The one difference is case only (L1752, "Consular jurisdiction"). I made light web checks on two claims (Kalākaua's prince, the French treaty). I did not read the writer's notes, earlier reviews, sessions or other branches.

## Verdict

**Not ready for approval yet, but close.** The narrative part (A1–A7) is consistent with canon on dates, ages, identities, authority and protected intent. The Altai, the Kronstadt gold and Noe's death are untouched. Kiyotada's age, descent and offices match L989, L1258, L1709, L1780 and L1792–L1794. Japan's agency is real and well argued in A2 and A5. One clause contradicts APPROVED canon (Ralston College "behind the wall" in 1910). Appendix A is much improved and mostly balances. Its money flows have payers and payees, and the three worked hands below settle. But it still has one direct contradiction between A.6 and A.7, and two undefined cases that will cause table arguments: the Syndicate's rounding after a drop, and whether leverage han count as a yaku. It also has one contradiction between A.1 and A.8 about when the game ends. Each is a one- or two-sentence fix. Once they are made, the CR can go to the author.

## Blockers

1. **Ralston College does not leave public sport in 1910.**
   - **CR:** `A3.6` item 4 (line 338): the Intercollegiate Series runs "against Ralston College until 1910, when it goes behind the wall".
   - **Canon:** L1288 (APPROVED CR-050/CR-050-R1). Ralston College goes behind the wall under the Compact of the Tuolumne, and "Its public life is unchanged". Only the inner circle is in the valley (CR-051).
   - **Problem:** this would carry a false fact into §26–§27 (Impact notes, line 554).
   - **Fix:** keep Ralston College in the Series through 1932, or say that its walled scholars stop travelling and the college's team plays on.

2. **The Category Knife and the Maturity Draw contradict each other.**
   - **CR:** `A.6` (line 917) and `A.7` (line 938).
   - **Problem:** after a "none", "any tile of [that group] drawn … on a Maturity Draw must be discarded". But A.7 says that if the Maturity tile "completes a winning hand, the declarer … wins". The cover-story tile is exempt from the denial ("does not count"). So a declarer can be denied a group and still wait on it. Example: the cover story is a lone 5-man, the knife names Characters, the declarer says "none", and the hand waits tanki on 5-man. Drawing the 5-man then both completes the hand and must be discarded. The same conflict arises on an ordinary tsumo during grace. A.6 also says holding a denied-group tile "at any reveal, a win included" is chombo, which leaves open whether the drawn winning tile counts as "hidden".
   - **Fix:** state one rule. Either a denied-group tile that completes the hand with the cover-story tile may be won on (by tsumo or on the Maturity Draw), or the cover-story tile cannot belong to the group the knife names.

3. **The Syndicate's arithmetic is undefined after a drop.**
   - **CR:** `A.7` The Syndicate (line 931), Renewal (lines 932–934), The spoils (line 945).
   - **Problem:** shares are "rounded to 100, with the remainder to the first caller", but the rule does not say whether that means rounding down or to the nearest 100. Thirds of 10,000 give 3,400/3,300/3,300 if rounded down. Thirds of 8,000 are 2,666.7: rounded to the nearest 100 they total 8,100, which leaves a negative remainder. After a Renewal the first caller is often the one who dropped, and their share is "retired". So nobody is named to receive the remainder of the doubled payment among the takers, which is 20,000/3 again. The spoils rule ("any odd note … to the first of them") also leaves open whether notes are split as points or as whole 1,000 slips. Two notes among three callers cannot be split as whole slips.
   - **Fix:** fix each caller's share as an amount when the Syndicate forms: round down to 100, remainder to the first caller. Each later payment is then that share times a multiplier (×1, ×2, or the hand value divided pro rata). Give the remainder to the first caller *still in the run*. Divide spoils as points, rounded down to 100, remainder to the first caller still in the run.

4. **Leverage han and the yaku requirement.**
   - **CR:** `A.5` Leverage both ways (line 880). Compare `A.1` Emergency Rate (line 822): "It is not a yaku".
   - **Problem:** the rules do not say whether the declarer's notes, added "as han" to the winner's hand, can serve as the winner's yaku. A player with no yaku who sees a Paper declarer discard a winning tile will claim ron, and the table will argue. This case comes up all the time.
   - **Fix:** add "Leverage han are not a yaku; they count only for a hand that already has one", or the opposite if that is intended. Change A.10's first bullet to match.

5. **When the game ends (tobi): A.1 and A.8 disagree.**
   - **CR:** `A.1` End (line 827): "Tobi counts only the Gold and Paper on the table (A.8)". `A.8` Totals (line 956): a player's total is Gold plus Paper "less any recorded shortfall; a player who carries a shortfall is below zero". S30 agrees with A.8. D-36's "tobi on the table only" is the older wording.
   - **Problem:** the two sections give different answers to whether a shortfall counts for tobi.
   - **Fix:** in A.1, say "Gold and Paper on the table, less any recorded shortfall; loans and printing debts do not count". Note in D-37 that it supersedes D-36's "tobi on the table only".

## Should fix

1. **Kiyotada's lesson of 1907 should be canon's.**
   - **CR:** `A6.2` (line 512) and `A6.4` (line 519): "dual loyalty survives only when you guard the boundary between the two crowns".
   - **Canon:** L1780 (APPROVED CR-026): "He learned in 1907 that a fleet cannot make a sovereign". The registry's `CT-KURODA-SON` profile says the same.
   - **Fix:** lead with canon's lesson and present the CR's wording as his gloss on it, so the character bible does not end up with two mottos.

2. **The order of payments when a payer runs out partway.**
   - **CR:** `A.3`, `A.8` Out of Gold and Shortfall.
   - **Problem:** some events produce several Gold-first debts at once. A Call found noten pays shares to each caller plus the bad note to the assayer. A locked noten declarer's deal-in pays the leveraged hand plus the Fraud Penalty. A payer whose Gold runs out on the first debt pays the later ones in Paper at two for one, so the order decides who receives Gold and who receives Paper (worth something only under cover). No order is given.
   - **Fix:** fix an order, for example (a) the hand or showdown payment, (b) penalties in the order listed in A.3, (c) payees in turn order from the payer. Or pay all simultaneous debts pro rata in each currency.

3. **A player with no Gold can Call or Assay at no risk.**
   - **CR:** `A.6` (fee "1,000 Gold"), `A.7`, `A.8` Shortfall (S30).
   - **Problem:** under S30 the reserve pays any shortfall in full. A player at 0 Gold and 0 Paper (who "continues") can therefore Call every Paper Riichi with no downside. If the declarer is tenpai, the reserve pays the declarer and the caller goes bust, which costs fourth place nothing (A.10 says as much). If the declarer is noten, the caller collects. The rules also let a player with no Gold pay the Assay fee in Paper at two for one (the fee is on A.3's Gold-first list), which leaves open what currency is "returned" later.
   - **Fix:** require at least 1,000 Gold in hand to Assay. Require Gold at least equal to the caller's share of the noten penalty in force to Call or join a Syndicate. Or bar players out of Gold from both.

4. **A.10's rescue example is wrong.**
   - **CR:** `A.10` Contested rescues (line 1032): a 7,000 offer is "enough for the borrower to declare three notes at once", against an earlier 5,000.
   - **Problem:** the 5,000 floor already passes the cover test for three notes (Gold of at least 3,000), and allows printing up to 10,000 under the 50% test.
   - **Fix:** give a real difference between the offers, for example the Gold-first cushion against the next deal-in, or room to Gold Riichi and Paper Riichi in the same hanchan.

5. **The "none" cannot always be checked.**
   - **CR:** `A.10` The Category Knife (line 1030) says the "none" "can be checked at the end". But `A.5` Clearing item 4 (line 910) sends an unpresented hand back "face down, unseen".
   - **Fix:** either a declarer who answered "none" must show the hand at the Clearing (or may not be left unpresented), or correct A.10.

6. **A third player's chombo.**
   - **CR:** `A.1` Chombo (line 826): "No rotation, no other exchanges".
   - **Problem:** the rules do not say what happens to a live Paper declarer's notes, a laid Assay fee, or a pending Open Specie check when someone else's false win ends the hand.
   - **Fix:** one sentence: notes and fee return to whoever laid them, and Open Specie is still checked.

7. **D-27's text is stale.**
   - **CR:** Decisions table, D-27 (line 756) still lists "freedom for the Hawaiian missions" as a condition. `A2.6` condition 3, `C-1919-MARSHALLS` and D-37 now say the clause names no mission.
   - **Fix:** add "(worship clause superseded by D-37)" to D-27. Revise D-17 the same way ("five historical figures"; `A7` now keeps many more in the background).

8. **The Ojo Caliente set piece contradicts A3.4.**
   - **CR:** `## C` (line 568): Chichibu in a "*rotenburo*" inside a "timber-and-adobe *ryokan*" at Ojo Caliente.
   - **Problem:** `A3.4` item 2 makes Ojo Caliente the Hispano *baños* that serve chile and coffee and that its users call "neither onsen nor *baño*".
   - **Fix:** move the scene to Pagosa (where the council's rules, women's hours and no photographs give it friction), or rewrite it as the Hispano bathhouse. As written the scene is also a postcard with no conflict.

9. **Nitobe's fourth point.**
   - **CR:** `A2.5` item 4 (line 206): "will one day be claimed by men who act in the Emperor's name against the Emperor's government. This is not a prophecy."
   - **Problem:** in a book whose climax is 15 May 1932, the line works as a prophecy whatever the disclaimer says. The disclaimer is the narrator arguing with the reader.
   - **Fix:** ground it in the past (Sakuradamon 1860, Saga 1874, Saigō 1877: men who claimed the Emperor against his ministers), cut "This is not a prophecy", and let the set piece's Peirce press him on it.

10. **Kiyotada's career between 1924 and 1932.**
    - **CR:** `A6.3`–`A6.4`.
    - **Problem:** he is Maria's reader at the Navy General Staff in Tokyo from 1920 (L1709). By 15 May 1932 he commands the western squadron's Japanese units (L1780). And "the reports he forwarded in 1931–32" (line 518) imply he still reads her reports. The CR never posts him from the Staff to the squadron, and never says how her reports and her warning reach him at sea. The registry already labels this posting PROPOSED.
    - **Fix:** add one line, for example a sea command from about 1928 with Maria's reports routed to him by name.

11. **Who awards the Gate bridge.**
    - **CR:** `A3.3` item 5 (line 272): "the Development Fund's board, which is lending for the bridge, awards it to Ammann".
    - **Problem:** a lender can make its loan conditional; awarding the contract belongs to the owner (a bridge district, the county, or the state).
    - **Fix:** the Fund makes its loan conditional on the Office's figures, and the owner awards the contract. Also align "the Realm's code" (lines 248 and 251) with canon's "the Polytechnic's earthquake code" (L1660), or say how the two relate.

12. **"Pacifica's crowns are Polynesian" overstates.**
    - **CR:** `A3.1` (line 232).
    - **Problem:** the Hawaiian crown is Polynesian. The Crown of Pacifica is a created crown held by Elias's son Julian, whose mother Noe was the daughter of a New England surgeon and a woman of a minor chiefly line (registry, CT-JULIAN-MOTHER).
    - **Fix:** say "Hawaii's crown is Polynesian, and the Realm's sovereign is the Queen's hānai son of Noe's Maui line". Cut the opening lecture sentence ("Japan could never culturally mirror …").

13. **Brochure passages remain.**
    - `A3.2`: "culturally legible … in a way Jacksonian Atlantic politics never was". It has no actor, and it is a claim rather than an event.
    - `A3.6` item 1: "Go embodies Pacifica's own strategic grammar…".
    - `A3.6` item 2's close: "Pacifica's signature game of diplomacy and crisis reading".
    - `A3.7`'s "dignified warm-weather attire" list.
    - `A4.1` ("showing cousins living as citizens … rather than humiliated contract labourers"). It has no friction: no Japanese government restriction, no recruiters' fraud, no emigrant debt. It also sits awkwardly beside Sacramento 1906.
    - **Fix:** give each of these a named actor with a motive or a loser (as `A3.3`–`A3.5` now do), or cut them back to the beats.

14. **Canon's "Prince Komatsu".**
    - **CR:** `## Sources`, Kalākaua (line 779): "whether the two are the same prince is to verify".
    - **Web check:** the prince of 1881 is Yorihito, styled Prince Yamashina (born Fushimi Sadamaro). He was adopted into Komatsu-no-miya in 1885 and became Higashifushimi in 1903 ([Wikipedia](https://en.wikipedia.org/wiki/Prince_Higashifushimi_Yorihito)). So canon's name is the same man by a later title. In 1881, "Prince Komatsu" most naturally means the adult Komatsu Akihito.
    - **Fix:** D-21 keeps canon's wording, so put a note in `historical_background.md` (as a source note, not a canon tension) so that no later writer marries Kaʻiulani's suitor to the wrong prince.

15. **The ledger: Japan as recipient.**
    - **CR:** `## E`, `C-1919-HAGUE` (line 597).
    - **Problem:** the revised `owes` line describes the Marshalls going to Japan but is still `by = "DE", to = "PAC"`.
    - **Fix:** add a separate `{ by = "DE", to = "JP", … }` line for the Marshalls. Consider whether Ka Lōkahi should be a party to `C-1919-MARSHALLS` for Nauru's trust.

## Nits

- `A6.4` cites `L1794` for the appointment with Saitō's countersignature. The sentence is at L1792 ("In July Julian names the common Navy minister's successor").
- `A3.6` item 2: the riichi declarer turns a *discard* sideways and puts down the stick. As written, the stick is laid sideways.
- `A3.3`: the Kabuki-za was still under construction on 1 September 1923. "Naitō's Industrial Bank and Kabuki-za stand" should say its frame stood.
- `A2.5` item 3: Japan "never adopted China's" examination is too strong. The ritsuryō state had one, and the bakufu ran *gakumon ginmi* from 1792. "Never kept" is safer.
- `A1.2` item 3: Hawaii's treaty of 1846 with France was replaced by the treaty signed on 29 October 1857 (ratification within ten months, in force twelve months after; [Punawaiola](https://manoa.hawaii.edu/punawaiola/?p=853)). "Still has" in 1858 is borderline; verify whether the new treaty kept the jury clause.
- `A1.2`: "Hawaii's negotiators" against L306, "California and the Tokugawa government conclude". Consider "the Confederation's negotiators, Hawaii's among them".
- `A2.3` item 2: "costs the army Liaodong". Canon (L1084) has no mainland cession ever on the table; "costs the army the mainland gains it hoped for" is safer.
- `A2.6`: Nauru lies south of the equator, so a division "following the equator" already gives it to Pacifica. "Carved out" makes sense only against the administrative unit (governed from Jaluit). Also, "Pacifica surrounds the group" overstates: the British Gilberts lie directly south (CR-084 keeps them).
- `A3.4` (line 289): "Lolo in Missoula County and Chico in Three Forks County, west of the line of 1865 though east of the divide". Only Chico is east of the divide. Chico's placement in 1880 Gallatin (Three Forks) checks out.
- `A3.6` summary: "every aborted run adds heavy honba". A.1 says honba rise "after every Call". Use the same words.
- A.9 S22: the setting now keeps other declarers' notes as deposits *and* audits them, so the alternative "Notes stay as deposits, no Audit" should read just "no Audit".
- A.8 Window: "taken in turn order from the dealer". Say the dealer of the next hand.
- A.10 Loans: "unless they also win Gold before settlement". Seizure happens at settlement, so this clause does no work.
- A.8 Shortfall: a Paper shortfall is repaid in Gold at par, while a player out of Gold elsewhere pays two Paper for one Gold. If the asymmetry is intended, say so in A.10.
- A.10 "What only play can settle": add whether the floor plus a deep shortfall (for example 6,900 + 5,000) can exceed every rival's Gold, which makes a Refusal to Print automatic.
- `## C` 1928 Shōkin-jan scene: "Carquinez / Tokyo back room". Pick one.
- `A4.5` has Kiyotada "take the common Navy's oath" at Thalassia; `A6.4` does not mention the oath.
- `A5`: the Kronstadt gold (CR-046: never told to Hirohito; Kiyotada never learns it) is a second latent fact beside the Altai. Consider naming it in G15's row or in the Boundaries paragraph.

## Worked hands (Appendix A)

These assume East round, no Emergency Rate and 0 honba unless stated. They use the rounding I propose in Blocker 3.

**1. Paper Riichi Call with a Syndicate and a partial-drop Renewal.**

Setup:
- South (non-dealer) declares Paper Riichi with 2 notes from his own stack. The noten penalty in force is P = 10,000.
- East assays for 1,000 Gold. The knife names Honours, and South says "none".
- In the window after South's first grace turn, West calls "Shōkin on South". North and East join.
- Shares are 3,400 / 3,300 / 3,300.

Renewal:
- South renews.
- West drops and pays South 3,400 Gold. His share is retired.
- North and East take.

Maturity Draw:
- South is still in grace and draws an Honour, which he must discard (A.6). He stays noten.

Showdown and settlement:
- South pays North 6,600 and East 6,600 in Gold.
- The spoils (2 notes) are split between North and East, 1,000 each.
- Bad note: East gets his 1,000 fee back plus 2,000 Gold from South.
- Honba +1. No rotation.

Result:
- South's net is −11,800 Gold and −2,000 Paper.
- Had he not renewed, he would have paid 10,000 + 2,000 = −12,000 Gold.

Every payment has a payer and a payee. The only gaps are those in Blocker 3. A design note to record in A.10: with three callers and k takers, a known bluffer's showdown cost is (3k − 3)/3 × P, so if only one of three takes, renewing costs him nothing but the notes.

**2. Below zero partway through a payment, then rescued.**

Setup:
- South round, Emergency Rate on, 1 honba.
- West holds 0 Gold and 2,000 Paper.
- North wins a 3-note Paper Riichi ron off West: tanyao 1 + 3 notes + Emergency Rate 1 = 5 han, a mangan of 8,000, plus 900 Gold for the honba.

Payment:
- West pays 2,000 Paper. The reserve credits North 6,000 Paper and 900 Gold.
- West's shortfall is 6,900, so his total is −6,900.

Window (offers begin with the player after West, so North first):
- The floor is 6,900 + 5,000 = 11,900 Gold.
- North cannot afford it. East offers 12,000.
- The reserve is repaid 6,900. West keeps 5,100 Gold and owes East 18,000.
- From the next hand the table plays at Emergency Rate, and the Leash takes West's Gold income.

This settles consistently under A.3, A.8 and S30. If no rival holds 11,900 Gold, the game ends (see the nit on the floor).

**3. Exhaustive draw with a Clearing presentment.**

Setup:
- South 1, Emergency Rate on, East is dealer.
- West has a locked 1-note Paper Riichi. East has a Gold Riichi.
- At the draw East and South are tenpai and North is noten. West says "tenpai".

Presentment:
- North presents first (turn order after West). West is noten.
- West pays North the noten penalty in force, 10,000 Gold, and North takes the note.
- If South had assayed, South gets 1,000 back plus a 1,000 bad note.

Standard draw payments:
- West and North each pay 1,500 (750 to each tenpai player).
- East's stick stays on the table. Honba +1. East keeps the deal.

If instead West was tenpai: North pays West 2,000 Gold, West takes his note back, and West counts as tenpai. All of this is consistent with A.5, A.6 and A.10's "confess or bluff" bullet.

**A3.6, the 1928 set piece, D-36 and D-37 against Appendix A:** they agree, apart from the D-36/S30 tobi wording (Blocker 5) and "aborted run" (nit). The set piece works:
- A 3-note bluff, renewed and taken, missing on the Maturity Draw, owes 24,000 doubled plus the 3,000 bad note. That plausibly leaves the attaché below zero.
- "Kashevarov speaks last" fits a seat directly before the attaché.

## What works

- `A2.1`–`A2.2`: Japan accepts for its own counted gains, in a Diet speech that needs no gratitude, with a named voice for and against in each era. This answers the author's question directly.
- `A1.2`'s two-halves structure makes Elias's motives about capability, not virtue. The four reasons for the mixed panels are concrete.
- `A5`'s four kinds of grievance, with holders, years and answers, give the domestic-politics CR a clean handoff. The Altai and Kronstadt boundaries respect canon (L1511, CR-046).
- `T-AINU-1` Case B keeps losers: 1870–99, the hunting country, the Diet's assimilationists. It gives the Diet Japanese reasons rather than Pacifican tutelage.
- `A3.3`–`A3.5` now have real rivals and losers: Burnham's architects, Ōmori against Imamura, the carpenters' union, the iemoto houses, the benshi.
- Kiyotada's cost (signing the postings that end his father's men's careers) and the key he does not hold are strong, quiet material.
- Appendix A is ambitious and almost playable: currency rules, cover, the Clearing and the Renewal economics (the quarter threshold checks out) hold together, and every number in the tables and in A.10 checks except the one in Should fix 4.
