# Fresh-context review: CR-088 Appendix A, *Shōkin-jan* (revision 17)

Scope read: `## Appendix A` (A.1–A.10) to the end of the file, the *Shōkin-jan* paragraph in `A3.6`, the "1928, Tokyo back room" set piece, and decision rows D-36, D-37 and D-38. Nothing else was read. For the base game I used my own knowledge of standard Japanese riichi: riichi.wiki is not on this session's allowlist, and a search did not return it. I did not run `tools/session.py start`, because it shows the last session's notes, which this review must not see. No repository file was edited.

## Verdict

**Not yet playable without table arguments, but close.** The core loop works, and its numbers check out: the stacks, cover, Paper Riichi with grace, leverage, the Category Knife, the Call with its queue, Renewal and the Maturity Draw, the Clearing, and the noten-penalty table. Hands (a), (b) and the first half of (c) can be played from the text alone, and every figure balances (60,000 Gold and 60,000 Paper are conserved). Seven gaps would still stop a real table:
- what a chombo does to a hand that ends by a draw or a Call;
- whether Refusal to Print voids every frozen claim or only the bust player's;
- the order of payment at settlement when a lender or claimant is also a debtor;
- the reserve's role on a run (S30 contradicts A.7);
- a run on a bank that is already on the Leash;
- what "collects" means for the Leash;
- what happens to Gold Riichi sticks when a third player's chombo ends the hand.

Each needs a sentence or two. There are also two balance problems. After any renewed run that is taken, Refusal to Print becomes close to automatic, so games will often end in East. And the reserve-backed Call, join and presentment give a hopeless player free options and a way to play kingmaker.

---

## Blockers

**B1. Chombo when the hand ends without a win** (A.1 "Chombo"; A.4 "Checking"; A.6 "none")
A.1 says "No rotation, no other exchanges and no honba follow", and the only exception is "where this appendix lets another player's win stand". But A.4 checks Open Specie "at the end of every hand, however it ends", and A.6 checks a denied group "at any reveal". So at an **exhaustive draw** (hand d) or at a **Call's showing**, a failed check is chombo, and the text can be read as cancelling all of these:
- the Clearing (confession, presentment);
- the noten payments;
- the honba rise;
- the dealer's seat;
- the Call's whole showdown.

It is also undefined what a Call "win" is: "if the declarer won, the win is void". If a declarer found tenpai at a Call is caught holding a denied tile, do the callers then collect the noten penalty?
*Fix:* add to A.1: "A chombo found at the end of a hand that ends in an exhaustive draw or a Call is paid besides that hand's settlement, which stands; the offender counts as noten for the noten payments, the dealer's seat and Hollow Specie." Add to A.6: "A named declarer at a Call who is found holding a denied tile counts as noten there."

**B2. Refusal to Print: whose frozen claims lapse** (A.8 "Refusal to Print" against "The moratorium")
The moratorium says that if no one rescues *the bank*, "its frozen claims lapse". Refusal to Print says that when *any* player below zero is refused, "the game ends at once … and any frozen claims lapse". So if a bank was rescued earlier and a different player busts later, it is unclear whether the bank's old claims are still paid in Step 2. In hand (c) this is worth up to 9,400 to E and N.
*Fix:* "…the frozen claims against the player refused lapse; all other frozen claims are settled in Step 2."

**B3. The order of settlement is not deterministic** (A.8 Settlement, Steps 1–2)
Step 1 repays shortfalls and printing debt "in Gold" before any Step-2 receipts. Step 2 pays "loans … then frozen claims" without saying which debtor pays first. When a player is both a debtor and a lender or claimant, the result depends on the order. For example, A owes a loan to B, A holds a frozen claim on bank C, and C owes a loan to A. If A pays B first, B suffers the Poison Pill even though A is about to receive Gold. Repeat rescues and runs make such chains likely. The same rule also makes a busted claimant's shortfall come off their score in Step 1 before their claim is paid in Step 2.
*Fix:* "Steps 1 and 2 are settled debtor by debtor in seat order from the hanchan's first dealer. Each debtor pays all of their Step 1 and Step 2 debts, in that order, from what they hold at that moment, including anything received from earlier debtors."

**B4. The reserve on a run: S30 contradicts A.7** (A.9 S30; A.7 "If tenpai"; A.8 "Shortfall")
S30 says the reserve pays in full "except on a run (S33)". A.7 says that against a tenpai bank "A caller who runs dry is covered by the reserve", and A.8 "Shortfall" has no exception at all. A table will argue about three payments:
- a dropper at a Renewal who cannot pay the bank;
- an other declarer's Fraud Penalty at a Call;
- a caller who runs dry against a tenpai bank.

*Fix:* in S30 (and add the same words to A.8 "Shortfall"), replace "except on a run" with "except the payments a noten bank owes its queue and its assayer on a run (A.7)".

**B5. A run on a bank that is already on the Leash** (A.7 "If noten"; A.8 "The Leash" and "Totals")
There are two gaps:
- *During the run:* the Leash sends "all Gold the borrower collects from any exchange" to the lender first. That includes droppers' Renewal payments (and an Assay fee won). Read that way, a leashed bank's drop income goes to its lender rather than into the vault that pays the takers. The amounts differ by tens of thousands.
- *After the run:* Totals counts frozen claims only "until a rescue loan is accepted". A bank that was rescued before has already accepted one. So its new claims arguably do not count, it is not below zero, and a broke bank is never tobi.

*Fix:* "Gold paid to a bank during its own Call goes into its vault and is paid to its queue before the Leash takes anything. Frozen claims from a new run count against the bank's total for the Window that run opens, whatever loans it already carries."

**B6. "Collects" under the Leash is undefined** (A.8 "The Leash"; A.8 "The moratorium" "Gold income")
It is unclear whether a borrower who wins with Gold Riichi "collects" their own returned 1,000 stick, a returned Assay fee, or the deposits. In hand (c), this decides whether S keeps 5,000 or 4,000 Gold, and so whether S can declare riichi next hand. It will come up every time a borrower wins after a Gold Riichi.
*Fix:* "Gold income is Gold received from another player, the reserve or the table's deposits. The borrower's own stick or fee returned is not income."

**B7. Gold Riichi sticks on a third player's chombo** (A.1 "Chombo")
A.1 sends Paper notes back and the Assay fee back, but says nothing about Gold Riichi sticks laid in the hand that the chombo voided. Under A.3 "Deposits", they would sit on the table as deposits for the next winner. Most riichi rule sets return them to their owners.
*Fix:* add "and every Gold Riichi stick laid in the hand returns to its owner".

---

## Should fix

1. **The 1928 set piece contradicts A.7 and A.8.** "an offer must clear his shortfall and leave him 5,000 Gold" is wrong under revision 17. A noten bank on a run has frozen claims, not a shortfall ("The reserve pays nothing on a run"), and "A rescue loan does not pay it". *Fix:* "an offer need only leave him 5,000 Gold; it pays none of his frozen claims, which wait behind the lender."
2. **The Clearing with several declarers** (A.5 "The Clearing"):
   - The text does not say in what order the presentments against two "tenpai" declarers run. It matters, because a presenter who loses Gold on the first presentment may not hold Gold for the second.
   - It does not say whether another Paper declarer, or one who has just confessed, may present ("each opponent" suggests yes; say so).
   - It does not say whether a confessor's hand is shown. If it is not, confession hides a false "none" and a karaten-based check.

   *Fix:* "Presentments run declarer by declarer in turn order from the dealer; any opponent, a Paper declarer included, may present; a confessing declarer's hand is not shown."
3. **Frozen claims a player holds** (A.8 "Totals"): Totals lists "Loans, whether owed or owed to them" but not frozen claims owed *to* a player. Add "and frozen claims owed to them". Also state that a claim repayment received by a leashed claimant goes to that claimant's lender.
4. **Interest** (A.8 "Interest (S18): fixed at 50%"): per hand, per round, or once? The Leash's "until principal and interest are repaid" suggests once. *Fix:* "a flat 50% of the principal, charged once".
5. **Balance: Refusal to Print becomes automatic after a renewed take.** At the starting stacks, a player can meet Gold-first debts up to 15,000 + 15,000 ÷ 2 = **22,500**:
   - every renewed take on 1 note (16,000) or 2 notes (20,000) empties a taker's Gold (hand b: both takers end at 0 Gold);
   - a renewed take on 3 notes (24,000) puts the taker **below zero**.

   After a tenpai massacre, the Gold sits with the bank, which is now the leader and will refuse to lend. The other players rarely hold 5,000 Gold plus any shortfall. So Refusal to Print, and the end of the game in East, is the expected result. A.10 lists this only as a question ("whether a deep shortfall makes the floor larger…"). *Fix options:*
   - adopt S34's alternative for **taking** at a Renewal (Gold at least equal to the doubled stake);
   - or cap any one player's loss at a Call at their Gold plus half their Paper;
   - or let the reserve lend at the floor when no rival can.
6. **Balance: free options for a hopeless player.** S34 lets a player with 100 Gold call, join, take or present. If the bank or declarer is tenpai, the reserve pays them in full in Gold, minted from nothing, and the player who went below zero loses nothing, because "Fourth place loses the same uma whether or not they go bust". So the last player can:
   - join every run;
   - present every declarer;
   - end the game at a chosen moment;
   - and steer reserve Gold to one rival (kingmaking that "No other deals" cannot stop, since no deal is needed).

   A noten bank's liability, by contrast, is capped at its vault, so a near-broke declarer's bluff is a limited-liability bet. *Fix:* require Gold at least equal to the stake (S34's alternative) to call, join or present, or make the moratorium symmetric (no reserve cover for callers either).
7. **Balance: the zombie bank.** After a rescue, a bank whose frozen claims exceed what it can hope to win plays for nothing: every Gold point goes first to the lender, then to its claimants, and its settlement score stays 0 (hand c). It becomes a free kingmaker. *Fix:* either let claims still unpaid at settlement come off the bank's score (so it still plays for rank), or cap frozen claims at the bank's starting stack.
8. **Balance: a one-note tenpai Paper Riichi dominates Gold Riichi.** A.10 already asks this; the case is stronger than it lets on. A tenpai one-note Paper Riichi has all of these:
   - the same 1 han;
   - tedashi in grace;
   - a raise option;
   - **its note back** at a draw, where a Gold stick is lost to the deposits;
   - a Call against it that pays **at least 8,000 Gold**.

   Gold Riichi keeps only ippatsu, a Gold payment and no leverage. *Fix:* at an exhaustive draw, the notes of a declarer counted tenpai (shown or unpresented) stay as deposits, like a Gold stick.
9. **Balance: lenders harvesting a borrower's uncovered Paper.** A lender with spare cover can lend a large principal (for example 30,000) to a Paper-rich player who is out of Gold. At settlement the lender seizes the borrower's uncovered Paper "at par", which is worth nothing to the borrower, and gains up to the 50% interest in score at no cost to the borrower. *Fix:* seized Paper counts at half, or the principal is capped at the floor plus, for example, 5,000.
10. **The A.10 Maturity Draw arithmetic** ("roughly fourteen live tiles among the fifty-odd unseen"): from the declarer's seat, the unseen tiles are the 39 in opponents' hands, the 14 in the dead wall and the live wall. That is fifty-odd only in the last few draws. In the grace window it is about 85–95, so a quarter needs about 22 live tiles. Also, a **locked noten** hand has zero chance (13 tiles that are noten cannot be completed by one draw). "A disciplined declarer one tile from tenpai … may renew even when caught" is therefore true only in grace. Say so.

## Nits

- A.1 "Chombo" list: add "a false 'none' under the Category Knife (A.6)".
- A.1 exhaustive draw, two tenpai: say who pays whom (each noten player pays 1,500 to one tenpai player, or 750 to each).
- A.1 "End": state the hanchan's natural end (after South 4; West extension or not; agari-yame or not), and whether a Window opens after the last hand.
- A.2: Paper needs slips smaller than 1,000 (hands such as 7,700 are paid Paper first, and steps of 100 at two for one). Name the denominations. "Zero-prop" in A3.6 also needs a score sheet.
- A.4: say whether Open Specie is still checked if the declaring discard is claimed by ron and the riichi fails.
- A.5: say outright that a declarer still in grace when the wall runs out is judged at the Clearing like any other declarer. The Clearing has no grace exception, unlike the Audit.
- A.6/A.7: whether completion on the Maturity Draw is compulsory. Discarding a winning tile makes the hand furiten, so it is compulsory in effect; say so. Doubling the Bill on the Maturity Draw: say "no".
- A.7 Timing: "each eligible opponent gets exactly one chance". A pon or chi can skip an opponent's turn. Say "each eligible opponent whose turn falls in the window".
- A.7: define "vault" as the bank's Gold and Paper in hand, not its staked notes or a laid Assay fee.
- A.9 S13: say "two tiles exposed, at least one part of the wait"; as written, "One exposed tile" reads as one tile exposed.
- A.10 "The teller's queue": "three takers on a renewed run can owe 60,000, the whole table's Gold". That is the *minimum* on two notes (3 × 20,000). On three notes it is 72,000. And the takers hold at most 45,000 Gold of the 60,000. Reword.
- A.10 "Renewal": the "quarter" holds for the head of the queue against a solvent bank, valued at the minimum. Later in the queue, or against a big hand, the threshold is higher. Add one clause.
- A3.6 "any rival may present the note": the rule is the first opponent in turn who holds Gold.

---

## Worked hands

Seats: E (dealer), S, W, N; turn order E→S→W→N. East 1, honba 0, no Emergency Rate. Everyone has 15,000 Gold / 15,000 Paper unless stated. G = Gold, P = Paper.

### (a) Two-note Paper Riichi, assayed, three callers, renewed, first drops, two take; declarer noten

- S declares with 2 own notes: S has 15,000 G / 13,000 P, and 2,000 P lies on the table. Cover: 15,000 ≥ 2,000 ✓.
- N assays: lays 1,000 G (N has 14,000 G). The knife runs as in A.6.
- After the lock, on W's turn, W calls "Shōkin on South". Joins in turn order from W: N joins, E joins. Queue: **W, N, E**. All three hold Gold and none is an active Paper declarer ✓. N is both assayer and caller (allowed: Assay and Call fall on different turns).
- Noten penalty in force: 2 notes, non-dealer, East = **10,000**. Renewed showdown = **20,000** per taker.
- S renews. W **drops**: pays S 10,000 G (A.3 Gold first). W has 5,000 G. N and E **take**.
- Maturity Draw: S draws. A locked noten hand cannot be completed by one tile, so it must discard. S shows: **noten**.
- S's vault: 25,000 G / 13,000 P. Payments in queue order:
  - N: 20,000 G, paid in full. Vault: 5,000 G.
  - E: 5,000 G, then 13,000 P at two for one (= 6,500). E is still owed 8,500, which becomes a **frozen claim**.
  - Bad note to assayer N (A.6): the fee of 1,000 G comes back from the table. Then 2 × 1,000 = 2,000 from the vault, which is empty, so N holds a **frozen claim of 2,000**, written after E's.
- Spoils: S's 2 notes (2,000 P) go to N, the first caller still in the queue.
- Honba becomes 1. No rotation. No honba are paid at a Call.

| | Gold | Paper | Frozen claim held | Total for tobi |
|---|---|---|---|---|
| S | 0 | 0 | owes 10,500 | **−10,500** |
| W | 5,000 | 15,000 | — | 20,000 |
| N | 35,000 | 17,000 | 2,000 | 52,000 |
| E | 20,000 | 28,000 | 8,500 | 48,000 |
| Check | 60,000 | 60,000 | | |

S goes to the Window. Floor: no shortfall, so a loan must leave S with at least 5,000 G. Offers come from W (who holds 5,000, so can offer at most 5,000), then N, then E. If the game ended now, the scores after Cover would be N 52,000, E 40,000, W 10,000, S 0. N leads and should pass, giving up its 2,000 claim. E is the natural lender.

(If the Call had come in the grace window, the money would be the same. The only difference is that the Maturity Draw could keep the tile and reach tenpai.)

### (b) As (a), but the declarer is tenpai

- The hand is worth, say, 2 han and 40 fu as a ron, which is 2,600, so the minimum of 10,000 applies. Renewed: 20,000 per taker.
- W drops: pays S 10,000 G. S declines the draw and shows tenpai.
- N pays 20,000: 14,000 G, then 6,000 at two for one = 12,000 P. N ends at **0 G / 3,000 P**.
- E pays 20,000: 15,000 G, then 5,000 at two for one = 10,000 P. E ends at **0 G / 5,000 P**.
- The Assay fee of 1,000 G goes to S. S takes back its 2 notes. Honba becomes 1, with no rotation.

| | Gold | Paper |
|---|---|---|
| S | 55,000 | 37,000 |
| W | 5,000 | 15,000 |
| N | 0 | 3,000 |
| E | 0 | 5,000 |
| Check | 60,000 | 60,000 |

"One taker runs out of Gold" cannot happen alone here: at the starting stacks, **every** taker on a renewed take runs out, because 20,000 is more than 15,000. Windows open for E and then N (in turn order from the next dealer, E, since there is no rotation). Neither is below zero, so both may decline and play on, but with no riichi, no Call and no presentment. Only S (the leader) and W (5,000 G) can lend. The first shortfall either player then suffers will put them below zero, and the floor of 5,000 plus that shortfall will be more than W holds. This is Should-fix 5 in practice.

### (c) The bank from (a) is rescued, wins in Gold, and the game is settled

- At the Window, E lends S **5,000 G** at 50%, so S owes 7,500. Frozen claims now count only at settlement (E 8,500, then N 2,000). Emergency Rate applies to the next hand.
- Next hand (East 1, honba 1, Emergency Rate): S declares Gold Riichi (stick 1,000 G, leaving S 4,000 G) and wins by ron off N:
  - riichi + pinfu + tanyao + Emergency Rate = 4 han 30 fu = **7,700**;
  - plus 900 honba;
  - N pays **8,600 G**.
- The Leash takes all 8,600 (assuming S's own returned stick is not "income"; see B6):
  - 7,500 to E, and the loan is cleared;
  - 1,100 to the frozen claims in queue order, so E's claim falls to 7,400;
  - S keeps 4,000 + its stick of 1,000 = **5,000 G**.
  - (If the stick counts as income, S keeps 4,000 and E's claim falls to 6,400. The settlement result below is the same either way, because the extra 1,000 reaches E later.)
- After the hand: E 23,600 G, N 26,400 G. The dealer rotates to S, honba returns to 0, and Emergency Rate ends from the next hand (still East).
- Assumed last hand: W declares Gold Riichi and is the only player tenpai at an exhaustive draw. E and N pay W 1,000 P each; S, with no Paper, pays 1,000 G. W's stick (1,000 G) stays as a deposit.
- Holdings at the end:
  - S: 4,000 G / 0 P
  - W: 5,000 G / 17,000 P
  - N: 26,400 G / 16,000 P
  - E: 23,600 G / 27,000 P
  - on the table: 1,000 G
  - Check: 60,000 G / 60,000 P ✓
- **Step 1:** nothing to repay.
- **Step 2:** no loans remain. Frozen claims in queue order:
  - S pays E 4,000 G, and has no Paper to seize;
  - E loses the last 3,400 and N loses its 2,000 (the claimants' loss).
- **Step 3 (Cover):**
  - E: 27,600 + 27,000 = 54,600
  - N: 26,400 + 16,000 = 42,400
  - W: 5,000 + 5,000 = 10,000 (12,000 P uncovered)
  - S: 0
- **Step 4:** the 1,000 G deposit goes to E, giving E 28,600 G / 27,000 P = 55,600.
- **Step 5 (uma):** **E 70,600; N 47,400; W 5,000; S −15,000**. The uma sums to zero, and the 12,000 that vanished is exactly W's uncovered Paper.

### (d) Exhaustive draw: two Paper declarers (one confesses, one is presented) and a Gold Riichi with Open Specie whose check fails

Setup:
- S: Paper Riichi, 1 note (15,000 G / 14,000 P).
- W: Paper Riichi, 2 notes (15,000 G / 13,000 P).
- N: Gold Riichi with Open Specie (14,000 G, stick on the table).
- E: no riichi, tenpai.

Clearing, in turn order from the dealer: S, then W.
1. S says "noten" and **confesses**: 4,000 G paid like a tsumo (W 1,000, N 1,000, E 2,000). S's note becomes a deposit.
2. W says "tenpai". In turn order after W: **N presents**. W is karaten, so noten: W pays N **10,000 G**, and N takes W's 2 notes.
3. N lays down the hand. Neither exposed tile is part of the wait, so **chombo**.

Reading the chombo as paid besides the draw (the fix proposed in B1), with N counted noten:
- Noten payments (only E tenpai): S, W and N pay E 1,000 each (payer's choice; all pay in Paper).
- Chombo: N pays 2,000 to S, 2,000 to W and 4,000 to E, Gold first.
- N's stick (1,000 G) and S's note (1,000 P) stay as deposits. E keeps the seat.
- Honba: "+1" from the draw clashes with "no honba follow" from the chombo. This is B1 again.

| | Gold | Paper |
|---|---|---|
| S | 13,000 | 13,000 |
| W | 8,000 | 12,000 |
| N | 17,000 | 16,000 |
| E | 21,000 | 18,000 |
| Deposits | 1,000 | 1,000 |
| Check | 60,000 | 60,000 |

Under the literal reading of A.1 ("no other exchanges"), none of the confession, the presentment or the noten payments would happen; only the chombo would be paid. N, the offender, would then lose the 10,000 it won by presenting. Which reading applies, and whether N counts tenpai or noten for the draw, is not answered by the text: **B1**.

---

## Arithmetic checked

- Noten-penalty table: 8/10/12 (dealer ×1.5 = 12/15/18); Emergency Rate +2,000 or +3,000 = 10/12/14 and 15/18/21 ✓.
- Exhaustive-draw payments total 3,000 in every case ✓.
- Chombo 8,000/12,000 ✓. Confession 4,000/6,000 ✓.
- Floor examples: 5,000; 2,000 + 5,000 = 7,000; 5,000 with 38,500 in frozen claims ✓.
- Shortfall example: 2,000 P plus 10,000 from the reserve in Paper ✓. Out-of-Gold example: 1,000 G + 14,000 P ✓.
- A.10:
  - 72,000 = 12,000 × 2 × 3 ✓; 108,000 = 18,000 × 2 × 3 ✓;
  - 28,000 = 14,000 × 2 ✓; 42,000 = 21,000 × 2 ✓;
  - 60,000 = 10,000 × 2 × 3: right only as the two-note minimum (nit);
  - 3 notes + Emergency Rate = 4 han ✓; tanyao + 3 + 1 = 5 han ✓.
- Renewal threshold: taking is worth p·2N − (1−p)·2N, dropping costs N, so take when p > ¼ ✓ (with the caveats in the Nits).
- Maturity Draw for the declarer, all callers taking: q·2N − (1−q)·2N ≥ −N gives q ≥ ¼ ✓. The "fifty-odd unseen" figure is wrong except late in the hand (Should-fix 10).

## Consistency with A3.6, the 1928 set piece and D-36–D-38

- D-38 correctly supersedes D-36's "tobi on the table only" and D-37's equal shares and divided spoils. A.1, A.7 and A.8 follow D-38. Every D-37 item (bad note in grace, other declarers' notes kept as deposits, two for one in steps of 200, a Paper declarer's deal-in paid Gold first, a locked hand discarding on the Maturity Draw) is in the text. A.9 matches the rules except S30 (B4) and the wording of S13 (nit).
- A3.6 matches the rules; one nit ("any rival may present").
- The 1928 set piece is right in its sequence (3 notes, knife on Honours, banker and Kiyotada in the queue, renewed and taken, the miss, offers in turn with Kashevarov last). Its "clear his shortfall" is wrong (Should-fix 1). Note also that Kashevarov, the assayer, holds a frozen bad-note claim of 3,000, which gives him a motive to rescue: useful for the scene.

## What works

- The **teller's queue with the moratorium** is clean and playable: queue order, vault order, the bad note after the queue, spoils to the head of the queue. Hand (a) settles to the last 100 without a judgement call.
- **Full cover with Paper at par for tobi but capped at settlement** gives the hot-paper and baron dynamics A.10 claims. Hand (c) shows Paper evaporating exactly as designed.
- **The Category Knife** is fully specified: the cover-story tile is barred from the named group, "none" freezes the group, the discard tell, and the fee's fate in every outcome. I found no hole in it.
- **Grace furiten** (temporary until the lock, riichi furiten after it) and the **Hollow Specie** test are precise.
- **Renewal plus the Maturity Draw** is a working doubling cube: the drop is priced, and the take threshold of a quarter is correct.
- **The order-of-payment rule** (A.3) settles who is paid in Gold and who in Paper when a payer runs short.
- The **leverage** and **Gold first on a declarer's deal-in** rules make three notes genuinely dangerous, as A.10 intends.
