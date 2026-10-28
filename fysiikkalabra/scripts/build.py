"""Render content/ folders into site/. Usage: python scripts/build.py [lesson-id | --all]

Without an argument only lessons whose reviews are current are built (scripts/reviews.py: state reviewed, or
legacy for a prototype lesson kept visible by the teacher), into site/ (committed, served by GitHub Pages).
The exercise set is reviewed on its own (exercises/, README "Exercises"): a published page shows the exercises
both reviewers last passed (reviews.published_exercises: the working tree, or an earlier commit while a new
version waits for review), and a note instead when no version has passed yet.
With a lesson id that lesson is built regardless of its state into the git-ignored preview/; with --all every
lesson is (CI uses this to test drafts too). So a draft can never end up in the published folder.
The plain build renders into site.tmp/, checks that every expected page is there and swaps it in only then,
so a failed build never leaves site/ incomplete. A lesson that is on the live site but whose reviews are no
longer current is left out with a WARNING (an annotation on CI), never silently.

Page anatomy (human decisions 2026-10-25 and 2026-10-26, CLAUDE.md "Lesson page"): the worked example is shown in
stages split by `<!-- vaihe -->` lines (staged_example); the formula section `## Kaava: <law>` is headed by the
law's name (named_sections); a figure sits beside the paragraph it explains on a wide screen (fig_rows). Each
exercise gets a browser-side answer check and, its complete worked solution from solutions.md behind its
own "Näytä ratkaisu" button (teacher 2026-10-27: every exercise, meta.solutions "all"; scripts/check_solutions.py); the exercises close the page, after the exit ticket.
A lesson with inquiry.json (scripts/inquiry.py, docs/inquiry.md) is laid out as inquiry stages: the theory
sections, simulation and exit ticket are placed where the stages say. Without it (the classic layout) the
simulation goes after the formula section (before "## Esimerkki") or where lesson.md has a line `<!-- sim -->`.

Assets come from the course's folders (scripts/courses.py): a simulation folder assets/sims/<course>/<name>/ is
published whole at sims/<course>/<name>/ (sim.js, its sim.css and images; a shared one once, however many lessons use
it), and the pictures the text refers to (pics/<course>/<file>, shared/pics/<file>) at the same path under the
output folder, so every reference is relative and works on GitHub Pages under any base path. FY3's simulations
stay in their lesson folders and keep their <id>-sim.js URLs.
"""
import json, os, sys, re, shutil, pathlib, atexit, html as _h, markdown
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from reviews import status as review_status, published_exercises, WorkTree
import courses, i18n, inquiry, mathlayout, practice
from i18n import t as T

ROOT = pathlib.Path(os.environ.get("FYSIIKKALABRA_ROOT") or pathlib.Path(__file__).resolve().parents[1])   # tests build a copy
HOME = "../../index.html"                      # the portfolio front page, two levels above site/ (set per language)
BASE_URL = "https://hellsla.github.io/fysiikkalabra/site/"
URL = BASE_URL                                 # where the language being built is published: site/, site/<lang>/
UP = ""                                        # from a page to site/: "" for Finnish, "../" for site/<lang>/
COURSES = {}                                   # content/<lang>/courses.json of the language being built
arg = sys.argv[1] if len(sys.argv) > 1 else None
build_all = arg == "--all"; only = None if build_all else arg
LIVE = ROOT / "site"                                  # committed, served by GitHub Pages
SITE = ROOT / ("preview" if (only or build_all) else "site.tmp")   # the plain build renders here and swaps it in at the end
if SITE.name == "site.tmp":
    if SITE.exists(): shutil.rmtree(SITE)             # leftover of an interrupted build
    SITE.mkdir()
    atexit.register(lambda: shutil.rmtree(SITE, ignore_errors=True))   # a failed build leaves nothing behind (already gone after the swap)
else:
    SITE.mkdir(exist_ok=True)                         # preview/ is shared by agents building at the same time, so it is never wiped
TPL = ROOT / "templates"
for f in ("site.css", "lesson.js", "sim-embed.js", "inquiry.js", "selfassess.js"): shutil.copy(TPL / f, SITE / f)
shutil.copytree(TPL / "vendor", SITE / "vendor", dirs_exist_ok=True)   # p5 + KaTeX, no CDN needed
tpl = (TPL / "lesson.html").read_text()
page_tpl = (TPL / "page.html").read_text()
curriculum = json.loads((ROOT / "curriculum.json").read_text())


def render_md(text, **kw):
    """Markdown -> HTML, with LaTeX kept out of markdown's reach.
    ```latex fences become $$...$$; every $$...$$ and $...$ is swapped for a token first,
    so underscores, backslashes and asterisks inside maths are not read as markdown."""
    text = re.sub(r"```latex\n(.*?)```", lambda m: "\n$$" + m.group(1).strip() + "$$\n", text, flags=re.S)
    maths = []
    def stash(m):
        x = m.group(0)
        if x.startswith("$$"): x = "$$" + mathlayout.align_equals(x[2:-2]) + "$$"   # equals signs of a calculation in one column
        else: x = mathlayout.split_list(x[1:-1]) or x                                # a list of values may wrap between its items
        maths.append(x); return f"MATHTOKEN{len(maths) - 1}X"
    text = re.sub(r"\$\$.*?\$\$|\$[^$\n]+?\$", stash, text, flags=re.S)
    html = markdown.markdown(text, extensions=["fenced_code", "tables"] + kw.get("extensions", []))
    return re.sub(r"MATHTOKEN(\d+)X", lambda m: maths[int(m.group(1))], html)


UNIT = r"(?:N/kg|m/s²|m/s|km/h|kPa|MPa|Pa|°C|K|kN|N|kg|g|km|cm²|cm|mm|m³|m|s|min|h|kJ|J|kW|W|dm³|l|Hz|%)"


def nbsp_units(text):
    """A non-breaking space between a number and its unit in page text, so '9,81 m/s²' never breaks at the
    line end on a phone. Maths and inline SVG are stashed first, so LaTeX spacing and path data ("0,-80 s-18,…") are untouched."""
    maths = []
    def stash(m):
        maths.append(m.group(0)); return f"MATHTOKEN{len(maths) - 1}X"
    text = re.sub(r"<svg\b.*?</svg>|\$\$.*?\$\$|\$[^$\n]+?\$", stash, text, flags=re.S)
    text = re.sub(rf"(?<=\d) (?={UNIT}(?![\wäöå²³/]))", "\u00a0", text)
    text = re.sub(r"(?<=\S) = (?=[\d−\-+(])", "\u00a0=\u00a0", text)   # "s = 0,15 m" never breaks at the equals sign
    return re.sub(r"MATHTOKEN(\d+)X", lambda m: maths[int(m.group(1))], text)


STEP = "<!-- vaihe -->"


def staged_example(lesson_html):
    """Worked example in stages. In lesson.md the solution of `## Esimerkki` is split by lines `<!-- vaihe -->`:
    the part before the first marker is the problem, each later part one stage of the solution. The page shows
    the problem and stage 1, and a button reveals the next stage (lesson.js). Without JavaScript, and in print,
    every stage is visible. The problem sits in its own framed box (.example-task); on a wide screen it stays in view
    beside the steps (site.css .example)."""
    m = re.search(rf"(<h2[^>]*>{re.escape(T('sections.Esimerkki'))}</h2>)(.*?)(?=<h2|<section|\Z)", lesson_html, flags=re.S)
    if not m or STEP not in m.group(2): return lesson_html
    parts = [p.strip() for p in m.group(2).split(STEP)]
    n = len(parts) - 1
    steps = "".join(f'<div class="step" data-step="{i}"><p class="step-label">{T("lesson.example_step", i=i, n=n)}</p>{p}</div>'
                    for i, p in enumerate(parts[1:], 1))
    body = (f'<div class="example"><div class="example-task"><p class="example-label">{T("lesson.example_task")}</p>{parts[0]}</div>'
            f'<div class="worked" data-steps="{n}">{steps}'
            f'<p class="step-controls"><button type="button" class="next-step">{T("lesson.example_next")}</button> '
            f'<button type="button" class="all-steps">{T("lesson.example_all")}</button></p></div></div>')
    return lesson_html[:m.start(2)] + body + lesson_html[m.end(2):]


def named_sections(html):
    """`## Kaava: Lämpömäärä` is shown as "Lämpömäärä"; the key stays in data-section for the layout (inquiry.heading)."""
    def sub(m):
        key, shown = inquiry.heading(m.group(1))
        return f'<h2 data-section="{esc(key)}">{shown}</h2>' if shown != key else m.group(0)
    return re.sub(r"<h2>(.*?)</h2>", sub, html)


FIG = re.compile(r"(<p>(?:(?!</?p>|<svg).)*</p>|<table>.*?</table>|<ul>(?:(?!<ul>).)*?</ul>|<ol>(?:(?!<ol>).)*?</ol>)\s*<p>(<svg\b.*?</svg>)</p>", re.S)


def fig_rows(html):
    """A figure with the paragraph, table or list it explains (NOTES.md §3 puts it right after that block), as one
    unit: the text first, then its figure (teacher 2026-10-27, "kuvien sijoittelu"). On a wide screen the two stand
    side by side only when they are about as tall as each other (fig_side), so neither column is left with a long
    empty stretch; otherwise the figure stands under its text in the reading column. After the unit the text runs on
    in the reading column. On a phone and in print the figure is always under its text."""
    def row(m):
        side = fig_side(m.group(1), m.group(2))
        return f'<div class="fig-row {"side" if side else "stack"}"><div class="fig-text">{m.group(1)}</div><div class="fig">{m.group(2)}</div></div>'
    return FIG.sub(row, html)


SIDE_FIG = 26 * 16          # px: the figure column of a side-by-side unit (site.css .fig-row.side)
LINE, CHARS = 18 * 1.6, 72  # px per line and characters per line of the 38rem text column at 18 px (measured)


def text_height(html):
    """About how tall a block of text is in the reading column: its characters over the line length, maths counted
    by a third of its source, a table row 42 px, a list item a little extra for its spacing."""
    maths = sum(len(x) for x in re.findall(r"\$[^$]*\$", html))
    plain = re.sub(r"<[^>]+>", " ", re.sub(r"\$[^$]*\$", "", html))
    return (len(" ".join(plain.split())) + maths / 3) / CHARS * LINE + html.count("<tr") * 42 + html.count("<li") * LINE * 0.4


def fig_side(text_html, svg):
    """Side by side only when the text and the figure are of a similar height (0.6 to 1.5 times)."""
    vb = re.search(r'viewBox="[\d.\s-]*?([\d.]+)\s+([\d.]+)"', svg)
    if not vb: return False
    fig_h = SIDE_FIG * float(vb.group(2)) / float(vb.group(1))
    return 0.6 <= text_height(text_html) / fig_h <= 1.5


def fi(x):
    """Numbers with a decimal comma in page text (JSON keeps the point)."""
    return str(x).replace(".", T("format.decimal")).replace("-", "−") if isinstance(x, (int, float)) else str(x)   # true minus sign


def esc(s): return _h.escape(str(s), quote=True)


def texts(html):
    """{{t:site.footer}} in a template -> the text in the language being built (lang/<lang>.json)."""
    return re.sub(r"\{\{t:([\w.]+)\}\}", lambda m: esc(T(m.group(1))), html)


def page(title, body, crumbs, name, description, main_class="reading"):
    return rebase(texts(page_tpl).replace("{{title}}", esc(title)).replace("{{body}}", body).replace("{{crumbs}}", crumbs)
            .replace("{{main_class}}", main_class).replace("{{home}}", HOME).replace("{{languages}}", languages_nav(name))
            .replace("{{description}}", esc(description)).replace("{{url}}", URL + name))


def description_of(meta, lesson_md):
    """The motivating question makes the best one-line description; fall back to the first goal."""
    why = T("lesson.why_marker")
    m = re.search(rf"^> \*\*{re.escape(why)}\*\*\s*(.+)$", lesson_md, re.M)
    if m: return why + " " + re.sub(r"[*_`]", "", m.group(1)).strip()
    goals = [re.sub(rf"^(LOPS \w+:|{re.escape(T('lesson.goal_note'))}:)\s*", "", g) for g in meta.get("goals", [])]
    return (meta["title"] + ". " + (goals[0] if goals else "")).strip()


def solution_html(text):
    """A stepwise solution on the page (teacher 2026-10-27, "laskuratkaisujen luettavuus"): every step a block of its
    own with its label on a line of its own, a long chain of equalities in aligned rows, the answer set apart from the
    reasons for its precision (scripts/mathlayout.py). The source keeps the one-line-per-step form NOTES.md §3 asks for."""
    body = mathlayout.solution_md(text, T("lesson.solution_display_steps"))
    return mathlayout.steps_html(nbsp_units(render_md(body, extensions=["nl2br"])), T("lesson.solution_answer_step"))


def example_md(lesson_md):
    """The worked example's stages with their long chains in display rows, as in a solution (mathlayout)."""
    m = re.search(rf"^## {re.escape(T('sections.Esimerkki'))}\n(.*?)(?=^## |\Z)", lesson_md, flags=re.S | re.M)
    if not m or STEP not in m.group(1): return lesson_md
    def stage(part):
        h = re.match(r"\s*\*\*([^*\n]+?)[:.]\*\*", part)
        if not h or h.group(1).strip() not in T("lesson.solution_display_steps"): return part
        return part[:h.end()] + " " + mathlayout.display_chains(part[h.end():]) + "\n\n"
    return lesson_md[:m.start(1)] + STEP.join(stage(p) for p in m.group(1).split(STEP)) + lesson_md[m.end(1):]


def solutions_of(text):
    """{exercise id: html} from solutions.md, one `## id` block each: every bold step (**Annettu:**, **Periaate:**, ...)
    starts a paragraph of its own so the steps read one by one on a phone; other line breaks are kept (nl2br)."""
    out = {}
    for block in re.split(r"^## ", text or "", flags=re.M)[1:]:
        head, _, body = block.partition("\n")
        out[head.strip()] = solution_html(body)
    return out


def exercise_html(e, solution_html):
    ans = nbsp_units(f"{fi(e['answer'])} {e.get('unit', '')}".strip())
    numeric = isinstance(e["answer"], (int, float))
    check = ""
    if numeric:
        unit = esc(e.get("unit", ""))
        check = (f'<form class="check" data-answer="{e["answer"]}" data-tol="{e.get("tolerance", 0.02)}" novalidate>'
                 f'<input type="text" inputmode="decimal" autocomplete="off" enterkeyhint="done" aria-label="{esc(T("lesson.answer_for", id=e["id"]))}" placeholder="?">'
                 + (f'<span class="unit">{unit}</span>' if unit else "")
                 + f'<button type="submit">{T("lesson.check")}</button><output aria-live="polite"></output></form>')
    sol = f'<details class="solution"><summary>{T("lesson.solution")}</summary><div class="steps">{solution_html}</div></details>' if solution_html else ""
    return (f'<li id="{e["id"]}">{inquiry.task_text(nbsp_units(e["text"]))}{check}'
            f'<details class="answer"><summary>{T("lesson.answer")}</summary><p>{ans}</p></details>{sol}</li>')


def sim_head(inq):
    """The simulation card's heading. In an inquiry lesson it is a label over the panel, and a status line under it names
    the experiment that drives the simulation now (inquiry.js), so the picture and the task it serves stay linked."""
    if not inq: return f"<h2>{T('lesson.simulation')}</h2>"
    return f'<h3>{T("lesson.simulation")}</h3><p class="sim-context" aria-live="polite"></p>'


def notice(state): return f'<p class="notice" role="note">{T("lesson.notice_" + state)}</p>' if state != "reviewed" else ""


def strings_block(sim_key):
    """The texts the page's scripts read (lesson.js, inquiry.js, sim-embed.js and the simulation): lang "js", the
    number format and the simulation's own block of "sims", as one JSON element in the page."""
    data = {"js": T("js"), "format": {"decimal": T("format.decimal")}}
    if sim_key: data["sim"] = i18n.sim_strings(sim_key, T.lang) or i18n.sim_strings(sim_key)
    return '<script id="fl-strings" type="application/json">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"
assets = []  # published asset paths (relative to the output folder), checked before the swap
expected = []  # pages every language must have written
removed = []   # lessons on the live site that this build leaves out


def rebase(html):
    """A page of another language lives in site/<lang>/ and shares the assets of site/ (style, scripts, vendor/, the
    simulations and pictures): every relative src, href and data-base that is not a page gets the prefix ../ ."""
    if not UP: return html
    keep = lambda v: re.match(r"[a-z]+:|#|/|\.\./", v) or re.match(r"[\w.-]+\.html(#|$)", v)
    return re.sub(r'\b(src|href|data-base)="([^"]*)"', lambda m: m.group(0) if keep(m.group(2)) else f'{m.group(1)}="{UP}{m.group(2)}"', html)


def languages_nav(name):
    """{{languages}} in the templates: links to the same page in the site's other languages, empty while the site has
    one. A marker now; link_languages() fills it in once every language is built and it is known which pages exist."""
    return f"<!--fl-languages:{name}-->" if len(LANGS) > 1 else ""


def link_languages():
    """Every page's marker -> links to that page in the other languages (to their front page where it is missing)."""
    if len(LANGS) < 2: return
    for lang in LANGS:
        for f in OUTS[lang].glob("*.html"):
            def links(m):
                out = []
                for other in LANGS:
                    if other == lang: continue
                    target = m.group(1) if (OUTS[other] / m.group(1)).is_file() else "index.html"
                    href = os.path.relpath(OUTS[other] / target, OUTS[lang]).replace(os.sep, "/")
                    out.append(f'<a class="lang" href="{href}" hreflang="{other}" lang="{other}">{esc(i18n.T(other)("format.language_name"))}</a>')
                return "".join(out)
            f.write_text(re.sub(r"<!--fl-languages:([\w.-]+)-->", links, f.read_text()))


def course_text(code, mod):
    """A module's title, goals and lesson titles in the language being built: curriculum.json is the Finnish source,
    content/<lang>/courses.json holds the translations ({"FY3": {"title", "tavoitteet", "lessons": {id: title}}})."""
    if T.lang == i18n.SOURCE: return mod
    tr = COURSES.get(code, {})
    out = dict(mod, title=tr.get("title", mod["title"]), tavoitteet=tr.get("tavoitteet", mod.get("tavoitteet", [])))
    out["lessons"] = [dict(l, title=tr.get("lessons", {}).get(l["id"], l["title"])) for l in mod.get("lessons", [])]
    return out


def build_language(lang):
    """Every lesson, course page and the front page of one language into OUTS[lang]."""
    global UP, HOME, URL, COURSES
    i18n.set_lang(lang); out = OUTS[lang]; out.mkdir(exist_ok=True)
    UP = "" if lang == i18n.SOURCE else "../"; HOME = UP + "../../index.html"; URL = BASE_URL + ("" if lang == i18n.SOURCE else f"{lang}/")
    f = ROOT / "content" / lang / "courses.json"
    COURSES = json.loads(f.read_text()) if lang != i18n.SOURCE and f.is_file() else {}
    built = {}   # course -> [meta, ...]
    states = {}  # lesson id -> review state of every lesson seen, also the ones left out
    for folder in courses.lessons(lang=lang):
        meta = json.loads((folder / "meta.json").read_text())
        if only and meta["id"] != only: continue
        try: rs = review_status(folder)
        except ValueError as e: sys.exit(str(e))
        meta["state"] = rs["state"]; states[meta["id"]] = rs
        if rs["state"] == "draft" and not (only or build_all): continue   # publish only lessons whose reviews are current
        missing = [f for f in ("lesson.md", "exit-ticket.json") if not (folder / f).exists()]
        if (only or build_all): missing += [f"exercises/{f}" for f in courses.EXERCISE_FILES if not courses.lesson_file(folder, f).exists()]
        if missing:                                      # a draft still being written: skip it instead of failing the whole build
            print("skipped", meta["id"], "(missing " + ", ".join(missing) + ")"); continue
        try: ex_src = WorkTree() if (only or build_all) else published_exercises(folder)   # a preview shows the exercises as they are
        except ValueError as e: sys.exit(f"{meta['id']} exercises: {e}")
        ex_text = ex_src and ex_src.read(courses.lesson_rel(folder, "exercises.json")); sol_text = ex_src and ex_src.read(courses.lesson_rel(folder, "solutions.md"))
        if not (only or build_all) and not isinstance(ex_src, WorkTree):
            print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING:'} {meta['id']}: exercise reviews are not current; "
                  + (f"the page keeps the exercises last reviewed (commit {ex_src.sha[:7]})" if ex_src else "no version has passed yet, the page says the exercises are coming"))
        ex = json.loads(ex_text) if ex_text else {}
        publish = meta.get("solutions", "all")
        solutions = solutions_of(sol_text) if publish != "none" else {}
        ex_html = "" if ex else f'<p class="notice" role="note">{T("lesson.exercises_pending")}</p>'
        for lvl, items in ex.items():
            ex_html += f"<details class=\"level\"><summary>{T('lesson.level', n=lvl[-1])} <span class=\"count\">{T('lesson.level_count', n=len(items))}</span></summary><ol>"
            for i, e in enumerate(items):
                show = publish == "all" or (publish == "first" and i == 0)
                ex_html += exercise_html(e, solutions.get(e["id"]) if show else None)
            ex_html += "</ol></details>"
        exit_q = json.loads((folder / "exit-ticket.json").read_text())
        exit_items = "<ol>" + "".join(
            f"<li>{nbsp_units(q['q'])}<details class=\"answer\"><summary>{T('lesson.answer')}</summary><div class=\"answer-body\">{nbsp_units(render_md(mathlayout.display_chains(q['a'])))}</div></details></li>"
            for q in exit_q) + "</ol>"
        lesson_md = (folder / "lesson.md").read_text()
        lesson_html = staged_example(fig_rows(named_sections(nbsp_units(render_md(example_md(lesson_md))))))
        inq = inquiry.load(folder)
        if inq is not None:
            errs = inquiry.validate(folder, inq, lesson_md)
            if errs: sys.exit("\n".join(errs))
        howto = f'<p class="howto">{T("lesson.check_howto")}</p>'
        sim = ""
        where = courses.sim_dir(folder, meta)
        if where and where[0] == "lesson":                # FY3: sim.js in the lesson folder, published as <id>-sim.js
            shutil.copy(courses.lesson_file(folder, "sim.js"), SITE / f"{meta['id']}-sim.js"); assets.append(f"{meta['id']}-sim.js")
            sim = (f'<section id="sim">{sim_head(inq)}<div id="sim-root"></div>'
                   f'<script src="vendor/p5.min.js"></script><script src="sim-embed.js"></script><script src="{meta["id"]}-sim.js"></script><!--sim-info--></section>')
        elif where:                                       # a simulation folder of the course (or shared): published whole
            src, pub = where[1], where[2]
            if not (src / "sim.js").is_file(): sys.exit(f"{meta['id']}: simulation folder {src.relative_to(ROOT)} has no sim.js")
            shutil.copytree(src, SITE / pub, dirs_exist_ok=True); assets.append(f"{pub}/sim.js")
            css = f'<link rel="stylesheet" href="{pub}/sim.css">' if (src / "sim.css").is_file() else ""
            sim = (f'<section id="sim">{sim_head(inq)}{css}<div id="sim-root" data-base="{pub}/"></div>'
                   f'<script src="vendor/p5.min.js"></script><script src="sim-embed.js"></script><script src="{pub}/sim.js"></script><!--sim-info--></section>')
        for ref in courses.pic_refs_in([(courses.lesson_file(folder, n).read_text() if courses.lesson_file(folder, n).exists() else "") for n in courses.LESSON_TEXTS] + [ex_text, sol_text]):   # pictures the text refers to, at the same relative path
            if not courses.pic_source(ref).is_file(): sys.exit(f"{meta['id']}: picture {ref} not found (expected assets/{ref})")
            (SITE / ref).parent.mkdir(parents=True, exist_ok=True); shutil.copy(courses.pic_source(ref), SITE / ref); assets.append(ref)
        name = f"{meta['id']}.html"
        if inq is None:                                   # classic layout: theory (with the sim inside), exit ticket, exercises
            sim = sim.replace("<!--sim-info-->", "")
            if sim and "<!-- sim -->" in lesson_html: lesson_html = lesson_html.replace("<!-- sim -->", sim, 1)
            elif sim and re.search(rf"<h2[^>]*>{re.escape(T('sections.Esimerkki'))}", lesson_html):
                lesson_html = re.sub(rf"(<h2[^>]*>{re.escape(T('sections.Esimerkki'))})", lambda m: sim + m.group(1), lesson_html, count=1)
            elif sim: lesson_html += sim
            toc = (f'<a href="#teoria">{T("lesson.theory")}</a>' + (f'<a href="#sim">{T("lesson.simulation")}</a>' if sim else "")
                   + f'<a href="#exit">{inquiry.exit_title()}</a><a href="#exercises">{inquiry.exercises_title()}</a>')
            main = (f'<article id="teoria">{lesson_html}</article>\n'
                    f'<section id="exit"><h2>{inquiry.exit_title()}</h2>{exit_items}</section>\n'
                    f'<section id="exercises"><h2>{inquiry.exercises_title()}</h2>{howto if ex else ""}{ex_html}</section>')
        else:                                             # inquiry layout: the same parts placed by inquiry.json (scripts/inquiry.py)
            lesson_html = lesson_html.replace("<!-- sim -->", "")
            pieces = re.split(r"(?=<h2[ >])", lesson_html)
            intro = pieces[0] if not pieces[0].startswith("<h2") else ""
            sections = {}
            for piece in pieces[1:] if intro or len(pieces) > 1 else []:
                m = re.match(r'<h2(?: data-section="([^"]*)")?>(.*?)</h2>', piece)
                if m: sections[_h.unescape(m.group(1) or m.group(2))] = re.sub(r"^<h2[^>]*>(.*?)</h2>", r'<h3 class="theory-h">\1</h3>',
                                                                     re.sub(r"<(/?)h3>", r"<\1h4>", piece), count=1)   # a ### subheading under its section heading
            parts = {"intro": intro, "sections": sections, "sim": sim, "exercises": f'{howto if ex else ""}{ex_html}',
                     "exit": f'<div id="exit"><h3>{inquiry.exit_title()}</h3>{exit_items}</div>',
                     "selfcheck": practice.selfcheck_html(inq.get("learn"), lambda t: nbsp_units(render_md(t)), bool(ex))}   # Arvioi osaamistasi (teacher 2026-10-28)
            body, toc = inquiry.render(folder, inq, parts, lambda t: nbsp_units(render_md(t)))
            main = f'<article id="teoria" class="inquiry">{body}</article>'
        skey = (meta["id"] if where[0] == "lesson" else where[1].name) if where else None   # the sim's block of lang "sims"
        html = (texts(tpl).replace("{{title}}", esc(meta["title"])).replace("{{course}}", meta["course"]).replace("{{notice}}", notice(meta["state"]))
                .replace("{{strings}}", strings_block(skey)).replace("{{back_to_course}}", esc(T("site.back_to_course", course=meta["course"])))
                .replace("{{toc}}", toc).replace("{{main}}", main)
                .replace("{{scripts}}", '<script src="inquiry.js"></script><script src="selfassess.js"></script>' if inq else "")
                .replace("{{description}}", esc(description_of(meta, lesson_md))).replace("{{url}}", URL + name)
                .replace("{{home}}", HOME).replace("{{languages}}", languages_nav(name)))
        (out / name).write_text(rebase(html))
        built.setdefault(meta["course"], []).append(meta)
        print("built", meta["id"], f"({meta['state']})")

    # Sovella itsenäisesti: one page per course with module-end tasks (scripts/practice.py, teacher 2026-10-28), published
    # like a lesson only when both its reviews pass; a preview builds it with `build.py <COURSE>-sovella` or --all.
    practice_built = {}
    for code in practice.courses_with(lang):
        pname = practice.page_name(code)
        if only and only != pname[:-5]: continue
        ps = practice.status(code, lang)
        if ps["state"] != "reviewed" and not (only or build_all):
            if (LIVE / out.relative_to(SITE) / pname).is_file():
                print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING:'} {pname} is on the live site but its reviews are not current; this build removes it")
            continue
        body, ptoc = practice.render(code, lang, lambda t: nbsp_units(render_md(t)), solution_html, T("practice.title"))
        ptitle = T("practice.title")
        html = (texts(tpl).replace("{{title}}", esc(ptitle)).replace("{{course}}", code).replace("{{notice}}", notice("reviewed" if ps["state"] == "reviewed" else "draft"))
                .replace("{{strings}}", strings_block(None)).replace("{{back_to_course}}", esc(T("site.back_to_course", course=code)))
                .replace("{{toc}}", ptoc).replace("{{main}}", f'<article id="teoria" class="inquiry practice">{body}</article>')
                .replace("{{scripts}}", '<script src="selfassess.js"></script>')
                .replace("{{description}}", esc(T("practice.description", code=code, title=course_text(code, curriculum[code])["title"]))).replace("{{url}}", URL + pname)
                .replace("{{home}}", HOME).replace("{{languages}}", languages_nav(pname)))
        (out / pname).write_text(rebase(html))
        tasks = practice.load(code, lang)["tasks"]
        practice_built[code] = T("practice.course_count", n=len(tasks), points=sum(practice.total(t) for t in tasks if t.get("kind") != "own"))
        print("built", pname, f"({ps['state']})")

    # Course pages and front page. Every module in curriculum.json gets a page; lessons built in this run are
    # links, the rest are listed as "tulossa" so students see the whole course and nav links always resolve.
    modules = [(k, course_text(k, v)) for k, v in curriculum.items() if not k.startswith("_")]
    built_ids = {m["id"] for ms in built.values() for m in ms}
    legacy_ids = {m["id"] for ms in built.values() for m in ms if m["state"] == "legacy"}

    cards = ""
    for code, mod in modules:
        slots = mod.get("lessons", [])
        done = sum(1 for l in slots if l["id"] in built_ids)
        pct = round(100 * done / len(slots)) if slots else 0
        kind = T("site.course_type_required") if mod.get("type") == "pakollinen" else T("site.course_type_optional")
        state = T("site.lessons_ready", done=done, n=len(slots)) if done else T("site.lessons_planned", n=len(slots))
        cards += (f'<a class="card{" live" if done else ""}" href="{code}.html"><span class="code">{code}</span>'
                  f'<span class="ctitle">{esc(mod["title"])}</span><span class="meta">{T("site.credits", n=mod.get("op", ""))} · {kind}</span>'
                  f'<span class="bar" aria-hidden="true"><span style="width:{pct}%"></span></span><span class="state">{state}</span></a>')

        items = ""
        for l in slots:
            if l["id"] in legacy_ids:
                items += f'<li class="live legacy"><a href="{l["id"]}.html">{esc(l["title"])}</a> <span class="count">{T("site.lesson_prototype")}</span></li>'
            elif l["id"] in built_ids:
                items += f'<li class="live"><a href="{l["id"]}.html">{esc(l["title"])}</a></li>'
            else:
                items += f'<li class="soon"><span>{esc(l["title"])}</span> <span class="count">{T("site.lesson_coming")}</span></li>'
        goals = "".join(f"<li>{esc(g)}</li>" for g in mod.get("tavoitteet", []))
        body = (f'<span class="eyebrow">{code} · {T("site.credits", n=mod.get("op", ""))} · {kind}</span><h1>{esc(mod["title"])}</h1>'
                f'<p class="lead">{T("site.lessons_ready", done=done, n=len(slots))}</p>'
                + (f'<h2>{T("site.course_goals")}</h2><p>{T("site.course_goals_lead")}</p><ul>{goals}</ul>' if goals else "")
                + f'<h2>{T("site.course_lessons")}</h2><ol class="lessons">{items}</ol>'
                + (f'<h2>{T("practice.title")}</h2><p>{T("practice.course_lead")}</p><ul class="lessons practice-link"><li class="live">'
                   f'<a href="{practice.page_name(code)}">{T("practice.title")}</a> <span class="count">{practice_built[code]}</span></li></ul>' if code in practice_built else ""))
        desc = T("site.course_description", code=code, title=mod["title"], done=done, n=len(slots))
        (out / f"{code}.html").write_text(page(T("site.course_title", code=code, title=mod["title"]), body,
                                                f'<a href="index.html">{T("site.name")}</a> › {code}', f"{code}.html", desc))

    latest = ""
    for code, mod in modules:                       # most recently planned published lesson of the highest module
        for l in mod.get("lessons", []):
            if l["id"] in built_ids: latest = f'<p class="latest">{T("site.latest_lesson")} <a href="{l["id"]}.html">{esc(l["title"])}</a> ({code})</p>'
    total = sum(len(m.get("lessons", [])) for _, m in modules)
    home = (
        f'<section class="hero"><span class="eyebrow">{T("site.home_eyebrow")}</span>'
        f'<h1>{T("site.name")}</h1>'
        f'<p class="lead">{T("site.home_lead")}</p>'
        + latest + '</section>'
        + '<ul class="how">' + "".join(f'<li><strong>{T(f"site.home_{k}")}</strong>{T(f"site.home_{k}_text")}</li>' for k in ("theory", "sim", "tasks")) + '</ul>'
        f'<h2 id="moduulit">{T("site.modules")}</h2>' f'<div class="cards">{cards}</div>'
        f'<p class="count">{T("site.home_count", built=len(built_ids), total=total)}</p>')
    (out / "index.html").write_text(page(T("site.name"), home, "", "index.html", T("site.home_description"), main_class=""))
    if SITE.name == "site.tmp":                  # a lesson leaves the live site only with a warning (an annotation on CI)
        live = LIVE / out.relative_to(SITE)
        for old_page in sorted(live.glob("*.html")):
            lid = old_page.stem
            if lid in states and lid not in built_ids:
                why = ", ".join(f"{n}={v}" for n, v in states[lid]["reports"].items() if v != "missing") or "no reports"
                removed.append(lid if lang == i18n.SOURCE else f"{lang}/{lid}")
                print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING:'} {old_page.relative_to(LIVE)} is on the live site but its reviews are not current ({why}); this build removes it")
    pre = out.relative_to(SITE).as_posix() + "/" if out != SITE else ""
    expected.extend(pre + n for n in ["index.html"] + [f"{c}.html" for c, _ in modules] + [f"{i}.html" for i in built_ids] + [practice.page_name(c) for c in practice_built])
    print(f"built {pre or ''}index +", len(modules), "module pages ->", ((LIVE if SITE.name == "site.tmp" else SITE) / pre).relative_to(ROOT),
          f"({sum(m['state'] == 'reviewed' for ms in built.values() for m in ms)} reviewed, {len(legacy_ids)} legacy, "
          f"{sum(m['state'] == 'draft' for ms in built.values() for m in ms)} draft" + (f", {len(removed)} removed: {', '.join(removed)}" if removed else "") + ")")


LANGS = i18n.languages()                          # fi at site/, every other language at site/<lang>/
OUTS = {lang: SITE if lang == i18n.SOURCE else SITE / lang for lang in LANGS}
for lang in LANGS: build_language(lang)
link_languages()
i18n.set_lang(i18n.SOURCE)
if SITE.name == "site.tmp":                      # check the render, then swap it in; the old site comes back if the swap fails
    expected += ["site.css", "lesson.js", "sim-embed.js", "inquiry.js", "selfassess.js"] + assets
    broken = [n for n in expected if not (SITE / n).is_file() or (SITE / n).stat().st_size == 0]
    if broken or not (SITE / "vendor").is_dir(): sys.exit(f"build check failed, site/ left unchanged: missing or empty {broken or ['vendor/']}")
    old = ROOT / "site.old"
    if old.exists(): shutil.rmtree(old)
    if LIVE.exists(): LIVE.rename(old)
    try: SITE.rename(LIVE)
    except BaseException:
        if old.exists(): old.rename(LIVE)
        raise
    shutil.rmtree(old, ignore_errors=True)
