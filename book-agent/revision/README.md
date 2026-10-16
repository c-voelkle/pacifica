# Pacifica — Revision workspace

## Read the story

**[Master Storyline](master_storyline.md)** is the single continuous, chronological account of the second-draft plot, from Elias's Kentucky childhood (born c.1824) to the fall of Pacifica around 1932. It integrates author-approved character, family, constitutional and geopolitical decisions directly into the narrative, without describing what used to happen in the first draft. Unsettled decisions are labeled **[OPEN]**.

Additional reference documents:
- [change_requests.json](change_requests.json) — the authoritative machine-readable record of approved authorial decisions and remaining questions.
- [historical_background.md](historical_background.md) — real dates, source links, legal/geopolitical context and precisely identified historical divergences. Kept separate to avoid turning the storyline into a research memo.
- [approved_change_index.md](approved_change_index.md) — automatically generated administrative index of all approved CRs and provisional chronology, **not part of the story**.

## Procedure for any newly approved storyline change

1. **Amend the actual plot** in the relevant sections of `master_storyline.md`. Carry consequences forward through subsequent generations, institutions and events. Use positive, affirmative narrative statements—not instructions to undo older versions. Mark unchosen facts **[OPEN]**.
2. Record the author-approved decision in `change_requests.json` (maintain stable CR identifiers and precise approval statuses). Distinguish author-approved choices from editorial options, research findings and proposals.
3. Refresh the separate administrative index with `python3 book-agent/revision/sync_master_storyline.py --write`. The GitHub sync workflow also performs this on a change-register push.
4. Run `python3 book-agent/revision/sync_master_storyline.py --check`. This checks the index and that approved CRs have an editorial coverage reference in the synopsis. PR checks run it too.
5. Review the actual narrative implications before merging the change into the authoritative revision. An automated index **cannot** author or judge literary prose, and neither a CR identifier nor a passing CI test proves substantive narrative reconciliation.

## Authority and scope

An explicit author approval changes the planned canon even if the first-draft manuscript or original `beats.json` still says otherwise. Authorial approvals and the master storyline govern planning; the earlier draft is evidence of material to preserve or transform, not a competing source of canon.

Do not revise `manuscript_chaptered.md`, `beats.json`, `bible.md`, or the production writing scripts until the author authorizes manuscript reconstruction. Keep canon changes on the revision branch and under review.

## Unavailable temporary working document

The author referred to `rise_to_power.md` on 16 October 2026. It was **not present on accessible GitHub branches** when the update was made. The detailed proposals provided in the chat were incorporated directly, and supporting historical anchors were checked against published sources. If that file is later committed, compare its contents with the master storyline and historical background; merge only genuinely new material and preserve established author approvals.
