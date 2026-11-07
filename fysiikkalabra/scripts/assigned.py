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
reasoning, model). Short answer-only tasks (teacher 2026-11-07: a one-item multiple choice or a level-1 calculation
with one formula that needs no solving, e.g. Celsius to kelvins) do not count towards the 4-5 of a chapter: a core
one stays assigned on top of them. Extension tasks ("Syventävä tehtävä." at the start of the text) are never assigned, and the
contents and levels of the exercises are not touched. FY9, FY10 and FY14 have no assigned tasks."""
import json
import re
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


def solution_lines(code, lid, lang="fi"):
    """{task id: the **Kaava:** line of its model solution} from the chapter's solutions.md"""
    p = ROOT / "content" / lang / code / lid / "exercises" / "solutions.md"
    out, cur = {}, None
    for line in (p.read_text().splitlines() if p.is_file() else []):
        m = re.match(r"## (\S+)", line)
        if m: cur = m.group(1); out[cur] = ""
        elif cur and line.startswith("**Kaava:**"): out[cur] = line
    return out


def is_short(e, formula):
    """only an answer is asked: a level-1 one-item multiple choice, or a level-1 calculation with one formula that is
    used as it is (no "joten" solving step, at most one "=") and no data or figure"""
    if e.get("level") != 1 or e.get("data") or e.get("figure") or e.get("statements") or e.get("order"): return False
    if e.get("choices"): return True
    return isinstance(e.get("answer"), (int, float)) and bool(formula) and "joten" not in formula and formula.count("=") <= 1


def shorts(code, lid):
    ex = exercises(code, lid) or {}
    f = solution_lines(code, lid)
    return {e["id"] for items in ex.values() for e in items if is_short(e, f.get(e["id"], ""))}


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
    picks, extra_short = {}, {}
    short = {lid: shorts(code, lid) for lid in sets}
    for lid, ex in sets.items():
        by_id = {e["id"]: e for items in ex.values() for e in items}
        core = [i for i in core_ids(ex) if not by_id[i]["text"].startswith(EXT)]
        picks[lid] = [i for i in core if i not in short[lid]]
        extra_short[lid] = [i for i in core if i in short[lid]]   # on top of the chapter's 4-5
    def add_one(lid, level):
        """the next task of a chapter: of the given level first, the one adding most kinds the chapter's picks lack"""
        ex = sets[lid]; by_id = {e["id"]: e for items in ex.values() for e in items}
        have = set().union(*(kinds(by_id[i]) for i in picks[lid])) if picks[lid] else set()
        cands = [e for items in ex.values() for e in items if e["id"] not in picks[lid] and e["id"] not in short[lid] and not e["text"].startswith(EXT)]
        cands.sort(key=lambda e: (e.get("level") != level, -len(kinds(e) - have - {"calc"})))
        if cands: picks[lid].append(cands[0]["id"])
    target = TARGET.get(code, DEFAULT_TARGET)
    base = target // len(picks)
    for lid in picks:                                 # a chapter with fewer core tasks: filled up to the module's base
        while len(picks[lid]) < base:
            n = len(picks[lid]); add_one(lid, 2)
            if len(picks[lid]) == n: break            # the bank has nothing more to give
    extra = max(0, target - sum(len(v) for v in picks.values()))
    order = [lid for lid in picks if len(picks[lid]) == base]   # one level-3 task more, spread evenly over the teaching order
    chosen = [order[int(i * len(order) / extra)] for i in range(extra)] if 0 < extra <= len(order) else order[:extra]
    for lid in chosen: add_one(lid, 3)
    for lid in picks:                                 # page order (levels, then the bank's order)
        picks[lid] += extra_short[lid]
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
        n, sizes = 0, []
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
            short = shorts(code, lid)
            sizes.append(len([i for i in ids if i not in short])); n += sizes[-1]
        lo, hi = RANGE.get(code, DEFAULT_RANGE)
        if not lo <= n <= hi: errs.append(f"{code}: {n} assigned tasks (short ones not counted), expected {lo}-{hi}")
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
            sh = {lid: shorts(code, lid) for lid in p}
            print(code, sum(len([i for i in v if i not in sh[lid]]) for lid, v in p.items()), "tasks +", sum(len([i for i in v if i in sh[lid]]) for lid, v in p.items()), "short:",
                  " ".join(f"{lid.split('-')[1]}:{len([i for i in v if i not in sh[lid]])}+{len([i for i in v if i in sh[lid]])}" for lid, v in p.items()))
            if args[0] == "--propose": data[code] = p
        if args[0] == "--propose": write(data)
        if args[0] == "--dry": sys.exit(0)
    data = load()
    errs = check(data)
    for code, chs in data.items():
        main = [len([i for i in v if i not in shorts(code, lid)]) for lid, v in chs.items()]
        print(f"{code}: {sum(main)} annettua tehtävää + {sum(map(len, chs.values())) - sum(main)} lyhyttä vastaustehtävää, {len(chs)} lukua ({min(main)}-{max(main)} / luku)")
    ids = [i for chs in data.values() for v in chs.values() for i in v]
    print(f"tunnisteita {len(ids)}, yksilöllisiä {len(set(ids))}")
    if errs: sys.exit("\n".join(errs))
