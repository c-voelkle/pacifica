# Aumakua independent prose audit — master storyline §§4–8

Date: 26 October 2026. Repository: `outputs/compact-ontology-20261026/repo`. Observed HEAD: `1bd0729d35b012eff1bf5f519e4f2e22c25c915d`.

The clearest problems are the Council of State appearing four years before its stated creation and a secret explicitly known to at least seven people being described as known to only five. Both touch CR-028's **proposed** recognition/gold machinery; this review does not promote those mechanics into approved canon. Section 6 also drops the attribution that protects the uncertainty of Abigail's deathbed-marriage story. Two further points require clarification, rather than a finding that incompatible facts have been established.

No canon was changed. No previous assessment, ontology dataset, comparison output, issue register, or other agent's findings was consulted. This pass began with the governing instructions and a continuous reading of §§4–8, then traced selected counterparts in the raw prose, approval register and current character documents. No web or historical-plausibility work was performed. This is a bounded review, not a certification of the whole storyline.

## Authority and source locators

`M` means `book-agent/revision/master_storyline.md`; `CR` means `book-agent/revision/change_requests.json`; `CB` means `book-agent/revision/character_bible.md`; `REG` means `book-agent/revision/character_registry.json`. All paths are relative to the repository above. Line numbers are one-based in the inspected snapshot. JSON locators use the request ID and, when supplied, the exact JSON pointer. Raw-byte SHA-256 hashes, inspected ranges, partial outputs and exclusions are in `input-manifest.json`.

Authority followed `AGENTS.md`: current master and explicit approvals, with later decisions overriding superseded earlier provisions; current character bible and stable-ID registry for identity. Register/source-excerpt duplication is provenance, not independent corroboration. In particular, CR-027's November 1858 marriage supersedes older February 1857 entries; CR-028 retains local PROPOSED labels. No generated index or old character source was used to override this order.

## Issue ledger

### AUM-4-8-001 — Council of State receives a report before it exists

- **Classification:** Integration mismatch, with an explicit institutional chronology conflict. **Lifecycle:** Open, newly detected in this pass. **Consequence:** High for the legal sequence; evidence strong.
- **Evidence A:** M §5, L125 places the formal report after the party's spring 1848 return: “Elias reports the discovery formally, in confidence, to President Pico and the Council of State”. CB CT-PIO-PICO, L420 repeats the confidential 1848 report to that body; REG CT-PIO-PICO repeats it too.
- **Evidence B:** M §8, L183: “In 1852 the assembly reorganizes government at Monterey, creating a Council of State”. M §5, L137 also says the 1852 convention “establishes a Council of State”. CR-008, `/requests/7/requirements/16`: “The 1852 reorganization creates the Council of State”.
- **Aligned scope:** The Californian Council of State, not the later Confederal Council, is the body receiving Pico's report. The report is in spring 1848; the institution is created in 1852. The early report belongs to the proposed CR-028 sequence; the 1852 institutional creation is an established reorganization commitment.
- **Why it conflicts:** A formal report cannot be delivered to that institution four years before its creation under the stated chronology.
- **Compatible reading and uncertainty:** A pre-existing advisory council could later be reconstituted, but none is identified in the inspected passages and “creating” is repeated in the approval. Treating it as the same body without an explanation would invent institutional history. The master and character records agreeing on the 1848 wording does not solve this.
- **Smallest repair options:** Retain 1852 and change the 1848 recipient to an already established authority; or, if the author intends a predecessor body, explicitly establish it and distinguish it from the 1852 body. The recipient choice requires authorial resolution. Carry any authorized repair into CB/REG CT-PIO-PICO and the CR-028 source/current distinction; do not rewrite historical source excerpts as though they had never said this.
- **Prior issue mapping:** None consulted.

### AUM-4-8-002 — The gold secret has at least seven knowers, not five

- **Classification:** Contradiction within a PROPOSED narrative sequence, not a financial/model discrepancy. **Lifecycle:** Open, newly detected. **Consequence:** Medium for the diplomatic concealment plot; evidence strong.
- **Evidence A:** M §4, L117, during the December 1847 Querétaro bargain: “a find that only five people in the world know of”.
- **Evidence B:** M §5, L125 describes the October 1847 discoverers: “he and Caleb” travel “with an experienced Sonoran placer miner and a Miwok guide”, then “He tells only Pico, Castro and Alvarado”. It also explicitly has the guide keep the secret. CB L416 and L420 identify Castro and Pico as informed; CB L481 and L487 and REG CT-SONORAN-MINER/CT-MIWOK-GUIDE preserve the miner's and guide's participation and knowledge.
- **Aligned scope:** Knowledge of this particular October 1847 Mokelumne find by the December 1847 mission, not general knowledge of California gold or the 1842 Placerita discovery. Both passages carry CR-028's PROPOSED scope, reaffirmed in CR-028 `/requests/25/requirements/0`.
- **Check:** Four discoverers (Elias, Caleb, miner, guide) plus three separately informed leaders (Pico, Castro, Alvarado) gives **at least seven**. No overlap is supported by the roles or stable identities. This is a lower bound, not a claim that nobody else could have learned it.
- **Compatible reading and uncertainty:** “Five” might have meant a narrower political circle excluding the two local collaborators, but “in the world” rules out that restriction. No departure, death or loss of knowledge is stated. Excluding the miner and guide would also erase explicit agency without authorial support.
- **Smallest repair options:** Replace the exact count with a non-exhaustive formulation, or reconcile the count and disclosure sequence with the author. Changing “five” to “seven” fits the named minimum but would newly assert an exhaustive total; do not silently choose it.
- **Prior issue mapping:** None consulted.

### AUM-4-8-003 — Abigail's reported deathbed words become unqualified narrator fact

- **Classification:** Integration mismatch in narrative/knowledge status; not proof that the words were false. **Lifecycle:** Open, newly detected. **Consequence:** Medium because the uncertainty is expressly protected; evidence strong for the attribution seam.
- **Evidence A:** M §6, L145: “Her father dies in the cholera of 1850, telling her to marry him.”
- **Evidence B:** M §1, L73: “Only she heard it”; the story is “impossible for the Chronicler to verify”. CR-022 `/requests/20/requirements/0`: “the deathbed-marriage story remains unverifiable”. CR-002 `/requests/1/requirements/5` calls it “unverifiable early Chronicler testimony”. CB CT-PASTOR L399 says “Abigail alone reports” it; CB CT-PASTOR-DAUGHTER L406 leaves its reliability open. The corresponding stable-ID records preserve the same caveat.
- **Aligned scope:** The same pastor (CT-PASTOR) and Abigail (CT-PASTOR-DAUGHTER), the 1850 deathbed and the purported instruction to marry Elias. This does not concern whether Abigail and Elias later became lovers or whether Silas is their son; those are settled.
- **Why it matters:** The §6 synopsis sentence presents the instruction in the same unqualified voice as the death and subsequent relationship. It ceases to signal a claim whose source and reliability remain constrained by the approval.
- **Compatible reading and uncertainty:** The novel permits independent viewpoints to know more than the Chronicler (M L49; CB L13). If §6 is implicitly summarizing Abigail's own testimony, these facts can coexist. But the synopsis supplies no such attribution here, and the governing instruction specifically retains unverifiable testimony. Therefore this is an integration/stance problem, not a definitive contradiction between an actual utterance and the Chronicler's inability to verify it.
- **Smallest repair options:** Attribute the instruction to Abigail's later account in §6, retaining the 1850 death as fact. Alternatively, explicitly mark the intended focalization if that is the author's decision, while preserving the required uncertainty. Do not resolve whether the pastor really said it.
- **Prior issue mapping:** None consulted.

### AUM-4-8-004 — Authority for California's 1858 Edo treaty is unstated after foreign relations become common

- **Classification:** Missing bridge; clarification needed. **Lifecycle:** Open, newly detected. **Consequence:** Medium for the confederation's treaty authority; moderate evidence, no confirmed contradiction.
- **Evidence A:** M §7, L175: “In 1858, California and the Tokugawa government conclude the Treaty of Edo.” CR-005's requirements retain a definitive 1858 treaty; CB CT-II L523 confirms the year.
- **Evidence B:** M §8, L213 says the Confederation comes into force following November 1856 ratification and “The common institutions control defense, the navy, customs, currency and external relations.” CR-009 describes shared foreign relations; CR-021's A/D requirements retain the 1856 common machinery and member residual powers.
- **Aligned scope:** An external treaty concluded in 1858, after California becomes a member state of Pacifica. The earlier 1854–55 exchanges and Shimoda agreement are not caught by this question.
- **Missing connection:** The text gives external relations to common institutions but calls California the concluding party to the later treaty. It does not identify a confederal mandate or distinguish negotiating agents from treaty parties.
- **Compatible reading and uncertainty:** “California” may be geographical shorthand, or Californian negotiators may act for Pacifica. Neither reading is ruled out; no explicit sole/exclusive treaty power or unauthorized act is stated. A retained member treaty right is another possible choice, but cannot be invented here. This is not a finding that the treaty is invalid.
- **Smallest repair options:** Specify the treaty party and the capacity in which the Californian envoys act, consistent with the author's intended confederal authority. A one-clause clarification in §7 may suffice; review CR-005 wording if the party changes.
- **Prior issue mapping:** None consulted.

### AUM-4-8-005 — Assay-office opening sequence needs a distinction

- **Classification:** Suspected contradiction; clarification needed. **Lifecycle:** Open, newly detected. **Consequence:** Low to medium for the public-gold timetable; moderate evidence.
- **Evidence A:** M §4, L121 confirms gold publicly “only in October” of 1848, after the June exchange. M §5, L125 makes official confirmation conditional on “an emergency mining decree, an assay office and a royalty” being “in force”.
- **Evidence B:** M §5, L131: “A mint and assay office opens in San Francisco in 1850.”
- **Aligned scope:** The public machinery needed before October 1848 confirmation versus the 1850 opening of a mint/assay office. No currency or production calculation is involved.
- **Potential incompatibility:** If these refer to the same public assay institution, the precondition is unavailable until two years after the announcement it enables.
- **Compatible reading and uncertainty:** A temporary or differently located assay office in 1848 could precede the combined San Francisco mint/office in 1850. The indefinite “an” and the later specified location make that a plausible reading, but the text does not actually supply the distinction. Elias's private assaying at Carquinez (L125) does not establish a public office. Hence this remains suspected, not a confirmed chronology contradiction.
- **Smallest repair options:** Distinguish an earlier office and its relation to the 1850 mint, if intended; otherwise align the public-confirmation condition with the intended opening date. Do not invent the earlier institution as a fact to close the issue.
- **Prior issue mapping:** None consulted.

## Compatible readings and preserved open decisions

- **Marriage:** M §§6/8 L161/L221 agree on November 1858 after the 1856 confederation. Older CR-004/009 February 1857 wording is superseded by CR-027 A6 and the current character documents. It is not a current-prose contradiction.
- **Hawaiian signature versus confederal assent:** M §6 L155's Hawaiian public-document signature rule and §8 L215/L217's denial of an exclusive personal confederal veto concern different legal capacities. M L229 makes Washoe a coalition victory through Hawaiian governmental assent. No personal-veto contradiction was established.
- **Turret ship versus armor:** M L193's unfinished first fighting turret ship, M L233's “some armored warships” in April 1861 and M §10 L259's first operational Ericsson turret ship in 1862 do not logically identify all armored vessels as turret ships. The classes and capacities are unspecified, so the inspected text does not prove a contradiction. Detailed fleets and engineering remain outside this audit.
- **Gold secrecy and later publicity:** An October 1847 discovery and October 1848 confirmation are locally PROPOSED under CR-028, which narrows/supersedes earlier spring-1848 discovery planning. They are not the old four-year secret-mining premise. The arithmetic issue above concerns the specific secret's knowers.
- **Treaty duration:** Twelve-year 1848 commercial articles expiring in 1860 (M L119/L231) reconcile arithmetically. The 1861 Sausalito sealing is an approved later action, not proof that the earlier storehouse never existed.
- **Japanese contacts:** M §7's 1851 castaways, 1852–53 return of “some” castaways, 1858 treaty and 1860 visit agree with CR-005 and the inspected CT-MANJIRO/CT-HECO/CT-ABE/CT-NARIAKIRA/CT-II records. “Some” does not establish that Heco personally returned in 1852–53. Perry's altered mission remains explicitly OPEN (L169); the review does not turn that gap into an internal contradiction.
- **Denomination:** M L145 mentions a Methodist mission, while M L65/L886 and CB L397 retain open/proposed denomination. This is a local status seam worth preserving during drafting, but leading a mission does not strictly entail a denomination and no authorial choice is made here. No separate factual contradiction is claimed.
- **Kinship:** Marcus is called Caleb's relative (M L185), consistent with CB L122/L130's unresolved brother/older-kinsman options. Victoria's stable ID CT-KAIULANI does not create a second woman. No lineage was silently resolved.
- **Numbers and finance:** The £3m debt assumption remains MODEL/PROPOSED under CR-028. Private claims, public royalties and total national mineral production are distinguished in M L129–139/L201. No workbook, GDP, force-size or industrial-feasibility audit was performed.

## Coverage and limits

The continuous primary sweep covered **all of M §§4–8, L99–234**. Earlier setup and metadata were read at L1–98; later counterpart reading covered §10 L249–270 and the unresolved-decision list L883–910. Targeted whole-file searches in M and CB extended only the named issues; a hit elsewhere does not imply its surrounding section was audited.

The approval review read selected current requirements/open decisions for the early Japanese opening, gold/state finance, republic, confederation, emergency authority, industrial/character chronology, Abigail, Victoria and CR-028. CR-021's requirements were read to establish the constitutional framework; unrelated later-period contents were not audited against the plot. CB/REG coverage was selective and is enumerated in the manifest. A broad character search returned truncated output before narrower continuous reads; no completeness is inferred from it.

Uninspected material includes the full later storyline, original manuscripts and legacy profiles, full external CR attachments, historical background, war assumptions, financial workbook, generated indexes, ontology data and all prior assessments. Some standalone CR originals are unavailable according to AGENTS/CR; this review used the current register's clearly identified requirements/excerpts rather than reconstructing missing sources.

Checks actually performed: continuous prose reading, targeted exact-term searches, JSON field inspection, stable-ID comparison for selected people, the 4+3 knowledge count, 1848+12 treaty duration, Git HEAD lookup and raw-byte source hashing. No synchronization, character validator, schema/SHACL checker or financial recalculation ran. One read-only PowerShell pointer-extraction command failed to parse and was corrected; it produced no substantive evidence and no file changes.

All five ledger entries are **open**; “open” is their lifecycle, not a claim that all five are contradictions. There is no prior-issue reconciliation because prior findings were withheld. The report makes no overall consistency score.
