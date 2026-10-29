"""Edellinen luku / Seuraava luku on the built site (teacher 2026-10-29, build.py chapter_nav): in every language each
lesson and Sovella page has one chapter navigation; the links follow curriculum.json's teaching order (FY3 is not
numeric), skip unpublished chapters, never point to a page that is not there, stay in the page's language, and the
first and last chapter lead to the module page or to Sovella itsenäisesti.

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
A = re.compile(r'<a class="(prev|next)[^"]*" href="([^"]+)"')
pages = 0
for out in [root] + sorted(p for p in root.iterdir() if p.is_dir() and (p / "index.html").is_file() and len(p.name) <= 8):
    for code, mod in cur.items():
        if code.startswith("_"): continue
        seq = [l["id"] + ".html" for l in mod.get("lessons", []) if (out / f"{l['id']}.html").is_file()]
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
check("FY3 follows the teaching order (fy3-3 → fy3-13)", 'href="fy3-13.html" rel="next"' in (root / "fy3-3.html").read_text() if (root / "fy3-3.html").is_file() and (root / "fy3-13.html").is_file() else True)
check("pages were checked", pages > 0)
print(f"{pages} pages, {fails} failure(s)"); sys.exit(1 if fails else 0)
