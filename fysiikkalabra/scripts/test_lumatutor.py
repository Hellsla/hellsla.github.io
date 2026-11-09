"""LUMA-tutor's pages (teacher's brief 2026-11-09, scripts/lumatutor.py) in the built site/: every page in every language
that publishes the course, the part navigation marking the page, every internal link resolving to a built file and its
anchor, external links https and marked external, the workload adding up to 23 lessons and 1 725 minutes, five ready
workshops with all their parts and a participant section kept apart, the ideas marked as ideas, ten templates that can
be copied, downloaded and printed, nothing stored (no form, no browser storage), and in a browser the workshop filters
working, printing hiding the navigation, and no sideways scroll at 360, 768 and 1280 px.

  python scripts/test_lumatutor.py"""
import re, sys, pathlib, subprocess, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n, lumatutor, local_courses

SITE = ROOT / "site"
fails = []
def expect(name, ok, got=None):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f"  ({got!r})"[:300]))
    if not ok: fails.append(name)


PARTS = ("tavoitteet", "valineet", "valmistelut", "turvallisuus", "toteutus", "tausta", "kysymykset", "ongelmat", "eriyttaminen", "lopetus", "itsearviointi")
js = (ROOT / "templates" / "lumatutor.js").read_text()
expect("lumatutor.js stores nothing", not re.search(r"localStorage|sessionStorage|indexedDB|fetch\(|XMLHttpRequest|document\.cookie", js))
pages = []
for lang in i18n.languages():
    if lumatutor.CODE not in local_courses.load(lang): continue
    out = SITE if lang == i18n.SOURCE else SITE / lang
    d, ws = lumatutor.load(lang), lumatutor.workshops(lang)
    sections = lumatutor.section_pages(d)
    for name in lumatutor.all_pages(d, ws):
        f = out / name
        expect(f"{lang} {name}: built", f.is_file())
        if not f.is_file(): continue
        pages.append(f.relative_to(SITE).as_posix())
        html = f.read_text()
        main = html[html.find("<main"):html.find("</main>")]
        expect(f"{lang} {name}: in Kiviruukin lukio's theme", "kr-theme kr-team" in main[:200] and "ruukkilabra-symboli-kiviruukki.svg" in html)
        own = name in sections + [lumatutor.PAGE, lumatutor.TOOLS]
        current = f'<a href="{name}" aria-current="page"' if own else f'<a href="{lumatutor.section_of(d, "suunnittele")["page"]}" aria-current="true"'
        expect(f"{lang} {name}: the part navigation marks the page (a workshop marks Plan)", current in main)
        expect(f"{lang} {name}: no form and no browser storage", "<form" not in main and "localStorage" not in html)
        bad = []
        for href in re.findall(r'href="([^"]+)"', main):
            if href.startswith("data:"): continue
            if re.match(r"[a-z]+:", href):
                if not (href.startswith("https://") and re.search(rf'href="{re.escape(href)}" rel="external noopener"', main)): bad.append(href)
                continue
            path, _, frag = href.partition("#")
            target = (out / path).resolve() if path else f
            if not target.is_file() or (frag and f'id="{frag}"' not in target.read_text()): bad.append(href)
        expect(f"{lang} {name}: every link resolves (internal with its anchor, external https and marked)", not bad, bad)
    hub = (out / lumatutor.PAGE).read_text()
    expect(f"{lang}: five parts in the brief's order", [s["id"] for s in d["sections"]] == lumatutor.SECTION_IDS and all(f'href="{p}"' in hub for p in sections))
    expect(f"{lang}: the workload is 23 lessons and 1 725 minutes", sum(s["lessons"] for s in d["sections"]) == 23 and "1 725" in hub)
    expect(f"{lang}: six requirements and six assessment areas, pass/fail as a planning decision",
           len(d["hub"]["requirements"]) == 6 and len(d["hub"]["criteria"]) == 6 and local_courses.esc(d["ui"]["plan_badge"]) in hub)
    bank = (out / lumatutor.section_of(d, "suunnittele")["page"]).read_text()
    ready = [w for w in ws if w["status"] == "ready"]; ideas = [w for w in ws if w["status"] == "idea"]
    expect(f"{lang}: five ready workshops and five ideas in the bank", len(ready) >= 5 and len(ideas) >= 5
           and bank.count('class="lt-wcard lt-ready"') == len(ready) and bank.count('class="lt-wcard lt-idea-card"') == len(ideas))
    expect(f"{lang}: every idea is marked as an idea, not a ready workshop", bank.count(local_courses.esc(d["ui"]["status_idea"]) + "</span>") >= len(ideas))
    expect(f"{lang}: four filters (topic, audience, duration, equipment), hidden without the script",
           all(f'<select data-f="{k}"' in bank for k in ("topic", "audience", "duration", "equipment")) and '<div class="lt-filter" hidden' in bank)
    for w in ready:
        page = (out / lumatutor.ws_page(w["id"])).read_text()
        missing = [p for p in PARTS if f'id="{p}"' not in page]
        expect(f"{lang} {w['id']}: all the card's parts", not missing and 'class="lt-meta"' in page, missing)
        tutor, part = page.find('class="lt-side lt-tutor"'), page.find('id="osallistujille"')
        expect(f"{lang} {w['id']}: a printable participant section after the tutor's part", 0 < tutor < part and "lt-printable" in page[part - 80:part])
        expect(f"{lang} {w['id']}: three questions and no unfilled tokens", len(w["questions"]) == 3 and not re.search(r"\{(?:cipher|plain|shift|top|topplain|co2|co2diff|warmest|decade|decadediff):[^}]*\}|\{(?:cooler|retrieved)\}", page))
    tools = (out / lumatutor.TOOLS).read_text()
    tpl = d["tyokalut"]["templates"]
    expect(f"{lang}: ten templates, each copyable, downloadable and printable", len(tpl) == 10 and all(
        f'data-copy="lt-txt-{t["id"]}"' in tools and f'data-print="{t["id"]}"' in tools and f'download="{t["file"]}"' in tools for t in tpl))
    expect(f"{lang}: the observation template has the six questions", len(d["tutustu"]["observe"]) == 6 and len(d["toteuta"]["task"]) == 6 and len(d["arvioi"]["parts"]) == 6)
    climate = (out / lumatutor.ws_page("ilmastodata")).read_text()
    expect(f"{lang}: the climate data is downloadable and sourced", climate.count('href="data:text/csv') == 2 and "gml.noaa.gov" in climate and "data.giss.nasa.gov" in climate)

# In a browser: the filters work, printing hides the navigation, nothing scrolls sideways
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("SKIP browser: playwright not installed"); pages = []
if pages:
    srv = subprocess.Popen([sys.executable, "-m", "http.server", "8768", "--directory", str(SITE)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        time.sleep(1)
        with sync_playwright() as p:
            try: b = p.chromium.launch()
            except Exception: b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
            pg = b.new_page(viewport={"width": 1280, "height": 900})
            errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
            d = lumatutor.load(); bank = lumatutor.section_of(d, "suunnittele")["page"]
            pg.goto(f"http://localhost:8768/{bank}")
            expect("filter: shown when the script runs", pg.is_visible(".lt-filter"))
            total = pg.locator(".lt-wcard").count()
            pg.select_option('select[data-f="audience"]', "alakoulu")
            vis = pg.evaluate("[...document.querySelectorAll('.lt-wcard')].filter(c => !c.hidden).map(c => c.dataset.audience)")
            expect("filter: audience shows only its workshops", vis and all(a == "alakoulu" for a in vis) and len(vis) < total, vis)
            pg.select_option('select[data-f="equipment"]', "paristot")
            vis = pg.evaluate("[...document.querySelectorAll('.lt-wcard')].filter(c => !c.hidden).map(c => c.id)")
            expect("filter: audience and equipment together (AND)", vis == ["tp-virtapiiri"], vis)
            pg.select_option('select[data-f="topic"]', "ilmasto")
            expect("filter: no match says so", pg.is_visible(".lt-filter-none") and pg.locator(".lt-wcard:not([hidden])").count() == 0)
            pg.click(".lt-reset")
            expect("filter: reset shows every workshop", pg.locator(".lt-wcard:not([hidden])").count() == total)
            pg.goto(f"http://localhost:8768/{lumatutor.TOOLS}")
            expect("toolkit: copy and print buttons shown", pg.locator("[data-print]:visible").count() == 10)
            pg.emulate_media(media="print")
            expect("print: the part navigation is hidden", not pg.is_visible(".lt-nav") if pg.locator(".lt-nav").count() else True)
            pg.emulate_media(media="screen")
            expect("no script errors", not errs, errs)
            pg.close()
            for w in (360, 768, 1280):
                pg = b.new_page(viewport={"width": w, "height": 900})
                for name in pages:
                    pg.goto(f"http://localhost:8768/{name}")
                    sw, cw = pg.evaluate("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
                    expect(f"{name} at {w} px: no sideways scroll", sw <= cw, (sw, cw))
                pg.close()
            b.close()
    finally:
        srv.terminate()

print(f"\n{len(fails)} failure(s)" if fails else "\nall LUMA-tutor checks pass")
sys.exit(1 if fails else 0)
