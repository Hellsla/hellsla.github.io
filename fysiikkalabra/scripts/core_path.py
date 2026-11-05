#!/usr/bin/env python3
"""The core path of FY1–FY8 by skill (teacher's brief 2026-11-05, "ydinpolku taitojen kannalta monipuoliseksi").

Report only; it changes nothing. For each chapter it lists the core exercises (`"core": true`, or by default the first
two of levels 1 and 2, scripts/build.py core_ids) and the tasks of the lesson that are on the core path (not
`optional`), each by the skill it practises:

  lasku      a calculation (an exercise with a number to check and no other kind)
  sanallinen a reasoning, concept or error-finding task (kind reasoning/concept/error, a multiple choice)
  kuvaaja    a graph to draw or read (kind graph)
  voimakuvio a force diagram (an exercise with "fbd", an explain with "draw": true)
  tutkimus   an investigation, measurement data or a model of it (kind experiment/data/model; an experiment;
             an interpret)
  selitys    a written explanation in the lesson (explain without draw)

  python scripts/core_path.py                 summary per module (markdown, stdout)
  python scripts/core_path.py FY4             one module, chapter by chapter, with every exercise's skills
  python scripts/core_path.py --write         writes docs/core-path/summary.md
"""
import collections, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses


def core_ids(ex):
    """Same rule as scripts/build.py core_ids (importing build would run a build): marked ones, or in a level with none
    marked the first two of levels 1 and 2."""
    out = set()
    for lvl, items in ex.items():
        marked = [e["id"] for e in items if e.get("core")]
        out |= set(marked) if any("core" in e for e in items) else ({e["id"] for e in items[:2]} if lvl[-1] in "12" else set())
    return out

ROOT = courses.ROOT
MODULES = [f"FY{i}" for i in range(1, 9)]
SKILLS = ("lasku", "sanallinen", "kuvaaja", "voimakuvio", "tutkimus", "selitys")


def exercise_skills(e):
    kind = set(e.get("kind") or [])
    s = set()
    if e.get("fbd"): s.add("voimakuvio")
    if "graph" in kind: s.add("kuvaaja")
    if kind & {"experiment", "data", "model"}: s.add("tutkimus")
    if kind & {"reasoning", "concept", "error"} or e.get("choices"): s.add("sanallinen")
    return s or {"lasku"}


def activity_skills(a):
    t = a.get("type")
    if t == "explain": return {"voimakuvio"} if a.get("draw") else {"selitys"}
    if t in ("experiment", "interpret"): return {"tutkimus"}
    if t == "numeric": return {"lasku"}
    if t == "choice": return {"sanallinen"}
    return set()


def chapter(folder):
    """(learn goals, core exercises [(id, skills)], all exercises by skill, lesson core tasks [(id, type, skills, marked)])."""
    ex_f, inq_f = folder / "exercises" / "exercises.json", folder / "inquiry.json"
    ex = json.loads(ex_f.read_text()) if ex_f.exists() else {}
    ex = {k: v for k, v in ex.items() if isinstance(v, list)}
    core = core_ids(ex)
    items = [e for v in ex.values() for e in v]
    core_ex = [(e["id"], exercise_skills(e)) for e in items if e["id"] in core]
    pool = collections.Counter(s for e in items for s in exercise_skills(e))
    inq = json.loads(inq_f.read_text()) if inq_f.exists() else {}
    acts = [(a.get("id"), a.get("type"), activity_skills(a), bool(a.get("core"))) for a in inq.get("activities", [])
            if isinstance(a, dict) and not a.get("optional") and a.get("stage") != "ennusta" and activity_skills(a)
            and a.get("type") in ("experiment", "interpret", "explain") or (isinstance(a, dict) and a.get("core"))]
    return inq.get("learn", []), core_ex, pool, acts


def folders(module):
    return sorted((p for p in (ROOT / "content" / "fi" / module).glob(f"{module.lower()}-*") if p.is_dir()),
                  key=lambda p: int(p.name.split("-")[1]))


def summary():
    out = ["# Ydinpolku taidoittain (FY1–FY8)", "",
           "Lähde: `python scripts/core_path.py`. Ydintehtävät = merkityt (`\"core\": true`) tai oletuksena tasojen 1 ja 2 kaksi ensimmäistä.",
           "Oppitunnin ydintehtävät = ei-valinnaiset tutkimukset, tulkinnat ja selitykset (Ennusta-vaihetta ei lasketa) sekä merkityt.", "",
           "| Moduuli | Lukuja | Ydinteht. | lasku | sanallinen | kuvaaja | voimakuvio | tutkimus | Luvut, joiden ydintehtävät ovat pelkkiä laskuja |",
           "|---|---|---|---|---|---|---|---|---|"]
    for m in MODULES:
        fs = folders(m); c = collections.Counter(); only_calc = []
        for f in fs:
            _, core_ex, _, _ = chapter(f)
            for _, s in core_ex: c.update(s)
            if core_ex and all(s == {"lasku"} for _, s in core_ex): only_calc.append(f.name)
        n = sum(len(chapter(f)[1]) for f in fs)
        out.append(f"| {m} | {len(fs)} | {n} | " + " | ".join(str(c[s]) for s in SKILLS[:5]) + f" | {len(only_calc)}: {', '.join(only_calc)} |")
    return "\n".join(out) + "\n"


def detail(module):
    out = [f"# {module}: ydinpolku luvuittain", ""]
    for f in folders(module):
        learn, core_ex, pool, acts = chapter(f)
        out.append(f"## {f.name}")
        for g in learn: out.append(f"- tavoite: {g}")
        out.append("- ydinharjoitukset: " + ", ".join(f"{i.split('-', 2)[-1]} ({'/'.join(sorted(s))})" for i, s in core_ex))
        out.append("- kaikki harjoitukset: " + ", ".join(f"{s} {pool[s]}" for s in SKILLS if pool[s]))
        out.append("- oppitunnin ydintehtävät: " + (", ".join(f"{i} ({t}{', merkitty' if mk else ''})" for i, t, _, mk in acts) or "–"))
        out.append("")
    return "\n".join(out)


def main(argv):
    if "--write" in argv:
        d = ROOT / "docs" / "core-path"; d.mkdir(parents=True, exist_ok=True)
        (d / "summary.md").write_text(summary()); print(f"wrote {d / 'summary.md'}"); return 0
    mods = [a for a in argv if a in MODULES]
    print("\n".join(detail(m) for m in mods) if mods else summary())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
