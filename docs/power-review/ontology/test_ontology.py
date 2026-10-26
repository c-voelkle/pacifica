"""Behavioral checks for status, scope, evidence and power-review boundaries."""
from decimal import Decimal
from contextlib import redirect_stderr
from io import StringIO
import json
import tempfile
from pathlib import Path
import unittest

from rdflib import Graph, Literal, Namespace, RDF
from validate import (HERE, REPOSITORY, PC, V, check_inputs, checked_path,
                      load_graph, main, query_views, validate_graph)

GOLD = Namespace('urn:pacifica:review:gold-20261026:')
CT = Namespace('urn:pacifica:character:')
PROV = Namespace('http://www.w3.org/ns/prov#')


class ReviewOntologyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = load_graph()

    def setUp(self):
        self.graph = Graph()
        for triple in self.original:
            self.graph.add(triple)

    def assert_invalid(self, expected_message=None):
        conforms, _, report = validate_graph(self.graph)
        self.assertFalse(conforms)
        if expected_message:
            self.assertIn(expected_message, report)

    def test_pilot_conforms_and_input_bytes_are_pinned(self):
        self.assertTrue(validate_graph(self.graph)[0])
        self.assertEqual(check_inputs(self.graph), 6)

    def test_historical_support_cannot_replace_authorial_status(self):
        self.graph.set((GOLD.Cutoff1918, PC.authorialStatus, V.Supporting))
        self.assert_invalid()

    def test_unknown_quantity_cannot_have_a_zero_value(self):
        self.graph.add((GOLD.NetService, PC.numericValue, Literal(Decimal('0'))))
        self.assert_invalid()

    def test_known_zero_is_valid_and_different_from_missing(self):
        self.graph.set((GOLD.NetService, PC.valueState, V.Known))
        self.graph.remove((GOLD.NetService, PC.missingReason, None))
        self.graph.add((GOLD.NetService, PC.numericValue, Literal(Decimal('0'))))
        self.assertTrue(validate_graph(self.graph)[0])

    def test_false_relation_is_a_known_boolean_value(self):
        self.assertEqual(self.graph.value(GOLD.CrownNoPurse, PC.truthValue), Literal(False))
        self.assertEqual(self.graph.value(GOLD.CrownNoPurse, PC.valueState), V.Known)

    def test_quantity_requires_unit_and_accounting_basis(self):
        for predicate in (PC.unit, PC.accountingBasis):
            with self.subTest(predicate=predicate):
                saved = list(self.graph.triples((GOLD.GrossRoyalty, predicate, None)))
                self.graph.remove((GOLD.GrossRoyalty, predicate, None))
                self.assert_invalid()
                for triple in saved:
                    self.graph.add(triple)

    def test_control_requires_institutional_capacity_and_refusal_terms(self):
        for predicate in (PC.actingThrough, PC.refusalTerms):
            with self.subTest(predicate=predicate):
                saved = list(self.graph.triples((GOLD.Cutoff1918, predicate, None)))
                self.graph.remove((GOLD.Cutoff1918, predicate, None))
                self.assert_invalid()
                for triple in saved:
                    self.graph.add(triple)

    def test_instrument_and_instrument_gap_are_mutually_exclusive(self):
        self.graph.add((GOLD.Cutoff1918, PC.controlInstrument, GOLD.Settlement1914))
        self.assert_invalid()

    def test_unqualified_world_relationship_is_rejected(self):
        self.graph.add((CT['CT-JULIAN'], PC.commands, GOLD.HomeArmy))
        self.assert_invalid('Represent world relationships inside a dated, case-scoped Claim')

    def test_cross_case_mechanism_is_rejected(self):
        self.graph.set((GOLD.Accession, PC.case, GOLD.C))
        self.assert_invalid('A link may not silently mix claims from different cases')

    def test_exposition_does_not_become_a_power_improvement(self):
        self.graph.set((GOLD.ClarificationVerdict, PC.verdictBasis, V.WorldPower))
        self.graph.set((GOLD.ClarificationVerdict, PC.targetDimension, V.Implementation))
        self.assert_invalid('An exposition-only case cannot establish a world-power improvement')

    def test_unresolved_dependency_blocks_unconditional_endpoint_success(self):
        self.graph.set((GOLD.ServiceVerdict, PC.verdict, V.Improves))
        self.graph.set((GOLD.ServiceVerdict, PC.conditional, Literal(False)))
        self.assert_invalid('Unconditional power improvement has a declared provisional or unresolved dependency')

    def test_fiscal_dimension_does_not_become_a_power_dimension(self):
        self.graph.set((GOLD.LowerRateVerdict, PC.verdictBasis, V.WorldPower))
        self.assert_invalid("A world-power verdict must use the contract's power dimensions")

    def test_evidence_requires_a_locator_and_applicability_boundary(self):
        self.graph.remove((GOLD.H1, PC.locator, None))
        self.graph.remove((GOLD.MintAnalogy, PC.applicability, None))
        self.assert_invalid()

    def test_wrong_source_hash_is_detected_without_rewriting_inputs(self):
        self.graph.set((GOLD.Assessment, PC.sha256, Literal('0' * 64)))
        with self.assertRaisesRegex(ValueError, 'hash disagreement'):
            check_inputs(self.graph)

    def test_input_path_cannot_escape_repository(self):
        with self.assertRaisesRegex(ValueError, 'escapes the repository'):
            checked_path(REPOSITORY, '../outside.txt')

    def test_custom_review_replaces_the_pilot_instead_of_merging_it(self):
        with tempfile.TemporaryDirectory(prefix='review-data-', dir=REPOSITORY.parent) as temporary:
            root = Path(temporary)
            self.assertTrue(root.resolve().is_relative_to(REPOSITORY.parent.resolve()))
            dataset = root / 'new-review.ttl'
            dataset.write_text('''@prefix pc: <urn:pacifica:ontology:review:> .
@prefix v: <urn:pacifica:vocab:review:> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
<urn:test:only-entity> a pc:Entity ; rdfs:label "New review only" ; pc:entityKind v:Institution .
''', encoding='utf-8')
            graph = load_graph(data_paths=[dataset])
            self.assertEqual(len(set(graph.subjects(RDF.type, PC.Claim))), 0)
            self.assertNotIn((GOLD.Cutoff1918, RDF.type, PC.Claim), graph)
            self.assertTrue(validate_graph(graph)[0])

    def test_custom_review_cannot_silently_reuse_the_pilot_manifest(self):
        with redirect_stderr(StringIO()), self.assertRaises(SystemExit) as error:
            main(['--data', 'another-review.ttl'])
        self.assertEqual(error.exception.code, 2)

    def test_input_integrity_survives_lf_and_crlf_source_checkouts(self):
        manifest = json.loads((HERE / 'inputs/manifest.json').read_text(encoding='utf-8'))
        with tempfile.TemporaryDirectory(prefix='review-test-', dir=REPOSITORY.parent) as temporary:
            root = Path(temporary)
            self.assertTrue(root.resolve().is_relative_to(REPOSITORY.parent.resolve()))
            for endings in (b'\n', b'\r\n'):
                for relative, metadata in manifest['files'].items():
                    content = (REPOSITORY / relative).read_bytes()
                    if metadata['hash_basis'] == 'LFNormalizedText':
                        content = content.replace(b'\r\n', b'\n').replace(b'\n', endings)
                    target = root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(content)
                self.assertEqual(check_inputs(self.graph, repository=root), 6)
            target = root / 'docs/power-review/ontology/inputs/assessment.md'
            target.write_bytes(target.read_bytes() + b'changed')
            with self.assertRaisesRegex(ValueError, 'Pinned source bytes changed'):
                check_inputs(self.graph, repository=root)

    def test_queries_preserve_the_material_gaps_and_proposed_cutoff(self):
        views = query_views(self.graph)
        self.assertEqual(set(views), {'unresolved-links', 'control-boundaries',
                         'provisional-dependencies', 'quantities-and-gaps', 'evidence-boundaries'})
        self.assertEqual({row['link'] for row in views['unresolved-links']},
                         {str(GOLD[name]) for name in ('CollectionBridge', 'RegencyBridge', 'AccessionBridge', 'PrivateCompliance')})
        cutoff = next(row for row in views['control-boundaries'] if row['claim'] == str(GOLD.Cutoff1918))
        self.assertEqual(cutoff['status'], str(V.Proposed))
        self.assertIn('gap', cutoff)
        self.assertNotIn('instrument', cutoff)
        net = next(row for row in views['quantities-and-gaps'] if row['claim'] == str(GOLD.NetService))
        self.assertEqual(net['state'], str(V.Unmodeled))
        self.assertIn('reason', net)
        self.assertNotIn('value', net)
        analogy = next(row for row in views['evidence-boundaries'] if row['application'] == str(GOLD.MintAnalogy))
        self.assertEqual(analogy['historicalSupport'], str(V.Analogous))
        self.assertEqual(analogy['retrieval'], str(V.ReportedByDossier))


if __name__ == '__main__':
    unittest.main()
