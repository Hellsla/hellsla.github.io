"""Sovella itsenäisesti and the self-assessment components (teacher's brief 2026-10-28, NOTES.md §9).

  python scripts/practice.py check [<COURSE>]          the deterministic checks (CI), every course and language by default
  python scripts/practice.py hash <COURSE> [--lang en]  the content hash a reviewer puts in its report
  python scripts/practice.py status                    reviewed | draft of every course's tasks, per language
  python scripts/practice.py figures <COURSE> [--check] lessons/<COURSE>/sovella/figures.py into solutions.md
  python scripts/practice.py packet <COURSE> --role developer|science|pedagogy|visual [--lang en]
                                                       the agent's packet, content/<lang>/<COURSE>/sovella/review/packet-<role>.md

A course's module-end tasks are a part of their own, like a lesson's exercise set:

  content/<lang>/<COURSE>/sovella/tasks.json     the tasks: situation, source material, parts with points, rubric
                                                 criteria, links to chapters (schema: README "Sovella itsenäisesti")
  content/<lang>/<COURSE>/sovella/solutions.md   one worked solution per task: `## <task id>`, `### a)` per part with
                                                 the steps of CLAUDE.md "Lesson form" 7, then `### Yleisiä virheitä`
                                                 (and `### Hyväksytään myös` for other accepted methods)
  content/<lang>/<COURSE>/sovella/review/        science.md and pedagogy.md, the same format as a lesson's
  lessons/<COURSE>/sovella/answers.py            recomputes every number of the solutions from the task data
  lessons/<COURSE>/sovella/figures.py            the solutions' model graphs (scripts/figlib.py)

The page site/<COURSE>-sovella.html is published when both reviews PASS for the current hash (build.py); the course
page links it. Criteria name a shared key of competencies.json (its text is in lang/<lang>.json "criteria", so it is
written and translated once) or carry their own `text` and competency `tag`; a part's points are the sum of its
criteria. The same rubric component (rubric_html, templates/selfassess.js) scores every task of every course (the
chapter-level "Arvioi osaamistasi" of 2026-10-28 was removed by the teacher the same day: guided self-assessment of
written answers lives in the explain tasks, scripts/inquiry.py).
Nothing here needs a model at runtime: links for a weak competency come from the task's `links`.

A course unit (scripts/units.py) can carry a task set of its own in the same format: its key is "units/<unit id>", so
content/<lang>/units/<id>/sovella/ holds tasks.json and solutions.md and lessons/units/<id>/sovella/ answers.py and
figures.py (FY9, the exam review course, teacher 2026-11-04). Its task ids are <unit id>-s<n>, the files are part of
the unit's content hash and reviews (no page of their own), and the unit page shows the tasks last, as its Tehtävät
(render(..., embedded=True)). Any task may name `skills`: the chapters of FY1–FY8 whose skills it uses, by lesson id,
shown as chapter-name links (never an id, teacher's rule 6).

A course's Esimerkkikoe (example exam, teacher 2026-11-05, docs/exam-guidelines.md, command /exam) is a task set in the
same format with the key "<COURSE>/koe": content/<lang>/<COURSE>/koe/ and lessons/<COURSE>/koe/, task ids
<course slug>-k<n>, page site/<COURSE>-koe.html after Sovella itsenäisesti, published when its reviews pass. On top of
the Sovella format tasks.json has `sections` (Osa 1, 2, 3: title, `choose` = how many of its tasks count, the task ids)
and `max_points` (the maximum achievable under the selection rules, checked); parts of kind `choice` are multiple
choice (`options`, `correct` index, fixed points, no criteria), scored by the page, with a `**Perustelu:**` solution.
"""
import hashlib, importlib.util, json, re, subprocess, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n

ROOT = courses.ROOT
DIR = "sovella"
UNIT_PREFIX = "units/"                  # the task set of a course unit: "units/<unit id>"
TEXTS = ("tasks.json", "solutions.md")
CODE = ("answers.py", "figures.py")
KINDS = ("calc", "word", "graph", "own", "choice")
EXAM = "/koe"                           # the example exam of a course: "<COURSE>/koe"
STEPS = {"calc": ["Annettu", "Kysytty", "Periaate", "Kaava", "Muunnokset", "Sijoitus", "Vastaus", "Järkevyys"],
         "word": ["Kysytty", "Periaate", "Mallivastaus"],
         "graph": ["Kysytty", "Kuvaaja", "Mallivastaus"],
         "choice": ["Perustelu"]}
GRAPH_STEP = "Kuvaajan lukeminen"
EXTRA = ("Yleisiä virheitä", "Hyväksytään myös")
MAX_CRITERION = 4                       # points: a criterion worth more is several criteria
TEXT_KEYS = {"intro", "title", "text", "detail", "source_note"}   # what a translation translates in tasks.json


def esc(s): return _h.escape(str(s), quote=True)
def is_exam(code): return code.endswith(EXAM)
def course_of(code): return code[:-len(EXAM)] if is_exam(code) else code
def _sub(code): return code if is_exam(code) else f"{code}/{DIR}"
def folder(code, lang=i18n.SOURCE): return ROOT / "content" / lang / _sub(code)
def code_folder(code): return ROOT / "lessons" / _sub(code)
def page_id(code): return f"{course_of(code)}-koe" if is_exam(code) else f"{code}-sovella"
def page_name(code): return page_id(code) + ".html"
def is_unit(code): return code.startswith(UNIT_PREFIX)
def set_slug(code): return code[len(UNIT_PREFIX):] if is_unit(code) else courses.slug(course_of(code))
def id_pattern(code): return rf"{set_slug(code)}-{'k' if is_exam(code) else 's'}\d+"
def is_choice(task): return bool(task.get("parts")) and all(p.get("kind") == "choice" for p in task["parts"])
def framework(): return json.loads((ROOT / "competencies.json").read_text())


def source(code):
    """The language a task set is written in: Finnish, or a course unit's own language (scripts/units.py lang_of, FY14:
    English); a set in any other language is a translation of it (teacher 2026-11-04, FY9 in en and fi-easy)."""
    if not is_unit(code): return i18n.SOURCE
    import units
    return units.lang_of(set_slug(code)) or i18n.SOURCE


def figure_texts_file(code, lang):
    """A translation's figures.json: in the Sovella folder, for a unit in the unit's folder (one file with its figures)."""
    return (folder(code, lang).parent if is_unit(code) else folder(code, lang)) / "figures.json"


def courses_with(lang=i18n.SOURCE):
    """The courses that have module-end tasks in this language."""
    return [c for c in courses.codes() if (folder(c, lang) / "tasks.json").is_file()]


def exams(lang=i18n.SOURCE):
    """The keys ("<COURSE>/koe") of the courses that have an example exam in this language."""
    return [c + EXAM for c in courses.codes() if (folder(c + EXAM, lang) / "tasks.json").is_file()]


def max_points(data):
    """The maximum achievable score of an exam under its selection rules: per section the `choose` best tasks."""
    by = {t["id"]: total(t) for t in data["tasks"]}
    return sum(sum(sorted((by.get(i, 0) for i in s["tasks"]), reverse=True)[:s.get("choose") or len(s["tasks"])]) for s in data.get("sections", []))


def unit_sets(lang=i18n.SOURCE):
    """The keys ("units/<id>") of the course units that have a task set in this language."""
    base = ROOT / "content" / lang / "units"
    return sorted(UNIT_PREFIX + d.parent.parent.name for d in base.glob(f"*/{DIR}/tasks.json")) if base.is_dir() else []


def answer_list(part):
    """A part's answers: one {value, unit, tolerance} or, when it asks for several quantities (two waxes' coefficients),
    a list of them, each with a `name` that answers.py keys as `<task>-<part>-<name>`."""
    a = part.get("answer")
    return [] if a is None else a if isinstance(a, list) else [a]


def load(code, lang=i18n.SOURCE): return json.loads((folder(code, lang) / "tasks.json").read_text())


def total(task): return sum(p["points"] for p in task["parts"])


def files(code, lang=i18n.SOURCE):
    """[(name, path)] of everything the reviews judge."""
    return [(n, folder(code, lang) / n) for n in TEXTS] + [(n, code_folder(code) / n) for n in CODE]


def content_hash(code, lang=i18n.SOURCE, read=None):
    """The hash the reviews are for. read(relpath) gives a file as a commit had it (reviews.Commit.read, for a carry
    over a teacher-approved figure); default the working tree."""
    from reviews import normalized
    import figcat
    read = read or (lambda rel: (ROOT / rel).read_text() if (ROOT / rel).is_file() else None)
    rel = lambda path: path.relative_to(ROOT).as_posix()
    h = hashlib.sha256()
    for name, path in files(code, lang):
        text = read(rel(path))
        if text is None: continue
        text = figcat.without_reuse(text) if name == "figures.py" else text   # the REUSE note draws nothing
        h.update(name.encode() + b"\0" + normalized(text, name).encode() + b"\0")
    tasks = read(rel(folder(code, lang) / "tasks.json"))   # a figure of another chapter that a task refers to: the code that draws it
    for fid in figcat.refs_in(tasks or ""):
        if figcat.code_rel(fid) == rel(code_folder(code) / "figures.py"): continue   # already in figures.py above
        sl = figcat.slice_of(fid, read)
        if sl: h.update(f"figure:{fid}".encode() + b"\0" + sl.encode() + b"\0")
    return h.hexdigest()[:16]


def status(code, lang=i18n.SOURCE):
    """{'state': reviewed|draft, 'hash', 'reports': {science|pedagogy|visual: PASS|FAIL|stale|missing}, 'baseline'}: the gate
    of reviews.item_status (three reviews; a visual baseline row for exactly this hash stands in for the visual one)"""
    from reviews import item_status
    return item_status("koe" if is_exam(code) else "sovella", code, lang, folder(code, lang), content_hash(code, lang))


# ------------------------------------------------------------------------------------------------ solutions.md
def solution_blocks(text):
    """{task id: {"parts": {part id: body}, "extra": {heading: body}}} of solutions.md."""
    out = {}
    for m in re.finditer(r"^## (\S+)[^\n]*\n(.*?)(?=^## |\Z)", text or "", re.M | re.S):
        parts, extra = {}, {}
        for s in re.finditer(r"^### (.+?)\s*\n(.*?)(?=^### |\Z)", m.group(2), re.M | re.S):
            head = s.group(1).strip()
            pm = re.fullmatch(r"([a-z])\)", head)
            (parts if pm else extra)[pm.group(1) if pm else head] = s.group(2).strip()
        out[m.group(1)] = {"parts": parts, "extra": extra}
    return out


def answers(code):
    f = code_folder(code) / "answers.py"
    if not f.is_file(): return None, f"{f.relative_to(ROOT)} missing"
    r = subprocess.run([sys.executable, "-I", str(f)], capture_output=True, text=True)
    if r.returncode: return None, f"answers.py failed: {r.stderr.strip()[-300:]}"
    try: return json.loads(r.stdout.strip().splitlines()[-1]), None
    except (ValueError, IndexError): return None, "answers.py must print one JSON object {\"<task>-<part>\": value}"


MISSING = []                            # the Finnish texts the last figures() call drew without a translation


def figures(code, lang=i18n.SOURCE, write=True):
    """Put each figure of figures.py into solutions.md in place of its <svg data-fig="name"> block. True when up to date."""
    import figlib
    f = code_folder(code) / "figures.py"
    if not f.is_file(): return True
    sys.path.insert(0, str(ROOT / "scripts"))
    spec = importlib.util.spec_from_file_location(f"figures_{code.replace('/', '_')}", f); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    if lang != source(code):                             # after the import: a figures.py may set its own language there
        tr = figure_texts_file(code, lang)
        figlib.set_language(json.loads(tr.read_text()) if tr.is_file() else {}, i18n.T(lang)("format.decimal"))
    sol = folder(code, lang) / "solutions.md"; text = sol.read_text(); new = text
    for name, fn in mod.FIGURES.items():
        pat = re.compile(r'<svg\b[^>]*\bdata-fig="' + re.escape(name) + r'"[^>]*>.*?</svg>', re.S)
        svg = fn()
        if 'data-fig=' not in svg: svg = svg.replace("<svg ", f'<svg data-fig="{name}" ', 1)
        new = pat.sub(lambda m: svg, new, count=1)
    MISSING[:] = figlib.MISSING if lang != source(code) else []
    figlib.set_language({}, ",")
    if write and new != text: sol.write_text(new)
    return new == text


# ------------------------------------------------------------------------------------------------ checks
def check(code, lang=i18n.SOURCE, seen=None):
    """The deterministic checks of one course's tasks in one language, as messages (empty: all good)."""
    errs = []; where = f"content/{lang}/{_sub(code)}"
    E = lambda m: errs.append(f"{where}: {m}")
    fw = framework(); tags = set(fw["competencies"]); shared = fw["criteria"]; T = i18n.T(lang)
    try: data = load(code, lang)
    except (OSError, ValueError) as e: return [f"{where}/tasks.json: {e}"]
    sol_file = folder(code, lang) / "solutions.md"
    sols = solution_blocks(sol_file.read_text() if sol_file.is_file() else "")
    slug = set_slug(code)
    for key in list(shared) + [f"_{t}" for t in tags]:     # the shared texts every language must have
        k = f"competency.{key[1:]}" if key.startswith("_") else f"criteria.{key}"
        try: i18n.lookup(i18n.strings(lang), k)
        except KeyError: E(f"lang/{lang}.json has no {k}")
    for k, t in shared.items():
        if t not in tags: errs.append(f"competencies.json: criterion {k} has the unknown competency {t!r}")
    tasks = data.get("tasks")
    if not isinstance(tasks, list) or not tasks: return errs + [f"{where}/tasks.json: no tasks"]
    import figcat                                      # "figure": "<id>" on a task or a part (scripts/figcat.py)
    for _, msg in figcat.check_refs(json.dumps(data)): E(f"tasks.json: {msg}")
    for task in tasks:
        tid = task.get("id", "?"); W = lambda m: E(f"{tid}: {m}")
        if not re.fullmatch(id_pattern(code), str(tid)): W(f"id must be {slug}-{'k' if is_exam(code) else 's'}<n>")
        if any(p.get("kind") == "choice" for p in task.get("parts") or []) and not is_choice(task): W("a multiple-choice task has only parts of kind choice")
        if seen is not None:
            if tid in seen: W(f"duplicate task id (also in {seen[tid]})")
            seen[tid] = code
        for k in ("title", "text"):
            if not str(task.get(k, "")).strip(): W(f"no {k}")
        own = task.get("kind") == "own"
        parts = task.get("parts") or []
        if not parts: W("no parts")
        ids = [p.get("id") for p in parts]
        if ids != [chr(ord("a") + i) for i in range(len(parts))]: W(f"part ids must be a, b, c … in order, not {ids}")
        used = set()
        for p in parts:
            pid = f"{tid}-{p.get('id')}"; P = lambda m: E(f"{pid}: {m}")
            kind = p.get("kind")
            if kind not in KINDS: P(f"kind must be one of {KINDS}")
            if (kind == "own") != own: P("kind own belongs to a task of kind own (its student's own work), and only there")
            if not str(p.get("text", "")).strip(): P("no text")
            if kind == "choice":
                opts, ok = p.get("options"), p.get("correct")
                if not (isinstance(opts, list) and 3 <= len(opts) <= 5 and all(isinstance(o, str) and o.strip() for o in opts)): P("options: 3–5 texts")
                elif len(set(opts)) != len(opts): P("options must differ")
                elif not (isinstance(ok, int) and 0 <= ok < len(opts)): P("correct: the index of the right option")
                if not (isinstance(p.get("points"), int) and 1 <= p["points"] <= MAX_CRITERION): P(f"points: a whole number 1–{MAX_CRITERION}")
                if p.get("criteria"): P("a choice part is scored by the page: no criteria")
                used.add(p.get("tag", "concept"))
                if p.get("tag", "concept") not in tags: P(f"tag {p.get('tag')!r} is not one of {sorted(tags)}")
            crit = [] if kind == "choice" else p.get("criteria") or []
            if not crit and kind != "choice": P("no rubric criteria")
            pts = 0
            for i, c in enumerate(crit):
                n = c.get("points")
                if not (isinstance(n, int) and 1 <= n <= MAX_CRITERION): P(f"criterion {i + 1}: points must be a whole number 1–{MAX_CRITERION}"); n = 0
                pts += n
                if "key" in c:
                    if c["key"] not in shared: P(f"criterion {i + 1}: unknown shared criterion {c['key']!r} (competencies.json)")
                    if "text" in c or "tag" in c: P(f"criterion {i + 1}: a shared criterion takes its text and competency from its key; add a `detail` instead")
                    tag = shared.get(c["key"])
                else:
                    if not str(c.get("text", "")).strip(): P(f"criterion {i + 1}: needs a shared `key` or its own `text`")
                    tag = c.get("tag")
                    if tag not in tags: P(f"criterion {i + 1}: competency tag {tag!r} is not one of {sorted(tags)}")
                used.add(tag)
            if kind != "choice" and p.get("points") != pts: P(f"points {p.get('points')} differ from the sum of its criteria {pts}")
            if own: continue
            body = sols.get(tid, {}).get("parts", {}).get(p.get("id"))
            if body is None: P("no worked solution (`### " + str(p.get("id")) + ")` under `## " + tid + "` in solutions.md)"); continue
            from check_solutions import check_steps
            needed = list(STEPS.get(kind, []))
            if kind == "calc" and "**" + GRAPH_STEP in body: needed.insert(needed.index("Kaava"), GRAPH_STEP)
            for m in check_steps(body, [T("practice.step_names").get(n, n) for n in needed]): P(f"solution: {m}")   # the language's step names
            if kind == "graph" and "<svg" not in body: P("a graph part's solution shows the model graph (<svg data-fig> from figures.py)")
            for a in answer_list(p):
                if not (isinstance(a, dict) and isinstance(a.get("value"), (int, float)) and "unit" in a): P("answer must be {value, unit[, tolerance]} or a list of them, each with its `name`")
            if isinstance(p.get("answer"), list) and len({a.get("name") for a in p["answer"] if isinstance(a, dict)}) != len(p["answer"]): P("each answer of a list needs its own `name`")
        if not own:
            if tid not in sols: W("no `## " + tid + "` in solutions.md")
            elif "Yleisiä virheitä" not in sols[tid]["extra"]: W("no `### Yleisiä virheitä` in its solution")
            for head in sols.get(tid, {}).get("extra", {}):
                if head not in EXTRA: W(f"unknown solution section `### {head}` (parts are `### a)`, then {', '.join(EXTRA)})")
        skills = task.get("skills", [])
        if not isinstance(skills, list) or not all(isinstance(x, str) for x in skills): W("skills: a list of lesson ids (the chapters whose skills the task uses)")
        else:
            for lid in skills:
                if not any(l["id"] == lid for c in courses.codes() for l in courses.course(c).get("lessons", [])): W(f"skills: {lid!r} is not a lesson of curriculum.json")
                elif not (ROOT / "content" / i18n.SOURCE / courses.course_of(lid) / lid / "meta.json").is_file(): W(f"skills: lesson {lid} has no folder yet")
        links = task.get("links") or {}
        for tag in used - set(links):
            if tag in tags: W(f"no link for the competency {tag!r}: links names the chapter to practise it in")
        for tag, lid in links.items():
            if tag not in tags: W(f"links: unknown competency {tag!r}")
            elif not any(l["id"] == lid for c in courses.codes() for l in courses.course(c).get("lessons", [])): W(f"links.{tag}: {lid!r} is not a lesson of curriculum.json")
            elif not (ROOT / "content" / i18n.SOURCE / courses.course_of(lid) / lid / "meta.json").is_file(): W(f"links.{tag}: lesson {lid} has no folder yet")
    if is_exam(code):                                  # sections and selection rules (docs/exam-guidelines.md)
        secs = data.get("sections")
        if not isinstance(secs, list) or not secs: E("tasks.json: an exam has `sections`")
        else:
            listed = [i for s in secs for i in s.get("tasks", [])]
            if sorted(listed) != sorted(t.get("id") for t in tasks): E(f"sections must list every task once: {listed}")
            by = {t.get("id"): t for t in tasks}
            for s in secs:
                n, ch = len(s.get("tasks", [])), s.get("choose")
                if not str(s.get("title", "")).strip(): E("a section has no title")
                if ch is not None and not (isinstance(ch, int) and 1 <= ch < n): E(f"{s.get('title')}: choose must be 1–{n - 1} (or left out: every task counts)")
                if ch and len({total(by[i]) for i in s.get("tasks", []) if i in by}) > 1: E(f"{s.get('title')}: the tasks to choose from are worth the same")
            if data.get("max_points") != max_points(data): E(f"max_points {data.get('max_points')} differs from the sections' maximum {max_points(data)}")
    extra_sols = set(sols) - {t.get("id") for t in tasks}
    if extra_sols: E(f"solutions.md has blocks for unknown tasks {sorted(extra_sols)}")
    src = source(code)
    if lang == src:
        got, err = answers(code)
        if err: E(err)
        else:
            for task in tasks:
                for p in task["parts"]:
                    for a in answer_list(p):
                        if not isinstance(a, dict) or not isinstance(a.get("value"), (int, float)): continue
                        k = f"{task['id']}-{p['id']}" + (f"-{a.get('name')}" if isinstance(p["answer"], list) else "")
                        if k not in got: E(f"{k}: answers.py does not compute this part's answer"); continue
                        tol = a.get("tolerance", 0.02); v = a["value"]
                        if abs(got[k] - v) > tol * abs(v if v else 1): E(f"{k}: tasks.json answer {v} differs from answers.py {got[k]} (tolerance {tol})")
        try:
            if not figures(code, lang, write=False): E("solutions.md figures differ from figures.py (python scripts/practice.py figures " + code + ")")
        except Exception as e: E(f"figures.py: {e}")
    else:                                                  # a translation: the same tasks, points, criteria and links
        from check_i18n import formulas
        terrs = []; _same(load(code, src), data, "tasks.json", terrs)
        errs += [f"{where}/{e}" for e in terrs]
        try:
            if not figures(code, lang, write=False): E(f"solutions.md figures differ from figures.py in {lang} (python scripts/practice.py figures {code} --lang {lang})")
            if MISSING: E(f"{figure_texts_file(code, lang).relative_to(ROOT)} has no translation for: " + "; ".join(MISSING)[:400])
        except Exception as e: E(f"figures.py: {e}")
        fs = solution_blocks((folder(code, src) / "solutions.md").read_text())
        for tid, b in fs.items():
            o = sols.get(tid)
            if o is None: E(f"solutions.md: no `## {tid}`"); continue
            if set(b["parts"]) != set(o["parts"]): E(f"solutions.md {tid}: parts {sorted(o['parts'])} differ from Finnish {sorted(b['parts'])}")
            for pid in b["parts"]:
                if pid in o["parts"] and formulas(b["parts"][pid]) != formulas(o["parts"][pid]): E(f"solutions.md {tid} {pid}): formulas differ from Finnish")
    return errs


def _same(a, b, path, errs, key=None):
    """b is a translation of a: same keys, lists, ids, points, answers and links; only TEXT_KEYS differ (formulas kept)."""
    from check_i18n import formulas
    if isinstance(a, dict):
        if not isinstance(b, dict) or set(a) != set(b): errs.append(f"{path}: keys differ from Finnish"); return
        for k in a: _same(a[k], b[k], f"{path}.{k}", errs, k)
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b): errs.append(f"{path}: {len(a)} items in Finnish"); return
        for i, (x, y) in enumerate(zip(a, b)): _same(x, y, f"{path}[{i}]", errs, key)
    elif isinstance(a, str) and key in TEXT_KEYS:
        if formulas(a) != formulas(b): errs.append(f"{path}: formulas differ from Finnish")
    elif a != b: errs.append(f"{path}: {b!r} differs from Finnish {a!r} (only texts are translated)")


# ------------------------------------------------------------------------------------------------ page parts
def chapter(lid):
    """The chapter title of a lesson (curriculum.json, the language's courses.json) for a link; never its id."""
    code = courses.course_of(lid)
    title = next((l["title"] for l in courses.course(code)["lessons"] if l["id"] == lid), lid)
    f = ROOT / "content" / i18n.t.lang / "courses.json"
    if i18n.t.lang != i18n.SOURCE and f.is_file():
        title = json.loads(f.read_text()).get(code, {}).get("lessons", {}).get(lid, title)
    return title


def criterion_text(c, md):
    T = i18n.t
    text = T(f"criteria.{c['key']}") if "key" in c else c["text"]
    detail = f' <span class="crit-detail">{md(c["detail"])}</span>' if c.get("detail") else ""
    return md(text) + detail


def rubric_html(task, md, parts=None, lead=None):
    """The shared rubric and self-assessment component: per part its criteria, each with point buttons 0..max (partial
    credit), the self-assessed total and, for a competency scored at most half, links to the chapters in the task's
    links (templates/selfassess.js). Works for any task of any course; every text but the criteria is lang "practice"."""
    T = i18n.t; tid = task["id"]; inline = lambda s: re.sub(r"^<p>(.*)</p>$", r"\1", md(s).strip(), flags=re.S)
    rows = ""
    for p in (parts or task["parts"]):
        crit = ""
        for i, c in enumerate(p["criteria"]):
            tag = c.get("tag") or framework()["criteria"][c["key"]]
            name = f"{tid}-{p['id']}-{i}"
            opts = "".join(f'<label><input type="radio" name="{name}" value="{n}"><span>{n}</span></label>' for n in range(c["points"] + 1))
            crit += (f'<fieldset class="crit" data-tag="{tag}" data-max="{c["points"]}"><legend class="crit-text">{criterion_text(c, inline)}'
                     f' <span class="pts">{T("practice.points", n=c["points"])}</span></legend><div class="crit-points">{opts}</div></fieldset>')
        head = f'<p class="rubric-part-h">{p["id"]})<span class="pts">{T("practice.points", n=p["points"])}</span></p>' if p["kind"] != "own" else ""
        rows += f'<div class="rubric-part">{head}{crit}</div>'
    links = "".join(f'<li data-tag="{tag}" hidden>{T("competency." + tag)}: <a href="{lid}.html">{esc(chapter(lid))}</a></li>'
                    for tag, lid in task.get("links", {}).items())
    mx = total(task)
    return (f'<div class="rubric" data-id="{tid}" data-max="{mx}"><p class="rubric-lead">{lead or T("practice.rubric_lead")}</p>{rows}'
            f'<p class="rubric-total" aria-live="polite">{T("js.rubric_partial", got=0, max=mx, left=sum(len(p["criteria"]) for p in task["parts"]))}</p>'
            f'<p class="rubric-note">{T("practice.rubric_note")}</p>'
            + (f'<div class="rubric-more" hidden><p>{T("practice.practise_more")}</p><ul>{links}</ul></div>' if links else "") + '</div>')


def _with_figures(solution_html, body):
    """A solution with its figures: the SVG is kept out of the step layout (nl2br would put <br> inside it) and put back
    as a block of its own."""
    figs = []
    def stash(m): figs.append(m.group(0)); return f"\n\nFIGTOKEN{len(figs) - 1}X\n\n"
    out = solution_html(re.sub(r"<svg\b.*?</svg>", stash, body, flags=re.S))
    return re.sub(r"(?:<p>)?FIGTOKEN(\d+)X(?:</p>)?", lambda m: f'<div class="fig">{figs[int(m.group(1))]}</div>', out)


def skills_html(task):
    """'Taidot luvuista: <chapter>, <chapter>': where the skills of a task were taught, by chapter name."""
    if not task.get("skills"): return ""
    return (f'<p class="task-skills">{i18n.t("practice.skills")} '
            + ", ".join(f'<a href="{lid}.html">{esc(chapter(lid))}</a>' for lid in task["skills"]) + "</p>")


def number(n, prefix=None):
    """A task's number: on a module's Sovella itsenäisesti page its place on the page ("2", the page is the module's
    own and holds a few tasks); in a review unit's task set the unit's number and the place, "1.2-3", like a chapter's
    exercises "6-3" (teacher 2026-11-04)."""
    return f"{prefix}-{n}" if prefix else str(n)


def choice_html(task, p, inline):
    """A multiple-choice part: its options as radio buttons; the page scores it when the solution is opened."""
    name = f"{task['id']}-{p['id']}"
    opts = "".join(f'<li><label class="mc-opt"><input type="radio" name="{name}" value="{i}"><span>{inline(o)}</span></label></li>'
                   for i, o in enumerate(p["options"]))
    return f'<ul class="choices mc" data-id="{name}" data-correct="{p["correct"]}" data-points="{p["points"]}">{opts}</ul>'


def _card(task, sols, md, solution_html):
    """(badge, situation, parts, reveal, points label) of one task card, shared by the Sovella, unit and exam pages."""
    T = i18n.t; tid, own = task["id"], task.get("kind") == "own"
    inline = lambda s: re.sub(r"^<p>(.*)</p>$", r"\1", md(s).strip(), flags=re.S)
    import figcat
    fig = lambda x: figcat.figure_html(x["figure"], i18n.t.lang) if x.get("figure") else ""   # a task's or a part's figure by its id
    src = task.get("source")
    badge = ((f'<p class="source" data-source="{src}"><strong>{T("inquiry.source_" + src)}</strong>' if src else '<p class="source">')
             + (f'{" · " if src else ""}{inline(task["source_note"])}' if task.get("source_note") else "") + '</p>') if (src or task.get("source_note")) else ""
    parts = "" if own else "<ol class=\"parts\">" + "".join(
        f'<li><span class="part-id">{p["id"]})</span> <span class="part-text">{inline(p["text"])}</span> <span class="pts">{T("practice.points", n=p["points"])}</span>{fig(p)}'
        + (choice_html(task, p, inline) if p["kind"] == "choice" else "") + '</li>'
        for p in task["parts"]) + "</ol>"
    if own:
        reveal = (f'<details class="reveal"><summary>{T("practice.own_reveal")}</summary><div class="reveal-body">'
                  f'{rubric_html(task, md, lead=T("practice.own_rubric_lead"))}</div></details>')
    else:
        s = sols.get(tid, {"parts": {}, "extra": {}}); kinds = {p["id"]: p for p in task["parts"]}
        def head(pid):
            p = kinds.get(pid)
            if p and p["kind"] == "choice":
                return f'<h4 class="sol-part">{pid}) <span class="mc-key">{T("exam.correct", option=inline(p["options"][p["correct"]]))}</span></h4>'
            return f'<h4 class="sol-part">{pid})</h4>'
        sol = "".join(f'{head(pid)}<div class="steps">{_with_figures(solution_html, b)}</div>' for pid, b in s["parts"].items())
        extra = "".join(f'<h3>{T("practice.mistakes" if h == "Yleisiä virheitä" else "practice.also")}</h3>{md(b)}' for h, b in s["extra"].items())
        score = (f'<p class="mc-score" data-id="{tid}" data-max="{total(task)}" aria-live="polite"></p>' if is_choice(task)
                 else f'<h3>{T("practice.rubric")}</h3>{rubric_html(task, md)}')
        reveal = (f'<details class="reveal"><summary>{T("practice.reveal")} <span class="reveal-hint">{T("practice.reveal_hint")}</span></summary>'
                  f'<div class="reveal-body">{score if is_choice(task) else ""}<h3>{T("practice.solution")}</h3>{sol}{extra}{"" if is_choice(task) else score}</div></details>')
    pts = T.count("practice.task_points", total(task)) if not own else T("practice.kind_own")
    return badge, f'<div class="situation">{md(task["text"])}{fig(task)}</div>', parts, reveal, pts


def render(code, lang, md, solution_html, title, embedded=False, prefix=None):
    """(body html, toc html) of the course's Sovella itsenäisesti page; embedded=True: the tasks only, each a task card
    under an h3, for the end of a unit page (no header, no stage sections, no table of contents). prefix: the unit's
    number, so the tasks are numbered "1.2-1", "1.2-2" (number())."""
    if is_exam(code): return render_exam(code, lang, md, solution_html)
    T = i18n.t; data = load(code, lang)
    sols = solution_blocks((folder(code, lang) / "solutions.md").read_text() if (folder(code, lang) / "solutions.md").is_file() else "")
    body = "" if embedded else (f'<header class="practice-head"><span class="eyebrow">{T("practice.eyebrow", code=code)}</span><h1>{T("practice.title")}</h1>'
            f'<p class="lead">{T("practice.lead")}</p>' + (md(data["intro"]) if data.get("intro") else "")
            + f'<p class="howto">{T("practice.howto")}</p></header>')
    toc = ""
    for n, task in enumerate(data["tasks"], 1):
        tid = task["id"]
        badge, situation, parts, reveal, pts = _card(task, sols, md, solution_html)
        if embedded:
            body += (f'<div class="activity task-card practice-task" id="{tid}" data-type="practice" data-written="1" data-num="{number(n, prefix)}"><h3>{(f'<span class="ex-num"><span class="visually-hidden">{T("lesson.exercise_word")} </span>{number(n, prefix)}</span> ' if prefix else f"{n}. ")}{esc(task["title"])} <span class="pts">{pts}</span></h3>'
                     f'{badge}{situation}{parts}{skills_html(task)}{reveal}</div>')
            continue
        body += (f'<section class="stage practice-task" id="{tid}"><h2><span class="stage-no" aria-hidden="true">{n}</span>{esc(task["title"])}'
                 f' <span class="pts">{pts}</span></h2><div class="activity task-card" data-written="1">{badge}{situation}{parts}{skills_html(task)}{reveal}</div></section>')
        toc += (f'<a href="#{tid}"><span class="toc-no" aria-hidden="true">{n}</span><span class="toc-label">{esc(task["title"])}</span></a>')
    return body, toc


def render_exam(code, lang, md, solution_html):
    """(body html, toc html) of a course's Esimerkkikoe: the instructions with the selection rules and the maximum, one
    section per Osa (its rule, its task cards numbered through the exam), then the exam's own total: the student's
    points per section counted under its rule (templates/selfassess.js), so offered points never pass for the maximum."""
    T = i18n.t; data = load(code, lang); course = course_of(code)
    sols = solution_blocks((folder(code, lang) / "solutions.md").read_text() if (folder(code, lang) / "solutions.md").is_file() else "")
    by = {t["id"]: t for t in data["tasks"]}; mx = max_points(data)
    def rule(sec):
        n, ch = len(sec["tasks"]), sec.get("choose")
        each = {total(by[i]) for i in sec["tasks"]}
        if ch: return T("exam.rule_choose", choose=ch, n=n, points=next(iter(each)), max=ch * next(iter(each)))
        return T("exam.rule_all", max=sum(total(by[i]) for i in sec["tasks"]))
    rules = "".join(f'<li><strong>{esc(s["title"])}</strong>: {rule(s)}</li>' for s in data["sections"])
    offered = sum(total(t) for t in data["tasks"])
    body = (f'<header class="practice-head exam-head"><span class="eyebrow">{T("exam.eyebrow", code=course)}</span><h1>{T("exam.title")}</h1>'
            f'<p class="lead">{T("exam.lead")}</p>' + (md(data["intro"]) if data.get("intro") else "")
            + f'<div class="exam-rules"><h2>{T("exam.rules")}</h2><ul>{rules}</ul>'
            f'<p class="exam-max">{T("exam.max", max=mx, offered=offered)}</p>'
            + (f'<p>{T("exam.minutes", minutes=data["minutes"])}</p>' if data.get("minutes") else "")
            + f'<p class="howto">{T("exam.howto")}</p></div></header>')
    toc = ""; n = 0
    for k, sec in enumerate(data["sections"], 1):
        cards = ""
        for tid in sec["tasks"]:
            n += 1; task = by[tid]
            badge, situation, parts, reveal, pts = _card(task, sols, md, solution_html)
            cards += (f'<div class="activity task-card practice-task exam-task" id="{tid}"><h3>{n}. {esc(task["title"])} <span class="pts">{pts}</span></h3>'
                      f'{badge}{situation}{parts}{skills_html(task)}{reveal}</div>')
        sid = f"osa-{k}"
        body += (f'<section class="stage exam-section" id="{sid}" data-choose="{sec.get("choose") or len(sec["tasks"])}"><h2><span class="stage-no" aria-hidden="true">{k}</span>{esc(sec["title"])}</h2>'
                 f'<p class="exam-rule">{rule(sec)}</p>{cards}</section>')
        toc += f'<a href="#{sid}"><span class="toc-no" aria-hidden="true">{k}</span><span class="toc-label">{esc(sec["title"])}</span></a>'
    body += (f'<section class="stage exam-total" id="kokeen-pisteet" data-max="{mx}"><h2>{T("exam.total_title")}</h2>'
             f'<p class="exam-total-line" aria-live="polite">{T("js.exam_total", got=0, max=mx)}</p><p class="rubric-note">{T("exam.total_note")}</p>'
             + "".join(f'<p class="exam-sec-line" data-sec="osa-{k}">{esc(s["title"])}: <span>0</span> / {sum(sorted((total(by[i]) for i in s["tasks"]), reverse=True)[:s.get("choose") or len(s["tasks"])])} p</p>'
                       for k, s in enumerate(data["sections"], 1))
             + f'<p>{T("exam.revise")}</p></section>')
    toc += f'<a href="#kokeen-pisteet"><span class="toc-no" aria-hidden="true">Σ</span><span class="toc-label">{T("exam.total_title")}</span></a>'
    return body, toc


# ------------------------------------------------------------------------------------------------ packets
def packet(code, role, lang=i18n.SOURCE):
    """The agent's packet: the course's scope, the framework, the shared criteria and the files to write or judge. An
    agent reads this file and nothing else of the course (token economy: no lesson texts)."""
    if is_unit(code): return unit_packet(code, role, lang)
    c = courses.course(course_of(code)); fw = framework(); T = i18n.T(lang); st = status(code, lang)
    what = "Esimerkkikoe" if is_exam(code) else "Sovella itsenäisesti"
    lines = [f"# {what} {code} ({lang}): {role} packet", "",
             f"Course: {code} {c['title']}, {c.get('op', '')} op. Content hash now: {st['hash']} (python scripts/practice.py hash {code}"
             + (f" --lang {lang}" if lang != i18n.SOURCE else "") + "). Reports: " + ", ".join(f"{k}={v}" for k, v in st["reports"].items()), "",
             "## Scope", "Central contents: " + "; ".join(c.get("keskeiset_sisallot", [])), "Goals: " + "; ".join(c.get("tavoitteet", []))]
    lines += ["Scope notes: " + n for n in c.get("scope_notes", [])]
    if is_exam(code):
        lines += ["", "## Exam design (docs/exam-guidelines.md, the only exam brief; no reference exam is needed or allowed)",
                  (ROOT / "docs" / "exam-guidelines.md").read_text().strip(), ""]
    lines += ["Chapters (link targets, by id): " + "; ".join(f"{l['id']} {l['title']}" for l in c.get("lessons", [])), "",
              "## Framework (competencies.json, NOTES.md §9)"] + [f"- {k}: {v} ({T('competency.' + k)})" for k, v in fw["competencies"].items()]
    lines += ["", "## Shared criteria (lang \"criteria\"; use the key, add `detail` for the task's specifics)"] + [f"- {k} [{t}]: {T('criteria.' + k)}" for k, t in fw["criteria"].items()]
    errs = check(code, lang)
    lines += ["", "## Deterministic checks", "\n".join(errs) if errs else "practice.py check: OK"]
    got, err = answers(code)
    lines += ["", "## answers.py output", err or json.dumps(got, ensure_ascii=False)]
    if role == "developer":
        pid = page_id(code)
        lines += ["", "## Your job", "Write or fix tasks.json, solutions.md, answers.py and figures.py (schema and rules: README \"Sovella itsenäisesti\", NOTES.md §9"
                  + (", docs/exam-guidelines.md" if is_exam(code) else "") + "). "
                  "Run `python scripts/practice.py figures " + code + "` and `python scripts/practice.py check " + code + "` until OK, then "
                  "`python scripts/build.py " + pid + "` and `python scripts/check_layout.py " + pid + " --width 360` (and 768, 1280)."]
    else:
        lines += ["", "## Your job", f"Judge the files below as the {role} reviewer (.claude/agents/{role}-reviewer.md, \"Sovella itsenäisesti\"). "
                  f"Write {(folder(code, lang) / 'review' / (role + '.md')).relative_to(ROOT)}: line 1 `VERDICT: PASS|FAIL`, line 2 `CONTENT-HASH: {st['hash']}`, then Blocking, Polish, Checked (under 400 words)."]
    for name, path in files(code, lang):
        if path.is_file():
            txt = re.sub(r"<svg\b.*?</svg>", "<svg …figure from figures.py…>", path.read_text(), flags=re.S) if name == "solutions.md" else path.read_text()
            lines += ["", f"## {path.relative_to(ROOT)}", "```", txt.rstrip(), "```"]
    out = folder(code, lang) / "review" / f"packet-{role}.md"
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text("\n".join(lines) + "\n")
    return out


def unit_packet(code, role, lang=i18n.SOURCE):
    """A unit's task set is reviewed with its unit (one hash, scripts/units.py): this packet is the developer's
    checklist for it, the framework, the shared criteria, the chapters it may name and the checks."""
    fw = framework(); T = i18n.T(lang); uid = set_slug(code)
    lines = [f"# Task set of unit {uid} ({lang}): {role} packet", "",
             "## Chapters of FY1–FY8 with a folder (ids for `skills` and `links`)"]
    for c in courses.codes():
        ls = [l for l in courses.course(c).get("lessons", []) if (ROOT / "content" / i18n.SOURCE / c / l["id"] / "meta.json").is_file()]
        if ls: lines.append(f"- {c}: " + "; ".join(f"{l['id']} {l['title']}" for l in ls))
    lines += ["", "## Framework (competencies.json, NOTES.md §9)"] + [f"- {k}: {v} ({T('competency.' + k)})" for k, v in fw["competencies"].items()]
    lines += ["", "## Shared criteria (lang \"criteria\"; use the key, add `detail` for the task's specifics)"] + [f"- {k} [{t}]: {T('criteria.' + k)}" for k, t in fw["criteria"].items()]
    errs = check(code, lang)
    lines += ["", "## Deterministic checks", "\n".join(errs) if errs else "practice.py check: OK"]
    for name, path in files(code, lang):
        if path.is_file():
            txt = re.sub(r"<svg\b.*?</svg>", "<svg …figure from figures.py…>", path.read_text(), flags=re.S) if name == "solutions.md" else path.read_text()
            lines += ["", f"## {path.relative_to(ROOT)}", "```", txt.rstrip(), "```"]
    out = folder(code, lang) / "review" / f"packet-{role}.md"
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text("\n".join(lines) + "\n")
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    lang = a[a.index("--lang") + 1] if "--lang" in a else i18n.SOURCE
    cmd, rest = a[0], [x for x in a[1:] if not x.startswith("--") and x != lang]
    if cmd == "check":
        errs, seen = [], {}
        for lg in i18n.languages():
            for code in courses_with(lg) + unit_sets(lg) + exams(lg):
                if rest and code != rest[0]: continue
                e = check(code, lg, seen if lg == source(code) else None); errs += e
                print(("FAIL " if e else "OK   ") + f"{lg}/{code}: {len(load(code, lg)['tasks'])} tasks, {sum(total(t) for t in load(code, lg)['tasks'])} points")
        for e in errs: print("  " + e)
        sys.exit(1 if errs else 0)
    elif cmd == "hash": print(content_hash(rest[0], lang))
    elif cmd == "status":
        for lg in i18n.languages():
            for code in courses_with(lg) + exams(lg):
                s = status(code, lg); print(f"{lg}/{code} {'koe' if is_exam(code) else 'sovella'}: {s['state']} ({', '.join(f'{k}={v}' for k, v in s['reports'].items())}) hash {s['hash']}")
    elif cmd == "figures":
        ok = figures(rest[0], lang, write="--check" not in a)
        print("figures up to date" if ok else ("solutions.md figures differ from figures.py" if "--check" in a else "wrote the figures into solutions.md"))
        sys.exit(0 if ok or "--check" not in a else 1)
    elif cmd == "packet":
        if a[a.index("--role") + 1] == "visual":            # the visual & editorial reviewer's packet (scripts/review_packet.py item_packet)
            import review_packet; review_packet.item_packet(page_id(rest[0]), lang)
        else: print(packet(rest[0], a[a.index("--role") + 1], lang).relative_to(ROOT))
    else: sys.exit(__doc__)
