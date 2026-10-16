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

Critical identity collisions: Elias's father Silas is not the later Silas claimant; Julian is Elias's biological son and Kaiulani's adopted son (not uncertain ancestry); Kaiulani's deceased legitimate child has no descendants; Marcus I, II and III are distinct generations; Kalanimoku's family tree is open; early and later Takashima/Kuroda, Shen, Hoshino and Kalākaua entries must not be silently merged; Dao's pronouns remain unresolved. This is not a complete list; see `character_bible.md`.

## Latest authorial decisions

Elias was born c.1824; childhood with a possible French Napoleonic engineer mentor; 1840 Council House fight and 1841–42 captivity with Caleb; independent California founded **31 May 1846**; public 1848 gold; Elias becomes Superintendent of Mines and Public Revenue in 1852 and First Minister c.1855.

**Pacifica is a Confederation of the California Republic and Hawaiian Kingdom, declared in Honolulu on 31 July 1856 and ratified that autumn.** Elias becomes Chancellor. Kaiulani, born 1838 and Kuhina Nui from 1855, marries him in February 1857 after ratification.

Japan: Shimoda arrangement c.1855, **definitive Treaty of Edo 1858**, then the *Kanrin Maru* voyage in **March 1860 as a treaty follow-up**. Never restore a 1860 Edo treaty signing.

The 1860 Washoe crisis involves Kaiulani's Article XIV veto; in 1861 she and California's president authorize a temporary Protectorship for Elias. The 1864 abolition of Kuhina Nui under Lot creates a constitutional dispute **not automatically solved by domestic law**. A 1865 settlement consolidates the Protectorate. Hawaiian incorporation and massacre occur in c.1874 after the royal succession crisis.

Family and later: lost legitimate child, Julian born c.1886–87 to a younger Hawaiian-American woman, adopted by Kaiulani after his mother's ambiguous death, eventual Julian Restoration in 1931. These and other unresolved genealogical details remain **[OPEN]**.

Population 1.2m, army and navy figures are narrative planning targets subject to demographic, engineering and financial auditing. Use `war_base_assumptions.md`.

The uploaded `rise_to_power.md` has been fully reviewed and archived as `book-agent/revision/sources/rise_to_power.md`. Its author-approved narrative proposals have been reconciled with the master storyline, with historical/legal exceptions documented explicitly.
