"""Edellinen luku / Seuraava luku on the built site (teacher 2026-10-29, build.py chapter_nav): in every language each
lesson and Sovella page has one chapter navigation; the links follow curriculum.json's teaching order (FY3 is not
numeric), skip unpublished chapters, never point to a page that is not there, stay in the page's language, and the
first and last chapter lead to the module page or to Sovella itsenäisesti. The path over the page (teacher 2026-11-08,
build.py chapter_crumbs) holds the chapter menu with this page as the current one, every link of it to a page that is
there, and Edellinen / Seuraava to the same pages as the links under the page.

  python scripts/test_chapter_nav.py [site]"""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses

root = courses.ROOT / (sys.argv[1] if len(sys.argv) > 1 else "site")
cur = json.loads((courses.ROOT / "curriculum.json").read_text())
fails = 0
def check(name, ok, detail=""):
    global fails
    if not ok: print(f"FAIL {name}: {detail}"); fails += 1

NAV = re.compile(r'<nav class="chapter-nav"[^>]*>(.*?)</nav>', re.S)
CRUMBS = re.compile(r'<nav class="crumbs"[^>]*>(.*?)</nav>', re.S)
A = re.compile(r'<a class="(prev|next)[^"]*" href="([^"]+)"')
pages = 0
for out in [root] + sorted(p for p in root.iterdir() if p.is_dir() and (p / "index.html").is_file() and len(p.name) <= 8):
    for code, mod in cur.items():
        if code.startswith("_"): continue
        seq = [l["id"] + ".html" for l in mod.get("lessons", []) if (out / f"{l['id']}.html").is_file()]
        if (out / f"{code}-koe.html").is_file(): seq.append(f"{code}-koe.html")
        if (out / f"{code}-sovella.html").is_file(): seq.append(f"{code}-sovella.html")
        for i, name in enumerate(seq):
            html = (out / name).read_text(); pages += 1
            navs = NAV.findall(html)
            check(f"{out.name}/{name} has one chapter navigation", len(navs) == 1, len(navs))
            if len(navs) != 1: continue
            links = dict(A.findall(navs[0]))
            want_prev = seq[i - 1] if i else f"{code}.html"
            want_next = seq[i + 1] if i + 1 < len(seq) else f"{code}.html"
            check(f"{out.name}/{name} previous", links.get("prev") == want_prev, f"{links.get('prev')} != {want_prev}")
            check(f"{out.name}/{name} next", links.get("next") == want_next, f"{links.get('next')} != {want_next}")
            for h in links.values(): check(f"{out.name}/{name} link {h} exists in the same language", (out / h).is_file())
            crumbs = CRUMBS.search(html)
            check(f"{out.name}/{name} has the chapter menu in its path", crumbs and "details class=\"ch-menu\"" in crumbs.group(1))
            if not crumbs: continue
            menu = re.search(r'<div class="ch-menu-panel">(.*?)</div>', crumbs.group(1), re.S)
            marked = re.findall(r'<a href="([^"]+)" aria-current="page">', menu.group(1) if menu else "")
            check(f"{out.name}/{name} menu marks this page", marked == [name], marked)
            for h in re.findall(r'href="([^"]+)"', menu.group(1) if menu else ""): check(f"{out.name}/{name} menu link {h} exists", (out / h).is_file())
            arrows = dict(re.findall(r'<a class="(prev|next)" href="([^"]+)"', crumbs.group(1)))
            check(f"{out.name}/{name} path arrows = links under the page", arrows == links, f"{arrows} != {links}")
check("FY3 follows the teaching order (fy3-3 → fy3-13)", 'href="fy3-13.html" rel="next"' in (root / "fy3-3.html").read_text() if (root / "fy3-3.html").is_file() and (root / "fy3-13.html").is_file() else True)
# a card's very long word breaks at a syllable or at a compound's joint, never elsewhere (UI audit 2026-11-10, finding 16; tablefit.cards)
import tablefit
_h = lambda w: tablefit.hyphenate_card(w).replace(tablefit.SHY, "-")
check("card title: syllables", _h("Liukukitkakertoimen") == "Liu-ku-kit-ka-ker-toi-men", _h("Liukukitkakertoimen"))
for _w, _want in (("Potentiaalienergia", "Po-ten-tiaa-li-ener-gia"), ("puoliintumisaika", "puo-liin-tu-mis-ai-ka"), ("desibeliasteikko", "de-si-be-li-as-teik-ko"), ("mikroaaltouunilla", "mik-ro-aal-to-uu-nil-la")):
    check(f"card title: the joint of the compound {_w}", _h(_w) == _want, _h(_w))
_card = '<li><div class="ch-box"><span class="l-num">1</span><a href="a.html">Liukukitkakertoimen määrittäminen $F_\\text{kitkakerroinkitkakerroin}$</a></div></li>'
_out = tablefit.cards(_card, True)
check("card title: only the very long word gets soft hyphens, a formula and the link are left alone", _out.replace(tablefit.SHY, "") == _card and _out.count(tablefit.SHY) == 6 and "määrittäminen $F" in _out, _out.replace(tablefit.SHY, "-"))
check("card title: a second pass changes nothing, another language is left alone", tablefit.cards(_out, True) == _out and tablefit.cards(_card, False) == _card)
if (root / "FY10.html").is_file():
    check("FY10: the long card titles of the built page carry soft hyphens", "Liu\u00adku\u00adkit\u00adka\u00adker\u00adtoi\u00admen" in (root / "FY10.html").read_text())
check("pages were checked", pages > 0)
print(f"{pages} pages, {fails} failure(s)"); sys.exit(1 if fails else 0)
