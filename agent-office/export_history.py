#!/usr/bin/env python3
"""Export committed metadata only. Never reads Claude sessions or modifies lesson files."""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import re
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CONTENT = ('meta.json', 'lesson.md', 'exercises.json', 'solutions.md', 'answers.py',
           'exit-ticket.json', 'sim.js', 'sim-spec.md', 'inquiry.json')


def normalized(text, name):
    """Match reviews.py's published hash rule without executing historical code."""
    if name.endswith('.json'):
        return json.dumps(json.loads(text), sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    out = []
    for line in text.replace('\r\n', '\n').split('\n'):
        line = line.rstrip()
        if line == '' and out and out[-1] == '':
            continue
        out.append(line)
    while out and out[-1] == '':
        out.pop()
    return '\n'.join(out)


def read_objects(ids):
    ids = sorted(ids)
    data = subprocess.run(['git', 'cat-file', '--batch'], cwd=ROOT,
                          input=('\n'.join(ids)+'\n').encode(), capture_output=True, check=True).stdout
    objects, pos = {}, 0
    for oid in ids:
        end = data.index(b'\n', pos)
        sha, kind, size = data[pos:end].decode().split()
        if sha != oid or kind != 'blob':
            raise ValueError(f'Expected committed blob {oid}')
        pos = end + 1
        objects[oid] = data[pos:pos+int(size)].decode('utf-8')
        pos += int(size) + 1
    return objects


def lesson_states(tree, objects):
    def read(path):
        return objects.get(tree.get(path), '')
    lessons = []
    for path in sorted(tree):
        if not re.fullmatch(r'fysiikkalabra/content/[^/]+/[^/]+/meta.json', path):
            continue
        folder = path.rsplit('/', 1)[0]
        lid = folder.rsplit('/', 1)[1]
        if lid == '_gold':
            continue
        try:
            meta = json.loads(read(path))
            digest = hashlib.sha256()
            parts = [(n, folder+'/'+n) for n in CONTENT]
            parts.append((f'tests/sims/{lid}.json', f'fysiikkalabra/tests/sims/{lid}.json'))
            for name, file in parts:
                if file in tree:
                    digest.update(name.encode()+b'\0'+normalized(read(file), name).encode()+b'\0')
            current_hash = digest.hexdigest()[:16]
            def review(role):
                report_path = folder+'/review/'+role+'.md'
                if report_path not in tree:
                    return {'status': 'missing'}
                lines = read(report_path).splitlines()[:3]
                verdict = lines[0].split(':',1)[1].strip() if lines and lines[0].startswith('VERDICT:') else None
                content_hash = next((line.split(':',1)[1].strip() for line in lines if line.startswith('CONTENT-HASH:')), None)
                if verdict not in ('PASS','FAIL') or not content_hash:
                    return {'status': 'invalid'}
                return {'status': verdict if content_hash == current_hash else 'stale',
                        'verdict': verdict, 'hash': content_hash}
            science, pedagogy, legacy = review('science'), review('pedagogy'), review('legacy')
            checks = read(folder+'/review/checks.txt').splitlines()
            lessons.append({'id':lid, 'title':meta.get('title',lid), 'hash':current_hash,
                            'science':science, 'pedagogy':pedagogy, 'legacy':legacy,
                            'eligible':science['status']=='PASS' and pedagogy['status']=='PASS',
                            'included':f'fysiikkalabra/site/{lid}.html' in tree,
                            'checks':{'passed':sum(line.startswith('ok ') for line in checks),
                                      'failed':sum(line.startswith('FAIL ') for line in checks)},
                            'files':[name for name in CONTENT if folder+'/'+name in tree]})
        except (ValueError, KeyError) as error:
            # Bad historical content must never become a green gate.
            lessons.append({'id':lid,'title':lid,'error':str(error),'eligible':False,
                            'science':{'status':'invalid'},'pedagogy':{'status':'invalid'},
                            'legacy':{'status':'invalid'},'included':False,'files':[],
                            'checks':{'passed':0,'failed':0}})
    return lessons


def export():
    raw = subprocess.run(
        ["git", "log", "--topo-order", "--diff-merges=first-parent", "-200", "--date=iso-strict",
         "--format=%x1e%H%x00%cI%x00%s", "--name-only"],
        cwd=ROOT, check=True, capture_output=True, text=True,
    ).stdout
    events = []
    for record in raw.split("\x1e"):
        if not record.strip():
            continue
        header, *paths = record.strip().splitlines()
        sha, timestamp, title = header.split("\x00", 2)
        files = [p.strip() for p in paths if p.strip()]
        roles = []
        if any(p.startswith("fysiikkalabra/content/") and "/review/" not in p for p in files):
            roles.append("developer")
        if any(p.endswith("/review/science.md") for p in files):
            roles.append("science")
        if any(p.endswith("/review/pedagogy.md") for p in files):
            roles.append("pedagogy")
        local = dt.datetime.fromisoformat(timestamp).astimezone(ZoneInfo("Europe/Helsinki"))
        events.append({"id": sha, "timestamp": local.isoformat(), "day": local.date().isoformat(),
                       "minute": local.hour * 60 + local.minute + local.second / 60,
                       "title": title, "roles": roles or ["repository"], "files": len(files),
                       "merge": title.startswith("Merge "),
                       'changedLessons':sorted(set(re.findall(r'fysiikkalabra/content/[^/]+/([^/]+)/', '\n'.join(files))))})
    events.sort(key=lambda e: (e["timestamp"], e["id"]))
    trees, ids = {}, set()
    for event in events:
        raw_tree = subprocess.run(['git','ls-tree','-r',event['id'],'--',
                                   'fysiikkalabra/content/','fysiikkalabra/tests/sims/','fysiikkalabra/site/'],
                                  cwd=ROOT,check=True,capture_output=True,text=True).stdout
        tree = {}
        for line in raw_tree.splitlines():
            info, path = line.split('\t',1)
            mode, kind, oid = info.split()
            if kind != 'blob':
                continue
            if path.startswith('fysiikkalabra/site/'):
                if re.fullmatch(r'fysiikkalabra/site/[^/]+\.html',path):
                    tree[path] = oid
            elif path.rsplit('/',1)[-1] in {*CONTENT,'science.md','pedagogy.md','legacy.md','checks.txt'} or path.startswith('fysiikkalabra/tests/sims/') and path.endswith('.json'):
                tree[path] = oid
                ids.add(oid)
        trees[event['id']] = tree
    objects = read_objects(ids)
    snapshots, cache = [], {}
    for event in events:
        tree = trees[event['id']]
        key = tuple(sorted(tree.items()))
        if key not in cache:
            cache[key] = len(snapshots)
            snapshots.append(lesson_states(tree,objects))
        event['snapshot'] = cache[key]
    payload = {"repository": "Hellsla/hellsla.github.io", "timezone": "Europe/Helsinki",
               "exportedAt": dt.datetime.now(dt.timezone.utc).isoformat(), "events": events,
               'snapshots':snapshots}
    content = "window.OFFICE_HISTORY = " + json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c") + ";\n"
    # The only write is an atomic replacement inside this feature's directory.
    handle, temporary = tempfile.mkstemp(prefix=".history-", dir=HERE)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as output:
            output.write(content)
        os.replace(temporary, HERE / "history.js")
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    print(f"Exported {len(events)} commits across {len({e['day'] for e in events})} days to agent-office/history.js")


if __name__ == "__main__":
    export()
