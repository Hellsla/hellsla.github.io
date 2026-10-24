"""Render content/ folders into site/. Usage: python scripts/build.py [lesson-id]

Without an argument only lessons with "status": "reviewed" are built (publishing rule).
With a lesson id that lesson is built regardless of status, for previewing a draft.
With --all every lesson is built regardless of status (CI uses this to test drafts too).
The plain build writes to site/ (committed, served by GitHub Pages); a preview or --all build
writes to preview/ (git-ignored), so a draft can never end up in the published folder.
"""
import json, sys, re, shutil, pathlib, markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
HOME = "../../index.html"                      # the portfolio front page, two levels above site/
arg = sys.argv[1] if len(sys.argv) > 1 else None
build_all = arg == "--all"; only = None if build_all else arg
SITE = ROOT / ("preview" if (only or build_all) else "site"); SITE.mkdir(exist_ok=True)
for old in SITE.glob("*.html"): old.unlink()          # no stale pages from an earlier build
for old in SITE.glob("*-sim.js"): old.unlink()
TPL = ROOT / "templates"
shutil.copy(TPL / "site.css", SITE / "site.css")
shutil.copytree(TPL / "vendor", SITE / "vendor", dirs_exist_ok=True)   # p5 + KaTeX, no CDN needed
tpl = (TPL / "lesson.html").read_text()
page_tpl = (TPL / "page.html").read_text()
curriculum = json.loads((ROOT / "curriculum.json").read_text())


def render_md(text):
    """Markdown -> HTML, with LaTeX kept out of markdown's reach.
    ```latex fences become $$...$$; every $$...$$ and $...$ is swapped for a token first,
    so underscores, backslashes and asterisks inside maths are not read as markdown."""
    text = re.sub(r"```latex\n(.*?)```", lambda m: "\n$$" + m.group(1).strip() + "$$\n", text, flags=re.S)
    maths = []
    def stash(m):
        maths.append(m.group(0)); return f"MATHTOKEN{len(maths) - 1}X"
    text = re.sub(r"\$\$.*?\$\$|\$[^$\n]+?\$", stash, text, flags=re.S)
    html = markdown.markdown(text, extensions=["fenced_code", "tables"])
    return re.sub(r"MATHTOKEN(\d+)X", lambda m: maths[int(m.group(1))], html)


def fi(x):
    """Numbers with a decimal comma in page text (JSON keeps the point)."""
    return str(x).replace(".", ",") if isinstance(x, (int, float)) else str(x)


def page(title, body, crumbs, main_class="reading"):
    return (page_tpl.replace("{{title}}", title).replace("{{body}}", body).replace("{{crumbs}}", crumbs)
            .replace("{{main_class}}", main_class).replace("{{home}}", HOME))


built = {}   # course -> [meta, ...]
for folder in sorted((ROOT / "content").glob("*/*/")):
    if folder.parent.name == "_gold" or not (folder / "meta.json").exists(): continue
    meta = json.loads((folder / "meta.json").read_text())
    if only and meta["id"] != only: continue
    if meta.get("status") != "reviewed" and not (only or build_all): continue   # publish only reviewed lessons
    ex = json.loads((folder / "exercises.json").read_text())
    ex_html = ""
    for lvl, items in ex.items():
        ex_html += f"<details class=\"level\"><summary>Taso {lvl[-1]} <span class=\"count\">{len(items)} tehtävää</span></summary><ol>"
        for e in items:
            ans = f"{fi(e['answer'])} {e.get('unit', '')}".strip()
            ex_html += (f"<li id=\"{e['id']}\">{e['text']}<details class=\"answer\"><summary>Vastaus</summary>"
                        f"<p>{ans}</p></details></li>")
        ex_html += "</ol></details>"
    exit_q = json.loads((folder / "exit-ticket.json").read_text())
    exit_html = "<h2>Lähtölippu</h2><ol>" + "".join(
        f"<li>{q['q']}<details class=\"answer\"><summary>Vastaus</summary><p>{q['a']}</p></details></li>"
        for q in exit_q) + "</ol>"
    sim = ""
    if (folder / "sim.js").exists():
        shutil.copy(folder / "sim.js", SITE / f"{meta['id']}-sim.js")
        sim = (f'<section id="sim"><h2>Simulaatio</h2><div id="sim-root"></div>'
               f'<script src="vendor/p5.min.js"></script><script src="{meta["id"]}-sim.js"></script></section>')
    html = (tpl.replace("{{title}}", meta["title"]).replace("{{course}}", meta["course"])
            .replace("{{lesson_html}}", render_md((folder / "lesson.md").read_text()))
            .replace("{{sim_block}}", sim).replace("{{exercises_html}}", ex_html).replace("{{exit_html}}", exit_html)
            .replace("{{home}}", HOME))
    (SITE / f"{meta['id']}.html").write_text(html)
    built.setdefault(meta["course"], []).append(meta)
    print("built", meta["id"], f"({meta.get('status')})")

# Course pages and front page. Every module in curriculum.json gets a page; lessons built in this run are
# links, the rest are listed as "tulossa" so students see the whole course and nav links always resolve.
import html as _h
modules = [(k, v) for k, v in curriculum.items() if not k.startswith("_")]
built_ids = {m["id"] for ms in built.values() for m in ms}
def esc(s): return _h.escape(s, quote=True)

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
    (SITE / f"{code}.html").write_text(page(f"{code} · {mod['title']}", body, f'<a href="index.html">Fysiikkalabra</a> › {code}'))

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
    '<li><strong>Tehtävät ja lähtölippu</strong>kolmella tasolla, vastaukset avattavissa.</li></ul>'
    '<h2 id="moduulit">Moduulit</h2>' f'<div class="cards">{cards}</div>'
    f'<p class="count">{len(built_ids)} oppituntia valmiina, {total} suunnitteilla kaikkiaan. Uusia oppitunteja julkaistaan sitä mukaa kuin ne valmistuvat.</p>')
(SITE / "index.html").write_text(page("Fysiikkalabra", home, "", main_class=""))
print("built index +", len(modules), "module pages ->", SITE.relative_to(ROOT), f"({len(built_ids)} lessons)")
