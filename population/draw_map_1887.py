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
from shapely.geometry import LineString, Polygon, box, shape
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
# rough sketches of the large homelands (I-8, I-26), lon/lat rings drawn from Part I's wording
HOMELANDS = {
    "Diné country\n(Hopi within)": [(-111.75, 35.45), (-111.2, 36.9), (-109.0, 37.1), (-108.0, 36.85), (-107.45, 35.45),
                                    (-107.9, 35.65), (-109.0, 35.75), (-110.6, 35.3), (-111.5, 35.3)],
}
HOMELAND_LABELS = {  # no outline: lines OPEN
    "Yakama": (-120.8, 46.25), "Colville": (-118.9, 48.35), "Nez Perce": (-116.6, 45.9), "Klamath": (-121.6, 42.75),
    "Fort Hall": (-112.5, 43.0), "Tohono O'odham": (-112.0, 32.15), "Apache\n(White Mtn, San Carlos)": (-110.1, 33.7),
    "Chiricahua": (-109.5, 31.85),
}
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
        draw_poly(ax, P(g), facecolor="#ffffff", edgecolor="#999999", linewidth=0.4, hatch="////")
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
    for label, ring in HOMELANDS.items():
        g = P(Polygon(ring))
        draw_poly(ax, g, facecolor="#fdf1e7", edgecolor="#7a3b12", linewidth=1.4, alpha=0.93)
        pt = g.representative_point()
        ax.text(pt.x, pt.y, label, ha="center", va="center", fontsize=7.5, style="italic", color="#7a3b12", weight="bold")
    for label, (lo, la) in HOMELAND_LABELS.items():
        x, y = albers(lo, la)
        ax.text(x, y, label, ha="center", va="center", fontsize=5.6, style="italic", color="#7a3b12",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="#7a3b12", lw=0.5, alpha=0.9))
    for label, lo, la in (("Utes' Slope\nand Parks", -108.0, 39.4), ("Nez Perce\n(Wallowa)", -117.2, 45.45)):
        x, y = albers(lo, la)
        ax.text(x, y, label, ha="center", va="center", fontsize=6.5, style="italic", color="#7a3b12", weight="bold",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.8))
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
    fig.text(0.02, 0.962, "CR-071 Part I, draft 4 (16 November 2026). Colours: the old members and territories the counties replace. "
             "Dotted grey: our timeline's county lines of 1887.\nHatched: ground in no county. "
             "Brown: large homelands, outside the 124 (outlines are sketches; boxed names have no agreed lines yet). "
             "Not shown: Alaska, a territory under the Northern Commission.\n"
             "Lines inside split counties are drawn by eye. MODEL and PROPOSED.", fontsize=9.5, va="top")
    handles = [plt.Rectangle((0, 0), 1, 1, fc=c, ec="#333333") for c in UNIT_COLOUR.values()]
    fig.legend(handles, list(UNIT_COLOUR), loc="lower right", bbox_to_anchor=(0.985, 0.03), fontsize=9, ncol=2,
               title="Old unit", frameon=True)
    out = HERE / "outputs" / "map_1887.png"
    fig.savefig(out)
    print("wrote", out, "| counties with no shape:", missing or "none", "| drawn:", len([n for n in merged if not merged[n].is_empty]))


if __name__ == "__main__":
    main()
