"""H4177 stage-B launcher for hold / first-handoff units of the frozen B version (scene 11).

Every launch is a counted start: PREREGISTRATION -> LAUNCH_LEDGER -> run -> raw
sealed into RAW_ORIGINAL_BYTES.tar.xz with streamed SHA readback -> DEV_RESULT.
Nominal only, frozen stage-B source verified file by file; refuses starts below 1500 MiB free.
"""
import argparse
import datetime
import gzip
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

R = Path('/workspace/oilpalm_resume_20261013')
HERE = Path(__file__).resolve().parent
EXEC = R / 'formal_confirmation/H4176_EXECUTION_V1'
BASE = R / 'experiments/H4176040_NORMAL_STALK_CACHED_BRAKE_LIVE_D0/PREREGISTRATION.json'
PY = '/workspace/oilpalm_diagnostic_venv/bin/python'
MIN_FREE = 1500 * 1024 ** 2


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def dump(path, value):
    with open(path, 'x') as f:
        json.dump(value, f, ensure_ascii=False, indent=2)


def check_freeze(source):
    freeze = json.loads((HERE / 'STAGE_B_SOURCE_FREEZE.json').read_text())
    assert sha(HERE / 'STAGE_B_SOURCE_FREEZE.json') == (HERE / 'STAGE_B_SOURCE_FREEZE.sha256').read_text().split()[0]
    assert str(Path(source)) == freeze['source'], 'not the frozen stage-B source'
    for rel, h in freeze['source_files'].items():
        assert sha(Path(source) / rel) == h, rel
    prereg = HERE / 'STAGE_B_PREREGISTRATION.json'
    assert sha(prereg) == (HERE / 'STAGE_B_PREREGISTRATION.sha256').read_text().split()[0]
    return sha(HERE / 'STAGE_B_SOURCE_FREEZE.json'), sha(prereg)


def summarize(raw):
    trace = next(Path(raw).glob('model_iter*.jsonl.gz'), None)
    out = dict(trace=str(trace) if trace else None, cut_steps=[], stop_reason=None, last_state=None, frames=0)
    if trace is None:
        return out
    with gzip.open(trace, 'rt') as f:
        for line in f:
            r = json.loads(line)
            out['frames'] = r['step']
            h = (r.get('geometry_controller') or {}).get('shape_release_handoff') or {}
            out['last_state'] = h.get('state') or out['last_state']
            if h.get('stop_reason'):
                out['stop_reason'] = h['stop_reason']
            if r.get('cut_allowed'):
                out['cut_steps'].append(r['step'])
            for e in h.get('events', []):
                if e.get('reason') == 'actual_release_receipt' or 'release' in str(e.get('reason', '')) and 'receipt' in str(e.get('reason', '')):
                    out.setdefault('release_events', []).append((r['step'], e['reason']))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('case')
    ap.add_argument('--source', required=True)
    ap.add_argument('--level', required=True)
    ap.add_argument('--mode', choices=['hold', 'handoff'], required=True)
    ap.add_argument('--seed', type=int, required=True)
    ap.add_argument('--purpose', required=True)
    a = ap.parse_args()
    free = shutil.disk_usage(R).free
    if free < MIN_FREE:
        raise SystemExit(f'disk below 1500 MiB ({free >> 20} MiB); stop and report')
    base = json.loads(BASE.read_text())
    case = a.case
    D = R / 'experiments' / case
    raw = str(R / 'raw' / case)
    args = [v.replace(base['raw_output'], raw) for v in base['original_environment_initialization_arguments']]
    args[args.index('--seeds') + 1] = str(a.seed)
    if a.mode == 'hold':
        args[args.index('--screened-mode') + 1] = 'hold'
    if a.mode == 'handoff':
        args.append('--first-handoff-only')
    env = dict(base['environment'], TMPDIR=str(R / 'native_cache' / case))
    freeze_sha, prereg_sha = check_freeze(a.source)
    assert a.level == 'NOMINAL', 'stage-B hold/handoff units are nominal only'
    driver = a.source + '/scripts/rl/diagnose_native_contact_prediction_v36full1.py'
    reg = dict(case=case, registered_utc=now(), source=a.source, source_sha256=json.loads((HERE / 'STAGE_B_SOURCE_FREEZE.json').read_text())['source_files'],
               raw_output=raw, environment=env,
               observer_original_argv=[driver] + args, observer_original_entry_sha256=sha(driver),
               command=[PY, '-B', str(EXEC / 'substep_observer_entry.py'), case],
               formal_confirmation=True, development_only=False, version='H4177_stage_B', level=a.level,
               mode=a.mode, process_seed=a.seed, purpose=a.purpose,
               stage_b_freeze_sha256=freeze_sha, stage_b_preregistration_sha256=prereg_sha,
               launcher_sha256=sha(__file__), kind='H4177_stage_B_formal', maximum_wall_s=10800)
    D.mkdir()
    dump(D / 'PREREGISTRATION.json', reg)
    penv = dict(os.environ, **env)
    penv.pop('OPENBLAS_CORETYPE', None)
    penv.pop('NPY_DISABLE_CPU_FEATURES', None)
    Path(env['TMPDIR']).mkdir(parents=True, exist_ok=True)
    log = open(D / 'PROCESS_STDOUT.original.log', 'x')
    p = subprocess.Popen(reg['command'], cwd=a.source, env=penv, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
    ledger = dict(case=case, process_started=True, pid=p.pid, started_utc=now(), status='running',
                  formal_confirmation=True, development_only=False, source=a.source, not_confirmation=False,
                  level=a.level, mode=a.mode)
    (D / 'LAUNCH_LEDGER.json').write_text(json.dumps(ledger, indent=2))
    try:
        rc = p.wait(timeout=reg['maximum_wall_s'])
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, 15)
        rc = p.wait()
        ledger['administrative_stop_reason'] = 'maximum_wall_exceeded'
    log.close()
    ledger.update(status='finished', returncode=rc, finished_utc=now())
    (D / 'LAUNCH_LEDGER.json').write_text(json.dumps(ledger, indent=2))
    sys.path[:0] = [str(EXEC), str(R / 'src')]
    from formal_runner import seal_raw
    storage = seal_raw(D, case, reg)
    result = dict(case=case, level=a.level, mode=a.mode, seed=a.seed, returncode=rc, **summarize(raw),
                  archive_sha256=storage['archive_sha256'], raw_files=len(storage['files']))
    manifest = Path(raw) / 'ACTUAL_SOLVER_OBSERVER_MANIFEST.json'
    if manifest.exists():
        m = json.loads(manifest.read_text())
        result['observer'] = dict(records=m.get('records_written'), controls=m.get('controls_observed'), complete=m.get('coverage_complete'), errors=m.get('errors'))
    ledger['integrated_control_frames'] = result['frames']
    (D / 'LAUNCH_LEDGER.json').write_text(json.dumps(ledger, indent=2))
    dump(D / 'DEV_RESULT.json', result)
    print(json.dumps(result))


if __name__ == '__main__':
    main()
