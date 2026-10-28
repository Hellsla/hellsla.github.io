"""Read committed evidence across the old and multilingual lesson layouts.

Only the current checkout's trusted review helpers are imported. Historical Python
is read as schema metadata, never imported or executed.
"""
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'fysiikkalabra/scripts'))
import reviews

PREFIX = 'fysiikkalabra/'
META = re.compile(r'fysiikkalabra/content/(?:fi/)?([^/]+)/([^/]+)/meta.json$')


class Snapshot(reviews.Source):
    def __init__(self, tree, objects):
        self.tree, self.objects = tree, objects

    def exact(self, path, binary=False):
        data = self.objects.get(self.tree.get(path))
        if data is None:
            return None
        if isinstance(data, str):
            return data.encode() if binary else data
        return data if binary else data.decode('utf-8')

    def read(self, rel, binary=False):
        candidates = [rel]
        moved = reviews.MOVED.match(rel)
        if moved:
            candidates.append(f'{moved[1]}/{moved[2]}')
        for candidate in candidates:
            for location in [candidate, *(['content/' + reviews.LEGACY.match(candidate)[1]]
                                         if reviews.LEGACY.match(candidate) else [])]:
                data = self.exact(PREFIX + location, binary)
                if data is not None:
                    return data
        return None

    def files(self, reldir):
        return sorted(path[len(PREFIX):] for path in self.tree
                      if path.startswith(PREFIX + reldir + '/'))


def rows(text):
    return list(csv.DictReader(io.StringIO(text or ''), delimiter='\t'))


def report(src, folder, role, current_hash):
    text = src.exact(f'{folder}/review/{role}.md')
    if text is None:
        return {'status': 'missing'}
    lines = text.splitlines()[:3]
    verdict = lines[0].split(':', 1)[1].strip() if lines and lines[0].startswith('VERDICT:') else None
    digest = next((line.split(':', 1)[1].strip() for line in lines if line.startswith('CONTENT-HASH:')), None)
    if verdict not in ('PASS', 'FAIL') or not digest:
        return {'status': 'invalid'}
    result = {'status': verdict if digest == current_hash else 'stale', 'verdict': verdict, 'hash': digest}
    # Same evidence used by reviews.py status; CI verification remains a separate fact.
    carry = next((r for r in rows(src.exact(folder + '/review/carry.tsv'))
                  if r.get('reviewer') == role and r.get('from') == digest and r.get('to') == current_hash), None)
    if verdict == 'PASS' and role != 'legacy' and carry:
        result.update(status='PASS', carried={k: carry.get(k, '') for k in ('base', 'categories')})
    return result


def usage(src, folder):
    paths = [folder + '/review/usage.tsv', folder + '/exercises/review/usage.tsv']
    entries, seen = [], set()
    for path in paths:
        for row in rows(src.exact(path)):
            # A moved/copied log entry is still the same recorded run.
            key = row.get('ref') or tuple(sorted(row.items()))
            if key not in seen:
                seen.add(key)
                entries.append(row)
    return {
        'entries': len(entries),
        'development': sum(r.get('agent') == 'developer' for r in entries),
        'orchestration': sum(r.get('agent') == 'orchestrator' for r in entries),
        'support': sum(r.get('agent') == 'general-purpose' for r in entries),
        'fixes': sum(r.get('agent') == 'developer' and r.get('mode') == 'fix' for r in entries),
        'science': sum(r.get('agent') == 'science-reviewer' for r in entries),
        'pedagogy': sum(r.get('agent') == 'pedagogy-reviewer' for r in entries),
        'full': sum(r.get('mode') == 'full' and 'reviewer' in r.get('agent', '') for r in entries),
        'delta': sum(r.get('mode') == 'delta' and 'reviewer' in r.get('agent', '') for r in entries),
        'round': max((int(r['round']) for r in entries if r.get('round', '').isdigit()), default=0),
        'sources': [p for p in paths if p in src.tree]
    }


def states(tree, objects, content, normalized):
    src = Snapshot(tree, objects)
    policy = src.exact(PREFIX + 'scripts/reviews.py') or ''
    asset_schema = 'def entries(' in policy
    split_schema = 'LESSON_CONTENT' in policy
    out = []
    for path in sorted(tree):
        match = META.fullmatch(path)
        if not match:
            continue
        course, lid = match.groups()
        folder = path.rsplit('/', 1)[0]
        canonical = ROOT / PREFIX / 'content/fi' / course / lid
        try:
            meta = json.loads(src.exact(path))
            if asset_schema:
                digest = reviews.hash_of(canonical, src, 'lesson' if split_schema else 'all')
            else:
                hasher = hashlib.sha256()
                for name, location in [*((n, folder + '/' + n) for n in content),
                                       (f'tests/sims/{lid}.json', PREFIX + f'tests/sims/{lid}.json')]:
                    text = src.exact(location)
                    if text is not None:
                        hasher.update(name.encode() + b'\0' + normalized(text, name).encode() + b'\0')
                digest = hasher.hexdigest()[:16]
            state = {'id': lid, 'title': meta.get('title', lid), 'hash': digest}
            state.update({r: report(src, folder, r, digest) for r in ('science', 'pedagogy', 'legacy')})
            checks = (src.exact(folder + '/review/checks.txt') or '').splitlines()
            state.update(
                eligible=all(state[r]['status'] == 'PASS' for r in ('science', 'pedagogy')),
                included=PREFIX + f'site/{lid}.html' in tree,
                checks={'passed': sum(line.startswith('ok ') for line in checks),
                        'failed': sum(line.startswith('FAIL ') for line in checks)},
                files=[n for n in content if src.read(reviews.courses.lesson_rel(canonical, n)) is not None],
                work=usage(src, folder)
            )
            if split_schema:
                exercise_hash = reviews.hash_of(canonical, src, 'exercises')
                exercise_folder = folder + '/exercises'
                state['exercises'] = {'hash': exercise_hash, **{
                    r: report(src, exercise_folder, r, exercise_hash) for r in ('science', 'pedagogy')}}
            out.append(state)
        except (ValueError, KeyError, UnicodeError) as error:
            out.append({'id': lid, 'title': lid, 'error': str(error), 'eligible': False,
                        **{r: {'status': 'invalid'} for r in ('science', 'pedagogy', 'legacy')},
                        'included': False, 'files': [], 'checks': {'passed': 0, 'failed': 0},
                        'work': usage(src, folder)})
    return out
