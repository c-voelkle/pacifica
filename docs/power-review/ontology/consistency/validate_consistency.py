"""Validate an explicit Aumakua graph, verify quotes/inputs, and run suggestion views."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

from pyshacl import validate
from rdflib import Graph, Namespace, RDF

HERE = Path(__file__).resolve().parent
CORE = HERE.parent
sys.path.insert(0, str(CORE))
from validate import PC, V, PROV, REPOSITORY, check_inputs, checked_path, load_graph as core_graph, query_views

AC = Namespace('urn:pacifica:ontology:consistency:')
CV = Namespace('urn:pacifica:vocab:consistency:')


def load_graph(data_paths: list[Path]) -> Graph:
    if not data_paths:
        raise ValueError('Explicit audit data is required; no old pilot is loaded')
    graph = core_graph(data_paths=data_paths)
    return graph.parse(HERE / 'ontology.ttl', format='turtle')


def validate_graph(graph: Graph):
    shapes = Graph().parse(CORE / 'shapes.ttl', format='turtle')
    shapes.parse(HERE / 'shapes.ttl', format='turtle')
    return validate(graph, shacl_graph=shapes, inference='none', advanced=False,
                    do_owl_imports=False, inplace=False, allow_warnings=False)


def check_quotes(graph: Graph, repository: Path) -> int:
    count = 0
    for passage in set(graph.objects(None, AC.passage)):
        doc = graph.value(passage, PROV.specializationOf)
        if graph.value(doc, PC.retrievalStatus) != V.LocalPinned:
            raise ValueError(f'Finding passage must have pinned local text: {passage}')
        path = checked_path(repository, str(graph.value(doc, PC.documentPath)))
        text = path.read_text(encoding='utf-8-sig').replace('\r\n', '\n')
        start, end = graph.value(passage, AC.startLine), graph.value(passage, AC.endLine)
        if (start is None) != (end is None):
            raise ValueError(f'Incomplete quote line window: {passage}')
        if start is not None:
            lines = text.splitlines()
            if not 1 <= int(start) <= int(end) <= len(lines):
                raise ValueError(f'Quote line window out of bounds: {passage}')
            text = '\n'.join(lines[int(start) - 1:int(end)])
        quotes = list(graph.objects(passage, AC.quotation))
        if not quotes or any(not str(quote) or str(quote) not in text for quote in quotes):
            raise ValueError(f'Quotation not found in pinned passage window: {passage}')
        count += len(quotes)
    return count


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', action='append', type=Path, required=True,
                        help='Audit Turtle, then any explicitly selected existing review fragments')
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--repository', type=Path, default=REPOSITORY)
    args = parser.parse_args(argv)
    try:
        graph = load_graph(args.data)
        if not any(graph.subjects(RDF.type, AC.Audit)):
            raise ValueError('At least one explicit consistency Audit is required')
        conforms, _, report = validate_graph(graph)
        if not conforms:
            raise ValueError(report)
        sources = check_inputs(graph, repository=args.repository, manifest_path=args.manifest)
        quotes = check_quotes(graph, args.repository)
        views = query_views(graph, HERE)
    except Exception as error:
        print(f'Consistency validation failed: {error}', file=sys.stderr)
        return 1
    summary = {'conforms': True, 'local_inputs_verified': sources, 'quotations_verified': quotes,
               'audits': len(set(graph.subjects(RDF.type, AC.Audit))),
               'findings': len(set(graph.subjects(RDF.type, AC.Finding))),
               'coverage_records': len(set(graph.subjects(RDF.type, AC.CoverageRecord))),
               'query_row_counts': {name: len(rows) for name, rows in views.items()},
               'data_sha256_exact': {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in args.data},
               'limit': 'Candidate rows are suggestions; conformance is not consistency or coverage certification.'}
    print(json.dumps({'summary': summary, 'views': views}, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
