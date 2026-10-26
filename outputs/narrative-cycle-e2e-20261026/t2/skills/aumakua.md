# Aumakua consistency review: candidate §23 ("Noe's move")

**Question:** Is `outputs/review-input/candidate-23.md`, a proposed replacement for master storyline §23, consistent with current canon?
**Date:** 26 October 2026
**Mode:** Review only. The candidate says it is "Not approved". No canon, CR, character or registry file was edited (R2).
**Verdict in brief:** The candidate is not consistent with current canon as written. It contains three firm contradictions, which are Albert Kūnuiākea's parentage, Noe's vaccination reach and Noe's age. It also has two cross-section contradictions, about Hollerith's start date and the Gulf admission test, and one breach of the protected Noe-death ambiguity. The new move itself, the Chamber petition, rests on an authority that canon does not give and needs a bridge. Most repairs are small. The petition is the only one that needs an authorial choice.

## Scope, sources and coverage

Authority order follows `AGENTS.md` (R1): `master_storyline.md`, then `change_requests.json`, then `character_bible.md` and `character_registry.json` for identity questions.

Pinned inputs (sha256):

| File | sha256 |
|---|---|
| `outputs/review-input/candidate-23.md` | `b8b4e126…5c90` |
| `book-agent/revision/master_storyline.md` | `8b5df6f2…acdc1` |
| `book-agent/revision/change_requests.json` | `7899e29f…d52b` |
| `book-agent/revision/character_bible.md` | `6b36de1b…5a745` |
| `book-agent/revision/character_registry.json` | `23bf3d9b…dc2a` |
| `book-agent/revision/CR-021.md` | `b1a63127…ee30` |
| `book-agent/revision/CR-027.md` | `773b1898…7678` |
| `.agents/skills/aumakua/SKILL.md` | `6e1e7d72…e7` |

Git history was not inspected (sandbox rule), so no commit is pinned.

**Read directly and continuously:**
- the whole candidate;
- master storyline lines 1–55 (header, integration notes, larger movement);
- master storyline §§17–27 (lines 416–644), which covers every earlier setup and later consequence of §23 through Julian's accession;
- master storyline "Explicitly unresolved canonical decisions" (lines 883–919);
- character bible entries for Victoria (CT-KAIULANI), Kalanimoku, Noe (CT-JULIAN-MOTHER), Julian, Albert Kūnuiākea, Hollerith and the Five;
- character bible lines 660–685 (POV table and authorial decisions);
- CR-021 §F1 (lines 487–527);
- `AGENTS.md`.

**Searched only:**
- `change_requests.json` (CR-004, CR-021 R9-09, CR-027 A16/A20/A22, OPEN-027-02);
- `character_registry.json` (CT-ALBERT-KUNUIAKEA, CT-JULIAN links);
- `CR-027.md` (A16, A22);
- `CR-020.md` (B5 Gulf test);
- the `alternatives/CR-032/` drafts (searched for Noe; they are non-canonical and do not touch 1888).

**Not read:**
- master §§1–16 and §§28–37, except where search hits landed;
- `historical_background.md` and `war_base_assumptions.md`, except a search for population figures (no hit);
- first-draft sources.

These are not needed for the period the candidate covers, but this is a bounded review, not a full-text audit.

**Independence:** No prior review findings were consulted. Another file is already present in `outputs/review-output/`. It was not opened, per the task rule. The pass is prose-first.

**Tools:** I did not build an ontology graph or run the validator. This is a review of one section, which the skill allows to remain a prose answer. I did not use the consistency profile, and I claim no graph validation. The only mechanical check was a sentence-level diff between current §23 (master lines 507–515) and the candidate.

**What the candidate changes** (from that diff):
1. a new title;
2. "her cousin and heir" becomes "Emma's son", and the `[APPROVED — CR-027]` label is dropped;
3. a new paragraph about the petition (candidate line 9);
4. a clause added to the death certificate sentence;
5. a new Hollerith sentence.

Everything else is identical to current §23.

## Issue ledger (ranked by narrative consequence and strength of evidence)

### A23-01: Albert Kūnuiākea made "Emma's son"
- **Classification:** Contradiction (identity/kinship). **Lifecycle:** Open.
- **Candidate** (line 7): "they also look to Emma's son Albert Kūnuiākea, by common knowledge a natural son of Kamehameha III".
- **Canon:**
  - Master §23 line 509: "**[APPROVED — CR-027]** … they also look to her cousin and heir Albert Kūnuiākea".
  - Bible CT-ALBERT-KUNUIAKEA (line 890): "her cousin and heir Albert".
  - The registry gives the link `loyalist_successor → CT-EMMA`, not a parent/child link.
  - Bible CT-EMMA (line 497): "Alexander's wife from June 1856 and Anglican widow after 1863."
- **Why it conflicts:** It is the same person under the same approved CR-027 A16. Cousin and son are incompatible kin relations. The candidate's own wording also makes no sense on its own terms: a son of Emma who is the natural son of Kamehameha III would mean Emma had a child by Kamehameha III, which conflicts with her canonical marriage to Alexander.
- **The label is also gone:** The candidate removes the `[APPROVED — CR-027]` marker from an approved detail. That is a separate labelling mismatch (R1).
- **Compatible reading:** None. Nothing in the candidate suggests the change is deliberate.
- **Repair:** Restore "her cousin and heir" and the `[APPROVED — CR-027]` label. Or, if a kinship change is intended, raise it as a new decision affecting CR-027 A16, the bible and the registry. This review does not supply one.

### A23-02: "her vaccinators have reached forty thousand Hawaiians" by summer 1888
- **Classification:** Contradiction (quantity and achievement scope). **Lifecycle:** Open.
- **Candidate** (line 9): "By the summer her vaccinators have reached forty thousand Hawaiians."
- **Canon:**
  - CR-021 F1 (line 498, approved): "the Hawaiian people are dying (perhaps a quarter of a million or more in 1778, about 40,000 by the 1880s)".
  - CR-021 F1 (line 502): "A vaccination campaign, begun in Honolulu and on Maui and unfinished when she dies."
  - CR-021 F1 (line 519): Victoria "Completes the vaccination of every island" in 1888–92.
  - Master §20 line 474: "the unfinished work is her achievement, not a miraculous reversal of mortality in three years".
  - Master §23 line 513 (kept in the candidate): "She completes vaccination across the islands in 1888–1892".
  - Bible line 79: "Her achievement in 1886–1888 is limited and foundational … She does not cure the islands in three years."
- **Aligned scope:** The same population (Hawaiians), the same period (1888) and the same programme.
- **Why it conflicts:** Forty thousand is canon's estimate of the entire Hawaiian population in the 1880s. Reaching it by summer 1888 means the campaign is essentially complete. That cancels the "begun in Honolulu and Maui … unfinished" limit and leaves Victoria's 1888–92 completion with nothing to do. The candidate keeps that completion sentence, so the candidate's own text conflicts with itself.
- **Possible readings:**
  - "Hawaiians" could mean all island residents, a larger number that canon does not state.
  - "Reached" could mean contacted rather than vaccinated.

  Neither reading is stated in the text, and both would be the reader's own narrowing of the terms.
- **Repair:** Drop the figure, or replace it with a bounded, unquantified progress claim confined to Honolulu and Maui. Any number needs its own basis and should not be invented to fill the gap (R3).

### A23-03: Noe is "twenty-four" in January 1888
- **Classification:** Numerical discrepancy, strong. **Lifecycle:** Open.
- **Candidate** (line 9): "In January 1888 the twenty-four-year-old physician petitions".
- **Canon:**
  - Master §20 line 472: "born about 1860 in Lahaina".
  - Bible CT-JULIAN-MOTHER: "**Born:** c.1860".
  - CR-004 and CR-021 F1: "c.1860 Lahaina birth".
- **Arithmetic:** Born in 1860, she is 27 or 28 in January 1888. Being 24 would need a birth in 1863–64. That would also make her about 17–18 as a 1881 epidemic nurse and about 20 when she qualifies in 1884, as "the first Hawaiian" physician.
- **Possible reading:** "About" allows some slack, but three to four years is outside the usual meaning of c.1860. No canon text widens the range.
- **Repair:** Say "twenty-seven-year-old" (or "twenty-eight"), or drop the age. A later birth year would be a new identity change touching §20, the bible, the registry and CR-021 F1.

### A23-04: The death certificate is signed "before he has seen the body, on instructions from the palace"
- **Classification:** Suspected contradiction with a protected mystery, plus an integration mismatch with an explicit author decision. **Lifecycle:** Open.
- **Candidate** (line 11): "certified by Victoria's physician, who signs the certificate before he has seen the body, on instructions from the palace."
- **Canon:**
  - CR-021 R9-09 (approved; `change_requests.json`): "Noe's death remains ambiguous: official autumn 1888 typhoid certificate and poisoning testimony retained, no culprit established."
  - Bible line 83: "The approved event preserves real uncertainty rather than making Victoria guilty by implication."
  - `AGENTS.md` line 43: "Never establish a murderer."
  - Master line 25: "The remaining uncertainty over Noe's death concerns culpability, not her identity or the recorded circumstances."
- **Narrative stance:** The candidate states this in narrator voice, as fact, not as testimony or rumour. A palace-ordered certificate signed before anyone examined the body is evidence of a palace cover-up.
- **Why it conflicts:** Formally the candidate still says "the Chronicler can prove none guilty". The new clause does not name a murderer. So this is a suspected contradiction rather than a firm one. In practice, though, it implicates Victoria's household in falsifying the official record. That is exactly what the bible says the approved event avoids. It also changes the "recorded circumstances", which master line 25 treats as settled: canon has only "certified by Victoria's physician".
- **Repair options** (an author choice):
  1. Delete the clause.
  2. Recast it as an allegation inside the existing stance, for example as part of what the servants or loyalists claim.
  3. If a firm narrator-fact irregularity is wanted, treat it as an amendment to R9-09 and the bible, and check that the "no culprit" ambiguity still holds.

### A23-05: Noe "knows that her district registers will one day decide which territories enter the Gulf"
- **Classification:** Contradiction (institutional direction and entity), compounded by a knowledge anachronism. **Lifecycle:** Open.
- **Candidate** (line 9): "she knows that her district registers will one day decide which territories enter the Gulf and how the county league tables rank them."
- **Canon:**
  - Master §25 line 566: "Texas, Louisiana and Arkansas form the Federal Republic of the Gulf in 1899–1900".
  - Master line 568: "Pacifica considers admission only if the Republic adds usable power …"
  - Master line 570: "The compact also requires registers covering at least ninety percent of births, deaths …" (these are the Gulf's own registers).
  - Master line 574: admission is "outside the novel".
- **Why it conflicts:**
  - Canon's test governs the Gulf Republic's admission *to Pacifica*, measured by the Gulf's own registers. It does not decide which territories enter the Gulf. Noe's Hawaiian district registers are not the instrument. At most her *method* and the infant-mortality measure are carried forward, which is what current §23 says retrospectively: "later carried into county league tables and the Gulf admission test".
  - In January 1888 the Gulf Republic does not exist; it forms in 1899–1900. The Office of Public Measures and its league tables are only just being created (Office "established in 1888", master line 489).
  - The candidate gives a character certain knowledge of authored outcomes eleven or more years ahead (R4).
- **Possible reading:** It could be read as a vague ambition for her method. But "knows … will one day decide" is a statement of certainty.
- **Repair:** Remove the sentence, or give Noe a hope of her own time, for example that honest numbers will force governments to act. Leave the retrospective link to the narrator, as current line 513 already does.

### A23-06: Hollerith's tabulation starts in 1890, against 1888 in §24
- **Classification:** Contradiction across sections (it would arise inside the master on adoption). **Lifecycle:** Open.
- **Candidate** (line 13): "Hollerith's punched cards begin to tabulate the recovered registers in 1890."
- **Canon:**
  - Master §24 line 522: "**[PROPOSED — CR-027]** Herman Hollerith, whose punched cards tabulate Noe's registers from 1888".
  - Bible CT-HERMAN-HOLLERITH (line 915): "punched cards tabulate Noe's registers from 1888".
  - OPEN-027-02 keeps Hollerith's membership PROPOSED.
- **Why it conflicts:** It is the same activity on the same registers. "Begin … in 1890" is incompatible with "from 1888". The candidate also states the Hollerith detail without the `[PROPOSED — CR-027]` label, which would turn a proposed detail into apparently approved prose (R1).
- **Possible reading:** The cards could tabulate *recovered* registers from 1890 and other registers from 1888. That is unstated, and the registers are back in the Office within a month of an autumn 1888 death.
- **Repair:** Delete the sentence, since §24 already carries the detail, or align it to 1888 and keep the PROPOSED label. Changing §24 to 1890 is an author choice that touches CR-027 A22 and the bible.

### A23-07: The Chamber of Deputies names Noe "guardian of the heir's Hawaiian education"
- **Classification:** Missing bridge, and needs clarification on institutional authority. Not a proven contradiction. **Lifecycle:** Open.
- **Candidate** (line 9): "petitions the Chamber of Deputies to name her guardian of the heir's Hawaiian education, and the Chamber grants the petition by a large majority."
- **Canon:**
  - Master §21 line 483: the regency article "names Victoria … Regent of the Realm … and Julian Heir of the Realm".
  - Master line 489: "The elected lower house becomes the Chamber of Deputies … The ruler appoints and dismisses ministers; they answer to the ruler, not the Chamber."
  - Master §20 line 476: the 1886 hānai bargain already gives Noe "a place in the boy's life and Hawaiian upbringing" and makes Julian "her son and successor" to Victoria.
  - Master §24 line 520: Victoria governs "as Regent … rather than as guardian".
- **What is missing:**
  1. Canon gives the Chamber no power to appoint guardians or to direct the heir's education, and nothing shows the regency article or the Truce delegating it. The candidate treats a lower-house resolution as dispositive without saying under what power.
  2. The petition asks for what the hānai bargain already granted. The reader needs to know whether Victoria had withheld it, or whether the petition formalises it.
  3. The loyalists who court Noe reject the 1887 constitution (master line 485: "Hawaiian loyalists reject it"). Noe acting through that constitution's Chamber needs a reason, or it puts her at odds with her own backers.
  4. Nothing says whether the Chamber elected under the 1888 Franchise Law is sitting in January 1888. That is not settled either way.
- **Knock-on effects to check on adoption:**
  - What happens to the guardianship at her death in autumn 1888: does it lapse or transfer?
  - §24's statement that Victoria governs "rather than as guardian".
  - Bible CT-JULIAN-MOTHER, CT-JULIAN and CT-KAIULANI, none of which mention a statutory guardianship.
  - Whether the new event is a CR-level change. It is a new right and institution act, so it is a new premise under R3, not a clarification.
- **Repair options** (an author choice; none adopted here):
  1. Route the move through an organ canon already gives a role: the Regent, the Regency Council or the Truce. For a Hawaiian-crown matter, the ʻAha Aliʻi.
  2. Make the petition a political act whose outcome is a negotiated concession from Victoria rather than a binding legal grant.
  3. If the Chamber route is kept, state the enabling power and add it to the CR record.

### A23-08: Victoria "accepts every condition at once"
- **Classification:** Suspected contradiction (characterization and relationship). **Lifecycle:** Open.
- **Candidate** (line 9): "Victoria, who admires her courage, accepts every condition at once."
- **Canon:**
  - Bible line 81: "Respect and fear join the women; their rivalry concerns the boy and the state."
  - CR-021 F1: "Respect and fear, not simple jealousy"; "Rivals after August 1887."
  - Master §24 line 530: "Victoria governs through bargaining."
  - The candidate's own line 7: "Her rivalry with Victoria concerns the boy and Hawaii's future".
- **Why it conflicts:** Immediate, complete acceptance of a rival's terms over the heir sits badly with a rivalry over that same boy and with a ruler who bargains. Admiration can coexist with rivalry, so this is not a firm contradiction. But "every condition at once" removes the bargaining canon attributes to her.
- **A related effect:** The concession also changes the motive picture behind the protected death ambiguity. Canon lists Victoria among those with motives. A Victoria who has just conceded everything reads differently. No contradiction arises, because the candidate still lists her motive, but the balance of the ambiguity shifts.
- **Repair:** Let Victoria concede with conditions or a price of her own, consistent with "respect and fear", or state why she concedes.

### A23-09: The Anne of Austria comparison
- **Classification:** Integration mismatch with repository rules (minor), plus an internal scope tension. **Lifecycle:** Open.
- **Candidate** (line 9): "Like Anne of Austria during the minority of Louis XIV, she understands that a mother's guardianship of a royal child can outlast any council of ministers."
- **Rules:**
  - `AGENTS.md` line 21: keep "reasons for proposed divergences in `historical_background.md`, not explanatory comparisons in the storyline".
  - `AGENTS.md` canonical read order: storyline prose "must read as what happens".
- **Why it is a problem:**
  - The sentence is an explanatory historical comparison inside the synopsis.
  - Anne of Austria held the *regency*, which matches canon's "As natural guardian she could claim a regency". The candidate's actual move, though, is a narrower guardianship of *Hawaiian education*. The analogy points to a larger claim than the action described.
  - Julian is "Heir of the Realm" of a crown not yet established, so "royal child" needs care.
  - Whether the analogy is historically apt is a separate question for Clio, not settled here.
- **Repair:** Remove the comparison from the synopsis, or move it to an author note or `historical_background.md`, and keep Noe's aim stated in story terms.

## Checked and not a finding (compatible readings)
- **"Noe's death" changed to "Noe's move" in the title, with the date range 1887–1889 kept:** compatible.
- **Kept text from current §23:** natural guardian and regency claim, Emma dead since 1885, typhoid in autumn 1888, servants' poison testimony, registers missing for a month and returning to the Office, "the Regent's year" (Caleb, the January telegraphist, Noe), Silas and Abigail's mutual suspicion, Victoria's 1888–92 vaccination, 1890s nurses and Kalaupapa, the c.1895 population turn, and Julian's four languages and 1921 falsification. All unchanged and consistent with master §§20–25 and the bible.
- **January 1888 petition vs "the Donner telegraphist burned in his hut that January":** no conflict.
- **"Natural guardian" and the regency article:** canon already holds both: Noe *could* claim and Victoria *is* Regent. The candidate does not make Noe Regent.
- **The "no murderer" rule:** the candidate never names a culprit. A23-04 concerns implication through narrator-fact evidence, not a named murderer.

## Conclusion
Within the reviewed scope, the candidate cannot be adopted as written without creating contradictions with approved canon:
- **Firm contradictions:** A23-01 (Albert's kinship, an approved CR-027 detail), A23-02 (vaccination of essentially the whole Hawaiian population against "unfinished"), A23-05 (Gulf admission direction and Noe's foreknowledge) and A23-06 (Hollerith 1890 vs 1888).
- **Strong numerical discrepancy:** A23-03 (age 24 vs c.1860).
- **Protected-mystery risk:** A23-04, the palace-instructed certificate, conflicts with the approved R9-09 ambiguity and the bible's "not … guilty by implication" standard.
- **Needs an authorial choice before adoption:** A23-07, because the Chamber's authority over the heir is not established in canon.
- **Lower-severity:** A23-08 (characterization) and A23-09 (style rule).

Repairs for A23-01, -02, -03, -05, -06 and -09 are local to candidate lines 7, 9 and 13 and do not need new canon. A23-04, A23-07 and A23-08 depend on what the author wants Noe's "move" to be.

If the author approves a version, adoption would need, per `AGENTS.md`:
- master §23 prose;
- a check of §24 (guardian wording, Hollerith date);
- the bible entries for CT-JULIAN-MOTHER, CT-KAIULANI and CT-JULIAN, and the registry if any identity changes;
- a CR entry with a coverage comment;
- `sync_master_storyline.py --write/--check` and `validate_character_docs.py`.

None of this has been done. No overall consistency score is given.
