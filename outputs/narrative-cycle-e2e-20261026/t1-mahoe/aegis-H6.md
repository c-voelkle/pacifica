# Aegis H6: bounded succession-power check of CR-033 (draft)

**Handoff:** `handoffs/H6-aegis.md` · **Date:** 26 October 2026 · **Mode:** Compare (R2), bounded. This review approves nothing, does not select a case and edits no canonical file.
**Contract:** Pacifica power success contract v0.1.1 (`.agents/skills/aegis/references/success-contract.md`). Authority rules R1–R7 (`.agents/skills/mahoe/references/authority-and-scope.md`).
**Question:** Compared with the baseline, does the proposed 1888 written undertaking (CR-033 A5–A7) improve, weaken or leave unchanged the transmission of the Hawaiian crown and related legitimacy to Julian? Does it create a refusal point or a liability for him through 1932? This is not a full review of CR-033 or of Noe's agency.

## 0. Pins, coverage and limits

Pinned by sha256, first 16 hex characters, computed in this sandbox. Git history was not inspected, and remote refs were not resolved, so this is an **unverified local snapshot**.

| File | sha256 prefix |
|---|---|
| `AGENTS.md` | `1e574d3c958cfdeb` |
| `book-agent/revision/master_storyline.md` | `8b5df6f2b8bc9e32` (same as the draft's baseline) |
| `book-agent/revision/CR-021.md` | `b1a63127ba7174b3` |
| `book-agent/revision/CR-029.md` | `11f377359e9d45be` |
| `book-agent/revision/character_bible.md` | `6b36de1bc0728fd7` |
| `outputs/sessions/20261026-noe-succession-move/CR-033-draft.md` | `56b907ec5635801f` |
| `outputs/sessions/20261026-noe-succession-move/candidate-sections.md` | `98193c9a292d1762` |
| `outputs/sessions/20261026-noe-succession-move/clio-H1.md` | `cc4201f1c431a214` |
| `.agents/skills/aegis/SKILL.md` / `success-contract.md` | `fe2626bdeaa57ec9` / `9f7436ab930d0425` |
| `.agents/skills/mahoe/references/authority-and-scope.md` | `8e73ecce96740521` |

**Read:** the files the brief lists, and only the ranges it names. These were master §20–§29 (lines 470–668), §36–§37 (804–832) and the trajectories (834–852); CR-021's summary, constitution table, chronology (§D) and F1; all of CR-029, a 51-line reading record; the character bible's CT-KAIULANI, CT-JULIAN-MOTHER and CT-JULIAN; the CR-033 draft; the candidate sections; and Clio H1 §3, §4 and §8.
**Not read (withheld or out of scope):** `session.md`, `kalai-H3-notes.md`, `imi-H2.md`, any H4/H5 output, `change_requests.json`, `historical_background.md`, the registry, CT-ALBERT-KUNUIAKEA and master §30–§35.
**Independence (R5):** I saw no other reviewer's conclusions. The CR-033 draft does contain the drafter's own reasoning (§B), so this assessment is not independent of the writer's advocacy. I tested its claims instead of adopting them.
**Ontology:** The rdflib/pyshacl runtime is not installed in this sandbox, and per the brief it was not installed. **Turtle validation was unavailable and was not performed.** No review graph, query output or input manifest was produced. Claim and link identifiers below (CL-nn, ML-nn) are prose labels only and have not been validated structurally.
**Quantities:** None are material to this question. No Chryseis work was needed or done.
**History:** Every item from Clio H1 remains **[HIST-U]**, unverified in this run.

## 1. Cases compared

- **C0 (baseline).** Master as pinned. Noe is courted in 1887–88 and dies in autumn 1888. Julian is Heir of the Realm by the 1887 article (master 483). He is not proclaimed Hawaiian heir before 1914, and the master gives no reason beyond the Act's delay (622). In 1913 the ʻAha Aliʻi "will proclaim only Julian" (632). In 1914 the ʻAha Aliʻi proclaims him (634) and he accedes in 1915. Loyalists dispute the hānai line, and the 1876 judgment stays unreversed (638).
- **C-033 (draft defaults).** Same, plus A1–A12, under these defaults: petition unfiled (OPEN-033-01a); undertaking witnessed by chiefs and unpublished (02a); consenting body unnamed in the text, with story wording assuming the ʻAha Aliʻi acting in 1914 (03d/a); Victoria concedes by choice (A4).
- **Diagnostic variants.** These are comparison aids, not proposals:
  - **C-033m:** A1, A2 and A9 only. Noe refuses the counter-court and turns some chiefs, with no petition and no undertaking.
  - **C-033c:** C-033 with OPEN-033-03 (c), so Victoria can obtain chiefly consent whenever she chooses.
  - **C-033p:** C-033 with OPEN-033-02 (c), so the undertaking is publicly witnessed in 1888.

## 2. Transmission chain

Narrative-link status uses the contract's terms: explained, asserted, missing or contradicted.

| ID | Date | Claim | Holder → instrument | Status and locator |
|---|---|---|---|---|
| CL-01 | 1886 | Julian is Victoria's hānai son, with Elias's written consent; "hānai under Hawaiian custom" | Victoria; customary hānai | Explained (master 476; CR-021 §D 1886 row) |
| CL-02 | 1887 | Julian is Heir of the Realm by the regency article | Realm constitution | Explained (483). Separate from the Hawaiian crown and untouched by the undertaking |
| CL-03 | 1887–88 | Loyalists court Noe and look to Albert | Loyalist movement | Explained (509). APPROVED — CR-027 for Albert |
| CL-04 | 1887–88 | Noe turns some chiefs to Julian; the movement does not follow | Unnamed chiefs | PROPOSED A2. Asserted; the count and the chiefs are OPEN-033-06 |
| CL-05 | 1888 | Victoria's written undertaking: Julian's Hawaiian heirship only by her appointment plus a lawful chiefly body's consent, never by the Council or the Realm constitution | Victoria (obligor); the witnessing chiefs (moral obligees) | PROPOSED A5–A6. Asserted. Body and time OPEN-033-03 |
| CL-06 | 1888 | The unfiled guardian's petition exists as a document | Unknown custodian until the sealed papers | PROPOSED A3 and A12. Custody between 1888 and 1915 is **missing** (§6, I-5) |
| CL-07 | 1888–1914 | Julian is not proclaimed Hawaiian heir because no lawful chiefly body can act while the Council stands | Victoria | PROPOSED §26 sentence. **Contradicted in part** by the eight aliʻi Senate seats from 1887 (master 489; CR-021 table line 85). See I-1 |
| CL-08 | 1913 | The ʻAha Aliʻi will proclaim only Julian | ʻAha Aliʻi | Baseline asserted (632). Its lawful standing before the Act is missing in both cases; the draft's B5 treats it as a declared intention |
| CL-09 | 1914 | The ʻAha Aliʻi proclaims Julian heir; in C-033 this is the Queen's appointment as undertaken | ʻAha Aliʻi; Victoria's appointment | Baseline explained (634). APPROVED — CR-029. The C-033 link is PROPOSED A11 and asserted |
| CL-10 | 1914 | Hawaiian union plebiscite; loyalists campaign; Hawaii votes yes narrowly | Restored legislature, ʻAha Aliʻi, Hawaiian subjects | Explained (634, 636). APPROVED — CR-029 |
| CL-11 | 1915 | Accession to both crowns | Julian | Explained (634, 640) |
| CL-12 | 1915 | The sealed papers pass to Julian; in C-033 they include the undertaking and petition | Julian | PROPOSED — CR-022 (662) and PROPOSED A12 |
| CL-13 | 1914–32 | Loyalists dispute the hānai line; the 1876 judgment stays unreversed | Loyalists | Explained (638) |
| CL-14 | 1914– | The Act's succession rule: eldest son, eldest daughter, or an adopted heir **with Senate consent** | Realm statute | Explained (638; CR-021 §D 1914 row, "the hānai precedent made law") |

**Mechanism links in C-033:**

- **ML-01, creation (1888).** CL-04 and CL-05 create two things: a cohort of chiefs with a personal stake in Julian, and a self-binding promise about the *form* of his heirship. They add no right to the crown, no date, no resource and no office. The draft says so itself: "a promise about how he will be made heir, not that he will be".
- **ML-02, preservation (1888–1914).** Three channels carry it forward: (i) Victoria's own will, since no one can enforce the promise; (ii) surviving witnesses and their families, who are unnamed and 26 years older by 1914; and (iii) the document, whose custody is unstated. The promise is unpublished and has no enforcing body, so in practice it persists only as long as Victoria chooses to honour it. **Status: asserted.** Persistence through the witnesses is plausible but not shown.
- **ML-03, transmission (1914).** The ʻAha Aliʻi's proclamation becomes the performance of the undertaking (CL-09). The authored outcome is unchanged. What changes is the stated legal-customary root of the proclamation.
- **ML-04, exercise (1915–32).** The undertaking is spent once it is performed. It gives Julian no instrument of command. His only usable residue is documentary: he can disclose it to answer the hānai-line dispute (CL-13). Disclosure has costs (§4.4).
- **ML-05, accumulation.** None that is demonstrable. The possible spill-overs are a precedent for chiefly consent applied to Kahekili's succession (a liability) and, through Ka Lōkahi, Hawaii's vote on succession (CR-029). Both are unresolved.

## 3. Checkpoints

### 3.1 1888
- **Gains.** A1 and A2 remove the loyalists' preferred figurehead and split some chiefs away from the Albert alternative (CL-04). This is a real, though modest and unquantified, improvement to Julian's future Hawaiian support base, and it would exist in C-033m without any undertaking.
- **Costs.** Victoria forecloses two routes to Julian's Hawaiian heirship: the Territorial Council and the Realm constitution. In C0 neither was used, and either would have yielded what the draft calls "the ordinances' heir", unacceptable to loyalists. So the routes lost were low-legitimacy fallbacks.
- **New knowledge held by others.** The witnessing chiefs know that the Regent conceded under threat of a second public failure of her court. That gives them a small personal leverage over Victoria and, under A10 and OPEN-033-07, adds motive without evidence. The protected mystery is untouched (R3).

### 3.2 1913–14: Kiyoshi's bid, the Act, the plebiscite and the ʻAha Aliʻi
- **Kiyoshi's bid concerns the Realm crown** (630). The undertaking does not touch the Realm crown or the 1887 Heir designation (CL-02). Victoria's working levers against him are untouched: the memorial, Tokyo, Tate, the officers and Julian's visit to Pearl Harbor. **No constraint on her 1913 freedom against Kiyoshi was found in the authored history.**
- **One structural coupling (default 03a).** If the only lawful consenting body comes into being through the Realm's Act, which restores the legislature, then the undertaking makes Julian's Hawaiian heirship depend on the Act clearing two-thirds. That is the very threshold Kiyoshi was trying to deny (630). The irony is that a promise meant to keep the Realm out of Julian's Hawaiian heirship makes that heirship wait on a Realm vote. In C0 nothing *required* this sequencing. In the authored history the Act passes, so the outcome is unchanged; the weakness appears only in the branches where the Act fails.
- **The ʻAha Aliʻi lever in 1913 (CL-08).** Its force in C0 comes from Victoria's own unalienated Hawaiian crown and Thalassia's land, not from the chiefs' lawful power to act that year. C-033 adds an 1888 root and chiefs with a stake, which **improves the explanation** of the stance. Under 03a, the stance is only a declared intention, so the draft gains no added legal force here.
- **The plebiscite (CL-10).** The plebiscite asks about union of the crowns, not Julian's heirship, and the vote is narrow. Chiefs with a stake in Julian could plausibly lean their followers toward union, but nothing in the text establishes it, and under default 02a the undertaking is unknown to the electorate. **Unresolved, no claimed gain.** The plebiscite remains Victoria's act beyond what she promised (A11), so the undertaking takes nothing from it.
- **Act packaging (I-2).** Master 634 and CR-021 §D (1914 row) present the ʻAha Aliʻi proclamation inside the Act's provisions. Anyone who knows the undertaking could argue that Julian's Hawaiian heirship was conferred *by the Realm's statute*, the route Victoria forswore. The candidate clause "on the Queen's appointment as she undertook in 1888" mitigates this but does not separate the acts.

### 3.3 1915 accession
Unchanged in both cases. The undertaking has been performed and lapses. Julian inherits no obligation from it (no burden), and the sealed papers give him knowledge of his mother's bargain (CL-12).

### 3.4 1932 Hawaiian legitimacy
- **Hānai-line dispute (CL-13).** The undertaking concerns the *form* of heirship, not the line, so it does not answer the loyalists' objection. At most, if disclosed, it shows Julian was made heir by royal appointment with chiefly consent, at his loyalist-patronised mother's insistence. The Alexander Liholiho comparator [HIST-U] would support that form. **In-world effect without disclosure: none.**
- **Disclosure costs.** Disclosing it exposes Victoria's concession under pressure, which feeds the suspicion added by A10 and OPEN-033-07. In 1932 Victoria is Julian's broker for the Lands and Waters Charter (812). The asset is therefore latent and costly to use.
- **The petition is a latent liability (I-3).** Its premise is that the customary hānai left Noe's legal status as natural guardian intact (A3; OPEN-033-04a). A 1932 loyalist reading it would find, in Julian's own mother's hand, an argument that the adoption half of his claim was legally incomplete. That half is the one the Act's "adopted heir" clause made law (CL-14), and it is exactly what the hānai-line dispute contests. Under default 01a it lies only in the sealed papers that Julian controls. Under 01b (filed, then withdrawn) it would sit in a court registry.
- **The unreversed 1876 judgment.** Unchanged. The draft's appeal to that court reminds readers of the 1876 failure but does nothing to reverse the judgment.

## 4. Burdens, vetoes and grievances

| Actor | New veto? | New grievance or leverage? | Assessment |
|---|---|---|---|
| A lawful body of chiefs (ʻAha Aliʻi, or a restored House of Nobles under 03b) | **Yes, a one-time consent veto over Julian's Hawaiian heirship.** In C0 the ʻAha Aliʻi acts but no promise makes its consent *necessary*. Under 03b the consenting body could include Albert's partisans or irreconcilables. | Witnesses know of a 26-year-delayed performance | In the authored history the veto is not exercised (632, 634). Under 03a the risk is low; under 03b it is real |
| Territorial Council | Removed as a route | None new; already illegal (485) | Consistent with canon |
| Realm (Senate, Chamber, constitution) | No veto over the Hawaiian heirship. Under 03a, though, the Act's two-thirds becomes a **practical precondition** (§3.2) | Low under 02a. Under 02c, centralists could read it as Victoria reserving Hawaiian separateness, which the 1914 co-equal crowns concede anyway | Mixed |
| Eight aliʻi senators | Ambiguous (I-1) | Possible slight if a body of chiefs they are excluded from is preferred | Needs an author decision |
| Irreconcilables, Albert's partisans | No institutional veto | They lose a banner. Motive is added (A10) without evidence. In 1914 they still campaign (634) | Unchanged in outcome |
| Japanese constituencies, naval party | None | None; the undertaking is Hawaiian-only | Unchanged |
| Kahekili (beyond 1932) | Possible: a precedent that a Mōʻī is made with chiefly consent, against the Act's eldest-son rule (CL-14) | Liability only if the undertaking is known | Unresolved. Outside Julian's own transmission |

## 5. Contract failure-mode tests

1. **Legitimacy without command.** **Confirmed.** The undertaking produces legitimacy (and explanation) only: no resources, decisions, reach or instrument for Julian. That is acceptable for a succession instrument, but no command gain may be claimed.
2. **Capacity held by an independent body.** **Partly confirmed.** The undertaking makes chiefly consent a necessary condition, which strengthens the ʻAha Aliʻi's claim to make Hawaiian sovereigns. Canon already gives the ʻAha Aliʻi custody of crown and kuleana lands, including Thalassia's ground (634). The precedent adds to an independent institution's standing rather than to Julian's. The magnitude is small and unresolved.
3. **Expiry or failed succession.** **A weakening in the failure branches.** If Victoria had died before a lawful body could consent (she is 75 in 1913, and Kiyoshi's strategy was to outlast her, 630), Julian would hold no Hawaiian appointment, and she would have forsworn every alternative route. C0 shares the gap, since he was not proclaimed, but in C0 an illegitimate emergency route stayed open. In the authored history the undertaking is performed and expires harmlessly in 1914.
4. **Partner refusal.** The consenting chiefs can refuse in principle, and the witnessing chiefs cannot compel Victoria. Neither happens in the authored outcome. What decides the risk is OPEN-033-03, not the undertaking itself.
5. **A restraint that protects later capacity.** **This is the draft's strongest power argument, and it holds conditionally.** Victoria's self-restraint guarantees that Julian is never "the ordinances' heir". That protects the Hawaiian legitimacy he draws on in 1914–32 (the narrow plebiscite; the Hawaiian delegation's backing in 1927 per CR-029). The protection becomes real only if the restraint is *known* at some point, through the witnesses, the 1914 proclamation's wording or a later disclosure. Under 02a it is mostly private.
6. **Wealth without command; gross gain against obligations.** Not applicable: no resources are involved.

## 6. Exposition-only gains and world change

- **Exposition only:**
  - Why the ʻAha Aliʻi backs only Julian in 1913 (CL-08).
  - Why Julian was not made Hawaiian heir between 1888 and 1914 (CL-07; flawed, see I-1).
  - Why the 1914 proclamation counts as Hawaiian rather than Realm-made (CL-09).
  - "The two halves Noe refused to separate" (638).

  None of these changes an authored outcome, and C-033m would deliver much of the first without any instrument.
- **World change:**
  - The undertaking itself, a binding promise with a necessary-consent condition.
  - The petition document.
  - A cohort of chiefs with a stake in Julian (also in C-033m).
  - Knowledge of the concession held by the witnesses.

  These are new premises under R3, with the burdens set out in §3–§5.

## 7. Directional verdicts

Each verdict states whether it concerns Julian's power or only explanatory support. Every verdict is conditional on the PROPOSED links CL-04 to CL-07, CL-09 and CL-12 being adopted.

| Dimension | Verdict | Basis | What would reverse it |
|---|---|---|---|
| 1. Mobilizable resources | **Unchanged** | No resource is created or transferred | Only a new premise tying crown lands to the undertaking (not proposed) |
| 2. Decisions Julian can implement | **Unchanged** | No instrument of command | — |
| 3. Leverage over independent Hawaiian actors (chiefs, loyalists) | **Mixed** | Gain: chiefs with a stake and a weaker Albert alternative in 1888 (ML-01). Loss: chiefly consent made necessary, which strengthens the ʻAha Aliʻi precedent (§5.2) | Toward **improves** if the consenting body is pinned to the ʻAha Aliʻi (03a) and the witnesses' persistence to 1914 is shown. Toward **weakens** under 03b, if Albert's partisans sit in the consenting House |
| 4. Freedom from obstruction and vetoes (crown transmission 1914–15) | **Mixed. Unchanged in the authored history, weaker in failure branches** | Couples the heirship to the Realm Act's two-thirds (§3.2); forecloses fallback routes if Victoria dies early (§5.3); exposes a breach argument from the Act's packaging (I-2) | Toward **unchanged or improves** with adjustments R-1 to R-3 below |
| Hawaiian legitimacy through 1932 | **Mixed, mostly latent** | Restraint protects against the "ordinances' heir" charge (§5.5). The undertaking is a usable but costly disclosure asset; the petition is a latent liability for the adoption half (I-3) | Toward **improves** if the 1914 proclamation publicly recites appointment with chiefly consent (R-2). Toward **weakens** if 01b or 01c puts the petition on record |
| Explanatory support (not power) | **Improves, conditionally** | Gives reasons the baseline lacks for CL-07 to CL-09 | Reverses to **weakens** if I-1 stands uncorrected: readers then meet an unexplained contradiction with the aliʻi Senate seats |

**Overall:** CR-033's undertaking is **not an unconditional improvement** in Julian's power, because the material links CL-05 to ML-03 are asserted, not shown. It is roughly **power-neutral in the authored history**, slightly **weakening in counterfactual robustness**, and **improving for explanation and the legitimacy narrative**. That is an acceptable profile for a change whose purpose is literary, provided the adjustments below are made.

## 8. Recommended adjustments to OPEN-033 defaults

None of these reduces Noe's agency. Every one remains an author choice and none is applied.

- **R-1 (OPEN-033-03, body and time).** Keep the undertaking text unspecified (d), and in the story wording either:
  - **(i)** keep (a) and add to the §26 sentence that the aliʻi who sit in the Realm's Senate sit by the constitution she has promised not to use (fixes I-1); or
  - **(ii)** adopt a variant of (a) in which the ʻAha Aliʻi can be convened by the Queen, and recast §26 so the 1888–1914 wait is Victoria's own choice, consistent with CR-021's "deliberate brake on the heir" (§D, line 382). This variant is conditional on the author deciding the ʻAha Aliʻi's standing before 1914.

  Option (ii) removes the coupling to the Realm Act and the early-death gap, and makes the 1913 stance a lawful body's intention (resolving the draft's B5 tension). Its cost is the loss of the draft's "no lawful body" explanation, and it adds a grievance the witnesses may hold against 26 years of delay, which is usable dramatic tension. **Avoid (b)**, which adds a refusal point that may include Albert's partisans.
- **R-2 (1914 packaging).** Present the proclamation as the Queen's appointment with the ʻAha Aliʻi's consent, *following* the Act's restoration of Hawaiian institutions and distinct from the Act's Realm provisions. Today 634 and the CR-021 §D 1914 row bundle them. The draft's clause at 634 goes most of the way; making the proclamation a separate sentence would close the breach argument (I-2). Whether the proclamation recites the 1888 undertaking publicly (a timing variant of 02, disclosure in 1914) is worth offering. It converts the latent legitimacy asset into a realized one without disclosing the petition.
- **R-3 (contingency).** Either leave the early-death gap visible as deliberate stakes, which sharpens Kiyoshi's "outlast a Regent of seventy-five" (630), or let the author decide whether the undertaking permits an appointment by Victoria's will subject to later chiefly consent. That would be a new PROPOSED detail, offered only as an option under R3, not supplied.
- **R-4 (OPEN-033-01).** Keep (a), unfiled. Options (b) and (c) turn the petition's premise (I-3) into a public record against the adoption half of Julian's claim.
- **R-5 (OPEN-033-02).** Keep (a) over (c) for 1888, since (c) adds motive and campaign material in 1888 and 1914. Pair it with R-2 if a realized legitimacy gain is wanted.

## 9. Issues found (reported, not resolved; R1)

- **I-1. The aliʻi Senate seats against the §26 candidate sentence.** Master 489 and CR-021's constitution table (line 85) give the Realm Senate eight Hawaiian aliʻi seats from 1887. The candidate sentence ("no such body can act lawfully while the Territorial Council holds the legislature's place") does not address them. Whether consent by aliʻi senators is a "Realm constitution" route is undecided.
- **I-2. Proclamation bundled in the Act.** Master 634 and CR-021 §D (1914 row) place the proclamation within the Act's provisions. The undertaking forbids a Realm-constitution route.
- **I-3. The petition's premise against the adoption half.** The petition asserts that the customary hānai left Noe's guardianship intact. Canon (CR-021 §D 1886 row; the 1914 "hānai precedent made law") relies on hānai as effective adoption.
- **I-4. Stale CR-021 text.** The CR-021 summary (line 71) and §D 1874 row (line 351) still say the throne was "in abeyance since 1874" and that "the massacre follows". AGENTS.md's current authority says there is no massacre or throne abeyance, and master 634 has Victoria wearing the Hawaiian crown since 1872. Under AGENTS.md the current master governs, so this does not affect the verdicts, but CR-033 cites "CR-021 chronology". It should cite only the 1886 row.
- **I-5. Custody of the instrument and petition, 1888–1915, is unstated.** If Noe held a copy, its fate after her death touches the protected mystery (the registers vanish for a month, 511). Do not resolve it by invention. The author should state the custody, or keep it to Victoria's copy only.

## 10. Unresolved dependencies

No Clio or Chryseis sub-handoffs were made in this run.

- **Clio:**
  - **D-1.** The ʻAha Aliʻi's legal or customary standing before 1914 and its relation to the House of Nobles (Clio H1 §3 already flags this). It decides R-1 (i) or (ii).
  - **D-2.** Verify the 1864 Article 22 appointment-with-consent clause and the Alexander Liholiho precedent [HIST-U]. They support the form of the undertaking and the 1932 disclosure value.
  - **D-3.** Whether period Hawaiian practice treated a customary hānai as displacing the birth parent's legal guardianship [HIST-U]. This determines how much of a liability I-3 is.
- **Canon:**
  - **D-4.** Albert Kūnuiākea's status after 1888. Not in the files read, so the persistence of the "weaker Albert alternative" to 1914 is unresolved.
- **Chryseis:** none. No quantity is material.

## 11. Author decisions still needed

1. OPEN-033-03: R-1 (i) or (ii), or the draft default as is with I-1 accepted.
2. Whether the 1914 proclamation is separated from the Act and whether it recites the undertaking (R-2).
3. Whether to keep the early-death gap as stakes or to permit a testamentary appointment (R-3).
4. Confirm OPEN-033-01 (a) and 02 (a). Decide the custody of the instrument (I-5).
5. Whether the author prefers C-033m. It keeps Noe's refusal and the turned courtship (most of the 1888 gain) without the instrument's burdens, but at a real loss of Noe's agency, which is the purpose of the request. This review does not recommend C-033m over C-033. It is the baseline-adjacent comparator if the instrument's burdens are judged too high.
