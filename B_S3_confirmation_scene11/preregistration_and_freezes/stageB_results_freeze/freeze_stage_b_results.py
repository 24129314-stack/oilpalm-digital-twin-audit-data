"""Freeze H4177 stage-B results: SHA256 of every evidence file (read only; nothing modified)."""
import datetime, hashlib, json
from pathlib import Path
W = Path('/workspace'); R = W / 'oilpalm_resume_20261013'; OUT = Path(__file__).resolve().parent
def sha(p):
    with open(p, 'rb') as f: return hashlib.file_digest(f, 'sha256').hexdigest()
roots = sorted((R / 'experiments').glob('H41772*')) + sorted((R / 'evidence').glob('H41772*')) + sorted((R / 'raw').glob('H41772*')) + \
        [R / 'formal_confirmation/H4177_STAGE_B', R / 'formal_confirmation/H4177_STAGE_B_AMEND01', R / 'CURRENT_RESUME_LEDGER.json', R / 'CURRENT_RESUME_LEDGER.csv']
files = {}
for r in roots:
    if r == OUT: continue
    for q in ([r] if r.is_file() else sorted(r.rglob('*'))):
        if q.is_file() and not q.is_symlink() and '__pycache__' not in q.parts:
            files[str(q.relative_to(W))] = dict(sha256=sha(q), bytes=q.stat().st_size)
doc = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), kind='H4177_stage_B_results_freeze', queue_done='2026-11-02T08:36:55Z',
           note='frozen after QUEUE_DONE; no file modified; no further stage-B runs; stage C not started; no new development round',
           file_count=len(files), total_bytes=sum(v['bytes'] for v in files.values()), files=files)
(OUT / 'STAGE_B_RESULTS_FREEZE.json').write_text(json.dumps(doc, ensure_ascii=False, indent=1))
s = sha(OUT / 'STAGE_B_RESULTS_FREEZE.json'); (OUT / 'STAGE_B_RESULTS_FREEZE.sha256').write_text(s + '  STAGE_B_RESULTS_FREEZE.json\n')
print(len(files), doc['total_bytes'], s)
