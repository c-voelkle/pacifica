#!/usr/bin/env python3
"""CR-049: the atomic industry, 1864-1932 -- uranium, costs and returns (MODEL).

A stand-alone estimate requested by the author on 2 November 2026 before
integration. It reads Pacifica's real GDP (1913 $m) from the current workbook
and does not modify it; cr049_atomic_programme.py enters its central case.

Every input is a labelled assumption in the tables below; low and high cases
scale them. Weapons quantities are kept deliberately coarse: they are a
resource bucket (separation-hall feed), never a per-device figure.

    python3 finance/build/cr049_atomic_estimate.py   # writes finance/CR-049-atomic-estimate.md
"""
from __future__ import annotations

from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[2]
WORKBOOK = ROOT / "finance" / "Pacifica_financial_model_1846-1932.xlsx"
OUT = ROOT / "finance" / "CR-049-atomic-estimate.md"
YEARS = range(1864, 1933)


def ramp(points: dict[int, float]) -> dict[int, float]:
    """Annual values from {year: value} break-points; constant until the next point, 0 before the first."""
    keys = sorted(points)
    out = {}
    for y in YEARS:
        v = 0.0
        for k in keys:
            if y >= k:
                v = points[k]
        out[y] = v
    return out


# ---------------------------------------------------------------- supply (t U contained)
# Radium era: uranium recovered as a by-product of the source trade (CR-049 F1).
SUPPLY = {
    "Radium-era by-product (Joachimsthal residues, early Western Slope)": ramp({1864: 1, 1876: 3, 1882: 10, 1909: 0}),
    "Western Slope (Roc Creek, Paradox Valley; Ute lease)": ramp({1909: 40, 1910: 70, 1911: 100, 1912: 140, 1913: 180,
                                                                  1914: 120, 1919: 100, 1927: 150, 1928: 150, 1932: 80}),
    "Joachimsthal (contract 1909, concession 1919)": ramp({1909: 10, 1919: 30, 1920: 20}),  # 1919 includes wartime stock
    "Shinkolobwe (option 1916, three-quarters 1919)": ramp({1920: 50, 1921: 120, 1922: 150, 1927: 250, 1932: 100}),
    "Fergana (Tyuya-Muyun, from 1921)": ramp({1921: 7}),
}

# ---------------------------------------------------------------- uses (t U)
USES = {
    "Research installations (1913, 1916, 1921)": {1913: 50, 1916: 50, 1921: 50},
    "Weapons: separation-hall feed 1911-1927 (test 1920, three devices 1927)": {y: 250 / 17 for y in range(1911, 1928)},
    "Weapons: separation-hall feed 1928-1932 (small arsenal; count OPEN)": {y: 60 for y in range(1928, 1933)},
    "Energy: Tokyo station (two units, first load 1926-27, refuelling from 1928)": {1926: 110, 1927: 110,
                                                                                     **{y: 45 for y in range(1928, 1933)}},
    "Energy: Pacifican stations (1929, 1930, two in 1931)": {1929: 110, 1930: 130, 1931: 260, 1932: 80},
}

# ---------------------------------------------------------------- costs (1913 $m)
MINING_COST_PER_KG = {  # mining, milling and refining, 1913 $ per kg U
    "Radium-era by-product (Joachimsthal residues, early Western Slope)": 6.0,
    "Western Slope (Roc Creek, Paradox Valley; Ute lease)": 7.0,
    "Joachimsthal (contract 1909, concession 1919)": 9.0,
    "Shinkolobwe (option 1916, three-quarters 1919)": 2.5,
    "Fergana (Tyuya-Muyun, from 1921)": 8.0,
}
COSTS = {
    # (category, label): {year: $m}
    ("acquisition", "Joachimsthal contract premium and royalties"): ramp({1909: 0.5, 1919: 0.7}),
    ("acquisition", "Shinkolobwe: option, Tanganyika Concessions shares, royalties"): {
        **{y: 0.3 for y in range(1916, 1917)}, 1917: 3.0, 1918: 3.0, 1919: 2.5,
        **{y: 0.6 for y in range(1920, 1933)}},
    ("acquisition", "Fergana concession and Ute lease fees"): ramp({1909: 0.1, 1921: 0.3}),
    ("research", "The Works' atomic laboratories (staff, instruments, recruits)"): ramp({1909: 2, 1914: 5, 1928: 8}),
    ("research", "Research installations (graphite, metal, buildings)"): {1913: 3, 1916: 3, 1921: 3},
    ("weapons", "Separation halls: construction 1912-1919, enlargement 1928-1930"): {
        **{y: 120 / 8 for y in range(1912, 1920)}, **{y: 20 for y in range(1928, 1931)}},
    ("weapons", "Separation halls: operation and hydro power"): ramp({1914: 8, 1928: 10}),
    ("weapons", "Weapon engineering, test site, security"): ramp({1911: 2, 1928: 3}),
    ("weapons", "Desert test (1920) and sea demonstration (1927)"): {1920: 3, 1927: 6},
    ("energy", "Tokyo station (80 MWe, 1925-1927; financed jointly, OPEN)"): {1925: 10, 1926: 12, 1927: 10},
    ("energy", "Pacifican stations (4 x 40 MWe, 1928-1931)"): {1928: 12, 1929: 16, 1930: 18, 1931: 18},
}

# ---------------------------------------------------------------- returns (1913 $m)
RADIUM_MARGIN = ramp({1876: 0.5, 1909: 2.0, 1922: 1.5})      # source trade and medical radium, net
V_PER_U = 3.0                                                 # t vanadium per t uranium in Western Slope ore
V_PRICE = 7.0                                                 # 1913 $ per kg V, net of recovery
STATION_MWE = ramp({1928: 80, 1929: 120, 1930: 160, 1931: 240})  # in service from the year after first load
CAPACITY_FACTOR = 0.7
POWER_PRICE = 0.015                                           # 1913 $ per kWh, wholesale
NAVY_SAVING = ramp({1928: 30})                                # capital ships not laid down after 1927 (option)

CASES = {"low": 0.7, "central": 1.0, "high": 1.5}


def real_gdp() -> dict[int, float]:
    wb = openpyxl.load_workbook(WORKBOOK, read_only=True, data_only=True)
    rows = list(wb["Economy"].iter_rows(values_only=True))
    hdr = rows[4]
    col = hdr.index("Real GDP (1913 $m)")
    return {r[0]: r[col] for r in rows[5:] if isinstance(r[0], int) and r[col] is not None}


def total(d: dict[int, float], a: int = 1864, b: int = 1932) -> float:
    return sum(v for y, v in d.items() if a <= y <= b)


def main() -> None:
    gdp = real_gdp()
    periods = [(1864, 1908), (1909, 1913), (1914, 1919), (1920, 1927), (1928, 1932)]
    lines: list[str] = []
    w = lines.append

    w("# CR-049 — the atomic industry, 1864–1932: uranium, costs and returns (MODEL)\n")
    w("**Status:** MODEL estimate (2 November 2026), accepted by the author for integration and entered in the "
      "workbook's Atomic sheet as the central case (see [CR-049-workbook.md](CR-049-workbook.md)). Built by "
      "[`build/cr049_atomic_estimate.py`](build/cr049_atomic_estimate.py); the workbook is read for real GDP. "
      "Pacifica means to mine as much uranium as it can get; how is the next CR, and these quantities will rise with it. All money in 1913 dollars (multiply by the workbook's price level for current dollars: "
      "1.66 in 1918, 1.58 in 1927). Weapons quantities are a coarse resource bucket, never per device.\n")

    # supply
    w("## 1. Uranium mined (tonnes of uranium contained)\n")
    w("| Source | " + " | ".join(f"{a}–{b}" for a, b in periods) + " | Total |")
    w("|---|" + "---:|" * (len(periods) + 1))
    sup_total = 0.0
    for name, d in SUPPLY.items():
        cells = [total(d, a, b) for a, b in periods]
        sup_total += sum(cells)
        w(f"| {name} | " + " | ".join(f"{c:,.0f}" for c in cells) + f" | {sum(cells):,.0f} |")
    w(f"| **Total** | " + " | ".join(f"{sum(total(d, a, b) for d in SUPPLY.values()):,.0f}" for a, b in periods)
      + f" | **{sup_total:,.0f}** |\n")

    # uses
    w("## 2. Where it goes (tonnes)\n")
    w("| Use | Tonnes | Share |")
    w("|---|---:|---:|")
    used = 0.0
    groups = {"Research": 0.0, "Weapons": 0.0, "Energy": 0.0}
    for name, d in USES.items():
        t = total(d)
        used += t
        groups[name.split(":")[0].split(" ")[0]] = groups.get(name.split(":")[0].split(" ")[0], 0) + t
        w(f"| {name} | {t:,.0f} | {t / sup_total:.0%} |")
    reserve = sup_total - used
    w(f"| **Reserve held in 1932** (stock for the 1930s power programme, and the margin that denial leaves in Pacifican hands) | {reserve:,.0f} | {reserve / sup_total:.0%} |\n")
    w(f"Summary: energy {groups['Energy']:,.0f} t ({groups['Energy'] / sup_total:.0%}), weapons {groups['Weapons']:,.0f} t "
      f"({groups['Weapons'] / sup_total:.0%}), research {groups['Research']:,.0f} t ({groups['Research'] / sup_total:.0%}), "
      f"reserve {reserve:,.0f} t ({reserve / sup_total:.0%}).\n")

    # costs
    mining = {}
    for name, d in SUPPLY.items():
        for y, v in d.items():
            mining[y] = mining.get(y, 0) + v * MINING_COST_PER_KG[name] / 1000  # t * $/kg -> $m
    cat_tot = {"mining": mining}
    for (cat, _), d in COSTS.items():
        acc = cat_tot.setdefault(cat, {})
        for y, v in d.items():
            acc[y] = acc.get(y, 0) + v
    w("## 3. What it costs (1913 $m)\n")
    w("| Category | " + " | ".join(f"{a}–{b}" for a, b in periods) + " | Total |")
    w("|---|" + "---:|" * (len(periods) + 1))
    labels = {"mining": "Mining, milling, refining", "acquisition": "Contracts, concessions, shares, royalties",
              "research": "Laboratories and research installations", "weapons": "Separation halls, weapons, tests",
              "energy": "Power stations"}
    grand = {}
    for cat in ["mining", "acquisition", "research", "weapons", "energy"]:
        cells = [total(cat_tot[cat], a, b) for a, b in periods]
        for i, c in enumerate(cells):
            grand[i] = grand.get(i, 0) + c
        w(f"| {labels[cat]} | " + " | ".join(f"{c:,.1f}" for c in cells) + f" | {sum(cells):,.0f} |")
    w("| **Total** | " + " | ".join(f"{grand[i]:,.1f}" for i in range(len(periods))) + f" | **{sum(grand.values()):,.0f}** |\n")

    # GDP shares
    w("Against the economy (central case):\n")
    w("| Period | Industry cost per year | Real GDP per year | Share of GDP |")
    w("|---|---:|---:|---:|")
    for i, (a, b) in enumerate(periods):
        n = b - a + 1
        g = sum(gdp.get(y, 0) for y in range(a, b + 1)) / n
        w(f"| {a}–{b} | ${grand[i] / n:,.1f}m | ${g:,.0f}m | {grand[i] / n / g:.2%} |")
    w("")
    weap = sum(total(cat_tot["weapons"], a, b) for a, b in [(1909, 1927)]) + 0.6 * total(cat_tot["research"], 1909, 1927)
    w(f"The weapon to 1927 (separation halls, engineering, tests and three-fifths of the laboratories) costs about "
      f"**${weap:,.0f}m** (1913 $), roughly ${weap * 1.6:,.0f}m in 1927 money: a few percent of the Treasury's "
      f"technical programmes each year, which is how it stays inside the Works' and the Polytechnic's budgets "
      f"without a vote. For comparison, the Manhattan Project cost about $2 billion in 1945 money, close to 1% of "
      f"one year's American GDP; Pacifica's smaller, slower programme spreads a fraction of that over 15 years. The separation halls are priced at about twice what their output would cost with 1940s equipment, because 1910s vacuum, magnet and valve technology is less efficient.\n")

    # returns
    w("## 4. What it feeds into the economy (1913 $m, central case)\n")
    radium = total(RADIUM_MARGIN)
    vanad = sum(SUPPLY["Western Slope (Roc Creek, Paradox Valley; Ute lease)"].values()) * V_PER_U * V_PRICE / 1000
    power = sum(STATION_MWE[y] * 8760 * CAPACITY_FACTOR * 1000 * POWER_PRICE / 1e6 for y in YEARS)
    navy = total(NAVY_SAVING)
    w("| Return | 1864–1932 | Note |")
    w("|---|---:|---|")
    w(f"| Radium and the source trade | {radium:,.0f} | Net margin; prices fall after 1922 as Pacifica's supply grows |")
    w(f"| Vanadium from Western Slope ore | {vanad:,.0f} | About {V_PER_U:.0f} t of vanadium per t of uranium; armour, tool and motor steel |")
    w(f"| Electricity sold, 1928–1932 | {power:,.0f} | Tokyo from 1928, Pacifican stations from 1930; {CAPACITY_FACTOR:.0%} load, ${POWER_PRICE}/kWh |")
    w(f"| Navy capital ships not laid down after 1927 | {navy:,.0f} | Option: the demonstration makes new battleships pointless |")
    direct = radium + vanad + power + navy
    w(f"| **Direct returns** | **{direct:,.0f}** | Against total cost of {sum(grand.values()):,.0f} |\n")
    w("**What the direct returns leave out**, and why they are not added: the valve (from 1895) and electrical "
      "industry, X-ray and radium medicine, the Calculation Office's machines, pure metals, graphite and electric "
      "furnaces are real and large, but the workbook already carries them inside the national champions "
      "(electrical, chemicals and drugs, steel) and the talent multiplier. Adding them here would count them twice. "
      "The atom's decisive return is strategic and not in dollars: the 1927 settlement with Britain, the Concord "
      "and a lead that, on these numbers, rests on a reserve of uranium most of the world does not know exists.\n")

    # cases
    w("## 5. Low and high cases\n")
    w("| Case | Uranium mined (t) | Weapons (t) | Energy (t) | Total cost (1913 $m) |")
    w("|---|---:|---:|---:|---:|")
    for case, k in CASES.items():
        w(f"| {case} | {sup_total * k:,.0f} | {groups['Weapons'] * k:,.0f} | {groups['Energy'] * k:,.0f} | {sum(grand.values()) * k:,.0f} |")
    w("\nThe cases scale every quantity together; the shares do not change. The decisions that move the result most: "
      "how many devices after 1927 (OPEN), how many Pacifican power stations by 1932, and whether naval propulsion "
      "starts before 1932 (not assumed).\n")

    w("## 6. Assumptions to check\n")
    w("- **Ore:** Shinkolobwe is extraordinarily rich and cheap to work; the Western Slope is low-grade but carries vanadium. "
      "Historical cross-checks: ten tons of ore at about 20% uranium oxide shipped from Roc Creek in 1898; Shinkolobwe "
      "ore above ground in 1940 at about 65%.\n"
      "- **Power stations:** natural-uranium, graphite units of about 40 MWe each, with a first load of about 110 t and "
      "yearly refuelling of about a fifth, on the pattern of the first British stations of the 1950s, built "
      "first-of-a-kind at about $400 per kW (1913 $).\n"
      "- **Radium:** at about a third of a gram per tonne of uranium, Pacifica's ore yields more radium than the "
      "historical world produced before 1940; prices fall and radium medicine spreads.\n"
      "- **Everything is MODEL.** No number here enters the workbook until the author asks for it.\n")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: mined {sup_total:,.0f} t; cost {sum(grand.values()):,.0f} (1913 $m); "
          f"energy {groups['Energy']:,.0f} t, weapons {groups['Weapons']:,.0f} t, reserve {reserve:,.0f} t")


if __name__ == "__main__":
    main()
