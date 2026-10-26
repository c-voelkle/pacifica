"""Reproduce this task-owned review; all mutations stay in this directory."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
for script in ('diagnostic.py','build_review.py'):
    subprocess.run([sys.executable,'-X','utf8',str(OUT/script)],cwd=ROOT,check=True,capture_output=True)
relative=OUT.relative_to(ROOT)
cmd=[sys.executable,'-X','utf8','docs/power-review/ontology/validate.py','--data',str(relative/'review.ttl'),'--manifest',str(relative/'input-manifest.json'),'--repository','.','--json']
result=subprocess.run(cmd,cwd=ROOT,capture_output=True)
(OUT/'validation.json').write_bytes(result.stdout)
(OUT/'validation-stderr.txt').write_bytes(result.stderr)
if result.returncode:
    print(result.stderr.decode('utf-8',errors='replace'))
    raise SystemExit(result.returncode)
validated=json.loads(result.stdout)
for name,rows in validated['views'].items():
    with (OUT/(name+'.json')).open('w',encoding='utf-8',newline='\n') as f:
        f.write(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
manifest=json.loads((OUT/'run-manifest.json').read_text(encoding='utf-8'))
manifest['validation']={
    'command':'../.venv/Scripts/python.exe -X utf8 docs/power-review/ontology/validate.py --data outputs/power-review-gold-ontology-20261026/after/review.ttl --manifest outputs/power-review-gold-ontology-20261026/after/input-manifest.json --repository . --json',
    'exit_code':result.returncode,'summary':validated['summary'],
    'reviewed_views':list(validated['views']),
    'structural_limit':'Conformance does not validate truth, dependency completeness, causal sufficiency or authorial approval.'}
manifest['integration_friction']=[
    'Initial Windows cp1252 stdout failed printing Hawaiian characters after checks; documented -X utf8 invocation resolves output. No schema change needed.',
    'Task-owned calculation text uses LFNormalizedText input hashes for portable Git normalization; bundled inherited originals retain ExactBytes.']
manifest['reconciliation']={
    'unresolved_links_retained':[r['link'].rsplit(':',1)[-1] for r in validated['views']['unresolved-links']],
    'control_boundaries_inspected':'C21 explicit false authority; C35 proposed instrument; C06/C15/C18/C24 gaps retained.',
    'quantities_inspected':'Q06/Q07/Q10 unmodeled; Q09 inherited; no 1932 numeric power result.',
    'evidence_inspected':'ReportedByDossier and Unretrieved remain distinct; retrieval qualifications retained.',
    'comparison_inspected':'J01/J05 explanatory only; J03 bounded fiscal loss; J02/J04/J06/J07 conditional unresolved world effect; J07 compares retaining B with adopting R.'}
manifest['output_sha256_exact_bytes']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.iterdir() if p.is_file() and p.name!='run-manifest.json'}
with (OUT/'run-manifest.json').open('w',encoding='utf-8',newline='\n') as f:
    f.write(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(validated['summary'],indent=2))
