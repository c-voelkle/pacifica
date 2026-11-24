# CR-083 — second fresh-context review

**Second fresh-context review of CR-083, revision 5, 22 November 2026. The reviewer read the draft, AGENTS.md and current canon, and not the writer's notes or earlier reviews.**

**Verdict.** Not ready to integrate. The fork of 1871 and the Canadian side are close, but four things stop it besides the water round: Caledonia has no constitutional form, the settlers who are meant to carry the vote may not be on the roll, the water is pledged before the nations who own it have agreed, and Japan's side of the Hayama bargain is still too contingent for a strong Japan to sign. Each has a fix inside the approved decisions.

Checks run: `cr_facts.py preview` lists 9 passages in canon (AGENTS.md 115; storyline 91, 708 twice, 1137 twice, 1142 twice, 1554) and 14 in the draft itself. `lint_canon.py --only` is clean. Line numbers below are the storyline's on this branch today.

## Blockers

**B1. Caledonia has no constitutional form, and "what Hawaii has" is not what canon gives Hawaii.**
- *Passage:* A10, A11 ("Caledonia has what Hawaii has, a crown, a legislature and a place inside the Realm's count"; "the Senate passes the Act of Union in December 1931, narrowly").
- *Problem:*
  - Hawaii is inside the 124 counties. Canon 914: "California and Hawaii remain historic lands with entrenched language and tenure guarantees". Canon 1033: "Hawaiian counties with large Japanese populations become trilingual in 1928". Canon 927: "County boards choose one senator each … with twelve Polytechnic seats and eight aliʻi seats. The elected lower house becomes the Chamber of Deputies."
  - Canon 1234 gives every crown three things the draft does not give Caledonia: "Each crown keeps its own legislature, language of the Crown and coronation … A Kuhina Nui in Honolulu and a Lugarteniente General in Manila govern day to day in the Sovereign's name".
  - So the draft does not say who governs at Victoria (a lieutenant? a Commissioner? the premier?), whether the premier answers to his legislature when canon 927 says the Realm's ministers "answer to the ruler, not the Chamber", who chooses Caledonia's senators, whether it sits in the Chamber of Deputies, whether the Franchise Law of 1888 (987) and the Office's posted officers (1005) run there, whose the customs, the courts of appeal, the militia and Esquimalt are, and whether Caledonia keeps its own budget. A13 and B assume it keeps a treasury and a debt.
  - The Act's passage is under-specified. In 1907 "Senate and Chamber confer the Realm's sovereignty by two-thirds" (1232). In 1928 the Concord needed "two-thirds Senate consent" (1604). A new crown, a territory outside the 124 and new Senate seats change the Constitution; the terms of union and the treaty with Canada are treaties. "The Senate … narrowly" names one chamber and no threshold.
- *Fix:* one paragraph in A11. The least-cost form, from canon's own parts: Caledonia is a crown land inside the Realm's citizenship and count, outside the 124, on the Philippine crown's pattern at home (its own legislature, budget and debt, a lieutenant at Victoria governing in the Sovereign's name) and on Hawaii's pattern abroad (the Realm's customs, forces, Court and floors). Say whether the plural franchise applies to its elections, who names its senators (its legislature is the obvious body), and that it has seats in the Chamber or none. State that the Act of Union passes both chambers by two-thirds, narrowly. That makes the sufficers' defeat a real count: they need one third and fall short.

**B2. The settlers who carry the vote may not be on the roll.**
- *Passage:* A5 ("Sixty years of the railway south and free entry have settled Pacificans in the interior"), A7 ("taken … on the dominion's own roll, under the dominion's own law … the interior carries the vote").
- *Problem:* a British dominion's roll is a roll of British subjects. Pacifican settlers are aliens until they naturalise and swear to the King. The draft's majority rests on the interior, and the interior's Pacificans are either not voters, or voters who took a British oath and now vote the King out. The draft says neither. The same question governs the legislature that offers the crown: if the interior's Pacificans vote, how did Victoria's race laws and an Islander premier survive them to 1930; if they do not, who in the interior votes yes?
- *Fix:* decide it and say it. The stronger story is that most did naturalise (a miner's or a homesteader's title required it), that the Island calls the vote a foreigners' vote, and that the terms of union therefore let any resident keep British nationality by declaration within a year. That gives the Island's no a legal afterlife and makes the narrow yes believable without changing N-10. Tolmie, an Islander, then leads an offer his own island refuses; give him the reason (the treasury) and the cost (his seat).

**B3. After the renewal of 1932 Japan holds too little that is certain.**
- *Passage:* Part H, J-2, J-4, J-5; the calendar.
- *Problem:*
  - Canon 1734: the renewal puts "Japan's overseas commands … to common control at the price of renewal", "the naval party loses its reserved squadron", and "Japan's demand for an alternating executive is refused". Against that the draft gives Japan a shore station on another crown's land, the chair of a pool that holds no oil until the Dutch sign, and a resolution by which a Pacifican Foreign minister will "seek" a treaty with a fleet forbidden to fire, blockade or land. Julian's gain (a country, a river system, about 0.7 million citizens) is certain on 1 January 1932. Japan's main gain depends on a third party's consent and on its partner's good faith in pursuing it.
  - J-5 says in terms that "Julian's lever of 1931 … survives". The lever was used on Japan a few weeks before the Council (1720: "Julian threatens the resources Tokyo cannot easily replace: oil from Pacifica and the Gulf Republic"). A strong Japan does not accept, as its prize, an oil route whose allocation stays with the ministry that has just threatened it.
  - Authority at Hayama does not match canon. Canon 1651: "Julian convenes, sets the agenda and presides with the common ministers, without their national ministers." There is no "Japan's delegation" at the Council to ask in 1928 or name a price in 1930, and no "Realm's delegation" to undertake anything; delegations sit at Thalassia (1602). Japan's cabinet also changes between the resolution and the union: Wakatsuki's in the autumn of 1931 (1720), Inukai's by May 1932 (1732).
  - Sequence. "Japan consents before the settlers vote, so Julian signs nothing he cannot honour" is contradicted by the calendar: the terms of union are signed in the spring of 1931 and Japan consents in the autumn. The Cortes's vote and Ka Lōkahi's extraordinary sitting, on which the resolution depends, have no date at all.
- *Fix (inside J-1 to J-6):*
  1. Give Japan something certain. Until Indies oil reaches the pool, the oil trust supplies the pool the guaranteed tonnage at the fixed price of J-2(1). That is the trust's objection in the Senate, and it now has weight.
  2. Give the chair a power. No allocation to the common fleet is reduced without the chair's countersignature. The lever of 1931 survives against a national army acting outside common command, which is the only case canon needs.
  3. Use canon's own clock. 1734 ends "Japan may refuse in 1937". Write the Dutch treaty into the renewal as a matter reviewed in 1937. Japan then holds a date, and Julian has a reason to deliver.
  4. Name who speaks: the Japanese Navy minister, a common minister, raises the Indies in 1928 and 1930 with the Emperor's leave; the resolution of 1931 is the two crowns' act, countersigned by Japan's prime minister as common appointments are (1597), and it is recited in the renewal's instruments of 1932 so that the next cabinet inherits it.
  5. Put the Cortes's vote, Ka Lōkahi's sitting and Japan's agreement in principle before the terms of union are signed, or change the sentence.

**B4. The water is disposed of before its owners agree, and the debt hangs on their yes.**
- *Passage:* A7 term 6, A8, A13, Part B ("Two rents"; "the bankrupt dominion's one asset large enough to refund its debt").
- *Problem:*
  - The terms of union are signed and published in the spring with "the northern water and its rent" in them. The lessor nations sign in the summer and ratify in November. For some months the Crown and a settler legislature have published a bargain over water on country that, by the draft's own account, was never ceded. Canon's rule (AGENTS.md, CR-070) is "no land is granted on a nation's country without its compact"; 695: "the nation leases and does not sell".
  - The "wayleave" to Caledonia's treasury assumes the dominion owns the soil the canal crosses. The compacts assume the nations do. In a country with no treaties that is the whole land question, and the terms do not answer it.
  - The settlers' main reason to vote yes is that the water refunds their debt. Every settler therefore has a money interest in the Sekani, the Kaska and the Dane-zaa saying yes in one summer. The draft does not draw this, and no nation refuses anything except the larger plan. Canon shows what a real choice looks like at 1137: "The Chilkat of Klukwan refuse, and their pass stays theirs and closed".
  - The refunding is secured on works whose engineering is open (Part B) and which are "built in stages after 1932".
- *Fix:*
  1. Reword term 6: the terms bind the Crown and Caledonia to build nothing and pledge nothing on a nation's country before its compact, and they recognise the nations' title where no treaty exists. The legislature's price for that recognition is the wayleave.
  2. Make the wayleave a share of the power sold from works on leased ground, paid by the Realm's power estate, so it does not rest on a title the terms have just conceded.
  3. Let one lessor nation refuse or cut its waterline in 1931, so that the first stage is smaller than the terms hoped and the legislature at Victoria has a grievance on its first day. N-7's 20 km³ stays the planned first stage.
  4. Secure the refunding on more than the water: the dominion's existing half of the Columbia's downstream power (1554: "a compact gives British Columbia half of the extra power its storage makes downstream") is already flowing and is the natural first security.

## Should fix

**S1. The remitted instalment collides with the moratorium.**
- *Passage:* A6 ("an instalment of its gold-dollar debt to Pacifica is remitted").
- *Problem:* canon 1693: "Hoover's June 1931 war-debt moratorium restrains forced selling, and debt is restructured." An instalment already suspended is no price. The ledger's own note on C-1923-UK-FUNDING leaves the moratorium's effect open.
- *Fix:* London's price is a cancellation of principal, a stated number of the sixty-two annuities of 1923 (1385). It also settles part of OPEN-019-05, since the cession is payment in kind. That entry and item 26 at 1861 belong in Part C.

**S2. Westminster's Act and the Statute of Westminster.** Canon 1752 dates the dominions' treaty "After the Statute of Westminster". A dominion of 1907 falls under the Statute (11 December 1931, from memory), under which London legislates for a dominion only at its request. The draft's "Westminster's Act" of December 1931 should be that request answered. It also gives London a second motive: refusing a dominion's request in the month it passes the Statute would cost it the other dominions.

**S3. Canada's option needs Ottawa's own decision.** A6 has London offer "union with Canada" and A7 puts it on the ballot. Nothing says what Ottawa offers. In 1931 Ottawa is carrying the prairie's relief and its wheat stocks and cannot assume a gold-dollar debt owed in San Francisco. Let Bennett decline to make terms. Then the option fails by Canada's interest, the treaty of December follows from the same decision, and the vote is less convenient for Julian because the Island can say Canada was never really offered.

**S4. The Canadian Pacific without British Columbia (A3; canon 708).** History's line was the price of the province's entry. The draft keeps the line and the quiet money and marks the builder OPEN and the scandal of 1873 "needs a new cause or goes". Both must be settled before the storyline can be revised: 708's "The scandal of 1873 over the foreign money behind Allan's syndicate shows what visible money would cost" is a causal sentence. See item 2 below for a form that also explains the dominion's debt.

**S5. The wheat contract is paid in the wrong things (A13).**
- Canon's granary (1695) buys abroad "beans and rice, which the Realm's fields do not grow in the quantities the Office's tables ask". Wheat is what the Realm sells: 1672 has it selling "3 to 4 million tonnes of grain … to Asia, in 1929 about a sixth of the world's wheat trade". A ten-harvest purchase of a rival's wheat, resold to the Realm's own customers, is a different investment from the granary and must be argued as one: a resale margin, the carriage, and the position of sole seller to Asia. Say that the prairie's wheat replaces Canada's own direct sales to Japan and China and not the Realm's.
- Prairie farms of 1931 used almost no nitrogen fertiliser (from memory), and Bennett's government had just raised the tariff to protect Ontario's implement makers (from memory). Ammonia is the wrong coin, and machines are a concession Ottawa would have to make against its own tariff.
- By late 1931 the pools' central selling agency was no longer the pools' in substance: the federal government guaranteed its debts and took over the sale of its stocks (see History checked). The seller is state-backed. That strengthens "Bennett asks first" and should be said.
- *Fix:* the board pays by an earmarked gold-dollar credit at San Francisco, which is what Ottawa lacks after sterling's fall, and by carriage; machines enter under a quota the treaty states, and that is Ottawa's concession.

**S6. If the Dutch refuse.** J-2 forbids fire, blockade and landing; the "Published" paragraph has The Hague "protest and agree to talk". The draft does not say why they would concede item 6, which is sovereignty, or what happens when they stall. In history they stalled two Japanese missions with their own country occupied. The atomic monopoly appears in J-0 as Japan's motive and nowhere as anyone's calculation.
- *Fix:* three sentences.
  1. What the Dutch calculate: Britain gave way in 1927 (1612) and "is managed through debt" (1754), the Union's navy sits below the common fleet's ratio, and nobody will fight for Batavia.
  2. What the Concord offers, in the Pacifican way: slump contracts for Java's sugar, rubber and tin, a guarantee of Dutch sovereignty, and rent.
  3. What happens on refusal: nothing by force; the trust's guaranteed supply (B3) carries Japan to 1937, when Japan may refuse the renewal. The monopoly also sets the clock: the Works expects a British device "about 1933–1935" (1614), which is why Japan wants the resolution in 1931 and not later.

**S7. The Gulf, the Union and Britain have interests the draft leaves out.**
- *The Gulf, oil.* 1697: "The Gulf's oil compact arrives in 1932, after a year of ten-cent East Texas oil … its purchases of the Republic's crude help hold the floor." A pool that brings fixed-price Indies crude to Japan undercuts the floor in the year it is set. Houston objects, not only the trust.
- *The Gulf, admission.* 1100: the Senate refuses a shorter count because "the parity tests are the Gulf's promise to its Black citizens". Caledonia enters in a year, on a roll from which its Asian residents are shut out. The draft uses this as the sufficers' third argument and gives the winners no answer. They need one (the floors apply in full on the day of union; the Gulf's tests measure outcomes because its law already promises equality), and the Gulf's press needs a line.
- *The Union.* Since 1866 Pacifica "has let London know that a Union move on Rupert's Land or the coast would concern the Pacific" (708). It now takes that coast itself in the winter of the gold rescue, six months before the Union's Senate "renounces the surviving claims" at Thalassia (1746). The *Tribune* and the revanchists get a gift; say so.
- *Britain and the Union in the Indies.* Tarakan and Balikpapan are Royal Dutch Shell's (see History checked), and the Union, which "imports four-fifths of its oil" (91), has its own company in Sumatra (from memory). The resolution is published in the autumn of 1931, and at the conference of June–July 1932 "Germany, Britain and France enter the monetary settlement" (1748). The Indies cannot be absent from that table. One sentence at 1746–1748 is owed here, not in the partners' CR.

**S8. Australia has no agency.** Canon 1752: the dominions sign "while refusing the racial equality clause", for "the guarantee that no hostile base stands on the dominions' soil". The draft reads this as proof that a station at Davao carries no dread. A dominion that still refuses the equality clause signs "knowing of Davao" only for a price. Give it one: for example, the treaty of 1932 names a line (Timor and New Guinea) south of which the Concord seeks no station or leased port.

**S9. Davao before the renewal, and the coup.** Until the renewal "the western squadron is reserved to the Japanese naval party" (1597), and in May 1932 "Japanese-crewed carriers in the western squadron make the danger to Oʻahu concrete" (1732). A station voted in 1931 puts a reserved, Japanese-crewed squadron on Mindanao during the coup. Either the station is not occupied until after the renewal, or 1732 needs Davao's ships accounted for. The first is cheaper and gives the Cortes a further term.

**S10. The lessee is two different parties.** J-4: the lease is "in the Emperor's name". Part F: the parties are "the Philippine crown as lessor; the Concord's Navy ministry". The first is Japan's lasting gain; the second takes it back. Write: lessee, the Emperor of Japan; user, the common Navy; commandant Japanese by right.

**S11. The Philippine side.**
- Canon 1133 grades the provinces with "the Cordillera and Moroland administered". If Davao and Zamboanga are administered country, the Cortes that votes the lease does not represent the people who live beside it. The separatists' line ("Manila pays with its land") is then half the story; the other half is that Manila pays with Mindanao's.
- The compacts of 1878: "Their Tausug text is authoritative, and the Sultan alone can consent to undo them" (764). The draft must say whether either site lies under a datu's compact. If Zamboanga's does, the yard contract needs that datu.
- "No Japanese land title" must be defined by subjecthood (subjects of Japan), or it bars the crown's own subjects of Japanese origin by descent.
- The freeze answers the army's own charge in Manchuria that "acres stay closed to Japan" (1720). The manifesto of May 1932 should name the freeze, not only "Davao's fence".
- North Borneo has been the Pacifican Borneo company's since 1878 (764) and adjoins Tarakan. Say in one clause why the station is not at Sandakan or Tawau (the Sultan's lease, the company's compacts), or readers who know the map will ask.

**S12. The Council's season.** Canon 1539: Pacifica raises Zhang's killing "at the Council at Hayama in 1929, and Tanaka's cabinet … falls in July 1929", so that Council met by early summer. The draft needs Councils in late autumn 1930 and autumn 1931. Fix the season, or call the sitting of 1931 extraordinary.

**S13. Commitments that end at the union.** Part C and Part F change the parties of the western waters treaty, the Columbia compact and the Halibut Treaty. On 1 January 1932 both parties to each are under one crown. Say what becomes of them: the commission of equals (1142) becomes an internal board or lapses; the half of the downstream power becomes Caledonia's revenue (see B4). The ledger needs end or conversion dates, not only new parties.

**S14. The treaty's maker.** Canon 1597: "Foreign Affairs, the common Navy and their Finance belong to the Concord." The soybean compact of 1929 is the Concord's (1679). The draft's treaty with Canada is "Pacifica, Canada". Say who signs (the common Foreign minister for the Crown of Pacifica) and whether the Concord's quota, "reviewed at every renewal" (1597), is reopened by a larger Realm. It gives Japan's standing in J-1 a legal ground.

**S15. Victoria has no vote.** A10 places "Victoria, at ninety-three" among those who lose in the Senate. Appointed seats end at sixty-eight (927). She can oppose from Honolulu and cannot vote. Canon then has her broker the Charter of 1932, "one last bargain with the son whose methods she condemned" (1738). The draft should connect the two: what she could not stop in December is the reason she can extract the Charter in 1932.

**S16. Fact changes.**
- `Britain,? for Canada` forbids the phrase everywhere, including any future sentence on the Treaty of Washington, where Britain does act for Canada. Anchor it: `Pacifica(?:,| and) Britain,? for Canada`.
- `grants Canada, for nothing` does not catch 91 ("grants Canada the Alaskan rivers") or AGENTS.md 115 ("grants Canada the Stikine"); both are flagged today only because the same sentence also contains the Confederation phrase. Widen to `grants Canada(?:,| the)`.
- Nothing guards the author's condition of 16:57. Consider a forbidden pattern for a Caledonian vote in Ka Lōkahi (for example `Ka Lōkahi[^.]{0,80}four votes`).
- Untracked wordings that will survive a clean lint: "Canada's own wire to the Yukon" (1137), "gives Canada fifteen percent of the Pribilof catch" (1142), "the Canadian line" (1643), "British, then Canadian, soil" (731). They are impact notes only; list them.
- On integration the linter does not scan CR records, so the draft's own 14 findings are harmless.

## Minor

- **M1.** T13 quotes "no bar of race or origin" as the Realm's floors in general. In canon 918 the phrase belongs to the floors that "bind every marriage". Cite the floor the draft means.
- **M2.** A7 term 6 says "rent", A13 "Caledonia's share of the water's rent", Part B "wayleave". Use one word.
- **M3.** "Victoria" is a queen and a city in the same paragraphs of A10. In the storyline the city needs a fixed form. Columbia already has a Vancouver (455).
- **M4.** A2: "with the head of the Liard" adds nothing; the Liard's head already lies in the country that became the Yukon Territory (from memory).
- **M5.** A2's Fort Yukon reason overstates: the Company withdrew up the Porcupine and still reached the country from the Mackenzie (from memory). "Its cheapest road" is safer than "its only road".
- **M6.** A8: Canada's Treaty 8 of 1899–1900 covered the Peace country and Fort Nelson in history (from memory; the Canadian Encyclopedia's Kaska article confirms Treaty 8 reaches into north-eastern British Columbia). With that country the colony's, no Treaty 8 is made there. Say so once; it is why the Dane-zaa and the Fort Nelson Dene come to 1931 with nothing signed.
- **M7.** The Hague treaty of 1919 "carries Japan's racial equality clause" (1381) and Britain signed it. Thalassia's standing quarrel with Victoria's race laws from 1907 has a treaty ground after 1919; use it in A5.
- **M8.** A11: the Yukon is "a territory of the crown". Which crown? Alaska beside it is under the Northern Commission.
- **M9.** The style of the fourth crown is not given (25 carries the other three).
- **M10.** The Mackenzie commission: Alberta, not Ottawa, has owned its natural resources since 1930 in history (from memory). One clause on who signs for the Peace below the line.
- **M11.** The title's "(1858–1931)" should read 1932.
- **M12.** Bennett pays a price the draft omits: he accepts a sister dominion's passing to a foreign crown months before he hosts the imperial conference canon mentions at 1752.

## The twelve proposed items and the question

1. **The fork's motives; the instrument of 1870; Fort Yukon; Macdonald's protest (A2).** Keep. Soften Fort Yukon (M5). Macdonald's restraint is right for the year of 705's *Chicora*.
2. **London's imperial route as Canada's motive (A3).** Change. Canada builds to the colony's boundary for its own reason, which canon already gives at 705 (the Union "can cut the Dominion in two at the Soo"). The colony builds its own section to Burrard Inlet on bonds sold in San Francisco and gives the Canadian Pacific running rights. That closes the OPEN builder, explains the gold-dollar debt of A6, and leaves London's mail subsidy as a help, not the cause.
3. **Petitions filed; commission and compensation in 1907 (A5).** Keep both. The commission is the dominion's own, pressed by London; history's commissioner was Ottawa's. Add M7.
4. **The rescue without union; London's two courses; the remitted instalment; Bamfield; Tolmie (A6).** Keep the rescue and the two courses. Change the instalment (S1). Change Bamfield's wording: by 1931 history's station belonged to a company, not the board. Keep Tolmie, and note that his historical career was federal, so the registry entry must give him a local one.
5. **Vancouver splits, the interior carries, Canada third (A7).** Keep, after B2 and S3.
6. **What a nation decides; the signing places (A8).** Keep the principle and add a refusal (B4). Change two places: the Secwépemc of the canal's line sign in their own country or at Spences Bridge, not at Fort St James in Dakelh country; and "the Tahltan of the Dease" is doubtful (see History checked).
7. **The sufficers' three arguments; the refusal of a fourth vote (A10).** Keep all three and add the Gulf's (S7). Keep the reason for the refusal, worded exactly: a fourth vote ends the two smaller crowns' majority by making two against two.
8. **The name; the stores (A11).** Keep both. France's Nouvelle-Calédonie lies in the same ocean; a wit in the Senate can say so.
9. **Bennett asks first; the entrenched quay; the downstream peoples; Camsell (A12).** Keep the first, second and fourth. Change the third: the Realm cannot seat another country's subjects as its commissioners without making 1265's "Canada's sovereignty is never in question" false. Ottawa refuses and wins; the commission instead hears petitions from any people of the basin and publishes them. Camsell fits the character bible's "Canada's partner, never Pacifica's agent".
10. **The price band; payment in kind; the enlarged home purchase; the refunding (A13).** Keep the band and the home purchase. Change the payment (S5). Keep the refunding, on wider security (B4).
11. **The two rents; the surveys; the chum clause; the reaches' say (B).** Change the rents (B4). Keep the surveys and the chum clause. Keep the reaches' say, and state whether it is a consent or a hearing; canon 931 says compacts "change only with the nation's consent".
12. **Part H's details.**
    - Councils of 1928 and 1930: keep the dates, change the speaker and the season (B3, S12). The first Council also agrees the annex under which Pacifica supplies the Concord's oil (1600); that annex is Julian's answer in 1928 and should be named as such. Canon 1135 already has a "southward school in Tokyo" about 1900; cite it as the wish's ancestry.
    - The plot's second motive: keep.
    - The first Dutch reply: change (S6).
    - Tarakan and Balikpapan: change to Tarakan and a new field. Balikpapan is Shell's refinery and headquarters; leasing it is a quarrel with London inside the first clause.
    - The limit on the fleet: keep, with its consequence stated (S6).
    - Fifty years: keep, and use the echo. Canon's Puʻuloa lease was fifty years, was stretched by illegal ordinances, and ended with the fleet as "tenant at the Mōʻī's pleasure". The Cortes knows that history; its speakers should say it.
    - The trust's objection: keep, add the Gulf (S7).
    - Zamboanga's form: keep, after S11.
    - The manifesto: keep, add the freeze.

**The question.** Yes to the Acts and the treaty in December 1931 and the union on 1 January 1932, on two conditions: Westminster's Act is tied to the Statute (S2), and Japan's assent is complete in 1931 by the route in B3(4) and not left to the renewal. If either fails, the union should take effect on the exchange of instruments in the spring of 1932.

## Literary effect

- **What works.** The fork of 1871 is the draft's best invention: one refusal, sixty years of consequence, and nobody acts out of character. The sufficers losing with three true arguments, Julian choosing "which Japan to strengthen", and the petitioner of 1913 who signs at Spences Bridge are scenes the book can use.
- **Too convenient.** Everything Julian wants arrives in one year and every party says yes: the legislature, the settlers, every nation asked, both chambers, the Cortes, Japan, London, Ottawa, and The Hague agrees to talk. Only the Island and the sufficers lose, and neither costs him anything. One refusal that holds is needed. The cheapest are a lessor nation's (B4) and Ottawa's on the commission (item 9).
- **Consent.** A bankrupt debtor votes to join its creditor, and the alternative is rule by commission. The draft half-knows this (T8, the member who says the Realm counts the dominion's acres). It should let someone say "foreclosure" aloud, and let the answer be the terms and not a denial.
- **Japan.** As written Japan is paid in prospects and Julian in territory. A strong partner bargains for a date and a default (B3). The draft's own best line, that Julian stops the army with oil and feeds the navy weeks later, is weakened if the navy's prize leaves the same hand on the tap.
- **Agency below the crowns.** Tolmie, Bennett and the nations' spokesmen are names without decisions. Each needs one choice that costs him: Tolmie his island, Bennett his imperial standing, a Sekani headman the valley or the rent.
- **The Realm's own contradiction.** The Senate that would not shorten the Gulf's count for its Black citizens' sake admits a settler dominion whose Asian residents could not vote on it. This is the richest material in the draft and it is one line in a list. It deserves the Gulf's voice and a Chinese Pacifican's at Steveston on the day after.

## History checked

**Confirmed**
- Simon Fraser Tolmie: born at Victoria on 25 January 1867, premier from 21 August 1928 to 15 November 1933. He sat in the federal Parliament from 1917 to 1928 and was federal Minister of Agriculture; unemployment reached 28 per cent in 1931 and the Kidd Report followed in 1932. https://en.wikipedia.org/wiki/Simon_Fraser_Tolmie
- R. B. Bennett: prime minister from 7 August 1930 to 23 October 1935, born at Hopewell Hill, New Brunswick. His Calgary firm acted for the Canadian Pacific and the Hudson's Bay Company, which suits the entrenched quay. https://www.thecanadianencyclopedia.ca/en/article/richard-bedford-viscount-bennett
- Fort Yukon, 1869: Captain Charles Raymond fixed the post west of the 141st meridian, raised the American flag and displaced the Company's agent. https://www.gi.alaska.edu/alaska-science-forum/early-ascent-yukon-river
- Liquor: British Columbia's prohibition ran from 1 October 1917 to 15 June 1921, when government stores opened. This agrees with canon 1024. https://en.wikipedia.org/wiki/BC_Liquor_Stores
- The riot of 1907: 7–9 September; Mackenzie King's commission; $26,000 to the Chinese community and $9,000 to the Japanese. https://en.wikipedia.org/wiki/1907_Vancouver_anti-Asian_riots
- Davao: "at least a hundred Japanese were murdered by ethnic groups" in 1918–21, after displacement from the Gulf's western shore; the census counts 4,472 Japanese in 1918 and 17,888 in 1939. https://journals.upd.edu.ph/index.php/kasarinlan/article/download/4976/4484
- Kobayashi's mission, 1940: the last demand was 3,150,000 tons above the normal 600,000, a total of 3,750,000 tons a year with a five-year guarantee; the Dutch did not accept. The draft's "570,000" should read "about 600,000" or be sourced. https://history.state.gov/historicaldocuments/frus1940v04/d207
- Kaska places: Lower Post is a Kaska community, and the Dease River valleys and the north of Dease Lake are Kaska country. https://thecanadianencyclopedia.ca/en/article/kaska

**Confirmed in part**
- The wheat pools' agency: the three pools sold through the Central Selling Agency from 1924 to 1931; in 1931 the federal government guaranteed the pools and took over the sale of their stocks. The draft's "prairie pools' selling agency" exists in December 1931 only as a state-backed body. I could not open a source for John I. McFarland's appointment in 1930 (from memory). https://plainshumanities.unl.edu/encyclopedia/doc/egp.ag.057.html
- Tarakan and Balikpapan: Tarakan's concession went in 1905 to the Royal Dutch company, and it produced over five million barrels a year in the 1920s, about a third of the Indies' oil. Balikpapan was the Bataafsche company's headquarters from 1907, with a refinery from 1922. Both were Royal Dutch Shell's. No figure for 1931 found. https://en.wikipedia.org/wiki/Tarakan and https://en.wikipedia.org/wiki/Balikpapan
- Bamfield: built in 1902 as the Pacific cable's terminus. The Pacific cable was sold to Imperial and International Communications Ltd, with payment completing about March 1930, so in 1931 the station was the company's and not a board's. https://en.wikipedia.org/wiki/Bamfield and https://api.parliament.uk/historic-hansard/commons/1930/feb/18/imperial-and-international

**Wrong or doubtful**
- "The Tahltan of the Dease." Tahltan country centres on the Stikine, with Telegraph Creek its main settlement; the Dease River is Kaska. If the Tahltan sign in 1931 it is for the Stikine's head, and the Stikine is not a river the draft diverts. https://thecanadianencyclopedia.ca/en/article/tahltan
- "Fort St James … for the Dakelh and the Secwépemc of the canal's line." Fort St James is Dakelh. The Secwépemc of the upper Fraser and the Canoe River are a North Thompson people (from memory; not checked).

**Not checked**
- Requests for exploration areas in 1940–41 (the source above is silent on them; from memory they were made).
- The Sekani at McLeod Lake and the reservoir on the Finlay and Parsnip; the Dane-zaa at Fort St John; the Dene of Fort Nelson (all plausible from memory).
- The franchise dates of 1872, 1895 and 1907; Esquimalt in 1905; the Liard's flow; the Parsons plan; Peter Kelly and Andrew Paull.
- The date of the Statute of Westminster and of the Wakatsuki cabinet's fall are from memory.

## Impact notes missing from Part C

Storyline, with current line numbers:
- **101, 927, 931:** the Senate's composition and "Alaska stays a territory under the Northern Commission, outside the 124". Caledonia's senators and its place outside the counties belong here (B1).
- **705, 707:** Canada in 1869–70 and the section comment "British Columbia and the Canadian Pacific".
- **987, 1005:** the Franchise Law and the Office's posted officers, if either runs in Caledonia.
- **1135:** "the southward school in Tokyo", the antecedent of J-0.
- **1139:** "Pacifica recognizes British Fanning as the station of the Pacific Cable". Bamfield is its other end.
- **87, 1163:** the Columbia's dams, "each … leased from the peoples of its reach". Part B sends 20 km³ through every one.
- **1236:** the succession, which Ka Lōkahi's minute extends to Caledonia.
- **1381:** the racial equality clause of 1919 and the naval limits.
- **1539:** the Council of 1929, for the Councils' season (S12).
- **1643:** "the Columbia from the Canadian line to the sea".
- **1693:** the moratorium of June 1931 (S1).
- **1697:** the Gulf's oil compact of 1932 (S7).
- **1703, 1726:** the Restoration circles' aims and "the common institutions hold", which should now mention the south.
- **1740:** the defences of 1932, if Davao is occupied before the renewal (S9).
- **1748:** who attends the Thalassia conference (S7).
- **1782:** the paragraph on Hirohito and Hayama.
- **1861:** item 26, OPEN-019-05, "British payment in kind".
- **1885:** item 38 still lists "any southern renunciation (the partners' CR)". T10 withdraws it.
- **35, 55, 85:** the header summaries on the crowns, Ka Lōkahi and the annex.

Other files:
- `historical_background.md` 195: "Historical gold is Canadian Yukon gold."
- `character_bible.md` 1494–1496: Camsell.
- AGENTS.md: the sentence "Julian's Realm, Hawaiian and Philippine crowns form one party opposite Japan".

Ledger entries not in the draft's list:
- C-1923-UK-FUNDING (the cancelled annuities).
- C-1899-FANNING-PALMYRA (Bamfield).
- C-1912-GREATBEAR-OFFTAKE (the Slave as the ore road).
- C-1920-MARIVELES (the dockyard work).
- C-1878-SULU and C-1878-NBORNEO (S11).
- C-1914-PH-CROWN (the Cortes leases crown land).
- C-1927-CONCORD-EXEC.
- C-1932-NZ-CROP-GUARANTEE (Australia's term, S8).
- C-1897-WHITE-PASS (its inland end is now on the colony's soil).
- The party entries CA and BCCO, and new parties for Caledonia, the Netherlands and each signing nation.
- End or conversion dates in 1932 for C-1906-WESTERN-WATERS, C-1923-HALIBUT and C-1924-COLUMBIA-STORAGE (S13).
