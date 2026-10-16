# Pacifica — instructions for AI collaborators

## Canonical read order

1. `book-agent/revision/master_storyline.md` — **single continuous story synopsis**, with all currently approved narrative changes already embodied, and **[OPEN]** markers for unresolved decisions. Its prose must read as what happens, not as an edit memo.
2. `book-agent/revision/change_requests.json` — source of truth for explicit authorial approvals and remaining decisions.
3. `book-agent/revision/historical_background.md` — factual context, dated historical anchors, divergences, historical/legal uncertainties and source URLs.
4. `book-agent/revision/approved_change_index.md` — **generated** change-list and chronology, not story prose.
5. `book-agent/manuscript_chaptered.md`, `book-agent/beats.json`, `book-agent/character_bible.json`, `book-agent/bible.md`, `book-agent/concept.txt` — first-draft sources, potentially superseded by approved canon.

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

## Latest authorial decisions

Elias born c.1824; French Napoleonic engineering mentor preferred; 1840 Council House witness, 1841–42 Santa Fe captivity with Caleb; California independent in spring 1846 (not part of USA), public 1848 gold and 1852 treasury office rather than the presidency; Hawaii friendship with Lot and political alliance with Alexander, marriage to fictional Kaiulani (born 1838) in Honolulu 1857; Japan exchange and diplomacy 1849–1860; Hawaiian incorporation and massacre during succession crisis around 1874; later family tragedy and Julian's adoption; narrative largely chronological in a hybrid Chronicler/multi-POV form.

The uncommitted `rise_to_power.md` mentioned in chat was not accessible. Review it when supplied before claiming complete document-level reconciliation.
