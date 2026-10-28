"""Sovella itsenäisesti and the self-assessment components (teacher's brief 2026-10-28, NOTES.md §9).

  python scripts/practice.py check [<COURSE>]          the deterministic checks (CI), every course and language by default
  python scripts/practice.py hash <COURSE> [--lang en]  the content hash a reviewer puts in its report
  python scripts/practice.py status                    reviewed | draft of every course's tasks, per language
  python scripts/practice.py figures <COURSE> [--check] lessons/<COURSE>/sovella/figures.py into solutions.md
  python scripts/practice.py packet <COURSE> --role developer|science|pedagogy [--lang en]
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
"""
import hashlib, importlib.util, json, re, subprocess, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n

ROOT = courses.ROOT
DIR = "sovella"
TEXTS = ("tasks.json", "solutions.md")
CODE = ("answers.py", "figures.py")
KINDS = ("calc", "word", "graph", "own")
STEPS = {"calc": ["Annettu", "Kysytty", "Periaate", "Kaava", "Muunnokset", "Sijoitus", "Vastaus", "Järkevyys"],
         "word": ["Kysytty", "Periaate", "Mallivastaus"],
         "graph": ["Kysytty", "Kuvaaja", "Mallivastaus"]}
GRAPH_STEP = "Kuvaajan lukeminen"
EXTRA = ("Yleisiä virheitä", "Hyväksytään myös")
MAX_CRITERION = 4                       # points: a criterion worth more is several criteria
TEXT_KEYS = {"intro", "title", "text", "detail", "source_note"}   # what a translation translates in tasks.json


def esc(s): return _h.escape(str(s), quote=True)
def folder(code, lang=i18n.SOURCE): return ROOT / "content" / lang / code / DIR
def code_folder(code): return ROOT / "lessons" / code / DIR
def page_name(code): return f"{code}-sovella.html"
def framework(): return json.loads((ROOT / "competencies.json").read_text())


def courses_with(lang=i18n.SOURCE):
    """The courses that have module-end tasks in this language."""
    return [c for c in courses.codes() if (folder(c, lang) / "tasks.json").is_file()]


def load(code, lang=i18n.SOURCE): return json.loads((folder(code, lang) / "tasks.json").read_text())


def total(task): return sum(p["points"] for p in task["parts"])


def files(code, lang=i18n.SOURCE):
    """[(name, path)] of everything the reviews judge."""
    return [(n, folder(code, lang) / n) for n in TEXTS] + [(n, code_folder(code) / n) for n in CODE]


def content_hash(code, lang=i18n.SOURCE):
    from reviews import normalized
    import figcat
    h = hashlib.sha256()
    for name, path in files(code, lang):
        if not path.is_file(): continue
        text = figcat.without_reuse(path.read_text()) if name == "figures.py" else path.read_text()   # the REUSE note draws nothing
        h.update(name.encode() + b"\0" + normalized(text, name).encode() + b"\0")
    tasks = folder(code, lang) / "tasks.json"           # a figure of another chapter that a task refers to: the code that draws it
    for fid in figcat.refs_in(tasks.read_text() if tasks.is_file() else ""):
        if figcat.code_rel(fid) == (code_folder(code) / "figures.py").relative_to(ROOT).as_posix(): continue   # already in figures.py above
        sl = figcat.slice_of(fid, lambda rel: (ROOT / rel).read_text() if (ROOT / rel).is_file() else None)
        if sl: h.update(f"figure:{fid}".encode() + b"\0" + sl.encode() + b"\0")
    return h.hexdigest()[:16]


def status(code, lang=i18n.SOURCE):
    """{'state': reviewed|draft, 'hash', 'reports': {science|pedagogy: PASS|FAIL|stale|missing}}"""
    from reviews import report, REVIEWS
    h = content_hash(code, lang); reports = {}
    for name in REVIEWS:
        r = report(folder(code, lang), name)
        reports[name] = "missing" if r is None else r[0] if r[1] == h else "stale"
    return {"state": "reviewed" if all(v == "PASS" for v in reports.values()) else "draft", "hash": h, "reports": reports}


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
    if not f.is_file(): return None, f"lessons/{code}/{DIR}/answers.py missing"
    r = subprocess.run([sys.executable, "-I", str(f)], capture_output=True, text=True)
    if r.returncode: return None, f"answers.py failed: {r.stderr.strip()[-300:]}"
    try: return json.loads(r.stdout.strip().splitlines()[-1]), None
    except (ValueError, IndexError): return None, "answers.py must print one JSON object {\"<task>-<part>\": value}"


def figures(code, lang=i18n.SOURCE, write=True):
    """Put each figure of figures.py into solutions.md in place of its <svg data-fig="name"> block. True when up to date."""
    import figlib
    f = code_folder(code) / "figures.py"
    if not f.is_file(): return True
    sys.path.insert(0, str(ROOT / "scripts"))
    if lang != i18n.SOURCE:
        tr = folder(code, lang) / "figures.json"
        figlib.set_language(json.loads(tr.read_text()) if tr.is_file() else {}, i18n.T(lang)("format.decimal"))
    spec = importlib.util.spec_from_file_location(f"figures_{code}", f); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    sol = folder(code, lang) / "solutions.md"; text = sol.read_text(); new = text
    for name, fn in mod.FIGURES.items():
        pat = re.compile(r'<svg\b[^>]*\bdata-fig="' + re.escape(name) + r'"[^>]*>.*?</svg>', re.S)
        svg = fn()
        if 'data-fig=' not in svg: svg = svg.replace("<svg ", f'<svg data-fig="{name}" ', 1)
        new = pat.sub(lambda m: svg, new, count=1)
    figlib.set_language({}, ",")
    if write and new != text: sol.write_text(new)
    return new == text


# ------------------------------------------------------------------------------------------------ checks
def check(code, lang=i18n.SOURCE, seen=None):
    """The deterministic checks of one course's tasks in one language, as messages (empty: all good)."""
    errs = []; where = f"content/{lang}/{code}/{DIR}"
    E = lambda m: errs.append(f"{where}: {m}")
    fw = framework(); tags = set(fw["competencies"]); shared = fw["criteria"]; T = i18n.T(lang)
    try: data = load(code, lang)
    except (OSError, ValueError) as e: return [f"{where}/tasks.json: {e}"]
    sol_file = folder(code, lang) / "solutions.md"
    sols = solution_blocks(sol_file.read_text() if sol_file.is_file() else "")
    slug = courses.slug(code)
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
        if not re.fullmatch(rf"{slug}-s\d+", str(tid)): W(f"id must be {slug}-s<n>")
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
            crit = p.get("criteria") or []
            if not crit: P("no rubric criteria")
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
            if p.get("points") != pts: P(f"points {p.get('points')} differ from the sum of its criteria {pts}")
            if own: continue
            body = sols.get(tid, {}).get("parts", {}).get(p.get("id"))
            if body is None: P("no worked solution (`### " + str(p.get("id")) + ")` under `## " + tid + "` in solutions.md)"); continue
            from check_solutions import check_steps
            needed = list(STEPS.get(kind, []))
            if kind == "calc" and "**" + GRAPH_STEP in body: needed.insert(needed.index("Kaava"), GRAPH_STEP)
            for m in check_steps(body, needed): P(f"solution: {m}")
            if kind == "graph" and "<svg" not in body: P("a graph part's solution shows the model graph (<svg data-fig> from figures.py)")
            a = p.get("answer")
            if a is not None and not (isinstance(a, dict) and isinstance(a.get("value"), (int, float)) and "unit" in a): P("answer must be {value, unit[, tolerance]}")
        if not own:
            if tid not in sols: W("no `## " + tid + "` in solutions.md")
            elif "Yleisiä virheitä" not in sols[tid]["extra"]: W("no `### Yleisiä virheitä` in its solution")
            for head in sols.get(tid, {}).get("extra", {}):
                if head not in EXTRA: W(f"unknown solution section `### {head}` (parts are `### a)`, then {', '.join(EXTRA)})")
        links = task.get("links") or {}
        for tag in used - set(links):
            if tag in tags: W(f"no link for the competency {tag!r}: links names the chapter to practise it in")
        for tag, lid in links.items():
            if tag not in tags: W(f"links: unknown competency {tag!r}")
            elif not any(l["id"] == lid for c in courses.codes() for l in courses.course(c).get("lessons", [])): W(f"links.{tag}: {lid!r} is not a lesson of curriculum.json")
            elif not (ROOT / "content" / i18n.SOURCE / courses.course_of(lid) / lid / "meta.json").is_file(): W(f"links.{tag}: lesson {lid} has no folder yet")
    extra_sols = set(sols) - {t.get("id") for t in tasks}
    if extra_sols: E(f"solutions.md has blocks for unknown tasks {sorted(extra_sols)}")
    if lang == i18n.SOURCE:
        got, err = answers(code)
        if err: E(err)
        else:
            for task in tasks:
                for p in task["parts"]:
                    a = p.get("answer")
                    if not isinstance(a, dict) or not isinstance(a.get("value"), (int, float)): continue
                    k = f"{task['id']}-{p['id']}"
                    if k not in got: E(f"{k}: answers.py does not compute this part's answer"); continue
                    tol = a.get("tolerance", 0.02); v = a["value"]
                    if abs(got[k] - v) > tol * abs(v if v else 1): E(f"{k}: tasks.json answer {v} differs from answers.py {got[k]} (tolerance {tol})")
        try:
            if not figures(code, lang, write=False): E("solutions.md figures differ from figures.py (python scripts/practice.py figures " + code + ")")
        except Exception as e: E(f"figures.py: {e}")
    else:                                                  # a translation: the same tasks, points, criteria and links
        from check_i18n import formulas
        terrs = []; _same(load(code), data, "tasks.json", terrs)
        errs += [f"{where}/{e}" for e in terrs]
        fs = solution_blocks((folder(code) / "solutions.md").read_text())
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


def render(code, lang, md, solution_html, title):
    """(body html, toc html) of the course's Sovella itsenäisesti page."""
    T = i18n.t; data = load(code, lang)
    sols = solution_blocks((folder(code, lang) / "solutions.md").read_text() if (folder(code, lang) / "solutions.md").is_file() else "")
    inline = lambda s: re.sub(r"^<p>(.*)</p>$", r"\1", md(s).strip(), flags=re.S)
    import figcat
    fig = lambda x: figcat.figure_html(x["figure"], lang) if x.get("figure") else ""   # a task's or a part's figure by its id
    body = (f'<header class="practice-head"><span class="eyebrow">{T("practice.eyebrow", code=code)}</span><h1>{T("practice.title")}</h1>'
            f'<p class="lead">{T("practice.lead")}</p>' + (md(data["intro"]) if data.get("intro") else "")
            + f'<p class="howto">{T("practice.howto")}</p></header>')
    toc = ""
    for n, task in enumerate(data["tasks"], 1):
        tid, own = task["id"], task.get("kind") == "own"
        src = task.get("source")
        badge = ((f'<p class="source" data-source="{src}"><strong>{T("inquiry.source_" + src)}</strong>' if src else '<p class="source">')
                 + (f'{" · " if src else ""}{inline(task["source_note"])}' if task.get("source_note") else "") + '</p>') if (src or task.get("source_note")) else ""
        parts = "" if own else "<ol class=\"parts\">" + "".join(
            f'<li><span class="part-id">{p["id"]})</span> <span class="part-text">{inline(p["text"])}</span> <span class="pts">{T("practice.points", n=p["points"])}</span>{fig(p)}</li>'
            for p in task["parts"]) + "</ol>"
        if own:
            reveal = (f'<details class="reveal"><summary>{T("practice.own_reveal")}</summary><div class="reveal-body">'
                      f'{rubric_html(task, md, lead=T("practice.own_rubric_lead"))}</div></details>')
        else:
            s = sols.get(tid, {"parts": {}, "extra": {}})
            sol = "".join(f'<h4 class="sol-part">{pid})</h4><div class="steps">{_with_figures(solution_html, b)}</div>' for pid, b in s["parts"].items())
            extra = "".join(f'<h3>{T("practice.mistakes" if h == "Yleisiä virheitä" else "practice.also")}</h3>{md(b)}' for h, b in s["extra"].items())
            reveal = (f'<details class="reveal"><summary>{T("practice.reveal")} <span class="reveal-hint">{T("practice.reveal_hint")}</span></summary>'
                      f'<div class="reveal-body"><h3>{T("practice.solution")}</h3>{sol}{extra}<h3>{T("practice.rubric")}</h3>{rubric_html(task, md)}</div></details>')
        pts = T("practice.task_points", n=total(task)) if not own else T("practice.kind_own")
        body += (f'<section class="stage practice-task" id="{tid}"><h2><span class="stage-no" aria-hidden="true">{n}</span>{esc(task["title"])}'
                 f' <span class="pts">{pts}</span></h2><div class="activity task-card">{badge}<div class="situation">{md(task["text"])}{fig(task)}</div>{parts}{reveal}</div></section>')
        toc += (f'<a href="#{tid}"><span class="toc-no" aria-hidden="true">{n}</span><span class="toc-label">{esc(task["title"])}</span></a>')
    return body, toc


# ------------------------------------------------------------------------------------------------ packets
def packet(code, role, lang=i18n.SOURCE):
    """The agent's packet: the course's scope, the framework, the shared criteria and the files to write or judge. An
    agent reads this file and nothing else of the course (token economy: no lesson texts)."""
    c = courses.course(code); fw = framework(); T = i18n.T(lang); st = status(code, lang)
    lines = [f"# Sovella itsenäisesti {code} ({lang}): {role} packet", "",
             f"Course: {code} {c['title']}, {c.get('op', '')} op. Content hash now: {st['hash']} (python scripts/practice.py hash {code}"
             + (f" --lang {lang}" if lang != i18n.SOURCE else "") + "). Reports: " + ", ".join(f"{k}={v}" for k, v in st["reports"].items()), "",
             "## Scope", "Central contents: " + "; ".join(c.get("keskeiset_sisallot", [])), "Goals: " + "; ".join(c.get("tavoitteet", []))]
    lines += ["Scope notes: " + n for n in c.get("scope_notes", [])]
    lines += ["Chapters (link targets, by id): " + "; ".join(f"{l['id']} {l['title']}" for l in c.get("lessons", [])), "",
              "## Framework (competencies.json, NOTES.md §9)"] + [f"- {k}: {v} ({T('competency.' + k)})" for k, v in fw["competencies"].items()]
    lines += ["", "## Shared criteria (lang \"criteria\"; use the key, add `detail` for the task's specifics)"] + [f"- {k} [{t}]: {T('criteria.' + k)}" for k, t in fw["criteria"].items()]
    errs = check(code, lang)
    lines += ["", "## Deterministic checks", "\n".join(errs) if errs else "practice.py check: OK"]
    got, err = answers(code)
    lines += ["", "## answers.py output", err or json.dumps(got, ensure_ascii=False)]
    if role == "developer":
        lines += ["", "## Your job", "Write or fix tasks.json, solutions.md, answers.py and figures.py (schema and rules: README \"Sovella itsenäisesti\", NOTES.md §9). "
                  "Run `python scripts/practice.py figures " + code + "` and `python scripts/practice.py check " + code + "` until OK, then "
                  "`python scripts/build.py " + code + "-sovella` and `python scripts/check_layout.py " + code + "-sovella --width 360` (and 768, 1280)."]
    else:
        lines += ["", "## Your job", f"Judge the files below as the {role} reviewer (.claude/agents/{role}-reviewer.md, \"Sovella itsenäisesti\"). "
                  f"Write content/{lang}/{code}/{DIR}/review/{role}.md: line 1 `VERDICT: PASS|FAIL`, line 2 `CONTENT-HASH: {st['hash']}`, then Blocking, Polish, Checked (under 400 words)."]
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
            for code in courses_with(lg):
                if rest and code != rest[0]: continue
                e = check(code, lg, seen if lg == i18n.SOURCE else None); errs += e
                print(("FAIL " if e else "OK   ") + f"{lg}/{code}: {len(load(code, lg)['tasks'])} tasks, {sum(total(t) for t in load(code, lg)['tasks'])} points")
        for e in errs: print("  " + e)
        sys.exit(1 if errs else 0)
    elif cmd == "hash": print(content_hash(rest[0], lang))
    elif cmd == "status":
        for lg in i18n.languages():
            for code in courses_with(lg):
                s = status(code, lg); print(f"{lg}/{code} sovella: {s['state']} ({', '.join(f'{k}={v}' for k, v in s['reports'].items())}) hash {s['hash']}")
    elif cmd == "figures":
        ok = figures(rest[0], lang, write="--check" not in a)
        print("figures up to date" if ok else ("solutions.md figures differ from figures.py" if "--check" in a else "wrote the figures into solutions.md"))
        sys.exit(0 if ok or "--check" not in a else 1)
    elif cmd == "packet":
        print(packet(rest[0], a[a.index("--role") + 1], lang).relative_to(ROOT))
    else: sys.exit(__doc__)
