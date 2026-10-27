import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import ledger  # noqa: E402

STORY = ledger.Story([
    "## 3. A section",
    "Plain text. The treaty binds both for ten years. **[PROPOSED — CR-099]** A lease of the bay runs fifty years.",
    "## 4. Another",
    "**[APPROVED — CR-098]** The office ends with its holder.",
])

BASE = {
    "party": [{"id": "A", "name": "A"}, {"id": "B", "name": "B"}],
    "person": [{"id": "P1", "name": "Person One", "died": 1900}],
}


def entry(**kw):
    c = {"id": "C-1", "name": "Treaty", "kind": "treaty", "parties": ["A", "B"], "from": 1890,
         "status": "CANON", "section": 3, "quote": "The treaty binds both for ten years."}
    c.update(kw)
    return c


def ledger_with(*cs):
    return dict(BASE, commitment=list(cs))


class Check(unittest.TestCase):
    def errs(self, *cs):
        return ledger.check(ledger_with(*cs), STORY)

    def test_valid_entry_passes(self):
        self.assertEqual(self.errs(entry()), [])

    def test_quote_must_be_in_storyline(self):
        self.assertTrue(any("quote not found" in e for e in self.errs(entry(quote="An invented clause."))))

    def test_label_in_force_at_quote(self):
        c = entry(quote="A lease of the bay runs fifty years.", status="CANON")
        self.assertTrue(any("label at the quote is PROPOSED" in e for e in self.errs(c)))
        self.assertEqual(self.errs(dict(c, status="PROPOSED")), [])
        self.assertEqual(self.errs(dict(c, label_note="scope")), [])

    def test_section_must_match(self):
        self.assertTrue(any("§3, entry says §4" in e for e in self.errs(entry(section=4))))

    def test_term_and_renewals_consistent(self):
        self.assertTrue(any("term_years" in e for e in self.errs(entry(until=1900, term_years=5))))
        self.assertTrue(any("renewal 1910 after until" in e for e in self.errs(entry(until=1900, renewals=[1910]))))

    def test_parties_and_people_declared(self):
        self.assertTrue(any("undeclared party" in e for e in self.errs(entry(parties=["A", "Z"]))))
        self.assertTrue(any("not in canon_facts" in e for e in self.errs(entry(lapses_on_death=["NOBODY"]))))

    def test_lapse_before_start_is_an_error(self):
        self.assertTrue(any("before it starts" in e for e in self.errs(entry(**{"from": 1905, "lapses_on_death": ["P1"]}))))


class Queries(unittest.TestCase):
    L = ledger_with(
        entry(id="C-T", until=1900, renewals=[1895]),
        entry(id="C-O", name="Office", kind="office", lapses_on_death=["P1"], holder="P1"),
        entry(id="C-E", name="Ended", **{"from": 1880}, ended=1885, ended_by="war"),
    )

    def test_in_force(self):
        self.assertEqual({c["id"] for c in ledger.at(self.L, 1892)}, {"C-T", "C-O"})
        self.assertEqual({c["id"] for c in ledger.at(self.L, 1901)}, set())
        self.assertEqual({c["id"] for c in ledger.at(self.L, 1883)}, {"C-E"})

    def test_schedule(self):
        s = ledger.schedule(self.L, 1880, 1905)
        self.assertIn(1895, s)
        self.assertTrue(any("lapses on the death of Person One" in x for x in s[1900]))
        self.assertTrue(any("ended" in x and "war" in x for x in s[1885]))

    def test_if_dies(self):
        r = ledger.if_dies(self.L, "P1")
        self.assertEqual([c["id"] for c in r["lapse"]], ["C-O"])


class RealLedger(unittest.TestCase):
    def test_canon_ledger_checks_clean(self):
        led = ledger.load_ledger()
        self.assertEqual(ledger.check(led), [])
        self.assertGreater(len(led["commitment"]), 0)


if __name__ == "__main__":
    unittest.main()
