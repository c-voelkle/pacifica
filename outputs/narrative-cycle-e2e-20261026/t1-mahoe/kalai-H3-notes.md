# Kalai H3: impact notes and self-review

**Brief:** `handoffs/H3-kalai.md` · **Mode:** Draft (R2). Nothing was adopted. · **Date:** 26 October 2026
**Deliverables:** [CR-033-draft.md](CR-033-draft.md), [candidate-sections.md](candidate-sections.md), and this file. Nothing else was written. `master_storyline.md`, `change_requests.json`, the character bible, the registry, `historical_background.md`, all CR files and `alternatives/` are untouched. I ran no sync script and made no commit.

## Baseline and files read

These are the files the brief listed, with sha256 16-hex prefixes:

| File | Hash |
|---|---|
| AGENTS.md | `1e574d3c958cfdeb` |
| `.agents/skills/kalai/SKILL.md` | `fb0f0609339d9650` |
| `.agents/skills/mahoe/references/authority-and-scope.md` | `8e73ecce96740521` |
| `master_storyline.md` | `8b5df6f2b8bc9e32` |
| `change_requests.json` | `7899e29f81298663` |
| `CR-021.md` | `b1a63127ba7174b3` |
| `CR-027.md` | `773b18984c94b90e` |
| `CR-016.md` | `b45ef14c66e2303c` |
| `CR-029.md` | `11f377359e9d45be` |
| `character_bible.md` | `6b36de1bc0728fd7` |
| `clio-H1.md` | `cc4201f1c431a214` |
| `H3-kalai.md` | `256629d20909efa1` |

- **Master:** read in full, lines 1–919, including §17–§29, the trajectories and the unresolved list, continuously.
- **CR-021:** the chronology at 350–389 and F1 at 484–529.
- **CR-016:** E1–E3 only.
- **Character bible:** CT-KAIULANI, CT-JULIAN-MOTHER, CT-JULIAN, the Hawaiian circle (including CT-EMMA), CT-ALBERT-KUNUIAKEA and the perspective table.
- **Not read:** git history, `session.md`, `imi-H2.md` (withheld), `character_registry.json` and `historical_background.md` (not listed).
- **Hashes:** the master, CR-021, CR-027, CR-016 and character-bible hashes match Clio's H1 pins, so the draft and the dossier share a baseline.

**CR number:** I found no `CR-033` in `change_requests.json` (the latest is CR-031-R1), in any `book-agent/revision/` filename, or in the master. The number stays provisional, as the draft header states.

## Impact notes

- **Changed premises:**
  - **One new instrument.** The 1888 written undertaking constrains the *form* of Julian's Hawaiian heirship: the Queen's appointment with the consent of a lawful body of chiefs, never by the Council or the Realm constitution.
  - **One unfiled document.** The guardian's petition.
  - **A partial shift of loyalist chiefs to Julian.** The chiefs are unnamed.
- **Unchanged assumptions:**
  - Victoria is Regent and Queen; no succession war; consolidation 1887–89; §22 Donner and Truce untouched.
  - No sitting Hawaiian legislature, Nobles or ʻAha Aliʻi before 1914.
  - Noe's death exactly as R9-09 has it. Registers outside the bargain.
  - The 1914 plebiscite remains Victoria's own act ("as she did not ask them in 1874"). The 1876 judgment is unreversed. The "eldest son" delay is kept. The Realm Heir designation of 1887 is untouched.
- **Affected passages:**
  - Master lines 509 (three new paragraphs after it), 511, 622, 632, 634, 638, 662, 838, 850 and 895.
  - Line 909 was considered and left unchanged.
  - The full list of passages read and left unchanged is at the end of `candidate-sections.md`.
- **Dates and ages:**
  - Julian is about 1–2 years old in 1887–88, and Victoria 49–50.
  - The undertaking is 26 years old at the 1914 Act.
  - The move sits after Donner (October 1887) and before the autumn 1888 outbreak (OPEN-033-08).
- **Author choices needed:**
  - OPEN-033-01 to 08 (draft §D).
  - Whether to keep the canonical "natural guardian … regency" sentence as political framing.
  - Confirmation of the CR number.
- **Historical support:**
  - Every legal comparator in the CR (Article 22's appointment clause, Alexander Liholiho, *Nash*, *Barnardo*, *Chapsky*, Iturbide, customary reclaiming) is Clio's **[HIST-U], unverified in this run**. It is confined to CR §B3 and §E and kept out of story prose.
  - None should go into `historical_background.md` until it has been checked against Clio H1 §9's sources.

## Self-review

This is self-review by the same agent that wrote the draft. It is not independent review (R5). The withheld H2 review has not been reconciled here.

**Brief conditions, checked against the draft text:**

| Condition | Result |
|---|---|
| Undertaking narrower than the 1914 plebiscite; she exceeds it | Met. The plebiscite sentence is untouched, and the trajectory says "gives her people more than she promised". |
| Registers outside the bargain; Noe honest, with a blind spot | Met (§23 third paragraph: "does not ask who will use them after her"). |
| Health work frames her last year; she dies fighting the outbreak | Met. |
| No §22 additions; Regent and Queen; no war; consolidation holds | Met. §22 is unchanged. "The Truce" appears only as a motive clause in §23. |
| No Hawaiian body sitting in 1887–88 | Met in the prose. See issue 1. |
| Synopsis form, no dialogue, no legal argument in prose | Met. The case names and comparators are only in the CR notes. |
| Every new detail labelled; bridges carry OPEN-033-nn with alternatives | Met. There are 13 PROPOSED labels in the candidate passages and eight OPEN entries, each with alternatives. |
| No culprit established or implied | Met. Motives are added without evidence or weighting, and §29 says the papers "do not show how she died". The line 511 sentence lists the new motives in no order and is optional (OPEN-033-07). |
| Temptation to reclaim the boy in one clause | Met ("taking him back, however tempting, would cut away the half of his claim…"). |
| No named invented chiefs | Met. |
| Baseline quoted verbatim | Met. All 11 baseline quotes were checked programmatically against the master lines, and each CR §C anchor occurs exactly once. |

**Issues found and left visible:**

1. **The 1913 ʻAha Aliʻi stance.** Baseline line 632 has the ʻAha Aliʻi resolved in 1913, before the Act restores the legislature. Under OPEN-033-03 (a) I read this as a declared intention of unsitting chiefs. The added clause does not resolve whether the ʻAha Aliʻi exists as a body before 1914. CR §B5 and OPEN-033-03 carry the choice. This is a pre-existing ambiguity, which the draft surfaces and does not resolve.
2. **The canonical "regency" sentence.** "As natural guardian she could claim a regency" (APPROVED via CR-021 F1) has no legal basis on Clio's reading. I kept it verbatim as the loyalists' political framing and reported the tension (R1). I did not reword it.
3. **Unpublished, yet a motive.** Under the default that the undertaking is unpublished, "factions for whom word of an heir made by Hawaiian forms unsettles the Truce" depends on rumour. I kept "word" deliberately, but if OPEN-033-02 (b) is chosen, the clause weakens.
4. **The petition as a threat.** It is unfiled by default, so its force is the choice it puts to Victoria, not a court act. The prose says "Filed, it would leave the Queen two courses". A reviewer should check that this is enough to explain why Victoria concedes. The draft relies on her concessions also serving her (A4).
5. **The registry was not read.** I noted relationship changes as "check on adoption".
6. **Literary review.** I have not tested whether three PROPOSED paragraphs in §23 overweight Noe's last year relative to the section. The death paragraph and §23's later paragraphs (lines 513 and 515) were read after drafting and still follow without contradiction.

**Not claimed:** I have not established literary quality, historical accuracy of any [HIST-U] item, or validator or sync status. Nothing is adopted.
