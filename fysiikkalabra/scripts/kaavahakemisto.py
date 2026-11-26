"""Kaavahakemisto (work queue 17f PR 1; teacher 2026-11-15): kaavat.html in every language, the formulas that have a MAFY
name, module by module, each with its formula in display LaTeX and links to the chapters (FY9: units) that present it.

The source is the teacher-approved lists docs/<module>/kaavanimet.tsv (scripts/kaavat.py `table`): nothing is written
by hand and no physics is rewritten. Only a row with a name counts (a row `=` is another form of the formula above it and
stands under it; a row `+` is extra information that is not in MAFY's tables and is left out), and only a lesson or unit
that is published in the page's language is linked or counted. No script, no storage, no request: a static page in the
existing `.kaavat` style (templates/site.css).

  python scripts/kaavahakemisto.py       print the index of every language from the lists (what build.py would publish)
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kaavat

PAGE = "kaavat.html"
LANG_COLS = {"fi": ("kaava", "nimi"), "fi-easy": ("kaava", "nimi"), "en": ("kaava_en", "name_en")}
ID = re.compile(r"fy\d+-[a-z0-9-]+")        # a lesson (fy3-4) or a unit (fy9-aallot); a stray line of a list is not one


def esc(s): return html.escape(str(s), quote=True)


def collect(lang, published, module_titles):
    """[{code, title, entries: [{name, forms: [tex], links: [(label, href)]}]}] in module order.

    published: {lesson or unit id: (label, href)} of the pages this language publishes; module_titles: {code: title}.
    An entry is one name: every distinct form of its formula in the lists' order, and the pages that show any of them."""
    fcol, ncol = LANG_COLS[lang]
    mods = {}
    last = None                                   # the entry a `=` row belongs to
    for r in kaavat.table("all"):
        key = r["_key"]
        if not ID.fullmatch(key): last = None; continue
        code = key.split("-")[0].upper()
        name, tex = (r.get(ncol) or "").strip(), " ".join((r.get(fcol) or "").split())
        if not tex: continue
        if name == kaavat.PLUS: last = None; continue
        if name == kaavat.SAME:
            entry = last
        elif name:
            entry = mods.setdefault(code, {}).setdefault(name, {"forms": [], "links": []})
            last = entry
        else:
            last = None; continue
        if entry is None or key not in published: continue
        if tex not in entry["forms"]: entry["forms"].append(tex)
        link = published[key]
        if link not in entry["links"]: entry["links"].append(link)
    out = []
    for code in sorted(mods, key=lambda c: int(c[2:])):
        entries = [dict(name=n, **e) for n, e in mods[code].items() if e["links"]]
        if entries: out.append({"code": code, "title": module_titles.get(code, code), "entries": entries})
    return out


def body(T, mods):
    """The page's <main> content: the heading, a row of module links (codes only) and one `.kaavat` table per module."""
    nav = "".join(f'<li><a href="#{esc(m["code"])}">{esc(m["code"])}</a></li>' for m in mods)
    secs = ""
    for m in mods:
        rows = ""
        for e in m["entries"]:
            forms = "\n".join(f"$${html.escape(f, quote=False)}$$" for f in e["forms"])
            links = ", ".join(f'<a href="{esc(h)}">{esc(l)}</a>' for l, h in e["links"])
            rows += (f'<div class="kaava-rivi"><dt>{esc(e["name"])}</dt><dd>{forms}'
                     f'<p class="kaava-luvut"><span class="kaava-luvut-t">{esc(T("kaavat.in"))}</span> {links}</p></dd></div>')
        secs += (f'<section class="kaava-moduuli" id="{esc(m["code"])}" aria-labelledby="h-{esc(m["code"])}">'
                 f'<h2 id="h-{esc(m["code"])}"><span class="mod-code">{esc(m["code"])}</span> {esc(m["title"])}</h2>'
                 f'<dl class="kaavat">{rows}</dl></section>')
    return (f'<h1>{esc(T("kaavat.title"))}</h1><p class="lead">{esc(T("kaavat.lead"))}</p>'
            f'<nav class="kaava-nav" aria-label="{esc(T("site.modules"))}"><ul>{nav}</ul></nav>' + secs)


if __name__ == "__main__":
    import json
    import courses
    for lang in LANG_COLS:
        pub = {}
        for f in courses.lessons(lang=lang):
            m = json.loads((f / "meta.json").read_text())
            pub[m["id"]] = (m["title"], f'{m["id"]}.html')
        mods = collect(lang, pub, {})
        print(lang, sum(len(m["entries"]) for m in mods), "names in", len(mods), "modules")
