"""Link the saved prose-first audit to a pinned existing Aegis graph; no new detection claim."""
from pathlib import Path
import hashlib
import json

from rdflib import Graph, Literal, Namespace, RDF, RDFS, XSD

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PC = Namespace('urn:pacifica:ontology:review:')
V = Namespace('urn:pacifica:vocab:review:')
AC = Namespace('urn:pacifica:ontology:consistency:')
CV = Namespace('urn:pacifica:vocab:consistency:')
PROV = Namespace('http://www.w3.org/ns/prov#')
FG = Namespace('urn:pacifica:review:forward-gold-20261026:')
A = Namespace('urn:pacifica:consistency:aumakua-20261026:')
BASE = 'outputs/power-review-gold-ontology-20261026/after'


def build():
    graph = Graph()
    for prefix, ns in [('pc', PC), ('v', V), ('ac', AC), ('cv', CV), ('prov', PROV), ('fg', FG), ('au', A)]:
        graph.bind(prefix, ns)
    manifest = json.loads((ROOT / BASE / 'input-manifest.json').read_text(encoding='utf-8'))
    manifest['review'] = 'aumakua-ontology-20261026'
    manifest['source_origin'] = 'Retrospective graph conversion of the saved independent Aumakua prose audit, with explicitly selected existing Aegis graph. No new blind prose pass or new research.'

    def literal(subject, predicate, value):
        graph.add((subject, predicate, Literal(value)))

    def document(identifier, path):
        raw = (ROOT / path).read_bytes()
        digest = hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest()
        manifest['files'][path] = {'sha256': digest, 'hash_basis': 'LFNormalizedText'}
        graph.add((identifier, RDF.type, PC.SourceDocument))
        literal(identifier, RDFS.label, path)
        graph.add((identifier, PC.sourceKind, V.ReviewSource))
        graph.add((identifier, PC.retrievalStatus, V.LocalPinned))
        graph.add((identifier, PC.hashBasis, V.LFNormalizedText))
        literal(identifier, PC.documentPath, path)
        literal(identifier, PC.sha256, digest)

    document(A.ProseSnapshot, 'outputs/aumakua-pilot-20261026/actual/review.md')
    document(A.InspectedGraph, BASE + '/review.ttl')
    graph.add((A.Audit, RDF.type, AC.Audit))
    literal(A.Audit, RDFS.label, 'Aumakua §§4–8: linked conversion of saved prose-first findings')
    literal(A.Audit, PC.sourceRevision, manifest['baseline_commit'])
    literal(A.Audit, AC.coverageNote, 'The saved reviewer read master §§4–8 continuously (lines 99–234), selected setup/later counterparts and approval/identity records. This conversion verifies paired quotations and graph links; it does not newly read or certify the whole story. Detailed original coverage remains in the saved prose review and its original manifest.')
    literal(A.Audit, AC.independenceNote, 'The original prose audit was independently completed before graph consultation and is pinned unchanged. This later conversion knowingly uses its five findings. It is not another independent detection trial; no new graph-suggested finding was adopted.')
    graph.add((A.Audit, AC.proseSnapshot, A.ProseSnapshot))
    graph.add((A.Audit, AC.inspectedGraph, A.InspectedGraph))
    graph.add((A.Audit, PROV.wasDerivedFrom, A.ProseSnapshot))

    def passage(identifier, line, quote):
        graph.add((identifier, RDF.type, PC.SourcePassage))
        graph.add((identifier, PROV.specializationOf, FG['D-master']))
        literal(identifier, RDFS.label, f'Master storyline line {line}')
        literal(identifier, PC.locator, f'line {line}')
        literal(identifier, AC.quotation, quote)
        graph.add((identifier, AC.startLine, Literal(line, datatype=XSD.integer)))
        graph.add((identifier, AC.endLine, Literal(line, datatype=XSD.integer)))
        coverage = A[str(identifier).split(':')[-1] + '-coverage']
        graph.add((coverage, RDF.type, AC.CoverageRecord))
        literal(coverage, RDFS.label, f'Directly read evidence at line {line}')
        graph.add((coverage, AC.audit, A.Audit))
        graph.add((coverage, AC.coveredPassage, identifier))
        graph.add((coverage, AC.readingMode, CV.DirectlyRead))
        literal(coverage, AC.extractionNote, 'This exact conflicting commitment has no declared complete Claim mapping. Broader contextual claim links are recorded on the finding separately; they do not fill this extraction gap.')

    issues = [
        ('001', 'Council of State report before creation', CV.IntegrationMismatch,
         (125, 'Elias reports the discovery formally, in confidence, to President Pico and the Council of State'),
         (183, 'In 1852 the assembly reorganizes government at Monterey, creating a Council of State'),
         'Same Californian body, spring 1848 report versus 1852 creation. The early report is in the locally PROPOSED CR-028 sequence; the reorganization has separate approval support.',
         'The named recipient appears before its stated creation; repeated character records do not establish a predecessor.',
         'A predecessor could explain it, but none is established in the inspected passages; do not silently invent one.',
         'Retain 1852 and choose an existing recipient, or explicitly establish and distinguish an intended predecessor; author choice required.',
         [FG.C01, FG.C06], 'C01 supplies proposed discovery context and C06 the 1852 administration context. Neither extracts the exact receiving-body/creation pair.'),
        ('002', 'Gold secrecy count', CV.Contradiction,
         (117, 'a find that only five people in the world know of'),
         (125, 'He tells only Pico, Castro and Alvarado'),
         'The October 1847 Mokelumne find by the December 1847 bargain; both passages locally PROPOSED. The full line-125 context explicitly names four discoverers before three informed leaders.',
         'Four distinct discoverers plus three informed leaders imply at least seven knowers, inconsistent with the stated global total of five.',
         'A narrower political circle could contain five, but the phrase in the world does not state that scope. Seven is a lower bound, not a newly established exhaustive total.',
         'Use a non-exhaustive formulation or ask the author to reconcile count and disclosure sequence; do not silently replace five with an exhaustive seven.',
         [FG.C01], 'C01 represents proposed discovery and secrecy, but contains no count or enumerated knowledge set.'),
        ('003', 'Unverifiable testimony becomes unqualified narration', CV.IntegrationMismatch,
         (145, 'Her father dies in the cholera of 1850, telling her to marry him.'),
         (73, 'impossible for the Chronicler to verify'),
         'Same pastor, Abigail and reported 1850 instruction. CR-022 retains unverifiable testimony; this is narrative stance, not uncertain settled kinship.',
         'Section 6 omits the attribution protecting the story in section 1. This is an integration/stance mismatch, not proof that the instruction was false.',
         'Implicit focalization through Abigail could reconcile it, but the synopsis supplies no such attribution and approval preserves uncertainty.',
         'Attribute the instruction to Abigail’s account while preserving uncertainty; do not decide what was actually said.',
         [], ''),
        ('004', 'Edo treaty party after common foreign relations', CV.MissingBridge,
         (175, 'In 1858, California and the Tokugawa government conclude the Treaty of Edo.'),
         (213, 'The common institutions control defense, the navy, customs, currency and external relations.'),
         '1858 treaty after the 1856 Confederation enters force; California as member state versus common external relations. Earlier pre-confederation contacts are separate.',
         'The text does not specify the capacity in which California concludes the treaty after external relations become common.',
         'Geographical shorthand or envoys acting with a common mandate could explain it. The inspected prose does not establish invalidity or sole treaty power.',
         'Clarify the treaty party and envoys’ capacity consistently with the intended constitutional arrangement.',
         [], ''),
        ('005', 'Assay office before public confirmation versus 1850 opening', CV.SuspectedContradiction,
         (125, 'an emergency mining decree, an assay office and a royalty are in force'),
         (131, 'A mint and assay office opens in San Francisco in 1850.'),
         'Public assay machinery required before October 1848 confirmation versus the San Francisco mint/office opening in 1850. Local proposed discovery timetable remains proposed.',
         'The sequence conflicts if these are the same public institution; the text does not establish that identity.',
         'An earlier temporary or differently located office is plausible but unstated. Private assays at Carquinez do not establish a public office.',
         'Distinguish an intended earlier office or align the opening condition; no earlier institution is invented here.',
         [FG.C01, FG.C03], 'C01 covers delayed public confirmation; C03 covers state receipts and mint context. Neither fully extracts assay-office identity and opening conditions.')
    ]
    for number, label, classification, left, right, scope, reasoning, alternative, repair, claims, link_note in issues:
        finding = A['AUM-4-8-' + number]
        graph.add((finding, RDF.type, AC.Finding))
        literal(finding, RDFS.label, label)
        graph.add((finding, AC.audit, A.Audit))
        graph.add((finding, AC.classification, classification))
        graph.add((finding, AC.lifecycle, CV.Open))
        graph.add((finding, AC.detectionBasis, CV.ProseFirst))
        graph.add((finding, PROV.wasDerivedFrom, A.ProseSnapshot))
        for suffix, (line, quote) in [('left', left), ('right', right)]:
            node = A[f'F{number}-{suffix}']
            passage(node, line, quote)
            graph.add((finding, AC.passage, node))
        for predicate, value in [(AC.normalizedScope, scope), (AC.reasoning, reasoning), (AC.alternativeReading, alternative), (AC.repairOption, repair)]:
            literal(finding, predicate, value)
        literal(finding, AC.claimGap, 'The exact commitments producing this consistency issue are not fully represented in the selected power-review graph. Source-passage evidence remains primary.')
        for claim in claims:
            graph.add((finding, AC.relatedClaim, claim))
        if claims:
            literal(finding, AC.claimLinkNote, link_note)

    literal(A['F002-right'], AC.quotation, 'he and Caleb travel through the Stanislaus and Mokelumne drainages with an experienced Sonoran placer miner and a Miwok guide')

    # Coverage of the continuous sweep, separate from the ten evidence fragments.
    graph.add((A.Sweep, RDF.type, PC.SourcePassage))
    graph.add((A.Sweep, PROV.specializationOf, FG['D-master']))
    literal(A.Sweep, RDFS.label, 'Original independent sweep: master §§4–8')
    literal(A.Sweep, PC.locator, 'sections 4–8, lines 99–234')
    graph.add((A.SweepCoverage, RDF.type, AC.CoverageRecord))
    literal(A.SweepCoverage, RDFS.label, 'Original continuous sweep coverage')
    graph.add((A.SweepCoverage, AC.audit, A.Audit))
    graph.add((A.SweepCoverage, AC.coveredPassage, A.Sweep))
    graph.add((A.SweepCoverage, AC.readingMode, CV.DirectlyRead))
    for claim in [FG.C01, FG.C02, FG.C03, FG.C04, FG.C05, FG.C06, FG.C07]:
        graph.add((A.SweepCoverage, AC.mappedClaim, claim))
    literal(A.SweepCoverage, AC.extractionNote, 'Selected existing Claims extract some power propositions from this span, not all commitments. Fine-grained consistency evidence remains explicitly unmapped; original manifest records additional partial readings and exclusions.')
    graph.serialize(HERE / 'audit.ttl', format='turtle', encoding='utf-8')
    (HERE / 'input-manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'finding_records': 5, 'coverage_records': 11, 'new_graph_suggested_detections': 0, 'source': 'saved prose-first review'}))


if __name__ == '__main__':
    build()
