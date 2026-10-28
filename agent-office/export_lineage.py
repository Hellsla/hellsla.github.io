#!/usr/bin/env python3
"""Link exported snapshots through Git ancestry and merge parents; never recompute reviews."""
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
history = json.loads((HERE / 'history.js').read_text().removeprefix('window.OFFICE_HISTORY = ').rstrip().removesuffix(';'))
ids = {event['id'] for event in history['events']}
parents = {}
merge_parents = {}
for commit in sorted(ids):
    chain = subprocess.check_output(['git', 'rev-list', '--first-parent', commit], cwd=HERE, text=True).splitlines()
    parents[commit] = next((ancestor for ancestor in chain[1:] if ancestor in ids), None)
    direct = subprocess.check_output(['git','rev-list','--parents','-n','1',commit], cwd=HERE, text=True).split()[1:]
    if len(direct) > 1:
        merge_parents[commit] = [parent for parent in direct if parent in ids]
parents['_parents'] = merge_parents
(HERE / 'history-lineage.js').write_text('window.OFFICE_LINEAGE = ' + json.dumps(parents, sort_keys=True) + ';\n')
