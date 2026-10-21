# Pacifica — instructions for AI collaborators

## Canonical read order

1. `book-agent/revision/master_storyline.md` — **single continuous story synopsis**, with all currently approved narrative changes already embodied, and **[OPEN]** markers for unresolved decisions. Its prose must read as what happens, not as an edit memo.
2. `book-agent/revision/change_requests.json` — source of truth for explicit authorial approvals and remaining decisions.
3. `book-agent/revision/historical_background.md` — factual context, dated historical anchors, divergences, historical/legal uncertainties and source URLs.
4. `book-agent/revision/war_base_assumptions.md` — demographic, treasury and military scenario assumptions to audit, not assert as fact.
5. `book-agent/revision/sources/rise_to_power.md` — original author-provided early-history proposal; preserve verbatim as an archival source.
6. `book-agent/revision/character_bible.md` — **authoritative character arcs and differentiated voice guidance** for the second draft.
7. `book-agent/revision/character_registry.json` — stable character IDs and documented relationships, including unresolved genealogy.
8. `book-agent/revision/legacy_character_crosswalk.json` — maps all 250 original character sketches to confirmed/provisional identities or retained secondary profiles.
9. `book-agent/revision/approved_change_index.md` — **generated** change-list and chronology, not story prose.
10. `book-agent/manuscript_chaptered.md`, `book-agent/beats.json`, `book-agent/character_bible.json`, `book-agent/bible.md`, `book-agent/concept.txt` — first-draft sources, potentially superseded by approved canon.

## Mandatory on author approval

- Revise the **actual narrative prose** in `master_storyline.md`, including knock-on effects across later sections, **before** calling it integrated. Never merely write a new entry saying the old material will be changed. Don't fill unresolved decisions with unsupported inventions.
- Update the structured CR or add a stable new CR ID in `change_requests.json`.
- If adding a CR, add its stable ID in a hidden coverage comment in the synopsis adjacent to the relevant plot section; the checker confirms IDs, not literary quality.
- Keep historical research, bibliographies and reasons for proposed divergences in `historical_background.md`, not explanatory comparisons in the storyline.
- Run `python3 book-agent/revision/sync_master_storyline.py --write`, then `--check`; commit all three related files when applicable. The push-triggered workflow updates the generated `approved_change_index.md`. The PR workflow rejects stale administrative synchronization.
- Never claim that generated index synchronization guarantees literary integration. It does not. Review the narrative in light of the author’s approval.
- Preserve `main`, old manuscripts, original beat and character sources until the author authorizes an actual prose revision; use review branches and PRs.
- Do not mistake an editorial proposal, assistant suggestion or historical illustration for author-approved canon.

When presenting the story, link only to `master_storyline.md`. For source claims use the historical background document.

## Character documentation

Use the canonical character bible and registry for all character work. `book-agent/character_bible.json` remains an **unmodified original 250-profile source** referenced by legacy generation tools; it contains superseded character facts. Never use it to override approved kinship or chronology.

After an explicit author decision affecting character identity or development, update the master storyline where the plot changes, the narrative character bible and the identity registry in the same revision. Preserve the original profiles and update crosswalk mappings rather than deleting them. Run `python3 book-agent/revision/validate_character_docs.py`. CI also checks it.

Critical identity collisions: Elias's father Silas is not the later Silas claimant; Julian is Elias's biological son and Victoria’s adopted son (not uncertain ancestry); Victoria’s deceased legitimate child has no descendants; Marcus I, II and III are distinct generations; Kalanimoku's family tree is open; early and later Takashima/Kuroda, Shen, Hoshino and Kalākaua entries must not be silently merged; Dao's pronouns remain unresolved. This is not a complete list; see `character_bible.md`.

## Current authorial authority (21 October 2026)

Follow the current master storyline, CR register and CR-027 after the source-qualified decisions embodied in the supplied 21 October storyline. CR-021 revision 9 continues to govern where later decisions do not supersede it. Later explicit author decisions override the older source proposals and labels. Preserve APPROVED, PROPOSED, OPEN and MODEL distinctions.

CR-014 retains the Kuhina Nui under Lot. Constitutional amendment and member ratification govern enabling authority; do not restore the superseded personal-veto or abolished-office explanations. The western peace framework is 1865, with Senate ratification in 1867.

Noe Kaʻanoe Ward is Julian’s mother; the hānai adoption bargain is made in 1886, before her ambiguous death in 1888. Never establish a murderer. Victoria Kamāmalu is Queen of Hawaii from December 1872 and Regent of Pacifica from 1887. The legal fifty-year Puʻuloa lease of 1874 precedes illegal ordinances of 1874–1876 and the ignored 1876 judgment. There is no massacre or throne abeyance. The 1914 Act joins crowns and dissolves the appointed Council; Julian accedes to both in 1915. Kahekili / Ikazuchi is the future Kamehameha VII; preserve his existing stable ID CT-KALANIMOKU-HEIR and distinguish the lost Kalanimoku.

The Constitution of the Realm uses 124 counties. Tongue votes are uncapped. The Pacific Concord has coequal crowns; Julian is Sovereign/Mōʻī, never President. Annual Councils are at Hayama. Illegal provisional application in 1927 receives consent and indemnity in 1928. The crowns agree the 1932 renewal at Hayama, and ministers sign/exchange instruments at Thalassia; the renewal runs to 1937.

Prince Chichibu is Japan’s resident representative at Thalassia, educated in Pacifica in 1925–26 instead of Oxford. His honors and outdoorsman reputation develop in Pacifica, expressing Japan’s turn toward Pacifica instead of Britain. Do not invent specific decorations, climbs or command authority. At least one common minister must be Japanese, conventionally Navy; Foreign Affairs and Finance normally remain Pacifican.

Dawes remains incumbent during the 1931–32 rescue and negotiations. Young campaigns for acceptance, wins in November 1932 and assumes office in 1933. Korea is independent and guaranteed after 1905, with agreed economic, military and transit rights. From 1921 the Siberian Republic holds Kamchatka, the Okhotsk coast and Nikolayevsk; Japanese access is treaty-only.

Keawe’s environmental arc leads from Living Bay to the 1928 plan and 1932 Lands and Waters Charter. The Gulf remains outside membership; all five general measures and two parity tests must hold for twenty-five years. Numerical and financial results remain MODEL estimates, with unresolved feasibility questions retained.

The character registry contains 132 stable identities, including six retired records, with all 250 original profiles preserved through the legacy crosswalk. Read the current character documentation before resolving any identity collision.

## Current financial planning files

The author supplied and explicitly authorized publication of `finance/Pacifica_financial_model_1846-1932.xlsx` and `finance/Pacifica-Ledger.md` on 20 October 2026, superseding earlier financial models. Use this pair for current financial planning. Preserve supplied files verbatim. Older assessments under `outputs/pacifica-finances-*` are dated comparisons, not the current model. The ledger reports CR-021 revision 8; the narrative remains at revision 9. Do not revert narrative decisions or claim that publication constitutes independent recalculation. Financial results remain MODEL estimates.

CR-027 retains CT-KAIULANI as Victoria’s active stable ID and retires CT-VICTORIA-KAMAMALU as duplicate provenance. CT-KAIULANI-CLEGHORN is the separate princess born 1875. Preserve proposed Five personnel, instruments and mythic echoes. Historical CR attachments are not rewritten; earlier Kaiulani means Victoria. The missing CR-022/024/025/026 originals are represented only by source-qualified excerpts in dependency_decisions_211026.md. Section E’s financial handoff is finance/CR-027-handoff.md; do not infer a rent amount or recalculate the workbook without a separate financial task.
