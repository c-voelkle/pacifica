---
session: 20261029-integrate-cr040-s34-cr041
started: 2026-10-29
updated: 2026-10-29
mode: adopt
status: complete
baseline:
  commit: 1d4ae02
  files:
    book-agent/revision/master_storyline.md: sha256:525dbd45a00d6b041d181ab0b830196dd14b62be75e4eadf9ef1bebee4af0c07
    book-agent/revision/change_requests.json: sha256:de8e1047512ba871525f98850cc6240059b22d793ef8d99efba74372b20281be
independence: separate-agents (integration by one agent; the fresh-context review by a second agent given only the candidate §31–§32, the neighbouring canon §28–§30 and §33–§37, and AGENTS.md)
---

# Integrate CR-040 Stages 3–4 and CR-041 into the master storyline together

## Brief

- **Desired outcome:** the Russian war of 1918–1922 written into `master_storyline.md` as a record of the alternate-historical facts, with the ledger, facts file, character files and background updated, so that a new beats.json can later be generated from it.
- **Objective:** the approved sequence (CR-040 R6–R11, K1; CR-041 S1–S9, N1–N16) embodied as what happens, with labels preserved.
- **Authorization:** author, 29 October 2026: "I would say go ahead and integrate. We leave the Ukraine and other open sectors for a follow-up CR." Also: "the master_storyline file is not actually the 'book' but only an outline … a meticulous record of the alternate-historical facts and not as the actual novel."
- **Sources of history:** `CR-040.md` (R6–R13, K1), the Stage 3–4 draft on `review/cr040-stage3-4`, `CR-041.md`, the session record `20261029-cr041-plan-c`.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-10-29 | adopt | Author: "go ahead and integrate" |

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | Integrate CR-040 Stages 3–4 and CR-041 together now | author 2026-10-29 | current |
| D2 | decision | Ukraine, Bessarabia and the Turkish frontier go to a follow-up CR | author 2026-10-29 | current |
| D3 | decision | The master storyline is the factual outline for a future beats.json, not the novel | author 2026-10-29 | current (recorded in AGENTS.md) |
| Q1 | open choice | Which Ukraine, the Black Sea coast, Bessarabia, Kars–Ardahan–Batum | carried from CR-041 | open |
| Q3 | open choice | Siberia "from the Ob to Lake Baikal" (approved R11/CR-031 wording) excludes Omsk and sits beside the Okhotsk extent; reviewer suggests "from the Urals to Lake Baikal" | H1 finding F14 | open |
| Q2 | open choice | The hostages' names; the Kotelnich commander; Lenin's capture day; Kiyoshi's sword and poem; who attends the Romanov burial; monarchy or republic | carried from CR-040/041 | open |

## Handoffs

| ID | To | Task | Inputs (paths and IDs) | Withheld for independence | Output | Status |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | Fresh reviewer (separate agent) | Consistency, literary and plausibility review of §31–§32 | candidate §31–§32; canon §28–§30 and §33–§37; AGENTS.md | CR files, drafts, the integrator's notes | findings F1–Fn below | see Review judgments |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `tools/session.py start --topic integrate` | pass |
| X2 | `cr_facts.py apply CR-041` (4 forbidden patterns, incl. CR-040's deferred Kiyoshi pattern) | applied; all listed passages revised |
| X3 | `lint_canon.py` | clean, 4 files |
| X4 | `cr_facts.py check` | pass (13 approved fact changes) |
| X5 | `sync_master_storyline.py --write` / `--check` | pass |
| X6 | `validate_character_docs.py` | pass (171 dossiers: 3 updated, 9 new historical persons) |
| X7 | `commitments/ledger.py check` | 174 commitments, 0 problems (3 new: C-1918-SIB-TREATY, C-1918-EMBA, C-1919-WRANGEL-VOTE; 8 revised) |
| X8 | revision and commitments unit tests | OK |
| X9 | `lint_canon.py --only` on the candidate before review | clean |

## Review judgments

Fresh-context review (H1, separate agent, candidate §31–§32 + neighbouring canon + AGENTS.md only) returned 31 findings; verdict "not yet fit" with three blockers. Disposition:

| ID | Judgment | Finding | Location | Disposition |
| --- | --- | --- | --- | --- |
| F1 | consistency | *Izumo* "a Tsushima veteran" — no Tsushima in this timeline | §31 Baltic squadron | repaired: "a veteran of the 1905 war" |
| F2 | consistency | Kotlas–Glazov supply runs through Red-held Vyatka | §31 Volga battle | repaired: sentence deleted |
| F3 | consistency | "Kolchak's governor" at Petropavlovsk, though Kolchak never rules | §32 Kamchatka | repaired: "the Directory's governor" |
| F4 | consistency | treaty signed in late July adopts a draft finished 3 August | §31 treaty | repaired: signed Omsk 4 August, Samara 6 August 1918; propagated to CR-041.md, register, AGENTS.md, ledger, characters, background |
| F5 | consistency | Japan acting "at Urajio at Russian request" — Urajio is Japanese since 1899 | §31 no declaration | repaired: clause dropped |
| F6 | consistency | Japanese western limit contradicted (Legion relief, wounded on the bridge, Altai prisoners) | §31–§32 | repaired: Japanese line-guard battalions relieve the Legion as far as Omsk and the Altai branch; field divisions stay east of the Yenisei; "Japanese wounded" removed from the bridge; Altai prisoners are a line-guard battalion |
| F7 | consistency | who takes Yekaterinburg; Chelyabinsk taken twice | §31 | repaired: Legion and corps together; corps "relieves" Chelyabinsk |
| F8 | consistency | "only coalition force west of the Yenisei" vs Siberians, Alash, Cossacks | §31 order of battle | repaired: "only force from outside Russia, the Legion apart" |
| F9 | literary | Kiyoshi's Siberian command never established; Vance's inheritance undefined | §31 command | repaired: Kiyoshi named commander-in-chief at Irkutsk; gives up the command for the Baltic; Vance holds the line, then the senior command; bible and registry updated |
| F10 | consistency | Kotelnich bridge "held since January 1919" beyond Red Vyatka; removes Lenin's motive | §31 Lenin | repaired: January raid cuts and withdraws; *Māui* retakes the bridge days before Lenin's train |
| F11 | plausibility | barges and Kara Sea convoy "through the winter" | §31 | repaired: autumn while the barges run, and the winter after; CR-030 sentence "prepared the autumn before" |
| F12 | literary | Victoria's California charge tripled (1918, 1919, 1921) | §31–§32 | repaired: 1918 trimmed to the warning about his word; 1919 private remark and 1921 charge kept |
| F13 | consistency | "standing front on the Ob" — no Ob front exists | §32 alliance | repaired: "A standing front in Siberia" |
| F14 | consistency | "from the Ob to Lake Baikal" excludes Omsk and sits beside the Okhotsk extent | §32 Harbin | retained: approved CR-040 R11 / CR-031 wording; raised to the author as Q3 |
| F15 | edit-memo | four memo sentences in the record | §31–§32 | repaired: (a) deleted, (b) rewritten, (c) trimmed; (d) retained because its PROPOSED label scopes the ledger quotes that follow |
| F16 | consistency | 1921 renunciation vs her 1924–28 activity | §32 | repaired: "remaining executive role … keeping the private standing she uses in 1924 and 1928" |
| F17 | consistency | Julian at Irkutsk undated against §29–§30 | §31 command | repaired: summer 1918 at Irkutsk; from the autumn Thalassia and the cables |
| F18 | consistency | "Kuroda's men" in the Altai 1921 | §32 | repaired: "Japanese soldiers" |
| F19 | literary | Soviet acceptance of Pacifican railway help unmotivated after the gold seizure | §31 spring 1918 | repaired: one clause (famine, Allied missions doing the same) |
| F20 | nit | Beijing/Peking | §31 | repaired: Peking |
| F21 | plausibility | Hirose/Port Arthur comparison in a timeline without Port Arthur | §31 Kronstadt | repaired: comparison dropped |
| F22 | literary | Wrangel's council has no actor; Denikin's fate | §31 | repaired: convened by the Directory on Boldyrev's proposal, paymaster present; Denikin keeps the Volunteer Army's name and the Caucasus front |
| F23 | plausibility | Emba lies in Uralsk, outside the three treaty oblasts | §31 | repaired: Western Alash Orda at Dzhambeity adheres and signs the Emba concession |
| F24 | nit | five "our history" comparisons | §30–§32 | partly repaired: Omsk one dropped; the rest tolerated |
| F25 | plausibility | Pepelyaev's corps larger than the October army | §31 Perm | repaired: "the bulk of the Siberian Army and now some 45,000" |
| F26 | plausibility | Frunze commanding the Eastern Front in May 1919 | §31 Volga | repaired: "under Kamenev and Frunze" |
| F27 | nit | Zelenodolsk is the 1932 name | §31 | repaired: "Zelenodolsk, then Zelyony Dol" |
| F28 | literary | Vance's character paragraph placed after the war | §31 end | retained (existing canon placement) |
| F29 | nit | conditional-money beat doubled | §31 Wrangel | retained (second sentence is a ledger quote) |
| F30 | literary | "Out of fairness"; Kotelnich commander's refusal cryptic | §32, §31 | partly repaired: Kotelnich refusal stated ("handed to Russians, not treated with"); "Out of fairness" is existing CR-031 canon, retained |
| F31 | literary | Vance at the bridge without a reason | §31 | repaired: "having come forward from the depots to clear his own trains" |

Contract judgment: no power dimension weakened; the Alash and Emba articles and Kiyoshi's command add explanation, not new power. Consistency: 28 of 31 repaired, 3 retained with reasons. Literary: causality for the prose-writer improved at the council, the bridge, Kotelnich and the command chain.

## Round log and stop reason

| Round | Date | What changed | Stop reason |
| --- | --- | --- | --- |
| 1 | 2026-10-29 | §31 rewritten and §32 revised under CR-040 Stages 3–4 + CR-041; §25, §28, §30, §33, §35, §37, trajectories and unresolved item 23 from the review branch; register, facts, ledger, characters, background, AGENTS.md | awaiting H1 |
| 2 | 2026-10-29 | H1's 31 findings applied (28 repaired, 3 retained); treaty signing moved to 4–6 August 1918; Japanese line-guard battalions; Kiyoshi's command chain | usable; merged |

## Resume here

Integration complete and merged. Next: the follow-up CR for Ukraine and the southern sectors (Q1); then the OPEN character details (Q2). Stale: everything in the Stage 3–4 draft that CR-041 superseded (Ob battle, Omsk's fall, unilateral recognition, torn treaty).
