"""Deterministic dramatic views and bounded open exploration, without invented motives."""
import hashlib
import json
from pathlib import Path

from ontology import ENGINE_VERSION, StoryBookmark, StoryCandidate


def candidate(s, h):
    events = [e for e in h.events if e['kind'] != 'state']
    actions = {e['action'] for e in events}
    decisions = h.semantics.get('decisions', [])
    assurance = h.semantics.get('commitments', [])
    status = assurance[0]['status'] if assurance else 'not_made'
    mediator = s.actors[s.execution.roles['mediator']].name
    executive = s.actors[s.execution.roles['executive']].name
    rescued = h.measures['june_payments_met']
    concord = h.measures['concord_status_end']
    if status == 'breached':
        title = 'A broken assurance reaches the negotiating table' if 'assurance_breach_disclosed' in actions else 'A private breach costs a mediator'
        goal = 'Secure mediation while retaining executive discretion.'
        obstacle = 'The offered settlement does not contain the oversight terms previously promised.'
        choice = 'Preserve the requested terms instead of adding the assurance terms.'
        sacrifice = 'The recipient withholds cooperation under the declared assurance rule.'
        next_dilemma = 'Offer the missing oversight terms to regain mediation, or continue without that support?'
    elif status == 'honoured':
        title = 'Keeping an assurance changes the price of settlement'
        goal = 'Fulfil the settlement assurance and obtain mediation.'
        obstacle = 'Oversight terms constrain the executive’s proposed settlement.'
        choice = 'Include the promised oversight terms in the actual offer.'
        sacrifice = 'The actual offer includes the declared oversight conditions.'
        next_dilemma = 'Seek consent under the offered oversight, or revise the terms and risk a breach?'
    elif rescued and concord != 'consented':
        title = 'A successful rescue leaves the constitutional bargain unresolved'
        goal = 'Fund the rescue and pursue the selected consent policy.'
        obstacle = 'Financial rescue does not supply legislative consent.'
        choice = f"Follow {h.levers['consent_path'].replace('_', ' ')}."
        sacrifice = None
        next_dilemma = 'Offer different terms or accept the political limits of the rescue?'
    elif not rescued:
        title = 'The financing deadline defeats the rescue offer'
        goal = 'Meet the scheduled foreign payments.'
        obstacle = 'Available financing or prior acceptance is insufficient at the deadline.'
        choice = 'The independent government selects a response to the failed rescue.'
        sacrifice = None
        next_dilemma = 'Which supported alternative protects the cabinet, and what cooperation remains possible?'
    else:
        title = 'A rescue becomes a contested institutional settlement'
        goal = 'Turn accepted financing into an agreed Concord.'
        obstacle = 'Legislative authority and financing are separate decisions.'
        choice = 'The recorded actors negotiate the offered settlement under their own rules.'
        sacrifice = None
        next_dilemma = 'Which obligations and oversight conditions now constrain the next commitment?'
    consequence = f"Japan: {h.measures['japan_path'].replace('_', ' ')}; Concord: {concord}; constitutional case: {h.measures['monterey_case_end']}."
    selected_actions = {'make_assurance', 'offer_concessions', 'review_assurance', 'settlement_role', 'treaty_consent', 'alternative_if_refused'}
    supports = [e['id'] for e in events if e['action'] in selected_actions | {'assurance_breach_disclosed', 'payments_met', 'payments_short', 'case_mooted', 'conditional_ratification_lapses'}]
    signature = [status, h.measures['japan_path'], concord, h.measures['monterey_case_end']]
    signature += [f"{e['actor']}:{e['action']}:{json.loads(e['reason']).get('choice', json.loads(e['reason']).get('vote', ''))}"
                  for e in events if e['action'] in selected_actions]
    identity = hashlib.sha256(json.dumps([h.scenario_hash, h.seed, h.levers, h.branch], sort_keys=True).encode()).hexdigest()[:20]
    return StoryCandidate(id=identity, world=h.world, title=title, focal_actor=executive,
        goal=goal, obstacle=obstacle, choice=choice, sacrifice=sacrifice,
        consequence=consequence, next_dilemma=next_dilemma, support_refs=supports,
        decision_refs=[d['id'] for d in decisions if d['action'] in selected_actions],
        causal_signature=signature, claim_basis='mechanical_consequence' if h.branch else 'actor_generated',
        assumption_refs=['scenario:/drama', 'scenario:/execution'],
        element_statuses=dict(goal='supported', choice='supported', consequence='supported',
                              sacrifice='supported' if sacrifice else 'not_assessed', next_dilemma='not_assessed'))


def select(s, histories, limit=5, condition='All histories'):
    """One representative per causal signature first; no strategic-success pruning."""
    predicates = {'All histories': lambda h: True,
                  'Rescue without consent': lambda h: h.measures['june_payments_met'] and h.measures['concord_status_end'] != 'consented',
                  'Broken assurance': lambda h: any(c['status'] == 'breached' for c in h.semantics.get('commitments', [])),
                  'Disclosed breach': lambda h: any(e['action'] == 'assurance_breach_disclosed' for e in h.events),
                  'Financial failure': lambda h: not h.measures['june_payments_met']}
    if condition not in predicates:
        raise ValueError('Unsupported narrative filter')
    unique = {}
    for h in histories:
        if not predicates[condition](h):
            continue
        story = candidate(s, h)
        signature = tuple(story.causal_signature)
        unique.setdefault(signature, (h, story))
    # Inspect the whole evaluated population; early policies must not crowd out
    # later relational plots. Reserve representatives across assurance/disclosure strata.
    chosen, strata = [], set()
    remaining = list(unique.values())
    for h, story in remaining:
        stratum = (story.causal_signature[0], any('disclose_breach' in x for x in story.causal_signature))
        if stratum not in strata and len(chosen) < limit:
            chosen.append((h, story))
            strata.add(stratum)
    while len(chosen) < min(limit, len(remaining)):
        selected_ids = {c.id for _, c in chosen}
        available = [(h, c) for h, c in remaining if c.id not in selected_ids]
        def distance(item):
            signature = set(item[1].causal_signature)
            return min(1 - len(signature & set(c.causal_signature)) / max(1, len(signature | set(c.causal_signature)))
                       for _, c in chosen)
        chosen.append(max(available, key=distance))
    return chosen


def explore(s, count=100, levers=None):
    """Enumerate a declared policy family; equal world numbers, all outcomes retained."""
    from model import batch, chosen
    if type(count) is not int or not 1 <= count <= 100:
        raise ValueError('Open exploration supports 1–100 external worlds per policy')
    controls = chosen(s, levers)
    terms = [controls['concessions_1928'], [], s.drama.assurance_terms]
    unique_terms = list({tuple(t): list(t) for t in terms}.values())
    settings = [dict(controls, assurance_strategy=strategy, commitment_priority=priority, concessions_1928=terms)
                for strategy in ('none', 'private', 'public')
                for priority in ('honour_assurance', 'preserve_discretion') for terms in unique_terms]
    histories = []
    for policy in settings:
        histories.extend(batch(s, count, policy))
    return dict(histories=histories, proposals=len(settings), root_worlds=count,
                evaluations=len(histories), selection='bounded causal representatives before strategic pruning')


def bookmark(s, h, rationale):
    story = candidate(s, h)
    return StoryBookmark(schema_version='timeline-lab-bookmark/0.2', engine_version=ENGINE_VERSION,
                         id=story.id, rationale=rationale, candidate=story, history=h.export(s))


def save_bookmark(record, directory=None):
    root = Path(__file__).resolve().parent / 'exports' / 'bookmarks'
    directory = Path(directory).resolve() if directory else root
    if not directory.is_relative_to(root):
        raise ValueError('Bookmarks must be saved under timeline-lab/exports/bookmarks')
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f'{record.id}.json'
    payload = json.dumps(record.model_dump(), ensure_ascii=False, indent=2, allow_nan=False)
    if path.exists():
        if path.read_text(encoding='utf-8') != payload:
            raise ValueError('Bookmark already exists with different rationale; download the new bundle separately')
        return path
    with path.open('x', encoding='utf-8') as stream:
        stream.write(payload)
    return path


def replay_bookmark(payload):
    from model import Scenario, validate, simulate
    record = StoryBookmark.model_validate(payload)
    stored = record.history
    s = validate(Scenario.model_validate(stored['scenario']))
    if s.digest != stored['scenario_hash']:
        raise ValueError('Bookmark scenario hash does not match its inputs')
    h = simulate(s, stored['world'], stored['levers'], stored['seed'], stored['branch'])
    # JSON round-trips procedure tuples as lists. Compare portable evidence,
    # while deterministic runtime reconstruction retains its native state.
    expected = json.loads(json.dumps(h.export(s), allow_nan=False))
    if (h.events != stored['events'] or h.measures != stored['measures']
            or candidate(s, h).id != record.id or candidate(s, h) != record.candidate
            or stored.get('engine_version') != ENGINE_VERSION
            or any(stored.get(key) != expected[key] for key in ('semantics', 'ontology', 'entities', 'metric_samples', 'story'))):
        raise ValueError('Bookmark replay differs from saved evidence')
    return s, h, record
