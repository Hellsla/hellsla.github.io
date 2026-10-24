"""Render content/ folders into site/. Usage: python scripts/build.py [lesson-id]

Without an argument only lessons with "status": "reviewed" are built (publishing rule).
With a lesson id that lesson is built regardless of status, for previewing a draft.
With --all every lesson is built regardless of status (CI uses this to test drafts too).
"""
import json, sys, re, shutil, pathlib, markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE = ROOT / "site"; SITE.mkdir(exist_ok=True)
TPL = ROOT / "templates"
shutil.copy(TPL / "site.css", SITE / "site.css")
shutil.copytree(TPL / "vendor", SITE / "vendor", dirs_exist_ok=True)   # p5 + KaTeX, no CDN needed
tpl = (TPL / "lesson.html").read_text()
page_tpl = (TPL / "page.html").read_text()
curriculum = json.loads((ROOT / "curriculum.json").read_text())
arg = sys.argv[1] if len(sys.argv) > 1 else None
build_all = arg == "--all"; only = None if build_all else arg


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


def page(title, body, crumbs):
    return (page_tpl.replace("{{title}}", title).replace("{{body}}", body).replace("{{crumbs}}", crumbs))


built = {}   # course -> [meta, ...]
for folder in sorted((ROOT / "content").glob("*/*/")):
    if folder.parent.name == "_gold" or not (folder / "meta.json").exists(): continue
    meta = json.loads((folder / "meta.json").read_text())
    if only and meta["id"] != only: continue
    if meta.get("status") != "reviewed" and not (only or build_all): continue   # publish only reviewed lessons
    ex = json.loads((folder / "exercises.json").read_text())
    ex_html = ""
    for lvl, items in ex.items():
        ex_html += f"<details class=\"level\"><summary>Taso {lvl[-1]}</summary><ol>"
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
            .replace("{{sim_block}}", sim).replace("{{exercises_html}}", ex_html).replace("{{exit_html}}", exit_html))
    (SITE / f"{meta['id']}.html").write_text(html)
    built.setdefault(meta["course"], []).append(meta)
    print("built", meta["id"], f"({meta.get('status')})")

# Course pages and front page, listing only the lessons built in this run (nav links must resolve).
for course, lessons in built.items():
    title = curriculum.get(course, {}).get("title", course)
    order = {l["id"]: i for i, l in enumerate(curriculum.get(course, {}).get("lessons", []))}
    lessons.sort(key=lambda m: order.get(m["id"], 999))
    items = "".join(f'<li><a href="{m["id"]}.html">{m["title"]}</a></li>' for m in lessons)
    (SITE / f"{course}.html").write_text(page(f"{course} · {title}", f"<h1>{course} · {title}</h1><ol class=\"lessons\">{items}</ol>",
                                              '<a href="index.html">Fysiikkalabra</a> › ' + course))
courses = "".join(f'<li><a href="{c}.html">{c} · {curriculum.get(c, {}).get("title", c)}</a> '
                  f'<span class="count">{len(ls)} oppituntia</span></li>' for c, ls in sorted(built.items()))
(SITE / "index.html").write_text(page("Fysiikkalabra",
    "<h1>Fysiikkalabra</h1><p>Teoria, simulaatiot ja tehtävät lukion fysiikkaan ja matematiikkaan.</p>"
    f"<ul class=\"courses\">{courses}</ul>", "Fysiikkalabra"))
print("built index +", ", ".join(built) if built else "no courses")
