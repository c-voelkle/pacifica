"""What the settlement programme of 1867-87 costs (CR-071 Part C, C5). MODEL.

    python3 population/settlement_1887.py   -> outputs/settlement_1887.md

Reads outputs/regions_1887.csv (made by regions_1887.py) and data/counties/settlement_1887.toml.
The programme moves no one out of California: the population model's total is fixed, and the
programme decides only where the acceded units' extra people come from and what bringing them costs.
"""
from __future__ import annotations

import csv
import tomllib
from pathlib import Path

HERE = Path(__file__).parent


def main():
    p = tomllib.load(open(HERE / "data" / "counties" / "settlement_1887.toml", "rb"))
    rows = {r["unit"]: r for r in csv.DictReader(open(HERE / "outputs" / "regions_1887.csv"))}
    units = p["people"]["units"]
    extra = {u: float(rows[u]["pacifica_1887"]) - float(rows[u]["history_1887"]) for u in units}
    total_extra = sum(extra.values())

    pe = p["people"]
    arrivals = total_extra * pe["arrived_share"]
    assisted = arrivals * pe["assisted_share"]
    passage_out = assisted * pe["passage"]
    passage_back = passage_out * pe["repaid_share"]

    a = p["agents"]
    agents = a["per_year"] * (a["years"][1] - a["years"][0] + 1)

    ir = p["irrigation"]
    acres_irr = total_extra * ir["acres_per_person"]
    irr_capital = acres_irr * ir["cost_per_acre"]
    irr_cost = irr_capital * ir["loss_share"]

    ld = p["land"]
    farms = total_extra * ld["farm_share"] / ld["family"]
    acres_sold = farms * ld["acres"]
    land_in = acres_sold * ld["price"] * ld["paid_share"]
    land_out = acres_sold * (ld["purchase"] + ld["survey"])

    rw = p["railways"]
    rail_acres = sum(rw["miles"].values()) * rw["acres_per_mile"]

    gross_out = passage_out + agents + irr_capital + land_out
    net = passage_out - passage_back + agents + irr_cost + land_out - land_in

    m = lambda x: f"${x / 1e6:,.1f}m"
    L = ["# The settlement programme of 1867-87: what it costs (MODEL)\n",
         "Built by `population/settlement_1887.py` from `data/counties/settlement_1887.toml` and `outputs/regions_1887.csv`. "
         "Dollars of about 1880. CR-071 Part C, C5; Part I, I-4. Every figure is the assistant's, PROPOSED.\n",
         "## The people the programme brings\n",
         "| Unit | Our timeline, 1887 | Pacifica, 1887 | Extra |", "|---|---|---|---|"]
    for u in units:
        L.append(f"| {u} | {float(rows[u]['history_1887']):,.0f} | {float(rows[u]['pacifica_1887']):,.0f} | {extra[u]:,.0f} |")
    L.append(f"| **Total** | | | **{total_extra:,.0f}** |\n")
    L.append(f"Of the extra people, {pe['arrived_share']:.0%} arrived in 1867-87 ({arrivals:,.0f}) and the rest were born here. "
             f"{pe['assisted_share']:.0%} of the arrivals were assisted ({assisted:,.0f}).\n")
    L.append("## Costs and receipts, 1867-87\n")
    L.append("| Item | Out | Back | Net |")
    L.append("|---|---|---|---|")
    L.append(f"| Assisted passage at ${pe['passage']:.0f}, {pe['repaid_share']:.0%} repaid with the land | {m(passage_out)} | {m(passage_back)} | {m(passage_out - passage_back)} |")
    L.append(f"| Emigration offices, {a['years'][0]}-{a['years'][1]} | {m(agents)} | | {m(agents)} |")
    L.append(f"| Irrigation districts: {acres_irr:,.0f} acres at ${ir['cost_per_acre']:.0f}, lent and repaid by water rates; {ir['loss_share']:.0%} lost | {m(irr_capital)} | {m(irr_capital - irr_cost)} | {m(irr_cost)} |")
    L.append(f"| Land: {farms:,.0f} farms of {ld['acres']:.0f} acres ({acres_sold / 1e6:,.1f}m acres) bought from the nations and surveyed, sold at ${ld['price']:.2f} on instalments | {m(land_out)} | {m(land_in)} | {m(land_out - land_in)} |")
    L.append(f"| **Total** | **{m(gross_out)}** | **{m(gross_out - net)}** | **{m(net)}** |\n")
    new_net = passage_out - passage_back + agents + irr_cost
    L.append(f"**What is new to the workbook: {m(new_net)}** over 1867-87 (about {m(new_net / 21)} a year), the passage, the offices and the "
             "irrigation loss. The land line is already there in substance: since 14 November 2026 the members' land enters the Land Fund "
             "from 1867 (`Members' land` sheet, L15), so its receipts must not be added a second time. The irrigation loans "
             f"({m(irr_capital)} lent in {ir['built'][0]}-{ir['built'][1]}) are a balance-sheet item repaid over about twenty years.\n")
    L.append(f"**The railways** (I-53) cost the Treasury no cash: their grants are {rail_acres / 1e6:,.1f}m acres of Land Fund land along "
             f"{sum(rw['miles'].values()):,} miles (" + ", ".join(f"{k} {v}" for k, v in rw["miles"].items()) + "). "
             "Land that would not sell without the line.\n")
    L.append("**Not costed here** (private, or already in the workbook): the smelters, coal and timber that anchor the mining and "
             "forest counties (private capital, some on Realm loans); the Union's plains settlers diverted to the Palouse and the Sound "
             "(they pay their own way; the offices above recruit them); California's own Land Fund (CR-033).\n")
    open(HERE / "outputs" / "settlement_1887.md", "w", encoding="utf-8").write("\n".join(L))
    print(f"extra {total_extra:,.0f}; gross out {m(gross_out)}; net {m(net)}; new to workbook {m(passage_out - passage_back + agents + irr_cost)}")


if __name__ == "__main__":
    main()
