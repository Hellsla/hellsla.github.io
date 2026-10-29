"""Competency coverage of a course (teacher's brief 2026-10-28, NOTES.md §9): where each competency of competencies.json is
taught and practised, from what the activities actually ask, not from tags.

  python scripts/coverage.py <COURSE>           write docs/coverage/<COURSE>.md
  python scripts/coverage.py <COURSE> --check   exit 1 when the committed report is out of date (CI)
  python scripts/coverage.py --all [--check]    every course with Sovella itsenäisesti tasks (a course gets its report with them)

Evidence is derived deterministically from each activity's form (inquiry.json, the exercise levels, the Sovella
itsenäisesti rubric), so it cannot be claimed by tagging:

  activity                               competency      the student            support
  choice (prediction, check, error)      concept         recognises             guided (feedback)
  explain (conclusion, check)            communication   produces               guided (model answer)
  experiment on the simulation           experiment      produces (measures)    guided (setup given)
  interpret with data or a graph         graph           recognises / produces  guided
  numeric (transfer, check)              math            produces               guided when it has hints
  exercises level 1–2                    math            produces               guided (one formula, solution shown)
  exercises level 3                      transfer        produces               independent
  Sovella task criterion                 its tag         produces               independent, point-assessed

What this cannot see (a graph drawn by the simulation is not a graph the student built; a prompt that names its
formula is not independent model choice) is why graph construction counts only from a rubric's graph_axes and
graph_points criteria, and why the pedagogy reviewer judges the report's gaps. A gap is a competency with no
independent production in the course, or none assessed in Sovella itsenäisesti; fewer than THIN rubric points in
Sovella itsenäisesti is reported as thin evidence.

Force diagrams (docs/force-diagrams.md, teacher 2026-10-29): a lesson's curriculum entry may plan the force-diagram
skills it practises, "fbd": ["identify", "select", "error", "draw", "equations"], and its tasks say which one each
practises ("fbd": "draw" on an inquiry activity, an exercise or an exit-ticket question). The report then has a
section "Voimakuvio" per lesson, and --check fails when a built lesson lacks a planned skill.
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n, practice

ROOT = courses.ROOT
THIN = 3   # fewer self-assessed Sovella points than this is reported as thin evidence, not as covered
RULES = {"choice": ("concept", "tunnistaa", "ohjattu"), "explain": ("communication", "tuottaa", "ohjattu"),
         "experiment": ("experiment", "tuottaa", "ohjattu"), "reflect": ("concept", "tuottaa", "ohjattu")}


def evidence(code):
    """[(lesson id, activity, competency, produces?, independent?[, Sovella points])] of the course's lessons and Sovella tasks."""
    out = []
    for lesson in courses.course(code).get("lessons", []):
        lid = lesson["id"]; f = ROOT / "content" / i18n.SOURCE / code / lid
        if not (f / "meta.json").is_file(): continue
        inq = json.loads((f / "inquiry.json").read_text()) if (f / "inquiry.json").is_file() else {"activities": []}
        for a in inq["activities"]:
            t, aid = a["type"], a["id"]
            if t in RULES:
                comp, act, sup = RULES[t]; out.append((lid, aid, comp, act == "tuottaa", False))
            elif t == "numeric":
                out.append((lid, aid, "math", True, not a.get("hints")))
            elif t == "interpret":
                q = (a.get("question") or {}).get("type")
                out.append((lid, aid, "graph", q in ("numeric", "explain"), False))
                if q == "numeric": out.append((lid, aid, "math", True, False))
        ex = f / "exercises" / "exercises.json"
        if ex.is_file():
            for lvl, items in json.loads(ex.read_text()).items():
                for e in items:
                    out.append((lid, e["id"], "transfer" if lvl.endswith("3") else "math", True, lvl.endswith("3")))
    if (practice.folder(code) / "tasks.json").is_file():
        shared = practice.framework()["criteria"]
        for task in practice.load(code)["tasks"]:
            for p in task["parts"]:
                for c in p["criteria"]:
                    tag = c.get("tag") or shared[c["key"]]
                    out.append(("sovella", f"{task['id']}-{p['id']}", tag, True, True, c["points"]))
                    if c.get("key") in ("graph_axes", "graph_points"): out.append(("sovella", f"{task['id']}-{p['id']}", "graph-build", True, True, c["points"]))
    return out


FBD = ("identify", "select", "error", "draw", "equations")
FBD_FI = {"identify": "tunnistaa voimat", "select": "valitsee oikean kuvion", "error": "löytää virheen", "draw": "piirtää itse", "equations": "liikeyhtälöt kuviosta"}


def fbd_tags(code):
    """{lesson id: {tag: [task ids]}} of the course's built lessons: the force-diagram skill each task practises."""
    out = {}
    for lesson in courses.course(code).get("lessons", []):
        f = ROOT / "content" / i18n.SOURCE / code / lesson["id"]
        if not (f / "meta.json").is_file(): continue
        tags = out.setdefault(lesson["id"], {})
        def add(x, tid):
            if isinstance(x, dict) and x.get("fbd") in FBD: tags.setdefault(x["fbd"], []).append(tid)
        if (f / "inquiry.json").is_file():
            for a in json.loads((f / "inquiry.json").read_text())["activities"]: add(a, a["id"]); add(a.get("question"), a["id"])
        if (f / "exercises" / "exercises.json").is_file():
            for items in json.loads((f / "exercises" / "exercises.json").read_text()).values():
                for e in items: add(e, e["id"])
        if (f / "exit-ticket.json").is_file():
            et = json.loads((f / "exit-ticket.json").read_text())
            for i, q in enumerate(et if isinstance(et, list) else et.get("questions", [])): add(q, f"exit-{i + 1}")
    return out


def fbd_missing(code):
    """[(lesson id, planned tag)] that a built lesson plans in curriculum.json but no task practises."""
    tags = fbd_tags(code)
    return [(l["id"], t) for l in courses.course(code).get("lessons", []) if l["id"] in tags for t in l.get("fbd", []) if not tags[l["id"]].get(t)]


def fbd_section(code):
    lessons = [l for l in courses.course(code).get("lessons", []) if l.get("fbd")]
    if not lessons: return []
    tags = fbd_tags(code)
    lines = ["", "## Voimakuvio", "", "Suunnitelma `curriculum.json` (\"fbd\") ja tehtävät, joiden \"fbd\" kertoo harjoiteltavan taidon "
             "(docs/force-diagrams.md). Monivalinta yksin ei osoita, että oppilas osaa piirtää voimakuvion: jokaisessa voimakuvioluvussa on piirrä itse -tehtävä.", "",
             "| Luku | " + " | ".join(FBD_FI[t] for t in FBD) + " |", "|---|" + "---|" * len(FBD)]
    for l in lessons:
        got = tags.get(l["id"])
        cells = [("–" if t not in l["fbd"] else "suunniteltu") if got is None else
                 (str(len(got.get(t, []))) if got.get(t) else ("**puuttuu**" if t in l["fbd"] else "–")) for t in FBD]
        lines.append(f"| {l['title']}{'' if got is not None else ' (ei vielä rakennettu)'} | " + " | ".join(cells) + " |")
    return lines


def report(code):
    T = i18n.T(i18n.SOURCE); fw = practice.framework()["competencies"]
    ev = evidence(code); titles = {l["id"]: l["title"] for l in courses.course(code).get("lessons", [])}
    lines = [f"# {code}: osaamisten kattavuus", "",
             "Generated by `python scripts/coverage.py " + code + "` from what each activity asks (rules in the script); do not edit by hand. "
             "*Tuottaa* = the student produces an answer (a number, a text, a measurement), *tunnistaa* = picks one; "
             "*itsenäinen* = no hints, no named formula in the step, solution only after the attempt.", "",
             "| Osaaminen | Luvuissa: tunnistaa / tuottaa / itsenäisesti | Esimerkkejä | Sovella itsenäisesti | Aukko |", "|---|---|---|---|---|"]
    gaps = []
    for comp in list(fw) + ["graph-build"]:
        name = T(f"competency.{comp}") if comp in fw else "– siitä kuvaajan laatiminen aineistosta"
        ch = [e for e in ev if e[2] == comp and e[0] != "sovella"]; sv = [e for e in ev if e[2] == comp and e[0] == "sovella"]
        rec, prod, ind = sum(not e[3] for e in ch), sum(e[3] for e in ch), sum(e[3] and e[4] for e in ch)
        rank = {}
        for e in ch: rank[e[0]] = rank.get(e[0], 0) + (2 if e[4] else 1 if e[3] else 0.5)   # independent production counts most
        best = sorted(rank, key=lambda l: (-rank[l], list(titles).index(l)))
        ex = "; ".join(titles[l] for l in best[:2]) + (f" (+{len(best) - 2})" if len(best) > 2 else "")
        tasks = ", ".join(sorted({e[1].rsplit("-", 1)[0] + " " + e[1].rsplit("-", 1)[1] + ")" for e in sv}))
        gap = []
        if not sv: gap.append("ei Sovella-tehtävässä")
        if comp != "graph-build" and not ind and not sv: gap.append("ei itsenäistä tuottamista")
        if comp == "graph-build" and not sv: gap.append("oppilas ei laadi kuvaajaa itse")
        pts = sum(e[5] for e in sv)
        if 0 < pts < THIN: gap.append(f"ohut näyttö: {pts} p Sovella-tehtävissä")
        if gap: gaps.append(f"{name}: {', '.join(gap)}")
        lines.append(f"| {name} | {rec} / {prod} / {ind} | {ex or '–'} | {tasks or '–'} | {', '.join(gap) or '–'} |")
    lines += ["", "## Luvuittain", "", "| Luku | " + " | ".join(T(f"competency.{c}") for c in fw) + " |", "|---|" + "---|" * len(fw)]
    for lid, title in titles.items():
        row = [e for e in ev if e[0] == lid]
        if not row: continue
        lines.append(f"| {title} | " + " | ".join(f"{sum(e[2] == c for e in row)}" + ("*" if any(e[2] == c and e[4] for e in row) else "") for c in fw) + " |")
    lines += ["", "\\* = mukana itsenäistä tuottamista (tason 3 tehtävä tai vihjeetön lasku).", "",
              "## Aukot", ""] + ([f"- {g}" for g in gaps] or ["- Ei aukkoja tällä tarkkuudella; pedagogiikkatarkastaja arvioi, ovatko tehtävät aidosti itsenäisiä."])
    return "\n".join(lines + fbd_section(code)) + "\n"


if __name__ == "__main__":
    a = sys.argv[1:]
    fbd_courses = [c for c in courses.codes() if any(l.get("fbd") for l in courses.course(c).get("lessons", []))]
    codes = list(dict.fromkeys(practice.courses_with() + fbd_courses)) if "--all" in a else [x for x in a if not x.startswith("--")]
    if not codes: sys.exit(__doc__)
    bad = 0
    for code in codes:
        out = ROOT / "docs" / "coverage" / f"{code}.md"; text = report(code)
        if "--check" in a:
            ok = out.is_file() and out.read_text() == text; bad += not ok
            print(("OK   " if ok else "STALE ") + str(out.relative_to(ROOT)) + ("" if ok else f" (python scripts/coverage.py {code})"))
            for lid, t in fbd_missing(code):
                bad += 1; print(f"MISSING {lid}: plans the force-diagram skill \"{t}\" but no task has \"fbd\": \"{t}\" (docs/force-diagrams.md)")
        else:
            out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text); print("wrote", out.relative_to(ROOT))
    sys.exit(1 if bad else 0)
