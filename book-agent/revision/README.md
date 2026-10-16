# Pacifica — Revision workspace

## Read the story

**[Master Storyline](master_storyline.md)** is the single continuous, chronological account of the second-draft plot, from Elias's Kentucky childhood (born c.1824) to the fall of Pacifica around 1932. It integrates author-approved character, family, constitutional and geopolitical decisions directly into the narrative, without describing what used to happen in the first draft. Unsettled decisions are labeled **[OPEN]**.

Additional reference documents:
- [change_requests.json](change_requests.json) — the authoritative machine-readable record of approved authorial decisions and remaining questions.
- [historical_background.md](historical_background.md) — real dates, source links, legal/geopolitical context and precisely identified historical divergences. Kept separate to avoid turning the storyline into a research memo.
- [war_base_assumptions.md](war_base_assumptions.md) — immigration, revenue, military manpower, ships, weapons and infrastructure estimates with historical benchmarks and modeling caveats.
- [sources/rise_to_power.md](sources/rise_to_power.md) — the complete original author-supplied 1844–1861 proposal, archived unchanged.
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

## Reconciliation of rise_to_power.md

The full author-provided [rise_to_power.md](sources/rise_to_power.md) was uploaded and reviewed. Its narrative proposals are approved unless a specific historic, legal or numerical issue requires qualification. The definitive **Treaty of Edo is dated 1858**, explicitly overriding any alternative 1860 signing; the 1860 *Kanrin Maru* voyage is a follow-up. The March 1860/1858 treaty transition, July 1856 Pacifica Confederation, 1860 Washoe veto and 1861–65 legal ascent are integrated in the master storyline.

The 1864 domestic abolition of the Kuhina Nui cannot be assumed automatically to amend Article XIV of a treaty between states; the matter remains a constitutional question. Numerical figures for population, forces, naval construction and finances are model targets to test against historical benchmarks, not guaranteed facts.

These distinctions and any other remaining undecided matters are marked **[OPEN]** in the storyline or explicitly classified in the supporting reference files.
