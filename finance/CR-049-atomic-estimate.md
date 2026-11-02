# CR-049 — the atomic industry, 1864–1932: uranium, costs and returns (MODEL)

**Status:** MODEL estimate (2 November 2026), accepted by the author for integration and entered in the workbook's Atomic sheet as the central case (see [CR-049-workbook.md](CR-049-workbook.md)). Built by [`build/cr049_atomic_estimate.py`](build/cr049_atomic_estimate.py); the workbook is read for real GDP. Pacifica means to mine as much uranium as it can get; how is the next CR, and these quantities will rise with it. All money in 1913 dollars (multiply by the workbook's price level for current dollars: 1.66 in 1918, 1.58 in 1927). Weapons quantities are a coarse resource bucket, never per device.

## 1. Uranium mined (tonnes of uranium contained)

| Source | 1864–1908 | 1909–1913 | 1914–1919 | 1920–1927 | 1928–1932 | Total |
|---|---:|---:|---:|---:|---:|---:|
| Radium-era by-product (Joachimsthal residues, early Western Slope) | 300 | 0 | 0 | 0 | 0 | 300 |
| Western Slope (Roc Creek, Paradox Valley; Ute lease) | 0 | 530 | 700 | 850 | 680 | 2,760 |
| Joachimsthal (contract 1909, concession 1919) | 0 | 50 | 80 | 160 | 100 | 390 |
| Shinkolobwe (option 1916, three-quarters 1919) | 0 | 0 | 0 | 1,170 | 1,100 | 2,270 |
| Fergana (Tyuya-Muyun, from 1921) | 0 | 0 | 0 | 49 | 35 | 84 |
| **Total** | 300 | 580 | 780 | 2,229 | 1,915 | **5,804** |

## 2. Where it goes (tonnes)

| Use | Tonnes | Share |
|---|---:|---:|
| Research installations (1913, 1916, 1921) | 150 | 3% |
| Weapons: separation-hall feed 1911-1927 (test 1920, three devices 1927) | 250 | 4% |
| Weapons: separation-hall feed 1928-1932 (small arsenal; count OPEN) | 300 | 5% |
| Energy: Tokyo station (two units, first load 1926-27, refuelling from 1928) | 445 | 8% |
| Energy: Pacifican stations (1929, 1930, two in 1931) | 580 | 10% |
| **Reserve held in 1932** (stock for the 1930s power programme, and the margin that denial leaves in Pacifican hands) | 4,079 | 70% |

Summary: energy 1,025 t (18%), weapons 550 t (9%), research 150 t (3%), reserve 4,079 t (70%).

## 3. What it costs (1913 $m)

| Category | 1864–1908 | 1909–1913 | 1914–1919 | 1920–1927 | 1928–1932 | Total |
|---|---:|---:|---:|---:|---:|---:|
| Mining, milling, refining | 1.8 | 4.2 | 5.6 | 10.7 | 8.7 | 31 |
| Contracts, concessions, shares, royalties | 0.0 | 3.0 | 12.6 | 12.6 | 8.0 | 36 |
| Laboratories and research installations | 0.0 | 13.0 | 33.0 | 43.0 | 40.0 | 129 |
| Separation halls, weapons, tests | 0.0 | 36.0 | 150.0 | 89.0 | 125.0 | 400 |
| Power stations | 0.0 | 0.0 | 0.0 | 32.0 | 64.0 | 96 |
| **Total** | 1.8 | 56.2 | 201.2 | 187.3 | 245.7 | **692** |

Against the economy (central case):

| Period | Industry cost per year | Real GDP per year | Share of GDP |
|---|---:|---:|---:|
| 1864–1908 | $0.0m | $3,948m | 0.00% |
| 1909–1913 | $11.2m | $15,656m | 0.07% |
| 1914–1919 | $33.5m | $21,372m | 0.16% |
| 1920–1927 | $23.4m | $31,044m | 0.08% |
| 1928–1932 | $49.1m | $41,227m | 0.12% |

The weapon to 1927 (separation halls, engineering, tests and three-fifths of the laboratories) costs about **$328m** (1913 $), roughly $525m in 1927 money: a few percent of the Treasury's technical programmes each year, which is how it stays inside the Works' and the Polytechnic's budgets without a vote. For comparison, the Manhattan Project cost about $2 billion in 1945 money, close to 1% of one year's American GDP; Pacifica's smaller, slower programme spreads a fraction of that over 15 years. The separation halls are priced at about twice what their output would cost with 1940s equipment, because 1910s vacuum, magnet and valve technology is less efficient.

## 4. What it feeds into the economy (1913 $m, central case)

| Return | 1864–1932 | Note |
|---|---:|---|
| Radium and the source trade | 59 | Net margin; prices fall after 1922 as Pacifica's supply grows |
| Vanadium from Western Slope ore | 58 | About 3 t of vanadium per t of uranium; armour, tool and motor steel |
| Electricity sold, 1928–1932 | 77 | Tokyo from 1928, Pacifican stations from 1930; 70% load, $0.015/kWh |
| Navy capital ships not laid down after 1927 | 150 | Option: the demonstration makes new battleships pointless |
| **Direct returns** | **344** | Against total cost of 692 |

**What the direct returns leave out**, and why they are not added: the valve (from 1895) and electrical industry, X-ray and radium medicine, the Calculation Office's machines, pure metals, graphite and electric furnaces are real and large, but the workbook already carries them inside the national champions (electrical, chemicals and drugs, steel) and the talent multiplier. Adding them here would count them twice. The atom's decisive return is strategic and not in dollars: the 1927 settlement with Britain, the Concord and a lead that, on these numbers, rests on a reserve of uranium most of the world does not know exists.

## 5. Low and high cases

| Case | Uranium mined (t) | Weapons (t) | Energy (t) | Total cost (1913 $m) |
|---|---:|---:|---:|---:|
| low | 4,063 | 385 | 718 | 485 |
| central | 5,804 | 550 | 1,025 | 692 |
| high | 8,706 | 825 | 1,538 | 1,038 |

The cases scale every quantity together; the shares do not change. The decisions that move the result most: how many devices after 1927 (OPEN), how many Pacifican power stations by 1932, and whether naval propulsion starts before 1932 (not assumed).

## 6. Assumptions to check

- **Ore:** Shinkolobwe is extraordinarily rich and cheap to work; the Western Slope is low-grade but carries vanadium. Historical cross-checks: ten tons of ore at about 20% uranium oxide shipped from Roc Creek in 1898; Shinkolobwe ore above ground in 1940 at about 65%.
- **Power stations:** natural-uranium, graphite units of about 40 MWe each, with a first load of about 110 t and yearly refuelling of about a fifth, on the pattern of the first British stations of the 1950s, built first-of-a-kind at about $400 per kW (1913 $).
- **Radium:** at about a third of a gram per tonne of uranium, Pacifica's ore yields more radium than the historical world produced before 1940; prices fall and radium medicine spreads.
- **Everything is MODEL.** No number here enters the workbook until the author asks for it.
