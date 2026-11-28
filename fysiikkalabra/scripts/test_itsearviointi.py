"""Self-assessment of a written task: not assessed is not zero points (work queue 33.4; templates/selfassess.js, scripts/practice.py).
Usage: python scripts/test_itsearviointi.py [site|preview]
Before any criterion has points the total says lang js.rubric_start ("Pisteytä oma vastauksesi · enintään 15 p"), never "0 / 15"; once some are assessed it shows the points chosen and
how many items are not assessed; a 0 the student chooses is an assessed item (it counts, and the total is "0 / 15" only when every item has its points); the choices come back after a
reload; the radios work with the keyboard. Pages: a FY9 task (fy9-liike, Kiihdytyskaista) and a Sovella itsenäisesti task (FY3-sovella); fi, en, fi-easy; 360 and 1280 px. Exit status 1 on any failure."""
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


def fmt(s, **kw): return re.sub(r"\{\{(\w+)\}\}", lambda m: str(kw[m.group(1)]), s)


def text(p, rub): return rub.locator(".rubric-total").inner_text().strip()


with sync_playwright() as pw:
    b = launch(pw)
    for lang, pre in (("fi", ""), ("en", "en/"), ("fi-easy", "fi-easy/")):
        J = json.loads((ROOT / "lang" / f"{lang}.json").read_text())["js"]
        for page in ("fy9-liike.html", "FY3-sovella.html"):
            if not (SITE / pre / page).is_file(): continue
            for w, h in ((360, 740), (1280, 800)):
                tag = f"{lang} {w}px {page}"
                c = b.new_context(viewport={"width": w, "height": h}); p = c.new_page(); errs = []; p.on("pageerror", lambda e: errs.append(str(e)))
                p.goto(BASE + pre + page); p.wait_for_timeout(200)
                p.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
                rub = p.locator(".rubric").first
                n = rub.locator("fieldset.crit").count(); mx = int(rub.get_attribute("data-max"))
                expect(f"{tag}: before any points it says to score the answer, up to {mx} p, and shows no 0 / {mx}", text(p, rub) == fmt(J["rubric_start"], max=mx) and f"0 / {mx}" not in text(p, rub), text(p, rub))
                first = rub.locator("fieldset.crit").first
                zero = first.locator("input[value='0']").first
                zero.check(); p.wait_for_timeout(100)
                expect(f"{tag}: a chosen 0 is an assessed item: one fewer left, points 0", text(p, rub) == fmt(J["rubric_partial"], got=0, max=mx, left=n - 1) and "0 /" in text(p, rub), text(p, rub))
                second = rub.locator("fieldset.crit").nth(1)
                vals = [int(i.get_attribute("value")) for i in second.locator("input").all()]
                second.locator(f"input[value='{max(vals)}']").first.check(); p.wait_for_timeout(100)
                expect(f"{tag}: the points chosen and the items left are shown", text(p, rub) == fmt(J["rubric_partial"], got=max(vals), max=mx, left=n - 2), text(p, rub))
                p.reload(); p.wait_for_timeout(200); p.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
                rub = p.locator(".rubric").first
                expect(f"{tag}: after a reload the zero and the points are kept", rub.locator("fieldset.crit").first.locator("input[value='0']").first.is_checked() and text(p, rub) == fmt(J["rubric_partial"], got=max(vals), max=mx, left=n - 2), text(p, rub))
                if w == 1280:   # keyboard: arrow keys move inside a group of radios
                    third = rub.locator("fieldset.crit").nth(2).locator("input").first
                    third.focus(); p.keyboard.press("Space"); p.wait_for_timeout(100)
                    expect(f"{tag}: Space on a focused option chooses it and the items left go down by one", third.is_checked() and text(p, rub) == fmt(J["rubric_partial"], got=max(vals) + int(third.get_attribute("value")), max=mx, left=n - 3), text(p, rub))
                for k in range(n):   # every item assessed with 0: a complete assessment of 0 points
                    rub.locator("fieldset.crit").nth(k).locator("input[value='0']").first.check()
                p.wait_for_timeout(100)
                expect(f"{tag}: every item given 0 is a complete assessment: total 0 / {mx}", text(p, rub) == fmt(J["rubric_total"], got=0, max=mx), text(p, rub))
                expect(f"{tag}: no error, no overflow", not errs and p.evaluate("document.scrollingElement.scrollWidth - innerWidth") <= 1, errs)
                c.close()
    b.close()
srv.shutdown()
print("all ok" if not fails else f"{fails} FAILED"); sys.exit(1 if fails else 0)
