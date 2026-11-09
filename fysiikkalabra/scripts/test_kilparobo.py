"""Kilparobotiikka's team pages (teacher's brief 2026-11-09, scripts/kilparobo.py) in the built site/: the five pages in
every language that publishes the course, the section's navigation marking the page, every internal link resolving to a
built file and its anchor, external links only to VEX's and RECF's own sites (marked external), the Otarobo 2026 photos and
the students' quote still on the start page, no team news invented (an empty "now" says it is empty), the safety page
keeping the mentor's and the teacher's parts apart, the diary template downloadable, and in a browser no sideways scroll
at 360, 768 and 1280 px.

  python scripts/test_kilparobo.py"""
import re, sys, pathlib, subprocess, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n, kilparobo, local_courses

SITE = ROOT / "site"
fails = []
def expect(name, ok, got=None):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f"  ({got!r})"[:300]))
    if not ok: fails.append(name)


pages = []
for lang in i18n.languages():
    if kilparobo.CODE not in local_courses.load(lang): continue
    out = SITE if lang == i18n.SOURCE else SITE / lang
    d, c = kilparobo.load(lang), local_courses.load(lang)[kilparobo.CODE]
    for name in (kilparobo.PAGE,) + kilparobo.SUBPAGES:
        f = out / name
        expect(f"{lang} {name}: built", f.is_file())
        if not f.is_file(): continue
        pages.append(f.relative_to(SITE).as_posix())
        html = f.read_text()
        main = html[html.find("<main"):html.find("</main>")]
        expect(f"{lang} {name}: in Kiviruukin lukio's theme", 'kr-theme kr-team' in main[:200] and "ruukkilabra-symboli-kiviruukki.svg" in html)
        expect(f"{lang} {name}: the section's navigation marks this page", re.search(rf'<a href="{re.escape(name)}" aria-current="page">', main) is not None)
        bad = []
        for href in re.findall(r'href="([^"]+)"', main):
            if href.startswith("data:"): continue
            if re.match(r"[a-z]+:", href):
                m = re.match(r"https://([^/]+)/", href)
                if not (m and m.group(1) in kilparobo.OFFICIAL_HOSTS and re.search(rf'href="{re.escape(href)}" rel="external noopener"', main)): bad.append(href)
                continue
            path, _, frag = href.partition("#")
            target = (out / path).resolve() if path else f
            if not target.is_file() or (frag and f'id="{frag}"' not in target.read_text()): bad.append(href)
        expect(f"{lang} {name}: every link resolves (internal with its anchor, external only VEX/RECF)", not bad, bad)
    hub = (out / kilparobo.PAGE).read_text()
    expect(f"{lang}: the start page keeps every Otarobo 2026 photo and the students' quotes",
           all(re.search(rf'src="(?:\.\./)?{re.escape(p["src"])}"', hub) for p in c.get("photos", [])) and all(local_courses.esc(q["paragraphs"][0]) in hub for q in c.get("quotes", [])))
    expect(f"{lang}: the five quick answers come first", hub.find('class="kr-quick"') < hub.find('id="tule-mukaan"') and hub.count('class="kr-quick-n"') == 5)
    expect(f"{lang}: with no news written, 'now' says so (nothing invented)", bool(d["now"]["text"]) or local_courses.esc(d["ui"]["now_empty"]) in hub)
    path = (out / kilparobo.PATH).read_text()
    expect(f"{lang}: five stages, each with a goal, a practice, a mentor's tip and a way to show it",
           len(re.findall(r'<section class="kr-stage"', path)) == 5 and all(path.count(k) == 5 for k in ('class="kr-goal"', 'kr-box-practice', 'kr-box-mentor', 'kr-box-show')))
    season = (out / kilparobo.SEASON).read_text()
    expect(f"{lang}: eight season phases and the diary template with a download", season.count('class="kr-phase"') == 8 and 'download="' in season and 'id="kr-pohja"' in season)
    expect(f"{lang}: no dates on the season page", not re.search(r"\b\d{1,2}\.\d{1,2}\.\d{4}\b", re.sub(r"<[^>]+>", " ", season[season.find("<main"):season.find("</main>")])))
    safety = (out / kilparobo.SAFETY).read_text()
    expect(f"{lang}: safety keeps the mentor's and the teacher's parts apart and is a draft", 'kr-role-mentor' in safety and 'kr-role-teacher' in safety
           and safety.count('class="kr-teacher"') == len(d["safety"]["topics"]) and local_courses.esc(d["safety"]["draft"]) in safety)

# In a browser: nothing scrolls sideways at a phone's, a tablet's or a laptop's width
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("SKIP layout: playwright not installed"); pages = []
if pages:
    srv = subprocess.Popen([sys.executable, "-m", "http.server", "8767", "--directory", str(SITE)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        time.sleep(1)
        with sync_playwright() as p:
            b = p.chromium.launch()
            for w in (360, 768, 1280):
                pg = b.new_page(viewport={"width": w, "height": 900})
                for name in pages:
                    pg.goto(f"http://localhost:8767/{name}")
                    sw, cw = pg.evaluate("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
                    expect(f"{name} at {w} px: no sideways scroll", sw <= cw, (sw, cw))
                pg.close()
            b.close()
    finally:
        srv.terminate()

print(f"\n{len(fails)} failure(s)" if fails else "\nall Kilparobotiikka checks pass")
sys.exit(1 if fails else 0)
