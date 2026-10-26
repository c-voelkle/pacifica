# Consistency review: candidate §23 ("Noe's move, the registers and the heir")

**Input:** `outputs/review-input/candidate-23.md` (marked "Not approved").
**Checked against:** current canon per AGENTS.md read order: `book-agent/revision/master_storyline.md` (§17–§25, header), `change_requests.json`, `CR-021.md` F1, `CR-027.md` (A16, A20, A22, B-section anchors), `CR-016.md` E2, `CR-022.md`, `character_bible.md` (CT-JULIAN-MOTHER, CT-ALBERT-KUNUIAKEA, CT-EMMA, CT-HERMAN-HOLLERITH, Victoria), `character_registry.json` (CT-ALBERT-KUNUIAKEA), and AGENTS.md's current-authority section.
**Status of this review:** a consistency check only. It doesn't approve or integrate anything, and I haven't edited canon. The candidate stays a proposal until you decide on it.

## What changed

A word-level diff against the current §23 (`master_storyline.md` lines 507–516) shows the following:

- **New paragraph 2:** Noe's January 1888 petition to the Chamber of Deputies, Victoria's acceptance, Noe's foresight about the registers, the Anne of Austria comparison and a vaccination figure of 40,000.
- **Paragraph on her death:** two clauses added about the certificate ("before he has seen the body, on instructions from the palace").
- **Measures paragraph:** a new sentence, "Hollerith's punched cards begin to tabulate the recovered registers in 1890."
- **Paragraph 1:** "her cousin and heir" is now "Emma's son", and the **[APPROVED — CR-027]** label is gone.
- **Heading:** "Noe's death" is now "Noe's move".
- **Unchanged:** the Julian paragraph and the rest of the death and measures paragraphs, word for word.

## Findings

Severity key:
- **Contradiction:** conflicts with approved canon.
- **Authority breach:** conflicts with a standing author instruction or AGENTS.md rule.
- **Tension:** compatible only with a strained reading, or needs a decision.
- **Label:** a status marker is lost or misapplied.

### 1. Albert Kūnuiākea is "Emma's son" (Contradiction; also internally impossible)

- Candidate ¶1: "they also look to **Emma's son** Albert Kūnuiākea, by common knowledge a natural son of Kamehameha III".
- Canon: "they also look to **her cousin and heir** Albert Kūnuiākea" (`master_storyline.md` l.509, **[APPROVED — CR-027]**, CR-027 A16). `character_bible.md` CT-ALBERT-KUNUIAKEA and the registry profile say the same: "her cousin and heir Albert, widely understood to be Kamehameha III's unacknowledged natural son".
- The candidate sentence also contradicts itself. Emma is Alexander's wife and widow (§6, CT-EMMA), so her son would not be Kamehameha III's natural son.
- **Repair:** restore "her cousin and heir" and the **[APPROVED — CR-027]** marker.

### 2. Noe is "twenty-four" in January 1888 (Contradiction)

- Canon puts her birth at "about 1860" (`master_storyline.md` l.472; CR-021 F1; CT-JULIAN-MOTHER "Born: c.1860"). That makes her about 27–28 in January 1888. She would be 24 when she qualified in 1884, not in 1888.
- **Repair:** drop the age, or say "not yet thirty".

### 3. Forty thousand Hawaiians vaccinated by summer 1888 (Contradiction, in chronology and quantity)

- Candidate ¶2: "By the summer her vaccinators have reached forty thousand Hawaiians."
- CR-021 F1 gives the whole Hawaiian population as "about 40,000 by the 1880s". The candidate therefore has Noe vaccinating essentially the entire people in a few months.
- Canon limits her achievement:
  - The work is "the unfinished work … not a miraculous reversal of mortality in three years" (`master_storyline.md` l.474).
  - Vaccination is "begun in Honolulu and on Maui and unfinished when she dies" (CR-021 F1).
  - She "does not cure the islands in three years" (CT-JULIAN-MOTHER).
- Paragraph 4, which the candidate keeps unchanged, then has Victoria "complete vaccination across the islands in 1888–1892". With the new figure there would be little left to complete, and the rivalry built on outdoing Noe (CR-021 F1, "Kaiulani's need to outdo her") loses its basis.
- **Repair:** remove the figure, or replace it with a district-scale, clearly partial result. Any number would need MODEL treatment and a basis in `war_base_assumptions.md` or `historical_background.md`.

### 4. "Signs the certificate before he has seen the body, on instructions from the palace" (Authority breach)

- AGENTS.md says: "Never establish a murderer." The author's direct instruction (CR-021 revision 9, `change_requests.json` l.1773) is "Keep … Noe's death ambiguous".
- CT-JULIAN-MOTHER says the approved event "preserves real uncertainty rather than making Victoria guilty by implication". CR-021 R9-09 says: "official autumn 1888 typhoid certificate and poisoning testimony retained, no culprit established".
- The added clause states palace interference with the certification as narrative fact, not as rumour or testimony. It doesn't name a murderer, but it is exactly the "guilty by implication" the character bible excludes. It also weights the evidence against one of the three parties the Chronicler must leave equally unproved: Victoria, Silas's faction and the loyalists.
- **Repair:** cut the clause. Alternatively, attribute it to a source whose reliability stays open, such as servants' testimony or a loyalist pamphlet, alongside the existing poisoning testimony.

### 5. Hollerith tabulation dated 1890 (Contradiction with the adjacent section; Label)

- Candidate ¶4: "Hollerith's punched cards begin to tabulate the recovered registers in 1890."
- Canon §24 (l.522) and CT-HERMAN-HOLLERITH both say his "punched cards tabulate Noe's registers **from 1888**".
- Hollerith's seat and chronology are **[PROPOSED — CR-027]** (A22; OPEN-027-02). The candidate states the sentence as unlabelled narrative.
- **Repair:** either delete the sentence (§24 already carries the point), or align it to 1888 and keep it **[PROPOSED — CR-027]**.

### 6. Noe "knows" her registers will decide Gulf admission and county rankings (Contradiction in knowledge and chronology, plus a misstatement)

- Candidate ¶2: "she knows that her district registers will one day decide which territories enter the Gulf and how the county league tables rank them".
- **Chronology.** The Gulf Republic forms in 1899–1900 (l.566). Its admission test is a later Pacifican policy (l.568 onward). The county league tables come from the Office of Public Measures, founded after Elias's death (l.489) and run through the regency (§25). In January 1888 none of these exists for Noe to foresee. As written, the sentence is narratorial hindsight presented as Noe's knowledge.
- **Misstatement.** Canon's test decides whether the Gulf Republic may be **admitted to Pacifica**, not "which territories enter the Gulf".
- **Repair:** give her a period-plausible belief, for example that whoever holds the numbers will hold the argument over Hawaii's survival. Leave the Gulf and league-table consequences to the existing measures paragraph, where canon already places them in hindsight.

### 7. The Anne of Austria comparison (Authority breach)

- AGENTS.md: "Keep historical research, bibliographies and reasons for proposed divergences in `historical_background.md`, not explanatory comparisons in the storyline." The storyline must "read as what happens".
- The analogy also misleads. Anne of Austria was a regent, and the candidate gives Noe only guardianship of education, not the regency. Victoria is the one governing as Regent, so the parallel blurs §24's distinction: Victoria governs as Regent of a Realm "rather than as guardian obliged to surrender office on the boy's majority".
- **Repair:** remove it from the storyline. If you want the comparison, it belongs in `historical_background.md`, or in a character's mouth in manuscript prose.

### 8. The Chamber of Deputies grants the petition in January 1888 (Tension, in timing and institutional authority; needs a decision)

- **Timing.** The Chamber is "elected from 1888 on a plural franchise" under the 1888 Franchise Law (CR-021 constitutional table, l.86; `master_storyline.md` l.534). Canon doesn't say whether a Chamber is sitting in January 1888. A grant "by a large majority" in that month assumes an elected house already in session. This is possible but not established.
- **Competence.** Nothing in canon gives the Chamber power over the heir's household or education.
  - Under the 1887 Constitution the Regent rules and ministers "answer to the ruler, not the Chamber" (l.489).
  - The 1886 adoption is "hānai under Hawaiian custom" (CR-021 chronology), with Elias's written consent.
  - The Truce and Regency Council supply the governing balance (l.520).
- **Loyalist politics.** Hawaiian loyalists reject the 1887 Constitution (l.485), yet the loyalists courting Noe would see her petition the Realm's own Chamber. That can work as a deliberate move away from them, but the text should register it.
- **Decision for the author:** which body decides the matter (Chamber, Regent, Regency Council, or an ʻAha Aliʻi / Hawaiian customary forum)? Is a January 1888 sitting acceptable? Either needs a recorded decision before integration. The text shouldn't invent one silently.

### 9. Redundancy with the 1886 bargain, and Victoria "accepts every condition at once" (Tension in characterisation)

- Under the approved 1886 bargain Noe already holds "a place in the boy's life and Hawaiian upbringing" (l.476; CR-021 F1). The candidate doesn't say what the 1888 petition adds: legal title, enforceability against Victoria, or a check on the Regency Council. As written she petitions for something she already has.
- Canon characterises the women's relation as "Respect and fear, not simple jealousy" and as rivalry "over the boy and the future", and has Victoria govern "through bargaining" (§24). Instant, total acceptance "because she admires her courage" removes the bargaining and dulls the rivalry that §23 still describes in the next paragraph.
- It also bears on the death's ambiguity. If Victoria concedes everything, her motive weakens. If the guardianship is a real statutory office Victoria disliked, the motive strengthens (compare CR-016 E2: "her death … removes that claim, which strengthens the motive pointing at Kaiulani while the record stays inconclusive"). Either effect should be chosen deliberately so that the three-way balance of motive survives.
- **Repair:** make the petition gain something specific that Noe lacks, and let Victoria bargain over it, conceding in part.

### 10. Labels and coverage

- The candidate drops the **[APPROVED — CR-027]** marker on the Albert sentence (finding 1) and has no PROPOSED marker for Hollerith (finding 5).
- Noe's petition is new narrative beyond CR-021 F1. If you approve it, AGENTS.md requires a stable CR ID in `change_requests.json` and a coverage comment next to §23.
- Knock-on edits would follow in the same revision: §20 and §24 as needed, CT-JULIAN-MOTHER in `character_bible.md` and its registry profile ("natural guardianship makes her a possible regent"), followed by `validate_character_docs.py` and `sync_master_storyline.py --write/--check`. The candidate as submitted shouldn't be integrated before findings 1–7 are fixed.

## Compatible with canon (no change needed)

- Noe acting on her own initiative is not excluded. CR-021 R9-09 explicitly keeps "her agency, health work and hānai bargain", and nothing approved says she was merely passive. The core idea is open to the author.
- Kept intact: the autumn 1888 typhoid death, the official certificate by Victoria's physician, the servants' poisoning claim, the registers missing for a month and returning to the Office of Public Measures, the "Regent's year" rumour, Silas and Abigail's mutual suspicion, and "the Chronicler can prove none guilty". These match CR-021 F1 and CR-022, apart from the addition in finding 4.
- The Victoria measures arc (1888–1892 vaccination, 1890s nurses, water and Kalaupapa, the c.1895 upturn, infant mortality as the sacred number) and the Julian paragraph are verbatim canon. Only the consequences of findings 3 and 5 affect them.
- Retitling the section "Noe's move" doesn't break any reference I found. CR-016 and CR-021 cite "§23" by number only.

## Not covered

- I didn't review the first-draft manuscripts, `beats.json`, the CR-032 alternative timelines, the finance workbook or the power-review ontology. None of them governs §23 canon.
- I made no literary-quality judgement beyond where style rules overlap consistency (finding 7).
