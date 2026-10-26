# Kalai H7: CR-033 v2 disposition and self-review

**Brief:** `handoffs/H7-kalai.md` · **Mode:** Draft (R2), round 2. Nothing is adopted. · **Date:** 26 October 2026
**Deliverables:** [CR-033-draft-v2.md](CR-033-draft-v2.md), [candidate-sections-v2.md](candidate-sections-v2.md), and this file. The v1 files (`CR-033-draft.md`, `candidate-sections.md`, `kalai-H3-notes.md`) are byte-identical to their H5/H6 pins (`56b907ec…`, `98193c9a…`; notes `c7f32cc3…`).
**Not touched:** `master_storyline.md`, `change_requests.json`, every CR file, the character bible, the registry, `historical_background.md` and `alternatives/`. No sync script was run and nothing was committed. One scratch script (`_h7_build.py`) was written in the session folder, run with `python3 -I`, and deleted. Nothing was written outside the session folder.

## Baseline and files read

| File | sha256 prefix |
|---|---|
| AGENTS.md | `1e574d3c958cfdeb` |
| `.agents/skills/kalai/SKILL.md` | `fb0f0609339d9650` |
| `.agents/skills/mahoe/references/authority-and-scope.md` | `8e73ecce96740521` |
| `book-agent/revision/master_storyline.md` | `8b5df6f2b8bc9e32` (unchanged after the run) |
| `book-agent/revision/CR-021.md` | `b1a63127ba7174b3` |
| `book-agent/revision/CR-027.md` | `773b18984c94b90e` |
| `book-agent/revision/CR-029.md` | `11f377359e9d45be` |
| `book-agent/revision/character_bible.md` | `6b36de1bc0728fd7` |
| `handoffs/H7-kalai.md` | `28aa431f6932e87e` |
| `imi-H4.md` / `aumakua-H5.md` / `aegis-H6.md` | `9faa429eb92ab59d` / `15317503e36f8548` / `ceff515ab716fe7b` |
| `clio-H1.md` | `cc4201f1c431a214` |
| Outputs: `CR-033-draft-v2.md` / `candidate-sections-v2.md` | written this run (hashes not fixed here, because this file is written after them) |

**What was read:**
- The master in full, lines 1–919.
- CR-021 lines 60–194 (summary, the constitution table including line 85, B1–B6) and 340–534 (chronology §D including the 1886 row and line 382, E, F, F1).
- CR-027 lines 1–120 (summary, A1–A27, B1–B9).
- CR-029 in full.
- From the character bible: CT-KAIULANI, CT-LOST-SON, CT-JULIAN-MOTHER, CT-JULIAN, CT-ALBERT-KUNUIAKEA and the perspective table.
- Every session file the brief listed, in full.

**Not read:** `session.md` and `imi-H2.md` (withheld), any other session file, `change_requests.json`, the registry and `historical_background.md`.

**Disclosure:** while checking that the run had written nothing outside the session folder, I ran one `git status --porcelain`. It listed deletions under `outputs/narrative-cycle-skills-20261026/` that this run did not make; they were already present when the sandbox was provided. I did not view any git history (log, diff or show).

## Disposition table

**Legend:**
- **Applied:** v2 does it.
- **OPEN:** carried as an OPEN entry or as an author item in CR v2 §F.
- **Declined:** not done, with the reason given.
- **No action:** the finding requires nothing, for example a confirmation.

### Coordinator repair items

| ID | Disposition | Where / note |
|---|---|---|
| M1 exchange order | **Applied** | §23 P1: "She will not be their banner, but she does not yet tell them so." P2: "Noe tells the loyalists she is no one's banner…", after the signing. Victoria's gain is "Noe's public refusal of the loyalists". "However tempting" is kept. A1, A4. |
| M2 threat vs her choice | **Applied** | "Both women know she does not want the custody it asks for; what she can use is the hearing and its witnesses." A3 labels this as a perception, not a fact. B2. |
| M3 clarity of the lever | **Applied** | The "Filed, it would leave the Queen two courses…" sentence now comes first. The reason follows as her tactic: "Noe keeps it unfiled, a threat in hand being worth more than a ruling no one can enforce." |
| M4 Victoria's own reason | **Applied** | "…and an heir of the Council's making would be no more hers than Noe's." The concession stays by choice, and Noe's win stays primary. The trade-off is recorded in A4. |
| M5 allies' motive | **Applied** | OPEN-033-06 default is now (b): "from the chiefly families of her Maui kin and among her Queen's Hospital patrons" (CR-027 A20). No names. |
| M6 compress §23 | **Applied in part** | Three paragraphs become two. The reason list goes from four items to three ("she gave her word in 1886" is cut). The registers are one clause ("they are figures, not terms"). "Unbargained" and "does not ask who will use them after her" are cut. **Net length did not fall:** 510 words against v1's 501, because M1, M2, M4, M5 and M10 each add a clause. Further cuts the author could take, about 35 words: "and watches her read it", "With those chiefs behind her,", "a threat in hand…enforce", and the leverage list (moving it to A4 only). I kept them because Imi asked for one character beat at the confrontation and for the lever's logic on the page. |
| M7 release sentence | **Applied** | Cut from prose. A7 stays in the CR, marked "record only". |
| M8 Realm constitution phrase | **Applied** | "nor by the Realm constitution that already names him its Heir". Also answers AUM-11. |
| M9 line 511 verbatim | **Applied** | OPEN-033-07 (b) is the default. (a) is recorded only, reworded: before the "Victoria…" clause, no "under pressure", inference from visible conduct only. A10 now says the reader can infer motives with no narrator statement, and it acknowledges AUM-06's re-weighting point and Imi's counter-lean. |
| M10 custody of documents | **Applied** | "…leaves the petition with the Queen, who keeps both papers [OPEN-033-09]". New A13. §29 sees the papers through the Queen's keeping. The new OPEN-033-09 asks whether Noe kept a copy and what became of it, and explicitly not via her effects or the registers' month. |
| M11 replace §26 rule | **Applied** | The v1 rule is deleted. New sentence: "Nor does she name him her Hawaiian heir before the Act: her undertaking of 1888 sets no date, and the chiefs who witnessed it wait." It makes no legal claim about chiefly bodies, and A14 ties it to CR-021 line 382. "No … ʻAha Aliʻi sits in 1887–88" is removed from "Preserved without change". AUM-10 is recorded as a pre-existing gap. OPEN-033-03: body unspecified (d). (b) Nobles is kept listed but dropped from the recommended set. |
| M12 line 632 clause | **Applied** | Dropped. Line 632 is now verbatim. Imi's "among whose elders…" alternative is recorded under OPEN-033-06 (cross-referenced to 03) and §F 8, not in prose. |
| M13 line 634 | **Applied** | Own sentence after the approved proclamation sentence, which is not restructured: "The proclamation is the Queen's appointment with the ʻAha Aliʻi's consent, as she had undertaken in 1888." A return marker **[APPROVED — CR-029]** follows (M14). R-2's further option goes in §F 6. |
| M14 label scope | **Applied** | §23 uses whole new paragraphs. Line 622 sits before the existing CR-022 marker. Line 638 is its own sentence before the existing CR-026 marker. Lines 634 and 662 get return markers. Lines 838, 850 and 895 put their sentences at the paragraph end, because those paragraphs have no labels a return marker could restore. The convention is written up as CR B6 and §F 5 (AUM-12). See self-review issue 2 for the literary cost. |
| M15 trajectories and §29 | **Applied** | The line-838 clause "and in 1914 gives her people more than she promised" is deleted. The second line-850 addition is deleted. §29's CR-033 sentences now come *before* "He tells no one that he knows.", and the close still lands in my reading. |
| M16 CR record fixes | **Applied** | A11 now reads "is". The summary says "one new instrument … and one unfiled draft petition". CR-021 citations are limited to the 1886 row, F1 and the line-382 note that M11 requires; the abeyance/massacre rows (I-4) are not cited. The line-44 claim is replaced with Aumakua's finding (B3). §B gains I-3 (latent liability), R-3 (stakes) and the Realm-Act coupling, checked and found **removed conditionally**: it returns only if AUM-10 goes "no pre-1914 standing" *and* OPEN-033-03 (a) is chosen (B5). AUM-05 goes under OPEN-033-05. AUM-09 goes under §F 3. |

### Imi H4

| Point | Disposition | Note |
|---|---|---|
| Imi R1, exchange out of order (§1) | **Applied** | M1. |
| Imi R2, threat contradicts her choice (§1) | **Applied** | M2. |
| Imi §1, confrontation still summary | **Applied (minimal)** | "She shows it to Victoria and watches her read it." This gives the beat to Noe's eyes. The "two courses" analysis stays the Chronicler's. |
| Imi §1, allies lack motive | **Applied** | M5. |
| Imi §2, Victoria's reason defined by Noe | **Applied** | M4, with the trade-off in A4. |
| Imi §2, "a Regent who signed under pressure" | **Applied** | The sentence is gone (M9). The recorded (a) drops "under pressure". |
| Imi §2, line-838 "more than she promised" | **Applied** | M15. The bible note in CR §E now also says not to describe the plebiscite as exceeding the undertaking. |
| Imi §3.1, sequence leans toward Victoria | **OPEN (acknowledged)** | Inherent in the design. Imi says it cannot be removed entirely. Recorded honestly in A10. The additions around it now add no weight. |
| Imi §3.2, added motive sentence | **Applied** | M9. |
| Imi §3.3, release sentence | **Applied** | M7. |
| Imi §3, line-850 "Beside them…" placement | **Applied** | M15 deletes it. The remaining Noe sentence now ends the paragraph after "more suspects" (M14); the risk is in self-review issue 2. |
| Imi §3, §29 well guarded | **No action** | Kept word for word. |
| Imi §4, weight of §23 / two paragraphs | **Applied in part** | M6. Length is not reduced; see M6. |
| Imi §4, reason list as checklist | **Applied** | Three items. |
| Imi §4, register sentences | **Applied** | One clause. |
| Imi §4, unused "Regent's year" resonance | **Declined** | This was a noted opportunity, not a fix. Adding it would lengthen §23 against M6 and would lean the death sequence further toward Victoria. |
| Imi §4, §26 collides with 632 | **Applied** | M11 removes the rule, and with it the collision. |
| Imi §4, 632 clumsy | **Applied** | M12 (option a). |
| Imi §4, 634 "as she had undertaken" | **Applied** | M13. |
| Imi §4, 638 earned | **Applied (moved)** | Kept, now its own sentence (M14). It no longer sits directly after "adoption by a Kamehameha queen"; it answers the loyalist dispute instead. |
| Imi §4, §29 insertion point | **Applied** | M15. |
| Imi §4, trajectories bookkeeping | **Applied** | M15. |
| Imi §4, item 11 administrative | **No action** | Kept; now points to 01–09. |
| Imi §5, sentence order of the lever | **Applied** | M3. |
| Imi §5, "conferred by the Constitution of the Realm" | **Applied** | M8. |
| Imi OPEN preferences 01 (a), 02 (a), 04 (a), 05 (a), 08 (a) | **No action (defaults unchanged)** | They match the v1 defaults. |
| Imi OPEN preference 03, none | **No action** | M11 sets the recommended set. |
| Imi OPEN preference 06 (b) | **Applied** | M5. |
| Imi OPEN preference 07 (b) | **Applied** | M9. |
| Imi routing to Aumakua (632 vs §26; who knows under 02) | **Resolved** | AUM-01 and AUM-03 below. |

### Aumakua H5

| ID | Disposition | Note |
|---|---|---|
| AUM-01 §26 rule vs ʻAha Aliʻi functions | **Applied** | The rule is deleted (M11). The §26 sentence makes no claim about chiefly bodies. |
| AUM-02 new premise presented as preserved canon | **Applied** | Removed from "Preserved". The summary no longer claims "no sitting body". New A14 carries the wait as PROPOSED. |
| AUM-03 knowledge of the undertaking vs line 511 | **Applied** | The line 511 sentence is removed (07 (b)). B5 now says no Truce-faction motive is added. The recorded (a) uses only visible conduct. |
| AUM-04 label scope | **Applied** | M14. Every case is listed in candidate-sections-v2. |
| AUM-05 Supreme Court after 1887 | **OPEN** | Under OPEN-033-05, with (a) flagged as an assumption, and in B2. |
| AUM-06 balance of motives | **Applied + acknowledged** | M7 cuts the narrator sentence. A10 states the re-weighting honestly: one concrete Victoria motive is weakened, and the sequence leans the other way. The draft does not claim the two cancel. |
| AUM-07 petition's route to the sealed papers | **Applied** | M10 / A13; the copy question is OPEN-033-09. |
| AUM-08 wording mismatches | **Applied** | A11 "is" matches the line-634 sentence. The document count is corrected. |
| AUM-09 "natural guardian … regency" (pre-existing) | **OPEN** | B1 and §F 3. The sentence is unchanged. |
| AUM-10 ʻAha Aliʻi pre-1914 standing (pre-existing) | **OPEN** | "Not settled by this CR" and §F 4. It governs whether the Realm-Act coupling returns. |
| AUM-11 Realm heirship rests on Council assent | **Applied** | M8. |
| AUM-12 no label-closing convention (pre-existing) | **OPEN** | B6 and §F 5. v2 uses a return-marker convention that the author must confirm. |
| AUM §4 line-44 reconciliation | **Applied** | M16 / B3. |

### Aegis H6

| ID | Disposition | Note |
|---|---|---|
| I-1 aliʻi Senate seats vs §26 rule | **Applied** | The rule is deleted. Whether aliʻi senators could satisfy the undertaking stays inside OPEN-033-03 (d) (B5). |
| I-2 proclamation bundled in the Act | **Applied in part / OPEN** | A separate sentence names the Queen's appointment with the ʻAha Aliʻi's consent. Full separation from the Act's provisions would restructure approved text, so it is an author option (§F 6). |
| I-3 petition premise vs adoption half | **Applied (recorded)** | In B5 as a latent liability; it stays latent under 01 (a) and 09 (a). |
| I-4 stale CR-021 rows | **Applied** | Only the 1886 row, F1 and the line-382 note are cited. The staleness is reported in §E, not fixed (CR-021 is not to be edited). |
| I-5 custody 1888–1915 | **Applied** | M10 / A13 / OPEN-033-09. |
| R-1 OPEN-033-03 | **Applied in substance (via M11)** | v2 takes the core of R-1 (ii): the wait is Victoria's own choice under line 382. It does not adopt the "Queen may convene the ʻAha Aliʻi" variant as default, because that depends on AUM-10. (c) is listed and now compatible. R-1 (i) (the aliʻi-senators clause) is **declined**: it would reintroduce a legal claim about chiefly bodies, which M11 forbids. (b) is avoided, as R-1 advises. |
| R-2 1914 packaging / public recital | **OPEN** | §F 6. |
| R-3 early-death gap | **Applied (as stakes) / OPEN** | B5 keeps the gap visible as stakes. A testamentary appointment is an author option (§F 7); it is not supplied. |
| R-4 keep 01 (a) | **Applied** | Default unchanged. |
| R-5 keep 02 (a) | **Applied** | Default unchanged. (c) is marked as advised against. |

Aegis's dependencies D-1 to D-3 (for Clio) and D-4 (Albert's status after 1888) are not in the brief's list. They remain open and are untouched by v2. Its §11.5 comparator, C-033m, is in §F 1.

## Re-run checks

| Check | Result |
|---|---|
| Baseline quotes | All 11 baseline passages in `candidate-sections-v2.md` equal master lines 509, 511, 622, 632, 634, 638, 662, 838, 850, 895 and 909, copied by script. |
| Candidates are baseline plus insertions only | For each of the 8 changed passages, removing the CR-033 insertions (and the two new §23 paragraphs) gives back the baseline line exactly. No baseline word is altered or deleted. |
| Anchor uniqueness | Every anchor used to place an insertion occurs exactly once in the master. |
| CR §C ↔ candidates | All 9 inserted fragments are character-identical in `CR-033-draft-v2.md` §C and `candidate-sections-v2.md`, because both were generated from the same strings. |
| Labels | 9 `[PROPOSED — CR-033]` markers in the candidates. OPEN-033-01 to 09 each appear in the CR with alternatives. 2 return markers. |
| Inputs and v1 files unchanged | The hashes of the master, the CRs, the bible and the three v1 session files are identical before and after the run. |

These checks establish textual integrity only. They say nothing about literary quality or canon consistency, which the self-review below covers.

## Self-review

This is **self-review** by the same agent that wrote v1 and v2. It is not independent (R5). I read all three review files in full, so I am not independent of them either. The coordinator's repair decisions were applied as directed; I found no demonstrated regression that required departing from one.

**Continuity read.** I read §20–§29 and the trajectories in the unchanged master (hash identical before and after) and read each candidate insertion in place against its surrounding text.
- §20 → §23: "she lives to see neither" still holds.
- §23 P1/P2 → death paragraph: winter offer, spring undertaking, summer wards, autumn typhoid; the paragraph follows without contradiction.
- Lines 513 and 515 follow unchanged.
- §24's 1887–89 consolidation is undisturbed.
- §26: "Nor does she name him… before the Act" sits naturally after "Victoria delays while the eldest son lives".
- §27 line 630: "outlast a Regent of seventy-five" now also carries R-3's stakes.
- Line 632: the ʻAha Aliʻi's 1913 stance is unchanged and no longer in tension.
- Line 634: the new sentence follows the approved proclamation and precedes the return marker.
- Line 638: see issue 2.
- §29: the close lands.
- Trajectories: see issue 2.
- No culprit is added, no chief is named, and no Truce-faction knowledge is assumed.

**Issues left visible:**

1. **§23 is not shorter (M6).** It went from three paragraphs to two, but the word count is 510 against 501. The weight Imi flagged, about three times the Donner paragraph, remains. The possible cuts are listed under M6. This is an author or literary call; I did not take the cuts because each serves a repair or an Imi point.
2. **The M14 placements have a literary cost.**
   - At lines 838 and 850 the CR-033 sentence now ends the paragraph. The paragraphs carry no labels, so a return marker had nothing to restore.
   - At line 838 the Donner/Altai sentence loses its place as the close.
   - At line 850 the Noe sentence follows "Noe's death had more suspects than he knew". It speaks of her agency and ends on the wards, not on documents or motives, but this is next to the placement Imi warned against. A reader could take it as an answer to "more suspects".
   - At line 638 "the two halves" is two sentences away from the phrase it answers.
   - The fix is a repository label convention for unlabelled canon (AUM-12; CR §F 5), after which the v1 positions could return with return markers.
3. **The return-marker convention is new.** At lines 634 and 662 it relies on reading "a marker governs until the next marker; a paragraph boundary closes it". The master never states this rule. At line 634 the restored label is CR-029's, although the 1915 sentence's substantive approval is CR-027 A24, as AUM-04 noted. The display is "APPROVED" either way.
4. **"Before the Act" (§26) slightly extends the claim.** It is consistent with line 634, where the proclamation comes with the Act, and makes no legal claim. It does say Victoria makes no appointment between 1888 and 1914, which the baseline only implied.
5. **The Realm-Act coupling can return.** It comes back if the author settles AUM-10 as "no pre-1914 standing" and picks OPEN-033-03 (a). B5 says so.
6. **The weak court premise remains (AUM-05).** The 1887 judicial structure makes the Hawaiian Supreme Court's guardianship jurisdiction doubtful. The lever survives only because the petition is unfiled.
7. **The registry was not read** in H3 or H7. The relationship changes are listed as "check on adoption".
8. **The CR number was not re-checked.** `change_requests.json` was not in the H7 file list, so the absence of CR-033 is carried from v1.

**Not claimed:** literary quality, historical accuracy of any [HIST-U] item, validator or sync status, or independence of this review. Nothing is adopted.
