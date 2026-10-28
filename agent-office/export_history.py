#!/usr/bin/env python3
"""Export committed metadata only. Never reads Claude sessions or modifies lesson files."""
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import tempfile
import re
from history_evidence import states
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
        objects[oid] = data[pos:pos+int(size)]
        pos += int(size) + 1
    return objects


def lesson_states(tree, objects):
    return states(tree, objects, CONTENT, normalized)


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
        if any(p.startswith(("fysiikkalabra/content/", "fysiikkalabra/lessons/", "fysiikkalabra/assets/")) and "/review/" not in p for p in files):
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
                       'changedLessons':sorted(set(re.findall(r'fysiikkalabra/(?:content/(?:[a-z]{2}/)?|lessons/)[^/]+/([^/]+)/', '\n'.join(files))))})
    events.sort(key=lambda e: (e["timestamp"], e["id"]))
    trees, ids = {}, set()
    for event in events:
        raw_tree = subprocess.run(['git','ls-tree','-r',event['id'],'--',
                                   'fysiikkalabra/content/','fysiikkalabra/tests/sims/','fysiikkalabra/site/',
                                   'fysiikkalabra/lessons/','fysiikkalabra/assets/','fysiikkalabra/lang/',
                                   'fysiikkalabra/scripts/reviews.py'],
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
            elif path.rsplit('/',1)[-1] in {*CONTENT,'lesson-answers.py','science.md','pedagogy.md','legacy.md','checks.txt','carry.tsv','usage.tsv'} or path.startswith(('fysiikkalabra/tests/sims/','fysiikkalabra/assets/','fysiikkalabra/lang/')) or path == 'fysiikkalabra/scripts/reviews.py':
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
