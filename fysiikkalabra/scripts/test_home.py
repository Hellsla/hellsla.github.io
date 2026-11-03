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
  - Käsitetakomo (teacher 2026-11-03, scripts/concept_cards.py): the card data is valid; the front page has no card
    link (compact front page); a module page with cards has "Kertauspakkasi"; exactly the chapters with cards have "Kertaa luvun
    käsitteet" after the exit ticket (a definition list without JavaScript) and its "Käsitteet" stage; card terms are
    marked only in Teoriatiivistelmä; in a browser the card turns by keyboard, the marks go to localStorage
    ruukkilabra:kortit (three "Osasin" in a row leave the deck), the popover closes with Esc, the deck shows on the
    module and Sovella pages, and kasitteet.html reads its parameters (old ?kurssi= too)
Then in a browser, at 360, 390, 768, 1440 and 1920 px: no horizontal scroll, the header on one row, module titles
not cut, header and catalogue targets at least 44 px, and at 390 x 844 the module list starts in the first screen.
Exit status 1 on any failure."""
import json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n, investigations, local_courses, units

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
        hrefs = [h for h in re.findall(r'<li class="live[^"]*">.*?<a href="([^"]+)"', mod) if "kasitteet.html" not in h]   # the card links: below
        expect(f"{lang} {code}: the module page links {done} lessons, each published (two clicks)",
               len([h for h in hrefs if not h.endswith("-sovella.html")]) == done and all((out / h).is_file() for h in hrefs), hrefs)
        cards = re.findall(r'<li class="live ch-card">(.*?)</li>', mod, re.S)   # chapter cards (teacher 2026-11-03, "Ruukkikortit")
        expect(f"{lang} {code}: every published chapter is a card with one link, its opening illustration and its Miksi question",
               len(cards) == done and all(len(re.findall(r"<a ", c)) == 1 and 'class="ch-img"><svg aria-hidden="true"' in c and 'class="ch-why"' in c for c in cards),
               [re.findall(r'href="([^"]+)"', c)[:1] for c in cards if 'class="ch-why"' not in c or "ch-img" not in c][:3])
        themes = [t["first"] for t in curriculum[code].get("themes", [])]
        expect(f"{lang} {code}: the chapters are under the module's {len(themes)} themes", mod.count('class="ch-theme"') == len(themes))
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
            n_units = sum(1 for ul, u in units.all_units() if units.load(u, ul).get("course") == code and (SITE / ("" if ul == "fi" else ul) / f"{u}.html").is_file())   # course units, built only for their own language (scripts/units.py)
            want = (T.count("site.local_investigations", n_inv) if n_inv else T("units.home_sessions", n=local[code]["sessions"]) if n_units and local[code].get("sessions")
                    else T.count("units.home_count", n_units) if n_units else T("site.local_status_" + local[code]["status"]))
            expect(f"{lang} {code}: the row says what is published ('{want}'), the plan's status apart", f'<span class="mod-avail">{want}</span>' in r, r[:400])
            pg = (out / f"{code}.html").read_text() if (out / f"{code}.html").is_file() else ""
            expect(f"{lang} {code}: the page exists, says it is school-specific and what is planned",
                   bool(pg) and 'class="notice local-kind"' in pg and (('class="notice local-status"' not in pg) if local[code]["status"] == "ready" else ('class="notice local-status"' in pg and T("site.local_status_" + local[code]["status"]) in pg)))
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
    # module icons (teacher 2026-10-31, scripts/module_icons.py): every row of the catalogue, the school-specific courses
    # and Tulossa starts with its own module's icon, decorative (alt="", the name is text beside it); the module's own
    # page shows it beside the title; the file resolves from this language's folder; never on a chapter page
    def icon_of(chunk):
        m = re.search(r'<img class="(?:mod-icon|up-icon|mod-head-icon)" src="([^"]+)" alt="" width="\d+" height="\d+" aria-hidden="true">', chunk)
        return m.group(1) if m else None
    up_items = re.findall(r"<li>(<a href=\"\w+\.html\">.*?)</li>", upcoming.group(1), re.S) if upcoming else []
    all_rows = list(zip(codes, rows)) + list(zip(local, re.findall(r'<li class="mod-row local-row">(.*?)</li>', home, re.S))) + list(zip(up, up_items))
    for code, r in all_rows:
        src = icon_of(r)
        expect(f"{lang} {code}: the row starts with its own decorative icon", src is not None and r.lstrip().startswith(("<img", '<a href="' + code + '.html"><img'))
               and src.endswith(f"module-icons/{code.lower()}.svg") and (out / src).resolve().is_file(), (src, r[:160]))
        page_html = (out / f"{code}.html").read_text()
        psrc = icon_of(page_html[page_html.find("<main"):])
        expect(f"{lang} {code}: the module page shows the same icon beside its title", psrc == src and page_html.find("mod-head-icon") < page_html.find("<h1"), psrc)
    expect(f"{lang}: icons are counted once each (9 modules, no stray icons)", len(re.findall(r'class="(?:mod-icon|up-icon)"', home)) == len(all_rows), len(all_rows))
    expect(f"{lang}: no icon has alternative text (the name is already said)", not re.search(r'<img class="(?:mod-icon|up-icon|mod-head-icon)"[^>]*alt="[^"]', home))
    lesson_pages = [f for f in out.glob("fy*-*.html")]
    expect(f"{lang}: no module icon on a chapter page ({len(lesson_pages)})", not any("module-icons/" in f.read_text() for f in lesson_pages))
    for gone in ("Kokeile oppituntia", "Esimerkkioppitunti", "Try a lesson", "Sample lesson"):
        expect(f"{lang}: {gone!r} stays off the front page", gone not in home)
    bad_links = []
    for f in out.glob("*.html"):
        for href in re.findall(r'<a class="lang" href="([^"]+)"', f.read_text()):
            target, _, frag = href.partition("#"); t = (f.parent / target).resolve()
            if not t.is_file() or (frag and f'id="{frag}"' not in t.read_text()): bad_links.append(f"{f.name} -> {href}")
            elif not frag and t.name != f.name: bad_links.append(f"{f.name} -> {href} (another page without a note)")
    expect(f"{lang}: every language link resolves (a missing page to the module page's note)", not bad_links, bad_links[:5])


# Lukuvinkit (teacher 2026-11-03, scripts/reading_tips.py): every book of content/fi/lukuvinkit.json in its order, the
# loan tag on exactly the books marked "loan", no subheading inside the list, each title a link to its record, and the
# page reachable from the header and footer of every page of every language.
import reading_tips
expect("content/<lang>/lukuvinkit.json are valid (reading_tips.py)", not reading_tips.check(), reading_tips.check())
for lang in i18n.languages():
    T = i18n.T(lang); out = SITE if lang == i18n.SOURCE else SITE / lang
    rp = (out / reading_tips.PAGE).read_text() if (out / reading_tips.PAGE).is_file() else ""
    want = reading_tips.load(lang)["books"]
    lst = re.search(r'<ol class="books">(.*?)</ol>', rp, re.S)
    items = re.findall(r'<li class="book">(.*?)</li>', lst.group(1), re.S) if lst else []
    titles = [_h.unescape(re.search(r'<h2 class="book-title"><a href="([^"]*)"[^>]*>(.*?)</a></h2>', i).group(2)) if '<h2 class="book-title">' in i else None for i in items]
    expect(f"{lang} {reading_tips.PAGE}: all {len(want)} books in the given order", titles == [b["title"] for b in want], titles)
    hrefs = [_h.unescape(re.search(r'<a href="([^"]*)"', i).group(1)) if "<a " in i else None for i in items]
    expect(f"{lang} {reading_tips.PAGE}: each title links to its record", hrefs == [b["url"] for b in want], hrefs)
    loan = [T("site.reading_loan") in _h.unescape(i) for i in items]
    expect(f"{lang} {reading_tips.PAGE}: the loan tag on exactly books {[n for n, b in enumerate(want, 1) if b['loan']]}", loan == [b["loan"] for b in want], loan)
    expect(f"{lang} {reading_tips.PAGE}: no subheadings inside the list", lst and len(re.findall(r"<h[1-6]", lst.group(1))) == len(items))
    expect(f"{lang} {reading_tips.PAGE}: author, language, level, description and courses for every book",
           all(_h.escape(b["author"]) in i and _h.escape(b["language"]) in i and _h.escape(b["level"]) in i and _h.escape(b["text"]) in i and _h.escape(b["courses"]) in i for b, i in zip(want, items)))
    no_link = [p.name for p in out.glob("*.html") if 'href="lukuvinkit.html"' not in re.search(r'<header class="top">.*?</header>', p.read_text(), re.S).group(0)
               or 'href="lukuvinkit.html"' not in re.search(r'<footer class="bottom">.*?</footer>', p.read_text(), re.S).group(0)]
    expect(f"{lang}: every page links to {reading_tips.PAGE} in its header and footer", not no_link, no_link[:10])

# Käsitetakomo (teacher 2026-11-03, scripts/concept_cards.py): the cards come to the chapter
import concept_cards
expect("the concept card data is valid (concept_cards.py check)", not concept_cards.errors(), concept_cards.errors()[:5])
for lang in i18n.languages():
    out = SITE if lang == i18n.SOURCE else SITE / lang
    has = bool(concept_cards.modules(concept_cards.data_lang(lang)))
    home = (out / "index.html").read_text()
    expect(f"{lang}: kasitteet.html exists exactly when the language has cards, and the front page has no card link (teacher 2026-11-03, compact front page)", 'kasitteet.html' not in home and (out / "kasitteet.html").is_file() == has)
    for code in curriculum:
        f = out / f"{code}.html"
        if not f.is_file(): continue
        want = bool(concept_cards.cards_of(code, lang))
        expect(f"{lang} {code}.html: {'Kertauspakkasi' if want else 'no deck (no cards in this language)'}", ('class="kc-deck"' in f.read_text()) == want)
    wrong = []
    for code, m in curriculum.items():
        for l in m["lessons"]:
            f = out / f"{l['id']}.html"
            if not f.is_file(): continue
            page = f.read_text(); cards = concept_cards.chapter_cards(code, l["id"], lang)
            if bool(cards) != ('id="kasitteet"' in page): wrong.append(f"{l['id']}: section {'missing' if cards else 'without cards'}"); continue
            if not cards: continue
            sec = re.search(r'<section class="stage stage-concepts kc-section" id="kasitteet".*?</section>', page, re.S).group(0)
            if not all(f'data-id="{c["id"]}"' in sec for c in cards): wrong.append(f"{l['id']}: a card missing from the list")
            ex = page.find('id="exercises"')
            if not (page.index('id="exit"') < page.index('id="kasitteet"') and (ex < 0 or page.index('id="kasitteet"') < ex)): wrong.append(f"{l['id']}: not after the exit ticket")
            toc = re.search(r'<nav class="toc".*?</nav>', page, re.S)
            if not toc or 'href="#kasitteet"' not in toc.group(0): wrong.append(f"{l['id']}: no Käsitteet stage in the navigation")
            sel = re.search(r'<section class="stage" id="selita".*?</section>', page, re.S)
            if page.count("data-kortti=") != (sel.group(0).count("data-kortti=") if sel else 0): wrong.append(f"{l['id']}: a card term outside Teoriatiivistelmä")
            if f'href="kasitteet.html?moduuli={code}"' not in sec: wrong.append(f"{l['id']}: no link to the module's cards")
    expect(f"{lang}: exactly the chapters with cards have 'Kertaa luvun käsitteet' after the exit ticket, listed, in the navigation, terms only in Teoriatiivistelmä", not wrong, wrong[:5])

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
            for name in ("index.html", "FY4.html", "lukuvinkit.html") + tuple(f"{c}.html" for c in local_courses.load(lang)):
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
    # the concept cards in a browser (kortit.js), over http so that Käsitetakomo can read site/kortit/*.json
    import functools, http.server, threading
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    URL = f"http://127.0.0.1:{srv.server_address[1]}/"
    lid = next((l["id"] for c in curriculum for l in curriculum[c]["lessons"] if (SITE / f"{l['id']}.html").is_file()
                and concept_cards.chapter_cards(c, l["id"], "fi") and 'data-kortti=' in (SITE / f"{l['id']}.html").read_text()), None)
    if lid:
        code = lid.split("-")[0].upper()
        ctx = b.new_context(viewport={"width": 1280, "height": 900}); pg = ctx.new_page(); pg.goto(URL + f"{lid}.html"); pg.wait_for_timeout(300)
        first = concept_cards.chapter_cards(code, lid, "fi")[0]["id"]
        st = lambda: pg.evaluate(f"(JSON.parse(localStorage.getItem('ruukkilabra:kortit') || '{{}}')['{first}'] || null)")
        card = f'#kasitteet .kc-card[data-id="{first}"]'
        pg.focus(card + " .kc-face"); pg.keyboard.press("Enter"); pg.wait_for_timeout(500)
        expect(f"{lid}: a card turns with Enter and says so (aria-expanded)", pg.get_attribute(card + " .kc-face", "aria-expanded") == "true")
        pg.click(card + " .kc-again")
        e = st(); expect(f"{lid}: 'Kertaa myöhemmin' puts the card in the deck (ruukkilabra:kortit)", bool(e) and e["tila"] == "kertaa" and e["osasinPutki"] == 0 and e["muokattu"] > 0, e)
        for i in range(3): pg.click(card + " .kc-good")
        e = st(); expect(f"{lid}: three 'Osasin' in a row take it out of the deck", bool(e) and e["tila"] == "osasin" and e["osasinPutki"] == 3, e)
        n = pg.evaluate("document.querySelectorAll('#kasitteet .kc-card').length")
        expect(f"{lid}: the row shows the chapter's cards, at most 8", n == min(8, len(concept_cards.chapter_cards(code, lid, "fi"))), n)
        term = "#selita .kc-term-btn >> nth=0"
        pg.locator(term).scroll_into_view_if_needed(); pg.click(term); pg.wait_for_timeout(50)
        opened = pg.evaluate("!!document.querySelector('.kc-pop') && document.querySelector('#selita .kc-term-btn').getAttribute('aria-expanded') === 'true'")
        pg.keyboard.press("Escape")
        closed = pg.evaluate("!document.querySelector('.kc-pop') && document.activeElement.classList.contains('kc-term-btn')")
        pg.click(term); pg.mouse.click(5, 300); out_click = pg.evaluate("!document.querySelector('.kc-pop')")
        expect(f"{lid}: a bold term opens its popover, Esc and a click outside close it", opened and closed and out_click, (opened, closed, out_click))
        pg.evaluate("localStorage.clear()")
        pg.locator(".kc-chips .kc-chip >> nth=0").scroll_into_view_if_needed(); pg.click(".kc-chips .kc-chip >> nth=0"); pg.click(".kc-pop .kc-add")
        added = pg.evaluate("Object.values(JSON.parse(localStorage.getItem('ruukkilabra:kortit') || '{}')).some(e => e.tila === 'kertaa')")
        expect(f"{lid}: a chip opens the popover and 'Lisää kertauspakkaan' adds the card", added)
        pg.goto(URL + f"{code}.html"); pg.wait_for_timeout(200)
        deck = pg.evaluate("[document.querySelector('.kc-deck-count')?.textContent || '', document.querySelector('.kc-deck a.kc-button')?.getAttribute('href') || '']")
        expect(f"{code}.html: Kertauspakkasi counts the deck and 'Kertaa nyt' opens it", bool(deck[0]) and deck[1] == f"kasitteet.html?moduuli={code}&pakka=oma", deck)
        pg.goto(URL + f"kasitteet.html?moduuli={code}&pakka=oma"); pg.wait_for_timeout(300)
        expect("Käsitetakomo: ?pakka=oma studies the student's own deck", pg.evaluate("document.querySelectorAll('.kc-study .kc-card').length === 1"))
        if (SITE / f"{code}-sovella.html").is_file():
            pg.goto(URL + f"{code}-sovella.html"); pg.wait_for_timeout(200)
            expect(f"{code}-sovella.html: 'Varmista käsitteet' shows the deck's cards", pg.evaluate("!document.querySelector('.kc-practice').hidden && document.querySelectorAll('.kc-practice .kc-card').length > 0"))
            pg.evaluate("localStorage.clear()"); pg.reload(); pg.wait_for_timeout(200)
            expect(f"{code}-sovella.html: an empty deck shows no section", pg.evaluate("document.querySelector('.kc-practice').hidden"))
        ctx.close()
        ctx = b.new_context(viewport={"width": 1280, "height": 900}); pg = ctx.new_page()
        pg.add_init_script("Storage.prototype.setItem = () => { throw new Error('blocked'); }; Storage.prototype.getItem = () => { throw new Error('blocked'); };")
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(URL + f"{lid}.html"); pg.wait_for_timeout(200)
        pg.click('#kasitteet .kc-face >> nth=0'); pg.wait_for_timeout(500); pg.click('#kasitteet .kc-again >> nth=0')
        expect(f"{lid}: a browser that refuses storage still turns and marks cards (try/catch)", not errs and pg.evaluate("document.querySelector('#kasitteet .kc-status').textContent.length > 0"), errs)
        ctx.close()
    pg = b.new_page(viewport={"width": 360, "height": 780})
    code = next(c for c in curriculum if concept_cards.cards_of(c, "fi"))
    m = concept_cards.module(code); topics = [a["id"] for a in m["aiheet"]][:2]
    for q, sel, what in ((f"?moduuli={code}&aihe={','.join(topics)}", ".kc-study .kc-card", "a topic link starts the combined topics' cards"),
                         (f"?kurssi={code}&aihe={topics[0]}", ".kc-study .kc-card", "an old ?kurssi= link still works"),
                         (f"?moduuli={code}", ".kc-topics", "a module link opens the topic menu"),
                         (f"?moduuli={code}&pakka=oma", ".kc-empty", "the own deck, empty, says how to fill it"),
                         ("?moduuli=FY99", ".kc-grid", "an unknown module goes to the module menu"),
                         (f"?moduuli={code}&aihe=ei-ole", ".kc-topics", "an unknown topic goes to the topic menu"),
                         ("?aihe=%3Cscript%3E", ".kc-grid", "a malformed topic goes to the module menu")):
        pg.goto(URL + "kasitteet.html" + q); pg.wait_for_timeout(250)
        expect(f"Käsitetakomo: {what}", pg.evaluate(f"!!document.querySelector('{sel}') && document.querySelector('.kc-static').hidden"), q)
    found = pg.evaluate(JS); expect("Käsitetakomo at 360 px: no sideways scroll, header on one row", not found, found)
    pg.close()
    srv.shutdown()
    b.close()
sys.exit(1 if fails else 0)
