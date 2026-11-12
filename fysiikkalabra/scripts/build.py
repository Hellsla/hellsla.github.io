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
import hashlib, json, os, sys, re, shutil, pathlib, atexit, html as _h, markdown
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from reviews import status as review_status, published_exercises, WorkTree
import ahjo, answers_shown, figsize, jaksot, kaavat, kilparobo, lumatutor, assigned, booklets, cardgrid, concept_cards, courses, fbdspec, figcat, guides, i18n, inquiry, investigations, local_courses, mathlayout, mixer, module_icons, practice, reading_tips, svgids, units, tablefit
from i18n import t as T

ROOT = pathlib.Path(os.environ.get("FYSIIKKALABRA_ROOT") or pathlib.Path(__file__).resolve().parents[1])   # tests build a copy
BASE_URL = "https://ruukkilab.fi/"
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
for f in ("site.css", "lesson.js", "sim-embed.js", "inquiry.js", "selfassess.js", "investigation.js", "invfilter.js", "padstore.js", "palautus.js", "readaloud.js", "kortit.js", "tehty.js", "omaarvio.js", "jatka.js", "ahjo.js", "lumatutor.js"): shutil.copy(TPL / f, SITE / f)
card_files = concept_cards.publish(SITE)   # site/kortit/<module>.json, read by Käsitetakomo (scripts/concept_cards.py)
# p5 + KaTeX, no CDN needed. The read-aloud model and onnxruntime-web are not part of the site (teacher 2026-11-04,
# UI fix 3): they are in the repository Hellsla/ruukkilabra-models, copied into the published site's models/ folder
# when it is published, and loaded by readaloud.js from there (MODEL_BASE).
MODEL_DIRS = ("supertonic3-v1", "ort")
shutil.copytree(TPL / "vendor", SITE / "vendor", dirs_exist_ok=True, ignore=shutil.ignore_patterns(*MODEL_DIRS))
for _d in MODEL_DIRS: shutil.rmtree(SITE / "vendor" / _d, ignore_errors=True)
if booklets.DIR.is_dir():                                      # Vihkot: the printable course books (scripts/booklets.py)
    (SITE / booklets.PUBLISHED).mkdir(parents=True, exist_ok=True)
    for f in booklets.DIR.glob("*.pdf"): shutil.copy2(f, SITE / booklets.PUBLISHED / f.name)
if (ROOT / "assets/shared/ahjo/aloitus").is_dir():             # Ahjo's starter files (scripts/ahjo.py STARTERS): models, sketches, templates
    shutil.copytree(ROOT / "assets/shared/ahjo/aloitus", SITE / "ahjo-aloitus", dirs_exist_ok=True)
if (ROOT / "assets/shared/laskuri").is_dir():                 # the school's standalone countdown page, ruukkilab.fi/laskuri (teacher 2026-11-10)
    shutil.copytree(ROOT / "assets/shared/laskuri", SITE / "laskuri", dirs_exist_ok=True)
if (ROOT / "assets/shared/brand").is_dir():                   # the Ruukkilabra logos and favicon (scripts/brand_logos.py); test copies may leave them out
    shutil.copytree(ROOT / "assets/shared/brand", SITE / "brand", dirs_exist_ok=True)
if (ROOT / "assets/units").is_dir():                          # the local courses' unit components (scripts/units.py)
    shutil.copytree(ROOT / "assets/units", SITE / "units", dirs_exist_ok=True)
if module_icons.DIR.is_dir():                                 # one icon per module (scripts/module_icons.py), front page and module pages
    shutil.copytree(module_icons.DIR, SITE / module_icons.PUBLISHED, dirs_exist_ok=True)
tpl = (TPL / "lesson.html").read_text()
page_tpl = (TPL / "page.html").read_text()
curriculum = json.loads((ROOT / "curriculum.json").read_text())
if local_courses.validate(curriculum): sys.exit("\n".join(local_courses.validate(curriculum)))
_ahjo_errs = ahjo.validate({l["id"] for k, m in curriculum.items() if not k.startswith("_") for l in m.get("lessons", [])}, set(investigations.ids()),
                           set(guides.ids()), [p["icon"] for p in local_courses.planned()], list(local_courses.load()),
                           {k: m["title"] for k, m in curriculum.items() if not k.startswith("_")})
if _ahjo_errs: sys.exit("ERROR: ahjo.json (scripts/ahjo.py):\n" + "\n".join(_ahjo_errs))
_jk_errs = jaksot.validate(module_icons.ICONS)   # every unit of jaksot/ has the same header (scripts/jaksot.py, teacher 2026-11-12)
if _jk_errs: sys.exit("ERROR: jaksot/ (scripts/jaksot.py):\n" + "\n".join(_jk_errs))
_kr_errs = kilparobo.validate({l["id"] for k, m in curriculum.items() if not k.startswith("_") for l in m.get("lessons", [])})
if _kr_errs: sys.exit("ERROR: kilparobo.json (scripts/kilparobo.py):\n" + "\n".join(_kr_errs))
_lt_errs = lumatutor.validate({l["id"] for k, m in curriculum.items() if not k.startswith("_") for l in m.get("lessons", [])})
if _lt_errs: sys.exit("ERROR: lumatutor.json (scripts/lumatutor.py):\n" + "\n".join(_lt_errs))


# Submission trial (teacher 2026-11-05): "Lataa kaikki ratkaisut" on the chapters of these courses in these languages
# only (templates/palautus.js; first FY3-1, then every FY3 chapter); the teacher's side is palautus/ (a local grading
# page or a Sheets-bound Apps Script), never part of the site.
SUBMISSION_LANGS = {"fi", "fi-easy", "en"}           # teacher 2026-11-06: also English
SUBMISSION_CHAPTER = re.compile(r"^fy[1-8]-\d+$|^fy9-[a-z]+(-[a-z]+)*$")   # teacher 2026-11-06: every course FY1-FY8 (was FY3 only) and the FY9 review lessons (units)


def submits(lang, lesson_id):
    m = SUBMISSION_CHAPTER.match(lesson_id or "")
    return bool(m) and lang in SUBMISSION_LANGS


# Palautukset (teacher 2026-11-06): palautukset.json names the period and each group's Google Forms responder link. The
# chapters with the download button then get a "Palauta" link to palautukset.html, a page with one button per group.
# Only links: the site loads nothing from Google and receives no submission.
FORMS_FILE = ROOT / "palautukset.json"
FORMS_PAGE = "palautukset.html"
FORM_URL = re.compile(r"^https://(forms\.gle/[A-Za-z0-9]{6,40}|docs\.google\.com/forms/d/e/[A-Za-z0-9_-]{20,120}/viewform(\?usp=[a-z_]{1,20})?)$")


RETURN_CODES = courses.codes() + ["FY9"]   # the Palautukset page's courses: FY1-FY8 and the review course FY9 (teacher 2026-11-06)


def submission_forms():
    if not FORMS_FILE.is_file(): return None
    d = json.loads(FORMS_FILE.read_text())
    bad = lambda why: sys.exit(f"palautukset.json: {why}")
    if d.get("period") not in (1, 2, 3, 4, 5): bad("period must be 1-5")
    if not isinstance(d.get("year"), str) or not re.fullmatch(r"20\d\d-\d\d", d["year"]): bad("year must be like 2026-27")
    forms = d.get("forms")
    if not isinstance(forms, list): bad("forms must be a list")
    seen = set()
    for f in forms:
        if not isinstance(f, dict) or not isinstance(f.get("group"), str) or not re.fullmatch(r"[0-9A-Za-zÅÄÖåäö .-]{1,40}", f["group"]): bad(f"bad group in {f!r}")
        if not isinstance(f.get("url"), str) or not FORM_URL.match(f["url"]): bad(f"{f.get('group')}: the url must be a Google Forms responder link (https://forms.gle/...)")
        if f["group"].split(".")[0] not in RETURN_CODES: bad(f"{f['group']}: the group must start with a course code and a dot, e.g. FY3.2")
        if f["group"] in seen: bad(f"{f['group']} twice")
        seen.add(f["group"])
    return d if forms else None


FORMS = submission_forms()


# Guided self-assessment (teacher 2026-11-06, from his 2018 team sheet): in Itsearvio (#tarkista) the chapter's goals
# first and then every task get a level a-d or x (scripts/inquiry.py sa_fieldset, templates/inquiry.js part 8), kept on
# the student's device; the submission file carries only the goals' latest levels (templates/palautus.js, version 3,
# teacher 2026-11-06 evening). FY3 first, then FY1-FY8.
SELF_ASSESS_COURSES = {"FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8", "FY9"}   # teacher 2026-11-06: every chapter with the download button, then the review course FY9


def self_assesses(lang, meta):
    return meta.get("course") in SELF_ASSESS_COURSES and submits(lang, meta.get("id"))


def submission_script(lang, lesson_id):
    if not submits(lang, lesson_id): return ""
    ret = f' data-return="{FORMS_PAGE}"' if FORMS else ""
    return f'<script src="palautus.js" data-chapter="{lesson_id}"{ret}></script>'


# Annetut tehtävät (teacher 2026-11-07, FY3 first): the teacher's assigned exercises of a module, by their ids in
# annetut.json (scripts/assigned.py). The pages mark them and templates/tehty.js keeps the student's "Tehty" ticks.
ASSIGNED = assigned.load()
ASSIGNED_IDS = assigned.flat(ASSIGNED)


GOAL_PER_OP = 45   # the progress graph's goal line (teacher 2026-11-07): 90 tasks in a 2 op module, 45 in a 1 op one
COURSE_FILE = {f"FY{i}" for i in range(1, 9)}   # one work file per module (teacher 2026-11-07): FY1-FY8; FY9 keeps the chapter file


def self_goals(course, lid, lang):
    """The chapter's verbal self-assessment statements (Itsearvio's tavoite-1, -2, …) as plain text, for the module page's
    Oma itsearvio (templates/omaarvio.js): the same ones inquiry.sa_goals_html shows."""
    extra = inquiry.self_statements(lid, lang)
    if extra: return [inquiry.plain(x) for x in extra]
    inq = inquiry.load(courses.ROOT / "content" / ("fi" if lang == "fi-easy" else lang) / course / lid) or {}
    if inq.get("self_extra"): return [inquiry.plain(x) for x in inq["self_extra"]]
    return [inquiry.plain(T("inquiry.sa_goal_prefix") + " " + x) for x in inq.get("learn") or []]


def course_block(course, lang):
    """The module's chapters and their exercise ids (#fl-course) for palautus.js's one work file per module (Tallenna
    työ tiedostoon, Avaa tallennettu työ, Palauta), with the assigned tasks for tehty.js (and the script when there are
    any). Empty outside FY1-FY8 or a language without submissions."""
    if course not in COURSE_FILE or lang not in SUBMISSION_LANGS: return ""
    chs = []
    for n, l in enumerate(curriculum[course].get("lessons", []), 1):
        ex = assigned.exercises(course, l["id"])   # the ids are the same in every language
        if ex: chs.append({"id": l["id"], "n": n, "tasks": [e["id"] for items in ex.values() for e in items]})
        goals = self_goals(course, l["id"], lang)
        if goals and chs and chs[-1]["id"] == l["id"]: chs[-1]["goals"] = goals
    given = [i for ids in ASSIGNED.get(course, {}).values() for i in ids]
    data = {"course": course, "chapters": chs, "assigned": given, "goal": GOAL_PER_OP * curriculum[course].get("op", 2)}
    return ('<script id="fl-course" type="application/json">' + json.dumps(data, separators=(",", ":")) + "</script>"
            + ('<script src="tehty.js"></script>' if given else ""))


def progress_view(themes, given, block):
    """Näytä edistyminen (teacher 2026-11-07): Oma eteneminen (counter, bar, graph; tehty.js) and Oma itsearvio (the
    verbal statements and the fingerprint under the themes; omaarvio.js) behind one button, shown by the scripts. With
    assigned tasks (FY3) the counter is over them and their Tehty marks; otherwise over every task of the module, a
    task with a saved solution counting as done (FY1-FY9, no marks on the tasks)."""
    strings = {k: v for k, v in T("js").items() if k.startswith(("done_", "progress_", "palautus_", "work_", "selfmap_"))}
    strings.update({k: v for k, v in T("inquiry").items() if k in ("sa_a", "sa_b", "sa_c", "sa_d", "sa_x", "sa_x_short", "sa_a_short", "sa_b_short", "sa_c_short", "sa_d_short")})
    prog = (f'<section class="my-progress" id="oma-eteneminen" hidden><h2>{T("js.progress_title")}</h2>'
            '<p class="pm-count visually-hidden" aria-live="polite"></p><div class="pm-bar" role="progressbar" aria-valuemin="0"><span></span></div>'
            f'<div class="pm-graph" role="group" aria-label="{T("js.progress_graph")}"><div class="pm-chart"></div></div>'
            f'<p class="pm-note">{T("js.progress_note" if given else "js.progress_note_all")}</p></section>')
    mine = (f'<section class="my-selfmap" id="oma-itsearvio" data-themes="{esc(json.dumps(themes, ensure_ascii=False))}" hidden><h2>{T("js.selfmap_title")}</h2>'
            '<p class="sm-count visually-hidden" aria-live="polite"></p><div class="sm-map"></div></section>')
    # the button on one row with Tallenna työ tiedostoon and Avaa tallennettu työ (teacher 2026-11-08); it opens the
    # details below (its own summary hidden), so the work buttons stay beside it
    return (f'<div class="my-top"><button type="button" class="my-toggle" aria-expanded="false" aria-controls="omat-tiedot" hidden>{T("js.progress_show")}</button></div>'
            f'<details class="my-wrap" id="omat-tiedot" hidden><summary>{T("js.progress_show")}</summary><div class="my-row">' + prog + mine + '</div></details>'
            '<script id="fl-strings" type="application/json">' + json.dumps({"js": strings}, ensure_ascii=False).replace("</", "<\\/") + "</script>"
            + block + ("" if given else '<script src="tehty.js"></script>') + '<script src="omaarvio.js"></script>')


def progress_section(course, lang, mod=None):
    """The module page's own part (teacher 2026-11-07), after the heading, before the chapters: progress_view and the
    buttons Tallenna työ tiedostoon and Avaa tallennettu työ (palautus.js)."""
    block = course_block(course, lang)
    if not block: return ""
    ret = f' data-return="{FORMS_PAGE}"' if FORMS else ""
    themes = [{"t": th["title"], "first": th["first"]} for th in (mod or {}).get("themes", [])]
    view = progress_view(themes, bool(ASSIGNED.get(course)), block)
    return view.replace('</button></div>', '</button><div class="work-tools" id="oma-tyo" hidden></div></div>', 1) + f'<script src="palautus.js" data-course="{course}"{ret}></script>'


def local_progress(code, c, lang):
    """Näytä edistyminen on a local course's page (FY9, teacher 2026-11-07): its units' review tasks (sovella/tasks.json)
    and statements, the course's chapters as the themes. No work file: FY9 keeps its chapter files (palautus.js)."""
    if not c.get("chapters") or code != "FY9": return ""
    chs, themes, n = [], [], 0
    for ch in c["chapters"]:
        for k, u in enumerate(ch.get("units", [])):
            n += 1
            f = next((courses.ROOT / "content" / l / "units" / u["id"] / "sovella" / "tasks.json" for l in dict.fromkeys([lang, "fi"])
                      if (courses.ROOT / "content" / l / "units" / u["id"] / "sovella" / "tasks.json").is_file()), None)
            tasks = [t["id"] for t in json.loads(f.read_text()).get("tasks", [])] if f else []
            goals = inquiry.self_statements(u["id"], lang)
            if not tasks and not goals: continue
            if k == 0 or not themes or themes[-1]["t"] != ch["title"]: themes.append({"t": ch["title"], "first": u["id"]})
            chs.append({"id": u["id"], "n": n, "tasks": tasks, **({"goals": [inquiry.plain(x) for x in goals]} if goals else {})})
    if not chs: return ""
    block = '<script id="fl-course" type="application/json">' + json.dumps({"course": code, "chapters": chs, "assigned": [], "goal": GOAL_PER_OP * c.get("op", 2)}, separators=(",", ":")) + "</script>"
    return progress_view(themes, False, block)


def forms_title(): return T("site.returns_title", period=FORMS["period"], year=FORMS["year"])


def grading_file():
    """The running period's local grading page (palautus/arviointi-<year>-p<n>.html, scripts/palautus_tasks.py), the
    newest by name; None when there is none."""
    fs = sorted((ROOT / "palautus").glob("arviointi-*.html"))
    return fs[-1] if fs else None


def teacher_page_body(name):
    """Työkalut (teacher 2026-11-08; in English too, teacher 2026-11-08 "tee työkalusivu myös enkuksi"): the classroom
    screen and the newest grading tool to download and the steps in short, texts in lang/<lang>.json "teacher". No
    student data: the tool reads the Drive zip on the teacher's own computer and keeps the points in that browser."""
    pal = f'<a href="{FORMS_PAGE}">{esc(forms_title())}</a>' if FORMS else esc(T("teacher.returns_page"))
    screen = (TOOLS / "luokkanaytto.html").is_file()
    return (f'<h1>{esc(T("teacher.title"))}</h1>'
            f'<p class="lead">{esc(T("teacher.lead"))}</p>'
            + (f'<section class="teacher-tool"><h2>{esc(T("teacher.screen_h"))}</h2>'
               f'<p><a class="pad-btn" href="tyokalut/luokkanaytto.html">{esc(T("teacher.screen_open"))}</a></p></section>' if screen else '')
            + f'<section class="teacher-tool"><h2>{esc(T("teacher.grading_h"))}</h2>'
            f'<p>{esc(T("teacher.grading_p"))}</p>'
            f'<p><a class="pad-btn teacher-download" href="tyokalut/{esc(name)}" download="{esc(name)}">{esc(T("teacher.download", name=name))}</a></p>'
            f'<p>{esc(T("teacher.update_p"))}</p></section>'
            f'<section class="teacher-steps"><h2>{esc(T("teacher.steps_h"))}</h2><ol>'
            + "".join(f'<li>{T(f"teacher.step_{i}", returns=pal)}</li>' for i in range(1, 6)) + '</ol></section>'   # the steps keep their <i> and <b>
            + teacher_examples())


SHOTS = [("opiskelija", 1600, 702), ("opettaja-kooste", 1190, 1140), ("opettaja-sormenjalki", 1594, 656), ("opettaja-arviointi", 1600, 594)]   # captions: lang "teacher.shot_<name>"


def teacher_examples():
    """Example screenshots (teacher 2026-11-08): a student after six weeks and the grading view with 30 made-up students."""
    figs = []
    for name, w, h in SHOTS:
        if not (TOOLS / "kuvat" / f"{name}.webp").is_file(): continue
        cap = T(f"teacher.shot_{name}")
        figs.append(f'<figure class="teacher-shot"><img src="tyokalut/kuvat/{name}.webp" width="{w}" height="{h}" loading="lazy" '
                    f'alt="{esc(cap)}"><figcaption>{esc(cap)}</figcaption></figure>')
    return f'<section class="teacher-examples"><h2>{esc(T("teacher.examples_h"))}</h2>{"".join(figs)}</section>' if figs else ''


def return_title(code):
    """A course's name in this language on the Palautukset page: a curriculum course, or the local review course FY9."""
    if code in courses.codes(): return COURSES.get(code, {}).get("title") or courses.course(code)["title"]
    return ((local_courses.load(T.lang).get(code) or {}).get("title")) or (local_courses.load().get(code) or {}).get("title") or code   # a copy without the local courses (test_i18n)


def forms_page_body():
    """One section per course in curriculum order: the groups' form buttons, or a grey placeholder when the course has
    no forms this period (teacher 2026-11-06: one page for every course, updated when the period changes)."""
    natural = lambda g: [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", g)]
    out = []
    for code in RETURN_CODES:
        fs = sorted((f for f in FORMS["forms"] if f["group"].split(".")[0] == code), key=lambda f: natural(f["group"]))
        links = ("".join(f'<a class="return-form" href="{esc(f["url"])}">{esc(f["group"])}</a>' for f in fs)
                 or f'<span class="return-none">{esc(T("site.returns_none"))}</span>')
        out.append(f'<section class="return-course{'' if fs else ' is-empty'}"><h2>{esc(code)} {esc(return_title(code))}</h2>'
                   f'<nav class="return-forms" aria-label="{esc(T("site.returns_aria", code=code))}">{links}</nav></section>')
    return (f'<h1>{esc(forms_title())}</h1>'
            f'<p class="lead">{esc(T("site.returns_lead"))}</p>'
            + "".join(out))


def render_md(text, **kw):
    """Markdown -> HTML, with LaTeX kept out of markdown's reach, force-diagram specs drawn (scripts/fbdspec.py) and
    figures embedded by id (`<svg data-fig="fy5-2/lauta-voimat"></svg>`, figcat.embed) drawn in the page's language.
    ```latex fences become $$...$$; every $$...$$ and $...$ is swapped for a token first,
    so underscores, backslashes and asterisks inside maths are not read as markdown."""
    text = re.sub(r"```latex\n(.*?)```", lambda m: "\n$$" + m.group(1).strip() + "$$\n", text, flags=re.S)
    text = kaavat.as_html(text)                                                    # ```kaavat: named formulas as a formula table
    text, fbds = fbdspec.render(text)                                              # ```voimakuvio specs -> drawn diagrams
    text, figrefs = figcat.embed(text)                                             # a model figure by id inside a solution step
    maths = []
    def stash(m):
        x = m.group(0)
        if x.startswith("$$"): x = "$$" + mathlayout.align_equals(x[2:-2]) + "$$"   # equals signs of a calculation in one column
        else: x = mathlayout.split_list(x[1:-1]) or x                                # a list of values may wrap between its items
        maths.append(x); return f"MATHTOKEN{len(maths) - 1}X"
    text = re.sub(r"\$\$.*?\$\$|\$[^$\n]+?\$", stash, text, flags=re.S)
    html = markdown.markdown(text, extensions=["fenced_code", "tables"] + kw.get("extensions", []))
    html = fbdspec.restore(re.sub(r"MATHTOKEN(\d+)X", lambda m: maths[int(m.group(1))], html), fbds)
    return figcat.restore(html, figrefs, T.lang) if figrefs else html


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
    every stage is visible. The problem sits in its own framed box (.example-task), the steps under it in the reading
    column at every width (site.css .example, teacher 2026-11-03)."""
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


FIG = re.compile(r"(<p>(?:(?!</?p>|<svg).)*</p>|<table>(?:(?!</?table>).)*</table>|<ul>(?:(?!<ul>).)*?</ul>|<ol>(?:(?!<ol>).)*?</ol>)\s*<p>(<svg\b.*?</svg>)</p>", re.S)


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


PHOTO = re.compile(r'<figure class="unit-photo( wide)?"><img src="((?:pics/[a-z0-9]+|shared/pics)/[^"]+)"([^>]*)>(?:<figcaption>(.*?)</figcaption>)?</figure>', re.S)


def photo_credits(ref):
    """The credit of a photograph pics/<course>/<file> from that folder's photos.json (teacher 2026-11-03: FY1–FY3
    photos as in FY14): {file: {title, creator, source, licence, licence_url?, width, height, edit, checked}}; edit (crop, resize) and
    checked (the date the licence was checked) are the record, not shown."""
    f = courses.pic_source(ref).parent / "photos.json"
    data = json.loads(f.read_text()) if f.is_file() else {}
    c = data.get(ref.rsplit("/", 1)[1])
    if not c: sys.exit(f"{ref}: a photograph needs its credit in {f.relative_to(ROOT)} (title, creator, source, licence, width, height)")
    return c


def photos(html):
    """(html, credits section) of a lesson's photographs: each `<figure class="unit-photo"><img src alt><figcaption>`
    (class "unit-photo wide": a data map or chart that needs the column's width, 2026-11-03 FY2 temperature map)
    written in the text gets its size, lazy loading and a short credit under the caption from photos.json, and the
    page ends with the full credits (the FY14 units' form, scripts/units.py tail_html)."""
    used = []
    def one(m):
        wide, ref, attrs, cap = m.group(1) or "", m.group(2), m.group(3), m.group(4) or ""
        c = photo_credits(ref); used.append(c)
        credit = (f'{T("lesson.computed_by")}: {esc(c["creator"])}' if c.get("computed")      # a picture computed from a model (2026-11-07 FY5 ripple tank): no photo, no licence
                  else f'{T("lesson.photo_by")}: {esc(c["creator"])}, {esc(c["licence"])}')
        return (f'<figure class="unit-photo{wide}"><img src="{ref}"{attrs} width="{c["width"]}" height="{c["height"]}" loading="lazy" decoding="async">'
                f'<figcaption>{cap} <span class="photo-credit">{credit}</span></figcaption></figure>')
    html = PHOTO.sub(one, html)
    if not used: return html, ""
    items = "".join(f'<li><strong>{esc(c["title"])}</strong>. {esc(c["creator"])}. '
                    + (T("lesson.computed_note") if c.get("computed") else
                       f'<a href="{esc(c["source"])}">{T("units.credit_source")}</a>, '
                       + (f'<a href="{esc(c["licence_url"])}">{esc(c["licence"])}</a>' if c.get("licence_url") else esc(c["licence"])))
                    + "</li>" for c in used)
    return html, f'<section class="unit-credits" id="credits"><h2>{T("lesson.photos")}</h2><ul>{items}</ul></section>'


def fi(x):
    """Numbers with a decimal comma in page text (JSON keeps the point)."""
    return str(x).replace(".", T("format.decimal")).replace("-", "−") if isinstance(x, (int, float)) else str(x)   # true minus sign


def esc(s): return _h.escape(str(s), quote=True)


def plain_tex(s):
    """A title with LaTeX ("Teho: $P = \\Delta E/\\Delta t$") as plain text for the browser tab and link previews,
    which cannot render maths: "Teho: P = ΔE/Δt"."""
    def one(m):
        f = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", m.group(1))
        for tex, uni in (("\\Delta", "Δ"), ("\\rho", "ρ"), ("\\mu", "µ"), ("\\cdot", "·")): f = f.replace(tex + " ", uni).replace(tex, uni)
        f = re.sub(r"\\[,;:!]", "", f)   # a thin space between factors is no comma in the tab: "v = g\\,t" -> "v = gt"
        return f.replace("\\", "")
    return re.sub(r"\$([^$]+)\$", one, s)


def texts(html):
    """{{t:site.footer}} in a template -> the text in the language being built (lang/<lang>.json)."""
    html = re.sub(r"\{\{t:([\w.]+)\}\}", lambda m: esc(T(m.group(1))), html)
    if grading_file():   # Työkalut in every language's footers (teacher 2026-11-08)
        html = html.replace('<a href="tietosuoja.html">', f'<a href="{TEACHER_PAGE}">{esc(T("site.tools"))}</a><a href="tietosuoja.html">', 1)
        # Opettajalle in every page's header and phone menu (UI audit 2026-11-10, finding 15; teacher 2026-11-11): the classroom
        # screen and the grading page were only behind the footer's small Työkalut link. The footer link stays.
        link = f'<a href="{TEACHER_PAGE}">{esc(T("site.teacher_nav"))}</a>'
        html = re.sub(r'(<a class="nav-booklets" [^>]*>[^<]*</a>)', lambda m: m.group(1) + link.replace("<a ", '<a class="nav-teacher" ', 1), html, count=1)
        html = re.sub(r'(<li><a href="vihkot\.html">[^<]*</a></li>)', lambda m: m.group(1) + f"<li>{link}</li>", html, count=1)
    return html


# Modules the front page still lists dimmed under Tulossa although some of their chapters are published (teacher
# 2026-11-03, "tiivistä etusivu": FY6–FY8 stay there until the teacher moves them; curriculum.json "_front_page").
HOME_COMING = tuple(curriculum.get("_front_page", {}).get("coming", []))


def home_row(code, title, question, coming=False):
    """A front page row: one link over the whole row with the module's icon, code, title and Miksi question; the arrow
    appears on hover and focus only. The question is cut to one line in two columns, so it is whole in title too."""
    q = esc(question)
    return (f'<li><a class="mod-row{" coming" if coming else ""}" href="{code}.html">{module_icons.img(code, 40)}'
            f'<span class="mod-text"><span class="mod-name">{('<span class="mod-code">' + code + '</span> ') if local_courses.label(code) else ""}<span class="mod-title">{esc(title)}</span></span>'
            f'<span class="mod-q" title="{q}">{q}</span></span><span class="mod-go" aria-hidden="true">→</span></a></li>')


def planned_row(p):
    """A planned course of the school (teacher 2026-11-04): icon, name and one sentence, greyed out and not a link, as
    the course has no content yet."""
    q = esc(p["text"])
    return (f'<li><div class="mod-row coming planned">{module_icons.img(p["icon"], 40)}'
            # "tulossa" in words (UI audit 2026-11-10, finding 14): grey alone read as a broken link
            f'<span class="mod-text"><span class="mod-name"><span class="mod-title">{esc(p["title"])}</span> <span class="mod-soon">{esc(T("site.upcoming").lower())}</span></span>'
            f'<span class="mod-q" title="{q}">{q}</span></span></div></li>')


def ahjo_row(d, planned):
    """The front page's Ahjo rows: Ahjo 1 and Ahjo 2, each to its own course page, which opens with Ahjo's shared pages
    (teacher 2026-11-08: "tässä pitäisi olla Ahjo 1 ja Ahjo 2"; the shared pages first on the course pages)."""
    return "".join(ahjo_course_row(c, planned) for c in d["courses"])


def ahjo_course_row(c, planned):
    """Ahjo 1 and Ahjo 2 under Ahjo's row (teacher 2026-11-08 "tässä pitäisi olla Ahjo 1 ja Ahjo 2"): each links its own
    course page; the name from the course registry, the subtitle from ahjo.json, the icon from module-icons/."""
    p = next((p for p in planned if p.get("icon") == c["code"]), {"title": c["code"], "text": ""})
    q = esc(p["text"])
    return (f'<li><a class="mod-row ahjo-row ahjo-course-row" href="{ahjo.course_page(c["code"])}"><img class="mod-icon" src="module-icons/{c["code"].lower()}.svg" alt="" width="40" height="40" aria-hidden="true">'
            f'<span class="mod-text"><span class="mod-name"><span class="mod-code">{esc(p["title"])}</span> <span class="mod-title">{esc(c["subtitle"])}</span></span>'
            f'<span class="mod-q" title="{q}">{q}</span></span><span class="mod-go" aria-hidden="true">→</span></a></li>')


def resume_box():
    """Jatka (design audit 2026-11-10, P0-3): an empty row that templates/jatka.js fills from this browser's own record
    of started chapters; it stays hidden for a reader who has not started one, and without the script."""
    t = {"resume": T("site.resume"), "go": T("site.resume_go"), "stages": T("site.state_stages"), "started": T("site.state_started"), "stage": T("site.resume_stage")}
    return f'<div class="resume" id="jatka" data-t="{esc(json.dumps(t, ensure_ascii=False))}" hidden></div>'


ABOUT = "tietoa.html"
TEACHER_PAGE = "tyokalut.html"   # Työkalut (teacher 2026-11-08): the newest local grading page and the classroom screen, in every language
TOOLS = ROOT / "tyokalut"        # the classroom screen and its libraries (luokkanaytto.html, lib/), copied to site/tyokalut/
PRIVACY = "tietosuoja.html"   # Tietosuoja (teacher 2026-11-04): no student data, no cookies, what the browser keeps and why


def front_chrome(html):
    """The front page's own header and footer (teacher 2026-11-03): no Moduulit link in its header, as the front page is
    the module list (teacher 2026-11-04), and Sivustosta after Vihkot (2026-11-04); its footer is only Ruukkilabra and
    Tietosuoja like every page's (2026-11-04). Näin opiskelet is in every page's header (templates, teacher 2026-11-08)."""
    html = re.sub(r'<a class="nav-modules" [^>]*>[^<]*</a>', "", html, count=1)
    html = html.replace(f'{esc(T("site.booklets"))}</a>', f'{esc(T("site.booklets"))}</a><a class="nav-about" href="{ABOUT}">{esc(T("site.about"))}</a>', 1)   # Sivustosta in the header too (teacher 2026-11-04)
    return html


STUDY_ID = "nain-opiskelet"
STUDY_PAGE = STUDY_ID + ".html"   # a page of its own (teacher 2026-11-04: Lukuvinkit only the books, Näin opiskelet only the study tips)

# Line icons of the study guide (teacher 2026-11-08): 24 x 24, drawn with the text colour, never the only carrier of a meaning.
STUDY_ICONS = {
    "draw": "M4 20l1-4.2L15.6 5.2a2.1 2.1 0 0 1 3 3L8.2 19zM13.6 7.2l3 3",
    "theory": "M12 6.5C9.5 4.8 6.5 4.6 3.5 5.5v13c3-.9 6-.7 8.5 1 2.5-1.7 5.5-1.9 8.5-1v-13c-3-.9-6-.7-8.5 1zM12 6.5v13",
    "hint": "M9.5 18h5M10.5 21h3M12 3a6 6 0 0 0-3.6 10.8c.7.6 1.1 1.3 1.1 2.1h5c0-.8.4-1.5 1.1-2.1A6 6 0 0 0 12 3z",
    "talk": "M4 4.5h10a1 1 0 0 1 1 1V11a1 1 0 0 1-1 1H8.5L5 15v-3H4a1 1 0 0 1-1-1V5.5a1 1 0 0 1 1-1zM18 8.5h2a1 1 0 0 1 1 1V15a1 1 0 0 1-1 1h-1v3l-3.5-3H11a1 1 0 0 1-1-1v-1",
    "retry": "M19.5 12.5a7.5 7.5 0 1 1-2.2-5.8M19.5 3.5v4.8h-4.8",
    "graph": "M4 3.5v16.5h16.5M7 16.5c2.5 0 3.5-8.5 6.5-8.5s3 5 6 5",
    "explain": "M5 4.5h14a1 1 0 0 1 1 1v9.5a1 1 0 0 1-1 1h-7.5L7 19.5V16H5a1 1 0 0 1-1-1V5.5a1 1 0 0 1 1-1zM8 8.5h8M8 12h5",
    "calc": "M6.5 3h11a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1h-11a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zM8.5 6.5h7v3h-7zM9 13.5h.01M12 13.5h.01M15 13.5h.01M9 17h.01M12 17h.01M15 17h.01",
    "together": "M9 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15.5 5.2a3 3 0 0 1 0 5.6M17 14.3c2.3.6 4 2.8 4 5.7",
    "review": "M5 5h14a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM4 9.5h16M8 3v4M16 3v4M8 13.5h.01M12 13.5h.01M16 13.5h.01M8 17h.01M12 17h.01",
}
STUDY_WAYS = ["draw", "theory", "hint", "talk"]                  # lang guide.ways in this order
STUDY_TIPS = ["graph", "explain", "calc", "together", "review"]   # lang guide.tips in this order
# Each getting-started step shows the stages of a chapter it means, numbered as in a lesson's stage bar (Pohdinta 1 ...
# Itsearvio 7, the exercises sixth): the guide speaks the lessons' own words (inquiry.stage_*, lesson.exercises).
STUDY_STEP_STAGES = [[1, 2, 3], [4], [5], [6]]


def study_icon(name, cls="study-icon"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">'
            f'<path d="{STUDY_ICONS[name]}"/></svg>')


def study_guide():
    """Näin opit fysiikkaa, nain-opiskelet.html (teacher 2026-11-08, "Näin opiskelet -sivun uudistaminen"; its own page
    since 2026-11-04): three parts. Näin pääset alkuun: four numbered steps, each with the chapter stages it means as
    the lesson's stage chips. Jäikö tehtävä jumiin?: a problem-solving map, the question, four ways out side by side
    (HTML cards, so the text reflows) joined by quiet SVG lines to Yritä uudelleen itse; below 50rem the same map is a
    vertical rail, the lines' SVGs hidden. The ways are a <ul>: no order, help may be asked at once. Viisi vinkkiä:
    five short tips with line icons. Then the closing line and a link to the front page's module list."""
    g = lambda k: T("guide." + k)
    names = [T("inquiry.stage_" + k) for k in inquiry.STAGE_IDS[:5]] + [T("lesson.exercises")]
    def chips(nums):
        return (f'<p class="study-where"><span class="visually-hidden">{esc(g("where"))}: </span>'
                + "".join(f'<span class="study-chip"><span class="study-chip-no" aria-hidden="true">{n}</span>{esc(names[n - 1])}</span>' for n in nums) + '</p>')
    steps = "".join(f'<li><h3>{esc(s["title"])}</h3><p>{esc(s["text"])}</p>{chips(nums)}</li>'
                    for s, nums in zip(g("steps"), STUDY_STEP_STAGES))
    ways = "".join(f'<li>{study_icon(k)}<h3>{esc(w["title"])}</h3><p>{esc(w["text"])}</p></li>' for k, w in zip(STUDY_WAYS, g("ways")))
    tips = "".join(f'<li>{study_icon(k)}<div><h3>{esc(t["title"])}</h3><p>{esc(t["text"])}</p></div></li>' for k, t in zip(STUDY_TIPS, g("tips")))
    # the map's lines in a 400 x 40 box stretched over the row of four cards (preserveAspectRatio none, so the strokes
    # keep their width): from the question's centre to each card's centre, and from each card back to the retry card
    xs = [50, 150, 250, 350]
    fan = "".join(f'<path d="M200 0C200 22 {x} 18 {x} 40"/>' for x in xs)
    join = "".join(f'<path d="M{x} 0C{x} 22 200 18 200 40"/>' for x in xs)
    lines = lambda d, cls: f'<svg class="stuck-lines {cls}" viewBox="0 0 400 40" preserveAspectRatio="none" aria-hidden="true" focusable="false">{d}</svg>'
    return (f'<section class="study-intro" id="{STUDY_ID}" aria-labelledby="h-study"><h1 id="h-study">{esc(g("title"))}</h1><p class="lead">{esc(g("lead"))}</p></section>'
            f'<section class="study-sec" id="alkuun" aria-labelledby="h-start"><h2 id="h-start">{esc(g("start_h"))}</h2>'
            f'<ol class="study-steps">{steps}</ol></section>'
            f'<section class="study-sec stuck" id="jumissa" aria-labelledby="h-stuck"><h2 id="h-stuck">{esc(g("stuck_h"))}</h2>'
            f'<p class="section-lead">{esc(g("stuck_lead"))} {esc(g("stuck_note"))}</p>'
            f'<div class="stuck-map"><p class="stuck-q">{esc(g("stuck_question"))}</p>{lines(fan, "fan")}'
            f'<ul class="stuck-ways">{ways}</ul>{lines(join, "join")}'
            f'<div class="stuck-retry">{study_icon("retry")}<h3>{esc(g("retry_title"))}</h3><p>{esc(g("retry_text"))}</p></div></div></section>'
            f'<section class="study-sec" id="vinkit" aria-labelledby="h-tips"><h2 id="h-tips">{esc(g("tips_h"))}</h2>'
            f'<ul class="study-tips">{tips}</ul></section>'
            f'<section class="study-end"><p>{esc(g("closing"))}</p><a class="study-cta" href="index.html#moduulit">{esc(g("cta"))}<span aria-hidden="true">→</span></a></section>')


def page(title, body, crumbs, name, description, main_class="reading", full_title=None):
    """A front or module page. Its <title> is "<title> — Ruukkilabra"; the front page passes full_title instead, so
    the site's name is not said twice."""
    head = full_title or f"{title} — {T('site.name')}"
    tpl_ = page_tpl
    if re.search(r"\$[^$\s][^$]*\$", body):   # a chapter title with a formula (curriculum.json "$pV = nRT$"): the lesson pages' KaTeX
        tpl_ = (tpl_.replace('<link rel="stylesheet" href="site.css">', '<link rel="stylesheet" href="vendor/katex/katex.min.css">\n<link rel="stylesheet" href="site.css">', 1)
                .replace("</body>", '<script src="vendor/katex/katex.min.js"></script><script src="vendor/katex/contrib/auto-render.min.js" '
                         'onload="renderMathInElement(document.querySelector(\'main\'),{delimiters:['
                         + ("{left:\'$$\',right:\'$$\',display:true}," if "$$" in body else "")      # an Ahjo guide's displayed calculation
                         + '{left:\'$\',right:\'$\',display:false}],throwOnError:false})"></script>\n</body>', 1))
    return rebase(texts(tpl_).replace("{{head_title}}", esc(head)).replace("{{title}}", esc(title)).replace("{{body}}", body).replace("{{crumbs}}", crumbs)
            .replace("{{main_class}}", main_class).replace("{{languages}}", languages_nav(name))
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
        body = mathlayout.display_chains(part[h.end():])
        return part[:h.end()] + ("\n\n" if body.startswith("<div") else " ") + body + "\n\n"   # a block is not set inside the label's paragraph
    return lesson_md[:m.start(1)] + STEP.join(stage(p) for p in m.group(1).split(STEP)) + lesson_md[m.end(1):]


def solutions_of(text):
    """{exercise id: html} from solutions.md, one `## id` block each: every bold step (**Annettu:**, **Periaate:**, ...)
    starts a paragraph of its own so the steps read one by one on a phone; other line breaks are kept (nl2br)."""
    out = {}
    for block in re.split(r"^## ", text or "", flags=re.M)[1:]:
        head, _, body = block.partition("\n")
        out[head.strip()] = solution_html(body)
    return out


def core_ids(ex):
    """The core exercises (teacher 2026-10-29, "harjoituspolku"): those marked `"core": true`, or, in a level where none
    is marked, the first two of levels 1 and 2. Level 3 is challenging practice, the rest additional practice."""
    out = set()
    for lvl, items in ex.items():
        marked = [e["id"] for e in items if e.get("core")]
        out |= set(marked) if any("core" in e for e in items) else ({e["id"] for e in items[:2]} if lvl[-1] in "12" else set())
    return out


NUM_CELL = re.compile(r"[−-]?\d+(?:\.\d+)?")


def exercise_text(text, pid):
    """An exercise's task text. A text in paragraphs (a blank line before each part a), b), c)) keeps them: the
    situation first (split like any long task, inquiry.task_text), then each paragraph as its own (a part "a) …" as a bold question),
    the last one carrying pid (the answer field's description). A text without blank lines renders as before."""
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    if len(paras) < 2: return inquiry.task_text(text, pid=pid)
    head = inquiry.task_text(paras[0])
    idattr = f' id="{esc(pid)}"'
    part = lambda p: "task ask" if re.match(r"[a-h]\)", p) else "task more"   # "a) …" is a question; "Vakiot: …" plain text (never a 2nd bare p.task: test_writepad)
    parts = [f'<p class="{part(p)}"{idattr if i == len(paras) - 2 else ""}>{p}</p>' for i, p in enumerate(paras[1:])]
    return head + "".join(parts)


def data_table(d):
    """An exercise's data ("data": {"caption", "columns", "rows"}, teacher 2026-11-04, aineistotehtävät): a measurement
    table the student reads, copies into a spreadsheet or fits. A cell that is a plain number is written with a point
    in the JSON (the same in every language) and shown with the page language's decimal sign; any other cell, the
    caption and the column heads are text with LaTeX."""
    cell = lambda c: str(c).replace(".", T("format.decimal")).replace("-", "−") if NUM_CELL.fullmatch(str(c)) else nbsp_units(str(c))
    cap = f'<caption>{nbsp_units(d["caption"])}</caption>' if d.get("caption") else ""
    head = "".join(f'<th scope="col">{nbsp_units(h)}</th>' for h in d["columns"])
    body = "".join("<tr>" + "".join(f"<td>{cell(c)}</td>" for c in r) + "</tr>" for r in d["rows"])
    return f'<table class="exp-table ex-data">{cap}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def exercise_choice(e):
    """A conceptual multiple-choice exercise ("choices", teacher 2026-11-04): the same component as an inquiry choice
    (inquiry.choice_html, inquiry.js: feedback for the chosen option, one change, then the correct one), in an
    exercise's place. Its answer and model solution open after "Olen tehnyt ratkaisun", like a written task's."""
    md = lambda t: nbsp_units(render_md(t))
    lid = e["id"].rsplit("-L", 1)[0]
    if e.get("statements"):                                    # true-or-false statements (teacher 2026-11-05)
        return inquiry.truefalse_html({"prompt": e.get("prompt") or T("lesson.choose_tf"), "statements": e["statements"]}, md, e["id"])
    if e.get("order"):                                         # putting items in order by a quantity (teacher 2026-11-05)
        return inquiry.order_html({"prompt": e.get("prompt") or T("lesson.choose_order"), "order": e["order"]}, md, lid, e["id"])
    layout = "figures" if any(c.get("figure") for c in e["choices"]) else "list"   # options drawn as graphs or force diagrams
    html = inquiry.choice_html({"prompt": e.get("prompt") or T("lesson.choose"), "choices": e["choices"], "layout": layout}, md, lid, e["id"])
    if e.get("reasons"):                                       # two-stage: the answer, then the reason for it (teacher 2026-11-05)
        html += inquiry.choice_html({"prompt": e.get("reason_prompt") or T("lesson.choose_reason"), "choices": e["reasons"]}, md, lid, e["id"] + "-why")
    return html



def chapter_no(course, lid):
    """The chapter's number in its module: its place in curriculum.json's slots, the "Luku N" of the module page."""
    ids = [l["id"] for l in curriculum.get(course, {}).get("lessons", [])]
    return ids.index(lid) + 1 if lid in ids else None


def number_label(num):
    """An exercise's running number "6-3" (chapter-exercise, teacher 2026-11-04): shown first in the exercise, read
    out with its word ("Tehtävä 6-3") (site.css keeps it on one line)."""
    return f'<span class="ex-num"><span class="visually-hidden">{T("lesson.exercise_word")} </span>{num}</span>'


def chapter_eyebrow(html, code, n):
    """'FY3 · Luku 6' over the page's title, so a student knows the number the exercises carry (6-1, 6-2, ...)."""
    if n is None: return html
    return html.replace("<h1>", f'<span class="eyebrow ch-no">{esc(code)} · {T("site.chapter_n", n=n)}</span><h1>', 1)


def exercise_html(e, solution_html, read=None, core=False, num=None):
    numeric = isinstance(e["answer"], (int, float))
    ans = nbsp_units(f"{fi(answers_shown.fallback(e['answer']) if numeric else e['answer'])} {e.get('unit', '')}".strip())
    if numeric and solution_html:                                                  # the solution's own rounded answer
        label = T("lesson.solution_answer_step")
        step = re.search(rf'<p class="sol-label">{re.escape(label)}</p>(.*?)</div>', solution_html, re.S)
        tex = answers_shown.shown(f"**{label}:** " + step.group(1).replace("\n", " "), label, e["answer"], e.get("tolerance", 0.02)) if step else None
        if tex: ans = f"${tex}$"
    check = ""
    if numeric:
        unit = esc(e.get("unit", ""))
        st = answers_shown.step(ans.strip("$"), e["answer"]) if ans.startswith("$") else None   # one unit in the shown answer's last digit; the check allows half of it
        check = (f'<form class="check" data-answer="{e["answer"]}" data-tol="{e.get("tolerance", 0.02)}"' + (f' data-step="{st:g}"' if st else "") + ' novalidate>'
                 f'<input type="text" inputmode="decimal" autocomplete="off" enterkeyhint="done" aria-label="{esc(inquiry.answer_label(e.get("unit", "")))}" aria-describedby="{esc(e["id"])}-q" placeholder="?">'
                 + (f'<span class="unit">{unit}</span>' if unit else "")
                 + f'<button type="submit">{T("lesson.check")}</button><output aria-live="polite"></output></form>')
    model = figcat.figure_html(e["model_figure"], T.lang, read) if e.get("model_figure") else ""   # a drawing task's model diagram, inside the solution
    sol = f'<details class="solution"><summary>{T("lesson.solution")}</summary>{model}<div class="steps">{solution_html}</div></details>' if solution_html else ""
    fig = figcat.figure_html(e["figure"], T.lang, read) if e.get("figure") else ""   # a figure by its id (scripts/figcat.py)
    fig = (data_table(e["data"]) if e.get("data") else "") + fig + (exercise_choice(e) if e.get("choices") or e.get("statements") or e.get("order") else "")
    tag = f'<span class="ex-core">{T("lesson.core_exercise")}</span>' if core else ""
    given = e["id"] in ASSIGNED_IDS   # an assigned task (annetut.json, teacher 2026-11-07): "Annettu" beside its number, a green left edge
    if given: tag = f'<span class="ex-core ex-given">{T("lesson.assigned_exercise")}</span>' + tag
    text = e["text"]
    ext = T("lesson.extension_exercise") + "."   # "Syventävä tehtävä." at the start of a task's text: a tag, never a core task (teacher 2026-11-07, LOPS 2019)
    if text.startswith(ext): text, tag = text[len(ext):].lstrip(), tag + f'<span class="ex-core ex-ext">{T("lesson.extension_exercise")}</span>'
    written = "" if numeric else ' data-written="1"'   # a written task opens its answer once the student has written in the editor (lesson.js part 8; the tick "Olen tehnyt ratkaisun" removed, teacher 2026-11-06)
    cls = " ".join(c for c, on in (("core", core), ("assigned", given)) if on)
    return (f'<li id="{e["id"]}"{" class=" + chr(34) + cls + chr(34) if cls else ""}{written}' + (f' data-num="{num}">' + number_label(num) if num else ">") + f'{tag}{exercise_text(nbsp_units(text), f"{e['id']}-q")}{fig}{check}'
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
    data = {"js": T("js"), "format": {"decimal": T("format.decimal")}, "speech": T("speech")}   # speech: readaloud.js
    if sim_key: data["sim"] = i18n.sim_strings(sim_key, T.lang) or i18n.sim_strings(sim_key)
    return '<script id="fl-strings" type="application/json">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"
assets = []  # published asset paths (relative to the output folder), checked before the swap
expected = []  # pages every language must have written
removed = []   # lessons on the live site that this build leaves out


def rebase(html):
    """A page of another language lives in site/<lang>/ and shares the assets of site/ (style, scripts, vendor/, the
    simulations and pictures): every relative src, href and data-base that is not a page gets the prefix ../ .
    Every page passes here, so here a figure shown twice gets its own definition ids (svgids.py, teacher 2026-10-29)
    and a figure is never drawn larger than it was designed (figsize.py, teacher 2026-11-12)."""
    html = figsize.natural(svgids.namespace(html))
    if svgids.duplicates(html): sys.exit(f"ERROR: repeated ids on a page: {', '.join(svgids.duplicates(html))} (scripts/svgids.py)")
    if not UP: return html
    keep = lambda v: re.match(r"[a-z]+:|#|/|\.\./", v) or re.match(r"[\w.-]+\.html([#?]|$)", v)
    return re.sub(r'\b(src|href|data-base)="([^"]*)"', lambda m: m.group(0) if keep(m.group(2)) else f'{m.group(1)}="{UP}{m.group(2)}"', html)


def languages_nav(name):
    """{{languages}} in the templates: links to the same page in the site's other languages, empty while the site has
    one. A marker now; link_languages() fills it in once every language is built and it is known which pages exist."""
    return f"<!--fl-languages:{name}-->" if len(LANGS) > 1 else ""


def link_languages():
    """Every page's marker -> the language control: the current language shown, the others in a list (a <details>
    disclosure, so it works with a keyboard and without scripts). A page the other language has not published (a
    lesson not translated or reviewed yet) is never swapped for that language's front page: the link goes to the
    module page there, whose note at #unavailable-<id> says the page is not available in that language, and the
    menu says so before the click (teacher 2026-10-29). Drafts stay out: only built pages count."""
    if len(LANGS) < 2: return
    for lang in LANGS:
        here = i18n.T(lang)
        for f in OUTS[lang].glob("*.html"):
            def control(m):
                items = []
                for other in LANGS:
                    if other == lang: continue
                    there = i18n.T(other); name = m.group(1); note = ""
                    if (OUTS[other] / name).is_file(): target = name
                    else:
                        module = name.split("-")[0].upper() + ".html"; key = "site.lang_unavailable"
                        if (OUTS[other] / module).is_file(): target = f"{module}#unavailable-{name[:-5]}"
                        else:                    # a local course (or its investigation) this language lacks: the course's front page note
                            home = (OUTS[other] / "index.html").read_text()
                            guide = (("FY10",) if name.startswith("tvt-") else ())   # a TVT-ohje: its course's note (the guides are FY10's, as below)
                            ids = [i for i in (name[:-5], module[:-5]) + guide if f'id="unavailable-{i}"' in home]
                            target = "index.html" + (f"#unavailable-{ids[0]}" if ids else "")
                            key = "site.lang_unavailable_home"
                        note = f'<span class="lang-note" id="lang-note-{other}">{esc(here(key))}</span>'
                    href = os.path.relpath(OUTS[other] / target.split("#")[0], OUTS[lang]).replace(os.sep, "/") + ("#" + target.split("#")[1] if "#" in target else "")
                    described = f' aria-describedby="lang-note-{other}"' if note else ""
                    items.append(f'<li><a class="lang" href="{href}" hreflang="{there("format.html_lang")}" lang="{there("format.html_lang")}"{described}>'
                                 f'{esc(there("format.language_name"))}</a>{note}</li>')
                return (f'<details class="lang-menu"><summary><span class="visually-hidden">{esc(here("site.language"))}: </span>'
                        f'<span class="lang-current">{esc(here("format.language_name"))}</span></summary>'
                        f'<ul class="lang-list" aria-label="{esc(here("site.language_choose"))}">{"".join(items)}</ul></details>')
            html = re.sub(r"<!--fl-languages:([\w.-]+)-->", control, f.read_text())
            if lang != i18n.SOURCE:   # a link in the text to a page only the source language has (FY10's investigations from FY9): that page
                src = OUTS[i18n.SOURCE]
                html = re.sub(r'\bhref="([\w.-]+\.html)([#?][^"]*)?"', lambda m: m.group(0) if (OUTS[lang] / m.group(1)).is_file() or not (src / m.group(1)).is_file()
                              else f'href="{os.path.relpath(src / m.group(1), OUTS[lang]).replace(os.sep, "/")}{m.group(2) or ""}"', html)
            f.write_text(html)


def chapter_card(html):
    """What a chapter's card on its module page shows (teacher 2026-11-03, "Ruukkikortit"): the chapter's own opening
    illustration and its Miksi question, taken from the built page, so nothing is written twice (scripts/cardgrid.py)."""
    q = re.search(r'<div class="intro-head">.*?<blockquote>\s*<p>(.*?)</p>', html, re.S)
    why = re.sub(r"</?strong>", "", q.group(1)).strip() if q else ""
    return cardgrid.hero(html), why


def chapter_cards(code, mod, slots, built_ids, legacy_ids, cards):
    """The module page's chapters as cards, under the module's themes (curriculum.json "themes": [{title, first}],
    titles translated in content/<lang>/courses.json "themes"); a chapter still coming is a plain row without a link.
    Each theme has a row of its own over its tiles, with its chapters' range, and starts a new row of tiles (teacher
    2026-11-10, variant B of the comparison; until then one continuous grid with the name over the theme's first card,
    which hid where a theme ended). FY9, FY14 and the FY10 bank keep the label over the first card (cardgrid.label)."""
    themes = {th["first"]: th["title"] for th in mod.get("themes", [])}
    if themes and slots[0]["id"] not in themes: sys.exit(f"{code}: the first theme must start at the first chapter {slots[0]['id']}")
    bad = set(themes) - {l["id"] for l in slots}
    if bad: sys.exit(f"{code}: themes start at unknown chapters {sorted(bad)} (curriculum.json)")
    items = ""
    starts = [i for i, l in enumerate(slots, 1) if l["id"] in themes] + [len(slots) + 1]
    for i, l in enumerate(slots, 1):
        lab = ""
        if l["id"] in themes:     # the theme on its own row with its chapters' range (teacher 2026-11-10, variant B)
            last = starts[starts.index(i) + 1] - 1
            items += cardgrid.theme_row(esc(themes[l["id"]]), T("site.theme_chapter", n=i) if last == i else T("site.theme_chapters", a=i, b=last))
        num = T("site.chapter_n", n=i); title = esc(l["title"])
        if l["id"] in built_ids:
            svg, why = cards.get(l["id"], ("", ""))
            tags = f'<span class="tag">{T("site.lesson_prototype")}</span>' if l["id"] in legacy_ids else ""
            items += cardgrid.card(num, title, f'{l["id"]}.html', why, svg, tags, lab=lab)
        else:
            items += cardgrid.card(num, title, None, tags=f'<span class="tag">{T("site.lesson_coming")}</span>', lab=lab)
    return cardgrid.grid(items)


def chapter_titles(code, built=None):
    """{chapter id: title in the page's language} of a module (the card components name chapters by title, never by id)."""
    return {l["id"]: l["title"] for l in course_text(code, curriculum[code]).get("lessons", []) if built is None or l["id"] in built}


def course_text(code, mod):
    """A module's title, goals and lesson titles in the language being built: curriculum.json is the Finnish source,
    content/<lang>/courses.json holds the translations ({"FY3": {"title", "tavoitteet", "lessons": {id: title}}})."""
    if T.lang == i18n.SOURCE: return mod
    tr = COURSES.get(code, {})
    out = dict(mod, title=tr.get("title", mod["title"]), tavoitteet=tr.get("tavoitteet", mod.get("tavoitteet", [])))
    out["lessons"] = [dict(l, title=tr.get("lessons", {}).get(l["id"], l["title"])) for l in mod.get("lessons", [])]
    if mod.get("themes"): out["themes"] = [dict(th, title=t) for th, t in zip(mod["themes"], tr.get("themes", [th["title"] for th in mod["themes"]]))]
    return out


# Moduulin loppuosiot (teacher 2026-11-10, "omat kortit, samat kaikilla kursseilla"; the same size as the chapter tiles
# and without their lead texts, teacher 2026-11-10 evening): Kertauspakkasi, Esimerkkikoe, Haastetehtävät and Moduulin
# tavoitteet as tiles in a grid of their own under the chapters, each with one shared illustration
# (assets/shared/module-end/, the chapter tiles' 2:1 flat style, no text), the same on every module page and in every
# language; the small line over the title is a count, not a description. The goals tile opens its list in place.
END_DIR = ROOT / "assets/shared/module-end"
def end_img(name):
    f = END_DIR / f"{name}.svg"
    if not f.is_file(): return ""   # test copies (test_reviews.py) may leave the shared assets out
    svg = f.read_text(encoding="utf-8").strip()
    return svg.replace("<svg", '<svg aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid slice"', 1)


def end_tiles(code, mod, T, lang, built_ids, exam_built, practice_built):
    items = concept_cards.module_section(code, T, lang, chapter_titles(code, built_ids), end_img("deck"))
    if code in exam_built:
        items += cardgrid.card(exam_built[code], T("exam.title"), practice.page_name(code + practice.EXAM), svg=end_img("exam"), cls=" me-tile")
    if code in practice_built:
        items += cardgrid.card(practice_built[code], T("practice.title"), practice.page_name(code), svg=end_img("challenge"), cls=" me-tile")
    goals = mod.get("tavoitteet", [])
    if goals:
        img = end_img("goals")
        items += (f'<li class="live ch-card me-tile me-goals"><details class="goals"><summary>'
                  + (f'<span class="ch-img">{img}</span>' if img else "")
                  + f'<span class="l-num">{T.count("site.course_goals_n", len(goals))}</span><span class="ch-title">{T("site.course_goals")}</span></summary>'
                  f'<div class="me-goals-body"><p>{T("site.course_goals_lead")}</p><ul>{"".join(f"<li>{esc(g)}</li>" for g in goals)}</ul></div></details></li>')
    return cardgrid.grid(items, ' id="moduulin-loppu"') if items else ""


def chapter_nav(out, modules, built_ids, practice_built, exam_built=()):
    """Edellinen luku / Seuraava luku under every lesson and Sovella page of this language (teacher 2026-10-29). The
    order is the module's lesson order in curriculum.json (the teaching order: FY3 is not numeric), only published
    pages are linked, the first chapter leads back to the module page, the last to the Esimerkkikoe and then
    Haastetehtävät (Sovella) when published (else the module page), each back to the one before. Links stay in this language's
    folder, so the language is kept; new chapters join the sequence when they are published."""
    if only:                                       # a preview links the lessons a full build would publish, and itself
        built_ids = built_ids | {f.name for f in courses.lessons(lang=T.lang) if review_status(f)["state"] != "draft"}
    def link(cls, rel, href, direction, name):
        return (f'<a class="{cls}" href="{href}"{f" rel={chr(34)}{rel}{chr(34)}" if rel else ""}>'
                f'<span class="dir">{direction}</span><span class="name">{esc(name)}</span></a>')
    for code, mod in modules:
        seq = [(l["id"] + ".html", l["title"]) for l in mod.get("lessons", []) if l["id"] in built_ids]
        if code in exam_built: seq.append((practice.page_name(code + practice.EXAM), T("exam.title")))     # teacher 2026-11-05: koe, then Haastetehtävät
        if code in practice_built: seq.append((practice.page_name(code), T("practice.title")))
        course = (f"{code}.html", T("lesson.chapter_course", course=code))
        for i, (name, _) in enumerate(seq):
            f = out / name
            if f.is_file(): f.write_text(chapter_crumbs(f.read_text(), code, mod, seq, i, built_ids))
            f = out / name
            if not f.is_file(): continue
            prev = seq[i - 1] if i else None; nxt = seq[i + 1] if i + 1 < len(seq) else None
            nav = (f'<nav class="chapter-nav" aria-label="{esc(T("lesson.chapter_nav"))}">'
                   + (link("prev", "prev", prev[0], T("lesson.chapter_prev"), prev[1]) if prev else link("prev up", "", course[0], T("lesson.chapter_up"), course[1]))
                   + (link("next", "next", nxt[0], T("lesson.chapter_next"), nxt[1]) if nxt else link("next up", "", course[0], T("lesson.chapter_up"), course[1]))
                   + "</nav>")
            f.write_text(f.read_text().replace(f"<!--fl-chapter-nav:{name[:-5]}-->", nav))


CRUMBS = re.compile(r'(<nav class="crumbs"[^>]*>).*?(</nav>)', re.S)


def chapter_crumbs(html, code, mod, seq, i, built_ids):
    """The path over a chapter page goes from chapter to chapter (teacher 2026-11-08): its last part is a menu
    "Luku 13: title" (on a phone "Luku 13", as the title is right below) that opens the module's chapters under its
    themes, then Esimerkkikoe, Haastetehtävät and the module page; at its right end Edellinen / Seuraava in the same
    order as the links under the page (chapter_nav). No new row: "FY3 · Luku 13" over the title shows only on paper
    (site.css), where the path is not printed. A <details>, so it works without scripts; lesson.js closes it."""
    name, title = seq[i]
    lid = name[:-5]
    slots = mod.get("lessons", [])
    n = next((k for k, l in enumerate(slots, 1) if l["id"] == lid), None)
    here = (f'{T("site.chapter_n", n=n)}<span class="tt">: {esc(title)}</span>' if n else esc(title))
    themes = {th["first"]: th["title"] for th in mod.get("themes", [])}
    items, cur_ol = "", False
    for k, l in enumerate(slots, 1):
        if l["id"] in themes or not cur_ol:
            items += ("</ol>" if cur_ol else "") + (f'<p class="ch-menu-theme">{esc(themes[l["id"]])}</p>' if l["id"] in themes else "") + "<ol>"
            cur_ol = True
        label = f'<span class="n">{k}</span><span>{esc(l["title"])}</span>'
        if l["id"] == lid: items += f'<li><a href="{l["id"]}.html" aria-current="page">{label}</a></li>'
        elif l["id"] in built_ids: items += f'<li><a href="{l["id"]}.html">{label}</a></li>'
        else: items += f'<li><span class="soon">{label}</span></li>'
    items += "</ol>" if cur_ol else ""
    # Esimerkkikoe and Haastetehtävät numbered on after the chapters (17, 18 in a 16-chapter module), no "Moduulin
    # sivulle" row: the path above leads there (teacher 2026-11-08)
    extra = [(h, t) for h, t in seq if not h.startswith(tuple(l["id"] + "." for l in slots))]
    more = "".join(f'<li><a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if h == name else ""}><span class="n">{len(slots) + j}</span><span>{esc(t)}</span></a></li>'
                   for j, (h, t) in enumerate(extra, 1))
    prev = seq[i - 1] if i else (f"{code}.html", T("lesson.chapter_up"))
    nxt = seq[i + 1] if i + 1 < len(seq) else (f"{code}.html", T("lesson.chapter_up"))
    arrow = lambda cls, h, label, short, t: (f'<a class="{cls}" href="{h}" aria-label="{esc(label)}: {esc(t)}">'
                                             + (f'‹<span class="lbl">{short}</span>' if cls == "prev" else f'<span class="lbl">{short}</span>›') + "</a>")
    crumbs = (f'<a href="index.html">{T("site.name")}</a> › <a href="{code}.html">{code}</a> › '
              f'<details class="ch-menu"><summary><span class="t">{here}</span></summary>'
              f'<div class="ch-menu-panel">{items}' + (f'<ol class="ch-menu-more">{more}</ol>' if more else '') + '</div></details>'
              f'<span class="ch-arrows">{arrow("prev", prev[0], T("lesson.chapter_prev"), T("lesson.crumb_prev"), prev[1])}'
              f'{arrow("next", nxt[0], T("lesson.chapter_next"), T("lesson.crumb_next"), nxt[1])}</span>')
    return CRUMBS.sub(lambda m: m.group(1) + crumbs + m.group(2), html, count=1)


def unit_sections(md_text):
    """(intro html, {section key: html}) of a unit's text, laid out as a lesson's (figures beside their paragraph,
    the worked example in stages, a formula section named after its law)."""
    html = staged_example(fig_rows(named_sections(nbsp_units(render_md(example_md(md_text))))))
    pieces = re.split(r"(?=<h2[ >])", html)
    intro = pieces[0] if not pieces[0].startswith("<h2") else ""
    sections = {}
    for piece in pieces[1:] if intro or len(pieces) > 1 else []:
        m = re.match(r'<h2(?: data-section="([^"]*)")?>(.*?)</h2>', piece)
        if m: sections[_h.unescape(m.group(1) or m.group(2))] = re.sub(r"^<h2[^>]*>(.*?)</h2>", r'<h3 class="theory-h">\1</h3>',
                                                             re.sub(r"<(/?)h3>", r"<\1h4>", piece), count=1)
    return intro, sections


def build_units(lang, out, unit_pub):
    """The course units in this language, written in it or translated into it (scripts/units.py): each page in the
    lesson template with the inquiry stages, the course's components (units/<course>/units.js and units.css), its
    simulation, its credits, sources and teacher notes, Previous / Next unit in the course's order, "Luvun tärkeät
    käsitteet" in an S2 language and, once another language publishes the unit too, the language links (teacher
    2026-11-04, FY9 in en and fi-easy). A draft is built only as a preview. unit_pub: {unit id: languages published}."""
    published = {f"{u}.html" for u, ls in unit_pub.items() if lang in ls}
    for uid in units.ids(lang):
        if only and only != uid: continue
        if lang not in unit_pub.get(uid, ()): continue
        errs = units.check(uid, lang)
        if errs: sys.exit("\n".join(errs))
        d = units.load(uid, lang); st = units.status(uid, lang); f = units.folder(uid, lang); code = d["course"]
        md_text = (f / "unit.md").read_text()
        inq = json.loads((f / "inquiry.json").read_text())
        intro, sections = unit_sections(md_text)
        sim = ""; sf = units.sim_folder(uid, lang)
        if sf:
            pub = "sims/" + d["sim"]
            shutil.copytree(sf, SITE / pub, dirs_exist_ok=True); assets.append(f"{pub}/sim.js")
            css = f'<link rel="stylesheet" href="{pub}/sim.css">' if (sf / "sim.css").is_file() else ""
            model = f'<script src="{pub}/model.js"></script>' if (sf / "model.js").is_file() else ""
            sim = (f'<section id="sim">{sim_head(inq)}{css}<div id="sim-root" data-base="{pub}/"></div>'
                   f'<script src="vendor/p5.min.js"></script><script src="sim-embed.js"></script>{model}<script src="{pub}/sim.js"></script><!--sim-info--></section>')
        exit_html = ""
        if (f / "exit-ticket.json").is_file():
            exit_q = json.loads((f / "exit-ticket.json").read_text())
            exit_html = (f'<div id="exit"><h3>{inquiry.exit_title()}</h3><ol>' + "".join(
                f"<li>{nbsp_units(q['q'])}<details class=\"answer\"><summary>{T('lesson.answer')}</summary><div class=\"answer-body\">{nbsp_units(render_md(q['a']))}</div></details></li>"
                for q in exit_q) + "</ol></div>")
        md = lambda t: nbsp_units(render_md(t))
        tasks_html = ""                                  # the unit's own task set (FY9): its Tehtävät, last on the page
        if units.has_tasks(uid, lang):
            tasks_html, _ = practice.render(units.task_key(uid), lang, md, solution_html, T("practice.title"), embedded=True, prefix=units.number(uid))
        body, toc = inquiry.render(f, inq, {"intro": intro, "sections": sections, "sim": sim, "exercises": tasks_html, "exit": exit_html,
                                            "concepts": inquiry.key_concepts_html(uid, d.get("key_concepts"), md),
                                            "selfassess": self_assesses(lang, {"course": code, "id": uid})}, md)   # Selkeä suomi only (NOTES.md §12)
        if not tasks_html:
            for key in ("check_practice", "further_practice"):   # a unit without tasks has no exercises section: point to the theory summary only
                body = body.replace(T(f"inquiry.{key}"), re.sub(r'(,| and)[^<]*<a href="#exercises">[^<]*</a>', "", T(f"inquiry.{key}")))
        tail = units.tail_html(uid, lang, T, md, teacher=bool(only or build_all))   # sources and teacher notes: previews only
        if "id=\"sources\"" in tail: toc += f'<a href="#sources" class="toc-end"><span class="toc-label">{T("units.sources")}</span></a>'
        cdir = ROOT / "assets" / "units" / code.lower()
        if cdir.is_dir(): assets.append(f"units/{code.lower()}/units.js")
        head = f'<link rel="stylesheet" href="units/{code.lower()}/units.css">' if (cdir / "units.css").is_file() else ""
        block = strings_block(None)
        sb = units.sim_block(uid, lang)
        if sb is not None:
            data = json.loads(re.search(r'>(.*)</script>', block, re.S).group(1).replace("<\\/", "</")); data["sim"] = sb
            block = '<script id="fl-strings" type="application/json">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>"
        embedded = ""                                    # the data files the components read, in the page (works from file: and offline)
        for ref in dict.fromkeys(re.findall(r'data-src=\\?"(units/[^"\\]+\.json)\\?"', md_text + (f / "inquiry.json").read_text())):
            embedded += (f'<script type="application/json" class="fx-src" data-for="{ref}">'
                         + json.dumps(json.loads(units.asset_source(ref).read_text()), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>")
        body = chapter_eyebrow(body, code, units.number(uid)) if tasks_html else body   # "FY9 · Luku 1.2": the number its tasks carry
        notice_html = "" if st["state"] == "reviewed" else f'<p class="notice" role="note">{T("units.notice_draft")}</p>'
        html = (texts(tpl).replace("{{title}}", esc(d["title"])).replace("{{course}}", code).replace("{{notice}}", notice_html)
                .replace("{{strings}}", block + head).replace("{{back_to_course}}", esc(T("site.back_to_course", course=code)))
                .replace("{{toc}}", toc).replace("{{main}}", f'<article id="teoria" class="inquiry unit unit-{d["kind"]}" data-course="{code.lower()}">{body}{units.course_nav(uid, lang, T, published)}{tail}</article>' + embedded)   # Previous / Next before the credits (teacher 2026-11-06)
                .replace("{{scripts}}", f'<script src="inquiry.js"></script>' + ('<script src="selfassess.js"></script>' if tasks_html else "")
                         + (f'<script src="units/{code.lower()}/units.js"></script>' if cdir.is_dir() else "")
                         + (submission_script(lang, uid) if tasks_html else ""))
                .replace("{{description}}", esc(d["description"])).replace("{{url}}", URL + f"{uid}.html")
                .replace("{{languages}}", languages_nav(f"{uid}.html") if len(unit_pub[uid]) > 1 else ""))   # a unit in one language has none
        (out / f"{uid}.html").write_text(rebase(html))
        print("built", uid, f"({st['state']})")


def build_language(lang):
    """Every lesson, course page and the front page of one language into OUTS[lang]."""
    global UP, URL, COURSES
    i18n.set_lang(lang); out = OUTS[lang]; out.mkdir(exist_ok=True)
    UP = "" if lang == i18n.SOURCE else "../"; URL = BASE_URL + ("" if lang == i18n.SOURCE else f"{lang}/")
    f = ROOT / "content" / lang / "courses.json"
    COURSES = json.loads(f.read_text()) if lang != i18n.SOURCE and f.is_file() else {}
    built = {}   # course -> [meta, ...]
    cards = {}   # lesson id -> (opening illustration, Miksi question): the module page's chapter cards
    states = {}  # lesson id -> review state of every lesson seen, also the ones left out
    for folder in courses.lessons(lang=lang):
        meta = json.loads((folder / "meta.json").read_text())
        if only and meta["id"] != only: continue
        try: rs = review_status(folder)
        except ValueError as e: sys.exit(str(e))
        meta["state"] = rs["state"]; states[meta["id"]] = rs
        tr = folder / "figures.json"                                               # force-diagram symbols in this language
        fbdspec.SYMBOLS = {k: v for k, v in json.loads(tr.read_text()).items() if re.fullmatch(r"[A-Z]_\w+", k)} if tr.exists() else {}
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
        core = core_ids(ex)
        ch_no = chapter_no(meta["course"], meta["id"]); k = 0   # running number over all levels: 6-1 ... 6-12 (teacher 2026-11-04)
        for lvl, items in ex.items():
            ex_html += (f"<details class=\"level\"><summary>{T('lesson.level', n=lvl[-1])} · {T('lesson.level_kind_' + lvl[-1])} "
                        f"<span class=\"count\">{T.count('lesson.level_count', len(items))}</span></summary><p class=\"level-lead\">{T('lesson.level_lead_' + lvl[-1])}</p><ol>")
            for i, e in enumerate(items):
                show = publish == "all" or (publish == "first" and i == 0); k += 1
                ex_html += exercise_html(e, solutions.get(e["id"]) if show else None, None if isinstance(ex_src, WorkTree) else ex_src.read, core=e["id"] in core,
                                         num=f"{ch_no}-{k}" if ch_no else None)
            ex_html += "</ol></details>"
        exit_q = json.loads((folder / "exit-ticket.json").read_text())
        exit_items = "<ol>" + "".join(
            f"<li>{nbsp_units(q['q'])}<details class=\"answer\"><summary>{T('lesson.answer')}</summary><div class=\"answer-body\">{nbsp_units(render_md(mathlayout.display_chains(q['a'])))}</div></details></li>"
            for q in exit_q) + "</ol>"
        lesson_md = (folder / "lesson.md").read_text()
        lesson_html = staged_example(fig_rows(named_sections(nbsp_units(render_md(example_md(lesson_md))))))
        lesson_raw = lesson_html                          # the inquiry layout credits the photographs of the whole page (theory and tasks)
        lesson_html, photo_tail = photos(lesson_html)
        inq = inquiry.load(folder)
        if inq is not None:
            errs = inquiry.validate(folder, inq, lesson_md)
            if errs: sys.exit("\n".join(errs))
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
            # model.js: the physics without drawing (README "Simulation models"), loaded first and tested by test_models.py
            model = f'<script src="{pub}/model.js"></script>' if (src / "model.js").is_file() else ""
            if model: assets.append(f"{pub}/model.js")
            sim = (f'<section id="sim">{sim_head(inq)}{css}<div id="sim-root" data-base="{pub}/"></div>'
                   f'<script src="vendor/p5.min.js"></script><script src="sim-embed.js"></script>{model}<script src="{pub}/sim.js"></script><!--sim-info--></section>')
        for ref in courses.pic_refs_in([(courses.lesson_file(folder, n).read_text() if courses.lesson_file(folder, n).exists() else "") for n in courses.LESSON_TEXTS] + [ex_text, sol_text]):   # pictures the text refers to, at the same relative path
            if not courses.pic_source(ref).is_file(): sys.exit(f"{meta['id']}: picture {ref} not found (expected assets/{ref})")
            (SITE / ref).parent.mkdir(parents=True, exist_ok=True); shutil.copy(courses.pic_source(ref), SITE / ref); assets.append(ref)
        name = f"{meta['id']}.html"
        titles = chapter_titles(meta["course"])
        kc_section = concept_cards.lesson_section(meta["course"], meta["id"], T, lang, titles)   # "Kertaa luvun käsitteet": the end of Esimerkit (teacher 2026-11-05)
        if inq is None:                                   # classic layout: theory (with the sim inside), exit ticket, exercises
            sim = sim.replace("<!--sim-info-->", "")
            if sim and "<!-- sim -->" in lesson_html: lesson_html = lesson_html.replace("<!-- sim -->", sim, 1)
            elif sim and re.search(rf"<h2[^>]*>{re.escape(T('sections.Esimerkki'))}", lesson_html):
                lesson_html = re.sub(rf"(<h2[^>]*>{re.escape(T('sections.Esimerkki'))})", lambda m: sim + m.group(1), lesson_html, count=1)
            elif sim: lesson_html += sim
            toc = (f'<a href="#teoria">{T("lesson.theory")}</a>' + (f'<a href="#sim">{T("lesson.simulation")}</a>' if sim else "")
                   + f'<a href="#exit">{inquiry.exit_title()}</a>' + (concept_cards.lesson_nav(T) if kc_section else "") + f'<a href="#exercises">{inquiry.exercises_title()}</a>')
            main = (f'<article id="teoria">{lesson_html}</article>\n'
                    f'<section id="exit"><h2>{inquiry.exit_title()}</h2>{exit_items}</section>\n' + kc_section +
                    f'<section id="exercises"><h2>{inquiry.exercises_title()}</h2>{ex_html}</section><!--fl-chapter-nav:{meta["id"]}-->{photo_tail}')
        else:                                             # inquiry layout: the same parts placed by inquiry.json (scripts/inquiry.py)
            lesson_html = lesson_raw.replace("<!-- sim -->", "")
            pieces = re.split(r"(?=<h2[ >])", lesson_html)
            intro = pieces[0] if not pieces[0].startswith("<h2") else ""
            sections = {}
            for piece in pieces[1:] if intro or len(pieces) > 1 else []:
                m = re.match(r'<h2(?: data-section="([^"]*)")?>(.*?)</h2>', piece)
                if m: sections[_h.unescape(m.group(1) or m.group(2))] = re.sub(r"^<h2[^>]*>(.*?)</h2>", r'<h3 class="theory-h">\1</h3>',
                                                                     re.sub(r"<(/?)h3>", r"<\1h4>", piece), count=1)   # a ### subheading under its section heading
            if kc_section and "Tiivistelmä" in sections:   # the chapter's concept chips after the summary list (concept_cards.chips)
                tv = sections["Tiivistelmä"]; kc = concept_cards.chips(meta["course"], meta["id"], T, lang)
                sections["Tiivistelmä"] = tv.replace("</ul>", "</ul>" + kc, 1) if "</ul>" in tv else tv + kc
            parts = {"intro": intro, "sections": sections, "sim": sim, "exercises": ex_html,
                     "concepts": inquiry.key_concepts_html(meta["id"], meta.get("key_concepts"), lambda t: nbsp_units(render_md(t))),   # Selkeä suomi only (NOTES.md §12)
                     "exit": f'<div id="exit"><h3>{inquiry.exit_title()}</h3>{exit_items}</div>', "cards": kc_section,
                     "selfassess": self_assesses(lang, meta)}
            body, toc = inquiry.render(folder, inq, parts, lambda t: nbsp_units(render_md(t)))
            if kc_section:   # bold terms of Teoriatiivistelmä that name a card open it (never before that stage)
                body = re.sub(r'<section class="stage" id="selita".*?</section>', lambda m: concept_cards.mark_terms(m.group(0), meta["course"], lang), body, count=1, flags=re.S)
            body, photo_tail = photos(body)               # a photograph may also open a task (FY4 2026-11-03: Pohdinta)
            main = f'<article id="teoria" class="inquiry">{body}<!--fl-chapter-nav:{meta["id"]}-->{photo_tail}</article>'   # Edellinen / Seuraava luku before the photo credits (teacher 2026-11-06)
        main = chapter_eyebrow(main, meta["course"], ch_no)
        skey = (meta["id"] if where[0] == "lesson" else where[1].name) if where else None   # the sim's block of lang "sims"
        html = (texts(tpl).replace("<title>{{title}}", "<title>" + esc(plain_tex(meta["title"]))).replace('og:title" content="{{title}}', 'og:title" content="' + esc(plain_tex(meta["title"])))
                .replace("{{title}}", esc(meta["title"])).replace("{{course}}", meta["course"]).replace("{{notice}}", notice(meta["state"]))
                .replace("{{strings}}", strings_block(skey)).replace("{{back_to_course}}", esc(T("site.back_to_course", course=meta["course"])))
                .replace("{{toc}}", toc).replace("{{main}}", main)
                .replace("{{scripts}}", ('<script src="inquiry.js"></script>' if inq else "") + (course_block(meta["course"], lang) if submits(lang, meta["id"]) else "") + submission_script(lang, meta["id"]))
                .replace("{{description}}", esc(description_of(meta, lesson_md))).replace("{{url}}", URL + name)
                .replace("{{languages}}", languages_nav(name)))
        (out / name).write_text(rebase(html))
        built.setdefault(meta["course"], []).append(meta)
        cards[meta["id"]] = chapter_card(html)
        print("built", meta["id"], f"({meta['state']})")

    fbdspec.SYMBOLS = {}                                                           # the pages after the lessons: specs as written
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
        body = body.replace("</header>", "</header>" + concept_cards.practice_section(code, T, lang), 1)   # the deck's cards before the tasks (teacher 2026-11-03)
        ptitle = T("practice.title")
        html = (texts(tpl).replace("{{title}}", esc(ptitle)).replace("{{course}}", code).replace("{{notice}}", notice("reviewed" if ps["state"] == "reviewed" else "draft"))
                .replace("{{strings}}", strings_block(None)).replace("{{back_to_course}}", esc(T("site.back_to_course", course=code)))
                .replace("{{toc}}", ptoc).replace("{{main}}", f'<article id="teoria" class="inquiry practice">{body}</article><!--fl-chapter-nav:{code}-sovella-->')
                .replace("{{scripts}}", '<script src="selfassess.js"></script>')
                .replace("{{description}}", esc(T("practice.description", code=code, title=course_text(code, curriculum[code])["title"]))).replace("{{url}}", URL + pname)
                .replace("{{languages}}", languages_nav(pname)))
        (out / pname).write_text(rebase(html))
        tasks = practice.load(code, lang)["tasks"]
        practice_built[code] = T("practice.course_count", tasks=T.count("practice.tasks_n", len(tasks)),
                                                points=T.count("practice.task_points", sum(practice.total(t) for t in tasks if t.get("kind") != "own")))
        print("built", pname, f"({ps['state']})")

    # Esimerkkikoe: a course's example exam (scripts/practice.py render_exam, docs/exam-guidelines.md, teacher 2026-11-05),
    # the same task format and gate as Sovella itsenäisesti, its page after it; a preview builds it with `build.py <COURSE>-koe`.
    exam_built = {}
    for key in practice.exams(lang):
        code, pname = practice.course_of(key), practice.page_name(key)
        if only and only != pname[:-5]: continue
        ps = practice.status(key, lang)
        if ps["state"] != "reviewed" and not (only or build_all):
            if (LIVE / out.relative_to(SITE) / pname).is_file():
                print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING:'} {pname} is on the live site but its reviews are not current; this build removes it")
            continue
        body, ptoc = practice.render(key, lang, lambda t: nbsp_units(render_md(t)), solution_html, T("exam.title"))
        html = (texts(tpl).replace("{{title}}", esc(T("exam.title"))).replace("{{course}}", code).replace("{{notice}}", notice("reviewed" if ps["state"] == "reviewed" else "draft"))
                .replace("{{strings}}", strings_block(None)).replace("{{back_to_course}}", esc(T("site.back_to_course", course=code)))
                .replace("{{toc}}", ptoc).replace("{{main}}", f'<article id="teoria" class="inquiry practice exam">{body}</article><!--fl-chapter-nav:{code}-koe-->')
                .replace("{{scripts}}", '<script src="selfassess.js"></script>')
                .replace("{{description}}", esc(T("exam.description", code=code, title=course_text(code, curriculum[code])["title"]))).replace("{{url}}", URL + pname)
                .replace("{{languages}}", languages_nav(pname)))
        (out / pname).write_text(rebase(html))
        exam_built[code] = T("exam.course_count", max=practice.max_points(practice.load(key, lang)))
        print("built", pname, f"({ps['state']})")

    # Course pages and front page. Every module in curriculum.json gets a page; lessons built in this run are
    # links, the rest are listed as "tulossa" so students see the whole course and nav links always resolve.
    modules = [(k, course_text(k, v)) for k, v in curriculum.items() if not k.startswith("_")]
    built_ids = {m["id"] for ms in built.values() for m in ms}
    legacy_ids = {m["id"] for ms in built.values() for m in ms if m["state"] == "legacy"}

    # The front page's module list (teacher 2026-11-03, "tiivistä etusivu"): one row per module, the whole row one link
    # to its page, with the icon, code, title and Miksi question only (no counts, credits or calls to action). The
    # modules with published lessons on the left, except those the teacher still shows under Tulossa (HOME_COMING),
    # which go dimmed to the right column with the modules that have none yet.
    # Availability is what this language's build published (built_ids, practice_built), never a hardcoded count and
    # never a student's progress: the module page says it.
    def availability(done, n):
        """Concrete labels for a module: (main, extra), e.g. ("8 oppituntia", "") or ("2 oppituntia saatavilla", "14 tulossa")."""
        if not done: return T.count("site.lessons_planned", n), ""
        if done == n: return T.count("site.lessons_all", done), ""
        return T.count("site.lessons_available", done), T.count("site.lessons_coming", n - done)

    catalogue = ""; upcoming = ""
    for code, mod in modules:
        slots = mod.get("lessons", [])
        done = sum(1 for l in slots if l["id"] in built_ids)
        kind = T("site.course_type_required") if mod.get("type") == "pakollinen" else T("site.course_type_optional")
        main_label, extra_label = availability(done, len(slots))
        credits = f'{T("site.credits", n=mod.get("op", ""))} · {kind}'
        if done and code not in HOME_COMING: catalogue += home_row(code, mod["title"], T("site.module_question." + code))
        else: upcoming += home_row(code, mod["title"], T("site.module_question." + code), coming=True)

        items = chapter_cards(code, mod, slots, built_ids, legacy_ids, cards)
        # a language link from a page this language lacks lands here (link_languages): the note at its #unavailable-<id> says so
        missing = [(l["id"], l["title"]) for l in slots if l["id"] not in built_ids]
        if code not in practice_built: missing.append((f"{code}-sovella", T("practice.title")))
        if code not in exam_built: missing.append((f"{code}-koe", T("exam.title")))
        notes = "".join(f'<p class="unavailable" id="unavailable-{lid}" role="note" tabindex="-1">{T("site.unavailable_note", title=esc(title))}</p>'
                        for lid, title in missing)
        goals = "".join(f"<li>{esc(g)}</li>" for g in mod.get("tavoitteet", []))
        body = (notes + f'<div class="mod-head">{module_icons.img(code, 56, "mod-head-icon")}<div><span class="eyebrow">{code} · {credits}</span><h1>{esc(mod["title"])}</h1></div></div>'
                f'<p class="lead">{esc(T("site.module_question." + code))}</p>'
                f'<p class="mod-status">{main_label}{(" · " + extra_label) if extra_label else ""}</p>'
                + progress_section(code, lang, mod)
                + resume_box() + f'<h2>{T("site.course_lessons")}</h2>{items}'
                + end_tiles(code, mod, T, lang, built_ids, exam_built, practice_built) + '<script src="jatka.js"></script>')
        desc = T("site.course_description", code=code, title=mod["title"], done=done, n=len(slots))
        (out / f"{code}.html").write_text(page(T("site.course_title", code=code, title=mod["title"]), body,
                                                f'<a href="index.html">{T("site.name")}</a> › {code}', f"{code}.html", desc, main_class="reading module-page"))

    chapter_nav(out, modules, built_ids, practice_built, exam_built)

    # Lukiokohtaiset opintojaksot (teacher 2026-10-30, scripts/local_courses.py): school-specific courses from
    # local-courses.json, apart from the national modules; a page and a front-page row in each language that has the
    # course. A language without one keeps a note at its front page's #unavailable-<CODE> for the language links.
    chapters = {l["id"]: (code, l["title"]) for code, mod in modules for l in mod.get("lessons", [])}
    # Kokeelliset tutkimukset (teacher 2026-10-30, scripts/investigations.py): one canonical page each, published like
    # a lesson when both reviews pass; the pages of the courses it names list it.
    # TVT-ohjeet (teacher 2026-10-31, scripts/guides.py): one page per skill, published like an investigation and
    # linked from every investigation that needs it; each guide names the published investigations that use it.
    guide_built = {}
    guide_ok = {g for g in guides.ids(lang) if guides.status(g, lang)["state"] == "reviewed" or (only == g) or build_all}
    for gid in guides.ids(lang):
        if only and only != gid and gid not in guide_ok: continue
        if gid not in guide_ok:
            if (LIVE / out.relative_to(SITE) / f"{gid}.html").is_file():
                print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING:'} {gid}.html is on the live site but its reviews are not current; this build removes it")
            continue
        guide_built[gid] = guides.load(gid, lang)
    inv_ok = [i for i in investigations.ids(lang) if investigations.status(i, lang)["state"] == "reviewed" or build_all]
    published = {f"{i}.html" for i in built_ids} | {f"{g}.html" for g in guide_built}
    for gid, d in guide_built.items():
        if only and only != gid: continue
        st = guides.status(gid, lang)
        users = [(i, investigations.load(i, lang)["title"]) for i in inv_ok
                 if any(gid in p.get("guides", []) for p in investigations.load(i, lang)["prerequisites"])
                 or f"[[ohje:{gid}|" in (investigations.folder(i, lang) / "investigation.md").read_text()]
        body, gtoc = guides.render(gid, lang, T, lambda t: nbsp_units(render_md(t)), published, users)
        for ref in guides.pic_refs(gid, lang):            # screenshots, at the same relative path as a lesson's pictures
            if not courses.pic_source(ref).is_file(): sys.exit(f"{gid}: picture {ref} not found (expected assets/{ref})")
            (SITE / ref).parent.mkdir(parents=True, exist_ok=True); shutil.copy(courses.pic_source(ref), SITE / ref); assets.append(ref)
        html = (texts(tpl).replace("{{title}}", esc(d["title"])).replace("{{course}}", "FY10").replace("{{notice}}", "" if st["state"] == "reviewed" else f'<p class="notice" role="note">{T("guides.notice_draft")}</p>')
                .replace("{{strings}}", strings_block(None)).replace("{{back_to_course}}", esc(T("site.back_to_course", course="FY10")))
                .replace("{{toc}}", gtoc).replace("{{main}}", body).replace("{{scripts}}", "")
                .replace("{{description}}", esc(d["description"])).replace("{{url}}", URL + f"{gid}.html")
                .replace("{{languages}}", languages_nav(f"{gid}.html")))
        (out / f"{gid}.html").write_text(rebase(html))
        print("built", gid, f"({st['state']})")
    inv_built = {}
    for iid in investigations.ids(lang):
        if only and only != iid: continue
        st = investigations.status(iid, lang)
        if st["state"] != "reviewed" and not (only or build_all):
            if (LIVE / out.relative_to(SITE) / f"{iid}.html").is_file():
                print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING:'} {iid}.html is on the live site but its reviews are not current; this build removes it")
            continue
        d = investigations.load(iid, lang); course = d["courses"][0]
        body, itoc = investigations.render(iid, lang, T, lambda t: nbsp_units(render_md(t)), chapters, published)
        html = (texts(tpl).replace("{{title}}", esc(d["title"])).replace("{{course}}", course).replace("{{notice}}", "" if st["state"] == "reviewed" else f'<p class="notice" role="note">{T("investigation.notice_draft")}</p>')
                .replace("{{strings}}", strings_block(None)).replace("{{back_to_course}}", esc(T("site.back_to_course", course=course)))
                .replace("{{toc}}", itoc).replace("{{main}}", body).replace("{{scripts}}", '<script src="investigation.js"></script>')
                .replace("{{description}}", esc(d["description"])).replace("{{url}}", URL + f"{iid}.html")
                .replace("{{languages}}", languages_nav(f"{iid}.html")))
        (out / f"{iid}.html").write_text(rebase(html)); inv_built[iid] = d
        print("built", iid, f"({st['state']})")
    # Course units (teacher's brief 2026-11-01, FY14; scripts/units.py): the lessons of a local course written in its
    # own language and, for a course with "translations" (FY9, teacher 2026-11-04), translated, each language version
    # published in its language's folder when its own three reviews pass (a translation only where that language has
    # the course, so its links to the course page hold). Every language's course page links each unit's version in its
    # own language when published, else the source language's, so this is decided from the reviews, not from built files.
    unit_pub = {}
    for ul, u in units.all_units():
        if not (units.status(u, ul)["state"] == "reviewed" or build_all or only == u): continue
        if units.is_translation(u, ul) and not (build_all or only) and units.load(u, ul)["course"] not in local_courses.load(ul):
            if ul == lang: print(f"note: {ul}/{u}.html waits for {units.load(u, ul)['course']} in content/{ul}/local-courses.json"); continue
        unit_pub.setdefault(u, set()).add(ul)
    if lang in units.languages(): build_units(lang, out, unit_pub)
    local = local_courses.load(lang)
    local_rows = ""; kr_built = []; lt_built = []
    ahjo_data = ahjo.load(lang)
    for code, c in local.items():
        cu = []
        for u, ls in unit_pub.items():                   # (id, the language linked, href): this language's version, else the source's
            ul = lang if lang in ls else units.lang_of(u) if units.lang_of(u) in ls else None
            if ul and units.load(u, ul)["course"] == code: cu.append((u, ul, os.path.relpath(OUTS[ul] / f"{u}.html", out).replace(os.sep, "/")))
        local_rows += home_row(code, c["title"], c.get("front_line") or c["subtitle"])
        kr = kilparobo.load(lang) if code == kilparobo.CODE else None   # Kilparobotiikka's team pages (teacher 2026-11-09, scripts/kilparobo.py)
        lt = lumatutor.load(lang) if code == lumatutor.CODE else None   # LUMA-tutor's pages (teacher 2026-11-09, scripts/lumatutor.py)
        if lt:
            lt["_course_title"] = c["title"]; lt_ws = lumatutor.workshops(lang)
            body = lumatutor.hub_body(lt, local_courses.head(code, c, T), lt_ws)
        elif kr:
            kr["_course_title"] = c["title"]
            body = kilparobo.hub_body(kr, local_courses.head(code, c, T), local_courses.photos_html(c, T, heading=False), local_courses.quotes_html(c, T, heading=False))
        else:
            body = local_courses.page_body(code, c, T, chapters, {f"{i}.html" for i in built_ids}, [(i, d) for i, d in inv_built.items() if code in d["courses"]],
                                           guides.course_section(T, published, lang) if code == "FY10" else "", cu)
        prog = local_progress(code, c, lang)                 # Näytä edistyminen before the course's first section (FY9)
        if prog and "<h2" in body: body = body.replace("<h2", prog + "<h2", 1)
        for ph in c.get("photos", []):                  # the course's photos (local_courses.py), shared by every language like a lesson's
            (SITE / ph["src"]).parent.mkdir(parents=True, exist_ok=True); shutil.copy(ROOT / "assets" / ph["src"], SITE / ph["src"]); assets.append(ph["src"])
        name = f"{local_courses.label(code)} {c['title']}".strip()
        html = page(name, body + '<script src="invfilter.js"></script>', f'<a href="index.html">{T("site.name")}</a> › {local_courses.label(code) or esc(c["title"])}',
                    f"{code}.html", c["description"], main_class="reading module-page local-course" + (" kr-theme" if c.get("theme") == "kiviruukki" else "") + (" kr-team" if kr or lt else "") + (" lt-course" if lt else ""))
        (out / f"{code}.html").write_text(ahjo.kiviruukki_mark(html) if c.get("theme") == "kiviruukki" else html)
        if kr:                                           # its four other pages, under the course page in the breadcrumb
            ref = lambda rid: (chapters[rid][1], f"{rid}.html") if rid in chapters and rid in built_ids else None
            diary = "ahjo-projektipaivakirja.html" if ahjo_data and "ahjo-projektipaivakirja" in ahjo.ready_guides(ahjo_data) else None
            crumb = f'<a href="index.html">{T("site.name")}</a> › <a href="{code}.html">{esc(c["title"])}</a> › '
            for name, sub in ((kilparobo.PATH, kilparobo.path_body(kr, ref)), (kilparobo.SEASON, kilparobo.season_body(kr, diary)),
                              (kilparobo.MENTOR, kilparobo.mentor_body(kr)), (kilparobo.SAFETY, kilparobo.safety_body(kr, ahjo.SAFETY if ahjo_data else None))):
                title, lead = kilparobo.page(kr, name)["title"], kilparobo.page(kr, name)["lead"]   # the unit's pages are jakso.json's (scripts/jaksot.py)
                (out / name).write_text(ahjo.kiviruukki_mark(page(title, sub + '<script src="ahjo.js"></script>', crumb + esc(title), name, lead,
                                                                  main_class="reading module-page local-course kr-theme kr-team")))
                kr_built.append(name)
        if lt:                                           # its parts, toolkit and workshop cards, under the course page in the breadcrumb
            ref = lambda rid: (chapters[rid][1], f"{rid}.html") if rid in chapters and rid in built_ids else None
            crumb = f'<a href="index.html">{T("site.name")}</a> › <a href="{code}.html">{esc(c["title"])}</a> › '
            for name, title, sub, lead in lumatutor.subpages(lt, lt_ws, lang, ref):
                ws_crumb = f'<a href="{lumatutor.section_of(lt, "suunnittele")["page"]}">{esc(lumatutor.section_of(lt, "suunnittele")["title"])}</a> › ' if name.startswith("lumatutor-tyopaja-") else ""
                (out / name).write_text(ahjo.kiviruukki_mark(page(title, sub, crumb + ws_crumb + esc(title), name, lead,
                                                                  main_class="reading module-page local-course kr-theme kr-team lt-course")))
                lt_built.append(name)
    # A unit of jaksot/ written as "pages" (scripts/jaksot.py, teacher 2026-11-12): its pages from jakso.json alone, in its
    # theme, and its row under the school's courses on the front page. No unit has them yet; Droonilab is planned.
    jk_built = []
    for jid in jaksot.ids():
        row = jaksot.front_row(jid, lang)
        if not row: continue
        jd = jaksot.load(jid, lang); theme = jd["jakso"]["theme"]
        cls = {"kiviruukki": "reading module-page local-course kr-theme kr-team", "ahjo": "reading ahjo-page"}.get(theme, "reading module-page local-course")
        mark = ahjo.kiviruukki_mark if theme == "kiviruukki" else ahjo.tab_icons if theme == "ahjo" else (lambda h: h)
        first = jd["pages"][0]
        for name, title, lead, sub in jaksot.pages(jid, lang):
            crumb = f'<a href="index.html">{T("site.name")}</a> › ' + ("" if name == first["file"] else f'<a href="{first["file"]}">{esc(jd["title"])}</a> › ')
            (out / name).write_text(mark(page(title, sub, crumb + esc(title), name, lead, main_class=cls)))
            jk_built.append(name)
        q = esc(row["text"])
        local_rows += (f'<li><a class="mod-row" href="{row["href"]}">{module_icons.img(row["icon"], 40)}'
                       f'<span class="mod-text"><span class="mod-name"><span class="mod-title">{esc(row["title"])}</span></span>'
                       f'<span class="mod-q" title="{q}">{q}</span></span><span class="mod-go" aria-hidden="true">→</span></a></li>')
    mixer_built = []                             # the YO-sekoitin (scripts/mixer.py): every language, when a local course asks for it
    mcode = next((code for code, c in local_courses.load().items() if c.get("mixer")), None)
    if mcode:
        crumb = f' › <a href="{mcode}.html">{mcode}</a>' if mcode in local else ""   # the course page only where this language has it
        (out / mixer.PAGE).write_text(page(T("mixer.title"), mixer.page_body(T, mixer.items(lang, T, list(practice_built), unit_pub)) + '<script src="invfilter.js"></script>',
                                           f'<a href="index.html">{T("site.name")}</a>{crumb} › {T("mixer.title")}', mixer.PAGE, T("mixer.description")))
        mixer_built.append(mixer.PAGE)
    local_notes = "".join(f'<p class="unavailable" id="unavailable-{code}" role="note" tabindex="-1">'
                          f'{T("site.local_unavailable_note", title=esc(code + " " + c["title"]))}</p>'
                          for code, c in local_courses.load().items() if code not in local)

    # The front page (teacher 2026-10-29, trimmed 2026-10-31, compacted 2026-11-03 "tiivistä etusivu": the whole page in
    # one desktop screen). The heading and one line under it, then the module list in two columns from 700 px: the
    # modules on the left; on the right Tulossa (dimmed) and the school's own courses under the school's name. The
    # study guide is a page of its own, nain-opiskelet.html (study_guide), linked from the header as "Näin opiskelet".
    school = next(iter(local.values()))["school"] if local else ""
    ahjo_data = ahjo.load(lang)
    # Ahjo 1 and Ahjo 2 are shown on the Ahjo page only, not in the front page's planned list (teacher 2026-11-08)
    plan_rows = "".join(planned_row(p) for p in ahjo.front_page_planned(local_courses.planned(lang), ahjo_data))
    home = (local_notes +
        # beside the heading a small badge: the site is still being built (teacher 2026-11-05, "leima että työn alla")
        f'<section class="home-intro" aria-labelledby="h-intro"><div class="intro-title"><h1 id="h-intro">{T("site.home_h1")}</h1>'
        f'<p class="wip-badge" title="{esc(T("site.home_wip_title"))}">{T("site.home_wip")}</p></div>'
        f'<p class="lead">{T("site.home_sub")}</p>'
        # from 700 px the school's logo stands here, over the right column, so that both lists start level (teacher
        # 2026-11-04); the list's own heading (the same logo) is then visually hidden, site.css .intro-school
        + (f'<img class="intro-school" src="brand/kiviruukin-lukio-rivi-musta.svg" alt="" width="293" height="32">' if local_rows else "")
        + '</section>' + resume_box() + '<script src="jatka.js"></script>'
        f'<section class="catalogue" id="moduulit" aria-labelledby="h-modules"><h2 id="h-modules" class="visually-hidden">{T("site.modules")}</h2>'
        f'<div class="mod-cols"><ul class="mod-list">{catalogue}</ul><div class="mod-side">'
        + (f'<h3 class="mod-group">{T("site.upcoming")}</h3><ul class="mod-list up-list">{upcoming}</ul>' if upcoming else "")
        # the school's own courses under the school's logo (teacher 2026-11-04: its emblem and name, the list level with the
        # national modules: from 700 px the logo sits above the column, out of the flow, site.css .mod-school)
        + (f'<h3 class="mod-group mod-school"><img src="brand/kiviruukin-lukio-rivi-musta.svg" alt="{esc(school)}" width="293" height="32"></h3>'
           f'<ul class="mod-list local-list">{local_rows}</ul>' if local_rows else "")
        # after a gap, the school's planned courses, greyed out and unlinked (teacher 2026-11-04: no content yet)
        # Ahjo Makerspace (teacher 2026-11-08): the school's makerspace, one row with its original logo before the planned courses
        + (f'<ul class="mod-list ahjo-list">{ahjo_row(ahjo_data, local_courses.planned(lang))}</ul>' if ahjo_data else "")
        + (f'<ul class="mod-list plan-list" aria-label="{esc(T("site.planned_courses"))}">{plan_rows}</ul>' if plan_rows else "")
        + '</div></div></section>')
    (out / "index.html").write_text(front_chrome(page(T("site.home_title"), home, "", "index.html", T("site.home_description"), main_class="home",
                                         full_title=f'{T("site.name")} — {T("site.subtitle")}')))
    # Käsitetakomo (teacher 2026-11-03, scripts/concept_cards.py): every module's cards, topics and the student's own deck
    if concept_cards.modules(concept_cards.data_lang(lang)):
        names = {c: course_text(c, curriculum[c])["title"] for c in concept_cards.modules(concept_cards.data_lang(lang))}
        (out / concept_cards.APP).write_text(page(T("cards.app_title"), concept_cards.app_page_body(T, lang, names, {k: v for c in names for k, v in chapter_titles(c).items()}),
                                             f'<a href="index.html">{T("site.name")}</a> › {T("cards.app_title")}', concept_cards.APP, T("cards.app_description"), main_class="reading kc-app-page"))
    # Lukuvinkit (teacher 2026-11-03, scripts/reading_tips.py): a reading list of physics books, linked from every header (not the footer, teacher 2026-11-04)
    rt = reading_tips.load(lang) if reading_tips.SOURCE.is_file() else None
    if rt: (out / reading_tips.PAGE).write_text(page(rt["title"], reading_tips.body(T, lang), f'<a href="index.html">{T("site.name")}</a> › {esc(rt["title"])}',
                                              reading_tips.PAGE, rt["description"], main_class="reading reading-tips"))
    # Vihkot (teacher 2026-11-07, scripts/booklets.py): the printable A5 books of the courses, linked from every header
    bk_titles = {c: course_text(c, curriculum[c])["title"] for c in curriculum if c.startswith("FY")}
    (out / booklets.PAGE).write_text(page(T("site.booklets"), booklets.body(T, lang, bk_titles, lambda c: module_icons.img(c, 40)),
                                          f'<a href="index.html">{T("site.name")}</a> › {esc(T("site.booklets"))}', booklets.PAGE,
                                          T("booklets.lead"), main_class="reading booklets-page"))
    # Näin opiskelet (teacher 2026-11-04, renewed 2026-11-08): the study guide alone, apart from the books of Kirjavinkit;
    # its header link says it is the page shown
    (out / STUDY_PAGE).write_text(page(T("guide.title"), study_guide(), f'<a href="index.html">{T("site.name")}</a> › {esc(T("site.study"))}',
                                       STUDY_PAGE, T("guide.description"), main_class="reading study-page")
                                  .replace('<a class="nav-study" href=', '<a class="nav-study" aria-current="page" href=', 1))
    # Sivustosta (teacher 2026-11-04): the teacher's own text, content/<lang>/tietoa.md (the Finnish where a language has
    # none). No page of the site links to the teacher's portfolio (teacher 2026-11-04: students should not find it)
    about_md = next((f for f in (ROOT / "content" / lang / "tietoa.md", ROOT / "content" / i18n.SOURCE / "tietoa.md") if f.is_file()), None)
    about_body = render_md(about_md.read_text()) if about_md else f'<h1>{T("site.about")}</h1><p class="lead">{T("site.about_lead")}</p>'
    # in Kiviruukin lukio's colours under the school's logo (teacher 2026-11-04, after his school pages; site.css .about-page)
    h1 = re.match(r"\s*(<h1>.*?</h1>)", about_body, re.S)
    hero = ('<header class="about-hero"><img class="about-logo" src="brand/kiviruukin-lukio-oikea-valkoinen.svg" alt="Kiviruukin lukio" width="175" height="100">'
            + (h1.group(1) if h1 else "") + '</header>')
    about_body = hero + (about_body[h1.end():] if h1 else about_body)
    (out / ABOUT).write_text(page(T("site.about"), f'<article class="about">{about_body}</article>',
                                  f'<a href="index.html">{T("site.name")}</a> › {T("site.about")}', ABOUT, T("site.about_lead"), main_class="reading about-page"))
    if FORMS and lang in SUBMISSION_LANGS:   # Palautukset (teacher 2026-11-06): where the chapters have the button
        (out / FORMS_PAGE).write_text(page(forms_title(), forms_page_body(), f'<a href="index.html">{T("site.name")}</a> › {esc(forms_title())}',
                                           FORMS_PAGE, T("site.returns_desc"), main_class="reading return-page"))
    teacher_built = False
    if grading_file():   # Työkalut (teacher 2026-11-08): the grading tool and the classroom screen, linked from the footers
        gf = grading_file()
        if lang == i18n.SOURCE:   # the tools once, beside the Finnish pages in their own folder; the other languages' pages link there (rebase)
            shutil.rmtree(out / "tyokalut", ignore_errors=True)
            if TOOLS.is_dir(): shutil.copytree(TOOLS, out / "tyokalut")
            (out / "tyokalut").mkdir(exist_ok=True); shutil.copyfile(gf, out / "tyokalut" / gf.name)
        (out / TEACHER_PAGE).write_text(page(T("teacher.title"), teacher_page_body(gf.name), f'<a href="index.html">{T("site.name")}</a> › {esc(T("teacher.title"))}',
                                             TEACHER_PAGE, T("teacher.desc"), main_class="reading teacher-page"))
        teacher_built = True
    # Ahjo Makerspace (teacher 2026-11-08, scripts/ahjo.py): its start page, resource bank and safety section in every language
    ahjo_built = []
    if ahjo_data:
        mod_titles = {k: course_text(k, curriculum[k])["title"] for k, _ in modules}
        lesson_titles = {lid: t for k, _ in modules for lid, t in chapter_titles(k).items()}
        def ahjo_ref(rid):
            if rid in built_ids: return lesson_titles[rid], "lesson", False
            if rid in guide_built: return guide_built[rid]["title"], "guide", False
            if rid in inv_built: return inv_built[rid]["title"], "investigation", False
            if lang != i18n.SOURCE and (OUTS[i18n.SOURCE] / f"{rid}.html").is_file():   # only the Finnish page: linked there, marked "in Finnish"
                fi_only = not lang.startswith("fi")
                if rid in guides.ids(): return guides.load(rid)["title"], "guide", fi_only
                if rid in investigations.ids(): return investigations.load(rid)["title"], "investigation", fi_only
                return next(l["title"] for k, m in curriculum.items() if not k.startswith("_") for l in m.get("lessons", []) if l["id"] == rid), "lesson", fi_only
            return None
        planned = local_courses.planned(lang)
        crumb = f'<a href="index.html">{T("site.name")}</a> › '
        home_crumb = crumb + f'<a href="{ahjo.PAGE}">{esc(ahjo_data["title"])}</a> › '
        u = ahjo_data["ui"]; pages = [
            (ahjo.PAGE, ahjo_data["title"], ahjo.start_body(ahjo_data, planned, local, mod_titles, ahjo_ref), crumb + esc(ahjo_data["title"]), ahjo_data["description"]),
            (ahjo.BANK, u["bank_h"], ahjo.bank_body(ahjo_data, planned, local, mod_titles, ahjo_ref), home_crumb + esc(u["bank_h"]), u["bank_page_lead"]),
            (ahjo.SAFETY, u["safety_page_title"], ahjo.safety_body(ahjo_data, lang, render_md), home_crumb + esc(u["safety_h"]), u["safety_page_lead"]),
            (ahjo.PROJECTS, u["projects_h"], ahjo.projects_body(ahjo_data, planned, local, mod_titles), home_crumb + esc(u["projects_h"]), u["projects_page_lead"])]
        for c in ahjo_data["courses"]:            # Ahjo 1 and Ahjo 2 each on its own page (teacher 2026-11-08)
            ct = ahjo.course_info(c["code"], planned, local)[0]
            pages.append((ahjo.course_page(c["code"]), f'{ct}: {c["subtitle"]}', ahjo.course_body(ahjo_data, c, planned, local, mod_titles, ahjo_ref),
                          home_crumb + esc(ct), c["subtitle"]))
            for i, l in enumerate(c.get("lessons", []), 1):   # every lesson its own working view (teacher 2026-11-09)
                lt = l.get("make") or l["title"]
                pages.append((ahjo.lesson_page(c["code"], i), f'{ct}, {u["lesson_n"].replace("{n}", str(i))}: {lt}',
                              ahjo.lesson_body(ahjo_data, c, i, planned, local, ahjo_ref),
                              home_crumb + f'<a href="{ahjo.course_page(c["code"])}">{esc(ct)}</a> › ' + esc(u["lesson_n"].replace("{n}", str(i))), l["text"]))
        for g in ahjo.ready_guides(ahjo_data):   # an Ahjo guide the teacher marked ready: its own page under the bank
            r = next(r for r in ahjo_data["resources"] if r.get("id") == g)
            pages.append((f"{g}.html", r["title"], ahjo.guide_body(ahjo_data, g, lang, render_md),
                          home_crumb + f'<a href="{ahjo.BANK}">{esc(u["bank_h"])}</a> › ' + esc(r["title"]), r["text"]))
        for name, title, body, crumbs, desc in pages:
            (out / name).write_text(ahjo.tab_icons(page(title, body, crumbs, name, desc, main_class="reading ahjo-page")))
            ahjo_built.append(name)
    # Tietosuoja (teacher 2026-11-04): content/<lang>/tietosuoja.md (the Finnish where a language has none), linked from every footer
    priv_md = next((f for f in (ROOT / "content" / lang / "tietosuoja.md", ROOT / "content" / i18n.SOURCE / "tietosuoja.md") if f.is_file()), None)
    if priv_md:
        (out / PRIVACY).write_text(page(T("site.privacy"), f'<article class="privacy">{render_md(priv_md.read_text())}</article>',
                                        f'<a href="index.html">{T("site.name")}</a> › {T("site.privacy")}', PRIVACY, T("site.privacy_lead"), main_class="reading privacy-page"))
    if SITE.name == "site.tmp":                  # a lesson leaves the live site only with a warning (an annotation on CI)
        live = LIVE / out.relative_to(SITE)
        for old_page in sorted(live.glob("*.html")):
            lid = old_page.stem
            if lid in states and lid not in built_ids:
                why = ", ".join(f"{n}={v}" for n, v in states[lid]["reports"].items() if v != "missing") or "no reports"
                removed.append(lid if lang == i18n.SOURCE else f"{lang}/{lid}")
                print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING:'} {old_page.relative_to(LIVE)} is on the live site but its reviews are not current ({why}); this build removes it")
    pre = out.relative_to(SITE).as_posix() + "/" if out != SITE else ""
    expected.extend(pre + n for n in ["index.html", ABOUT] + ([PRIVACY] if priv_md else []) + ([TEACHER_PAGE] if teacher_built else []) + ([concept_cards.APP] if concept_cards.modules(concept_cards.data_lang(lang)) else []) + ([reading_tips.PAGE] if reading_tips.SOURCE.is_file() else []) + [booklets.PAGE, STUDY_PAGE] + ahjo_built + kr_built + lt_built + jk_built + [f"{c}.html" for c, _ in modules] + [f"{c}.html" for c in local] + [f"{i}.html" for i in built_ids] + [f"{i}.html" for i in inv_built] + [f"{g}.html" for g in guide_built] + [practice.page_name(c) for c in practice_built] + [practice.page_name(c + practice.EXAM) for c in exam_built] + mixer_built
                    + [f"{u}.html" for u, ls in unit_pub.items() if lang in ls and not only])
    if SITE.name == "site.tmp" and lang in units.languages():   # a unit that lost its reviews leaves the site only with a warning
        for u in units.ids(lang):
            if lang not in unit_pub.get(u, ()) and (LIVE / out.relative_to(SITE) / f"{u}.html").is_file():
                print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING:'} {u}.html is on the live site but its reviews are not current; this build removes it")
    print(f"built {pre or ''}index +", len(modules), "module pages ->", ((LIVE if SITE.name == "site.tmp" else SITE) / pre).relative_to(ROOT),
          f"({sum(m['state'] == 'reviewed' for ms in built.values() for m in ms)} reviewed, {len(legacy_ids)} legacy, "
          f"{sum(m['state'] == 'draft' for ms in built.values() for m in ms)} draft" + (f", {len(removed)} removed: {', '.join(removed)}" if removed else "") + ")")


if concept_cards.errors(): sys.exit("\n".join(["ERROR: concept cards (scripts/concept_cards.py):"] + concept_cards.errors()))
LANGS = i18n.languages()                          # fi at site/, every other language at site/<lang>/
OUTS = {lang: SITE if lang == i18n.SOURCE else SITE / lang for lang in LANGS}
for lang in LANGS: build_language(lang)
link_languages()
i18n.set_lang(i18n.SOURCE)
# Cache busting (teacher 2026-11-03: a page fetched just after a deploy showed new HTML with yesterday's cached site.css):
# every link to a shared stylesheet or script carries ?v=<first 8 hex of its SHA-256>, so a changed file is a new URL.
SHARED = ("site.css", "lesson.js", "sim-embed.js", "inquiry.js", "selfassess.js", "investigation.js", "invfilter.js", "padstore.js", "palautus.js", "readaloud.js", "kortit.js", "tehty.js", "omaarvio.js", "jatka.js", "ahjo.js", "lumatutor.js")
_ver = {f: hashlib.sha256((SITE / f).read_bytes()).hexdigest()[:8] for f in SHARED if (SITE / f).is_file()}
_ref = re.compile(r'((?:href|src)="(?:\.\./)*)(' + "|".join(re.escape(f) for f in _ver) + r')(?:\?v=[0-9a-f]*)?"')
for _page in SITE.rglob("*.html"):
    if "vendor" in _page.relative_to(SITE).parts: continue
    _old = _page.read_text(); _new = _ref.sub(lambda m: f'{m[1]}{m[2]}?v={_ver[m[2]]}"', _old)
    if "<table" in _new: _new = tablefit.fit(_new, re.search(r'<html[^>]*\blang="fi\b', _new[:400]) is not None)   # no table scrolls sideways (2026-11-08)
    if 'class="ch-box"' in _new: _new = tablefit.cards(_new, re.search(r'<html[^>]*\blang="fi\b', _new[:400]) is not None)   # a card's very long word breaks at a syllable (2026-11-11)
    if _new != _old: _page.write_text(_new)
if SITE.name == "site.tmp":                      # check the render, then swap it in; the old site comes back if the swap fails
    expected += ["site.css", "lesson.js", "sim-embed.js", "inquiry.js", "selfassess.js", "investigation.js", "invfilter.js", "padstore.js", "palautus.js", "readaloud.js", "kortit.js", "tehty.js", "omaarvio.js", "jatka.js", "ahjo.js", "lumatutor.js"] + card_files + assets
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
