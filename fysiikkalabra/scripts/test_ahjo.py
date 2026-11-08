"""Ahjo Makerspace pages (teacher 2026-11-08, scripts/ahjo.py) in the built site/: the three pages, the two course pages (Ahjo 1, Ahjo 2) and
every guide with a page (a draft marked "Luonnos" first, the twelve sections, its figures drawn) in every language,
the original logo on each, every internal link resolving to a built file or an anchor on it, no equipment the school will
not have, the safety page marked as a draft until a topic is approved, the front page's row, and in a browser no
sideways scroll at 360, 768 and 1280 px and a keyboard path through the section's navigation.

  python scripts/test_ahjo.py"""
import os, re, sys, pathlib, subprocess, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import ahjo, i18n

SITE = ROOT / "site"
fails = []
def expect(name, ok, got=None):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f"  ({got!r})"[:300]))
    if not ok: fails.append(name)


for lang in i18n.languages():
    out = SITE if lang == i18n.SOURCE else SITE / lang
    d = ahjo.load(lang)
    guides = ahjo.ready_guides(d)
    for name in (ahjo.PAGE, ahjo.BANK, ahjo.SAFETY, ahjo.PROJECTS) + tuple(ahjo.course_page(c["code"]) for c in d["courses"]) + tuple(f"{g}.html" for g in guides):
        f = out / name
        expect(f"{lang} {name}: built", f.is_file())
        if not f.is_file(): continue
        html = f.read_text()
        main = html[html.find("<main"):html.find("</main>")]
        head = html[:html.find("</head>")]
        expect(f"{lang} {name}: Ahjo's mark as the tab icon, not Ruukkilabra's", "ruukkilabra-32.png" not in head and "ruukkilabra-symboli.svg" not in head
               and all(re.search(rf'href="(?:\.\./)*{re.escape(i)}"', head) and (SITE / i).is_file() for i in ahjo.TAB_ICONS.values()))
        expect(f"{lang} {name}: the original logo with its name as alt", re.search(r'<img class="ahjo-logo" src="(?:\.\./)?brand/ahjo-makerspace-logo\.svg" alt="[^"]+"', main) is not None)
        expect(f"{lang} {name}: the section's navigation marks this page", f'aria-current="page"' in main and 'class="ahjo-nav"' in main)
        expect(f"{lang} {name}: no laser cutter or CNC anywhere", not ahjo.FORBIDDEN.search(re.sub(r"<[^>]+>", " ", main)))
        bad = []
        for href in re.findall(r'href="([^"]+)"', main):
            if re.match(r"[a-z]+:", href):      # Ahjo links only inside Ruukkilabra, but for a project card's inspiration (a known site)
                ext = re.match(r"https://([^/]+)/", href)
                if not (name == ahjo.PROJECTS and ext and ext.group(1) in ahjo.SOURCE_HOSTS): bad.append(href)
                continue
            path, _, frag = href.partition("#")
            target = (out / path).resolve() if path else f
            if not target.is_file() or (frag and f'id="{frag}"' not in target.read_text()): bad.append(href)
        expect(f"{lang} {name}: every link resolves to a built page (and its anchor)", not bad, bad)
    pr = (out / ahjo.PROJECTS).read_text() if (out / ahjo.PROJECTS).is_file() else ""
    cards = re.findall(r'<article class="ahjo-proj( approved)?" id="([^"]+)".*?</article>', pr, re.S)
    expect(f"{lang}: the project bank shows every card once", [c[1] for c in cards] == [p["id"] for p in sorted(d["projects"], key=lambda p: p["status"] != "hyvaksytty")], [c[1] for c in cards])
    expect(f"{lang}: a card is approved only where the teacher marked it (approved_by, date)",
           all(bool(a) == (p["status"] == "hyvaksytty" and bool(p.get("approved_by"))) for a, pid in cards for p in d["projects"] if p["id"] == pid))
    expect(f"{lang}: every card has its status badge, a measure of success and an inspiration link marked external",
           all(re.search(rf'id="{p["id"]}".*?ahjo-badge.*?{re.escape(ahjo.esc(d["ui"]["proj_success"]))}.*?rel="external noopener".*?ahjo-ext', pr, re.S) for p in d["projects"]))
    expect(f"{lang}: the project page says the cards are proposals", ahjo.esc(d["ui"]["projects_note"]) in pr)
    bank = (out / ahjo.BANK).read_text() if (out / ahjo.BANK).is_file() else ""
    for g in guides:
        r = next(r for r in d["resources"] if r.get("id") == g)
        f = out / f"{g}.html"; html = f.read_text() if f.is_file() else ""
        art = re.search(r'<article class="ahjo-guide">(.*?)</article>', html, re.S)
        heads = [re.sub(r"<[^>]+>", "", h) for h in re.findall(r"<h2[^>]*>(.*?)</h2>", art.group(1))] if art else []
        expect(f"{lang} {g}: the twelve guide sections in order", heads == d["ui"]["guide_sections"], heads)
        expect(f"{lang} {g}: a draft says so before the guide, and the bank links it with its badge",
               r["status"] != "draft" or (html.find('class="ahjo-draft"') != -1 and html.find('class="ahjo-draft"') < html.find('class="ahjo-guide"')
                                         and re.search(rf'href="{g}\.html".*?{re.escape(ahjo.esc(d["ui"]["res_draft"]))}', bank, re.S) is not None))
        placeholders = len(ahjo.FIG_REF.findall(ahjo.guide_file(g, lang).read_text()))
        expect(f"{lang} {g}: every figure drawn ({placeholders})", art is not None and art.group(1).count('class="fig ahjo-fig"><svg') == placeholders and not ahjo.FIG_REF.search(art.group(1)))
    safety = (out / ahjo.SAFETY).read_text() if (out / ahjo.SAFETY).is_file() else ""
    approved = any(s.get("status") == "hyvaksytty" for s in d["safety"])
    expect(f"{lang}: the safety page is marked as a draft while nothing is approved", approved or ('class="ahjo-draft"' in safety and ahjo.esc(d["ui"]["safety_draft_note"].split(".")[0]) in safety))
    expect(f"{lang}: every safety topic is listed", all(f'id="{s["id"]}"' in safety for s in d["safety"]))
    start = (out / ahjo.PAGE).read_text() if (out / ahjo.PAGE).is_file() else ""
    expect(f"{lang}: the equipment heading follows equipment_status", ahjo.esc(d["ui"]["equipment_h_" + d["equipment_status"]]) in start)
    expect(f"{lang}: Ahjo 1 and Ahjo 2 on the start page", all(f'id="{c["code"].lower()}"' in start for c in d["courses"]))
    for c in d["courses"]:
        card = re.search(rf'<article class="ahjo-course" id="{c["code"].lower()}".*?</article>', start, re.S)
        expect(f"{lang} {c['code']}: the start page's card links its own course page", card is not None and f'href="{ahjo.course_page(c["code"])}"' in card.group(0))
        cp = (out / ahjo.course_page(c["code"])).read_text() if (out / ahjo.course_page(c["code"])).is_file() else ""
        ol = re.search(r'<ol class="ahjo-lessons">(.*?)</ol>', cp, re.S)
        n = len(re.findall(r"<li>", ol.group(1))) if ol else 0
        expect(f"{lang} {c['code']}: the course page has the goals and {n} lessons, each with its picture",
               not c.get("lessons") or (n == len(c["lessons"]) == 16 and ol.group(1).count('class="ahjo-art"') == 16 and 'id="tavoitteet"' in cp))
        expect(f"{lang} {c['code']}: every lesson says what it produces", not c.get("lessons") or (ol and ol.group(1).count('class="ahjo-lesson-e ahjo-lesson-o"') == 16))
        hand = [l["milestone"] for l in c.get("lessons", []) if l.get("milestone")]
        expect(f"{lang} {c['code']}: the hand-ins ({len(hand)}) are marked on their lessons", ol is not None and all(ahjo.esc(h) in ol.group(1) for h in hand) and (c["code"] != "AHJO2" or len(hand) == 5))
        expect(f"{lang} {c['code']}: the optional deepening is its own section, not in the 16 lessons", bool(c.get("deepening")) == ('id="syventavat"' in cp)
               and all(ahjo.esc(x["title"]) not in (ol.group(1) if ol else "") for x in c.get("deepening", [])))
        expect(f"{lang} {c['code']}: the course page links Ahjo's materials and safety", f'href="{ahjo.BANK}"' in cp and f'href="{ahjo.SAFETY}"' in cp)
        expect(f"{lang} {c['code']}: the Makerspace licence only where the teacher said so (Ahjo 1)", bool(c.get("license")) == ('class="ahjo-sec ahjo-safety-teaser ahjo-license"' in cp))
    home = (out / "index.html").read_text()
    plan = re.search(r'<ul class="mod-list plan-list"[^>]*>(.*?)</ul>', home, re.S)
    expect(f"{lang}: Ahjo 1 and Ahjo 2 are not in the front page's planned list (teacher 2026-11-08)",
           not plan or not any(f'{c["code"].lower()}.svg' in plan.group(1) for c in d["courses"]))
    rows = re.search(r'<ul class="mod-list ahjo-list">(.*?)</ul>', home, re.S)
    expect(f"{lang}: the front page lists Ahjo 1 and Ahjo 2, each linking its course page with its icon (teacher 2026-11-08)",
           rows is not None and [h for h in re.findall(r'href="([^"]+)"', rows.group(1))] == [ahjo.course_page(c["code"]) for c in d["courses"]]
           and all(f'module-icons/{c["code"].lower()}.svg' in rows.group(1) for c in d["courses"]))
    for c in d["courses"]:
        cp = (out / ahjo.course_page(c["code"])).read_text() if (out / ahjo.course_page(c["code"])).is_file() else ""
        m = cp[cp.find("<main"):]
        sh = m.find('class="ahjo-sec ahjo-shared"')
        expect(f"{lang} {c['code']}: Ahjo's shared pages come first on the course page", 0 < sh < min(x for x in (m.find('class="ahjo-sec ahjo-safety-teaser'), m.find('id="tavoitteet"')) if x > 0)
               and all(f'href="{h}"' in m[sh:sh + 4000] for h in (ahjo.PAGE, ahjo.BANK, ahjo.SAFETY)))
expect("the header's Ruukkilabra symbol in Kiviruukin lukio's colours is up to date", ahjo.SITE_MARK_KR.is_file() and ahjo.SITE_MARK_KR.read_text() == ahjo.site_mark_kiviruukki())
for lang in i18n.languages():
    out = SITE if lang == i18n.SOURCE else SITE / lang
    h = (out / ahjo.PAGE).read_text()
    expect(f"{lang}: the Ahjo pages' header symbol is in Kiviruukin lukio's colours", "ruukkilabra-symboli-kiviruukki.svg" in h[:h.find("</header>")] and 'brand-mark" src="brand/ruukkilabra-symboli.svg' not in h)
expect("the mark is cut from the original logo unchanged (scripts/ahjo_art.py writes it)", ahjo.MARK.is_file() and ahjo.MARK.read_text() == ahjo.mark_svg())

# browser: widths and keyboard
from playwright.sync_api import sync_playwright
port = 8799
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(port)], cwd=SITE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
try:
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": os.environ["CHROMIUM_PATH"]} if os.environ.get("CHROMIUM_PATH") else {}))
        gpages = [f"{g}.html" for g in ahjo.ready_guides(ahjo.load())]
        for name in ["ahjo.html", "ahjo-1.html", "ahjo-2.html", "ahjo-materiaalit.html", "ahjo-turvallisuus.html", "ahjo-projektit.html", "en/ahjo.html", "en/ahjo-1.html", "en/ahjo-projektit.html"] + gpages + ["en/" + g for g in gpages]:
            for w in (360, 768, 1280):
                pg = b.new_page(viewport={"width": w, "height": 900}); pg.goto(f"http://localhost:{port}/{name}")
                ov = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
                expect(f"{name} @ {w}: no sideways scroll", ov <= 0, ov)
                small = pg.evaluate("""[...document.querySelectorAll('main a')].filter(a => { if (a.closest('.ahjo-guide p, .ahjo-guide li, .ahjo-guide td, .ahjo-proj dd')) return false; const r = a.getBoundingClientRect();
                    return r.width > 0 && r.height < 24; }).map(a => a.textContent.trim()).slice(0, 5)""")
                expect(f"{name} @ {w}: links are at least 24 px high", not small, small)
                pg.close()
        pg = b.new_page(viewport={"width": 1280, "height": 900}); pg.goto(f"http://localhost:{port}/ahjo.html")
        seen = []
        for _ in range(40):
            pg.keyboard.press("Tab")
            seen.append(pg.evaluate("(() => { const a = document.activeElement; return a.closest('.ahjo-nav') ? a.getAttribute('href') : null })()"))
        nav = [h for h in seen if h]
        expect("keyboard: Tab reaches every link of Ahjo's navigation in order", nav[:6] == ["ahjo.html", "ahjo.html#opintojaksot", "ahjo-materiaalit.html", "ahjo-projektit.html", "ahjo.html#laitteisto", "ahjo-turvallisuus.html"], nav)
        b.close()
finally:
    srv.terminate()

print(f"\n{len(fails)} failure(s)" if fails else "\nall Ahjo checks passed")
sys.exit(1 if fails else 0)
