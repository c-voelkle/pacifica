# Handoff: CR-040 Stages 3–4 (the Russian war)

**Written:** 28 October 2026, after PR #48 merged CR-040 Stages 1–2 into `main`.
**For:** a fresh session that writes and integrates Stages 3 and 4.
**Start with:** `python3 tools/session.py start --topic CR-040`, then read `AGENTS.md`, this note, and `book-agent/revision/CR-040.md` (sections "Decisions needed", "Second-round answers and proposals", R9, R10, K1, "Stage 3 — Outline", "Stage 4 — Outline").

## Where things stand

- **Canon now (merged):** Kiyoshi's 1905 Petropavlovsk victory (Russia keeps its battle fleets); Silas renounces December 1906; Kiyoshi's claim and renunciation, early and March 1907; the Act of Settlement of 1907; Julian accedes November 1907, swears in Manila December 1907; marries Chiyo November 1907; daughters first, Kahekili about 1916; the European tour from 1908; Bosnia 1909, Agadir 1911, the Balkan wars; the failure of July 1914 (§28); Ka Lōkahi's 1927 review admits Japan (§33). Section numbers were kept: the Act is in §26, Part VI opens at §27.
- **Canon still old (to replace):** §30's war years are mostly fine, but §31–§32 still tell the Siberian war for an *independent* Siberia, Kiyoshi's death "in Siberia in 1920", the Ob as a frontier, Harbin with the Siberian Republic, and the 1922 alliance with it. The trajectories and unresolved list repeat these.
- **All author decisions are made.** Nothing in Stages 3–4 waits on the author except approval of the written text.

## Decisions to embody (all APPROVED, 28 October 2026)

Quoted in full in CR-040; short form here.

| ID | Decision |
|---|---|
| Shape | A + D: the war Julian tried to prevent creates the revolution he then destroys; the coalition invades and the Bolshevik leaders are brought down. |
| R6 | Pacifica's railway advisers (in Petrograd since 1917 with the Russian-gauge locomotives, on the model of the Stevens commission) are taken hostage in the Red Terror. The Office of Public Measures publishes the Cheka's own lists beside the 5 September 1918 decree. |
| R7 | A coalition armoured train (the railway board's line extended west of the Urals behind the eastern armies' northern wing, which holds Perm) stops Lenin's train on the Vyatka line in spring 1920. |
| R8 | Lenin and Trotsky are arrested, tried in Russian courts for state crimes of which they were guilty, and executed in late 1920. Charges in CR-040 R8 (Penza hanging order; Trotsky's hostage orders; the Romanov murders); VERIFY each order's text and date. |
| R9 | The Romanovs: no rescue is planned or refused on the page; Julian's private reasons are never stated or hinted. The Ural Soviet kills the family on 16–17 July 1918 to prevent a rescue; Alapayevsk the next night; the Legion takes Yekaterinburg on 25 July. Pacifican investigators find the Koptyaki-road grave within weeks; the Office publishes the evidence; at the trial Trotsky names Lenin ("We decided it here"; "a live banner"); burial in the Peter and Paul Cathedral after Petrograd falls in 1920. |
| R10 | Julian goes in (1918) for an independent Siberia on the Pacifican model and publicly recognises Vologodsky's government; the Transbaikal Host's 1919 vote is cast for it. After the Red Terror he trades Siberian independence for Wrangel's army and Moscow. Victoria sees a betrayal of the Pacifican ideal and of the Siberians (the Union-and-California mirror; her own 1874–1876 guilt). The 1921 Altai partisans are Red remnants and Siberian regionalists refusing the compact; some of the gassed are Siberians Julian promised a country. Both sides arguable; no verdict. Her later arc (private silence, 1928 cure, 1932 Charter) unchanged. |
| R11 | Federal Russia under Wrangel's provisional leadership (Krivoshein premier); Siberia a federal land keeping the CR-031 territories; Transbaikalia and Kamchatka under Japanese protection; Ukraine independent with the western Donbas; Crimea autonomous in Russia (A §§6–10). |
| R12 / K1 | Stalin dies at Kronstadt. **K1's storyline text is approved verbatim** (CR-040, "Storyline text (APPROVED — CR-040 K1)"): letters across the ice, the boatswain's mate from the 1905 prize who learned Japanese at Matsuyama, the interpreter, the parley as diversion, the public offer, Stalin shoots, the Jigen-ryū cut, death on the quarterdeck in May 1920, the St Andrew's ensign. Kiyoshi commands the coalition's Baltic squadron (Japan's Mediterranean ships plus Pacifican cruisers, beside the British force); Vance keeps the Siberian line. |
| K1 knock-ons | Vance holds the Ob crossing in January 1920 (A's defence, with the last Legion transport) and is honoured by Czech and Slovak representatives; the Altai betrays his own act and Kiyoshi's. Japan enshrines Kiyoshi as a war god (Hirose precedent). Open: the boatswain's mate's name, Kiyoshi's sword, a death poem, who attends the Romanov burial. |
| F6 | Russia's surviving Baltic Fleet is in the Great War; larger 1917 mutinies. State it; invent no new battles. |
| F7 | The Twenty-One Demands passage already sends Victoria as Julian's envoy (integrated). |

## Stage 3: write and integrate

Storyline targets (current `main`):
- **§28 Pacific war.** Julian chooses war on Germany in August 1914 to keep Japan inside common action; Ballin's contracts become enemy contracts. (Proposed in CR-032e §6.)
- **§30.** Russia's Baltic Fleet in the war (F6). The January 1917 German offer to Washington also breaks Germany's 1909 undertaking (ledger `C-1908-UNION-NONASSISTANCE`: add `ended`); Thalassia publishes both texts. One sentence linking Julian's credibility as broker to 1908–1914, and stopping the credit in 1918 as the sanction he withheld in 1914. Keep the CR-025 credit text intact.
- **§31 opening.** 1917 revolutions on time; Brest-Litovsk; May 1918 railway intervention and the Legion (current text); **the 1918 promise to Siberia (R10)**; the Romanovs (R9); the Red Terror and hostages (R6); Julian's decision to go west and the approach to Wrangel (autumn 1918).

## Stage 4: write and integrate

- **§31 rest.** Wrangel's command (autumn 1919 council; Shatilov, Kutepov, Kappel, Yudenich); the trade of Siberian independence; Vance at the Ob (January 1920); Tula (February); the Oka line; Moscow (March 1920); Trotsky taken in the Oka retreat; Lenin taken on the Vyatka line; Petrograd falls by land (March–April); Kronstadt and Kiyoshi (May, K1 verbatim). Replace "The coalition fights for an independent Siberia…", the Omsk/Ob-frontier battle and "Fleet-General Kuroda Kiyoshi dies in Siberia in 1920".
- **§32.** Trials and executions (late 1920); the Romanov burial; the Altai (1921) with the mixed partisans; Victoria's confrontation naming Siberia; Harbin (1921) signed by Wrangel's government as the Moscow party; Siberia as a federal land. **Keep the approved CR-031 sentences true** by changing their subject only (the supersession table lists "The Siberian Republic extends to the Okhotsk coast…"). Nikolayevsk 1920 must be reassessed (A §11): keep the Kamchatka outcome without inventing an identical massacre if the course changes.
- **§32–§37, trajectories, unresolved items.** "Siberian Republic" becomes federal Russia (or Siberia within it) wherever it names the fourth alliance party; Kolyma stays Siberian (federal) production, foreign for Pacifican GDP; Vance's and Victoria's trajectories; Kiyoshi's trajectory ("He dies in Siberia in 1920").
- **Fact change deferred from Stage 1–2:** add to the CR-040 register entry and apply: `{"add_forbidden": {"pattern": "Kiyoshi dies in Siberia|killed in Siberia in 1920", "message": "Kiyoshi dies at Kronstadt in May 1920 (CR-040 K1)"}}`. Because CR-040 is already applied, add it as a further fact change and run `cr_facts.py apply CR-040` only if the tool accepts re-application; otherwise record it as a CR-040 Stage 4 amendment the way the tool expects (check `cr_facts.py` before acting). Then fix every hit (character bible line ~362 and ~549, registry `CT-KIYOSHI`, `CT-KURODA-II`, storyline §31 and the Kiyoshi trajectory).

## Supporting documents

- **Register:** amend the CR-040 entry (requirements for Stages 3–4; status to `approved_integrated` when done; `integrated_on`).
- **Characters:** check the registry before adding anyone. Likely new or updated: Wrangel, Krivoshein, Shatilov, Kutepov, Kappel, Denikin, Yudenich, Lenin, Trotsky, Stalin, Zimmermann, Ballin, Tisza, Franz Ferdinand, the boatswain's mate (unnamed), Vologodsky (exists?), Semenov (exists). Update Kiyoshi, Vance, Victoria, Julian. Run `validate_character_docs.py`.
- **Ledger:** Harbin's parties (SIB → RU or a Siberian federal subject), the 1922 alliance, Wrangel reconstruction credit, the Legion compact, the 1918 recognition of Siberia (and its end), Germany's breach of the 1909 undertaking. Quotes must be verbatim; status is the last label before the quote **in the same paragraph**.
- **historical_background.md:** Red Terror sources (decree; Cromie, 31 August 1918; Melgunov on the Cheka weekly no. 6), Romanovs (Yekaterinburg 25 July 1918; Koptyaki road; Trotsky's diary), Krasnaya Gorka (Stalin's 16 June 1919 telegram), Kronstadt ice (mid–late April), Jigen-ryū, Matsuyama POWs (JACAR), the 1921 Kronstadt resolution, West Siberian risings 1920–21 (VERIFY). Links are in CR-040 and CR-032e §13.
- **AGENTS.md:** the CR-040 paragraph says Stages 3–4 are not integrated; update it.
- **Finance:** no workbook change in this CR; note the modelling needs (CR-032e §12; A §12) for a separate task.

## Pitfalls learned in Stages 1–2

- Labels run to the next label **in the same paragraph**. Inserting a label mid-paragraph re-labels everything after it; restore the old label after your insertion.
- `lint_canon.py --only CR-040.md` reports the CR's own quotations of old text; that is expected. The full lint (`lint_canon.py`) must be clean.
- `sync_master_storyline.py --write` after any register edit, then `--check`.
- The ledger test (`python3 -m pytest -q commitments`) fails if `ledger.py check` has problems.
- Don't renumber sections.
- Run one fresh-context review on the integrated diff (storyline §28–§37 plus trajectories) before the PR, as AGENTS.md requires; give the reviewer only the diff, the affected canon and AGENTS.md.
- The author's working style: numbered decision lists; brief approvals; wants plausibility checked against sources; dislikes generic or over-the-top mechanics; prefers clever, character-true solutions.

## Done when

Stages 3–4 text is in `master_storyline.md` with `CR-040` coverage comments; all six checks are clean; a fresh review is applied; a PR is open and green; the session record's "Resume here" says what is left (if anything).
