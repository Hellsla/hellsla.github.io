"""Front page, module pages and language links of the built site (teacher 2026-10-29, "etusivu ja moduulinavigaatio").
Usage: python scripts/test_home.py [site]

For every language, from the pages that are actually in site/ (so nothing here hardcodes a publication count):
  - the catalogue lists exactly the modules with a published lesson in that language, the rest are under Tulossa,
    and each row says how many lessons are available in words that match the files (one/other forms, no bars)
  - every catalogue row has exactly one link, to its module page, whose lesson links all resolve: a published
    lesson is two clicks from the front page
  - the sample lesson is published in that language and the opening's "try a lesson" link goes to it
  - the six stages are shown with the names the lessons use, the <title> does not repeat the site's name
  - every language link resolves, and a link to a page the other language has not published goes to that
    language's module page, to a note that exists there
Then in a browser, at 360, 390, 768, 1440 and 1920 px: no horizontal scroll, the header on one row, module titles
not cut, header and catalogue targets at least 44 px, and at 390 x 844 the module list starts in the first screen.
Exit status 1 on any failure."""
import json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n

SITE = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "site")
curriculum = {k: v for k, v in json.loads((ROOT / "curriculum.json").read_text()).items() if not k.startswith("_")}
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


for lang in i18n.languages():
    T = i18n.T(lang); out = SITE if lang == i18n.SOURCE else SITE / lang
    home = (out / "index.html").read_text()
    published = {p.stem for p in out.glob("*.html")}
    live = [c for c, m in curriculum.items() if any(l["id"] in published for l in m["lessons"])]
    rows = re.findall(r'<li class="mod-row">(.*?)</li>', home, re.S)
    codes = [re.search(r'<span class="mod-code">(\w+)</span>', r).group(1) for r in rows]
    expect(f"{lang}: the catalogue lists the modules with published lessons, in order", codes == live, f"{codes} != {live}")
    upcoming = re.search(r'<ul class="up-list">(.*?)</ul>', home, re.S)
    up = re.findall(r'href="(\w+)\.html"', upcoming.group(1)) if upcoming else []
    expect(f"{lang}: the other modules are under Tulossa, linked to their pages", up == [c for c in curriculum if c not in live], up)
    for code, r in zip(codes, rows):
        slots = curriculum[code]["lessons"]; done = sum(l["id"] in published for l in slots)
        links = re.findall(r'<a [^>]*href="([^"]*)"', r)
        expect(f"{lang} {code}: one link per row, to its module page", links == [f"{code}.html"], links)
        want = T.count("site.lessons_all", done) if done == len(slots) else T.count("site.lessons_available", done)
        expect(f"{lang} {code}: availability '{want}' matches the published pages", f'<span class="mod-avail">{want}</span>' in r, r[:300])
        if done < len(slots):
            expect(f"{lang} {code}: the lessons still coming are said", T.count("site.lessons_coming", len(slots) - done) in r)
        mod = (out / f"{code}.html").read_text()
        hrefs = re.findall(r'<li class="live[^"]*">.*?<a href="([^"]+)"', mod)
        expect(f"{lang} {code}: the module page links {done} lessons, each published (two clicks)",
               len([h for h in hrefs if not h.endswith("-sovella.html")]) == done and all((out / h).is_file() for h in hrefs), hrefs)
        expect(f"{lang} {code}: lessons before the goals, goals behind a disclosure",
               mod.find('class="lessons"') < mod.find('class="goals"') or 'class="goals"' not in mod)
    for bad in ('class="bar"', 'class="card', "1 oppituntia", "1 lessons", "1 tehtävää", "1 pistettä"):
        expect(f"{lang}: front page has no {bad!r}", not re.search(r"(?<![\d])" + re.escape(bad), home))   # "11 lessons" is fine
    title = re.search(r"<title>(.*?)</title>", home).group(1)
    expect(f"{lang}: the front page title names the site once", _h.unescape(title).count(T("site.name")) == 1, title)
    feat = re.search(r'class="featured-link" href="([^"]+)"', home); sample = re.search(r'class="quiet-link" href="([^"]+)"', home)
    expect(f"{lang}: the sample lesson is published and the opening links to it",
           bool(feat and sample and feat.group(1) == sample.group(1) and (out / feat.group(1)).is_file()), (feat and feat.group(1), sample and sample.group(1)))
    stages = re.findall(r"<li><strong>(.*?)</strong>", re.search(r'<ol class="path-steps">(.*?)</ol>', home, re.S).group(1))
    expect(f"{lang}: the six stages with the lessons' names", stages == [T("inquiry.stage_" + k) for k in ["herata", "ennusta", "tutki", "selita", "sovella", "tarkista"]], stages)
    bad_links = []
    for f in out.glob("*.html"):
        for href in re.findall(r'<a class="lang" href="([^"]+)"', f.read_text()):
            target, _, frag = href.partition("#"); t = (f.parent / target).resolve()
            if not t.is_file() or (frag and f'id="{frag}"' not in t.read_text()): bad_links.append(f"{f.name} -> {href}")
            elif not frag and t.name != f.name: bad_links.append(f"{f.name} -> {href} (another page without a note)")
    expect(f"{lang}: every language link resolves (a missing page to the module page's note)", not bad_links, bad_links[:5])

JS = """() => { const R = (e) => e.getBoundingClientRect(), out = [];
  if (document.scrollingElement.scrollWidth > innerWidth) out.push('horizontal scroll ' + document.scrollingElement.scrollWidth);
  const h = document.querySelector('header.top'), kids = [...h.children].map(R);
  if (Math.max(...kids.map((r) => r.top)) - Math.min(...kids.map((r) => r.top)) > 20) out.push('header wraps');
  for (const e of document.querySelectorAll('.mod-title, .up-title')) if (e.scrollWidth > e.clientWidth + 1) out.push('cut: ' + e.textContent);
  for (const e of document.querySelectorAll('header.top a, header.top summary, a.button, a.quiet-link, .up-list a, details.more-tips > summary'))
    if (e.checkVisibility() && R(e).height < 43.5) out.push(`target ${Math.round(R(e).height)} px: ${e.textContent.trim().slice(0, 30)}`);
  for (const e of document.querySelectorAll('.mod-row')) if (R(e).height < 44) out.push('row under 44 px');
  return out; }"""
try:
    from playwright.sync_api import sync_playwright
    from _browser import launch
except ImportError:
    print("(no playwright: browser checks skipped)"); sys.exit(1 if fails else 0)
with sync_playwright() as pw:
    b = launch(pw)
    for lang in i18n.languages():
        base = SITE if lang == i18n.SOURCE else SITE / lang
        for w, hgt in ((360, 780), (390, 844), (768, 1024), (1440, 900), (1920, 1080)):
            for name in ("index.html", "FY4.html"):
                pg = b.new_page(viewport={"width": w, "height": hgt}); pg.goto((base / name).as_uri())
                pg.evaluate("document.fonts.ready.then(() => true)"); pg.wait_for_timeout(150)
                found = pg.evaluate(JS)
                expect(f"{lang}/{name} at {w} px: no sideways scroll, header on one row, titles whole, targets 44 px", not found, found)
                if name == "index.html" and w == 390:
                    top = pg.evaluate("document.querySelector('.mod-row').getBoundingClientRect().top")
                    expect(f"{lang}: at 390 x 844 the first module row starts in the first screen ({round(top)} px)", top < 844 - 60)
                pg.close()
    b.close()
sys.exit(1 if fails else 0)
