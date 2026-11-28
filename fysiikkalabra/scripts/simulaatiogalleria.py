"""Simulaatiogalleria (work queue 17f PR 2; teacher 2026-11-15, K9): simulaatiot.html in every language, every published
chapter that has a simulation (`meta.json` "sim": true), module by module as the chapter tiles of the module pages
(scripts/cardgrid.py). A tile links to the Tutki stage of its chapter (`<id>.html#tutki`), where the simulation is; there
are no pages of simulations of their own and no picture is added. A simulation has no name of its own, so the tile carries
its chapter's number and title. No script, no storage, no request.

  python scripts/simulaatiogalleria.py     print the number of simulations per module, from meta.json
"""
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cardgrid

PAGE = "simulaatiot.html"
ANCHOR = "tutki"        # the Tutki stage of a chapter page (inquiry.py STAGE_IDS)


def esc(s): return html.escape(str(s), quote=True)


def sim_ids(lessons):
    """{chapter id} of the lesson folders (courses.lessons) whose meta.json says "sim": true."""
    return {m["id"] for m in (json.loads((f / "meta.json").read_text(encoding="utf-8")) for f in lessons) if m.get("sim")}


def collect(modules, built, sims):
    """[{code, title, tiles: [(n, chapter title, chapter id)]}] in module order. modules: [(code, {"title", "lessons":
    [{id, title}]})] as build.py has them in the page's language; n is the chapter's number in its module; a chapter that
    is not published in the language or has no simulation is left out, and so is a module left with none."""
    out = []
    for code, mod in modules:
        tiles = [(n, l["title"], l["id"]) for n, l in enumerate(mod.get("lessons", []), 1) if l["id"] in built and l["id"] in sims]
        if tiles: out.append({"code": code, "title": mod["title"], "tiles": tiles})
    return out


def body(T, mods):
    """The page's <main> content: heading, lead, a row of module links (codes only) and one tile grid per module."""
    nav = "".join(f'<li><a href="#{esc(m["code"])}">{esc(m["code"])}</a></li>' for m in mods)
    secs = ""
    for m in mods:
        tiles = "".join(cardgrid.card(esc(T("site.chapter_n", n=n)), esc(title), f"{cid}.html#{ANCHOR}") for n, title, cid in m["tiles"])
        secs += (f'<section class="kaava-moduuli sim-moduuli" id="{esc(m["code"])}" aria-labelledby="h-{esc(m["code"])}">'
                 f'<h2 id="h-{esc(m["code"])}"><span class="mod-code">{esc(m["code"])}</span> {esc(m["title"])}</h2>'
                 f'{cardgrid.grid(tiles)}</section>')
    return (f'<h1>{esc(T("simulaatiot.title"))}</h1><p class="lead">{esc(T("simulaatiot.lead"))}</p>'
            f'<nav class="kaava-nav" aria-label="{esc(T("site.modules"))}"><ul>{nav}</ul></nav>' + secs)


if __name__ == "__main__":
    import courses
    ids = sim_ids(courses.lessons())
    from collections import Counter
    print(sorted(Counter(i.split("-")[0].upper() for i in ids).items()), len(ids), "simulations")
