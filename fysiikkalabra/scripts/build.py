"""Render content/ folders into site/. Usage: python scripts/build.py [lesson-id]

Without an argument only lessons with "status": "reviewed" are built (publishing rule).
With a lesson id that lesson is built regardless of status, for previewing a draft.
With --all every lesson is built regardless of status (CI uses this to test drafts too).
The plain build writes to site/ (committed, served by GitHub Pages); a preview or --all build
writes to preview/ (git-ignored), so a draft can never end up in the published folder.

Page anatomy: the worked example is shown in stages split by `<!-- vaihe -->` lines (staged_example).
The simulation is placed inside the theory, after the formula section (before "## Esimerkki"),
or where lesson.md has a line `<!-- sim -->`. Each exercise gets a browser-side answer check and, depending on
meta.solutions ("first" by default, "all", "none"), its worked solution from solutions.md.
"""
import json, sys, re, shutil, pathlib, html as _h, markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
HOME = "../../index.html"                      # the portfolio front page, two levels above site/
BASE_URL = "https://hellsla.github.io/fysiikkalabra/site/"
arg = sys.argv[1] if len(sys.argv) > 1 else None
build_all = arg == "--all"; only = None if build_all else arg
SITE = ROOT / ("preview" if (only or build_all) else "site"); SITE.mkdir(exist_ok=True)
for old in SITE.glob("*.html"): old.unlink()          # no stale pages from an earlier build
for old in SITE.glob("*-sim.js"): old.unlink()
TPL = ROOT / "templates"
for f in ("site.css", "lesson.js", "sim-embed.js"): shutil.copy(TPL / f, SITE / f)
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


built = {}   # course -> [meta, ...]
for folder in sorted((ROOT / "content").glob("*/*/")):
    if folder.parent.name == "_gold" or not (folder / "meta.json").exists(): continue
    meta = json.loads((folder / "meta.json").read_text())
    if only and meta["id"] != only: continue
    if meta.get("status") != "reviewed" and not (only or build_all): continue   # publish only reviewed lessons
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
    exit_html = "<h2>Lähtölippu</h2><ol>" + "".join(
        f"<li>{nbsp_units(q['q'])}<details class=\"answer\"><summary>Vastaus</summary><p>{nbsp_units(q['a'])}</p></details></li>"
        for q in exit_q) + "</ol>"
    lesson_md = (folder / "lesson.md").read_text()
    lesson_html = staged_example(nbsp_units(render_md(lesson_md)))
    sim = ""
    if (folder / "sim.js").exists():
        shutil.copy(folder / "sim.js", SITE / f"{meta['id']}-sim.js")
        sim = (f'<section id="sim"><h2>Simulaatio</h2><div id="sim-root"></div>'
               f'<script src="vendor/p5.min.js"></script><script src="sim-embed.js"></script><script src="{meta["id"]}-sim.js"></script></section>')
        if "<!-- sim -->" in lesson_html:
            lesson_html = lesson_html.replace("<!-- sim -->", sim, 1)
        elif re.search(r"<h2[^>]*>Esimerkki", lesson_html):
            lesson_html = re.sub(r"(<h2[^>]*>Esimerkki)", sim + r"\1", lesson_html, count=1)
        else:
            lesson_html += sim
    name = f"{meta['id']}.html"
    html = (tpl.replace("{{title}}", esc(meta["title"])).replace("{{course}}", meta["course"])
            .replace("{{lesson_html}}", lesson_html).replace("{{exercises_html}}", ex_html).replace("{{exit_html}}", exit_html)
            .replace("{{toc_sim}}", '<a href="#sim">Simulaatio</a>' if sim else "")
            .replace("{{description}}", esc(description_of(meta, lesson_md))).replace("{{url}}", BASE_URL + name)
            .replace("{{home}}", HOME))
    (SITE / name).write_text(html)
    built.setdefault(meta["course"], []).append(meta)
    print("built", meta["id"], f"({meta.get('status')})")

# Course pages and front page. Every module in curriculum.json gets a page; lessons built in this run are
# links, the rest are listed as "tulossa" so students see the whole course and nav links always resolve.
modules = [(k, v) for k, v in curriculum.items() if not k.startswith("_")]
built_ids = {m["id"] for ms in built.values() for m in ms}

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
        if l["id"] in built_ids:
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
    '<li><strong>Tehtävät ja lähtölippu</strong>kolmella tasolla, vastaukset tarkistettavissa ja ratkaisut avattavissa.</li></ul>'
    '<h2 id="moduulit">Moduulit</h2>' f'<div class="cards">{cards}</div>'
    f'<p class="count">{len(built_ids)} oppituntia valmiina, {total} suunnitteilla kaikkiaan. Uusia oppitunteja julkaistaan sitä mukaa kuin ne valmistuvat.</p>')
(SITE / "index.html").write_text(page("Fysiikkalabra", home, "", "index.html",
                                      "Teoria, simulaatiot ja tehtävät lukion fysiikkaan, LOPS 2019:n moduulit FY1–FY8.", main_class=""))
print("built index +", len(modules), "module pages ->", SITE.relative_to(ROOT), f"({len(built_ids)} lessons)")
