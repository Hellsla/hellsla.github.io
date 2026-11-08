"""Ahjo Makerspace pages (teacher 2026-11-08, scripts/ahjo.py) in the built site/: the three pages in every language,
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
    for name in (ahjo.PAGE, ahjo.BANK, ahjo.SAFETY):
        f = out / name
        expect(f"{lang} {name}: built", f.is_file())
        if not f.is_file(): continue
        html = f.read_text()
        main = html[html.find("<main"):html.find("</main>")]
        expect(f"{lang} {name}: the original logo with its name as alt", re.search(r'<img class="ahjo-logo" src="(?:\.\./)?brand/ahjo-makerspace-logo\.svg" alt="[^"]+"', main) is not None)
        expect(f"{lang} {name}: the section's navigation marks this page", f'aria-current="page"' in main and 'class="ahjo-nav"' in main)
        expect(f"{lang} {name}: no laser cutter or CNC anywhere", not ahjo.FORBIDDEN.search(re.sub(r"<[^>]+>", " ", main)))
        bad = []
        for href in re.findall(r'href="([^"]+)"', main):
            if re.match(r"[a-z]+:", href): bad.append(href); continue   # Ahjo links only inside Ruukkilabra
            path, _, frag = href.partition("#")
            target = (out / path).resolve() if path else f
            if not target.is_file() or (frag and f'id="{frag}"' not in target.read_text()): bad.append(href)
        expect(f"{lang} {name}: every link resolves to a built page (and its anchor)", not bad, bad)
    safety = (out / ahjo.SAFETY).read_text() if (out / ahjo.SAFETY).is_file() else ""
    approved = any(s.get("status") == "hyvaksytty" for s in d["safety"])
    expect(f"{lang}: the safety page is marked as a draft while nothing is approved", approved or ('class="ahjo-draft"' in safety and ahjo.esc(d["ui"]["safety_draft_note"].split(".")[0]) in safety))
    expect(f"{lang}: every safety topic is listed", all(f'id="{s["id"]}"' in safety for s in d["safety"]))
    start = (out / ahjo.PAGE).read_text() if (out / ahjo.PAGE).is_file() else ""
    expect(f"{lang}: the equipment heading follows equipment_status", ahjo.esc(d["ui"]["equipment_h_" + d["equipment_status"]]) in start)
    expect(f"{lang}: Ahjo 1 and Ahjo 2 on the start page", all(f'id="{c["code"].lower()}"' in start for c in d["courses"]))
    home = (out / "index.html").read_text()
    plan = re.search(r'<ul class="mod-list plan-list"[^>]*>(.*?)</ul>', home, re.S)
    expect(f"{lang}: Ahjo 1 and Ahjo 2 are not in the front page's planned list (teacher 2026-11-08)",
           not plan or not any(f'{c["code"].lower()}.svg' in plan.group(1) for c in d["courses"]))
    expect(f"{lang}: the front page links Ahjo with its logo", re.search(r'<ul class="mod-list ahjo-list"><li><a class="mod-row ahjo-row" href="ahjo\.html"><img [^>]*ahjo-makerspace-logo\.svg', home) is not None)

# browser: widths and keyboard
from playwright.sync_api import sync_playwright
port = 8799
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(port)], cwd=SITE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
try:
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": os.environ["CHROMIUM_PATH"]} if os.environ.get("CHROMIUM_PATH") else {}))
        for name in ("ahjo.html", "ahjo-materiaalit.html", "ahjo-turvallisuus.html", "en/ahjo.html"):
            for w in (360, 768, 1280):
                pg = b.new_page(viewport={"width": w, "height": 900}); pg.goto(f"http://localhost:{port}/{name}")
                ov = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
                expect(f"{name} @ {w}: no sideways scroll", ov <= 0, ov)
                small = pg.evaluate("""[...document.querySelectorAll('main a')].filter(a => { const r = a.getBoundingClientRect();
                    return r.width > 0 && r.height < 24; }).map(a => a.textContent.trim()).slice(0, 5)""")
                expect(f"{name} @ {w}: links are at least 24 px high", not small, small)
                pg.close()
        pg = b.new_page(viewport={"width": 1280, "height": 900}); pg.goto(f"http://localhost:{port}/ahjo.html")
        seen = []
        for _ in range(40):
            pg.keyboard.press("Tab")
            seen.append(pg.evaluate("(() => { const a = document.activeElement; return a.closest('.ahjo-nav') ? a.getAttribute('href') : null })()"))
        nav = [h for h in seen if h]
        expect("keyboard: Tab reaches every link of Ahjo's navigation in order", nav[:5] == ["ahjo.html", "ahjo.html#opintojaksot", "ahjo-materiaalit.html", "ahjo.html#laitteisto", "ahjo-turvallisuus.html"], nav)
        b.close()
finally:
    srv.terminate()

print(f"\n{len(fails)} failure(s)" if fails else "\nall Ahjo checks passed")
sys.exit(1 if fails else 0)
