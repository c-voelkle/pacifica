"""Behavioral boundaries for linked findings and conservative comparison suggestions."""
from contextlib import redirect_stderr
from decimal import Decimal
from io import StringIO
from pathlib import Path
import unittest

from rdflib import Graph, Literal, Namespace, RDF
from consistency.validate_consistency import (AC, CV, HERE, PC, V, REPOSITORY,
                                              check_inputs, check_quotes, load_graph,
                                              main, query_views, validate_graph)

PILOT = REPOSITORY / 'outputs/aumakua-ontology-20261026'
AFTER = REPOSITORY / 'outputs/power-review-gold-ontology-20261026/after/review.ttl'
A = Namespace('urn:pacifica:consistency:aumakua-20261026:')
FG = Namespace('urn:pacifica:review:forward-gold-20261026:')
TEST = Namespace('urn:pacifica:test:consistency:')


class ConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = load_graph([PILOT / 'audit.ttl', AFTER])

    def setUp(self):
        self.graph = Graph()
        for triple in self.original:
            self.graph.add(triple)

    def copy_claim(self, source, target):
        for predicate, value in self.graph.predicate_objects(source):
            self.graph.add((target, predicate, value))

    def invalid(self):
        self.assertFalse(validate_graph(self.graph)[0])

    def candidate_pairs(self, view):
        return {(row['left'], row['right']) for row in query_views(self.graph, HERE)[view]}

    def has_pair(self, view, left, right):
        ordered = tuple(sorted((str(left), str(right))))
        return ordered in self.candidate_pairs(view)

    def test_linked_pilot_conforms_pins_sources_and_verifies_quotes(self):
        self.assertTrue(validate_graph(self.graph)[0])
        self.assertEqual(check_inputs(self.graph, repository=REPOSITORY,
                                      manifest_path=PILOT / 'input-manifest.json'), 13)
        self.assertEqual(check_quotes(self.graph, REPOSITORY), 11)
        self.assertEqual(len(set(self.graph.subjects(RDF.type, AC.Finding))), 5)

    def test_finding_requires_two_evidence_passages(self):
        self.graph.remove((A['AUM-4-8-001'], AC.passage, A['F001-right']))
        self.invalid()

    def test_lifecycle_cannot_replace_classification(self):
        self.graph.set((A['AUM-4-8-001'], AC.classification, CV.Open))
        self.invalid()

    def test_prose_snapshot_must_be_pinned_local_text(self):
        self.graph.set((A.Audit, AC.proseSnapshot, FG['D-H1']))
        self.invalid()

    def test_unrepresented_issue_is_valid_without_inventing_power_claim(self):
        finding = A['AUM-4-8-001']
        self.graph.remove((finding, AC.relatedClaim, None))
        self.graph.remove((finding, AC.claimLinkNote, None))
        self.assertTrue(validate_graph(self.graph)[0])
        self.graph.remove((finding, AC.claimGap, None))
        self.invalid()

    def test_related_claim_needs_real_claim_and_bounded_relevance(self):
        finding = A['AUM-4-8-001']
        self.graph.add((finding, AC.relatedClaim, TEST.nonexistent))
        self.invalid()
        self.graph.remove((finding, AC.relatedClaim, TEST.nonexistent))
        self.graph.remove((finding, AC.claimLinkNote, None))
        self.invalid()

    def test_resolution_requires_evidence(self):
        finding = A['AUM-4-8-001']
        self.graph.set((finding, AC.lifecycle, CV.Resolved))
        self.invalid()
        self.graph.add((finding, AC.resolutionEvidence, Literal('Test evidence reference; not a pilot resolution.')))
        self.assertTrue(validate_graph(self.graph)[0])

    def test_search_hit_cannot_substitute_for_direct_reading(self):
        self.graph.set((A['F001-left-coverage'], AC.readingMode, CV.SearchedOnly))
        self.invalid()

    def test_quotes_must_match_pinned_text_and_line_window(self):
        passage = A['F001-left']
        self.graph.set((passage, AC.quotation, Literal('An invented quotation not in this manuscript.')))
        with self.assertRaisesRegex(ValueError, 'Quotation not found'):
            check_quotes(self.graph, REPOSITORY)
        copied = Graph()
        for triple in self.original:
            copied.add(triple)
        self.graph = copied
        self.graph.set((passage, AC.startLine, Literal(1)))
        self.graph.set((passage, AC.endLine, Literal(1)))
        with self.assertRaisesRegex(ValueError, 'Quotation not found'):
            check_quotes(self.graph, REPOSITORY)

    def test_directly_read_unmapped_passages_remain_visible(self):
        views = query_views(self.graph, HERE)
        rows = views['read-passages-without-claim-mapping']
        self.assertEqual(len(rows), 10)
        self.assertNotIn(str(A.Sweep), {row['passage'] for row in rows})
        # Contextual relatedClaim links do not erase fine-grained extraction gaps.
        self.assertIn(str(A['F001-left']), {row['passage'] for row in rows})

    def test_overlapping_opposite_relations_suggest_a_comparison_only(self):
        self.copy_claim(FG.C01, TEST.opposite)
        old = self.graph.value(FG.C01, PC.truthValue)
        self.graph.set((TEST.opposite, PC.truthValue, Literal(not old.toPython())))
        before = set(self.graph)
        self.assertTrue(self.has_pair('candidate-relational-disagreements', FG.C01, TEST.opposite))
        self.assertEqual(set(self.graph), before)
        self.assertEqual(len(set(self.graph.subjects(RDF.type, AC.Finding))), 5)

    def test_quantity_difference_suggested_but_different_scopes_excluded(self):
        self.copy_claim(FG.Q02, TEST.quantity)
        value = self.graph.value(FG.Q02, PC.numericValue).toPython()
        self.graph.set((TEST.quantity, PC.numericValue, Literal(Decimal(value) + 1)))
        self.assertTrue(self.has_pair('candidate-quantity-differences', FG.Q02, TEST.quantity))
        changes = [
            (PC.case, TEST.otherCase),
            (PC.jurisdiction, TEST.otherJurisdiction),
            (PC.authorialStatus, V.Proposed),
            (PC.unit, Literal('a different currency')),
            (PC.accountingBasis, Literal('a different gross/net basis')),
            (PC.quantityKind, V.Stock),
        ]
        for predicate, replacement in changes:
            with self.subTest(predicate=predicate):
                saved = self.graph.value(TEST.quantity, predicate)
                self.graph.set((TEST.quantity, predicate, replacement))
                self.assertFalse(self.has_pair('candidate-quantity-differences', FG.Q02, TEST.quantity))
                self.graph.set((TEST.quantity, predicate, saved))
        self.graph.set((TEST.quantity, PC.startYear, Literal(2000)))
        self.graph.set((TEST.quantity, PC.endYear, Literal(2001)))
        self.assertFalse(self.has_pair('candidate-quantity-differences', FG.Q02, TEST.quantity))

    def test_relational_candidates_do_not_merge_objects_or_nonoverlapping_periods(self):
        self.copy_claim(FG.C01, TEST.opposite)
        old = self.graph.value(FG.C01, PC.truthValue)
        self.graph.set((TEST.opposite, PC.truthValue, Literal(not old.toPython())))
        original_object = self.graph.value(TEST.opposite, PC.object)
        self.graph.set((TEST.opposite, PC.object, TEST.differentObject))
        self.assertFalse(self.has_pair('candidate-relational-disagreements', FG.C01, TEST.opposite))
        self.graph.set((TEST.opposite, PC.object, original_object))
        self.graph.set((TEST.opposite, PC.startYear, Literal(2000)))
        self.graph.set((TEST.opposite, PC.endYear, Literal(2001)))
        self.assertFalse(self.has_pair('candidate-relational-disagreements', FG.C01, TEST.opposite))

    def test_unknown_value_is_not_a_numeric_disagreement(self):
        self.copy_claim(FG.Q02, TEST.unknown)
        self.graph.remove((TEST.unknown, PC.numericValue, None))
        self.graph.set((TEST.unknown, PC.valueState, V.Unknown))
        self.graph.add((TEST.unknown, PC.missingReason, Literal('Unavailable in this test.')))
        self.assertFalse(self.has_pair('candidate-quantity-differences', FG.Q02, TEST.unknown))

    def test_custom_input_is_required_and_old_pilot_cannot_pass_as_audit(self):
        with self.assertRaises(ValueError):
            load_graph([])
        errors = StringIO()
        with redirect_stderr(errors):
            result = main(['--data', str(AFTER), '--manifest', str(PILOT / 'input-manifest.json')])
        self.assertEqual(result, 1)
        self.assertIn('explicit consistency Audit', errors.getvalue())


if __name__ == '__main__':
    unittest.main()
