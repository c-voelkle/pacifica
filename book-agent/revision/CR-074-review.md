# CR-074 — fresh-context review (draft 5, 18 November 2026)

Reviewer: a separate agent given only `AGENTS.md`, `CR-074.md` (draft 5, commit f6b3fe5, including its `## Canon tensions`) and the canon passages it touches; not the drafting conversation. Lint and `cr_facts.py preview` run first (only the expected unknown ID CT-FREDERICK-WARD). Findings as returned, lightly condensed.

**Verdict:** not ready for integration. Five blockers (the Philippine crown's date; the contradictory first treaty; T5 against CR-037 E7; the Logan licence overriding CR-062 A5; "only Convention VII"), and draft 5 still carries draft 4's superseded 1907-accession text. The design is sound and the Ward strand reads well once the §19 paragraph is split; most remaining issues are dates and authority (1865–87 licensing, Sherman's board, the 1907 transitions) and need a sentence or two each.

## Blockers

1. **The Philippine crown dated 1914; canon dates it 1907** (F8, "Not partners", T2, T7, D-28, D-32). The Cortes offers the crown with the Act of Settlement of 1907 (storyline l.1138, CR-029 as redated by CR-040); Julian swears at Manila in December 1907 (AGENTS.md). Fix: 1914 → 1907 throughout; the dependency's companies run 1888–1907.
2. **Two first treaties.** F1 and C6 make China's Customs capitulation the first under the Act; Part H §16 and the `korea-capitulation` fact make Korea first. Fix: choose one and align text and pattern.
3. **T5 / D-24 against CR-037 E7.** E7 (CR-037.md l.27) covers "what the Crown charters, funds or licenses"; the storyline audits "every chartered body" (l.950). Raised companies are chartered (I1) and paid in Land Fund warrants. Fix: take T5's amended case as a stated amendment to E7 (an exception for companies serving abroad under the Act, I3 as safeguard), or make raised companies registered associations, not chartered.
4. **J3.1 and the new §13 sentence override CR-062 A5.** The author decided Logan refuses Richmond "for a better offer from the Gulf's merchants" (CR-062 l.46; storyline l.562); a licence that could not be granted makes the refusal no choice. The 1854 law also covers ventures "from its soil". Fix: drop the §13 sentence; J3.1: such a contract would have needed a licence Monterey would not grant, but Logan never asks; he refuses for the Gulf's offer, and the consul's report is the licence's machinery noticing.
5. **"In 1907 the Regency's delegates sign only Convention VII."** The peace of 1919 is a special mediation under Article 8 of the 1907 Convention I (storyline l.1260; CR-043 P2). Fix: they sign the conventions, VII among them, keeping the reservation of 1856 on privateering.

## Should-fix

6. **Superseded text after D-31:** D1 "(until 1907, B5)"; B5's heading; the D-2 row; ledger C-1907-PARIS-ACCESSION; §28 and §30 "(if D-31 is approved)"; the D-3 row ("settles in San Francisco after the Crimea"); the D-21 row ("Part K PROPOSED"); registry "(candidate Forester)" and research "Still to check: Forester"; research on Hawaii's accession (settled by T4). Fix: clean; rename the ledger entry C-1919-PARIS-ACCESSION; add C-1914-LETTERS.
7. **B6 against the naval reserve.** F8 and I6 keep the 1907 enrolment under Convention VII; enrolled ships are commissioned state auxiliaries, not privateers. Fix: drop the 1907 enrolment, or issue letters only to ships outside the reserve; define "company steamers".
8. **B6's reason undercut by §28.** Julian does break the oil contracts in late July 1914 (l.1202–1204). Fix: a structural reason: the Declaration has no withdrawal clause, so accession is irrevocable and deferred to the peace.
9. **F1 runs past canon.** China recovers the Inspectorate and customs under the Treaty of Nanjing, 1928–29 (l.1411, CR-039). Fix: end F1 then, or renew it with the Nationalist service; F3 becomes a Concord matter.
10. **The war of 1894.** China (F1) and Japan, both partners, fight over Korea (F2); D10 forbids service against a partner; Fong's dilemma of 1894 is canon (l.1005). Fix: armed duties suspended in a war between partners; the revenue cruisers' companies stand down.
11. **The Korea sentence sits in §16 (1877–87)** before the 1887 pause (l.750). Fix: move to §25 and acknowledge the pause.
12. **OPEN-1:** canon already has "Queen Min survives and Gojong does not flee" (l.1003). Fix: limit OPEN-1 to the company's part in her survival.
13. **Company commissions bypass Sherman's board** (l.813), and carry the third vote. Fix: every company commission confirmed by the board or its successor.
14. **D2 "the inland command's general":** Silas is capped below general rank (l.811). Fix: "the inland command's commander".
15. **D5's tongue vote:** CR-021 C3 grants it only for languages on the Crown's list, alongside examined English (l.322). Fix: a tongue vote only where the language is on the list; otherwise a working-tongue certificate.
16. **C2a overstates naturalization canon:** §4 leaves franchise and naturalization rules OPEN (l.178); residence is a member power (l.334). Fix: Ward's oath of 1859 as a PROPOSED settlement of California's rule.
17. **Licensing authority 1865–87:** the Chancellorship lapses under the Providentorship from 1865 (CR-021 l.91). Fix: name the Providentor's cabinet or its external office for 1865–87.
18. **Crabb makes the law toothless** (C1: he sails without a licence and nothing happens); also contradicts J3.1's "first test in the Americas (1866)" and K5. Fix: he slips out overland across the Colorado while his backers are prosecuted and their bonds forfeited; drop "first" in J3.1.
19. **Keelung:** the French landed in August 1884 and held the port October 1884 – 22 June 1885; canon's squadron acts "after Ferry's fall" (l.744); a neutral guard on pitheads under attack is not neutral. Fix: from spring 1885, or the miners' town only. Check whether the Chinese wrecked the works in 1884.
20. **The letters of 1878:** Russian Pacific shipping thin, much under German or American charter (protected by B1); the Okhotsk iced in February. "About thirty vessels", "first fortunes", $1.5m doubtful. Fix: spring–summer 1878 to the Berlin settlement; fewer, visible fortunes.
21. **Hokkaido:** Sapporo settles its soldiers on Ainu land without asking (l.685), what D10 later forbids. Fix: acknowledge it as a second root of D10.
22. **C3's army mission against D13.** Fix: the sergeants discharge from the companies and enlist in the mission, or cite it as a reason for D13.
23. **Borneo constabulary untested:** the Sultan's lease, not compacts with the interior peoples; a Mat Salleh-type rising (1894–1900) falls in its years; protected intent. Fix: say what D9 and D10 require then.
24. **F8's Philippine warrants against E1;** friar land already resold to tenants (l.720), Calamba evictions (l.989). Fix: a separate warrant under the Organic Act; say what it does for evicted tenants.
25. **I6 Hawaii's act from 1888:** the Territorial Council governs until 1907 (l.1136). Fix: from 1907; say which court the Honolulu prize court of 1878 is, given the ignored judgment of 1876.
26. **"The Regent's review"** after 1907. Fix: "the sovereign's review"; check "Queen's Guard" after 1907.
27. **Two Wards:** CT-FREDERICK-WARD's entry must state no kinship with CT-JULIAN-MOTHER (Noe Ward) or CT-JOHN-WARD.
28. **Caleb and Silas:** Olompali's colour with Caleb in it is honoured from 1888, a year after Silas killed Caleb at Donner under the Truce's public lie. Fix: decide on purpose; note the risk to the lie.
29. **Approved items without storyline text:** D-7 (Borneo 1882), D-12 (Formosa 1895), D-30 (Crabb), D-32 (Philippine companies), D-20 (Hawaii). Fix: one sentence each at its date.
30. **Set piece 7:** Ward dies 22 September 1862; news of a New York sale must reach him before then; his Union money was in his will, not a lifetime offer; canon's war "has been paid for in gold" (l.557), no war loan. Fix: check Carr ch. VI; a gold subscription to the Treasury, or the taels in the will.
31. **§19 prose:** split the Harry sentence so the motive shows; "with two of every three men killed or wounded"; name Shanghai; present tense with motive for the oath; "on the Gulf", not "in Louisiana".
32. **Suzhou logic:** no order was given; D9 governs orders. Fix: its articles forbid it to serve a commander who kills prisoners who surrendered to him.
33. **§4 insertion** hangs after the rout clause. Fix: fold into the Olompali sentence (l.180).

## Nits

- B3: Russia was an original signatory, not an accession.
- C2: Álvarez was president only from October 1855; "General Álvarez".
- K2: Ynitia sold most of Olompali to James Black in 1852; drop "and keep".
- K1: 31 May to 14 June is two weeks.
- C2: Tan Shaoguang killed 4 December, surrender 5 December 1863.
- C3: Kuroda deputy of the Kaitakushi from 1870, director 1874; Hakodate passed to the Meiji Hakodate-fu in spring 1868, before Enomoto.
- Registry: CT-LI-HONGZHANG exists.
- I5's citation of CR-071 G D2.3 (home company law): label it an extension.
- I1's Nauvoo Legion at Bannack is a precedent against chartered raised companies; drop it.
- Numbering: B6 before B5, D13 before D12, Part H after L (and H collides with CR-071's H).
- "Read with … §26 (The Hague, 1907)": §26 has no Hague passage; a missing comma in the status line; "CR-029 table B4" not in the reading record.
- Epigrams: A3 "The author's word survives where words survive"; G "Each class thinks the other has the easier road"; B6 "the prize money of 1914 pays for the last fortunes"; §30 "Its letters of 1914 were the last any power issued".
- D11 omits the day of rest (l.876); say it covers Doheny's Mexican companies and Shinkolobwe.
- J3.5 "His firms": a seat among the Five means giving up management (CR-058-R1).
- G "the bridge": contrast with I9's Feather settler companies.
- E2 fixes the family farm at 80 irrigated / 160 dry acres, which canon never states: record as a new fact.
