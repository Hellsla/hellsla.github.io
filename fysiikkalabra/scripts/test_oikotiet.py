"""Oikotiet at the start of a FY9 unit (work queue 33.3; scripts/oikotiet.py).
Usage: python scripts/test_oikotiet.py [site|preview]
Every FY9 review unit has "Testaa lähtötasosi", "Kertaa teoria" and "Ratkaise yo-tyylinen tehtävä" (names from lang inquiry.sc_*) before its illustration, each taking the student to
its part (in view under the sticky bar, the task's situation shown at once); the practice exam (fy9-harjoituskoe) has its own names from its own headings: Kokeen ohjeet, Osa I, Osa II,
Osa III. Languages fi, en, fi-easy; 360 and 1280 px; no overflow, links 44 px; Tab and Enter reach a shortcut. Exit status 1 on any failure."""
import functools, http.server, json, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

args = sys.argv[1:]
SITE = ROOT / (args[0] if args and (ROOT / args[0]).is_dir() else ("site" if (ROOT / "site" / "fy9-liike.html").is_file() else "preview"))
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/"
EXAM = {"fi": ["Kokeen ohjeet", "Osa I", "Osa II", "Osa III"], "fi-easy": ["Kokeen ohjeet", "Osa I", "Osa II", "Osa III"]}
with sync_playwright() as pw:
    b = launch(pw)
    for lang, pre in (("fi", ""), ("en", "en/"), ("fi-easy", "fi-easy/")):
        f = SITE / pre / "valmentaja" / "fy9.json"
        if not f.is_file(): continue
        L = json.loads((ROOT / "lang" / f"{lang}.json").read_text())["inquiry"]
        units = [u["id"] for u in json.loads(f.read_text())["units"]]
        want = [L["sc_level"], L["sc_theory"], L["sc_task"]]
        for w, h in ((360, 740), (1280, 800)):
            c = b.new_context(viewport={"width": w, "height": h}); p = c.new_page(); errs = []; p.on("pageerror", lambda e: errs.append(str(e)))
            for u in units:
                tag = f"{lang} {w}px {u}"
                p.goto(BASE + pre + f"{u}.html"); p.wait_for_timeout(150)
                row = p.locator(".unit-short a")
                names = row.all_inner_texts()
                if u == "fy9-harjoituskoe":
                    expect(f"{tag}: the practice exam's own names", names == EXAM[lang] if lang in EXAM else (len(names) == 4 and [re.sub(r"^Part ", "", n) for n in names[1:]] == ["I", "II", "III"]), names)
                else:
                    expect(f"{tag}: the three shortcuts with their names", names == want, names)
                expect(f"{tag}: after the title and before the illustration, 44 px high, no overflow", p.locator(".intro-head .unit-short").count() == 1 and all(e.bounding_box()["height"] >= 44 for e in row.all())
                       and p.evaluate("document.scrollingElement.scrollWidth - innerWidth") <= 1 and not errs, errs)
                for i, e in enumerate(row.all()):
                    href = e.get_attribute("href")
                    p.goto(BASE + pre + f"{u}.html"); p.wait_for_timeout(100)
                    row.nth(i).click(); p.wait_for_timeout(250)
                    tgt = p.locator(href).first
                    box = tgt.bounding_box() if tgt.count() else None
                    ok = bool(box) and 50 <= box["y"] < h * 0.6 and tgt.is_visible()
                    if ok and href.startswith("#fy9-") and u != "fy9-harjoituskoe": ok = p.locator(f"{href} .situation, {href} p").first.is_visible()   # the task's situation is in view at once
                    expect(f"{tag}: '{names[i]}' takes the student to {href}, in view under the sticky bar", ok, (href, box))
            # keyboard
            if w == 1280:
                p.goto(BASE + pre + "fy9-liike.html"); n = 0
                while p.evaluate("document.activeElement.closest && !document.activeElement.closest('.unit-short')") and n < 40: p.keyboard.press("Tab"); n += 1
                p.keyboard.press("Enter"); p.wait_for_timeout(200)
                expect(f"{lang}: Tab reaches the shortcuts and Enter follows one", "#ennusta" in p.url, (p.url, n))
            c.close()
    b.close()
srv.shutdown()
print("all ok" if not fails else f"{fails} FAILED"); sys.exit(1 if fails else 0)
