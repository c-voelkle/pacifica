# Fresh-Context Canon & Literary Review — `CR-090.md` (Revision 2)

**Reviewed:** 27 November 2026 (independent fresh-context reviewer; candidate text `CR-090.md` revision 2 at commit `a8dfa42`, checked against `AGENTS.md`, `master_storyline.md`, `CR-085.md`, `CR-088.md`, `CR-083-087-open-questions.md`, `canon_facts.toml`, `character_registry.json`, and `commitments/data/ledger.toml`).
**Author disposition (27 November 2026, 16:39):** `"I approve D9, the suggestion for B4 and the remaining sharpenings for revision 3. Save the review file alongside it on the branch."` All findings below are worked into `CR-090.md` revision 3.

## Verdict
**Ready with revisions.**

`CR-090` has a genuinely strong conceptual spine: it respects every protected intent rule, honors the author's strict Victoria/Kaʻiulani boundary on women's suffrage, avoids registry bloat, introduces zero `CT-*` ID collisions, and weaves `CR-077`–`CR-079` technology into Japanese domestic politics in ways that feel organic to Pacifica's world (especially Emperor Shōwa's sacred radio silence, the Restorationists' "calculating-machine state" critique, and Yokosuka's sealed magnetic-wire courtroom rule).

However, four **blocking** issues must be fixed before adoption/integration — an R1 approval-label contradiction, an unreconciled legal/canon clash at Yokosuka (plus a mismatch on who assassinated Inukai), broken `## Fact changes` regex patterns, and two OTL-copying chronology gaps (1918 Hara's accession and Wakatsuki's April 1931 start date) — alongside seven **substantive** plausibility and anti-brochure tightenings so Japan's 1871–1932 arc carries real scars, losers, and authentically Japanese political friction rather than reading as "Pacifica cured Japan."

---

## Blocking Findings (`B1`–`B4`)

### `B1` — R1 Approval-Label Contradiction and Scope Inflation (`CR-090.md` L5, L37, L56, L68–69, L79–80, L125, L264–279)
- **Direct contradiction on D-9 (*Teishinshō* broadcast model):** At L37 the author asked *"For 1: what do you think works best for the story?"* — a question, not an approval. D-9 (L274) properly labels the *Teishinshō* model `PROPOSED (recommended model)`, yet **L5 (`Approved so far`) falsely lists `"recommended Teishinshō public-utility broadcast model"` as approved on 27 Nov 2026 at 16:17.** That violates `docs/authority-and-scope.md` R1/R2.
- **Unlabelled/bundled `PROPOSED` narrative settlements under `APPROVED` tech headings:**
  - **L68–69 (`A2.2`, closing `CR-085` Unresolved #41 on 1918 rice prices / `CR-083-087-open-questions.md` #21):** Tagged `(APPROVED tech upgrade)` with **no row in `## Decisions`**, even though closing an open item previously recommended left unsaid requires an explicit `PROPOSED` decision row.
  - **L79–80 (`A2.5`, 1925 Universal Manhood Suffrage + narrower Public Order Statute):** Tagged `(APPROVED tech upgrade)` with no `PROPOSED` label on the 1925 legislative settlement itself and no dedicated decision row.
  - **L56 (`A1` bullet 4, Army post-1894 politics):** Tagged `(fulfills CR-088 hand-off 3, APPROVED tech upgrade)` without keeping its underlying narrative particulars explicitly `PROPOSED`.
  - **L125 (`A5` item 4):** Places specific sentences (*"uncommuted capital and life sentences for Inukai's direct murderers and long penal servitude with cashiering for Kashiwagi and the carrier mutineers"*) under `APPROVED stern sentences`, whereas D-3 (`3a`) approved `"stern sentences"` in direction; the exact capital/life/cashiering breakdown should be labelled `PROPOSED`.
  - **L55, L74–77, L84–95 (`A1` no-Hibiya, `A2.4` party coalitions, `A3` four phases):** Missing explicit `PROPOSED` rows in `## Decisions`.

### `B2` — Unreconciled Legal Clash at Yokosuka (`L1822` & `L1654`) and Mismatch on Inukai's Assassins (`CR-090.md` L120–125, L148)
- **Clash with `CR-085` (`master_storyline.md` L1822) and the Common Tribunal (`L1654`):**
  - `master_storyline.md` L1822 states (`PROPOSED — CR-085`): *"Japan has had no navy apart from the Concord's since 1927, and two parts of the common Navy stand against the officers: the stations and yards in Japan, which Japanese officers command, and the western squadron's Japanese units."*
  - Yet `CR-090` L122 states that a **"Yokosuka Naval District Court-Martial (Japanese naval law)"** tries Commander Kashiwagi and the Japanese Common Navy officers **"under the Imperial Japanese Naval Penal Code"** with zero Thalassian appellate authority — without explaining how an Imperial Japanese Naval Penal Code and domestic naval district court-martial operate over Common Navy officers when Japan has no separate navy, and without mentioning **`L1654`'s Common Tribunal** (*"A Common Tribunal of three judges from each side, with alternating chair, decides competences"*).
  - *Required fix:* Add the legal bridge cleanly: under the 1927 Concord's domestic-law firewall (`L1654`) and the reserved-squadron / home-station regime still in force in May 1932 (until consolidated on 1 August 1932), Japanese officers in the western squadron and Japanese home stations retain Japanese imperial commissions and remain subject to Japan's domestic Naval Penal Code (*Kaigun Keihō*) for offences on Japanese territory/waters; both crowns decline to refer jurisdiction to the Common Tribunal (accepting that Concord institutions hold no domestic criminal court in Japan).
- **Factual/canon mismatch on who assassinated Inukai (`CR-090` L122–123 vs. `CR-085` & *Hist.*):**
  - `CR-090` L122 assigns ONLY *"Commander Kashiwagi and the Japanese Common Navy officers involved in the carrier plot"* to Yokosuka, while L123 assigns **"Inukai's direct assassins and the army/civilian conspirators"** to the *"Tokyo District Court & First Division Army Court-Martial."*
  - Historically (*Hist.*), **Inukai's direct assassins were young naval officers** (tried at the **Yokosuka Naval District Court-Martial**!), accompanied by Army cadets (tried by the **First Division Army Court-Martial**) and civilian rightists (tried by the **Tokyo District Court**). `CR-085` (line 142 of `CR-085.md`) deliberately tracks this (*"an army whose cadets stood beside the men who shot a premier"*), and `master_storyline.md` L1822 makes King's sharpest objection *"naval officers were among the men of 15 May, and the seat is being given to their service."*
  - *Required fix:* Assign all implicated naval officers (both Kashiwagi's carrier mutineers and the naval officers in the raid on Inukai's residence) to Yokosuka, the Army officers/cadets to the First Division Army Court-Martial, and civilian Restorationists to the Tokyo District Court.

### `B3` — Broken `## Fact changes` Regex Patterns (`CR-090.md` L237–256)
- **`jp-municipal-womens-suffrage` Pattern 1 (L242):** Fails to match `CR-090`'s own prose at L112 (`passes the compromise Municipal and Prefectural Women's Suffrage Act in March 1931`) because it lacks an optional month before `(?P<year>...)`.
- **`yokosuka-may-15-trials` Pattern (L253):** Matches zero sentences anywhere in `CR-090.md`. Add optional season/month qualifiers and a year-before-noun alternate pattern so `lint_canon.py` actually guards the event.

### `B4` — OTL-Copying Chronology Gaps: 1918 Cabinet Transition & Wakatsuki's April 1931 Start (`CR-090.md` L69, L76, L133)
- **1918 Cabinet Paradox (L69):** If *"no cabinet falls"* in summer 1918, supply why Field Marshal Terauchi steps down in autumn 1918 for Hara Takashi's premiership: Terauchi resigns from failing health (*Hist.*: died Nov 1919) and a Diet budget deadlock over the five-division Siberian mobilization (`L1448`), letting Saionji recommend Hara's Seiyūkai majority peacefully.
- **Wakatsuki's `"April–December 1931"` Premiership & Omission of Tanaka's Canonical 1927–29 Cabinet (L76, L133):**
  - In OTL, Wakatsuki returned in *April 1931* only because Prime Minister Hamaguchi Osachi was shot over the **1930 London Naval Treaty** — a treaty that **does not exist in canon** (`CR-088` A2.3 item 5).
  - `A2.4` also omitted **Tanaka Giichi's canonical 1927–29 Seiyūkai cabinet** (`L1587`, falls July 1929 over Zhang Zuolin's assassins).
  - *Required fix:* Fold Tanaka's canonical 1927–29 cabinet (`L1587`) into `A2.4`, and seat **Wakatsuki Reijirō** as Minseitō Prime Minister from **Tanaka's July 1929 fall through December 1931** (covering both March 1931 municipal suffrage and autumn 1931 Manchuria).

---

## Substantive Findings (`S1`–`S7`)

- **`S1` (1918 rice prices):** Account for `CR-041`'s five-division Siberian deployment (`L1448`) and wartime inflation — keep real urban/dock protests and merchant/landlord anger over rail caps, while rice sufficiency + tabulated logistics prevent nationwide insurrection.
- **`S2` (1923 Kantō radio physics & grit):** Specify **battery-powered receivers and Jensen PA loudspeakers at ward offices, railway depots, and relief ships in Tokyo Bay** after the grid collapses on 1 September 1923; contrast with OTL's **Funabashi naval wireless rumour broadcast** driven by post-1910 colonial paranoia over annexed Korea; keep real 24–48 hr terror, martial-law friction, and public anger at Tokyo authorities for rejecting Imamura Akitsune's 1906 warning (`L1254`, `L1593`).
- **`S3` (1925 Public Order / *Tokkō* precision):** Acknowledge Japan's surviving Meiji/Taishō police apparatus (1900 Police Law, 1911 *Tokkō* after the anarchist High Treason Incident). Having no USSR prevents OTL's **1928 death-penalty escalation and sweeping *tenkō* purges** of moderate socialists (`CT-ABE-ISOO`), legal unions, and liberal law faculties, while the Home Ministry fights a regulatory war over shortwave sets and newsreels.
- **`S4` (March 1931 Peers suffrage realism):** Credit Minseitō Home Minister **Adachi Kenzō**; note the spousal-consent clause was already the cabinet's compromise retained to scrape a narrow Peers vote as a *conservative local anti-corruption valve* meant to head off national suffrage; anchor `"autumn 1931"` to Japan's historical **September–October 1931 prefectural assembly elections**; show feminist frustration over spousal consent and traditionalist backlash ("Honolulu rot").
- **`S5` (*Teishinshō* broadcast model — Reviewer endorses `D-9`):** Add major dailies' resentment of *Teishinshō*'s airwave monopoly, and distinguish **1916–19 coastal/wire-desk reception** of Honolulu broadcasts from **~1920+ household transpacific shortwave** (`L1679`).
- **`S6` (Missing costs & counter-arguments):** Frame Army modernizers as **cold-eyed nationalists** eyeing harder industrial terms at the 1937 review; keep tens of thousands of clemency petitions and `"star-chamber"` attacks against Yokosuka's barred microphones; align 1894–99 treaty revision wording with `CR-088` `A1.3` (`L749`, mixed residence still argued); cross-link `CR-088` G29 (`L1194`) in State Shinto.
- **`S7` (`CR-088` hand-offs & `CR-083-087-open-questions.md` #16/#21):** All four `CR-088` hand-offs and both Japan-domestic items in #16/#21 are cleanly covered once `B1`, `B2`, `B4`, `S1`, `S6` are applied.

---

## Minor Findings (`M1`–`M9`) & Set-Piece Polish

- `M1`: Cite `L1199` (not `L1201`) for household valve receivers (~1914); clarify `L1201`'s 1916 Honolulu Japanese broadcasts are the air school.
- `M2`: Replace `"American card"` with `"San Francisco card"` (`L986`).
- `M3`: Cite `L1696` beside `L1679` on the Emperor's household radiotelephone.
- `M4`: Briefly distinguish Japan's domestic statutes/trials from `C-1899-HOKKAIDO-AINU` in `## E` (no new ledger entries required).
- `M5`: Move Set Piece 4 to **Okitsu in early June 1932**, hearing the *Teishinshō* broadcast of the **1 June Diet-opening Imperial Rescript**, matching Saionji's `L1816` movements.
- `M6`: Add specific URLs/references under `## Sources`.
- `M7`: Add a non-storyline integration file checklist under `## B` (`character_registry.json`, `character_bible.md`, `canon_facts.toml`, `change_requests.json`, `historical_background.md`, `AGENTS.md` `406 -> 408`).
- `M8`: Split `§33` (1925–27) from `§34`–`§35` (March 1931 suffrage and 1931 "calculating-machine" backlash) in `## B`.
- `M9`: Fold background figure **Adachi Kenzō** into `A4.3` prose (`S4`).
- **Set Pieces:** Sharpen Set Piece 2 (*First Ballots in Kanda*: spousal-consent seal + real political disagreement between women voters) and Set Piece 3 (*The Quiet Wire at Yokosuka*: Kashiwagi realizing his grand speech disappears into a humming spool of sealed magnetic wire watched from the gallery).
