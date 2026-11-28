"""FY9 course page, the way in (work queue 33.1; templates/valmentaja.js, scripts/valmentaja.py row_html, local_courses.head).
Usage: python scripts/test_fy9_start.py [site|preview]
First visit: one main button "Tee lähtötasotesti" to the diagnostic, three other routes, the description behind a closed "Tietoa opintojaksosta",
  at 360 and 1280 px the main button inside the first screen and no overflow. A returning student: "Jatka kertausta" to the coach's next task
  with its name. An exam in progress: "Jatka kertausta" to that exam. Keyboard: Tab reaches the main button first, Enter follows it.
Languages fi, en, fi-easy. Exit status 1 on any failure."""
import functools, http.server, json, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

args = sys.argv[1:]
SITE = ROOT / (args[0] if args and (ROOT / args[0]).is_dir() else ("site" if (ROOT / "site" / "FY9.html").is_file() else "preview"))
KEY, EXAM = "ruukkilabra:fy9-valmentaja", "ruukkilabra:fy9-koetila"
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
LANGS = [("fi", ""), ("en", "en/"), ("fi-easy", "fi-easy/")]
with sync_playwright() as pw:
    b = launch(pw)
    for lang, pre in LANGS:
        if not (SITE / pre / "FY9.html").is_file(): continue
        T = json.loads((ROOT / "lang" / f"{lang}.json").read_text())["coach"]
        for w, h in ((360, 740), (1280, 800)):
            c = b.new_context(viewport={"width": w, "height": h}); p = c.new_page(); errs = []; p.on("pageerror", lambda e: errs.append(str(e)))
            p.goto(BASE + pre + "FY9.html"); tag = f"{lang} {w}px"
            main = p.locator("#fy9-main")
            expect(f"{tag}: first visit: the main button is the diagnostic, in the first screen", main.inner_text().strip() == T["start"] and main.get_attribute("href").endswith("fy9-koe.html#testi-ohje")
                   and main.bounding_box()["y"] + main.bounding_box()["height"] <= h, (main.inner_text(), main.bounding_box()))
            routes = p.locator(".fy9-routes a")
            expect(f"{tag}: three other routes with the approved names", routes.all_inner_texts() == [T["route_topic"], T["route_yo"], T["route_mini"]] and
                   [x.get_attribute("href") for x in routes.all()][:2] == ["#chapters", "yo-sekoitin.html"], routes.all_inner_texts())
            expect(f"{tag}: the course description is behind a closed '{T['about']}' and after the button", p.locator("details.fy9-about > summary").inner_text().strip() == T["about"]
                   and not p.evaluate("document.querySelector('.fy9-about').open") and not p.locator(".local-desc").is_visible()
                   and p.evaluate("document.getElementById('fy9-main').compareDocumentPosition(document.querySelector('.fy9-about')) & Node.DOCUMENT_POSITION_FOLLOWING") > 0)
            expect(f"{tag}: the line under the button is hidden on a first visit and nothing failed", not p.locator("#fy9-coach-row").is_visible() and not errs, errs)
            expect(f"{tag}: no horizontal overflow, buttons at least 44 px", p.evaluate("document.scrollingElement.scrollWidth - innerWidth") <= 1
                   and all(x["height"] >= 44 for x in [e.bounding_box() for e in [main] + routes.all()]))
            p.locator("details.fy9-about > summary").click()
            expect(f"{tag}: the box opens and shows the description", p.locator(".local-desc").is_visible())
            if w == 1280:   # keyboard
                p.goto(BASE + pre + "FY9.html"); p.keyboard.press("Tab"); p.keyboard.press("Tab")
                while p.evaluate("document.activeElement.id") not in ("fy9-main", "") and p.evaluate("!!document.activeElement.closest('header')"): p.keyboard.press("Tab")
                tabs = 0
                while p.evaluate("document.activeElement.id") != "fy9-main" and tabs < 40: p.keyboard.press("Tab"); tabs += 1
                expect(f"{tag}: Tab reaches the main button", p.evaluate("document.activeElement.id") == "fy9-main", tabs)
                with p.expect_navigation(): p.keyboard.press("Enter")
                expect(f"{tag}: Enter opens the diagnostic", "fy9-koe.html" in p.url, p.url)
            if w == 360:   # a returning student: one real attempt of the diagnostic (a wrong answer), then the course page again
                p.goto(BASE + pre + "fy9-koe.html#testi-ohje")
                d = p.locator("details.opt:has(#testi-1)")
                d.locator("summary").first.click(); d.locator("input[type=radio]").nth(0).check(); d.locator("button.commit").click()
                p.wait_for_function("(k) => { try { return /fy9-koe#testi-/.test(localStorage.getItem(k) || ''); } catch (e) { return false; } }", arg="ruukkilabra:fy9-valmentaja")   # the page logs a moment after the click: leave it only then
                p.goto(BASE + pre + "FY9.html")
                main = p.locator("#fy9-main"); line = p.locator("#fy9-coach-row")
                expect(f"{tag}: returning: '{T['resume']}' to the coach's next task, which the line names", main.inner_text().strip() == T["resume"] and "fy9-koe.html#testi-" in main.get_attribute("href")
                       and line.is_visible() and len(line.locator(".fy9-next-task").inner_text()) > 2, (main.inner_text(), main.get_attribute("href"), line.inner_text() if line.is_visible() else None))
                expect(f"{tag}: returning: the main button is still in the first screen and nothing overflows", main.bounding_box()["y"] + main.bounding_box()["height"] <= h
                       and p.evaluate("document.scrollingElement.scrollWidth - innerWidth") <= 1)
                p.evaluate("(k) => localStorage.setItem(k, JSON.stringify({v: 1, exams: {'m30-osa1-1': {state: 'run'}}}))", EXAM)
                p.goto(BASE + pre + "FY9.html")
                expect(f"{tag}: an exam in progress: '{T['resume']}' leads to that exam", p.locator("#fy9-main").get_attribute("href") == "fy9-minikoe-m30-osa1-1.html", p.locator("#fy9-main").get_attribute("href"))
                p.locator(".fy9-routes a").nth(2).click()
                p.wait_for_url(re.compile(r"FY9-valmentaja\.html")); p.wait_for_function("() => { const m = document.getElementById('coach-mini'); return m && m.open && m.querySelectorAll('.coach-min').length > 0; }")   # the click navigates: wait for the page and its list
                expect(f"{tag}: Tee minikoe opens the exam choice, open, with a 30 and a 60 minute set", "FY9-valmentaja.html" in p.url and p.evaluate("document.getElementById('coach-mini').open")
                       and p.locator("#coach-mini .coach-min").filter(has_text=re.compile(r"^30")).count() > 0 and p.locator("#coach-mini .coach-min").filter(has_text=re.compile(r"^60")).count() > 0)
                expect(f"{tag}: the six-hour practice exam has its own name", p.locator("#coach-mini a.coach-task", has_text=T["mini_exam"]).count() == 1)
            c.close()
    b.close()
srv.shutdown()
print("all ok" if not fails else f"{fails} FAILED"); sys.exit(1 if fails else 0)
