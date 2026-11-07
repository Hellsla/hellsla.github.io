"""Annetut tehtävät (teacher 2026-11-07): the exercises a teacher assigns in each module, kept centrally in
`annetut.json` by their permanent ids ({"FY3": {"fy3-1": ["fy3-1-L1-06", ...], ...}}), never written in a lesson.
The site marks them (build.py exercise_html: a green left edge and "Annettu"), the student ticks one "Tehty" once a
solution is saved in its editor (templates/tehty.js), the module page shows the progress and the submission file
carries it (templates/palautus.js, version 4).

  python scripts/assigned.py               check annetut.json and print the counts per module
  python scripts/assigned.py --propose FY3 write a proposal for a module into annetut.json (its old list replaced)
  python scripts/assigned.py --dry FY1 ... print a proposal without writing it

The proposal keeps the chapter's core exercises (build.py core_ids) and adds, in as many chapters as the module's
target needs, one level-3 task (applying) that brings a kind the core lacks (data, graph, experiment, error,
reasoning, model). Extension tasks ("Syventävä tehtävä." at the start of the text) are never assigned, and the
contents and levels of the exercises are not touched. FY9, FY10 and FY14 have no assigned tasks."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / "annetut.json"
COURSES = ("FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8")
TARGET = {"FY1": 36, "FY2": 36}                      # 2 op modules: 70-75 (teacher 2026-11-07); FY1 and FY2 35-38 each
RANGE = {"FY1": (35, 38), "FY2": (35, 38)}
DEFAULT_TARGET, DEFAULT_RANGE = 72, (70, 75)
EXT = "Syventävä tehtävä."                           # lang/fi.json lesson.extension_exercise + "."


def curriculum(): return json.loads((ROOT / "curriculum.json").read_text())


def exercises(code, lid, lang="fi"):
    p = ROOT / "content" / lang / code / lid / "exercises" / "exercises.json"
    return json.loads(p.read_text()) if p.is_file() else None


def core_ids(ex):
    """The same rule as build.py core_ids: "core": true, or the first two of levels 1 and 2 where none is marked."""
    out = []
    for lvl, items in ex.items():
        marked = [e["id"] for e in items if e.get("core")]
        out += marked if any("core" in e for e in items) else ([e["id"] for e in items[:2]] if lvl[-1] in "12" else [])
    return out


def kinds(e):
    k = set(e.get("kind") or [])
    if e.get("figure"): k.add("graph")
    if e.get("data"): k.add("data")
    if e.get("choices") or e.get("statements") or e.get("order"): k.add("concept")
    if isinstance(e.get("answer"), (int, float)) and not e.get("choices"): k.add("calc")
    return k


def propose(code):
    slots = [l["id"] for l in curriculum()[code]["lessons"]]
    sets = {lid: exercises(code, lid) for lid in slots}
    sets = {lid: ex for lid, ex in sets.items() if ex}
    picks = {}
    for lid, ex in sets.items():
        by_id = {e["id"]: e for items in ex.values() for e in items}
        picks[lid] = [i for i in core_ids(ex) if not by_id[i]["text"].startswith(EXT)]
    def add_one(lid, level):
        """the next task of a chapter: of the given level first, the one adding most kinds the chapter's picks lack"""
        ex = sets[lid]; by_id = {e["id"]: e for items in ex.values() for e in items}
        have = set().union(*(kinds(by_id[i]) for i in picks[lid])) if picks[lid] else set()
        cands = [e for items in ex.values() for e in items if e["id"] not in picks[lid] and not e["text"].startswith(EXT)]
        cands.sort(key=lambda e: (e.get("level") != level, -len(kinds(e) - have - {"calc"})))
        if cands: picks[lid].append(cands[0]["id"])
    target = TARGET.get(code, DEFAULT_TARGET)
    base = target // len(picks)
    for lid in picks:                                 # a chapter with fewer core tasks: filled up to the module's base
        while len(picks[lid]) < base: add_one(lid, 2)
    extra = max(0, target - sum(len(v) for v in picks.values()))
    order = [lid for lid in picks if len(picks[lid]) == base]   # one level-3 task more, spread evenly over the teaching order
    chosen = [order[int(i * len(order) / extra)] for i in range(extra)] if 0 < extra <= len(order) else order[:extra]
    for lid in chosen: add_one(lid, 3)
    for lid in picks:                                 # page order (levels, then the bank's order)
        pos = {e["id"]: n for n, e in enumerate(e for items in sets[lid].values() for e in items)}
        picks[lid].sort(key=pos.get)
    return picks


def load():
    if not FILE.is_file(): return {}
    data = json.loads(FILE.read_text())
    return {k: v for k, v in data.items() if not k.startswith("_")}


def flat(data=None):
    """{task id: course} over every module."""
    return {i: code for code, chs in (data if data is not None else load()).items() for ids in chs.values() for i in ids}


def check(data):
    errs, seen = [], {}
    cur = curriculum()
    for code, chs in data.items():
        if code not in COURSES: errs.append(f"{code}: only FY1-FY8 have assigned tasks"); continue
        slots = [l["id"] for l in cur[code]["lessons"]]
        n = 0
        for lid, ids in chs.items():
            if lid not in slots: errs.append(f"{code}: {lid} is not a chapter of the module"); continue
            for lang in ("fi", "en", "fi-easy"):
                ex = exercises(code, lid, lang)
                if ex is None: continue
                by_id = {e["id"]: e for items in ex.values() for e in items}
                for i in ids:
                    if i not in by_id: errs.append(f"{code} {lid}: {i} is not an exercise ({lang})")
                    elif lang == "fi" and by_id[i]["text"].startswith(EXT): errs.append(f"{code} {lid}: {i} is an extension task")
            for i in ids:
                if i in seen: errs.append(f"{i} assigned twice ({seen[i]}, {lid})")
                seen[i] = lid
            n += len(ids)
        lo, hi = RANGE.get(code, DEFAULT_RANGE)
        if not lo <= n <= hi: errs.append(f"{code}: {n} assigned tasks, expected {lo}-{hi}")
        sizes = [len(v) for v in chs.values()]
        if sizes and max(sizes) - min(sizes) > 2: errs.append(f"{code}: uneven chapters {sizes}")
    return errs


def write(data):
    out = {"_note": "Annetut tehtävät (opettaja 7.11.2026): tehtävätunnisteet moduuleittain ja luvuittain. scripts/assigned.py tarkistaa ja ehdottaa."}
    out.update({k: data[k] for k in sorted(data, key=lambda c: int(c[2:]))})
    FILE.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] in ("--propose", "--dry"):
        data = load()
        for code in args[1:]:
            p = propose(code)
            print(code, sum(len(v) for v in p.values()), "tasks:", " ".join(f"{lid.split('-')[1]}:{len(v)}" for lid, v in p.items()))
            if args[0] == "--propose": data[code] = p
        if args[0] == "--propose": write(data)
        if args[0] == "--dry": sys.exit(0)
    data = load()
    errs = check(data)
    for code, chs in data.items():
        print(f"{code}: {sum(len(v) for v in chs.values())} annettua tehtävää, {len(chs)} lukua ({min(map(len, chs.values()))}-{max(map(len, chs.values()))} / luku)")
    ids = [i for chs in data.values() for v in chs.values() for i in v]
    print(f"tunnisteita {len(ids)}, yksilöllisiä {len(set(ids))}")
    if errs: sys.exit("\n".join(errs))
