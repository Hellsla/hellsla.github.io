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
import answers_shown, cardgrid, concept_cards, courses, fbdspec, figcat, guides, i18n, inquiry, investigations, local_courses, mathlayout, mixer, module_icons, practice, reading_tips, svgids, units
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
for f in ("site.css", "lesson.js", "sim-embed.js", "inquiry.js", "selfassess.js", "investigation.js", "invfilter.js", "padstore.js", "readaloud.js", "kortit.js"): shutil.copy(TPL / f, SITE / f)
card_files = concept_cards.publish(SITE)   # site/kortit/<module>.json, read by Käsitetakomo (scripts/concept_cards.py)
shutil.copytree(TPL / "vendor", SITE / "vendor", dirs_exist_ok=True)   # p5 + KaTeX, no CDN needed
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


def render_md(text, **kw):
    """Markdown -> HTML, with LaTeX kept out of markdown's reach, force-diagram specs drawn (scripts/fbdspec.py) and
    figures embedded by id (`<svg data-fig="fy5-2/lauta-voimat"></svg>`, figcat.embed) drawn in the page's language.
    ```latex fences become $$...$$; every $$...$$ and $...$ is swapped for a token first,
    so underscores, backslashes and asterisks inside maths are not read as markdown."""
    text = re.sub(r"```latex\n(.*?)```", lambda m: "\n$$" + m.group(1).strip() + "$$\n", text, flags=re.S)
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
        return (f'<figure class="unit-photo{wide}"><img src="{ref}"{attrs} width="{c["width"]}" height="{c["height"]}" loading="lazy" decoding="async">'
                f'<figcaption>{cap} <span class="photo-credit">{T("lesson.photo_by")}: {esc(c["creator"])}, {esc(c["licence"])}</span></figcaption></figure>')
    html = PHOTO.sub(one, html)
    if not used: return html, ""
    items = "".join(f'<li><strong>{esc(c["title"])}</strong>. {esc(c["creator"])}. '
                    + f'<a href="{esc(c["source"])}">{T("units.credit_source")}</a>, '
                    + (f'<a href="{esc(c["licence_url"])}">{esc(c["licence"])}</a>' if c.get("licence_url") else esc(c["licence"]))
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
        return f.replace("\\", "")
    return re.sub(r"\$([^$]+)\$", one, s)


def texts(html):
    """{{t:site.footer}} in a template -> the text in the language being built (lang/<lang>.json)."""
    return re.sub(r"\{\{t:([\w.]+)\}\}", lambda m: esc(T(m.group(1))), html)


# Modules the front page still lists dimmed under Tulossa although some of their chapters are published (teacher
# 2026-11-03, "tiivistä etusivu": FY6–FY8 stay there until the teacher moves them; curriculum.json "_front_page").
HOME_COMING = tuple(curriculum.get("_front_page", {}).get("coming", []))


def home_row(code, title, question, coming=False):
    """A front page row: one link over the whole row with the module's icon, code, title and Miksi question; the arrow
    appears on hover and focus only. The question is cut to one line in two columns, so it is whole in title too."""
    q = esc(question)
    return (f'<li><a class="mod-row{" coming" if coming else ""}" href="{code}.html">{module_icons.img(code, 40)}'
            f'<span class="mod-text"><span class="mod-name"><span class="mod-code">{code}</span> <span class="mod-title">{esc(title)}</span></span>'
            f'<span class="mod-q" title="{q}">{q}</span></span><span class="mod-go" aria-hidden="true">→</span></a></li>')


ABOUT = "tietoa.html"


def front_chrome(html):
    """The front page's own header and footer (teacher 2026-11-03): Näin opiskelet beside Moduulit and Lukuvinkit, and
    in the footer Tietoa sivustosta in place of the portfolio link, which is on that page now."""
    html = html.replace('<a class="nav-reading"', f'<a class="nav-study" href="{reading_tips.PAGE}#{STUDY_ID}">{esc(T("site.study"))}</a><a class="nav-reading"', 1)
    return re.sub(r'(<footer class="bottom">.*?)<a href="[^"]*">[^<]*</a></footer>', lambda m: m.group(1) + f'<a href="{ABOUT}">{esc(T("site.about"))}</a></footer>', html, count=1, flags=re.S)


STUDY_ID = "nain-opiskelet"


def study_guide():
    """Näin opiskelet Ruukkilabrassa (moved from the front page to the top of Lukuvinkit, teacher 2026-11-03): the six
    stages with the names the lessons use (lang inquiry.stage_*), where to start, more tips behind a disclosure."""
    stages = "".join(f'<li><strong>{T("inquiry.stage_" + k)}</strong><span>{T("site.home_path_" + k)}</span></li>' for k in inquiry.STAGE_IDS)
    return (f'<section class="path" id="{STUDY_ID}" aria-labelledby="h-path"><h2 id="h-path">{T("site.home_path")}</h2>'
            f'<p class="section-lead">{T("site.home_start_lead")}</p><ol class="path-steps">{stages}</ol>'
            f'<details class="more-tips"><summary>{T("site.home_start_more")}</summary><ul>'
            + "".join(f"<li>{esc(x)}</li>" for x in T("site.home_start_items")) + '</ul></details></section>')


def page(title, body, crumbs, name, description, main_class="reading", full_title=None):
    """A front or module page. Its <title> is "<title> — Ruukkilabra"; the front page passes full_title instead, so
    the site's name is not said twice."""
    head = full_title or f"{title} — {T('site.name')}"
    tpl_ = page_tpl
    if re.search(r"\$[^$\s][^$]*\$", body):   # a chapter title with a formula (curriculum.json "$pV = nRT$"): the lesson pages' KaTeX
        tpl_ = (tpl_.replace('<link rel="stylesheet" href="site.css">', '<link rel="stylesheet" href="vendor/katex/katex.min.css">\n<link rel="stylesheet" href="site.css">', 1)
                .replace("</body>", '<script src="vendor/katex/katex.min.js"></script><script src="vendor/katex/contrib/auto-render.min.js" '
                         'onload="renderMathInElement(document.querySelector(\'main\'),{delimiters:[{left:\'$\',right:\'$\',display:false}],throwOnError:false})"></script>\n</body>', 1))
    return rebase(texts(tpl_).replace("{{head_title}}", esc(head)).replace("{{title}}", esc(title)).replace("{{body}}", body).replace("{{crumbs}}", crumbs)
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
    return inquiry.choice_html({"prompt": e.get("prompt") or T("lesson.choose"), "choices": e["choices"]}, md, lid, e["id"])


def exercise_html(e, solution_html, read=None, core=False):
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
        st = answers_shown.step(ans.strip("$"), e["answer"]) if ans.startswith("$") else None   # ±1 in the shown answer's last digit
        check = (f'<form class="check" data-answer="{e["answer"]}" data-tol="{e.get("tolerance", 0.02)}"' + (f' data-step="{st:g}"' if st else "") + ' novalidate>'
                 f'<input type="text" inputmode="decimal" autocomplete="off" enterkeyhint="done" aria-label="{esc(inquiry.answer_label(e.get("unit", "")))}" aria-describedby="{esc(e["id"])}-q" placeholder="?">'
                 + (f'<span class="unit">{unit}</span>' if unit else "")
                 + f'<button type="submit">{T("lesson.check")}</button><output aria-live="polite"></output></form>')
    model = figcat.figure_html(e["model_figure"], T.lang, read) if e.get("model_figure") else ""   # a drawing task's model diagram, inside the solution
    sol = f'<details class="solution"><summary>{T("lesson.solution")}</summary>{model}<div class="steps">{solution_html}</div></details>' if solution_html else ""
    fig = figcat.figure_html(e["figure"], T.lang, read) if e.get("figure") else ""   # a figure by its id (scripts/figcat.py)
    fig = (data_table(e["data"]) if e.get("data") else "") + fig + (exercise_choice(e) if e.get("choices") else "")
    tag = f'<span class="ex-core">{T("lesson.core_exercise")}</span>' if core else ""
    solved = "" if numeric else f'<label class="solved"><input type="checkbox"> <span>{T("inquiry.did_solution")}</span></label>'   # a written task opens its answer after this tick (lesson.js part 8)
    return (f'<li id="{e["id"]}"{" class=" + chr(34) + "core" + chr(34) if core else ""}>{tag}{inquiry.task_text(nbsp_units(e["text"]), pid=f"{e['id']}-q")}{fig}{check}{solved}'
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
    Every page passes here, so here a figure shown twice gets its own definition ids (svgids.py, teacher 2026-10-29)."""
    html = svgids.namespace(html)
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
                            guide = (tuple(local_courses.load()) if name.startswith("tvt-") else ())   # a TVT-ohje: its course's note
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
            f.write_text(re.sub(r"<!--fl-languages:([\w.-]+)-->", control, f.read_text()))


def chapter_card(html):
    """What a chapter's card on its module page shows (teacher 2026-11-03, "Ruukkikortit"): the chapter's own opening
    illustration and its Miksi question, taken from the built page, so nothing is written twice (scripts/cardgrid.py)."""
    q = re.search(r'<div class="intro-head">.*?<blockquote>\s*<p>(.*?)</p>', html, re.S)
    why = re.sub(r"</?strong>", "", q.group(1)).strip() if q else ""
    return cardgrid.hero(html), why


def chapter_cards(code, mod, slots, built_ids, legacy_ids, cards):
    """The module page's chapters as cards, under the module's themes (curriculum.json "themes": [{title, first}],
    titles translated in content/<lang>/courses.json "themes"); a chapter still coming is a plain row without a link.
    One continuous grid (teacher 2026-11-04): a theme's name is a label above its first card, so the next theme's cards
    go on in the same row and a short theme leaves no hole beside it (scripts/cardgrid.py)."""
    themes = {th["first"]: th["title"] for th in mod.get("themes", [])}
    if themes and slots[0]["id"] not in themes: sys.exit(f"{code}: the first theme must start at the first chapter {slots[0]['id']}")
    bad = set(themes) - {l["id"] for l in slots}
    if bad: sys.exit(f"{code}: themes start at unknown chapters {sorted(bad)} (curriculum.json)")
    items = ""
    for i, l in enumerate(slots, 1):
        lab = cardgrid.label(esc(themes[l["id"]])) if l["id"] in themes else ""
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


def chapter_nav(out, modules, built_ids, practice_built):
    """Edellinen luku / Seuraava luku under every lesson and Sovella page of this language (teacher 2026-10-29). The
    order is the module's lesson order in curriculum.json (the teaching order: FY3 is not numeric), only published
    pages are linked, the first chapter leads back to the module page, the last to Sovella itsenäisesti when it is
    published (else the module page), and the Sovella page back to the last chapter. Links stay in this language's
    folder, so the language is kept; new chapters join the sequence when they are published."""
    if only:                                       # a preview links the lessons a full build would publish, and itself
        built_ids = built_ids | {f.name for f in courses.lessons(lang=T.lang) if review_status(f)["state"] != "draft"}
    def link(cls, rel, href, direction, name):
        return (f'<a class="{cls}" href="{href}"{f" rel={chr(34)}{rel}{chr(34)}" if rel else ""}>'
                f'<span class="dir">{direction}</span><span class="name">{esc(name)}</span></a>')
    for code, mod in modules:
        seq = [(l["id"] + ".html", l["title"]) for l in mod.get("lessons", []) if l["id"] in built_ids]
        if code in practice_built: seq.append((practice.page_name(code), T("practice.title")))
        course = (f"{code}.html", T("lesson.chapter_course", course=code))
        for i, (name, _) in enumerate(seq):
            f = out / name
            if not f.is_file(): continue
            prev = seq[i - 1] if i else None; nxt = seq[i + 1] if i + 1 < len(seq) else None
            nav = (f'<nav class="chapter-nav" aria-label="{esc(T("lesson.chapter_nav"))}">'
                   + (link("prev", "prev", prev[0], T("lesson.chapter_prev"), prev[1]) if prev else link("prev up", "", course[0], T("lesson.chapter_up"), course[1]))
                   + (link("next", "next", nxt[0], T("lesson.chapter_next"), nxt[1]) if nxt else link("next up", "", course[0], T("lesson.chapter_up"), course[1]))
                   + "</nav>")
            f.write_text(f.read_text().replace(f"<!--fl-chapter-nav:{name[:-5]}-->", nav))


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
    """The course units written in this language (scripts/units.py): each page in the lesson template with the
    inquiry stages, the course's components (units/<course>/units.js and units.css), its simulation, its credits,
    sources and teacher notes, and Previous / Next unit in the course's order. A draft is built only as a preview."""
    published = {f"{u}.html" for u, ul in unit_pub.items() if ul == lang}
    for uid in units.ids(lang):
        if only and only != uid: continue
        if uid not in unit_pub: continue
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
            tasks_html, _ = practice.render(units.task_key(uid), lang, md, solution_html, T("practice.title"), embedded=True)
        body, toc = inquiry.render(f, inq, {"intro": intro, "sections": sections, "sim": sim, "exercises": tasks_html, "exit": exit_html}, md)
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
        notice_html = "" if st["state"] == "reviewed" else f'<p class="notice" role="note">{T("units.notice_draft")}</p>'
        html = (texts(tpl).replace("{{title}}", esc(d["title"])).replace("{{course}}", code).replace("{{notice}}", notice_html)
                .replace("{{strings}}", block + head).replace("{{back_to_course}}", esc(T("site.back_to_course", course=code)))
                .replace("{{toc}}", toc).replace("{{main}}", f'<article id="teoria" class="inquiry unit unit-{d["kind"]}" data-course="{code.lower()}">{body}{tail}</article>' + units.course_nav(uid, lang, T, published) + embedded)
                .replace("{{scripts}}", f'<script src="inquiry.js"></script>' + ('<script src="selfassess.js"></script>' if tasks_html else "")
                         + (f'<script src="units/{code.lower()}/units.js"></script>' if cdir.is_dir() else ""))
                .replace("{{description}}", esc(d["description"])).replace("{{url}}", URL + f"{uid}.html")
                .replace("{{home}}", HOME).replace("{{languages}}", ""))
        (out / f"{uid}.html").write_text(rebase(html))
        print("built", uid, f"({st['state']})")


def build_language(lang):
    """Every lesson, course page and the front page of one language into OUTS[lang]."""
    global UP, HOME, URL, COURSES
    i18n.set_lang(lang); out = OUTS[lang]; out.mkdir(exist_ok=True)
    UP = "" if lang == i18n.SOURCE else "../"; HOME = UP + "../../index.html"; URL = BASE_URL + ("" if lang == i18n.SOURCE else f"{lang}/")
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
        for lvl, items in ex.items():
            ex_html += (f"<details class=\"level\"><summary>{T('lesson.level', n=lvl[-1])} · {T('lesson.level_kind_' + lvl[-1])} "
                        f"<span class=\"count\">{T.count('lesson.level_count', len(items))}</span></summary><p class=\"level-lead\">{T('lesson.level_lead_' + lvl[-1])}</p><ol>")
            for i, e in enumerate(items):
                show = publish == "all" or (publish == "first" and i == 0)
                ex_html += exercise_html(e, solutions.get(e["id"]) if show else None, None if isinstance(ex_src, WorkTree) else ex_src.read, core=e["id"] in core)
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
        kc_section = concept_cards.lesson_section(meta["course"], meta["id"], T, lang, titles)   # "Kertaa luvun käsitteet" after the exit ticket (teacher 2026-11-03)
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
                    f'<section id="exercises"><h2>{inquiry.exercises_title()}</h2>{ex_html}</section>{photo_tail}')
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
                     "cards_nav": concept_cards.lesson_nav(T) if kc_section else ""}
            body, toc = inquiry.render(folder, inq, parts, lambda t: nbsp_units(render_md(t)))
            if kc_section:   # bold terms of Teoriatiivistelmä that name a card open it (never before that stage)
                body = re.sub(r'<section class="stage" id="selita".*?</section>', lambda m: concept_cards.mark_terms(m.group(0), meta["course"], lang), body, count=1, flags=re.S)
            body, photo_tail = photos(body)               # a photograph may also open a task (FY4 2026-11-03: Pohdinta)
            main = f'<article id="teoria" class="inquiry">{body}{photo_tail}</article>'
        skey = (meta["id"] if where[0] == "lesson" else where[1].name) if where else None   # the sim's block of lang "sims"
        html = (texts(tpl).replace("<title>{{title}}", "<title>" + esc(plain_tex(meta["title"]))).replace('og:title" content="{{title}}', 'og:title" content="' + esc(plain_tex(meta["title"])))
                .replace("{{title}}", esc(meta["title"])).replace("{{course}}", meta["course"]).replace("{{notice}}", notice(meta["state"]))
                .replace("{{strings}}", strings_block(skey)).replace("{{back_to_course}}", esc(T("site.back_to_course", course=meta["course"])))
                .replace("{{toc}}", toc).replace("{{main}}", main + f"<!--fl-chapter-nav:{meta['id']}-->")
                .replace("{{scripts}}", '<script src="inquiry.js"></script>' if inq else "")
                .replace("{{description}}", esc(description_of(meta, lesson_md))).replace("{{url}}", URL + name)
                .replace("{{home}}", HOME).replace("{{languages}}", languages_nav(name)))
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
                .replace("{{home}}", HOME).replace("{{languages}}", languages_nav(pname)))
        (out / pname).write_text(rebase(html))
        tasks = practice.load(code, lang)["tasks"]
        practice_built[code] = T("practice.course_count", tasks=T.count("practice.tasks_n", len(tasks)),
                                                points=T.count("practice.task_points", sum(practice.total(t) for t in tasks if t.get("kind") != "own")))
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
        notes = "".join(f'<p class="unavailable" id="unavailable-{lid}" role="note" tabindex="-1">{T("site.unavailable_note", title=esc(title))}</p>'
                        for lid, title in missing)
        goals = "".join(f"<li>{esc(g)}</li>" for g in mod.get("tavoitteet", []))
        body = (notes + f'<div class="mod-head">{module_icons.img(code, 56, "mod-head-icon")}<div><span class="eyebrow">{code} · {credits}</span><h1>{esc(mod["title"])}</h1></div></div>'
                f'<p class="lead">{esc(T("site.module_question." + code))}</p>'
                f'<p class="mod-status">{main_label}{(" · " + extra_label) if extra_label else ""}</p>'
                + f'<h2>{T("site.course_lessons")}</h2>{items}<div class="mod-more">'
                + (f'<section><h2>{T("practice.title")}</h2><p>{T("practice.course_lead")}</p><ul class="lessons practice-link"><li class="live">'
                   f'<a href="{practice.page_name(code)}">{T("practice.title")}</a> <span class="count">{practice_built[code]}</span></li></ul></section>' if code in practice_built else "")
                + concept_cards.module_section(code, T, lang, chapter_titles(code, built_ids))   # Kertauspakkasi: the student's deck of the module (teacher 2026-11-03)
                + (f'<section><h2>{T("site.course_goals")}</h2><details class="goals"><summary>{T.count("site.course_goals_show", len(mod.get("tavoitteet", [])))}</summary>'
                   f'<p>{T("site.course_goals_lead")}</p><ul>{goals}</ul></details></section>' if goals else "") + "</div>")
        desc = T("site.course_description", code=code, title=mod["title"], done=done, n=len(slots))
        (out / f"{code}.html").write_text(page(T("site.course_title", code=code, title=mod["title"]), body,
                                                f'<a href="index.html">{T("site.name")}</a> › {code}', f"{code}.html", desc, main_class="reading module-page"))

    chapter_nav(out, modules, built_ids, practice_built)

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
                .replace("{{home}}", HOME).replace("{{languages}}", languages_nav(f"{gid}.html")))
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
                .replace("{{home}}", HOME).replace("{{languages}}", languages_nav(f"{iid}.html")))
        (out / f"{iid}.html").write_text(rebase(html)); inv_built[iid] = d
        print("built", iid, f"({st['state']})")
    # Course units (teacher's brief 2026-11-01, FY14; scripts/units.py): the lessons of a local course written in its
    # own language, published only in that language's folder when all three reviews pass. Every language's course
    # page links to them there, so which units are published is decided from their reviews, not from built files.
    unit_pub = {u: ul for ul, u in units.all_units() if units.status(u, ul)["state"] == "reviewed" or build_all or only == u}
    if lang in units.languages(): build_units(lang, out, unit_pub)
    local = local_courses.load(lang)
    local_rows = ""
    for code, c in local.items():
        cu = [(u, units.load(u, ul), os.path.relpath(OUTS[ul] / f"{u}.html", out).replace(os.sep, "/")) for u, ul in unit_pub.items() if units.load(u, ul)["course"] == code]
        local_rows += home_row(code, c["title"], c["subtitle"])
        (out / f"{code}.html").write_text(page(f"{code} {c['title']}", local_courses.page_body(code, c, T, chapters, {f"{i}.html" for i in built_ids},
                                                                                                  [(i, d) for i, d in inv_built.items() if code in d["courses"]],
                                                                                                  guides.course_section(T, published, lang) if code == "FY10" else "", cu)
                                                + '<script src="invfilter.js"></script>',
                                                f'<a href="index.html">{T("site.name")}</a> › {code}', f"{code}.html", c["description"], main_class="reading module-page local-course"))
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
    # study guide is on the Lukuvinkit page (study_guide), linked from the header as "Näin opiskelet".
    school = next(iter(local.values()))["school"] if local else ""
    home = (local_notes +
        f'<section class="home-intro" aria-labelledby="h-intro"><h1 id="h-intro">{T("site.home_h1")}</h1>'
        f'<p class="lead">{T("site.home_sub")}</p></section>'
        f'<section class="catalogue" id="moduulit" aria-labelledby="h-modules"><h2 id="h-modules" class="visually-hidden">{T("site.modules")}</h2>'
        f'<div class="mod-cols"><ul class="mod-list">{catalogue}</ul><div class="mod-side">'
        + (f'<h3 class="mod-group">{T("site.upcoming")}</h3><ul class="mod-list up-list">{upcoming}</ul>' if upcoming else "")
        + (f'<h3 class="mod-group">{esc(school)}</h3><ul class="mod-list local-list">{local_rows}</ul>' if local_rows else "")
        + '</div></div></section>')
    (out / "index.html").write_text(front_chrome(page(T("site.home_title"), home, "", "index.html", T("site.home_description"), main_class="home",
                                         full_title=f'{T("site.name")} — {T("site.subtitle")}')))
    # Käsitetakomo (teacher 2026-11-03, scripts/concept_cards.py): every module's cards, topics and the student's own deck
    if concept_cards.modules(concept_cards.data_lang(lang)):
        names = {c: course_text(c, curriculum[c])["title"] for c in concept_cards.modules(concept_cards.data_lang(lang))}
        (out / concept_cards.APP).write_text(page(T("cards.app_title"), concept_cards.app_page_body(T, lang, names, {k: v for c in names for k, v in chapter_titles(c).items()}),
                                             f'<a href="index.html">{T("site.name")}</a> › {T("cards.app_title")}', concept_cards.APP, T("cards.app_description"), main_class="reading kc-app-page"))
    # Lukuvinkit (teacher 2026-11-03, scripts/reading_tips.py): a reading list of physics books, linked from every header and footer
    rt = reading_tips.load(lang) if reading_tips.SOURCE.is_file() else None
    if rt: (out / reading_tips.PAGE).write_text(page(rt["title"], study_guide() + reading_tips.body(T, lang), f'<a href="index.html">{T("site.name")}</a> › {esc(rt["title"])}',
                                              reading_tips.PAGE, rt["description"], main_class="reading reading-tips"))
    # Tietoa sivustosta (teacher 2026-11-03): a page to fill later; the link back to the portfolio moved here from the front page
    (out / ABOUT).write_text(page(T("site.about"), f'<h1>{T("site.about")}</h1><p class="lead">{T("site.about_lead")}</p>'
                                  f'<p><a href="{HOME}">{T("site.back_to_portfolio")}</a></p>',
                                  f'<a href="index.html">{T("site.name")}</a> › {T("site.about")}', ABOUT, T("site.about_lead")))
    if SITE.name == "site.tmp":                  # a lesson leaves the live site only with a warning (an annotation on CI)
        live = LIVE / out.relative_to(SITE)
        for old_page in sorted(live.glob("*.html")):
            lid = old_page.stem
            if lid in states and lid not in built_ids:
                why = ", ".join(f"{n}={v}" for n, v in states[lid]["reports"].items() if v != "missing") or "no reports"
                removed.append(lid if lang == i18n.SOURCE else f"{lang}/{lid}")
                print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING:'} {old_page.relative_to(LIVE)} is on the live site but its reviews are not current ({why}); this build removes it")
    pre = out.relative_to(SITE).as_posix() + "/" if out != SITE else ""
    expected.extend(pre + n for n in ["index.html", ABOUT] + ([concept_cards.APP] if concept_cards.modules(concept_cards.data_lang(lang)) else []) + ([reading_tips.PAGE] if reading_tips.SOURCE.is_file() else []) + [f"{c}.html" for c, _ in modules] + [f"{c}.html" for c in local] + [f"{i}.html" for i in built_ids] + [f"{i}.html" for i in inv_built] + [f"{g}.html" for g in guide_built] + [practice.page_name(c) for c in practice_built] + mixer_built
                    + [f"{u}.html" for u, ul in unit_pub.items() if ul == lang and not only])
    if SITE.name == "site.tmp" and lang in units.languages():   # a unit that lost its reviews leaves the site only with a warning
        for u in units.ids(lang):
            if u not in unit_pub and (LIVE / out.relative_to(SITE) / f"{u}.html").is_file():
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
SHARED = ("site.css", "lesson.js", "sim-embed.js", "inquiry.js", "selfassess.js", "investigation.js", "invfilter.js", "padstore.js", "readaloud.js", "kortit.js")
_ver = {f: hashlib.sha256((SITE / f).read_bytes()).hexdigest()[:8] for f in SHARED if (SITE / f).is_file()}
_ref = re.compile(r'((?:href|src)="(?:\.\./)*)(' + "|".join(re.escape(f) for f in _ver) + r')(?:\?v=[0-9a-f]*)?"')
for _page in SITE.rglob("*.html"):
    if "vendor" in _page.relative_to(SITE).parts: continue
    _old = _page.read_text(); _new = _ref.sub(lambda m: f'{m[1]}{m[2]}?v={_ver[m[2]]}"', _old)
    if _new != _old: _page.write_text(_new)
if SITE.name == "site.tmp":                      # check the render, then swap it in; the old site comes back if the swap fails
    expected += ["site.css", "lesson.js", "sim-embed.js", "inquiry.js", "selfassess.js", "investigation.js", "invfilter.js", "padstore.js", "readaloud.js", "kortit.js"] + card_files + assets
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
