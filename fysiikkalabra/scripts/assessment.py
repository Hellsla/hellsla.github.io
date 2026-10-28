"""Assessment audit of a course (teacher's brief 2026-10-28, NOTES.md §11): per chapter, the conceptual multiple-choice
checks, the tasks that need a figure, the exit ticket and possible redundancy, all derived from the files.

  python scripts/assessment.py <COURSE>            write docs/assessment/<COURSE>.md
  python scripts/assessment.py <COURSE> --check    exit 1 when the committed report is out of date (CI)
  python scripts/assessment.py --all [--check]     every course that has lessons
  python scripts/assessment.py <id>                one chapter's lines on the terminal (what a developer packet carries)

What it counts, and what it cannot see:
  checks       choice tasks in Tarkista osaamisesi (and choice questions of interpret tasks there): the conceptual
               multiple-choice checks the brief asks 2–3 of; Ennusta predictions are counted apart (they come before
               the theory and are not assessment)
  figure tasks exercises, inquiry tasks and Sovella parts that show a figure ("figure": "<id>", or an SVG in an
               interpret task's representation); whether the figure is really needed to answer is the reviewers' call
  exit ticket  its questions; one that shares most of its words with a check or an exercise of the chapter is
               listed as a possible duplicate (word overlap, Jaccard ≥ OVERLAP)
  redundancy   two exercises of a chapter with the same words (Jaccard ≥ OVERLAP) are listed as possible repeats
  opportunity  a chapter without a figure task whose figures.py has figures marked "safe" in the catalog
Nothing here grades a task; it tells the developer where to look before writing and the reviewers what to confirm.
"""
import json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, figcat, i18n

ROOT = courses.ROOT
OVERLAP = 0.5
TARGET = (2, 3)        # conceptual checks in Tarkista osaamisesi, when the chapter's concepts call for them
STOP = set("ja on ei se että kun jos tai mikä mitä kuinka miten kuin sen niin myös vain tässä oli ovat olla joka "
           "the and is of a to in what how".split())


def words(t):
    t = re.sub(r"\$[^$]*\$", " ", t or ""); t = re.sub(r"<[^>]+>", " ", t)
    return {w for w in re.findall(r"[a-zåäö]{3,}", t.lower()) if w not in STOP}


def jaccard(a, b): return len(a & b) / len(a | b) if a and b else 0.0


def chapter(folder):
    """The chapter's numbers and findings as a dict."""
    lid = folder.name
    inq = json.loads((folder / "inquiry.json").read_text()) if (folder / "inquiry.json").is_file() else {"activities": []}
    acts = inq["activities"]
    checks, preds, figs, texts = [], [], [], {}
    for a in acts:
        q = a.get("question") if isinstance(a.get("question"), dict) else None
        is_choice = a["type"] == "choice" or (q and q.get("type") == "choice")
        if a.get("stage") == "tarkista" and is_choice: checks.append(a["id"])
        if a.get("stage") == "ennusta" and a["type"] == "choice": preds.append(a["id"])
        if a.get("figure") or (q and q.get("figure")) or (a["type"] == "interpret" and "<svg" in a.get("text", "")): figs.append(a["id"])
        if a.get("stage") == "tarkista" and a["type"] in ("choice", "numeric", "explain", "interpret"):
            texts[a["id"]] = words(" ".join(str(a.get(k, "")) for k in ("prompt", "text")) + " " + (q or {}).get("prompt", ""))
    ex_file = courses.lesson_file(folder, "exercises.json")
    ex = json.loads(ex_file.read_text()) if ex_file.is_file() else {}
    items = [e for v in ex.values() for e in v]
    figs += [e["id"] for e in items if e.get("figure")]
    for e in items: texts[e["id"]] = words(e["text"])
    exit_f = folder / "exit-ticket.json"
    exits = json.loads(exit_f.read_text()) if exit_f.is_file() else []
    dup = []
    for i, q in enumerate(exits, 1):
        w = words(q.get("q", "")); best = max(((jaccard(w, v), k) for k, v in texts.items()), default=(0, None))
        if best[0] >= OVERLAP: dup.append(f"exit {i} ~ {best[1]} ({best[0]:.2f})")
    rep = []
    ids = [e["id"] for e in items]
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            j = jaccard(texts[a], texts[b])
            if j >= OVERLAP: rep.append(f"{a} ~ {b} ({j:.2f})")
    opp = []
    if not figs and (courses.code_dir(folder) / "figures.py").is_file():
        reuse = getattr(figcat.module(str(courses.code_dir(folder))), "REUSE", {})
        opp = [f"{lid}/{n}" for n, v in reuse.items() if v.startswith("safe")]
    return {"id": lid, "title": json.loads((folder / "meta.json").read_text())["title"], "checks": checks, "predictions": preds,
            "figure_tasks": figs, "exit": len(exits), "exit_dup": dup, "repeats": rep, "opportunity": opp}


def course_report(code):
    order = [l["id"] for l in courses.course(code).get("lessons", [])]
    rows = [chapter(f) for f in sorted(courses.lessons(code), key=lambda f: order.index(f.name) if f.name in order else len(order))]
    lines = [f"# {code}: arvioinnin auditointi", "",
             f"Generated by `python scripts/assessment.py {code}` (rules in the script); do not edit by hand. *Tarkistukset* = monivalinnat "
             f"vaiheessa Tarkista osaamisesi (tavoite {TARGET[0]}–{TARGET[1]} käsitteellistä, kun luvun käsitteet sitä vaativat); *kuvatehtävät* = "
             "tehtävät, joissa on kuva; *mahdollinen toisto* = sanoista yli puolet samoja.", "",
             "| Luku | Tarkistukset (monivalinta) | Ennusteet | Kuvatehtävät | Exit ticket | Huomiot |", "|---|---|---|---|---|---|"]
    for r in rows:
        notes = []
        if len(r["checks"]) < TARGET[0]: notes.append(f"{len(r['checks'])} monivalintaa Tarkista-vaiheessa")
        if not r["figure_tasks"]: notes.append("ei kuvatehtävää" + (f" (käytettävissä: {', '.join(r['opportunity'])})" if r["opportunity"] else ""))
        if r["exit_dup"]: notes.append("exit ticket mahdollisesti toistaa: " + "; ".join(r["exit_dup"]))
        if r["repeats"]: notes.append("mahdollinen toisto: " + "; ".join(r["repeats"]))
        lines.append(f"| {r['title']} | {len(r['checks'])} | {len(r['predictions'])} | {len(r['figure_tasks'])} | {r['exit']} | {'; '.join(notes) or '–'} |")
    sov = ROOT / "content" / i18n.SOURCE / code / "sovella" / "tasks.json"
    if sov.is_file():
        data = json.loads(sov.read_text()); n = sum(1 for t in data["tasks"] for x in [t] + t["parts"] if x.get("figure"))
        lines += ["", f"Sovella itsenäisesti: {len(data['tasks'])} tehtävää, {n} kuvaviittausta (`\"figure\"`); kuvia voi olla myös tehtävätekstissä."]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    if courses.LESSON_ID.match(a[0]):
        print(json.dumps(chapter(courses.find_lesson(a[0])), ensure_ascii=False, indent=1)); sys.exit(0)
    codes = sorted({f.parent.name for f in courses.lessons()}) if "--all" in a else [x for x in a if not x.startswith("--")]
    bad = 0
    for code in codes:
        out = ROOT / "docs" / "assessment" / f"{code}.md"; text = course_report(code)
        if "--check" in a:
            ok = out.is_file() and out.read_text() == text; bad += not ok
            print(("OK   " if ok else "STALE ") + str(out.relative_to(ROOT)) + ("" if ok else f" (python scripts/assessment.py {code})"))
        else:
            out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text); print("wrote", out.relative_to(ROOT))
    sys.exit(1 if bad else 0)
