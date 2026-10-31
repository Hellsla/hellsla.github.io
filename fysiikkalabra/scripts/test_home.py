"""Front page, module pages and language links of the built site (teacher 2026-10-29, "etusivu ja moduulinavigaatio").
Usage: python scripts/test_home.py [site]

For every language, from the pages that are actually in site/ (so nothing here hardcodes a publication count):
  - the catalogue lists exactly the modules with a published lesson in that language, the rest are under Tulossa,
    and each row says how many lessons are available in words that match the files (one/other forms, no bars)
  - every catalogue row has exactly one link, to its module page, whose lesson links all resolve: a published
    lesson is two clicks from the front page
  - the page is a learning environment's front page, not a product page (teacher 2026-10-31): no sample lesson, no
    call-to-action buttons in the opening, the module catalogue right after the opening, and one study guide last
  - the six stages are shown with the names the lessons use, the <title> does not repeat the site's name
  - every language link resolves, and a link to a page the other language has not published goes to that
    language's module page, to a note that exists there
  - the course page's investigation bank (teacher 2026-10-31): every investigation with its topic, F/E levels and
    modes, the filter form hidden without scripts, and in a browser a search that hides all and "Näytä kaikki" that
    brings all back; the TVT-ohjeet it lists are published pages
  - Lukiokohtaiset opintojaksot (teacher 2026-10-30, local-courses.json): their own section right after the national
    modules and before Tulossa (2026-10-31), saying how many investigations this language publishes for the course
    (counted from the pages) apart from the course plan's status, one row and one link per course this language has, no
    local course among the national rows; its page names itself school-specific and says what is still planned,
    and links only chapters published in that language; a language without the course has the note
    #unavailable-<CODE> on its front page
Then in a browser, at 360, 390, 768, 1440 and 1920 px: no horizontal scroll, the header on one row, module titles
not cut, header and catalogue targets at least 44 px, and at 390 x 844 the module list starts in the first screen.
Exit status 1 on any failure."""
import json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n, investigations, local_courses

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
    expect(f"{lang}: no sample lesson and no call to action on the front page",
           not re.search(r'class="(featured[^"]*|actions|button|quiet-link)"', home), re.findall(r'class="(featured[^"]*|actions|button|quiet-link)"', home)[:3])
    intro_end = home.find("</section>", home.find('class="home-intro"'))
    expect(f"{lang}: the opening has no links and the catalogue follows it",
           "<a " not in home[home.find('class="home-intro"'):intro_end] and home.find('class="catalogue"') > intro_end)
    order = [home.find(f'class="{c}"') for c in ("catalogue", "local-courses", "upcoming", "path")]
    present = [i for i in order if i >= 0]
    expect(f"{lang}: modules, school-specific courses, Tulossa, study guide in that order", present == sorted(present) and order[0] >= 0 and order[3] >= 0, order)
    stages = re.findall(r"<li><strong>(.*?)</strong>", re.search(r'<ol class="path-steps">(.*?)</ol>', home, re.S).group(1))
    expect(f"{lang}: the six stages with the lessons' names", stages == [T("inquiry.stage_" + k) for k in ["herata", "ennusta", "tutki", "selita", "sovella", "tarkista"]], stages)
    local = local_courses.load(lang); everywhere = local_courses.load()
    sec = re.search(r'<section class="local-courses".*?</section>', home, re.S)
    if local:
        expect(f"{lang}: Lukiokohtaiset opintojaksot right after the national modules, before Tulossa",
               bool(sec) and home.find('class="catalogue"') < sec.start() < (home.find('class="upcoming"') % (len(home) + 1)),
               sec and sec.start())
        lrows = re.findall(r'<li class="mod-row local-row">(.*?)</li>', sec.group(0), re.S) if sec else []
        expect(f"{lang}: one row per local course, in registry order", [re.search(r'mod-code">(\w+)<', r).group(1) for r in lrows] == list(local), lrows)
        for code, r in zip(local, lrows):
            expect(f"{lang} {code}: one link per row, to its page", re.findall(r'<a [^>]*href="([^"]*)"', r) == [f"{code}.html"])
            n_inv = sum(1 for i in investigations.ids(lang) if (out / f"{i}.html").is_file() and code in investigations.load(i, lang)["courses"])
            want = T.count("site.local_investigations", n_inv) if n_inv else T("site.local_status_" + local[code]["status"])
            expect(f"{lang} {code}: the row says what is published ('{want}'), the plan's status apart", f'<span class="mod-avail">{want}</span>' in r, r[:400])
            pg = (out / f"{code}.html").read_text() if (out / f"{code}.html").is_file() else ""
            expect(f"{lang} {code}: the page exists, says it is school-specific and what is planned",
                   bool(pg) and 'class="notice local-kind"' in pg and 'class="notice local-status"' in pg and T("site.local_status_" + local[code]["status"]) in pg)
            prep = re.search(r'<ul class="local-prepare">(.*?)</ul>', pg, re.S)
            hrefs = re.findall(r'href="([^"]+)"', prep.group(1)) if prep else []
            expect(f"{lang} {code}: chapters to prepare with link only published pages ({len(hrefs)})", all((out / h).is_file() for h in hrefs), hrefs)
            expect(f"{lang} {code}: not a national module row", code not in codes)
            inv = re.search(r'<ol class="lessons local-inv">(.*?)</ol>', pg, re.S)
            ihrefs = re.findall(r'href="([^"]+)"', inv.group(1)) if inv else []
            expect(f"{lang} {code}: listed investigations are published pages that name this course ({len(ihrefs)})",
                   all((out / h).is_file() and code in investigations.load(h[:-5], lang)["courses"] for h in ihrefs), ihrefs)
            if ihrefs:                   # the bank (teacher 2026-10-31): every item carries its filter data, the form starts hidden
                items = re.findall(r'<li class="live bank-item" data-topic="(\w+)" data-f="([F123 ]+)" data-e="([E123 ]+)" data-mode="([OI ]+)"', inv.group(1))
                expect(f"{lang} {code}: every investigation in the bank has topic, F, E and modes ({len(items)})", len(items) == len(ihrefs), len(items))
                expect(f"{lang} {code}: the filter form starts hidden (all shown without scripts)", '<form class="bank-filter" id="bank-filter" hidden' in pg)
            ghrefs = re.findall(r'href="(tvt-[\w-]+\.html)"', pg)
            expect(f"{lang} {code}: listed TVT-ohjeet are published pages ({len(ghrefs)})", all((out / h).is_file() for h in ghrefs), ghrefs)
    else: expect(f"{lang}: no local-course section without a course in this language", not sec)
    for code in everywhere:
        if code not in local: expect(f"{lang}: front page note for {code}, which this language lacks", f'id="unavailable-{code}"' in home)
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
  for (const e of document.querySelectorAll('header.top a, header.top summary, .up-list a, details.more-tips > summary'))
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
            for name in ("index.html", "FY4.html") + tuple(f"{c}.html" for c in local_courses.load(lang)):
                pg = b.new_page(viewport={"width": w, "height": hgt}); pg.goto((base / name).as_uri())
                pg.evaluate("document.fonts.ready.then(() => true)"); pg.wait_for_timeout(150)
                found = pg.evaluate(JS)
                expect(f"{lang}/{name} at {w} px: no sideways scroll, header on one row, titles whole, targets 44 px", not found, found)
                if name.startswith("FY10") and pg.query_selector("#bank-filter"):      # the bank filters in place, by keyboard too
                    total = pg.evaluate("document.querySelectorAll('.bank-item').length")
                    pg.focus("#bank-q"); pg.keyboard.type("zzzz-ei-ole")
                    hidden = pg.evaluate("[...document.querySelectorAll('.bank-item')].every(li => li.hidden) && !document.getElementById('bank-none').hidden")
                    pg.keyboard.press("Tab"); pg.keyboard.press("ArrowDown")      # topic select by keyboard: the first topic
                    pg.click(".bank-reset"); pg.wait_for_timeout(30)
                    back = pg.evaluate("document.querySelectorAll('.bank-item:not([hidden])').length")
                    expect(f"{lang}/{name} at {w} px: the bank filters without reloading and 'show all' brings all {total} back", hidden and back == total, (hidden, back))
                if name == "index.html" and w == 390:
                    top = pg.evaluate("document.querySelector('.mod-row').getBoundingClientRect().top")
                    expect(f"{lang}: at 390 x 844 the first module row starts in the first screen ({round(top)} px)", top < 844 - 60)
                pg.close()
    b.close()
sys.exit(1 if fails else 0)
