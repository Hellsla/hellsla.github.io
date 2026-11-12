"""Design audit 2026-11-10, P0: the menu on a phone, the skip link, the named self-assessment levels and Jatka
(templates/page.html, lesson.html, site.css, jatka.js, lesson.js). Needs a built site/ (python scripts/build.py).

  python scripts/test_jatka.py

- At 390 px the header's links are gone and one Valikko button opens them all; at 1440 px the links show and the
  button is gone. The first Tab stop of a page is Siirry sisältöön, and it points at <main id="sisalto">.
- A lesson's self-assessment row shows a short name on every level before any choice; a choice shows its sentence.
- Reloading keeps the chosen level, the row and the marks, and closes the menu. A visit alone marks no tile and
  records no stage; a record written before the change (no stage count) is read as started and never rewritten.
- The front page and a module page show no Jatka row and no tile state for a reader who has started nothing; after a
  chapter has been opened the front page and its module page show the row with a link to it, and a finished and a
  started chapter are marked on their tiles.
"""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
sys.path.insert(0, str(ROOT / "scripts"))
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += 0 if ok else 1


curriculum = json.loads((ROOT / "curriculum.json").read_text())
COURSE = next(c for c in ("FY5", "FY3", "FY1") if (SITE / f"{c}.html").exists())
ids = [l["id"] for l in curriculum[COURSE]["lessons"] if (SITE / f"{l['id']}.html").exists()]
assert len(ids) >= 4, "the test needs a module with four published chapters"
FIRST, SECOND, THIRD, OPEN = ids[:4]

try:
    from playwright.sync_api import sync_playwright
    from _browser import launch
except ImportError:
    print("(no playwright: browser checks skipped)"); sys.exit(0)
with sync_playwright() as pw:
    b = launch(pw)
    # 1. the menu and the skip link
    for name in ("index.html", f"{COURSE}.html", f"{OPEN}.html", "en/index.html"):
        if not (SITE / name).exists(): continue
        pg = b.new_page(viewport={"width": 390, "height": 844}); pg.goto((SITE / name).as_uri())
        shown = pg.evaluate("[...document.querySelectorAll('header.top nav > a')].filter(a => a.offsetParent).length")
        expect(f"{name} at 390 px: no loose header links, one menu button", shown == 0 and pg.is_visible(".nav-menu > summary") and pg.evaluate("(() => { const r = document.querySelector('.nav-menu > summary').getBoundingClientRect(); return r.width >= 44 && r.height >= 44 && document.querySelector('.nav-menu-t').textContent.trim().length > 2; })()"), shown)
        pg.click(".nav-menu > summary")
        links = pg.evaluate("[...document.querySelectorAll('.nav-menu[open] .nav-list a')].filter(a => a.offsetParent && a.getBoundingClientRect().height >= 44).map(a => a.getAttribute('href'))")
        want = ["index.html#moduulit", "nain-opiskelet.html", "lukuvinkit.html", "vihkot.html", "tyokalut.html", "tietoa.html"]   # Opettajalle joined the menu 2026-11-11 (audit finding 15)
        expect(f"{name} at 390 px: the menu opens Moduulit, Näin opiskelet, Kirjavinkit, Vihkot, Opettajalle, Sivustosta (44 px rows)", [l.split("/")[-1] for l in links] == want, links)
        over = pg.evaluate("document.documentElement.scrollWidth > innerWidth")
        expect(f"{name} at 390 px: the open menu causes no sideways scroll", not over)
        pg.reload(); pg.wait_for_timeout(100)
        expect(f"{name} at 390 px: after a reload the menu is closed and opens again", not pg.is_visible(".nav-list") and (pg.click(".nav-menu > summary") or pg.is_visible(".nav-list")))
        missing = [l for l in links if not (SITE / name).parent.joinpath(l.split("#")[0]).resolve().exists()]
        expect(f"{name}: every menu link leads to a page", not missing, missing)
        pg.close()
        pg = b.new_page(viewport={"width": 1440, "height": 900}); pg.goto((SITE / name).as_uri())
        expect(f"{name} at 1440 px: the links show, the menu button does not", not pg.is_visible(".nav-menu > summary") and pg.is_visible("header.top nav > a.nav-study") and pg.is_visible("header.top nav > a.nav-teacher"))
        for w in (927, 928):   # the limit where the links give way to the button (site.css, 58rem): on both sides the header is one row
            pg.set_viewport_size({"width": w, "height": 900}); pg.wait_for_timeout(150)
            row = pg.evaluate("(() => { const h = document.querySelector('header.top'), n = h.querySelector('nav'), v = [...n.children].filter(c => c.getBoundingClientRect().width > 0); return [new Set(v.map(c => Math.round(c.getBoundingClientRect().top))).size, Math.abs(n.getBoundingClientRect().top - h.querySelector('.brand').getBoundingClientRect().top) < 30, document.documentElement.scrollWidth <= innerWidth, !!n.querySelector('a.nav-teacher') && n.querySelector('a.nav-teacher').getBoundingClientRect().width > 0]; })()")
            expect(f"{name} at {w} px: the header is one row, {'links' if w == 928 else 'the menu button'}", row[0] == 1 and row[1] and row[2] and row[3] == (w == 928), row)
        for w, px in ((1599, 16), (1760, 17.41), (1920, 18.82), (2560, 18.82)):   # a wide screen reads from the back of the classroom (site.css, 2026-11-11): the root size grows from 1600 px, 17 px text is 20 px at 1920 px and no larger beyond
            pg.set_viewport_size({"width": w, "height": 1000}); pg.wait_for_timeout(150)
            got = pg.evaluate("[parseFloat(getComputedStyle(document.documentElement).fontSize), document.documentElement.scrollWidth <= innerWidth, Math.round(document.querySelector('.page').getBoundingClientRect().width)]")
            expect(f"{name} at {w} px: root size {px} px, the page 80rem wide, no sideways scroll", abs(got[0] - px) < 0.06 and got[1] and abs(got[2] - min(80 * got[0], w - 32)) < 2, got)
        pg.set_viewport_size({"width": 1440, "height": 900})
        pg.keyboard.press("Tab")
        first = pg.evaluate("(() => { const a = document.activeElement; const r = a.getBoundingClientRect(); return [a.className, a.getAttribute('href'), r.top >= 0 && r.height > 20, !!document.querySelector('main#sisalto')]; })()")
        expect(f"{name}: the first Tab stop is the skip link, in view, to the main content", first == ["skip", "#sisalto", True, True], first)
        pg.close()
    # 1b. no page built from the lesson template scrolls sideways on a phone, closed or with its stage list open: the long
    # section names of an investigation or a guide go on the stage button (2026-11-10)
    kinds = [n for n in (f"{OPEN}.html", "fy10-heiluri.html", "tvt-kuvaaja.html", f"{COURSE}-koe.html", f"{COURSE}-sovella.html", "en/fy14-plasma.html", f"fi-easy/{OPEN}.html") if (SITE / n).exists()]
    for name in kinds:
        for w in (320, 360):
            pg = b.new_page(viewport={"width": w, "height": 780}); pg.goto((SITE / name).as_uri()); pg.wait_for_timeout(300)
            closed = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
            opened = None
            if pg.is_visible(".toc-now"):
                pg.click(".toc-now"); pg.wait_for_timeout(100); opened = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
            expect(f"{name} at {w} px: no sideways scroll, with the stage list closed and open", closed <= 0 and (opened is None or opened <= 0), (closed, opened))
            if opened is not None:      # the closed bar stays one row high whatever stage is on screen, so a heading scrolled to is not under it
                pg.keyboard.press("Escape")
                tall = pg.evaluate("""async () => { const n = document.querySelector('nav.toc'), out = [];
                    for (const a of n.querySelectorAll('a[href^="#"]')) { const t = document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))); if (!t) continue;
                      t.scrollIntoView(); await new Promise((f) => setTimeout(f, 250)); const h = Math.round(n.getBoundingClientRect().height);
                      const head = t.matches('h1,h2,h3') ? t : t.querySelector('h2,h3'); const under = head ? Math.round(n.getBoundingClientRect().bottom - head.getBoundingClientRect().top) : 0;
                      if (h > 64 || under > 2) out.push([a.getAttribute('href'), h, under]); }
                    return out; }""")
                expect(f"{name} at {w} px: at every stage the bar is one row high and the stage's heading is not under it", not tall, tall)
            pg.close()
    # 2. the self-assessment levels by name
    pg = b.new_page(viewport={"width": 390, "height": 844}); pg.goto((SITE / f"{OPEN}.html").as_uri()); pg.wait_for_timeout(300)
    names = pg.evaluate("""(() => { const fs = document.querySelector('fieldset.sa-rate'); if (!fs) return null;
      return [...fs.querySelectorAll('.sa-opt')].map(o => [o.dataset.level, o.querySelector('.sa-sw').textContent.trim(), getComputedStyle(o.querySelector('.sa-sw')).backgroundColor]); })()""")
    expect("a self-assessment row names all five levels before any choice", bool(names) and [n[0] for n in names] == ["d", "c", "b", "a", "x"] and all(len(n[1]) > 3 for n in names), names)
    expect("no level is coloured before it is chosen", bool(names) and len({n[2] for n in names}) == 1, names)
    if names:
        pg.click("fieldset.sa-rate .sa-opt[data-level=c]"); pg.wait_for_timeout(400)
        got = pg.evaluate("(() => { const fs = document.querySelector('fieldset.sa-rate'); return [fs.querySelector('.sa-desc').textContent.trim().length > 10, getComputedStyle(fs.querySelector('.sa-opt[data-level=c] .sa-sw')).backgroundColor !== getComputedStyle(fs.querySelector('.sa-opt[data-level=b] .sa-sw')).backgroundColor, document.documentElement.scrollWidth > innerWidth]; })()")
        expect("the chosen level shows its sentence and its colour, with no sideways scroll at 390 px", got == [True, True, False], got)
        pg.reload(); pg.wait_for_timeout(500)
        back = pg.evaluate("(() => { const fs = document.querySelector('fieldset.sa-rate'); const c = fs.querySelector('input:checked'); return [c && c.value, fs.querySelector('.sa-desc').textContent.trim().length > 10]; })()")
        expect("after a reload the chosen level is still chosen, with its sentence", back == ["c", True], back)
    pg.close()
    # 3. Jatka
    ctx = b.new_context(viewport={"width": 1440, "height": 900})
    pg = ctx.new_page()
    for name in ("index.html", f"{COURSE}.html"):
        pg.goto((SITE / name).as_uri()); pg.wait_for_timeout(150)
        quiet = pg.evaluate("document.getElementById('jatka') && document.getElementById('jatka').hidden && !document.querySelector('.ch-state')")
        expect(f"{name}: no Jatka row and no tile state before a chapter is started", quiet is True, quiet)
    pg.goto((SITE / f"{OPEN}.html").as_uri()); pg.wait_for_timeout(600)
    last = pg.evaluate("JSON.parse(localStorage.getItem('ruukkilabra:viimeisin') || 'null')")
    expect("opening a chapter records it as the last one, with its stage", bool(last) and last.get("file") == f"{OPEN}.html" and last.get("n") == 1 and last.get("of", 0) >= 3 and COURSE in last.get("num", ""), last)
    of = (last or {}).get("of", 7)
    pg.goto((SITE / f"{COURSE}.html").as_uri()); pg.wait_for_timeout(150)
    visit = pg.evaluate("[document.getElementById('jatka').hidden, document.querySelectorAll('.ch-state').length, localStorage.getItem('ruukkilabra:%s')]" % OPEN)
    expect("a visit alone is not progress: the row offers the chapter, but no tile is marked and no stage is recorded", visit == [False, 0, None], visit)
    # a record written before 2026-11-10 has no stage count: it is read as it is, shown as started, and left untouched
    old = json.dumps({"done": ["herata"], "answered": ["herata:0"]})
    pg.evaluate("([k, v]) => localStorage.setItem('ruukkilabra:' + k, v)", [SECOND, old]); pg.reload(); pg.wait_for_timeout(150)
    got = pg.evaluate("""(f) => { const a = document.querySelector('ol.ch-cards a[href="' + f + '.html"]'); const s = a.closest('.ch-box').querySelector('.ch-state'); return [s && s.textContent, s && s.classList.contains('is-done'), localStorage.getItem('ruukkilabra:' + f)]; }""", SECOND)
    expect("an older record without a stage count shows as started, never as finished, and is not rewritten", bool(got[0]) and "/" not in got[0] and got[1] is False and got[2] == old, got)
    pg.goto((SITE / f"{SECOND}.html").as_uri()); pg.wait_for_timeout(600)
    kept = pg.evaluate("JSON.parse(localStorage.getItem('ruukkilabra:%s'))" % SECOND)
    expect("opening that chapter keeps its done stages and answers", kept.get("done") == ["herata"] and kept.get("answered") == ["herata:0"], kept)
    pg.evaluate("([k, last]) => { localStorage.removeItem('ruukkilabra:' + k); localStorage.setItem('ruukkilabra:viimeisin', JSON.stringify(last)); }", [SECOND, last])
    pg.evaluate("""([a, b, of]) => { localStorage.setItem('ruukkilabra:' + a, JSON.stringify({ done: Array.from({ length: of }, (x, i) => 's' + i), answered: [], of }));
      localStorage.setItem('ruukkilabra:' + b, JSON.stringify({ done: ['s0', 's1'], answered: [], of })); }""", [FIRST, THIRD, of])
    pg.goto((SITE / "index.html").as_uri()); pg.wait_for_timeout(150)
    row = pg.evaluate("(() => { const b = document.getElementById('jatka'); return [b.hidden, (b.querySelector('a') || {}).getAttribute?.('href'), b.textContent]; })()")
    expect("the front page: Jatka leads to the chapter opened last", row[0] is False and row[1] == f"{OPEN}.html" and COURSE in row[2], row)
    pg.goto((SITE / f"{COURSE}.html").as_uri()); pg.wait_for_timeout(150)
    mod = pg.evaluate("""(() => { const b = document.getElementById('jatka'); const st = (f) => { const a = document.querySelector('ol.ch-cards a[href="' + f + '"]'); const s = a && a.closest('.ch-box').querySelector('.ch-state'); return s ? s.textContent : null; };
      return { hidden: b.hidden, href: (b.querySelector('a') || {}).getAttribute?.('href'), states: %s.map(st), over: document.documentElement.scrollWidth > innerWidth }; })()""" % json.dumps([f"{x}.html" for x in (FIRST, SECOND, THIRD)]))
    expect("the module page: Jatka leads to the chapter opened last", mod["hidden"] is False and mod["href"] == f"{OPEN}.html", mod)
    pg.evaluate("(c) => localStorage.setItem('ruukkilabra:' + c + '-koe', JSON.stringify({ done: ['osa-1'], answered: [], of: 3 }))", COURSE)
    pg.reload(); pg.wait_for_timeout(150)
    again = pg.evaluate("[document.getElementById('jatka').hidden, document.querySelector('#jatka a').getAttribute('href'), document.querySelectorAll('.ch-state').length, document.querySelectorAll('#jatka a').length]")
    expect("after a reload the row and the tile marks are the same, drawn once", again == [False, f"{OPEN}.html", 2, 1], again)
    expect("the module's end tiles (exam, challenge tasks, goals) are never marked as chapters", pg.evaluate("!document.querySelector('.me-tile .ch-state')"))
    expect("the module page: a finished chapter and a started one are marked, an unopened one is not",
           bool(mod["states"][0]) and mod["states"][1] is None and bool(mod["states"][2]) and f"2/{of}" in mod["states"][2] and mod["states"][0] != mod["states"][2] and not mod["over"], mod)
    pg.evaluate("localStorage.removeItem('ruukkilabra:viimeisin')"); pg.reload(); pg.wait_for_timeout(150)
    href = pg.evaluate("(document.querySelector('#jatka a') || {}).getAttribute?.('href')")
    expect("without a last chapter the row offers the first unfinished started chapter", href == f"{THIRD}.html", href)
    pg.set_viewport_size({"width": 390, "height": 844}); pg.wait_for_timeout(100)
    expect("the module page with Jatka at 390 px: no sideways scroll, a 44 px link", pg.evaluate("document.documentElement.scrollWidth <= innerWidth && document.querySelector('#jatka a').getBoundingClientRect().height >= 44"))
    b.close()
print("\n" + ("all passed" if not fails else f"{fails} failed")); sys.exit(1 if fails else 0)
