"""Offline SHACL validation, local input integrity and named SPARQL views."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

from pyshacl import validate
from rdflib import Graph, Namespace, RDF

HERE = Path(__file__).resolve().parent
REPOSITORY = HERE.parents[2]
PC = Namespace('urn:pacifica:ontology:review:')
V = Namespace('urn:pacifica:vocab:review:')
PROV = Namespace('http://www.w3.org/ns/prov#')


def load_graph(directory: Path = HERE) -> Graph:
    graph = Graph()
    for filename in ('ontology.ttl', 'vocabularies.ttl', 'gold-review.ttl'):
        graph.parse(directory / filename, format='turtle')
    return graph


def validate_graph(graph: Graph, directory: Path = HERE):
    shapes = Graph().parse(directory / 'shapes.ttl', format='turtle')
    # No imports, inference, advanced rule execution or network retrieval.
    return validate(graph, shacl_graph=shapes, inference='none', advanced=False,
                    do_owl_imports=False, inplace=False, allow_warnings=False)


def checked_path(repository: Path, relative: str) -> Path:
    candidate = (repository / relative).resolve()
    if not candidate.is_relative_to(repository.resolve()):
        raise ValueError(f'Input path escapes the repository: {relative}')
    return candidate


def check_inputs(graph: Graph, directory: Path = HERE, repository: Path = REPOSITORY) -> int:
    manifest = json.loads((directory / 'inputs/manifest.json').read_text(encoding='utf-8'))
    declared = manifest['files']
    recorded = {}
    for doc in graph.subjects(PC.retrievalStatus, V.LocalPinned):
        path = str(graph.value(doc, PC.documentPath))
        digest = str(graph.value(doc, PC.sha256))
        if path in recorded:
            raise ValueError(f'Duplicate local source path: {path}')
        recorded[path] = digest
        basis = str(graph.value(doc, PC.hashBasis)).removeprefix(str(V))
        if path not in declared or digest != declared[path]['sha256'] or basis != declared[path]['hash_basis']:
            raise ValueError(f'RDF/manifest hash disagreement: {path}')
        content = checked_path(repository, path).read_bytes()
        if basis == 'LFNormalizedText':
            content = content.replace(b'\r\n', b'\n')
        elif basis != 'ExactBytes':
            raise ValueError(f'Unsupported source hash basis: {basis}')
        actual = hashlib.sha256(content).hexdigest()
        if actual != digest:
            raise ValueError(f'Pinned source bytes changed: {path}')
    if set(recorded) != set(declared):
        raise ValueError('Manifest and RDF list different local inputs')
    registry = json.loads((repository / 'book-agent/revision/character_registry.json').read_text(encoding='utf-8'))
    ids = {person['id'] for person in registry['people']}
    for entity, identity in graph.subject_objects(PC.registryId):
        if str(identity) not in ids or str(entity) != 'urn:pacifica:character:' + str(identity):
            raise ValueError(f'Unrecognized or inconsistent character identity: {identity}')
    return len(recorded)


def named_queries(directory: Path = HERE) -> dict[str, str]:
    contents = (directory / 'queries.rq').read_text(encoding='utf-8')
    parts = re.split(r'^# query: ([a-z-]+)\s*$', contents, flags=re.MULTILINE)
    queries = dict(zip(parts[1::2], parts[2::2]))
    if not queries or len(queries) != (len(parts) - 1) // 2:
        raise ValueError('Missing or duplicate named queries')
    return queries


def query_views(graph: Graph, directory: Path = HERE) -> dict[str, list[dict]]:
    views = {}
    for name, query in named_queries(directory).items():
        result = graph.query(query)
        if result.type != 'SELECT':
            raise ValueError(f'Only SELECT views are supported: {name}')
        views[name] = [{str(key): str(value) for key, value in row.asdict().items()}
                       for row in result]
    return views


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true', help='Print validated query views as JSON')
    args = parser.parse_args(argv)
    try:
        graph = load_graph()
        conforms, _, report = validate_graph(graph)
        if not conforms:
            print(report, file=sys.stderr)
            return 1
        sources = check_inputs(graph)
        views = query_views(graph)
    except Exception as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        return 1
    summary = {'conforms': True, 'local_inputs_verified': sources,
               'review_triples': len(Graph().parse(HERE / 'gold-review.ttl', format='turtle')),
               'record_counts': {kind: len(set(graph.subjects(RDF.type, PC[kind])))
                                 for kind in ('Claim', 'MechanismLink', 'EvidenceApplication', 'ComparisonCase', 'Judgment')},
               'query_row_counts': {name: len(rows) for name, rows in views.items()}}
    print(json.dumps({'summary': summary, 'views': views} if args.json else summary,
                     indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
