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
            h, f, t = (pv.mouths(self.c, self.base, y, k, self.pop) for k in pv.CASES)
            self.assertLessEqual(h, f + 1)
            self.assertLessEqual(f, t + 1)
            self.assertLessEqual(pv.acres(self.c, self.base, y, "farmers", self.pop)[0], top + 1)

    def test_projection_slows_and_matches_closed_form(self):
        p = pv.project(1.0, 0.04, 0.015, 100, 100)
        self.assertAlmostEqual(p, 2.718281828 ** 2.75, places=6)
        self.assertLess(pv.project(1.0, 0.04, 0.015, 100, 100), pv.project(1.0, 0.04, 0.04, 100, 100))
        self.assertAlmostEqual(pv.project(1.0, 0.04, 0.015, 110, 100) / p, 2.718281828 ** 0.15, places=6)

    def test_table_of_1930_is_about_half_a_billion(self):
        t = pv.table(self.c, self.base, self.pop, 1930)
        self.assertTrue(400e6 < t["realm_100"] + t["crown_100"] < 600e6)

    def test_crown_is_counted_only_after_the_accession(self):
        self.assertEqual(pv.crown_people(self.c, 1907), 0.0)
        self.assertGreater(pv.crown_people(self.c, 1908), 8e6)
        self.assertEqual(pv.table(self.c, self.base, self.pop, 1900)["crown_100"], 0.0)


if __name__ == "__main__":
    unittest.main()
