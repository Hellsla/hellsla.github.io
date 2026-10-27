"""Every worked example and exercise has a complete model solution (teacher's rule 2026-10-27, CLAUDE.md "Lesson form" 7).

  python scripts/check_solutions.py <id>      one lesson
  python scripts/check_solutions.py --all     every lesson of every course, one line per lesson, then the findings

A solution is complete when it shows, in this order: what is given with units and what is asked, the principle
and why it fits, the formula solved for the asked quantity in symbols, the unit conversions (or that none are
needed), the substitution with units, the answer rounded with its unit, and a check that the result is
reasonable (NOTES.md §1, §3 "Complete solutions"). The rule covers:

- `exercises.json` + `solutions.md`: every exercise has its own `## <id>` block with the bold steps LABELS, each
  with text; a task whose text refers to a graph also has `**Kuvaajan lukeminen:**`; a task whose answer is words
  (`answer` a string) has `**Kysytty:**`, `**Periaate:**` and `**Mallivastaus:**` instead of the calculation;
- `meta.json` `solutions` is `all` (the page shows every exercise's solution behind its own Näytä ratkaisu button);
- `## Esimerkki` in `lesson.md`: the stages EXAMPLE_STAGES, one per `<!-- vaihe -->`;
- `inquiry.json`: every `numeric` task (the transfer task, the checks, an experiment's question) has a `solution`
  with the same steps as an exercise.

lint_lesson.py reports these as errors, so check_lesson.py and CI fail on a missing solution; this script lists
them for the whole site at once. Exit status 1 on any finding.
"""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses

LABELS = ["Annettu", "Kysytty", "Periaate", "Kaava", "Muunnokset", "Sijoitus", "Vastaus", "Järkevyys"]
WORD_LABELS = ["Kysytty", "Periaate", "Mallivastaus"]
GRAPH_LABEL = "Kuvaajan lukeminen"
GRAPH = re.compile(r"kuvaaj|kuvaa?jasta|\(t,\s*x\)|-kuvaaja", re.I)
EXAMPLE_STAGES = ["Tunnetut ja kysytty", "Periaate", "Kaava ratkaistuna", "Yksikkömuunnokset", "Sijoitus", "Tulos", "Järkevyys"]


def steps(body):
    """{label: text} of a solution written as `**Label:** text` or `**Label.** text`, each step running to the next label."""
    out = {}
    parts = re.split(r"\*\*([^*\n]+?)[:.]\*\*:?", body)
    for i in range(1, len(parts), 2):
        out.setdefault(parts[i].strip(), parts[i + 1].strip())
    return out


def check_steps(body, needed):
    """Missing, empty or out-of-order steps of one solution, as messages."""
    got = steps(body)
    msgs = [f"no '**{lab}:**' step" for lab in needed if lab not in got]
    msgs += [f"the '**{lab}:**' step is empty" for lab in needed if lab in got and not got[lab]]
    order = [lab for lab in got if lab in needed]
    if not msgs and order != needed: msgs.append("steps out of order: " + " → ".join(needed))
    return msgs


def blocks_of(text):
    """[(exercise id, line, body)] of solutions.md."""
    out = []
    for m in re.finditer(r"^## (\S+)[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        out.append((m.group(1), text.count("\n", 0, m.start()) + 1, m.group(2)))
    return out


def exercise_problems(folder):
    f = folder / "exercises.json"
    if not f.exists(): return [("exercises.json", 1, "missing")]
    ex = [e for items in json.loads(f.read_text()).values() for e in items]
    s = folder / "solutions.md"
    blocks = blocks_of(s.read_text()) if s.exists() else []
    found = {eid: (line, body) for eid, line, body in blocks}
    out = []
    for e in ex:
        eid = e["id"]
        if eid not in found: out.append(("solutions.md", 1, f"{eid}: no solution (every exercise has one, teacher 2026-10-27)")); continue
        line, body = found[eid]
        if not body.strip(): out.append(("solutions.md", line, f"{eid}: the solution is empty")); continue
        needed = WORD_LABELS if isinstance(e.get("answer"), str) else LABELS
        if GRAPH.search(e.get("text", "")): needed = needed[:3] + [GRAPH_LABEL] + needed[3:]
        out += [("solutions.md", line, f"{eid}: {m}") for m in check_steps(body, needed)]
    ids = {e["id"] for e in ex}
    out += [("solutions.md", line, f"{eid}: a solution for an exercise that does not exist") for eid, line, _ in blocks if eid not in ids]
    return out


def example_problems(folder):
    f = folder / "lesson.md"
    if not f.exists(): return []
    text = f.read_text()
    m = re.search(r"^## Esimerkki[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m: return [("lesson.md", 1, "no '## Esimerkki' (every lesson has a worked example)")]
    line = text.count("\n", 0, m.start()) + 1
    stages = m.group(1).split("<!-- vaihe -->")[1:]
    leads = [(re.match(r"\s*\*\*([^*]+?)\.?\*\*", st) or [None, ""])[1].rstrip(".") for st in stages]
    if leads != EXAMPLE_STAGES:
        return [("lesson.md", line, "the worked example's stages are " + (" · ".join(leads) or "none")
                 + "; write " + " · ".join(EXAMPLE_STAGES) + " (teacher 2026-10-27, NOTES §3)")]
    return [("lesson.md", line, f"worked example: the stage '{lead}' is empty") for lead, st in zip(leads, stages)
            if not re.sub(r"\*\*[^*]+\*\*", "", st).strip()]


def numeric_tasks(o, where=""):
    """(location, activity) for every numeric task in inquiry.json, an experiment's question included."""
    if isinstance(o, dict):
        if o.get("type") == "numeric": yield where, o
        for k, v in o.items():
            yield from numeric_tasks(v, o.get("id", where) if k == "question" else where)
    elif isinstance(o, list):
        for v in o:
            yield from numeric_tasks(v, v.get("id", where) if isinstance(v, dict) else where)


def inquiry_problems(folder):
    f = folder / "inquiry.json"
    if not f.exists(): return []
    out = []
    for where, a in numeric_tasks(json.loads(f.read_text())):
        name = a.get("id") or f"{where}'s question"
        sol = a.get("solution") or ""
        if not sol.strip(): out.append(("inquiry.json", 1, f"numeric {name}: no solution (every task has one, teacher 2026-10-27)")); continue
        out += [("inquiry.json", 1, f"numeric {name}: {m}") for m in check_steps(sol, LABELS)]
    return out


def meta_problems(folder):
    meta = json.loads((folder / "meta.json").read_text())
    if meta.get("solutions", "all") != "all":
        return [("meta.json", 1, f"solutions is {meta['solutions']!r}; every exercise shows its solution: \"solutions\": \"all\" (teacher 2026-10-27)")]
    return []


def problems(folder):
    return meta_problems(folder) + example_problems(folder) + exercise_problems(folder) + inquiry_problems(folder)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    folders = courses.lessons() if args[0] == "--all" else [courses.find_lesson(args[0])]
    bad = 0
    for folder in folders:
        p = problems(folder)
        bad += len(p)
        print(f"{'ok  ' if not p else 'FAIL'} {folder.name}: {len(p)} missing or incomplete solution(s)")
        for name, line, msg in p: print(f"     {name}:{line} {msg}")
    sys.exit(1 if bad else 0)
