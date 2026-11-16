"""Draw the 124 counties of 1887 (CR-071 Part I) from the Newberry atlas's geometry.

    python3 population/draw_map_1887.py /path/to/county-boundaries-topology/output
        -> population/outputs/map_1887.png

The geometry is not in this repository. It is the CC0 conversion of the Atlas of Historical
County Boundaries at https://github.com/localgeohistoryproject/county-boundaries-topology
(folder `output`: output_counties_metadata.csv, output_counties_ways.csv, output_ways.shp).
Needs shapely, pyshp and matplotlib.

What the picture is and is not: each new county is the union of our timeline's counties of
1 August 1887 named in data/counties/map_1887.toml. Where a historical county is divided between
two new ones, the cut is a straight line chosen by eye (CUTS below). The homelands' outlines are
rough sketches from Part I's verbal lines, not surveyed boundaries. MODEL and PROPOSED throughout.
"""
from __future__ import annotations

import csv
import json
import math
import sys
import tomllib
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import shapefile
from matplotlib.patches import PathPatch
from matplotlib.path import Path as MPath
from shapely.geometry import LineString, Point, Polygon, box, shape
from shapely.ops import nearest_points
from shapely.ops import polygonize, unary_union
import numpy as np
import shapely

HERE = Path(__file__).parent
DATA = HERE / "data" / "counties"
DAY = 18870801

# historical county -> [(new county, lon_min, lat_min, lon_max, lat_max)], the rest stays with the
# new county that holds the largest fraction in map_1887.toml. Lines chosen by eye.
CUTS = {
    "UT;Salt Lake": [("Jordan", -113.0, 40.0, -111.0, 40.69)],
    "UT;Box Elder": [("Bear River", -112.45, 41.62, -111.0, 42.1)],
    "CA;Solano": [("Suisun", -122.12, 38.17, -121.0, 39.0)],
    "CA;Contra Costa": [("Carquinez", -122.5, 37.97, -122.02, 38.2)],
    "CA;Los Angeles": [("Santa Ana", -118.12, 33.2, -117.3, 33.95)],
    "CA;San Bernardino": [("Mojave", -118.0, 34.55, -114.0, 36.0)],
    "NM;Lincoln": [("Mesilla", -106.6, 32.0, -105.85, 34.3)],
    "NM;Bernalillo": [("Little Colorado", -109.2, 34.9, -108.2, 35.75)],
    "NV;Lander": [("Elko", -118.0, 40.0, -116.0, 41.1)],
    "AZ;Mohave": [("Virgin", -114.2, 36.2, -112.0, 37.1)],
    "AZ;Yavapai": [("Coconino", -114.0, 35.0, -110.6, 37.1)],
}
# the homelands' sketched lines and the enclaves' places: data/counties/homelands_1887.toml
# where a county's detached remainder should go when the longest shared line is a mountain crest
PREFER = {"Spokane": "Big Bend"}
UNIT_COLOUR = {"California": "#f3d9a4", "Oregon": "#b9d8b0", "Columbia": "#a9cfe0", "Deseret": "#e6c3d6",
               "New Mexico": "#f2b8a0", "Idaho": "#d5d0ea", "Arizona": "#f6e39a", "Washoe": "#d9d9c3",
               "The Rockies": "#c9b79c", "Hawaii": "#b6e0d4", "Western Montana": "#c7dcef", "Baja": "#f0cfa0",
               "Thalassia": "#e86f5a"}


def albers(lon, lat, z=None, lon0=-114.0, lat0=38.0, p1=30.0, p2=46.0):
    r = math.radians
    n = (math.sin(r(p1)) + math.sin(r(p2))) / 2
    c = math.cos(r(p1)) ** 2 + 2 * n * math.sin(r(p1))
    rho0 = math.sqrt(c - 2 * n * math.sin(r(lat0))) / n
    if isinstance(lon, (int, float)):
        lon, lat = [lon], [lat]
    xs, ys = [], []
    for lo, la in zip(lon, lat):
        rho = math.sqrt(c - 2 * n * math.sin(r(la))) / n
        th = n * r(lo - lon0)
        xs.append(rho * math.sin(th))
        ys.append(rho0 - rho * math.cos(th))
    return (xs[0], ys[0]) if len(xs) == 1 else (xs, ys)


def load_geometry(topo: Path, wanted: dict[str, str], extra_ids: dict[str, str]):
    """wanted: key -> newberry id (version valid on DAY); extra_ids: key -> id_num (fixed versions)."""
    id_num = {}
    for r in csv.DictReader(open(topo / "output_counties_metadata.csv", encoding="utf-8")):
        if int(r["start_n"]) <= DAY <= int(r["end_n"]):
            for k, nid in wanted.items():
                if r["id"] == nid:
                    id_num[r["id_num"]] = k
    for k, n in extra_ids.items():
        id_num[n] = k
    edges = defaultdict(lambda: {"outer": [], "inner": []})
    for r in csv.DictReader(open(topo / "output_counties_ways.csv")):
        if r["id_num"] in id_num:
            edges[id_num[r["id_num"]]]["inner" if r["edge_type"] == "inner" else "outer"].append(int(r["edge_id"]))
    sf = shapefile.Reader(str(topo / "output_ways"))
    need = {e for v in edges.values() for t in v.values() for e in t}
    lines = {}
    for i, rec in enumerate(sf.iterRecords()):
        if rec[0] in need:
            shp = sf.shape(i)
            parts = list(shp.parts) + [len(shp.points)]
            lines[rec[0]] = [LineString(shp.points[a:b]) for a, b in zip(parts, parts[1:]) if b - a > 1]
    geom = {}
    for k, v in edges.items():
        outer = unary_union(list(polygonize([l for e in v["outer"] for l in lines.get(e, [])])))
        inner = unary_union(list(polygonize([l for e in v["inner"] for l in lines.get(e, [])]))) if v["inner"] else None
        geom[k] = outer.difference(inner) if inner is not None and not inner.is_empty else outer
    return geom


def colville(data: Path):
    """The ground between the Columbia and the Okanogan south of 49 N, from river centre lines."""
    riv = json.load(open(data / "rivers_colville.geojson"))
    lines = [shape(f["geometry"]) for f in riv["features"]]
    lines.append(LineString([(-120.2, 49.0), (-117.0, 49.0)]))
    col = unary_union([l for l, f in zip(lines, riv["features"]) if f["properties"]["name"] == "Columbia"])
    for l, f in zip(list(lines), riv["features"]):  # close the gap at the Okanogan's mouth
        if f["properties"]["name"] == "Okanogan":
            end = Point(l.coords[-1])
            lines.append(LineString([end, nearest_points(end, col)[1]]))
    net = unary_union([l.buffer(0.004) for l in lines]).boundary
    net = unary_union(lines + [net])
    faces = [f for f in polygonize(net) if f.area > 0.05 and f.representative_point().within(box(-119.55, 48.0, -118.1, 49.0))]
    return unary_union(faces).buffer(0.006).intersection(box(-121.0, 47.0, -117.0, 49.0))


def draw_poly(ax, g, **kw):
    if g.is_empty:
        return
    for p in getattr(g, "geoms", [g]):
        if p.geom_type != "Polygon":
            continue
        verts, codes = [], []
        for ring in [p.exterior, *p.interiors]:
            xy = list(ring.coords)
            verts += xy
            codes += [MPath.MOVETO] + [MPath.LINETO] * (len(xy) - 2) + [MPath.CLOSEPOLY]
        ax.add_patch(PathPatch(MPath(verts, codes), **kw))


def main():
    topo = Path(sys.argv[1])
    counties = tomllib.load(open(DATA / "map_1887.toml", "rb"))["county"]
    atlas = {f"{r['state']};{r['county']}": r["newberry_id"]
             for r in csv.DictReader(open(DATA / "newberry_1887.csv", encoding="utf-8")) if r["kind"] == "county"}
    hawaii = {"HI;Kauaʻi": "4434", "HI;Maui": "4436", "HI;Kalawao": "4432", "HI;Oʻahu": "4430"}
    for r in csv.DictReader(open(topo / "output_counties_metadata.csv", encoding="utf-8")):
        if r["state_terr"].startswith("Hawaii") and r["name"].startswith("EAST HAWAII"):
            hawaii["HI;Hilo"] = r["id_num"]
        if r["state_terr"].startswith("Hawaii") and r["name"].startswith("WEST HAWAII"):
            hawaii["HI;Kona"] = r["id_num"]
    geom = load_geometry(topo, atlas, hawaii)

    # assemble the new counties
    owner = {}
    new = defaultdict(list)
    unit = {c["name"]: c["unit"] for c in counties}
    for c in counties:
        for k, f in c["parts"].items():
            if k not in owner or f > owner[k][1]:
                owner[k] = (c["name"], f)
    for k, (name, _) in owner.items():
        g = geom[k]
        for other, x1, y1, x2, y2 in CUTS.get(k, []):
            piece = g.intersection(box(x1, y1, x2, y2))
            new[other].append(piece)
            g = g.difference(piece)
        new[name].append(g)
    for name, key in (("Oʻahu", "HI;Oʻahu"), ("Maui", "HI;Maui"), ("Maui", "HI;Kalawao"), ("Kauaʻi", "HI;Kauaʻi"),
                      ("Hilo", "HI;Hilo"), ("Kona", "HI;Kona")):
        if key in geom:
            new[name].append(geom[key])
    thal = box(-157.87, 21.38, -157.76, 21.53)
    oahu = unary_union(new["Oʻahu"])
    new["Thalassia"] = [oahu.intersection(thal)]
    new["Oʻahu"] = [oahu.difference(thal)]
    baja = {f["properties"]["name"]: shape(f["geometry"]) for f in json.load(open(DATA / "baja_outline.geojson"))["features"]}
    new["Ensenada"] = [baja["Baja California"]]
    new["La Paz"] = [baja["Baja California Sur"]]
    merged = {n: unary_union(gs).buffer(0) for n, gs in new.items()}
    hl = tomllib.load(open(DATA / "homelands_1887.toml", "rb"))
    homes = {}
    for h in hl["large"]:
        g = Polygon(h["ring"]) if "ring" in h else None
        if h.get("rivers"):  # Colville: between the Columbia and the Okanogan, south of 49 N
            g = colville(DATA)
        if "counties" in h:
            cg = unary_union([geom[k] for k in h["counties"]])
            if "box" in h:
                cg = cg.intersection(box(*h["box"]))
            g = cg if g is None else g.intersection(cg)
        homes[h["name"]] = g.buffer(0)
    report = []
    KM = 1 / 111.0  # degrees, roughly
    all_homes = unary_union(list(homes.values()))
    skip = {c["name"] for c in counties if c["unit"] in ("Hawaii", "Thalassia", "Baja")}
    for n in list(merged):
        if n in skip or not merged[n].intersects(all_homes):
            continue
        rest = merged[n].difference(all_homes)
        opened = rest.buffer(-6 * KM).buffer(6 * KM).intersection(rest)  # drop spikes and slivers under about 12 km
        slivers = rest.difference(opened)
        for h in homes:  # slivers touching a homeland go to it
            near = [q for q in getattr(slivers, "geoms", [slivers]) if not q.is_empty and q.intersects(homes[h].buffer(2 * KM))]
            if near:
                homes[h] = unary_union([homes[h]] + near).buffer(0)
        pieces = sorted([q for q in getattr(opened, "geoms", [opened]) if q.geom_type == "Polygon"], key=lambda q: -q.area)
        merged[n] = pieces[0]
        for pc in pieces[1:]:
            sqmi = pc.area * 69.0 * 69.0 * math.cos(math.radians(pc.centroid.y))
            best, blen = None, 0.0
            for m2, g2 in merged.items():
                if m2 == n or m2 in skip:
                    continue
                shared = pc.buffer(1.5 * KM).intersection(g2).area
                if shared > blen:
                    best, blen = m2, shared
            near_home = max(homes, key=lambda h: pc.buffer(1.5 * KM).intersection(homes[h]).area)
            best = PREFER.get(n, best)
            if sqmi < 500 and pc.buffer(1.5 * KM).intersects(homes[near_home]):
                homes[near_home] = unary_union([homes[near_home], pc]).buffer(0)
                report.append(f"{n}: a detached {sqmi:,.0f} sq mi goes to the {near_home} homeland")
            elif best:
                merged[best] = unary_union([merged[best], pc]).buffer(0)
                report.append(f"{n}: a detached {sqmi:,.0f} sq mi goes to {best}")
            else:
                merged[n] = unary_union([merged[n], pc])
                report.append(f"{n}: a detached {sqmi:,.0f} sq mi stays with it (no neighbour)")
    areas = {h: g.area * 69.0 * 69.0 * math.cos(math.radians(g.centroid.y)) for h, g in homes.items()}
    missing = [c["name"] for c in counties if c["name"] not in merged or merged[c["name"]].is_empty]
    # ground of Pacifican states in no county: the Utes' Slope, the Wallowa
    assigned = set(owner)
    states_in = ("CA", "OR", "WA", "ID", "NV", "UT", "AZ", "NM")
    shares = tomllib.load(open(DATA / "overrides.toml", "rb"))["pacifica_share"]
    outside = [g for k, g in geom.items() if k not in assigned and not k.startswith("HI;")
               and (k.split(";")[0] in states_in or float(shares.get(k, 0)) == 1)]
    union_side = [g for k, g in geom.items() if k not in assigned and not k.startswith("HI;")
                  and k.split(";")[0] in ("MT", "WY", "CO") and float(shares.get(k, 0)) < 1]

    def proj_with(fn):
        def f(g):
            def tr(c):
                xs, ys = fn(list(c[:, 0]), list(c[:, 1]))
                return np.column_stack([xs, ys])
            return shapely.transform(g, tr)
        return f

    P = proj_with(albers)
    local = lambda lon, lat: ([(a + 157.5) * math.cos(math.radians(20.5)) for a in lon], list(lat))
    PH = proj_with(local)
    fig = plt.figure(figsize=(17, 21), dpi=170)
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.95])
    ax.set_aspect("equal")
    ax.axis("off")
    for g in union_side:
        draw_poly(ax, P(g), facecolor="#f4f4f4", edgecolor="#dddddd", linewidth=0.3)
    for g in outside:
        left = g.difference(unary_union(list(homes.values())).buffer(3 * KM))
        if not left.is_empty:
            draw_poly(ax, P(left), facecolor="#ffffff", edgecolor="#999999", linewidth=0.4, hatch="////")
    for k, g in geom.items():  # our timeline's county lines, faint
        if k in assigned:
            draw_poly(ax, P(g), facecolor="none", edgecolor="#b0b0b0", linewidth=0.25, linestyle=":")
    small = {"San Francisco", "Carquinez", "Suisun", "Diablo", "Alameda", "San Mateo", "Marin", "Santa Cruz", "Napa",
             "Salt Lake", "Jordan", "Weber", "Santa Clara", "Sonoma", "Yolo", "Sacramento", "San Joaquin"}
    main_names = [c["name"] for c in counties if c["unit"] not in ("Hawaii", "Thalassia")]
    for n in main_names:
        g = P(merged[n])
        draw_poly(ax, g, facecolor=UNIT_COLOUR[unit[n]], edgecolor="#333333", linewidth=0.9)
    for n in main_names:
        if n in small:
            continue
        g = P(merged[n])
        big = max(getattr(g, "geoms", [g]), key=lambda p: p.area)
        pt = big.representative_point()
        fs = max(4.2, min(7.5, 3.6 + 95 * math.sqrt(big.area)))
        ax.text(pt.x, pt.y, n.replace(" ", "\n") if len(n) > 9 else n, ha="center", va="center", fontsize=fs,
                color="#111111", linespacing=0.9)
    for name, hg in homes.items():
        g = P(hg)
        draw_poly(ax, g, facecolor="#fdf1e7", edgecolor="#7a3b12", linewidth=1.3)
        pt = max(getattr(g, "geoms", [g]), key=lambda q: q.area).representative_point()
        ax.text(pt.x, pt.y, name.replace(" ", "\n", 1) if len(name) > 9 else name, ha="center", va="center",
                fontsize=6.4, style="italic", color="#7a3b12", weight="bold", linespacing=0.9)
    for h in hl["inner"]:
        g = P(Polygon(h["ring"]))
        draw_poly(ax, g, facecolor="#f6d9c2", edgecolor="#7a3b12", linewidth=1.1, linestyle="--")
        pt = g.representative_point()
        ax.text(pt.x, pt.y, h["name"], ha="center", va="center", fontsize=5.8, style="italic", color="#7a3b12", weight="bold")
    for group, fs in (("california", 4.4), ("elsewhere", 4.6)):
        for name, lo, la in hl["enclaves"][group]:
            x, y = albers(lo, la)
            ax.plot([x], [y], marker="s", ms=3.2, color="#7a3b12", mec="white", mew=0.4, zorder=6)
            ax.text(x + 0.0012, y, name, ha="left", va="center", fontsize=fs, style="italic", color="#5a2a0c", zorder=6)
    ax.autoscale_view()
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ax.set_xlim(x0 - 0.02, x1 + 0.005)

    def inset(rect, names, title, lonlat, fs=6.5, P=P, fn=albers):
        a = fig.add_axes(rect)
        a.set_aspect("equal")
        for n in names:
            draw_poly(a, P(merged[n]), facecolor=UNIT_COLOUR[unit[n]], edgecolor="#333333", linewidth=0.9)
        xs_, ys_ = fn([lonlat[0], lonlat[2]], [lonlat[1], lonlat[3]])
        (xa, ya), (xb, yb) = (xs_[0], ys_[0]), (xs_[1], ys_[1])
        a.set_xlim(min(xa, xb), max(xa, xb))
        a.set_ylim(min(ya, yb), max(ya, yb))
        for n in names:
            g = P(merged[n])
            pt = max(getattr(g, "geoms", [g]), key=lambda p: p.area).representative_point()
            if min(xa, xb) < pt.x < max(xa, xb) and min(ya, yb) < pt.y < max(ya, yb):
                a.text(pt.x, pt.y, n.replace(" ", "\n") if len(n) > 9 else n, ha="center", va="center", fontsize=fs,
                       linespacing=0.9)
        a.set_xticks([])
        a.set_yticks([])
        a.set_title(title, fontsize=9, loc="left")
        return a

    inset([0.02, 0.04, 0.33, 0.20], ["Kauaʻi", "Oʻahu", "Thalassia", "Maui", "Hilo", "Kona"],
          "Hawaii's five and Thalassia (the red mark on Kāneʻohe Bay)", (-160.4, 18.7, -154.6, 22.4), fs=8, P=PH, fn=local)
    inset([0.02, 0.26, 0.24, 0.20], main_names, "San Francisco Bay", (-123.25, 36.9, -120.9, 38.95), fs=6.3)
    inset([0.66, 0.13, 0.20, 0.19], main_names, "The Wasatch Front", (-113.3, 39.9, -110.8, 42.3), fs=7)

    fig.text(0.02, 0.975, "The 124 counties of the Constitution of the Realm, 1 August 1887", fontsize=20, weight="bold")
    fig.text(0.02, 0.962, "CR-071 Part I, draft 7 (16 November 2026). Colours: the old members and territories the counties replace. "
             "Dotted grey: our timeline's county lines of 1887.\n"
             "Brown outlines: the large homelands, outside the 124, on the lines of Royce's Indian Land Cessions where our timeline has a text "
             "(placed from the text within a few miles). Dashed: the Hopi.\n"
             "Brown squares: homelands that are enclaves inside a county, not yet outlined. Not shown: Alaska. MODEL and PROPOSED.",
             fontsize=9.5, va="top")
    handles = [plt.Rectangle((0, 0), 1, 1, fc=c, ec="#333333") for c in UNIT_COLOUR.values()]
    fig.legend(handles, list(UNIT_COLOUR), loc="lower right", bbox_to_anchor=(0.985, 0.03), fontsize=9, ncol=2,
               title="Old unit", frameon=True)
    out = HERE / "outputs" / "map_1887.png"
    fig.savefig(out)
    with open(HERE / "outputs" / "homelands_1887.md", "w", encoding="utf-8") as f:
        f.write("# The large homelands as drawn (MODEL)\n\nBuilt by `population/draw_map_1887.py` from "
                "`data/counties/homelands_1887.toml`.\n\n| Homeland | Square miles as drawn | Royce |\n|---|---|---|\n")
        for h in hl["large"]:
            f.write(f"| {h['name']} | {areas[h['name']]:,.0f} | {h['royce']} |\n")
        f.write(f"| **Total** | {sum(areas.values()):,.0f} | |\n\n## Counties adjusted to the homelands' lines\n\n")
        f.write("\n".join(f"- {r}" for r in report) + "\n")
    print("\n".join(report))
    print({h: round(a) for h, a in areas.items()})
    print("wrote", out, "| counties with no shape:", missing or "none", "| drawn:", len([n for n in merged if not merged[n].is_empty]))


if __name__ == "__main__":
    main()
