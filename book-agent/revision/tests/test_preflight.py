"""Tests for preflight.py: each check on a small draft built from the template."""
import sys
import tempfile
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
import preflight  # noqa: E402

TEMPLATE = (BASE / "CR-TEMPLATE.md").read_text(encoding="utf-8")
STORY = ["first line", "<!-- CR-058: the Columbia compact and the halibut treaty -->",
         "**[APPROVED — CR-058]** A compact gives British Columbia half of the extra power.",
         "", "The Reserve Bank keeps the dollar convertible.", "last line"]


def draft(**replace: str) -> str:
    text = TEMPLATE
    for old, new in replace.items():
        assert old in text, old
        text = text.replace(old, new, 1)
    return text


def with_facts(json_block: str) -> str:
    return draft(**{"\n## Fact changes\n": "\n## Fact changes\n\n```json\n" + json_block + "\n```\n"})


class Headings(unittest.TestCase):
    def test_template_has_every_heading(self):
        self.assertEqual(preflight.check_headings(TEMPLATE), [])

    def test_renamed_heading_is_named_in_the_error(self):
        errors = preflight.check_headings(draft(**{"\n## Fact changes\n": "\n## H. Fact Changes (JSON)\n"}))
        self.assertEqual(len(errors), 1)
        self.assertIn("'## Fact changes'", errors[0])
        self.assertIn("H. Fact Changes (JSON)", errors[0])

    def test_heading_inside_a_fence_does_not_count(self):
        text = draft(**{"\n## Sources\n": "\n```\n## Sources\n```\n\n## References\n"})
        self.assertTrue(any("Sources" in e for e in preflight.check_headings(text)))


class FactChanges(unittest.TestCase):
    def check(self, text: str):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "CR-999.md"
            path.write_text(text, encoding="utf-8")
            return preflight.check_fact_changes(path, run_preview=False)

    def test_none_is_clean(self):
        errors, warnings, changes = self.check(TEMPLATE)
        self.assertEqual((errors, warnings, changes), ([], [], []))

    def test_fixed_year_is_an_error(self):
        block = '[{"add_event": {"id": "x-test", "year": 1932, "patterns": ["In (?P<year>1932) it happens"]}}]'
        errors, _, _ = self.check(with_facts(block))
        self.assertTrue(any("fixes its year to 1932" in e for e in errors), errors)

    def test_general_year_group_passes(self):
        block = ('[{"add_event": {"id": "x-test", "year": 1932, '
                 '"patterns": ["In \\\\*{0,2}(?P<year>1[89]\\\\d\\\\d)\\\\*{0,2} it happens"]}}]')
        errors, _, _ = self.check(with_facts(block))
        self.assertEqual(errors, [])

    def test_missing_year_group_and_bad_regex(self):
        block = ('[{"add_event": {"id": "x-a", "year": 1932, "patterns": ["In 1932 it happens"]}},'
                 ' {"add_forbidden": {"pattern": "unclosed (group", "message": "m", "kind": "fact"}}]')
        errors, _, _ = self.check(with_facts(block))
        self.assertTrue(any("no (?P<year>" in e for e in errors), errors)
        self.assertTrue(any("does not compile" in e for e in errors), errors)

    def test_stale_was_value_is_an_error(self):
        block = '[{"event": "seal-convention-signed", "set": {"year": 1887}, "was": {"year": 1800}}]'
        errors, _, _ = self.check(with_facts(block))
        self.assertTrue(errors)

    def test_new_person_missing_from_registry_warns(self):
        block = '[{"add_person": {"id": "CT-NOBODY-AT-ALL", "aliases": ["Nobody At All"], "born": 1870}}]'
        errors, warnings, _ = self.check(with_facts(block))
        self.assertEqual(errors, [])
        self.assertTrue(any("CT-NOBODY-AT-ALL" in w for w in warnings))

    def test_broken_section_reports_once(self):
        errors, _, _ = self.check(draft(**{"\n## Fact changes\n": "\n## Facts\n"}))
        self.assertEqual(len(errors), 1)


class Ledger(unittest.TestCase):
    def setUp(self):
        self.parties, self.commitments = preflight.ledger_ids()
        self.party = sorted(self.parties)[0]
        self.commitment = sorted(self.commitments)[0]

    def test_template_is_clean(self):
        self.assertEqual(preflight.check_ledger(TEMPLATE), ([], []))

    def test_new_party_collision(self):
        text = draft(**{"### New parties\n\nnone": f"### New parties\n\n- `{self.party}` — a new republic"})
        errors, _ = preflight.check_ledger(text)
        self.assertEqual(len(errors), 1)
        self.assertIn("already exists", errors[0])

    def test_free_party_id_passes(self):
        text = draft(**{"### New parties\n\nnone": "### New parties\n\n- `ZZ-NOT-A-PARTY` — a new republic"})
        self.assertEqual(preflight.check_ledger(text)[0], [])

    def test_amended_commitment_must_exist(self):
        text = draft(**{"### Amended commitments\n\nnone":
                        f"### Amended commitments\n\n- `{self.commitment}` — new parties\n- `C-1900-NOT-THERE` — x"})
        errors, _ = preflight.check_ledger(text)
        self.assertEqual(len(errors), 1)
        self.assertIn("C-1900-NOT-THERE", errors[0])

    def test_new_commitment_collision(self):
        text = draft(**{"### New commitments\n\nnone": f"### New commitments\n\n- `{self.commitment}` — x"})
        self.assertIn("already exists", preflight.check_ledger(text)[0][0])

    def test_missing_list_and_empty_list(self):
        errors, _ = preflight.check_ledger(draft(**{"\n### New parties\n": "\n### Parties\n"}))
        self.assertTrue(any("no '### New parties' list" in e for e in errors))
        errors, _ = preflight.check_ledger(draft(**{"### New commitments\n\nnone": "### New commitments\n\nto follow"}))
        self.assertTrue(any("neither ID bullets nor the word none" in e for e in errors))

    def test_unknown_commitment_in_prose_warns(self):
        text = draft(**{"**A1.**": "**A1.** As in `C-1900-NOT-THERE`."})
        errors, warnings = preflight.check_ledger(text)
        self.assertEqual(errors, [])
        self.assertTrue(any("C-1900-NOT-THERE" in w for w in warnings))


class Citations(unittest.TestCase):
    def check(self, sentence: str):
        return preflight.check_citations(draft(**{"**A1.**": "**A1.** " + sentence}), STORY)

    def test_anchor_on_the_line(self):
        self.assertEqual(self.check('See L3 ("a compact gives British Columbia half").'), [])

    def test_anchor_in_the_comment_above(self):
        self.assertEqual(self.check('See L3 ("the Columbia compact").'), [])

    def test_wrong_line_says_where_the_phrase_is(self):
        errors = self.check('See L5 ("a compact gives British Columbia half").')
        self.assertEqual(len(errors), 1)
        self.assertIn("is not on L5", errors[0])
        self.assertIn("on line 3", errors[0])

    def test_range(self):
        self.assertEqual(self.check('See L2–5 ("keeps the dollar convertible").'), [])

    def test_bare_citation_needs_one_anchor_in_the_draft(self):
        errors = self.check("See L3 and again L3.")
        self.assertEqual(len(errors), 1)
        self.assertIn("never given an anchor", errors[0])
        self.assertEqual(self.check('See L3, and later L3 ("the Columbia compact").'), [])

    def test_out_of_range_short_anchor_and_curly_quotes(self):
        self.assertIn("outside", self.check('See L99 ("the Columbia compact").')[0])
        self.assertIn("too short", self.check('See L3 ("half").')[0])
        self.assertEqual(self.check("See L3 (“the Columbia compact”)."), [])

    def test_fences_and_comments_are_not_read(self):
        self.assertEqual(self.check("see below\n\n```\nL99\n```\n<!-- L98 -->"), [])

    def test_template_cites_nothing(self):
        self.assertEqual(preflight.check_citations(TEMPLATE, STORY), [])


class Warnings(unittest.TestCase):
    def test_line_word_without_a_file(self):
        text = draft(**{"**A1.**": "**A1.** See `line 1562`, and line 36 of `CR-082.md`."})
        warnings = preflight.warn_line_words(text)
        self.assertEqual(len(warnings), 1)
        self.assertIn("L1562", warnings[0])

    def test_future_cr(self):
        text = draft(**{"**A1.**": "**A1.** Completed in CR-998; see CR-082."})
        warnings = preflight.warn_future_crs(text, "CR-999")
        self.assertEqual(len(warnings), 1)
        self.assertIn("CR-998", warnings[0])

    def test_self_hit_outside_impact_notes_only(self):
        changes = [{"add_forbidden": {"pattern": "fourth crown", "message": "m", "kind": "fact"}}]
        text = draft(**{"**A1.**": "**A1.** The Senate refuses a fourth crown.",
                        "- none yet\n\n## C.": "- 91: remove \"fourth crown\"\n\n## C."})
        warnings = preflight.warn_self_hits(text, changes)
        self.assertEqual(len(warnings), 1)


class WholeDraft(unittest.TestCase):
    def test_template_passes_end_to_end(self):
        errors, warnings = preflight.check_draft(BASE / "CR-TEMPLATE.md")
        self.assertEqual((errors, warnings), ([], []))


if __name__ == "__main__":
    unittest.main()
