"""Render content/ folders into site/. Usage: python scripts/build.py [lesson-id | --all]

Without an argument only lessons whose reviews are current are built (scripts/reviews.py: state reviewed, or
legacy for a prototype lesson kept visible by the teacher), into site/ (committed, served by GitHub Pages).
With a lesson id that lesson is built regardless of its state into the git-ignored preview/; with --all every
lesson is (CI uses this to test drafts too). So a draft can never end up in the published folder.
The plain build renders into site.tmp/, checks that every expected page is there and swaps it in only then,
so a failed build never leaves site/ incomplete. A lesson that is on the live site but whose reviews are no
longer current is left out with a WARNING (an annotation on CI), never silently.

Page anatomy (human decisions 2026-10-25 and 2026-10-26, CLAUDE.md "Lesson page"): the worked example is shown in
stages split by `<!-- vaihe -->` lines (staged_example); the formula section `## Kaava: <law>` is headed by the
law's name (named_sections); a figure sits beside the paragraph it explains on a wide screen (fig_rows). Each
exercise gets a browser-side answer check and, depending on meta.solutions ("first" by default, "all", "none"),
its worked solution from solutions.md; the exercises close the page, after the exit ticket.
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
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from reviews import status as review_status
import courses, inquiry

ROOT = pathlib.Path(os.environ.get("FYSIIKKALABRA_ROOT") or pathlib.Path(__file__).resolve().parents[1])   # tests build a copy
HOME = "../../index.html"                      # the portfolio front page, two levels above site/
BASE_URL = "https://hellsla.github.io/fysiikkalabra/site/"
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
for f in ("site.css", "lesson.js", "sim-embed.js", "inquiry.js"): shutil.copy(TPL / f, SITE / f)
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
        maths.append(m.group(0)); return f"MATHTOKEN{len(maths) - 1}X"
    text = re.sub(r"\$\$.*?\$\$|\$[^$\n]+?\$", stash, text, flags=re.S)
    html = markdown.markdown(text, extensions=["fenced_code", "tables"] + kw.get("extensions", []))
    return re.sub(r"MATHTOKEN(\d+)X", lambda m: maths[int(m.group(1))], html)


UNIT = r"(?:N/kg|m/s²|m/s|km/h|kPa|MPa|Pa|°C|K|kN|N|kg|g|km|cm²|cm|mm|m³|m|s|min|h|kJ|J|kW|W|dm³|l|Hz|%)"


def nbsp_units(text):
    """A non-breaking space between a number and its unit in page text, so '9,81 m/s²' never breaks at the
    line end on a phone. Maths is stashed first, so LaTeX spacing is untouched."""
    maths = []
    def stash(m):
        maths.append(m.group(0)); return f"MATHTOKEN{len(maths) - 1}X"
    text = re.sub(r"\$\$.*?\$\$|\$[^$\n]+?\$", stash, text, flags=re.S)
    text = re.sub(rf"(?<=\d) (?={UNIT}(?![\wäöå²³/]))", "\u00a0", text)
    text = re.sub(r"(?<=\S) = (?=[\d−\-+(])", "\u00a0=\u00a0", text)   # "s = 0,15 m" never breaks at the equals sign
    return re.sub(r"MATHTOKEN(\d+)X", lambda m: maths[int(m.group(1))], text)


STEP = "<!-- vaihe -->"


def staged_example(lesson_html):
    """Worked example in stages. In lesson.md the solution of `## Esimerkki` is split by lines `<!-- vaihe -->`:
    the part before the first marker is the problem, each later part one stage of the solution. The page shows
    the problem and stage 1, and a button reveals the next stage (lesson.js). Without JavaScript, and in print,
    every stage is visible."""
    m = re.search(r"(<h2[^>]*>Esimerkki</h2>)(.*?)(?=<h2|<section|\Z)", lesson_html, flags=re.S)
    if not m or STEP not in m.group(2): return lesson_html
    parts = [p.strip() for p in m.group(2).split(STEP)]
    n = len(parts) - 1
    steps = "".join(f'<div class="step" data-step="{i}"><p class="step-label">Vaihe {i}/{n}</p>{p}</div>'
                    for i, p in enumerate(parts[1:], 1))
    body = (f'{parts[0]}<div class="worked" data-steps="{n}">{steps}'
            f'<p class="step-controls"><button type="button" class="next-step">Näytä seuraava vaihe</button> '
            f'<button type="button" class="all-steps">Näytä kaikki</button></p></div>')
    return lesson_html[:m.start(2)] + body + lesson_html[m.end(2):]


def named_sections(html):
    """`## Kaava: Lämpömäärä` is shown as "Lämpömäärä"; the key stays in data-section for the layout (inquiry.heading)."""
    def sub(m):
        key, shown = inquiry.heading(m.group(1))
        return f'<h2 data-section="{esc(key)}">{shown}</h2>' if shown != key else m.group(0)
    return re.sub(r"<h2>(.*?)</h2>", sub, html)


FIG = re.compile(r"(<p>(?:(?!</?p>|<svg).)*</p>|<table>.*?</table>|<ul>(?:(?!<ul>).)*?</ul>|<ol>(?:(?!<ol>).)*?</ol>)\s*<p>(<svg\b.*?</svg>)</p>", re.S)


def fig_rows(html):
    """A figure beside the paragraph, table or list it explains (NOTES.md §3 puts it right after that block): two
    columns on a wide screen, the figure under the text on a phone (site.css .fig-row)."""
    return FIG.sub(r'<div class="fig-row"><div class="fig-text">\1</div><div class="fig">\2</div></div>', html)


def fi(x):
    """Numbers with a decimal comma in page text (JSON keeps the point)."""
    return str(x).replace(".", ",").replace("-", "−") if isinstance(x, (int, float)) else str(x)   # true minus sign


def esc(s): return _h.escape(str(s), quote=True)


def page(title, body, crumbs, name, description, main_class="reading"):
    return (page_tpl.replace("{{title}}", esc(title)).replace("{{body}}", body).replace("{{crumbs}}", crumbs)
            .replace("{{main_class}}", main_class).replace("{{home}}", HOME)
            .replace("{{description}}", esc(description)).replace("{{url}}", BASE_URL + name))


def description_of(meta, lesson_md):
    """The motivating question makes the best one-line description; fall back to the first goal."""
    m = re.search(r"^> \*\*Miksi\*\*\s*(.+)$", lesson_md, re.M)
    if m: return "Miksi " + re.sub(r"[*_`]", "", m.group(1)).strip()
    goals = [re.sub(r"^(LOPS \w+:|Täsmennys:)\s*", "", g) for g in meta.get("goals", [])]
    return (meta["title"] + ". " + (goals[0] if goals else "")).strip()


def solutions_of(folder):
    """{exercise id: html} from solutions.md, one `## id` block each, line breaks kept (nl2br)."""
    f = folder / "solutions.md"
    if not f.exists(): return {}
    out = {}
    for block in re.split(r"^## ", f.read_text(), flags=re.M)[1:]:
        head, _, body = block.partition("\n")
        out[head.strip()] = nbsp_units(render_md(body.strip(), extensions=["nl2br"]))
    return out


def exercise_html(e, solution_html):
    ans = nbsp_units(f"{fi(e['answer'])} {e.get('unit', '')}".strip())
    numeric = isinstance(e["answer"], (int, float))
    check = ""
    if numeric:
        unit = esc(e.get("unit", ""))
        check = (f'<form class="check" data-answer="{e["answer"]}" data-tol="{e.get("tolerance", 0.02)}" novalidate>'
                 f'<input type="text" inputmode="decimal" autocomplete="off" enterkeyhint="done" aria-label="Vastaus tehtävään {esc(e["id"])}" placeholder="?">'
                 + (f'<span class="unit">{unit}</span>' if unit else "")
                 + '<button type="submit">Tarkista</button><output aria-live="polite"></output></form>')
    sol = f'<details class="solution"><summary>Ratkaisu</summary><div class="steps">{solution_html}</div></details>' if solution_html else ""
    return (f'<li id="{e["id"]}"><p class="task">{nbsp_units(e["text"])}</p>{check}'
            f'<details class="answer"><summary>Vastaus</summary><p>{ans}</p></details>{sol}</li>')


NOTICE = {"legacy": '<p class="notice" role="note">Prototyyppiversio: tämä oppitunti on julkaistu ennen nykyistä tarkistuskäytäntöä ja odottaa uudistusta. Sisältö voi vielä muuttua.</p>',
          "draft": '<p class="notice" role="note">Luonnos: tätä oppituntia ei ole vielä tarkistettu.</p>', "reviewed": ""}
assets = []  # published asset paths (relative to the output folder), checked before the swap
built = {}   # course -> [meta, ...]
states = {}  # lesson id -> review state of every lesson seen, also the ones left out
for folder in sorted((ROOT / "content").glob("*/*/")):
    if folder.parent.name == "_gold" or not (folder / "meta.json").exists(): continue
    meta = json.loads((folder / "meta.json").read_text())
    if only and meta["id"] != only: continue
    try: rs = review_status(folder)
    except ValueError as e: sys.exit(str(e))
    meta["state"] = rs["state"]; states[meta["id"]] = rs
    if rs["state"] == "draft" and not (only or build_all): continue   # publish only lessons whose reviews are current
    missing = [f for f in ("lesson.md", "exercises.json", "solutions.md", "exit-ticket.json") if not (folder / f).exists()]
    if missing:                                      # a draft still being written: skip it instead of failing the whole build
        print("skipped", meta["id"], "(missing " + ", ".join(missing) + ")"); continue
    ex = json.loads((folder / "exercises.json").read_text())
    publish = meta.get("solutions", "first")
    solutions = solutions_of(folder) if publish != "none" else {}
    ex_html = ""
    for lvl, items in ex.items():
        ex_html += f"<details class=\"level\"><summary>Taso {lvl[-1]} <span class=\"count\">{len(items)} tehtävää</span></summary><ol>"
        for i, e in enumerate(items):
            show = publish == "all" or (publish == "first" and i == 0)
            ex_html += exercise_html(e, solutions.get(e["id"]) if show else None)
        ex_html += "</ol></details>"
    exit_q = json.loads((folder / "exit-ticket.json").read_text())
    exit_items = "<ol>" + "".join(
        f"<li>{nbsp_units(q['q'])}<details class=\"answer\"><summary>Vastaus</summary><p>{nbsp_units(q['a'])}</p></details></li>"
        for q in exit_q) + "</ol>"
    lesson_md = (folder / "lesson.md").read_text()
    lesson_html = staged_example(fig_rows(named_sections(nbsp_units(render_md(lesson_md)))))
    inq = inquiry.load(folder)
    if inq is not None:
        errs = inquiry.validate(folder, inq, lesson_md)
        if errs: sys.exit("\n".join(errs))
    howto = '<p class="howto">Kirjoita vastaus ja paina Tarkista. Vastaus tarkistetaan selaimessa, mitään ei tallenneta.</p>'
    sim = ""
    where = courses.sim_dir(folder, meta)
    if where and where[0] == "lesson":                # FY3: sim.js in the lesson folder, published as <id>-sim.js
        shutil.copy(folder / "sim.js", SITE / f"{meta['id']}-sim.js"); assets.append(f"{meta['id']}-sim.js")
        sim = (f'<section id="sim"><{"h3" if inq else "h2"}>Simulaatio</{"h3" if inq else "h2"}><div id="sim-root"></div>'
               f'<script src="vendor/p5.min.js"></script><script src="sim-embed.js"></script><script src="{meta["id"]}-sim.js"></script><!--sim-info--></section>')
    elif where:                                       # a simulation folder of the course (or shared): published whole
        src, pub = where[1], where[2]
        if not (src / "sim.js").is_file(): sys.exit(f"{meta['id']}: simulation folder {src.relative_to(ROOT)} has no sim.js")
        shutil.copytree(src, SITE / pub, dirs_exist_ok=True); assets.append(f"{pub}/sim.js")
        css = f'<link rel="stylesheet" href="{pub}/sim.css">' if (src / "sim.css").is_file() else ""
        sim = (f'<section id="sim"><{"h3" if inq else "h2"}>Simulaatio</{"h3" if inq else "h2"}>{css}<div id="sim-root" data-base="{pub}/"></div>'
               f'<script src="vendor/p5.min.js"></script><script src="sim-embed.js"></script><script src="{pub}/sim.js"></script><!--sim-info--></section>')
    for ref in courses.pic_refs(folder):              # pictures the text refers to, at the same relative path
        if not courses.pic_source(ref).is_file(): sys.exit(f"{meta['id']}: picture {ref} not found (expected assets/{ref})")
        (SITE / ref).parent.mkdir(parents=True, exist_ok=True); shutil.copy(courses.pic_source(ref), SITE / ref); assets.append(ref)
    name = f"{meta['id']}.html"
    if inq is None:                                   # classic layout: theory (with the sim inside), exit ticket, exercises
        sim = sim.replace("<!--sim-info-->", "")
        if sim and "<!-- sim -->" in lesson_html: lesson_html = lesson_html.replace("<!-- sim -->", sim, 1)
        elif sim and re.search(r"<h2[^>]*>Esimerkki", lesson_html): lesson_html = re.sub(r"(<h2[^>]*>Esimerkki)", sim + r"\1", lesson_html, count=1)
        elif sim: lesson_html += sim
        toc = ('<a href="#teoria">Teoria</a>' + ('<a href="#sim">Simulaatio</a>' if sim else "")
               + f'<a href="#exit">{inquiry.EXIT_TITLE}</a><a href="#exercises">{inquiry.EXERCISES_TITLE}</a>')
        main = (f'<article id="teoria">{lesson_html}</article>\n'
                f'<section id="exit"><h2>{inquiry.EXIT_TITLE}</h2>{exit_items}</section>\n'
                f'<section id="exercises"><h2>{inquiry.EXERCISES_TITLE}</h2>{howto}{ex_html}</section>')
    else:                                             # inquiry layout: the same parts placed by inquiry.json (scripts/inquiry.py)
        lesson_html = lesson_html.replace("<!-- sim -->", "")
        pieces = re.split(r"(?=<h2[ >])", lesson_html)
        intro = pieces[0] if not pieces[0].startswith("<h2") else ""
        sections = {}
        for piece in pieces[1:] if intro or len(pieces) > 1 else []:
            m = re.match(r'<h2(?: data-section="([^"]*)")?>(.*?)</h2>', piece)
            if m: sections[_h.unescape(m.group(1) or m.group(2))] = re.sub(r"^<h2[^>]*>(.*?)</h2>", r'<h3 class="theory-h">\1</h3>', piece, count=1)
        parts = {"intro": intro, "sections": sections, "sim": sim, "exercises": f'{howto}{ex_html}',
                 "exit": f'<div id="exit"><h3>{inquiry.EXIT_TITLE}</h3>{exit_items}</div>'}
        body, toc = inquiry.render(folder, inq, parts, lambda t: nbsp_units(render_md(t)))
        main = f'<article id="teoria" class="inquiry">{body}</article>'
    html = (tpl.replace("{{title}}", esc(meta["title"])).replace("{{course}}", meta["course"]).replace("{{notice}}", NOTICE[meta["state"]])
            .replace("{{toc}}", toc).replace("{{main}}", main)
            .replace("{{scripts}}", '<script src="inquiry.js"></script>' if inq else "")
            .replace("{{description}}", esc(description_of(meta, lesson_md))).replace("{{url}}", BASE_URL + name)
            .replace("{{home}}", HOME))
    (SITE / name).write_text(html)
    built.setdefault(meta["course"], []).append(meta)
    print("built", meta["id"], f"({meta['state']})")

# Course pages and front page. Every module in curriculum.json gets a page; lessons built in this run are
# links, the rest are listed as "tulossa" so students see the whole course and nav links always resolve.
modules = [(k, v) for k, v in curriculum.items() if not k.startswith("_")]
built_ids = {m["id"] for ms in built.values() for m in ms}
legacy_ids = {m["id"] for ms in built.values() for m in ms if m["state"] == "legacy"}

cards = ""
for code, mod in modules:
    slots = mod.get("lessons", [])
    done = sum(1 for l in slots if l["id"] in built_ids)
    pct = round(100 * done / len(slots)) if slots else 0
    kind = "Pakollinen" if mod.get("type") == "pakollinen" else "Valinnainen"
    state = f"{done} / {len(slots)} oppituntia valmiina" if done else f"{len(slots)} oppituntia suunnitteilla"
    cards += (f'<a class="card{" live" if done else ""}" href="{code}.html"><span class="code">{code}</span>'
              f'<span class="ctitle">{esc(mod["title"])}</span><span class="meta">{mod.get("op", "")} op · {kind}</span>'
              f'<span class="bar" aria-hidden="true"><span style="width:{pct}%"></span></span><span class="state">{state}</span></a>')

    items = ""
    for l in slots:
        if l["id"] in legacy_ids:
            items += f'<li class="live legacy"><a href="{l["id"]}.html">{esc(l["title"])}</a> <span class="count">prototyyppi</span></li>'
        elif l["id"] in built_ids:
            items += f'<li class="live"><a href="{l["id"]}.html">{esc(l["title"])}</a></li>'
        else:
            items += f'<li class="soon"><span>{esc(l["title"])}</span> <span class="count">tulossa</span></li>'
    goals = "".join(f"<li>{esc(g)}</li>" for g in mod.get("tavoitteet", []))
    body = (f'<span class="eyebrow">{code} · {mod.get("op", "")} op · {kind}</span><h1>{esc(mod["title"])}</h1>'
            f'<p class="lead">{done} / {len(slots)} oppituntia valmiina</p>'
            + (f'<h2>Moduulin tavoitteet</h2><p>Opiskelija</p><ul>{goals}</ul>' if goals else "")
            + f'<h2>Oppitunnit</h2><ol class="lessons">{items}</ol>')
    desc = f"{code} {mod['title']}: lukion fysiikan moduulin oppitunnit, simulaatiot ja tehtävät. {done} / {len(slots)} oppituntia valmiina."
    (SITE / f"{code}.html").write_text(page(f"{code} · {mod['title']}", body, f'<a href="index.html">Fysiikkalabra</a> › {code}', f"{code}.html", desc))

latest = ""
for code, mod in modules:                       # most recently planned published lesson of the highest module
    for l in mod.get("lessons", []):
        if l["id"] in built_ids: latest = f'<p class="latest">Uusin oppitunti: <a href="{l["id"]}.html">{esc(l["title"])}</a> ({code})</p>'
total = sum(len(m.get("lessons", [])) for _, m in modules)
home = (
    '<section class="hero"><span class="eyebrow">Fysiikka · LOPS 2019 · Simulaatiot</span>'
    '<h1>Fysiikkalabra</h1>'
    '<p class="lead">Teoria, simulaatiot ja tehtävät lukion fysiikkaan. Oppitunnit noudattavat lukion opetussuunnitelman perusteita 2019 (LOPS), moduuli kerrallaan.</p>'
    + latest + '</section>'
    '<ul class="how"><li><strong>Teoria</strong>lyhyesti ja yksi ajatus kerrallaan, kaavat selitettyinä.</li>'
    '<li><strong>Simulaatio</strong>jota voit säätää itse ja josta näet laskennan tulokset heti.</li>'
    '<li><strong>Tehtävät ja exit ticket</strong>kolmella tasolla, vastaukset tarkistettavissa ja ratkaisut avattavissa.</li></ul>'
    '<h2 id="moduulit">Moduulit</h2>' f'<div class="cards">{cards}</div>'
    f'<p class="count">{len(built_ids)} oppituntia valmiina, {total} suunnitteilla kaikkiaan. Uusia oppitunteja julkaistaan sitä mukaa kuin ne valmistuvat.</p>')
(SITE / "index.html").write_text(page("Fysiikkalabra", home, "", "index.html",
                                      "Teoria, simulaatiot ja tehtävät lukion fysiikkaan, LOPS 2019:n moduulit FY1–FY8.", main_class=""))
removed = []
if SITE.name == "site.tmp":                      # a lesson leaves the live site only with a warning (an annotation on CI)
    for old_page in sorted(LIVE.glob("*.html")):
        lid = old_page.stem
        if lid in states and lid not in built_ids:
            why = ", ".join(f"{n}={v}" for n, v in states[lid]["reports"].items() if v != "missing") or "no reports"
            removed.append(lid)
            print(f"{'::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING:'} {lid} is on the live site but its reviews are not current ({why}); this build removes it")
if SITE.name == "site.tmp":                      # check the render, then swap it in; the old site comes back if the swap fails
    expected = ["index.html", "site.css", "lesson.js", "sim-embed.js", "inquiry.js"] + [f"{c}.html" for c, _ in modules] + [f"{i}.html" for i in built_ids] + assets
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
print("built index +", len(modules), "module pages ->", (LIVE if SITE.name == "site.tmp" else SITE).relative_to(ROOT),
      f"({sum(m['state'] == 'reviewed' for ms in built.values() for m in ms)} reviewed, {len(legacy_ids)} legacy, "
      f"{sum(m['state'] == 'draft' for ms in built.values() for m in ms)} draft" + (f", {len(removed)} removed: {', '.join(removed)}" if removed else "") + ")")
