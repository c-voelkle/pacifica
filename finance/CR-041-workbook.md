# Workbook revision, 30 October 2026: the Russian war re-planned (CR-040 Stages 3–4 and CR-041)

SHA-256 of the current workbook: `c3c975b81a487505504258b567c8bf192ddc48783aa02af6e2383df52575b6b9`. It is the 28 October CR-034 workbook with the changes below. They are made by [`build/cr041_russian_war.py`](build/cr041_russian_war.py) with [`build/paths_c_rates_cr041.csv`](build/paths_c_rates_cr041.csv), then recalculated in LibreOffice: 51,317 formulas, no errors. Before editing, the unchanged workbook was recalculated and reproduced all 65,702 numeric cells exactly, so the comparisons below are like for like. All amounts are MODEL estimates, and every new number is a lever or input with its source in a cell comment.

The model follows the storyline as integrated on `main` (PR #50). Decisions recorded only in the Anglo-Pacifican planning note are not in it (see "Not in the model" below).

## The answer: what Pacifica's finances look like

**The Russian war is affordable many times over. The constraints are the railway and the Senate, not the Treasury.**

| Story case, $m | 1918 | 1919 | 1920 | 1921 | 1922 | 1918–22 |
|---|---|---|---|---|---|---|
| Spending on the line (Siberia sheet) | 171 | 418 | 245 | 125 | 46 | 1,005 |
| Other war operations (Black Sea escorts, White Sea, Baltic squadron) | 0 | 16 | 30 | 0 | 0 | 47 |
| Cossack pay in gold | 3 | 5 | 3 | 0 | 0 | 12 |
| Kazan gold paid back for Pacifican munitions | 0 | −121 | −80 | 0 | 0 | −201 |
| **Net budget cost** | 174 | 319 | 198 | 125 | 46 | **862** |
| Lending to Russian governments (Directory, convoys, Yudenich, reconstruction) | 30 | 138 | 240 | 80 | 80 | 568, then 160 in 1923–24 |
| *For scale: GDP* | 38,055 | 43,649 | 51,270 | 41,915 | 43,385 | 218,274 |
| *Receipts* | 4,435 | 5,204 | 6,028 | 4,375 | 4,544 | 24,587 |
| *Budget surplus* | 1,140 | 1,275 | 1,724 | 889 | 1,037 | 6,066 |

- **At its peak in 1919 the war costs 1% of GDP and 8% of receipts.** The Treasury never borrows for it. The budget runs a surplus of $0.9–1.7bn in every war year.
- **It is paid for out of investment.** In 1918–1924 the Development Fund invests $4.63bn instead of $4.92bn. The lending to Russia is cash the fund would otherwise have put into Pacifica. Development stock is about $350m lower in 1920–22 and back above the old path by 1929, as Russia repays and the guarantee costs less.
- **One campaign is cheaper than a front.** Spending on the line in 1918–32 is $1.10bn, against $1.37bn under CR-030's Ob front. Most of the saving is the guarantee of the federal compact, about $10m a year after 1922, against about $42m for the standing front. The storyline's "one campaign that ends the regime costs less than a front held against it for ever **[MODEL]**" holds on these numbers.
- **Pacifica comes out a larger creditor of Russia.** Public claims in the Europe group are $2.02bn in 1932 instead of $1.32bn. That is the convoys, Yudenich, the Treasury's $400m of the reconstruction credit and the recognised 1918 write-off. Federal Russia recognises 75% of the write-off in 1922, which restores $153m of the Treasury's claims, $256m of the savers' and $356m of foreign subscribers'. Interest received rises by about $25–30m a year in the 1920s. This is also Pacifica's exposure: if Russia defaults again, these are the claims at risk.

**In the Stress case the war bites.** The Stress economy is half the size, with costs about 25% higher and works at 60% of plan. The war costs 2.7% of GDP and 23% of receipts in 1919. The Treasury borrows $1.28bn in 1918–22 instead of $0.64bn, and public debt is about $690m higher by 1920. In 1920 the bonds exceed what the model's savers can absorb by $197m (a check that did not fail under the old plan). The Development Fund invests $274m in 1918–24 instead of $649m.

## The railway is the constraint

The transport test now runs through a new section, section 5 (Novonikolayevsk–Omsk–Chelyabinsk), to the Ural gate. Story case:

| Period | Men west of Irkutsk | Westbound tons a day past the Ob | Busiest section | Share of its military paths used |
|---|---|---|---|---|
| 26 May–Sep 1918 | 94,000 | 828 | Manzhouli–Kitaisky branch | 56% |
| 1918 Q4 | 154,000 | 909 | Manzhouli–Kitaisky branch | 83% |
| 1919 Q1 | 189,000 | 1,088 | Manzhouli–Kitaisky branch | 84% |
| 1919 Q2 (Volga battle) | 244,000 | 1,399 | Harbin–Manzhouli | 51% |
| 1919 Q3 | 246,000 | 1,492 | Harbin–Manzhouli | 43% |
| 1920 Q1 | 226,000 | 278 (depots drawn) | Harbin–Manzhouli | 16% |

- **The first winter is the tight one.** At CR-030's pace of depot filling, the single-track branch into Transbaikalia reaches 93% of its military paths in autumn 1918, above the 90% limit, while the corps itself is still arriving. The schedule therefore fills harder in summer 1918, using the Amur barges at twice CR-030's plan, and more gently in the autumn. That matches the storyline's "while the barges still run".
- **Under Stress it fails.** With 60% of the works and a harsher winter, the branch needs 109% of its paths in 1918 Q4 and 138% in 1919 Q1. The old plan failed in the second winter, on the Ob in 1919–20. Plan C moves the failure to the first. In the novel this is Vance's winter: Plan C works only if the railway board's loops and water mains double the branch's trains in the first year, as §31 says they do.
- **Section 5 is never the problem.** It is double track and peaks at 20% of its paths (29% under Stress). Beyond Chelyabinsk the Russian armies run their own supply, and the sheet does not test it.

## What changed

| Area | Change |
|---|---|
| **Siberia schedule** | CR-030's schedule replaced by CR-041's. The first period runs 26 May–30 September 1918 (128 days). Forces: Japanese 30,000 rising to 70,000 by 1919; a Chinese brigade of 6,000–10,000 (CR-030 had up to 60,000); Russian and Siberian armies on the line, 15,000 rising to 150,000 in 1919 (column J, relabelled); the Legion at 42,000 and homebound from mid-1919; the Pacifican corps of 50,000 (column L, from 1918 Q4 to 1920 Q1), drawn down from 1920. From 1923: 15,000 Japanese in Transbaikalia, the Chinese guards and 3,000 Pacificans. There are no Siberian troops, Amur or Kara supply, or fortification stores (the guarantee of the federal compact). Munitions, depots, refugees and harvests follow the CR-041 sequence. |
| **Section 5** | New columns DQ–DW: the load past the Ob (a share of section 4's load: 0.8 to 1920, 0.4 in 1921, 0.3 in 1922, 0.2 after), planned and achieved pairs, trains available and needed, and path use. The maximum use, the tightest section, spare trains, train-km, wagons and operating cost include it. New levers `sib_L5` (1,425 km) and `sib_net5` (480 t). |
| **Levers** | `sib_pw` (Pacifican troops west of Irkutsk) is 0.9 instead of 0.85. There are 27 new levers under "CR-041 / CR-040 Stages 3-4", each with its source and a Stress value. |
| **Events** | 21 new rows (E170 onward): credit to Komuch and the Directory (in the Asia group, so the 1914–18 Entente reconciliation is untouched); Cossack pay in gold; the Kazan gold paying for Pacifican munitions; the Black Sea convoys (goods as a loan to Russia, escort and shipping as war operations); the White Sea route; the Baltic squadron's deployment; Yudenich and Estonia; the Treasury's share of the reconstruction credit; and the Emba, Grozny–Maikop and Baku oil receipts. The Siberia-fed rows are renamed ("Russian war 19xx…", "Guarantee of the federal compact 19xx…"). |
| **War credit and Loans** | A lever-driven reversal of the 1918 Russian write-off in the recognition year (`russia_recog` 0.75 in the Story case and 0.5 in Stress; `russia_recog_yr` 1922 and 1924). It applies to the Treasury's, the savers' and foreign subscribers' claims, which then follow the Entente funding path. |
| **Paths C** | Natural increase from 1918 now includes the corps' war deaths (population model, below). It was iterated once with the workbook and converged. |
| **Changes** | A row records the revision. |

## Population

The cohort model has a new `[war_deaths]` assumption: **3,500 Pacifican deaths in 1918–22** (800, 1,400, 800, 450 and 50). They are the corps, the Baltic squadron and the railway advisers shot as hostages. The anchor is Japan's Siberian intervention, which lost 3,116 dead (1,399 killed, 1,717 of disease) of about 70,000 men in 1918–22. The Pacifican corps is smaller, fights harder and for a shorter time.

The deaths are applied as a fixed extra mortality on men aged 19–35 in every group, solved so that the full run loses exactly these numbers. A fixed rate keeps the engine linear, so the flows chain stays exact.

Effect: residents are 14,000 fewer in 1932 (36.18m instead of 36.20m, 0.04%). That is the dead, the children they would have had, and the workbook's own response, since skilled-entry places are a share of residents. Population tests pass and the model and sheet agree to within 134 people in 1932.

Migration is **unchanged** on purpose. In this timeline there is no White emigration (the Whites win), and the Reds go to Europe. Ordinary Russian emigration is already inside the Europe stream. A specific Russian, Siberian or Czech stream would be a new author decision.

## Discrepancies found (for the author)

1. **Train paths.** §31 says "twelve pairs of trains a day on the single track east of Omsk" (PROPOSED, CR-041). The Siberia sheet (CR-030) has 22 planned pairs on double track for Irkutsk–Ob, and 15–18 on the Manchurian sections. The sheet's figures are kept. If the storyline's figure governs, the corps cannot be supplied at the Urals at all, so the sentence is probably meant for the Manchurian line.
2. **China's role.** §31 still says "China provides manpower and the Manchurian railway". CR-041's order of battle has one Chinese brigade of about 6,000 on the railway. The model follows CR-041.

## Not in the model

- **Decisions recorded only in the planning note:** the Alash western regiments as the Emba guard, Dzerzhinsky and Stalin, Turkey and the Straits, the Union's Baghdad railway, Ploiești. They have no amounts until a CR integrates them.
- **B7, the order of service on Russian debt.** The levers recognise all three claim classes at one rate and leave the order of service open. B8, what London collects in 1927, may change the Baku receipt after 1927.
- **The private part of the reconstruction credit** ($600m in the Story case) is placed with savers and not modelled as Treasury cash, as with the Entente credit.
- **Japan's costs** for its seven divisions are Japan's own. Only its share of the guarantee from 1923 reaches the Japan sheet, and it is smaller now.
- **The railway west of Chita,** which Harbin gives Pacifica (CR-031, PROPOSED), carries no commercial receipts. The oil concessions are counted at the Crown's share only, and the champions' profits from them are not added to output.

## Reproduce

```
python3 finance/build/cr041_russian_war.py CR034.xlsx OUT.xlsx --rates finance/build/paths_c_rates_cr041.csv
python3 <xlsx skill>/scripts/recalc.py OUT.xlsx 300
PACIFICA_WORKBOOK=OUT.xlsx python3 population/changes.py   # paths_C_model; one iteration converges
python3 -m unittest discover -s population/tests
```

`CR034.xlsx` is the workbook at commit `09fc30a` (SHA-256 `061d6c34…`).
