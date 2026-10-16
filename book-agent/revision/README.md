# Pacifica — approved revision framework

## One document containing the full working story

**Read [master_storyline.md](master_storyline.md) first.** It is the single chronological review narrative covering Elias's childhood, the independent Californian republic, the Hawaiian marriage and family tragedy, the Japanese alliance, the American wars, the empire's expansion, successive generations, Julian's restoration and the final collapse. It labels approved canon, retained first-draft material, proposals and unresolved questions.

The master storyline is the narrative reading copy; `change_requests.json` is the structured approval record.

### How future approvals are synchronized

1. When the author explicitly approves a new or modified plot request, record it in `change_requests.json` and update the relevant **authored chronological prose** in `master_storyline.md` in the same revision.
2. Run `python book-agent/revision/sync_master_storyline.py --write` from the repository root. This rebuilds the automatically managed approved-change index and timeline in the master storyline.
3. Run `python book-agent/revision/sync_master_storyline.py --check`. It fails if the index is stale or a newly approved CR ID is missing from the authored narrative.
4. Push on a revision branch. The `pacifica-storyline-sync.yml` GitHub Action also refreshes and commits the generated index following a change-register push. `pacifica-storyline-check.yml` checks synchronization on pull requests. Keep the pull request in review if an approved change has not been integrated in the narrative.
5. After approval, merge the reviewed change set. Do **not** modify `manuscript_chaptered.md`, original `beats.json`, or the production writing scripts until the author authorizes a rewrite.

**Scope of automation:** GitHub can regenerate the approved-change index from structured data and check for missing CR IDs. It cannot reliably invent or reconcile complex literary prose from an informal approval. An explicit approval given only in a chat must still be entered into the repository (by the assistant when working on the repository, or manually). The full narrative prose must be revised editorially, not assumed current just because its generated appendix is current. The workflows also depend on GitHub Actions being enabled and permitted to push in this repository.


Recorded 16 October 2026. This file is planning documentation, not revised novel prose.

## Author-approved direction
- **Chronology:** Primarily chronological with selective retrospection.
- **Form:** Hybrid historical chronicle and independent character POV scenes.
- **Length:** No preset length; scene space follows artistic necessity.
- **Workflow:** Collect and assess authorial storyline changes before structural reconstruction.

The structured source of truth for these approvals is [change_requests.json](change_requests.json). It records CR-001 through CR-008, provisional chronology, affected sources, and explicit guardrails.

## Family thread — approved direction
Elias Thorne and Kaiulani marry with genuine affection and political interests. Their legitimate son dies in an accident, and Kaiulani is afterward unable to have children. Their marriage deteriorates without simply dissolving: shared government, ambition, attachment and political necessity keep them together. Elias has affairs and children outside the marriage. During his final years, a much younger Hawaiian-American woman (possibly his caretaker) becomes the mother of Julian Thorne. After Elias's death in 1887, she dies in uncertain circumstances. Kaiulani adopts Julian and raises him as her son. Julian has independent choices and later becomes the Restorer.

**Important:** This approves the dramatic relationships, not a final medical explanation, named victim of the childhood tragedy, specific calendar year for each event, or a definitive solution to the succession genealogy. Kaiulani's responsibility for the younger woman's death is **not settled**. The exact dynastic lineage of Kalanimoku remains open. If Julian is born c.1886–87, he is c.44–45 in 1931, replacing the draft's stated age 32.

## Hawaiian political crisis — approved direction
The monarchy does **not** suddenly deny its son-in-law existing naval access. Instead, the cooperative alliance develops toward increasing military, financial and administrative dependence. Elias eventually imposes control, provoking royalist resistance and a bloody suppression the Hawaiian king and Kaiulani cannot stop. He does not threaten Kaiulani with a massacre of hostages to secure her obedience. Kaiulani stays for complex political and personal reasons, including ambitions of her own.

## Californian sovereignty — approved direction
Replace the draft's secret-gold/corporate-coup/1852-secession scenario with an independent republic established around 1845–46, before U.S. statehood. The coalition and 1846 U.S. naval threat must be dramatized plausibly. The 1848 gold discovery is public and regulated under a sovereign mineral framework. Britain's possible recognition and support are not to be treated as a guaranteed military shield.

## Editorial safeguards
- Kaiulani remains a major strategist and political agent in her own right.
- The legitimate son must be a character, not merely a casualty invented to manipulate the plot.
- Infertility and jealousy do not fully account for the marriage's deterioration.
- Julian's mother has an autonomous life, status and choices.
- Preserve the ambiguity around her death unless the author later resolves it.
- Julian's eventual ideology and actions are contingent, not inevitable.
- Elias's greatness must be earned through observed learning, organization, alliances, failure, and formidable adversaries.
- None of the recorded approvals authorize a rewrite of `manuscript_chaptered.md` or a change to existing `beats.json` yet.

## Next planning work
1. Continue collection of remaining storyline changes.
2. Produce a canonical identity/genealogy decision register and event-level timeline with source references.
3. Reconcile each approved change with manuscript passages and original beats.
4. Propose a new sequence and scene architecture for author approval.
5. Only then pilot prose changes on a separate revision branch.
