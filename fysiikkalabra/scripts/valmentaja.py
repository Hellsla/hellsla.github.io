"""FY9-valmentaja, part 1: the task index (work queue 11b PR 2; docs/FY9_ADAPTIVE_PLAN.md sections 3, 4.1-4.2, 7.2 R9).

The adaptive exam coach is a static page that works on what the student has done on this device. It needs one machine-readable
list of every FY9 task, from one place; this script builds it. It shows nothing to a student and writes no page: the only
output is one JSON file per language (`valmentaja/fy9.json` beside the pages) that later pull requests read.

  python scripts/valmentaja.py check              validate kertaus/FY9.json against the units (CI)
  python scripts/valmentaja.py build [--lang L] [--out DIR]
                                                  write the index of the units reviewed in L (default: every language, into site/)
  python scripts/valmentaja.py report             the tasks per unit and competency; the cells with no automatically checked task

What is read, and what is inferred (plan 4.1: nothing new is added to inquiry.json or tasks.json):
  - a short task is a `choice`, `numeric`, `explain` or `interpret` activity of a FY9 unit's inquiry.json; its id is
    `<unit>#<activity id>` (the activity ids `lt-1`, `tarkistus-2` repeat in every unit, so a bare id is never a key)
  - a long task is a task of the unit's sovella/tasks.json; its id is the task's own id (`fy9-voimat-s1`, unique)
  - competency: a short task's default is its type (choice concept, numeric math, interpret graph, explain communication), a
    long task's is its criteria's competencies by points (competencies.json); kertaus/FY9.json `items` holds the exceptions
  - check: `auto` (a numeric or choice the page checks) or `self` (explain, long tasks: the student's own rubric)
  - minutes: choice 2, numeric 4, interpret 4, explain 5; a long task 3 per point (plan 4.1; provisional, teacher P9)
  - part of the exam: a long task of 15 points is Osa II type, of 20 points Osa III type; short tasks are Osa I type
  - review: the chapters (lesson ids) to revisit, from the task's skills, links, `practice` text and the lesson links in its feedback

kertaus/FY9.json (outside the content folders, so it stales no review) holds only what cannot be inferred: `items`
(unit, competencies, minutes, followups), `misconceptions`, `minikokeet`, `plans` and `koetila` (the practice exam's exam mode, PR 6). `check` fails on a task that does
not exist, a diagnostic task without its unit, and a minikoe whose points or minutes do not add up.
"""
import json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n, practice, units
from courses import ROOT

COURSE = "FY9"
SIDE = ROOT / "kertaus" / "FY9.json"
OUT_NAME = "valmentaja/fy9.json"
VERSION = 1
SHORT = ("choice", "numeric", "explain", "interpret")
TYPE_COMP = {"choice": ["concept"], "numeric": ["math"], "interpret": ["graph"], "explain": ["communication"]}
TYPE_MIN = {"choice": 2, "numeric": 4, "interpret": 4, "explain": 5}
MIN_PER_POINT = 3          # plan 4.1 / P9: the exercise's sizing (6 h for 120 points is 3 min a point), not a claim about the real exam
SHORT_POINTS = 2           # what a short task counts for in a minikoe (plan 6.4: 6 short tasks, 5 answered, 10 points = 30 min)
STAGE_ORDER = ("herata", "ennusta", "tutki", "selita", "sovella", "tarkista")
LESSON_LINK = re.compile(r"\((fy\d+-\d+)\.html\)")
MINI_KINDS = ("osa1", "aihe", "osa2", "aineisto")     # plan 6.4: Osa I, one chapter's short tasks, Osa II type + short, Osa III type
ITEM_KEYS = {"unit", "competencies", "minutes", "followups"}
SIDE_KEYS = {"version", "items", "misconceptions", "minikokeet", "plans", "koetila"}
MINI_KEYS = {"id", "kind", "minutes", "points", "short", "answer", "long", "choose", "chapter"}
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fy9_units(lang=i18n.SOURCE):
    """[unit id] of the FY9 units this language holds, in course order."""
    return [u for u in units.ids(lang) if units.load(u, lang).get("course") == COURSE]


def side():
    return json.loads(SIDE.read_text(encoding="utf-8")) if SIDE.is_file() else {"version": VERSION}


def _lesson_links(*texts):
    found = set()
    for t in texts:
        if isinstance(t, str): found.update(LESSON_LINK.findall(t))
    return found


def _lesson_key(l):
    c = courses.course_of(l) or "FY99"
    return (int(c[2:]) if c[2:].isdigit() else 99, int(l.split("-")[1]))


def _activity_links(a):
    q = a.get("question") or {}
    texts = [a.get("practice"), q.get("practice")]
    for part in (a, q):
        texts += [c.get("feedback") for c in part.get("choices", [])]
        texts += [m.get("feedback") for m in part.get("mistakes", []) if isinstance(m, dict)]
    return _lesson_links(*texts)


def _short_tasks(uid, lang, items):
    """[task] of the unit's short tasks in page order, with the stage they sit in (the long tasks go in after sovella)."""
    inq = json.loads((units.folder(uid, lang) / "inquiry.json").read_text(encoding="utf-8"))
    out = []
    for a in inq["activities"]:
        if a["type"] not in SHORT: continue
        q = a.get("question") or {}
        kind = a["type"]
        check = "auto" if kind in ("choice", "numeric") or q.get("type") in ("choice", "numeric") else "self"
        key = f"{uid}#{a['id']}"
        it = items.get(key, {})
        n_opt = len(a["choices"]) if kind == "choice" else len(a.get("mistakes", [])) if kind == "numeric" else len(q.get("choices", [])) or len(q.get("mistakes", []))
        t = {"id": key, "unit": it.get("unit", uid), "kind": kind, "stage": a["stage"], "check": check,
             "comp": it.get("competencies", TYPE_COMP[kind]), "min": it.get("minutes", TYPE_MIN[kind]),
             "href": f"{uid}.html#{a['id']}", "part": "I", "title": a.get("title") or a["id"],
             "review": sorted(_activity_links(a), key=_lesson_key)}
        if n_opt: t["options"] = n_opt
        if it.get("followups"): t["followups"] = it["followups"]
        out.append(t)
    return out


def _long_tasks(uid, lang, items):
    fw = practice.framework()
    if not units.has_tasks(uid, lang): return []
    out = []
    for t in practice.load(units.task_key(uid), lang)["tasks"]:
        if t.get("kind") == "own": continue
        pts = practice.total(t)
        comp = {c: 0 for c in fw["competencies"]}
        for p in t["parts"]:
            for c in p["criteria"]:
                k = c.get("tag") or fw["criteria"].get(c.get("key"))
                if k in comp: comp[k] += c["points"]
        it = items.get(t["id"], {})
        review = set(t.get("skills", [])) | set((t.get("links") or {}).values())
        r = {"id": t["id"], "unit": it.get("unit", uid), "kind": "long", "stage": "sovella", "check": "self",
             "comp": {k: v for k, v in comp.items() if v}, "min": it.get("minutes", pts * MIN_PER_POINT),
             "href": f"{uid}.html#{t['id']}", "part": "II" if pts == 15 else "III" if pts == 20 else None, "points": pts,
             "title": t["title"], "parts": [{"id": p["id"], "kind": p["kind"], "points": p["points"]} for p in t["parts"]],
             "review": sorted(review, key=_lesson_key)}
        if it.get("followups"): r["followups"] = it["followups"]
        out.append(r)
    return out


def tasks_of(uid, lang, items):
    """Every task of one unit in page order: its short tasks, the long ones after the Sovella stage, then the checks."""
    short, long_ = _short_tasks(uid, lang, items), _long_tasks(uid, lang, items)
    before = [t for t in short if STAGE_ORDER.index(t["stage"]) <= STAGE_ORDER.index("sovella")]
    return before + long_ + [t for t in short if t not in before]


HOME_SHARE = 0.4    # a unit belongs to a course when that course holds at least this share of its tasks' review chapters (PR 4b)


def home_course(unit_tasks):
    """The course (1-8) a unit revises, or None for a unit that spans the course (the exam unit, the practice exam): the course that holds
    at least HOME_SHARE of the review chapters of the unit's tasks, a tie going to the earlier course. Inferred, never written by hand."""
    n = {}
    for t in unit_tasks:
        for l in t.get("review", []):
            c = courses.course_of(l)
            if c and re.fullmatch(r"FY[1-8]", c): n[int(c[2:])] = n.get(int(c[2:]), 0) + 1
    total = sum(n.values())
    if not total: return None
    best = min(n, key=lambda c: (-n[c], c))
    return best if n[best] / total >= HOME_SHARE else None


def build(lang, unit_pub=None):
    """The index of one language: the FY9 units it holds and has published (unit_pub: {unit id: languages}; default the
    units with three current reviews), their tasks, and the fixed minikokeet and plans whose tasks are all there."""
    s = side(); items = s.get("items", {})
    pub = [u for u in fy9_units(lang) if (lang in unit_pub.get(u, ()) if unit_pub is not None else units.status(u, lang)["state"] == "reviewed")]
    tasks = [t for u in pub for t in tasks_of(u, lang, items)]
    out_units = [{"id": u, "chapter": units.load(u, lang)["chapter"], "title": units.load(u, lang)["title"], "n": units.number(u)} for u in pub]
    for o in out_units:       # PR 4b: the course a unit revises (the student's courses decide which units show)
        c = home_course([t for t in tasks if t["unit"] == o["id"]])
        if c: o["course"] = c
    have = {t["id"] for t in tasks}
    mini = [m for m in s.get("minikokeet", []) if set(m.get("short", [])) | set(m.get("long", [])) <= have]
    return {"version": VERSION, "course": COURSE, "lang": lang, "units": out_units, "tasks": tasks,
            "misconceptions": {k: v for k, v in s.get("misconceptions", {}).items() if all(i.split("/")[0] in have for i in v["items"])},
            "minikokeet": mini, "plans": s.get("plans", {}),
            "koetila": {u: {"minutes": c["minutes"], "points": c["minutes"] // MIN_PER_POINT} for u, c in s.get("koetila", {}).items() if u in pub}}   # the exam mode of a unit (PR 6)


def dumps(index):
    return json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n"


def write(lang, out, unit_pub=None):
    """Write the language's index to <out>/valmentaja/fy9.json; returns the file's path relative to out, or None."""
    index = build(lang, unit_pub)
    if not index["units"]: return None
    f = pathlib.Path(out) / OUT_NAME
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(dumps(index), encoding="utf-8")
    return OUT_NAME


def languages():
    return [l for l in units.languages() if fy9_units(l)]


# ---- the pages (work queue 11b PR 4; plan 6.1-6.2): the coach page and the row and tile on the course page ---------------
PAGE = "FY9-valmentaja.html"
UI_KEYS = ("diag", "min", "why_stale", "why_wrong", "why_new", "why_more", "basis", "own", "note", "row_one", "row_n", "go", "clear", "clear_confirm", "nostore", "goal_h", "goal_lead", "goal_none", "goal_LE", "goal_MC", "goal_BA", "courses_h", "courses_lead", "courses_none", "set_note", "steps_h", "mistakes_h", "mistakes_n", "mini_item", "mini_exam")
STATES = ("none", "few", "practise", "growing", "strong", "strongdue")


def _esc(s):
    import html
    return html.escape(str(s), quote=True)


STEP_IDS = ("tulkinta", "annettu", "periaate", "kaava", "muunnokset", "sijoitus", "vastaus", "jarkevyys", "kuvaaja")
STEP_NAMES = {"annettu": "Annettu", "periaate": "Periaate", "kaava": "Kaava", "muunnokset": "Muunnokset", "sijoitus": "Sijoitus",
              "vastaus": "Vastaus", "jarkevyys": "Järkevyys", "kuvaaja": "Kuvaaja"}   # the page's own names of a solution's steps (practice.step_names)


def step_labels(T):
    """{step id: label} of the fixed list of "the hardest step" (PR 5): the names the solution itself shows, and one new one, the reading of the task."""
    names = T("practice.step_names")
    return {i: (T("coach.step_tulkinta") if i == "tulkinta" else names.get(STEP_NAMES[i], STEP_NAMES[i])) for i in STEP_IDS}


def unit_json(T):
    """The texts of the "Mikä vaihe oli vaikein?" row on a unit page (data-t of its script tag)."""
    return _esc(json.dumps({"q": T("coach.hard_q"), "steps": step_labels(T)}, ensure_ascii=False))


def ui_json(T):
    """The texts the script shows, as the JSON in data-t (T: the build's translator)."""
    t = {k: T("coach." + k) for k in UI_KEYS}
    t["steps"] = step_labels(T)
    t.update({"state_" + s: T("coach.state_" + s) for s in STATES})
    t["comp"] = {c: T("competency." + c) for c in practice.framework()["competencies"]}
    t["chapter"] = T("site.chapter_n", n="{n}")
    return _esc(json.dumps(t, ensure_ascii=False))


def index_script(index):
    """The task index inside the page (works offline and from a file; the page makes no request for it)."""
    return '<script type="application/json" id="fy9-index">' + dumps(index).strip().replace("</", "<\\/") + "</script>"


def page_body(T, index, course_page, lang=None, mini=None):
    """The coach page: heading, the next tasks, the competency areas and the data row, filled by templates/valmentaja.js; without the
    script it says so and links to the lessons and the task mixer (plan 7.3)."""
    return (f'<h1>{T("coach.title")}</h1>'
            f'<div class="coach" id="fy9-coach" data-t="{ui_json(T)}" data-diag="fy9-koe.html">'
            f'<noscript><p class="notice" role="note">{T("coach.nojs")}</p></noscript>'
            f'<section aria-labelledby="coach-next-h"><h2 id="coach-next-h">{T("coach.next")}</h2><div id="coach-recs"></div>'
            f'<p class="coach-free"><a href="yo-sekoitin.html">{T("coach.free")}</a> · <a href="{course_page}">{T("site.back_to_course", course="FY9")}</a></p></section>'
            f'<details class="coach-set" id="coach-set" hidden><summary>{T("coach.goal_h")}</summary><div class="coach-set-body"></div></details>'
            f'<details class="coach-areas" id="coach-areas" hidden><summary>{T("coach.areas")}</summary><div class="coach-areas-body"></div></details>'
            f'<details class="coach-areas" id="coach-steps" hidden><summary>{T("coach.steps_h")}</summary><div class="coach-steps-body"></div></details>'
            f'<details class="coach-areas" id="coach-mistakes" hidden><summary>{T("coach.mistakes_h")}</summary><div class="coach-mistakes-body"></div></details>'
            + (f'<details class="coach-areas" id="coach-mini" data-mini="{_esc(json.dumps(mini, ensure_ascii=False))}"><summary>{T("coach.mini_h")}</summary><div class="coach-mini-body"></div></details>' if mini else "") +
            f'<div class="coach-data" id="coach-data"></div></div>' + index_script(index) + (mistakes_script(lang, index) if lang else "") + '<script src="valmentaja.js"></script>')


def mistakes_data(lang, index):
    """{task id: [feedback of the option logged as number i]}: the existing, reviewed feedback of every wrong option and common mistake of the
    index's tasks (plan 4.2: no new text). A number task's number i is its i-th common mistake; a choice's is the position the option was shown in
    (inquiry.choice_order). Embedded in the coach page so that it shows the feedback again without a request."""
    import inquiry
    have = {t["id"] for t in index["tasks"]}
    out = {}
    for u in index["units"]:
        uid = u["id"]
        for a in json.loads((units.folder(uid, lang) / "inquiry.json").read_text(encoding="utf-8"))["activities"]:
            key = f"{uid}#{a['id']}"
            if key not in have: continue
            if a["type"] == "choice":
                fb = [c["feedback"] for c in inquiry.choice_order(a["choices"], uid, a["id"])]
            elif a["type"] == "numeric":
                fb = [m.get("feedback", "") if isinstance(m, dict) else "" for m in a.get("mistakes", [])]
            else:
                continue
            if any(fb): out[key] = fb
    return out


def mistakes_script(lang, index):
    return ('<script type="application/json" id="fy9-mistakes">' + json.dumps(mistakes_data(lang, index), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>")


def row_html(T, index):
    """The row under the course page's heading: hidden until this browser holds evidence (plan 6.1); the script fills it."""
    return (f'<div class="resume coach-row" id="fy9-coach-row" data-href="{PAGE}" data-t="{ui_json(T)}" hidden></div>'
            + index_script(index) + '<script src="valmentaja.js"></script>')


# ---- check ----------------------------------------------------------------------------------------------------------

def _all_tasks():
    """{id: task} of every FY9 task in the source language, published or not (a sidecar may name a draft's task)."""
    items = side().get("items", {})
    return {t["id"]: t for u in fy9_units() for t in tasks_of(u, i18n.SOURCE, items)}


def check():
    errs = []
    if not SIDE.is_file(): return [f"{SIDE.relative_to(ROOT)} is missing"]
    s = side(); tasks = _all_tasks(); fw = practice.framework(); comps = set(fw["competencies"])
    ids = [t["id"] for u in fy9_units() for t in tasks_of(u, i18n.SOURCE, {})]
    errs += [f"duplicate task id {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    if s.get("version") != VERSION: errs.append(f"version must be {VERSION}")
    errs += [f"unknown key '{k}'" for k in sorted(set(s) - SIDE_KEYS)]
    fy9 = set(fy9_units())
    for k, it in s.get("items", {}).items():
        if k not in tasks: errs.append(f"items: '{k}' is not a task of {COURSE}"); continue
        errs += [f"items.{k}: unknown field '{f}'" for f in sorted(set(it) - ITEM_KEYS)]
        if "unit" in it and it["unit"] not in fy9: errs.append(f"items.{k}: unit '{it['unit']}' is not a {COURSE} unit")
        if "competencies" in it:
            c = it["competencies"]
            if not (isinstance(c, list) and c and set(c) <= comps and len(set(c)) == len(c)): errs.append(f"items.{k}: competencies must be a list of {sorted(comps)}")
            if tasks[k]["kind"] == "long": errs.append(f"items.{k}: a long task's competencies come from its criteria")
        if "minutes" in it and not (isinstance(it["minutes"], int) and 1 <= it["minutes"] <= 120): errs.append(f"items.{k}: minutes must be an integer 1-120")
        for f in it.get("followups", []):
            if f not in tasks: errs.append(f"items.{k}: followup '{f}' is not a task of {COURSE}")
            elif f == k: errs.append(f"items.{k}: a task is not its own followup")
    for t in tasks.values():    # the diagnostic tasks review other units' content: they must say which
        if t["id"].startswith("fy9-koe#testi-") and t["unit"] == "fy9-koe": errs.append(f"items: the diagnostic task {t['id']} needs its \"unit\" (the unit whose content it revises)")
        for l in t["review"]:
            if not courses.course_of(l): errs.append(f"{t['id']}: review lesson '{l}' is not a lesson of curriculum.json")
    for name, m in s.get("misconceptions", {}).items():
        if not ID_RE.match(name): errs.append(f"misconceptions: '{name}' is not a slug")
        if len(m.get("items", [])) < 2: errs.append(f"misconceptions.{name}: needs at least two items")
        for ref in m.get("items", []):
            tid, _, n = ref.rpartition("/")
            if tid not in tasks or not n.isdigit() or int(n) >= tasks[tid].get("options", 0): errs.append(f"misconceptions.{name}: '{ref}' is not <task>/<option index>")
    seen = set()
    for m in s.get("minikokeet", []):
        errs += _check_mini(m, tasks, seen)
    for k, p in s.get("plans", {}).items():
        if not (k.isdigit() and isinstance(p.get("days"), int) and p["days"] == int(k) * 7): errs.append(f"plans.{k}: needs \"days\" = {k} weeks in days")
    for lang in units.languages():     # a translation has the same tasks as its source (ids are language-neutral keys)
        if lang == i18n.SOURCE: continue
        for u in fy9_units(lang):
            a = {t["id"] for t in tasks_of(u, lang, {})}; b = {t["id"] for t in tasks_of(u, i18n.SOURCE, {})}
            if a != b: errs.append(f"{lang}/{u}: task ids differ from the source: {sorted(a ^ b)[:4]}")
    return errs


def _chapter(uid):
    return units.load(uid, i18n.SOURCE)["chapter"] if (units.folder(uid, i18n.SOURCE) / "unit.json").is_file() else None


def _check_mini(m, tasks, seen):
    mid = m.get("id", "?"); errs = []
    def bad(msg): errs.append(f"minikokeet.{mid}: {msg}")
    errs_before = len(errs)
    bad_keys = sorted(set(m) - MINI_KEYS)
    if bad_keys: bad(f"unknown field {bad_keys}")
    if not ID_RE.match(str(mid)) or mid in seen: bad("id must be a unique slug")
    seen.add(mid)
    if m.get("kind") not in MINI_KINDS: bad(f"kind must be one of {MINI_KINDS}")
    short, long_ = m.get("short", []), m.get("long", [])
    for i in short:
        if i not in tasks or tasks[i]["kind"] == "long": bad(f"short task '{i}' is not a short task of {COURSE}")
    for i in long_:
        if i not in tasks or tasks[i]["kind"] != "long": bad(f"long task '{i}' is not a long task of {COURSE}")
    if len(set(short)) != len(short) or len(set(long_)) != len(long_): bad("a task is listed twice")
    if len(errs) > errs_before: return errs
    answer = m.get("answer", len(short)); choose = m.get("choose") or len(long_)
    if short and not 1 <= answer <= len(short): bad("answer is the number of short tasks answered, at most the number listed")
    if long_ and not 1 <= choose <= len(long_): bad("choose must be 1 to the number of long tasks")
    if len({tasks[i]["points"] for i in long_}) > 1: bad("the long tasks of one minikoe are worth the same points, so a choice between them costs the same")
    points = answer * SHORT_POINTS * bool(short) + (choose * tasks[long_[0]]["points"] if long_ else 0)
    if m.get("points") != points: bad(f"points {m.get('points')} differ from the budget {points} ({answer} short x {SHORT_POINTS} + {choose} long)")
    want = points * MIN_PER_POINT
    if not isinstance(m.get("minutes"), int) or abs(m["minutes"] - want) > max(3, want // 10): bad(f"minutes {m.get('minutes')} differ from {points} points x {MIN_PER_POINT} min = {want}")
    kind = m.get("kind")
    if kind == "osa1" and (long_ or len(short) < 2): bad("Osa I is short tasks only")
    if kind == "aihe":
        if long_ or m.get("chapter") not in range(1, 8): bad("a topic minikoe is short tasks of one chapter (\"chapter\" 1-7)")
        elif {_chapter(tasks[i]["unit"]) for i in short} != {m["chapter"]}: bad("its short tasks are not all of its chapter")
    if kind == "osa2" and not (short and long_ and {tasks[i]["part"] for i in long_} == {"II"}): bad("Osa II type: short tasks and long tasks of 15 points")
    if kind == "aineisto" and (short or {tasks[i]["part"] for i in long_} != {"III"}): bad("Osa III type: long tasks of 20 points only")
    return errs


# ---- report ---------------------------------------------------------------------------------------------------------

def report():
    """Text: tasks per unit by kind, and the unit x competency cells (a short task counts to the unit it revises) with
    the number of automatically checked tasks; the cells with none are where PR 4's recommender has no quick feedback."""
    fw = practice.framework(); comps = list(fw["competencies"]); tasks = list(_all_tasks().values())
    out = []
    kinds = ("choice", "numeric", "interpret", "explain", "long")
    out.append("tasks per unit: " + " ".join(f"{k}" for k in kinds))
    for u in fy9_units():
        mine = [t for t in tasks if t["href"].startswith(u + ".html")]
        out.append(f"  {u:20} " + " ".join(f"{sum(t['kind'] == k for t in mine):3}" for k in kinds) + f"   {len(mine)} tasks, {sum(t['min'] for t in mine)} min")
    out.append(f"\nunit x competency: automatic tasks (self-assessed tasks) ; {len(tasks)} tasks in all")
    out.append(f"  {'':20} " + " ".join(f"{c[:6]:>9}" for c in comps))
    empty = []
    for u in fy9_units():
        row = []
        for c in comps:
            mine = [t for t in tasks if t["unit"] == u and c in t["comp"]]
            auto = sum(t["check"] == "auto" for t in mine)
            row.append(f"{auto:3} ({len(mine) - auto:3})")
            if not auto: empty.append((u, c, len(mine)))
        out.append(f"  {u:20} " + " ".join(f"{r:>9}" for r in row))
    out.append(f"\ncells without an automatically checked task: {len(empty)} of {len(fy9_units()) * len(comps)}")
    out += [f"  {u} x {c}: {'no task at all' if not n else f'{n} self-assessed'}" for u, c, n in empty]
    return "\n".join(out)


if __name__ == "__main__":
    argv = sys.argv[1:]
    cmd = argv[0] if argv else "check"
    if cmd == "check":
        e = check()
        for x in e: print("ERROR", x)
        print(f"valmentaja: {len(e)} error(s)" if e else f"valmentaja: ok ({len(_all_tasks())} tasks)")
        sys.exit(1 if e else 0)
    elif cmd == "build":
        only = argv[argv.index("--lang") + 1] if "--lang" in argv else None
        base = pathlib.Path(argv[argv.index("--out") + 1]) if "--out" in argv else ROOT / "site"
        for l in ([only] if only else languages()):
            f = write(l, base if l == i18n.SOURCE else base / l)
            print(f"{l}: {f or 'no reviewed FY9 unit'}")
    elif cmd == "report":
        print(report())
    else:
        sys.exit(__doc__)
