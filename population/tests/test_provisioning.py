"""Provisioning account tests. Run: python3 -m unittest discover -s population/tests -v"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import provisioning as pv  # noqa: E402


class Provisioning(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = pv.cfg()
        cls.base = pv.land_1929(cls.c)
        cls.pop = pv.residents()

    def test_states_close_on_the_census_total(self):
        irr = self.c["irrigation_1929"]
        west = sum(v for v in irr.values() if isinstance(v, int))
        other = 9392 + 67107 + 532617 + 71290 + 151787 + 450901 + 1573 + 798917  # the eight states outside the frontier
        self.assertEqual(west + other, self.c["irrigation_totals"]["acres"][-1])

    def test_cases_are_ordered_and_capped(self):
        top = pv.ceiling_area(self.c, self.base)
        for y in range(pv.FIRST, pv.LAST + 1):
            h, f, r = (pv.mouths(self.c, self.base, y, k, self.pop) for k in ("history", "farmers", "research"))
            self.assertLessEqual(h, f + 1)
            self.assertLessEqual(f, r + 1)
            self.assertLessEqual(pv.mouths(self.c, self.base, y, "research", self.pop, "canon"), r + 1)
            self.assertLessEqual(pv.acres(self.c, self.base, y, "farmers", self.pop)[0], top + 1)

    def test_yield_ladder_is_the_verified_series(self):
        y = self.c["yield_ladder"]
        self.assertEqual(len(y["bushels"]), 1975 - y["first_year"] + 1)
        self.assertAlmostEqual(sum(y["bushels"][5:35]) / 30, 19.15, delta=0.05)   # 1900-1929
        self.assertEqual(pv.ladder(self.c, 1915), 1.0)
        self.assertAlmostEqual(pv.ladder(self.c, 1960), 1.81, delta=0.03)

    def test_components_track_the_series_and_order_the_cases(self):
        for y in (1935, 1945, 1950, 1955, 1960, 1965, 1970):       # the split fits the verified series
            self.assertAlmostEqual(pv.research(self.c, y, "history") / pv.ladder(self.c, y), 1.0, delta=0.11)
        self.assertEqual(pv.research(self.c, 1880), 1.0)
        for y in range(1880, 1941, 5):
            h, cen, e = (pv.research(self.c, y, k) for k in ("history", "canon_central", "canon_earliest"))
            self.assertLessEqual(h, cen + 1e-9)
            self.assertLessEqual(cen, e + 1e-9)
            self.assertLessEqual(pv.research(self.c, y, nitrogen=0.0), cen + 1e-9)
        total = 1.0
        for item in self.c["yield_components"]["items"]:
            total *= item["gain"]
        self.assertAlmostEqual(pv.research(self.c, 1945, "canon_earliest"), total, places=6)

    def test_nitrogen_and_sea(self):
        self.assertEqual(pv.canon_farm_nitrogen(self.c, 1914), 0.0)
        self.assertAlmostEqual(pv.canon_farm_nitrogen(self.c, 1929), 45000)
        self.assertGreater(pv.nitrogen_needed(self.c, self.base, 1930, self.pop), 2e5)
        self.assertTrue(3e6 < pv.sea_mouths(self.c, 1932) < 6e6)

    def test_works_and_work_stock(self):
        top = pv.ceiling_area(self.c, self.base)
        last = 0.0
        for y in range(pv.FIRST, pv.LAST + 1):
            w = pv.works_limit(self.c, self.base, y)
            self.assertGreaterEqual(w, last)                         # works are never unbuilt
            self.assertLessEqual(pv.acres(self.c, self.base, y, "research", self.pop)[0], w + 1)
            self.assertLessEqual(pv.draft_share(self.c, y, "canon"), pv.draft_share(self.c, y, "history") + 1e-9)
            last = w
        self.assertAlmostEqual(pv.works_limit(self.c, self.base, 1890), self.base["area"])
        self.assertAlmostEqual(pv.works_limit(self.c, self.base, 1930), top)
        self.assertAlmostEqual(pv.draft_share(self.c, 1910, "history"), 88 / 325, delta=0.005)   # HSUS Da661-664

    def test_crop_never_exceeds_capacity_or_demand(self):
        for y in range(1880, pv.LAST + 1):
            f = pv.fields(self.c, self.base, y, self.pop)
            self.assertLessEqual(f["crop"], f["capacity"] + 1)
            self.assertLessEqual(f["crop"], f["demand"] + 1)
            self.assertLessEqual(f["free"], f["capacity"] + 1)
            self.assertLessEqual(f["capacity"], f["full"] + 1)
            self.assertLessEqual(f["used"], f["supply"] + 1)
            self.assertLessEqual(f["used"], f["asked"] + 1)
            self.assertAlmostEqual(f["from_chile"] + f["from_home"], f["used"], delta=1)
            self.assertLessEqual(f["from_chile"],
                                 self.c["nitrogen_supply"]["chile_share_max"] * pv.chile_nitrogen(self.c, y) + 1)
        self.assertEqual(pv.fields(self.c, self.base, 1899, self.pop)["used"], 0.0)

    def test_first_draft_is_recovered(self):
        c = pv.cfg()
        c["works"]["basis"] = ["irrigable_in_enterprises_1940"] * 3
        c["draft"].update(history_share=[0.0] * 5, canon_share=[0.0] * 4)
        base = pv.land_1929(c)
        self.assertAlmostEqual(pv.central(c, base, 1910, self.pop, "full") / self.pop[1910], 2.04, delta=0.01)
        self.assertAlmostEqual(pv.central(c, base, 1932, self.pop, "full") / self.pop[1932], 1.31, delta=0.01)

    def test_century_adds_up(self):
        cy = pv.century(self.c, self.base, self.pop)
        k = self.c["century"]
        self.assertAlmostEqual(cy["need"], pv.table(self.c, self.base, self.pop, 1930)["realm_100"])
        self.assertAlmostEqual(45 * k["acre_feet_per_km3"] / 1e6, 36.5, delta=0.05)          # 45 km3 in acre-feet
        top = cy["water"]["ceiling_in_law"]
        self.assertAlmostEqual(top["acres"], 45 * k["acre_feet_per_km3"] / k["acre_feet_per_acre"])
        self.assertAlmostEqual(cy["water"]["first_stage"]["mouths"] / top["mouths"], 20 / 45)
        plan = (cy["home"] + top["mouths"] + cy["asked"]) / (1 - k["diet_saving"])
        self.assertAlmostEqual(cy["plan"]["fed"], plan, delta=1)
        self.assertAlmostEqual(cy["gap"], cy["need"] - plan, delta=1)
        fed = [r["fed"] for r in cy["rows"]]
        self.assertEqual(fed, sorted(fed))
        for r in cy["rows"]:                                         # the fitted slowing does feed the century
            end = pv.project(self.pop[1930], pv.rate(lambda y: self.pop[y], 1930), r["slowing"], 100, 100)
            self.assertAlmostEqual(end / r["fed"], 1.0, places=4)
            self.assertLessEqual(pv.project(self.pop[1930], pv.rate(lambda y: self.pop[y], 1930),
                                            self.c["levers"]["g_end_julian"], r["passed"] - 1931, 100), r["fed"])
        self.assertAlmostEqual(sum(s["now"] for s in cy["sellers"]) / 1e6, 29.7, delta=0.5)   # the outline's "20-30 million"

    def test_projection_slows_and_matches_closed_form(self):
        p = pv.project(1.0, 0.04, 0.015, 100, 100)
        self.assertAlmostEqual(p, 2.718281828 ** 2.75, places=6)
        self.assertLess(pv.project(1.0, 0.04, 0.015, 100, 100), pv.project(1.0, 0.04, 0.04, 100, 100))
        self.assertAlmostEqual(pv.project(1.0, 0.04, 0.015, 110, 100) / p, 2.718281828 ** 0.15, places=6)

    def test_tables_slow_less_under_julian(self):
        self.assertEqual(pv.slowing(self.c, 1900), self.c["levers"]["g_end"])
        self.assertEqual(pv.slowing(self.c, 1910), self.c["levers"]["g_end_julian"])
        t = pv.table(self.c, self.base, self.pop, 1930)
        old = pv.table(self.c, self.base, self.pop, 1930, g_end=self.c["levers"]["g_end"])
        self.assertTrue(400e6 < old["realm_100"] + old["crown_100"] < 600e6)     # the author's half-billion
        self.assertGreater(t["realm_100"], old["realm_100"])

    def test_crown_is_counted_only_after_the_accession(self):
        self.assertEqual(pv.crown_people(self.c, 1907), 0.0)
        self.assertGreater(pv.crown_people(self.c, 1908), 8e6)
        self.assertEqual(pv.table(self.c, self.base, self.pop, 1900)["crown_100"], 0.0)


if __name__ == "__main__":
    unittest.main()
