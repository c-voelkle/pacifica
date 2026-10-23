# Current revision — 23 October 2026

Read [the master storyline](master_storyline.md), supplied through CR-031 and preserved byte-for-byte. The [integration record](CR-031-integration.md), [character bible](character_bible.md), [identity registry](character_registry.json), [historical background](historical_background.md) and [financial review](../../finance/CR-031-review.md) describe this revision.

CR-028 narrows the recognition bargain while retaining proposed mechanics. CR-029 revises the Philippine/island sequence and three-crown settlement. CR-030 adds the railway operating schedule; CR-031 supersedes the all-Siberian northern destination. Missing standalone CRs have clearly marked excerpt records, not invented originals. The original CR-027 attachment and earlier CR sources remain unchanged.

The notes below describe earlier integration stages; current source precedence and financial references above govern where they differ.

---

# Pacifica revision workspace

**Updated:** 21 October 2026. The [master storyline](master_storyline.md) now follows [CR-027](CR-027.md): historical Victoria Kamāmalu, the legal Puʻuloa lease, illegal later ordinances, continuous Hawaiian crown and the Five. The supplied master also embodies CR-022 and CR-024–CR-026; [dependency excerpts](dependency_decisions_211026.md) preserve those decisions without reconstructing the missing standalone sources. CR-021 revision 9 remains authoritative elsewhere.

## Current documents

- [Master storyline](master_storyline.md) — primary narrative review copy, with **[PROPOSED]** and **[OPEN]** qualifications.
- [CR-027](CR-027.md) and [integration record](CR-027-integration.md) — approved storyline and Section E reconciliation; proposed details remain qualified.
- [CR-021 revision 9](CR-021.md) — approved constitutional record; [revision-9 report](../../outputs/CR-021-revision9/integration_report.md), author decisions, differences and verification.
- [CR-020](CR-020.md) — approved record; [integration report](../../outputs/CR-020/integration_report.md), final precedence decisions, review differences and verification.
- [CR-018](CR-018.md) and [CR-019](CR-019.md) — working records with source labels preserved. CR-018 incorporates the never-separately-merged CR-017.
- [Sequential integration report](../../outputs/CR-018-019/integration_report.md) — coverage, continuity decisions, remaining questions and verification.
- [CR-016](CR-016.md), [CR-015](CR-015.md) and [Power Timeline](power_timeline_1865_1900.md) — earlier directions with current later-precedence notes.
- [Character bible](character_bible.md) and [registry](character_registry.json) — 132 stable identities, including six retired provenance/alias records. CT-KAIULANI holds Victoria’s historical identity; the former separate CT-VICTORIA-KAMAMALU is retired duplicate provenance. The historical princess born 1875 has her own ID. Kiyoshi is Fleet-General Kuroda; the lost Kalanimoku and Kahekili / Ikazuchi are distinct; the heir’s stable ID is retained. All 250 original profiles and their ID mappings remain intact; crosswalk notes now explain Victoria’s identity.
- [Change register](change_requests.json) and [approval index](approved_change_index.md) — approved directions and open mechanics; the index is generated separately from the narrative.
- [Historical background](historical_background.md) — historical evidence, source-supplied comparisons and explicit fictional divergences.
- [Feasibility scope](war_base_assumptions.md) — numerical and operational work remaining, including the new war, coalition and creditor order.
- [Part I plan](planning/part_i_plan.md) and [rise-to-power companion](planning/elias_rise_to_power_1844_1861.md) — current derived companions; the original rise-to-power proposal is preserved in [the source archive](sources/rise_to_power.md).
- [Confederate values](confederate_value_schema.md), [CR-013 revision 5](../../outputs/CR-013/CR-013-consolidated.md), [legacy crosswalk](legacy_character_crosswalk.json) and [secondary cast](legacy_secondary_cast.md) — earlier characterization, questions and provenance.
- **Current financial planning:** the author-supplied [workbook](../../finance/Pacifica_financial_model_1846-1932.xlsx) and [Pacifica Ledger](../../finance/Pacifica-Ledger.md), published with explicit authorization on 20 October 2026, supersede earlier financial models. See [reference notes](../../finance/README.md) for the ledger’s revision-8 scope and the current narrative’s revision-9 authority. Reported results remain MODEL estimates.
- [CR-018/CR-019 financial assessment through 1932](../../outputs/pacifica-finances-1932/financial_plausibility.md) — preserved dated workbooks and bank/transport diagnostics, superseded as the working model reference. Their unresolved evidence is retained in the audit.
- [CR-015/CR-016 financial reconciliation](../../outputs/pacifica-finances-20261018/financial_reconciliation.md) — preserved dated comparison, superseded by the 1932 financial extension for the later arc.

## Authority and open decisions

The current user authorizes publication of the supplied updated storyline and CR-027’s Section E updates as a new PR. CR-027 supersedes the fictional cousin, 1857 wedding, massacre, abeyance and 1874 judgment: Victoria marries in November 1858, reigns from 1872, leases Puʻuloa lawfully in 1874 and accepts illegal encroachments in 1874–1876; the judgment is 1876. The 1914 Act joins crowns and restores legislature. Earlier CR source files are preserved. CR-021’s prior approval after CR-020 remains operative elsewhere. Revision 9 applies the direct author corrections to the previously approved framework and all seventeen OPEN-021 decisions. Final K decisions and revision-8 protocol override older labels. Noe’s identity and 1886 hānai bargain are settled, while culpability for her 1888 death is deliberately unproved. Kahekili / Ikazuchi is the heir, future Kamehameha VII. Unrelated Vance/1905 peace and earlier OPEN mechanics remain qualified. Numerical results stay MODEL.

The Western peace framework is 1865, Senate ratification 1867. Russia retains the northern coast until 1921; CR-021 revision 9 assigns Kamchatka, Okhotsk coast and Nikolayevsk to the Siberian Republic; any Japanese access is treaty-only. The eastern through route is completed under Japanese control through Chinese Manchuria. Combined allied fleet limits in 1919 precede the formal 1927 ministries. These distinctions govern broad or inconsistent source wording.

Thalassia stands on Kāneʻohe Bay, windward Oʻahu; Waimanu is the protected stream. The Gulf’s five general measures and two parity tests must hold for twenty-five years, so no admission occurs in the novel.

Sovereignty, leases, revenue administration, union and association stay distinct. Japan retains domestic institutions; China retains the Manchurian railway and Formosan sovereignty; the Philippines are a Crown dependency; Korea is an independent guaranteed state; the Gulf and Union remain associated sovereigns. Numerical targets and engineering capacity remain unvalidated where recorded in the audit scope.

## Maintaining the revision

1. Update relevant plot paragraphs and their later consequences, keeping the narrative affirmative and continuous.
2. Preserve decision labels and stable identities; record later precedence without erasing original attachments.
3. Update character prose and registry copies together; retain retired IDs and legacy mappings.
4. Regenerate the approval index with `sync_master_storyline.py --write`, then run its `--check` and `validate_character_docs.py`. These verify synchronization, not literary quality or historical feasibility.
5. Keep synced sources, original character JSON, production manuscripts and source archives unchanged. Original supplied CR-021 revision 8 is preserved in outputs/CR-021. Revision 9 follows the direct author decisions; the original revision-8 attachment is included in the published source package; local working backups are retained separately. CR-020’s original and previous backup remain unchanged. Earlier original attachments, backups and the intermediate CR-018 master remain unchanged. The author-supplied current financial workbook and ledger are published verbatim under finance/; earlier local workbooks are superseded.


The Concord’s annual Council is always at Hayama: Hirohito hosts, Julian convenes and presides, and Prince Chichibu represents Japan at Thalassia, with Pacifican education, honors and an outdoorsman reputation. Julian is never styled President. The 1927 illegal provisional application receives consent and indemnity in 1928; the 1932 renewal runs only to 1937. President-elect Young accepts association after his November 1932 election; Dawes remains incumbent during the rescue and conference.


Tongue votes are expressly uncapped. Noe’s death remains ambiguous. Foreign Affairs and Finance normally remain Pacifican; the law requires at least one Japanese common minister, conventionally Navy. The crowns agree the renewal at Hayama and ministers sign/exchange instruments at Thalassia. The updated source export and complete revision-9 package are in outputs/CR-021-revision9.

The [CR-027 financial handoff](../../finance/CR-027-handoff.md) records common customs, lease rent and Crown/estate classification for Sol. No lease amount is invented and no financial file is recalculated in this revision.

