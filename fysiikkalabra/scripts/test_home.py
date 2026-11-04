"""Front page, module pages and language links of the built site (teacher 2026-10-29, "etusivu ja moduulinavigaatio").
Usage: python scripts/test_home.py [site]

For every language, from the pages that are actually in site/ (so nothing here hardcodes a publication count):
  - the compact front page (teacher 2026-11-03, "tiivistä etusivu"): the heading and one line under it, then the
    module list in two columns; on the left the modules with a published lesson in that language (except those the
    teacher keeps under Tulossa, curriculum.json "_front_page"), on the right Tulossa (dimmed) and the school's own
    courses under the school's name; no counts, credits, required/optional, "Avaa moduuli →", Käsitetakomo or study
    guide there
  - every row is one link, to its module page, with icon, code, title and the Miksi question (whole in its title),
    the arrow hidden from screen readers; the module page's lesson links all resolve (two clicks to a lesson)
  - the <title>, og:title and description stay as they were; the header links Näin opiskelet (the study guide, now at
    the top of Lukuvinkit with the six stages under the lessons' names) and the footer Tietoa sivustosta, which has
    the portfolio link the front page no longer has
  - every language link resolves, and a link to a page the other language has not published goes to that
    language's module page, to a note that exists there
  - the course page's investigation bank (teacher 2026-10-31): every investigation with its topic, F/E levels and
    modes, the filter form hidden without scripts, and in a browser a search that hides all and "Näytä kaikki" that
    brings all back; the TVT-ohjeet it lists are published pages
  - Lukiokohtaiset opintojaksot (teacher 2026-10-30, local-courses.json): in the right column after Tulossa, one row
    and one link per course this language has, no local course among the national rows; its page names itself
    school-specific and says what is still planned,
    and links only chapters published in that language; a language without the course has the note
    #unavailable-<CODE> on its front page
  - Käsitetakomo (teacher 2026-11-03, scripts/concept_cards.py): the card data is valid; the front page has no card
    link (compact front page); a module page with cards has "Kertauspakkasi"; exactly the chapters with cards have "Kertaa luvun
    käsitteet" after the exit ticket (a definition list without JavaScript) and its "Käsitteet" stage; card terms are
    marked only in Teoriatiivistelmä; in a browser the card turns by keyboard, the marks go to localStorage
    ruukkilabra:kortit (three "Osasin" in a row leave the deck), the popover closes with Esc, the deck shows on the
    module and Sovella pages, and kasitteet.html reads its parameters (old ?kurssi= too)
Then in a browser, at 360, 390, 768, 1440 and 1920 px: no horizontal scroll, the header on one row, module titles
not cut, header and catalogue targets at least 44 px, and at 390 x 844 the module list starts in the first screen;
from 700 px two columns with rows at most 64 px and the question on one line, below it the whole question; the arrow
shows on hover only; at 1440 x 900 and 1920 x 1080 the whole front page fits without scrolling.
Exit status 1 on any failure."""
import json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n, investigations, local_courses, units

SITE = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "site")
curriculum = {k: v for k, v in json.loads((ROOT / "curriculum.json").read_text()).items() if not k.startswith("_")}
COMING = json.loads((ROOT / "curriculum.json").read_text()).get("_front_page", {}).get("coming", [])
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
    ROW = r'<li><a class="mod-row( coming)?" href="(\w+)\.html">(.*?)</a></li>'
    left = re.search(r'<div class="mod-cols"><ul class="mod-list">(.*?)</ul><div class="mod-side">', home, re.S)
    rows = re.findall(ROW, left.group(1), re.S) if left else []
    codes = [c for _, c, _ in rows]
    want_left = [c for c in live if c not in COMING]
    expect(f"{lang}: the left column lists the modules with published lessons, in order", codes == want_left and not any(d for d, _, _ in rows), f"{codes} != {want_left}")
    upcoming = re.search(r'<ul class="mod-list up-list">(.*?)</ul>', home, re.S)
    up_rows = re.findall(ROW, upcoming.group(1), re.S) if upcoming else []
    up = [c for _, c, _ in up_rows]
    expect(f"{lang}: the other modules are dimmed under Tulossa, linked to their pages", up == [c for c in curriculum if c not in want_left] and all(d for d, _, _ in up_rows), up)
    expect(f"{lang}: Tulossa and the school's courses in the right column, under small headings",
           bool(upcoming) and re.search(r'<div class="mod-side"><h3 class="mod-group">' + re.escape(T("site.upcoming")) + '</h3><ul class="mod-list up-list">', home) is not None)
    mods = {c: (r, curriculum[c]["title"]) for _, c, r in rows + up_rows}
    for li in re.findall(r"<li><a .*?</li>", home[home.find('class="mod-cols"'):], re.S):
        expect(f"{lang}: one link per row ({li[:40]})", len(re.findall(r"<a ", li)) == 1)
    for code, (r, _) in mods.items():
        q = T("site.module_question." + code)
        expect(f"{lang} {code}: the row has its icon, code, title and Miksi question (whole in title), the arrow hidden",
               f'<span class="mod-code">{code}</span>' in r and f'<span class="mod-q" title="{_h.escape(q)}">{_h.escape(q)}</span>' in r
               and '<span class="mod-go" aria-hidden="true">' in r and r.startswith("<img"), r[:300])
    for code in codes:
        slots = curriculum[code]["lessons"]; done = sum(l["id"] in published for l in slots)
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
    main_html = re.search(r"<main.*?</main>", home, re.S).group(0)
    for bad in ('class="bar"', 'class="card', 'class="mod-meta"', 'class="mod-avail"', 'class="mod-credits"', 'class="path"', 'class="concept-home"',
                'kasitetakomo.html', T("site.course_type_required"), T("site.course_type_optional"), "→</span></li>"):
        expect(f"{lang}: front page has no {bad!r}", bad not in main_html)
    expect(f"{lang}: no lesson counts on the front page", not re.search(r"\d+ (oppitunti|lesson|tutkimus|investigation)", main_html))
    title = re.search(r"<title>(.*?)</title>", home).group(1)
    expect(f"{lang}: the front page title is unchanged and names the site once", _h.unescape(title) == f'{T("site.name")} — {T("site.subtitle")}', title)
    expect(f"{lang}: og:title and description unchanged", f'<meta property="og:title" content="{_h.escape(T("site.home_title"))}">' in home
           and f'<meta name="description" content="{_h.escape(T("site.home_description"))}">' in home)
    expect(f"{lang}: no sample lesson and no call to action on the front page",
           not re.search(r'class="(featured[^"]*|actions|button|quiet-link)"', home), re.findall(r'class="(featured[^"]*|actions|button|quiet-link)"', home)[:3])
    intro = re.search(r'<section class="home-intro"[^>]*><h1 id="h-intro">(.*?)</h1><p class="lead">(.*?)</p></section>', home)
    expect(f"{lang}: the heading and one line under it, then the module list",
           bool(intro) and intro.group(1) == T("site.home_h1") and intro.group(2) == T("site.home_sub") and home.find('class="catalogue"') > intro.end())
    hdr = re.search(r'<header class="top">.*?</header>', home, re.S).group(0); ftr = re.search(r'<footer class="bottom">.*?</footer>', home, re.S).group(0)
    expect(f"{lang}: the header links Moduulit, Näin opiskelet and Lukuvinkit in that order",
           re.findall(r'<nav [^>]*><a class="nav-modules" href="index.html#moduulit">[^<]*</a><a class="nav-study" href="lukuvinkit.html#nain-opiskelet">([^<]*)</a><a class="nav-reading" href="lukuvinkit.html">', hdr) == [_h.escape(T("site.study"))], hdr[-400:])
    expect(f"{lang}: the footer links Lukuvinkit and Tietoa sivustosta, not the portfolio",
           'href="tietoa.html"' in ftr and 'href="lukuvinkit.html"' in ftr and T("site.back_to_portfolio") not in ftr and "../index.html" not in ftr, ftr)
    about = (out / "tietoa.html").read_text() if (out / "tietoa.html").is_file() else ""
    expect(f"{lang}: tietoa.html exists and links back to the portfolio", T("site.back_to_portfolio") in about and re.search(r'href="(\.\./)+index\.html"', about))
    rp = (out / "lukuvinkit.html").read_text()
    guide = re.search(r'<main[^>]*><section class="path" id="nain-opiskelet".*?</section>', rp, re.S)
    stages = re.findall(r"<li><strong>(.*?)</strong>", guide.group(0)) if guide else []
    expect(f"{lang}: the study guide opens Lukuvinkit with the six stages under the lessons' names and the more tips",
           stages == [T("inquiry.stage_" + k) for k in ["herata", "ennusta", "tutki", "selita", "sovella", "tarkista"]] and 'class="more-tips"' in guide.group(0), stages)
    local = local_courses.load(lang); everywhere = local_courses.load()
    sec = re.search(r'<ul class="mod-list local-list">(.*?)</ul>', home, re.S)
    if local:
        school = next(iter(local.values()))["school"]
        expect(f"{lang}: the school's courses under its name, after Tulossa",
               bool(sec) and f'<h3 class="mod-group">{_h.escape(school)}</h3><ul class="mod-list local-list">' in home and home.find('class="mod-list up-list"') < sec.start(), sec and sec.start())
        lrows = [r for d, c, r in re.findall(ROW, sec.group(1), re.S)] if sec else []
        lcodes = [c for d, c, r in re.findall(ROW, sec.group(1), re.S)] if sec else []
        expect(f"{lang}: one row per local course, in registry order", lcodes == list(local), lcodes)
        for code, r in zip(local, lrows):
            expect(f"{lang} {code}: the row has its subtitle as the question", f'title="{_h.escape(local[code]["subtitle"])}"' in r, r[:300])
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
    all_rows = [(c, r) for _, c, r in re.findall(ROW, home, re.S)]
    for code, r in all_rows:
        src = icon_of(r)
        expect(f"{lang} {code}: the row starts with its own decorative icon", src is not None and r.lstrip().startswith("<img")
               and src.endswith(f"module-icons/{code.lower()}.svg") and (out / src).resolve().is_file(), (src, r[:160]))
        page_html = (out / f"{code}.html").read_text()
        psrc = icon_of(page_html[page_html.find("<main"):])
        expect(f"{lang} {code}: the module page shows the same icon beside its title", psrc == src and page_html.find("mod-head-icon") < page_html.find("<h1"), psrc)
    expect(f"{lang}: icons are counted once each (one per row, no stray icons)", len(re.findall(r'class="(?:mod-icon|up-icon)"', home)) == len(all_rows), len(all_rows))
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
            if bool(cards) != ('id="kertaa-kasitteet"' in page): wrong.append(f"{l['id']}: section {'missing' if cards else 'without cards'}"); continue
            if not cards: continue
            sec = re.search(r'<section class="stage stage-concepts kc-section" id="kertaa-kasitteet".*?</section>', page, re.S).group(0)
            if not all(f'data-id="{c["id"]}"' in sec for c in cards): wrong.append(f"{l['id']}: a card missing from the list")
            ex = page.find('id="exercises"')
            if not (page.index('id="exit"') < page.index('id="kertaa-kasitteet"') and (ex < 0 or page.index('id="kertaa-kasitteet"') < ex)): wrong.append(f"{l['id']}: not after the exit ticket")
            toc = re.search(r'<nav class="toc".*?</nav>', page, re.S)
            if not toc or 'href="#kertaa-kasitteet"' not in toc.group(0): wrong.append(f"{l['id']}: no Käsitteet stage in the navigation")
            sel = re.search(r'<section class="stage" id="selita".*?</section>', page, re.S)
            if page.count("data-kortti=") != (sel.group(0).count("data-kortti=") if sel else 0): wrong.append(f"{l['id']}: a card term outside Teoriatiivistelmä")
            if f'href="kasitteet.html?moduuli={code}"' not in sec: wrong.append(f"{l['id']}: no link to the module's cards")
    expect(f"{lang}: exactly the chapters with cards have 'Kertaa luvun käsitteet' after the exit ticket, listed, in the navigation, terms only in Teoriatiivistelmä", not wrong, wrong[:5])

JS = """() => { const R = (e) => e.getBoundingClientRect(), out = [];
  if (document.scrollingElement.scrollWidth > innerWidth) out.push('horizontal scroll ' + document.scrollingElement.scrollWidth);
  const h = document.querySelector('header.top'), kids = [...h.children].map(R);
  if (Math.max(...kids.map((r) => r.top)) - Math.min(...kids.map((r) => r.top)) > 20) out.push('header wraps');
  for (const e of document.querySelectorAll('.mod-name')) if (e.scrollWidth > e.clientWidth + 1) out.push('cut: ' + e.textContent);
  for (const e of document.querySelectorAll('header.top a, header.top summary, .mod-list a, details.more-tips > summary'))
    if (e.checkVisibility() && R(e).height < 43.5) out.push(`target ${Math.round(R(e).height)} px: ${e.textContent.trim().slice(0, 30)}`);
  const cols = document.querySelector('.mod-cols');
  if (cols) {                      // the compact front page (teacher 2026-11-03)
    const two = innerWidth >= 700, n = getComputedStyle(cols).gridTemplateColumns.split(' ').length;
    if (n !== (two ? 2 : 1)) out.push(`${n} columns at ${innerWidth} px`);
    for (const e of document.querySelectorAll('.mod-row')) {
      const ht = R(e).height, q = e.querySelector('.mod-q'), go = e.querySelector('.mod-go');
      if (two && ht > 64.5) out.push(`row ${Math.round(ht)} px: ${e.getAttribute('href')}`);
      if (two && R(q).height > parseFloat(getComputedStyle(q).lineHeight) * 1.5) out.push('question on two lines: ' + e.getAttribute('href'));
      if (!two && q.scrollWidth > q.clientWidth + 1) out.push('question cut: ' + e.getAttribute('href'));
      if (getComputedStyle(go).opacity !== '0') out.push('arrow shown at rest: ' + e.getAttribute('href'));
    }
    for (const e of document.querySelectorAll('.mod-group')) if (R(e).height > 30) out.push(`group heading ${Math.round(R(e).height)} px`);
  }
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
            mix = ("yo-sekoitin.html",) if any(c.get("mixer") for c in local_courses.load().values()) else ()
            for name in ("index.html", "FY4.html", "lukuvinkit.html") + tuple(f"{c}.html" for c in local_courses.load(lang)) + mix:
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
                if name == "yo-sekoitin.html" and w == 390:     # the task mixer: filters in place, a random pick of three, reset
                    total = pg.evaluate("document.querySelectorAll('.bank-item').length")
                    pg.click("[data-random]"); pg.wait_for_timeout(30)
                    pick = pg.evaluate("document.querySelectorAll('.bank-item:not([hidden])').length")
                    pg.click("button[type=reset]"); pg.wait_for_timeout(30)
                    back = pg.evaluate("document.querySelectorAll('.bank-item:not([hidden])').length")
                    links = pg.evaluate("[...document.querySelectorAll('.bank-item a')].map(a => a.getAttribute('href'))")
                    missing = [h for h in links if not (base / h.split("#")[0]).is_file()]
                    expect(f"{lang}/yo-sekoitin at {w} px: {total} tasks, a random pick shows {min(3, total)}, 'show all' brings all back, every link reaches a page",
                           total > 0 and pick == min(3, total) and back == total and not missing, (total, pick, back, missing[:3]))
                if name == "index.html" and (w, hgt) in ((1440, 900), (1920, 1080)):
                    sh = pg.evaluate("document.scrollingElement.scrollHeight")
                    expect(f"{lang}: at {w} x {hgt} the whole front page fits without scrolling ({sh} px)", sh <= hgt)
                if name == "index.html" and w == 1440:   # hover: the row is tinted and its arrow shows; a Tulossa row is not tinted
                    pg.hover('.mod-list:not(.up-list) .mod-row'); pg.wait_for_timeout(50)
                    hov = pg.evaluate("(() => { const a = document.querySelector('.mod-list:not(.up-list) .mod-row'); return [getComputedStyle(a).backgroundColor, getComputedStyle(a.querySelector('.mod-go')).opacity]; })()")
                    pg.hover('.up-list .mod-row'); pg.wait_for_timeout(50)
                    dim = pg.evaluate("getComputedStyle(document.querySelector('.up-list .mod-row')).backgroundColor")
                    expect(f"{lang}: hover tints a row and shows its arrow; a Tulossa row stays untinted", hov[0] != "rgba(0, 0, 0, 0)" and hov[1] == "1" and dim == "rgba(0, 0, 0, 0)", (hov, dim))
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
        card = f'#kertaa-kasitteet .kc-card[data-id="{first}"]'
        pg.focus(card + " .kc-face"); pg.keyboard.press("Enter"); pg.wait_for_timeout(500)
        expect(f"{lid}: a card turns with Enter and says so (aria-expanded)", pg.get_attribute(card + " .kc-face", "aria-expanded") == "true")
        pg.click(card + " .kc-again")
        e = st(); expect(f"{lid}: 'Kertaa myöhemmin' puts the card in the deck (ruukkilabra:kortit)", bool(e) and e["tila"] == "kertaa" and e["osasinPutki"] == 0 and e["muokattu"] > 0, e)
        for i in range(3): pg.click(card + " .kc-good")
        e = st(); expect(f"{lid}: three 'Osasin' in a row take it out of the deck", bool(e) and e["tila"] == "osasin" and e["osasinPutki"] == 3, e)
        n = pg.evaluate("document.querySelectorAll('#kertaa-kasitteet .kc-card').length")
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
        pg.click('#kertaa-kasitteet .kc-face >> nth=0'); pg.wait_for_timeout(500); pg.click('#kertaa-kasitteet .kc-again >> nth=0')
        expect(f"{lid}: a browser that refuses storage still turns and marks cards (try/catch)", not errs and pg.evaluate("document.querySelector('#kertaa-kasitteet .kc-status').textContent.length > 0"), errs)
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
