"""Re-execute the linked consistency pilot and record the skill/profile versions used."""
from pathlib import Path
import hashlib
from importlib.metadata import version
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
relative = HERE.relative_to(ROOT).as_posix()
command = [sys.executable, '-X', 'utf8', 'docs/power-review/ontology/consistency/validate_consistency.py',
           '--data', relative + '/audit.ttl',
           '--data', 'outputs/power-review-gold-ontology-20261026/after/review.ttl',
           '--manifest', relative + '/input-manifest.json', '--repository', '.']
result = subprocess.run(command, cwd=ROOT, capture_output=True)
(HERE / 'validation.json').write_bytes(result.stdout)
(HERE / 'validation-stderr.txt').write_bytes(result.stderr)
if result.returncode:
    sys.stderr.buffer.write(result.stderr)
    raise SystemExit(result.returncode)
summary = json.loads(result.stdout)['summary']
paths = sorted((ROOT / '.agents/skills/aumakua').rglob('*'))
paths += sorted((ROOT / 'docs/power-review/ontology/consistency').glob('*'))
paths += [ROOT / 'docs/power-review/ontology/ontology.ttl', ROOT / 'docs/power-review/ontology/vocabularies.ttl', ROOT / 'docs/power-review/ontology/shapes.ttl', ROOT / 'docs/power-review/ontology/validate.py', ROOT / 'docs/power-review/ontology/test_consistency.py']
pins = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest() for path in paths if path.is_file()}
outputs = {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest() for name in ('audit.ttl', 'input-manifest.json', 'validation.json', 'validation-stderr.txt', 'tests.txt')}
record = {'date': '2026-10-26', 'purpose': 'Retrospective integration of saved prose-first findings; no new blind detection trial.',
          'python_version': sys.version, 'dependencies': {name: version(name) for name in ('rdflib', 'pyshacl')},
          'command': ['python'] + command[1:], 'returncode': result.returncode,
          'skill_profile_sha256_lf_text': pins, 'output_sha256_exact': outputs,
          'summary': summary,
          'separate_test_run': {'command': "python -X utf8 -m unittest discover -s docs/power-review/ontology -p 'test_*.py' -v", 'result': '35 tests passed: 20 existing and 15 consistency tests.', 'log': 'tests.txt', 'note': 'Executed separately before this validation command; this script does not rerun tests.'}}
(HERE / 'execution.json').write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
print(json.dumps(summary, indent=2, ensure_ascii=False))
