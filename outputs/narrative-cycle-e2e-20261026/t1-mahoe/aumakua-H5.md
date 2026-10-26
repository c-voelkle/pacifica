# Aumakua H5: consistency audit of the CR-033 candidate against current canon

**Session:** `outputs/sessions/20261026-noe-succession-move/` · **Brief:** `handoffs/H5-aumakua.md` · **Date:** 26 October 2026
**Mode:** Review only (R2). No canon edits, no `--write` sync. This ledger approves nothing and adopts no repair.
**Question:** If the candidate passages were merged into the master, could they all hold together with current canon and the governing approvals?

---

## 1. Conclusion

The candidate preserves every approved sentence word for word. Its chronology, ages and Noe's Kahekili descent are consistent with canon, and it establishes or implies no culprit. Three findings matter most:

1. **AUM-01 (suspected contradiction, high).** The new §26 rule, "no such body can act lawfully while the Territorial Council holds the legislature's place", does not fit the body the story assumes. The Council displaced the *legislature*, but the default consenting body is the *ʻAha Aliʻi*. Canon also gives the ʻAha Aliʻi lawful functions without saying when they begin: custody of crown and kuleana lands, which it "keeps" in 1914, and a collective stance in 1913. The CR draft lists "No … ʻAha Aliʻi sits in 1887–88" as preserved canon, but no canonical text says so (AUM-02).
2. **AUM-03 (integration mismatch, medium–high).** The sentence added to the death paragraph assumes that Truce factions and irreconcilables knew of the bargain in 1888. Under the draft's own default for OPEN-033-02, the undertaking is unpublished, and the draft assigns that wider knowledge to alternative (c). The same sentence also conflicts with the draft's B5 statement that "Realm constituencies are unaffected."
3. **AUM-04 (integration mismatch, medium).** Five mid-paragraph `[PROPOSED — CR-033]` insertions have no closing or return label. As a result, approved text that follows them (CR-027 A24's 1915 laying-down, the 1876-judgment sentence, the "no proven culprit" sentence) reads as if it fell under the PROPOSED label. The master's own label convention is already loose (AUM-12), but the candidate adds the problem to high-stakes approved passages.

Smaller items are listed below: AUM-05 (Supreme Court jurisdiction in 1887–88), AUM-06 (balance of motives), AUM-07 (how the petition reaches the sealed papers), AUM-08 (wording mismatches between the draft and the text) and AUM-11. Two tensions predate CR-033: AUM-09 (the canonical "natural guardian … regency" sentence) and AUM-10 (the ʻAha Aliʻi's status before 1914).

**Bounded result.** No contradiction was found in: the 1887–88 chronology (Donner, the January telegraphist, the 1888 restriction, the Office and Hollerith); ages; the 1887 regency article's "Heir of the Realm"; the 1914 plebiscite and Ka Lōkahi mechanics; Kahekili descent; Albert's description; or culprit protection (section 5). This finding covers only the material listed in section 2. It does not certify the whole text.

---

## 2. Scope, authority and coverage

### Authority order applied
`AGENTS.md` (current authority dated 23 October 2026) → `master_storyline.md` → `change_requests.json` (CR-016, CR-021 incl. R9-09, CR-022, CR-026, CR-027, CR-029) → CR reading records → `character_bible.md` / `character_registry.json` → `historical_background.md` (Hawaiian rows). The CR-033 draft and candidate passages are **Draft-mode proposals**. They are not canon.

### Source pins (sha256, 16-hex prefix)
| File | Hash | Note |
|---|---|---|
| `book-agent/revision/master_storyline.md` | `8b5df6f2b8bc9e32` | Matches the brief and `change_requests.json` `current_master_sha256` |
| `book-agent/revision/change_requests.json` | `7899e29f81298663` | Matches the CR-033 draft header |
| `book-agent/revision/character_bible.md` | `6b36de1bc0728fd7` | Matches the draft header |
| `book-agent/revision/character_registry.json` | `23bf3d9bc499bc7a` | |
| `book-agent/revision/CR-016.md` | `b45ef14c66e2303c` | |
| `book-agent/revision/CR-021.md` | `b1a63127ba7174b3` | Matches the draft header |
| `book-agent/revision/CR-022.md` | `1bd34f94758be655` | |
| `book-agent/revision/CR-026.md` | `f911e5f4b703bc19` | |
| `book-agent/revision/CR-027.md` | `773b18984c94b90e` | Matches the draft header |
| `book-agent/revision/CR-029.md` | `11f377359e9d45be` | |
| `book-agent/revision/historical_background.md` | `87ccd6ddb9b97cc7` | |

Git history was not inspected, so no commit is pinned. No `CR-033` string occurs in `change_requests.json` or the master.

### Coverage
| Material | Status |
|---|---|
| `AGENTS.md`; `.agents/skills/aumakua/SKILL.md`; `.agents/skills/aumakua/references/review-records.md`; `.agents/skills/mahoe/references/authority-and-scope.md` | Directly read, in full |
| `master_storyline.md` lines 1–919 | **Directly read, in full and continuously** |
| `candidate-sections.md`; `CR-033-draft.md` | Directly read, in full |
| `change_requests.json`: CR-016 (incl. `source_text`), CR-022, CR-026 | Directly read, in full |
| `change_requests.json`: CR-021 (all fields incl. R9-01–09 and OPEN-021 table), CR-027 (all fields), CR-029 (all fields) | Directly read, except the long `source_text` fields of CR-021 and CR-027 (unread there; see the `.md` files). CR-029's 21 `source_excerpts` were checked by script to be verbatim master paragraphs (21/21) |
| `CR-016.md` | Lines 1–36 read. The rest was compared by script with the register `source_text` I had read: only the precedence/integration header, E3, H5 and the OPEN-016-05/08 rows differ |
| `CR-022.md`, `CR-026.md`, `CR-029.md` | Script-verified as a provenance header plus master paragraphs, byte-identical (every non-header paragraph occurs in the master). Their content was therefore read through the master |
| `CR-021.md` | Directly read: lines 1–80, 100–130, 176–186, 340–529 (incl. B2, B6 table, D chronology, E, F, F1). Searched only: the rest (grep for Noe/guardian/ʻAha Aliʻi/court/heir/legislature) |
| `CR-027.md` | Directly read: lines 1–112 (summary, A table, B1–B8). Searched only: lines 113–300 (grep hits incl. C-section §23/§27 replacement text, E) |
| `character_bible.md` | Directly read: lines 40–111 (CT-KAIULANI, CT-LOST-SON, CT-JULIAN-MOTHER, CT-JULIAN), 489–511 (Hawaiian circle), 629–700 (safeguards, POV table, decisions), 878–957 (CR-027 figures incl. CT-ALBERT-KUNUIAKEA). Searched only: headings and the remainder |
| `character_registry.json` | Directly read: entries for CT-KAIULANI, CT-JULIAN-MOTHER, CT-JULIAN, CT-EMMA, CT-KALANIMOKU-HEIR, CT-ALBERT-KUNUIAKEA (links and status fields), `stats`, `warnings`. Searched only: term counts for ʻAha Aliʻi and guardian |
| `historical_background.md` | Hawaiian rows directly read: lines 35–45, 61–72, 283–302. Other Hawaiian mentions searched only (lines 140, 259, 261) |
| Not read | Every other repository file. `dependency_decisions_211026.md` and the outputs it links to. All withheld session files |

### Independence and prior exposure (R5)
- Withheld and **not opened**: `session.md`, `kalai-H3-notes.md`, `imi-H2.md`, `clio-H1.md`, and any H4/H6 output. A single directory listing of the session folder showed their file names (including `imi-H4.md`, `aegis-H6.md` and `directions-neutral.md`); none was opened.
- **Partial exposure:** the CR-033 draft and the notes in `candidate-sections.md` include the writer's own pre-flagging. B1 flags the regency sentence, B5 the 1913 ʻAha Aliʻi stance, OPEN-033-05 the court and "Clio's possible repository mismatch". Findings AUM-05 and AUM-09, and part of AUM-01, overlap with those flags, so they are not fully independent detections. The table records this in the "Detection origin" field.
- No prior review ledger was shown, so prior-issue reconciliation is still **pending**.

### Tool checks actually run (read-only, unchanged baseline)
| Check | Result | What it establishes | What it does not establish |
|---|---|---|---|
| `python3 book-agent/revision/sync_master_storyline.py --check` | Exit 0: "Approved-change index synchronized; approved CR IDs referenced in master storyline." | The baseline's generated index and CR coverage IDs are in sync | Nothing about CR-033, which is not registered, nor about the literary consistency of the candidate |
| `python3 book-agent/revision/validate_character_docs.py` | Exit 0: "Character documents valid: all canonical IDs, links and 250 legacy profiles agree." | The baseline's bible, registry and crosswalk agree structurally | Nothing about the candidate (it proposes no registry edits) or about narrative consistency |
| Scripted text checks (this audit) | All 11 baseline quotes in `candidate-sections.md` equal the cited master lines. Each candidate passage equals its baseline plus insertions only, with no deletions. All 11 inserted spans equal the CR draft §C text; the two that difflib aligned ambiguously (§26 and line 850) were re-verified by rebuilding them from the §C anchors. Each §C anchor occurs exactly once in the master | No approved sentence is altered, and the CR draft and candidate agree textually | Nothing about whether the inserted content is consistent with canon. That is the subject of the ledger |
| Ontology runtime | `rdflib` and `pyshacl` are not installed (import fails). Nothing was installed | — | **No graph integration, SHACL validation or graph-suggested candidates. None is claimed.** This audit is prose-first only |

---

## 3. Issue ledger

Fields follow `review-records.md`. All items are new detections in this first H5 pass, with lifecycle **Open** unless stated. Ontology trace for every item: *unavailable (runtime not installed); no Finding or SourcePassage IRIs.* Prior issue mapping for every item: *no prior review shown; reconcile after the independent sweep.*

### AUM-01: The §26 "no lawful chiefly body" rule against the ʻAha Aliʻi's canonical functions
- **Classification:** Suspected contradiction (candidate-introduced; it depends on the pre-existing gap in AUM-10).
- **Evidence:**
  - Candidate §26 (insertion after master line 622): "her undertaking of 1888 requires the consent of a lawful body of chiefs, and no such body can act lawfully while the Territorial Council holds the legislature's place **[OPEN-033-03]**."
  - CR draft D, OPEN-033-03 (a): "The ʻAha Aliʻi, as it acts in 1914. No such body can act lawfully while the Territorial Council stands, which explains the wait to 1914 (§26 sentence)." Default: "The story wording assumes (a) in §26 and §27."
  - Master line 432 [APPROVED — CR-027]: the 1876 Territorial Council "takes over the legislature's business".
  - Master line 634 (1914): "It dissolves the Territorial Council and restores Hawaii's legislature. … The ʻAha Aliʻi keeps custody of Hawaiian crown and kuleana lands".
  - Master line 632 (1913): "The ʻAha Aliʻi will proclaim only Julian".
  - `CR-021.md` line 126, B2 (APPROVED): "Hawaiian crown and kuleana lands are in the custody of the ʻAha Aliʻi." Line 183, B6 (APPROVED): Honolulu holds "The ʻAha Aliʻi, the Hawaiian historic land …". The B6 table is introduced as the map of the 1887 Truce factions (line 186), though its rows span eras.
  - Master line 489 (1887 constitution): the Senate includes "eight aliʻi seats".
- **Aligned scope:** Hawaii, 1888–1914. Lawful status of chiefly bodies under the Territorial Council. Stance: narrator fact in §26, not a character's belief.
- **Incompatibility:**
  1. *Reason versus body.* The rule derives the bar from the displacement of the **legislature**. The default consenting body is the **ʻAha Aliʻi**, which canon never places inside the legislature. The 1914 Act "restores Hawaii's legislature" and says nothing about constituting the ʻAha Aliʻi. Under (a), the stated reason does not produce the stated bar. It would follow under (b), the House of Nobles.
  2. *Rule versus function.* If the ʻAha Aliʻi held lawful custody of crown lands at any time between 1888 and 1914 ("keeps custody" in 1914; B2 custody under the Realm's division of powers), then a lawful chiefly body *could* act while the Council stood, and §26's narrator rule is false under (a).
  3. The 1887 constitution seats eight aliʻi in a lawful (legal in form) Senate. They are not "a body of chiefs", but they show that lawful chiefly participation exists in the period.
- **Alternative readings:** (i) "keeps custody" means custody conferred or confirmed *from* 1914, and B2 describes the post-1914 Realm. Then no lawful pre-1914 ʻAha Aliʻi function exists, but nothing in canon states this. (ii) The ʻAha Aliʻi exists informally before 1914 and becomes lawful only with the Act, as the draft's B5 assumes ("declared intention of chiefs who are not yet sitting lawfully"). This reading is only in the draft's notes; the prose does not convey it. (iii) OPEN-033-03 (b), the Nobles, matches the reason given, but the 1914 prose names only the ʻAha Aliʻi as the proclaiming and plebiscite body, and "Nobles consent" would be a new detail. **What would settle it:** an author statement on whether, and from when, the ʻAha Aliʻi holds lawful functions before the 1914 Act.
- **Consequence:** High. The §26 sentence is the candidate's only explanation for the 1888–1914 wait, and the §27 clauses rely on it. If canon has a lawful ʻAha Aliʻi before 1914, Victoria could have obtained consent earlier, and the delay becomes a choice that needs another reason.
- **Repair options (proposals only; the body is an open author choice):** (a) Drop the §26 sentence. The draft already lists this as the fallback under OPEN-033-03 (c). (b) Re-anchor the reason to OPEN-033-03 (b) and state it as such, accepting a new "Nobles consent" detail at line 634. (c) Turn the narrator rule into a stance, for example that Victoria or the chiefs hold no consent given under the Council lawful. This weakens the claim but is still a premise the author must accept. (d) The author decides AUM-10 first. Affected passages: candidate §26 (line 622), §27 (lines 632, 634), CR draft OPEN-033-03, B4 and B5.
- **Detection origin:** Prose first. The draft's B5 flags the 1913 point but not the mismatch between the legislature reason and the ʻAha Aliʻi, nor the custody function.

### AUM-02: The draft presents a new premise as preserved canon
- **Classification:** Integration mismatch (within the CR-033 draft).
- **Evidence:** CR draft A, "Preserved without change": "No Hawaiian legislature, House of Nobles or ʻAha Aliʻi sits in 1887–88." CR draft Summary: "It adds no institution, sitting body, office, quantity, genealogy or culprit." Against this, canon says only that the Council took the *legislature's* business (line 432). For the ʻAha Aliʻi, see AUM-01 evidence (CR-021 B2/B6; line 634 "keeps custody"). The §26 rule ("no such body can act lawfully …") is a legal disability that is not recorded among decisions A1–A12.
- **Aligned scope:** Draft labelling of what is canon and what is new; Hawaii 1887–1914.
- **Incompatibility:** The legislature half of the "preserved" statement is supported. The ʻAha Aliʻi half is not stated anywhere in canon. The §26 rule is a new premise (R3), yet the summary says nothing of the kind is added and the A-table does not carry it as a PROPOSED decision.
- **Alternative readings:** The writer may intend "sits" to mean "sits as a lawful body", in which case the point reduces to AUM-01 and AUM-10.
- **Consequence:** Medium. A reader of the CR would assume the premise is settled canon when deciding OPEN-033-03.
- **Repair options:** Move the ʻAha Aliʻi clause out of "Preserved without change" into a PROPOSED decision (for example a new A-row tied to OPEN-033-03), or delete it. Amend the summary sentence accordingly. Affected: CR draft A (preserved list), Summary, D OPEN-033-03.
- **Detection origin:** Prose first.

### AUM-03: Knowledge of the undertaking in 1888 (death-paragraph sentence) against the OPEN-033-02 default and B5
- **Classification:** Integration mismatch. Under the draft's default it is also a suspected contradiction of the knowledge bounds.
- **Evidence:**
  - Candidate §23 (third new paragraph): "The chiefs Noe brought over witness it, and it is not published **[OPEN-033-02]**."
  - Candidate line 511 insertion: "irreconcilables who watched the banner they courted make terms with the Regent, factions for whom word of an heir made by Hawaiian forms unsettles the Truce, and a Regent who signed under pressure **[OPEN-033-07]**."
  - CR draft OPEN-033-02: default (a) "witness it; it is not published". Alternative (c): "The loyalists and Truce factions know of it in 1888, which sharpens the irreconcilables' and factions' motives".
  - CR draft B5: "**Japanese and Realm constituencies** are unaffected. The undertaking concerns only the Hawaiian crown".
- **Aligned scope:** Autumn 1888 and earlier. Who knows that Victoria undertook a Hawaiian-form heirship. The Truce factions are Silas's inland command, Kiyoshi's naval party and Soberanes's Polytechnic (master lines 499–503).
- **Incompatibility:** The "factions" motive needs Truce factions to have heard of the undertaking in 1888. The draft itself assigns that knowledge to alternative (c), not to default (a). It also contradicts B5's claim that Realm constituencies are unaffected. "Watched … make terms" likewise implies that irreconcilables knew of a bargain, not merely that Noe stopped being their banner.
- **Alternative readings:** (i) Leakage through witnessing chiefs is plausible, but it is an unstated bridge. (ii) Irreconcilables could infer terms from visible behaviour (chiefs moving to the Regent's heir). This supports the first clause better than the second. (iii) Under OPEN-033-07 (b) the sentence disappears and the mismatch with it.
- **Consequence:** Medium–high. It widens knowledge beyond the stated default and adds Realm-faction motives to a protected mystery.
- **Repair options:** (a) Take OPEN-033-07 (b) and keep the paragraph verbatim. (b) Keep only the irreconcilables clause, worded as inference from visible conduct, and drop the "factions … word of" clause. (c) Adopt OPEN-033-02 (c) as the default and amend B5. All three are author choices. Affected: candidate line 511, CR draft OPEN-033-02/07 and B5, the Julian/Noe trajectory ("more suspects than he knew").
- **Detection origin:** Prose first.

### AUM-04: Mid-paragraph PROPOSED insertions leave approved text inside the PROPOSED label
- **Classification:** Integration mismatch (R1 label attachment).
- **Evidence (candidate text, each without a return label after the inserted clause):**
  - Line 634: "to reign as Kamehameha VI, **[PROPOSED — CR-033]** on the Queen's appointment as she undertook in 1888 **[OPEN-033-03]**; Senate and Chamber confer the Realm's sovereignty by two-thirds. In 1915 Victoria lays down both the regency and her crown, and Julian accedes to both. …". The 1915 sentence is CR-027 A24 (APPROVED).
  - Line 638: "**[PROPOSED — CR-033]** the two halves Noe refused to separate in 1888. Loyalists dispute whether a hānai son may continue the Kamehameha line. The Act heals much politically, but does not reverse the Supreme Court's ignored judgment of 1876. **[APPROVED — CR-026]**". The 1876-judgment sentence rests on OPEN-021-05 (APPROVED) as amended by CR-027.
  - Line 850: "**[PROPOSED — CR-033]** In 1888 she refuses … then returns to the typhoid wards. Her 1888 death has an official typhoid account and incompatible testimony, with no proven culprit. …". This is R9-09 (APPROVED) material.
  - Lines 632 and 838 have the same pattern: the rest of each paragraph follows the PROPOSED marker.
  - Pre-existing convention (master line 642): "**[PROPOSED]** he is born about 1916. Exact wedding and birth dates remain qualified. The heir will reign in Hawaii as Kamehameha VII". Approved CR-021 text follows a PROPOSED marker there too.
- **Aligned scope:** Label status of individual sentences in the merged master.
- **Incompatibility:** Under the master's working reading, a marker governs the text after it until the next marker. On that reading, approved commitments would display as PROPOSED — CR-033. That detaches labels from the details they qualify, contrary to R1 and AGENTS.md ("Preserve APPROVED, PROPOSED, OPEN and MODEL distinctions"). The candidate's notes state that the approved text is unchanged, which is true of the words but not of how their label displays.
- **Alternative readings:** If the convention is "a marker governs only its own sentence or clause", the insertions are harmless. The master does not define the convention, and line 642 shows the ambiguity already exists.
- **Consequence:** Medium. Approval status is the repository's core safeguard, and the affected sentences include the 1915 accession, the 1876 judgment and "no proven culprit".
- **Repair options:** (a) After each inserted clause, restore the governing label for the text that follows (for example re-mark the remainder with its prior label, or "canon" where it had none). (b) Move each CR-033 clause into its own sentence at the end of the paragraph. (c) Define a closing convention repository-wide (see AUM-12). Affected: candidate lines 632, 634, 638, 838, 850 and the corresponding CR draft §C instructions.
- **Detection origin:** Prose first.

### AUM-05: The Hawaiian Supreme Court's sitting and jurisdiction in 1887–88
- **Classification:** Missing bridge, needing clarification. Not a contradiction, because canon is silent.
- **Evidence:**
  - Candidate §23: "she has a guardian's petition drafted for the Hawaiian Supreme Court, the court whose judgment of 1876 the Queen let stand unenforced **[OPEN-033-05]**."
  - CR draft OPEN-033-05 (a, default): "the court that judged in 1876 still sits."
  - Master line 483: "The Constitution of the Realm of 1887 abolishes the states … California and Hawaii remain historic lands … the Court of the Realm sits at Monterey". Line 487: county boards keep "ordinary policing, with appointed judges and central standards".
  - `CR-021.md` lines 128–129 (B2, APPROVED): a single criminal and commercial code; civil law "A single code with historic-land exceptions: Spanish community property in California, Hawaiian land tenure". Line 141: "County courts of first instance have judges appointed by the Realm."
  - Master lines 432 and 638 mention the Supreme Court only for its 1876 judgment.
- **Aligned scope:** Hawaii, winter 1887 to spring 1888. Civil jurisdiction over the custody of the Heir of the Realm.
- **Incompatibility:** None stated. Canon never says the Hawaiian Supreme Court survives 1887. The 1887 judicial structure (states abolished, Realm courts, a single civil code whose Hawaiian exception covers *land tenure*, not family law) makes its jurisdiction over guardianship doubtful. The default asserts that the court survives without support from canon.
- **Alternative readings:** The court survives as an organ of the Hawaiian crown, which persists (Victoria still reigns), much as a Hawaiian legislature exists to be "restored" in 1914. Because the petition is never filed under OPEN-033-01 (a), the story needs only a credible threat, not a hearing.
- **Consequence:** Medium. The lever ("honour a Hawaiian court she once failed, or fail it a second time") depends on the court existing and being competent.
- **Repair options:** The author settles OPEN-033-05. If (b) or (c) is chosen, the §23 text can stand as written. If the court is held abolished in 1887, the lever must be re-based on the chiefs' witness alone, which is OPEN-033-04 (b)'s fallback. Affected: candidate §23, §29 ("petition … never filed"), CR draft B2.
- **Detection origin:** Prose first, also pre-flagged by the draft (OPEN-033-05). Not independent.

### AUM-06: Balance of motives around the protected death
- **Classification:** Missing bridge, needing clarification. Not a contradiction; no culprit is established or implied.
- **Evidence:**
  - Candidate §23: "Noe stops being the loyalists' banner"; "It is the Queen's promise, and Noe's death would release no one from it."
  - Candidate line 511 addition (see AUM-03), which adds irreconcilable and Truce-faction motives.
  - CR draft A10: "widens the plausible motives … without weighting any one".
  - Master line 509: "Her rivalry with Victoria concerns the boy and Hawaii's future".
  - Bible CT-JULIAN-MOTHER: "The approved event preserves real uncertainty rather than making Victoria guilty by implication."
  - Earlier provenance, CR-016 E2 (PROPOSED, superseded on Noe by CR-021 rev. 9): her death "removes that claim, which strengthens the motive pointing at Kaiulani".
- **Aligned scope:** Motives for Noe's death in autumn 1888. Narrator stance: motive, not evidence.
- **Incompatibility:** No logical conflict. However, the narrator's statement that the undertaking survives Noe's death, together with Noe ceasing to be a rival claimant by spring 1888, removes one concrete motive for Victoria. At the same time the candidate adds concrete motives for others. That is a re-weighting in effect, against A10's "without weighting". R9-09 governs and requires only "no culprit established", so the governing approval is satisfied. The concern is with the draft's own claim about balance.
- **Alternative readings:** The retained baseline sentence still gives Victoria motives, and "a Regent who signed under pressure" adds a resentment motive. A reader may judge the balance preserved.
- **Consequence:** Low–medium. This concerns the texture of the protected mystery, not its protection.
- **Repair options:** (a) Keep A7 in the CR record but drop "and Noe's death would release no one from it" from the narrator prose. (b) Adopt OPEN-033-07 (b). (c) The author accepts the shift explicitly. Affected: candidate §23, line 511, CR draft A7 and A10.
- **Detection origin:** Prose first.

### AUM-07: How the unfiled petition reaches the regency's sealed papers
- **Classification:** Missing bridge.
- **Evidence:** Candidate §23: "She does not file it … She shows it to Victoria." Candidate §29: "Among them are the Queen's undertaking of 1888 and the guardian's petition his birth mother drafted and never filed **[OPEN-033-01]**." Master line 511: "The registers disappear for a month and return in the new Office of Public Measures."
- **Aligned scope:** Custody of Noe's papers, 1888–1915.
- **Incompatibility:** None stated. The text does not say whether Noe handed the petition over as part of the bargain or whether it came into the regency's papers from her effects after death. The second route parallels the registers' disappearance and would bear on the protected mystery.
- **Consequence:** Low–medium. It affects how readers weigh the Regent's household; it does not make a contradiction.
- **Repair options:** The author picks the route, or leaves it deliberately ambiguous and marks it OPEN (for example under OPEN-033-01). Affected: candidate §23 and §29, CR draft A12.
- **Detection origin:** Prose first.

### AUM-08: Wording mismatches between the CR draft and the passages
- **Classification:** Integration mismatch (low).
- **Evidence:** (i) CR draft A11: "the ʻAha Aliʻi's proclamation of Julian **is** the Queen's appointment". §C and candidate line 634 read "proclaims Julian heir … **on** the Queen's appointment". B4: "as the Queen's appointment". (ii) Summary: "The draft adds one new instrument, the 1888 undertaking". A3 and A12 add a second new document, the unfiled petition, with its own downstream use in the §29 sealed papers.
- **Incompatibility:** (i) The A11 wording equates proclamation with appointment; the text sequences appointment, then proclamation. (ii) The count of new documents understates the change.
- **Consequence:** Low.
- **Repair options:** Align A11 and B4 with the text (or the reverse). Say "one new instrument and one unfiled draft petition". Affected: CR draft A11, B4, Summary.
- **Detection origin:** Prose first.

### AUM-09 (pre-existing): "As natural guardian she could claim a regency" against the constitutional regency
- **Classification:** Suspected contradiction, pre-existing. The candidate keeps it verbatim and does not worsen it.
- **Evidence:**
  - Master line 509: "As natural guardian she could claim a regency". `CR-021.md` line 510 (F1, APPROVED): "As natural guardian Noe could claim the regency". Bible CT-JULIAN-MOTHER: "Noe's natural guardianship makes her a possible regent". `CR-016.md` line 102, E2 (PROPOSED): "a competing claim to the regency of her own child".
  - Against these, master line 483: "A regency article names Victoria, Queen of Hawaii, Regent of the Realm until an Act of Settlement establishes the Crown". Master line 520: "Victoria governs as Regent of a Realm whose crown has yet to be established, rather than as guardian obliged to surrender office on the boy's majority."
- **Aligned scope:** Realm regency from August 1887. Legal basis.
- **Incompatibility:** The Realm regency is a named constitutional office that canon explicitly distinguishes from guardianship. "The regency" (CR-021 F1) and "a possible regent" (bible) cannot rest on natural guardianship under that article. No Hawaiian regency is vacant while the Queen reigns, and the Kuhina Nui is vacant from 1876 (line 432).
- **Alternative readings:** "Could claim" is a political assertion the loyalists entertain because they reject the 1887 constitution, not a lawful title. This is the draft's reading (B1). It is compatible, but it is not stated in canon.
- **Consequence:** Medium for canon generally, low for CR-033.
- **Repair options:** Author's choice (CR draft F3): keep the sentence as the loyalists' framing, possibly with a stance marker, or reword it. Not decided here. Affected: master line 509, CR-021 F1, bible CT-JULIAN-MOTHER.
- **Detection origin:** Prose first, also pre-flagged by the draft (B1). Not independent.

### AUM-10 (pre-existing): The ʻAha Aliʻi has no constituting instrument or pre-1914 status
- **Classification:** Missing bridge, pre-existing. AUM-01 depends on it.
- **Evidence:** Master line 632 (1913 collective stance); line 634 (1914 plebiscite role; "keeps custody"); line 774 (1928 custody); `CR-021.md` B2 line 126 and B6 line 183 (APPROVED). No canonical sentence says when or how the ʻAha Aliʻi is constituted, or whether it functions lawfully under the Territorial Council. The 1887 constitution (line 489) mentions only aliʻi Senate seats.
- **Aligned scope:** Hawaii, 1876–1914.
- **Incompatibility:** None internally until a candidate asserts a lawful status. Canon allows both "lawful custodian from 1887" and "constituted only by the 1914 Act".
- **Consequence:** Medium. It governs AUM-01 and any future scene with chiefs in 1888–1913.
- **Repair options:** The author states the ʻAha Aliʻi's status before 1914. If it is lawful from 1887, OPEN-033-03 (a) cannot carry the §26 reason.
- **Detection origin:** Prose first.

### AUM-11: Julian's existing Realm heirship rests on Council assent
- **Classification:** Missing bridge (low).
- **Evidence:** Candidate §23: "an heir made by the Council would be the ordinances' heir, and the chiefs she has turned would never accept him." Master line 483: the regency article names "Julian Heir of the Realm". Line 485: "Hawaii's assent comes from the appointed Territorial Council … Hawaiian loyalists reject it."
- **Incompatibility:** None. The undertaking concerns only Hawaiian heirship. But the text does not acknowledge that Julian's existing Realm heirship already rests on a Council-ratified constitution, which a careful reader of Noe's reasoning will notice.
- **Consequence:** Low.
- **Repair options:** Optional clause, or leave as is. Author's choice.
- **Detection origin:** Prose first.

### AUM-12 (pre-existing, related to AUM-04): The master has no label-closing convention
- **Classification:** Integration mismatch, pre-existing (repository convention). Lifecycle: Open; it lies largely outside this audit's scope of the CR-033 candidate.
- **Evidence:** Master line 642, as quoted under AUM-04. Master line 109: "**[PROPOSED — CR-028]** Pico asks the admiral for protection. … The Republic learns that it will have no patron." There, a run of text follows the marker with no marked end.
- **Consequence:** Medium as a repository-wide matter. Only these two instances were checked; no full label audit was run.
- **Repair options:** A repository-level convention decision. Not proposed in detail here.
- **Detection origin:** Prose first.

---

## 4. Item raised inside the CR draft: reconciliation (not a prior review)

- **CR draft B3/E, "`historical_background.md` line 44 may mislabel the 1864 Article 22 as fictional".** **Not reproduced internally.** Line 44 reads: "Article 22 of Lot's fictional 1864 constitution names Victoria heir". This labels Lot's *divergent* 1864 constitution as fictional, consistent with line 42, line 69 and CR-027 A8/A10. I found no internal mislabel. Whether the historical Article 22 contained an appointment-with-consent-of-the-Nobles clause is an external research question. It is **outside scope** for this audit (no web research) and belongs to Clio.

---

## 5. Checks with no finding (bounded)

| Check from the brief | Result |
|---|---|
| Any candidate sentence implying a Hawaiian legislature, House of Nobles or ʻAha Aliʻi **lawfully sitting** before 1914 | None. §23 uses individual "chiefs" and "witness"; §26 denies lawful sitting; §27 line 632 keeps the baseline. The tension runs the other way (AUM-01, AUM-10) |
| 1913 ʻAha Aliʻi stance (line 632) against the §26 rule | Reconcilable only through the draft's unstated "declared intention" reading. Recorded under AUM-01 |
| 1887 regency article: Victoria Regent, Julian Heir of the Realm | No conflict. The undertaking excludes only Hawaiian heirship by the Council or the Realm constitution; draft B5 is accurate on this point (AUM-11 notes a minor bridge) |
| 1914 Act, plebiscite and Ka Lōkahi | No conflict. The CR-029 plebiscite sentence is untouched. Ka Lōkahi's vote "over the succession" (line 636) applies after 1914 and does not confer Julian's own heirship. The Act's adopted-heir rule with Senate consent concerns later succession |
| Winter 1887–88 timing | Consistent: after Donner (October 1887, line 505), overlapping the January 1888 telegraphist death (line 511), before the autumn 1888 death. "Undertaking of 1888" is used consistently (§26, §27, §29, trajectories). 1914 − 1888 = 26 years (B4/B5) |
| 1888 restriction, Office of Public Measures (1888), Hollerith tabulation from 1888 | Untouched. The registers are explicitly outside the bargain (A8), consistent with the POV table ("How her rivals will use her honest figures after her death") |
| Ages | Julian born 1886 (1–2 in 1887–88; 21 in 1907). Victoria born 1 November 1838 (49 until 1 November 1888, so "49–50" holds) |
| Knowledge, default OPEN-033-02 (a) | §26, §27 and §29 are compatible (narrator relative clauses, the Regent's knowledge, Julian's finding the document). The death-paragraph sentence is not (AUM-03) |
| Noe's descent | "her own Maui line, which traces its descent to Kahekili" matches master line 472, CR-021 F1 and bible CT-JULIAN-MOTHER. No new genealogical link |
| Albert Kūnuiākea | Not re-described. "Albert's partisans keep their candidate" is consistent with CR-027 A16 and the bible ("no reign or successful revolt") |
| Invented named chiefs | None |
| Culprit | None established or implied. R9-09 sentences are retained verbatim; the §29 and trajectory additions state that the papers do not show how she died |
| APPROVED, PROPOSED and OPEN labels; approved sentences | All new text is labelled PROPOSED — CR-033 with OPEN-033-nn bridges. No approved sentence is altered (scripted check). The CR-022 PROPOSED label at line 662 is preserved. Label *scope* is the exception (AUM-04) |
| CR draft A1–A12 and §C against `candidate-sections.md` | Textually identical insertions, with unique anchors. Semantic mismatches: AUM-02, AUM-03 (against B5 and OPEN-033-02), AUM-08 |
| "a Hawaiian court she once failed" against line 432 | Compatible: she "lets the ruling stand on paper" |

---

## 6. Open uncertainties

- The status of the ʻAha Aliʻi before 1914 (AUM-10) decides whether AUM-01 is a contradiction or a request for clarification.
- The label-scope convention (AUM-04, AUM-12) is undefined in the repository.
- The persistence of Hawaiian judicial organs after 1887 is undefined (AUM-05).
- Historical evidence on Article 22, custody doctrine and hānai practice was not examined (no web research). The draft's B3 items remain [HIST-U].
- Prior findings (H1–H4, H6) have not been reconciled. Their reconciliation should map each earlier issue to retained, resolved, not reproduced or outside scope against AUM-01 to AUM-12.
