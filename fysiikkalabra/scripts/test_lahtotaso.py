"""Lähtötasotesti on fy9-koe.html (work queue 33.2; scripts/lahtotaso.py, templates/valmentaja.js part g).
Usage: python scripts/test_lahtotaso.py [site|preview]
The 24 diagnostic tasks are one test named by lang inquiry.lt_title, a box per module FY1–FY8, each task named "FY1 · 1/3 · Virheen laji" with one numbering; the real
worked example is still "Esimerkki 1". Arriving (#testi-ohje) opens the first module and its first task; a wrong answer shows "Kertaa tämä asia" (the page of the feedback)
and "Seuraava tehtävä"; a right one only the next; the third task of a module closes it with what to revise and where to go on; after a reload the test goes on from
the first task not answered; a student who answered under the earlier page (the same keys) goes on from there. No new storage key. Languages fi, en, fi-easy; 360 and 1280 px; Tab and Enter.
Exit status 1 on any failure."""
import functools, http.server, json, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

args = sys.argv[1:]
SITE = ROOT / (args[0] if args and (ROOT / args[0]).is_dir() else ("site" if (ROOT / "site" / "fy9-koe.html").is_file() else "preview"))
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
ACTS = {a["id"]: a for a in json.loads((ROOT / "content/fi/units/fy9-koe/inquiry.json").read_text())["activities"]}


def card(p, n): return p.locator(f"details.opt:has(#testi-{n})")


def answer(p, n, right):
    """Answer task n right or wrong (a choice by its marked option, a number by its answer or a clearly wrong one)."""
    d = card(p, n)
    if not d.evaluate("e => e.open"): d.locator("summary").first.click()
    if ACTS[f"testi-{n}"]["type"] == "choice":
        d.locator(f"input[type=radio][data-correct='{1 if right else 0}']").first.check(); d.locator("button.commit").click()
    else:
        d.locator("form.check input").first.fill(str(ACTS[f"testi-{n}"]["answer"] if right else 7)); d.locator("form.check button").first.click()
    p.wait_for_timeout(250)


with sync_playwright() as pw:
    b = launch(pw)
    for lang, pre in (("fi", ""), ("en", "en/"), ("fi-easy", "fi-easy/")):
        if not (SITE / pre / "fy9-koe.html").is_file(): continue
        L = json.loads((ROOT / "lang" / f"{lang}.json").read_text())["inquiry"]
        for w, h in ((360, 740), (1280, 800)):
            tag = f"{lang} {w}px"
            c = b.new_context(viewport={"width": w, "height": h}); p = c.new_page(); errs = []; p.on("pageerror", lambda e: errs.append(str(e)))
            p.goto(BASE + pre + "fy9-koe.html#testi-ohje"); p.wait_for_timeout(400)
            expect(f"{tag}: the test has its name, eight modules and 24 tasks", p.locator("#lahtotasotesti .lt-h").inner_text() == L["lt_title"] and p.locator("details.lt-mod").count() == 8 and p.locator("#lahtotasotesti .activity[id^=testi-]:not(#testi-ohje)").count() == 24)
            expect(f"{tag}: a task is named 'FY1 · 1/3 · …' once, not as an example", p.locator("details.opt:has(#testi-1) > summary").inner_text().replace("\n", " ").startswith("FY1 · 1/3") and "Esimerkki 2" not in p.locator("details.opt:has(#testi-1) > summary").inner_text()
                   and not re.search(r"\b1\. ", p.locator("details.opt:has(#testi-1) > summary").inner_text()))
            ex = p.locator("details.opt > summary").filter(has_text=re.compile(r"^(Esimerkki|Example) 1")).count() + p.locator("h3.example-title").filter(has_text=re.compile(r"^(Esimerkki|Example) 1")).count()
            expect(f"{tag}: the real example is still numbered 1", ex >= 1 or "Esimerkki 1" in p.content() or "Example 1" in p.content())
            expect(f"{tag}: arriving opens the first module and its first task, nothing else", p.evaluate("[...document.querySelectorAll('details.lt-mod[open]')].map(e => e.dataset.mod).join()") == "FY1"
                   and p.evaluate("[...document.querySelectorAll('details.lt-mod details.opt[open] .activity')].map(e => e.id).join()") == "testi-1")
            expect(f"{tag}: the heading is not under the sticky bar", p.locator("#lahtotasotesti .lt-h").bounding_box()["y"] >= 55, p.locator("#lahtotasotesti .lt-h").bounding_box())
            answer(p, 1, False)
            acts = card(p, 1).locator(".lt-actions")
            rev = acts.locator("a.lt-revise")
            expect(f"{tag}: a wrong answer shows '{L['lt_revise']}' to the chapter of the feedback and '{L['lt_next']}'", acts.is_visible() and rev.inner_text() == L["lt_revise"] and rev.get_attribute("href") == "fy1-3.html" and acts.locator("button.lt-next").inner_text() == L["lt_next"], acts.inner_text() if acts.count() else "none")
            expect(f"{tag}: the module counts the answer", p.locator("details.lt-mod").first.locator(".lt-count").inner_text() == "1/3")
            if w == 1280:   # keyboard: Tab to the button, Enter
                card(p, 1).locator("button.lt-next").focus(); p.keyboard.press("Enter"); p.wait_for_timeout(200)
                expect(f"{tag}: Enter on '{L['lt_next']}' opens the next task and closes this one", p.evaluate("[...document.querySelectorAll('details.lt-mod details.opt[open] .activity')].map(e => e.id).join()") == "testi-2" and p.evaluate("document.activeElement.closest('details.opt').querySelector('.activity').id") == "testi-2")
            else:
                card(p, 1).locator("button.lt-next").click(); p.wait_for_timeout(200)
                expect(f"{tag}: the next task opens", p.evaluate("[...document.querySelectorAll('details.lt-mod details.opt[open] .activity')].map(e => e.id).join()") == "testi-2")
            answer(p, 2, True)
            expect(f"{tag}: a right answer has the next step and no revision link", card(p, 2).locator(".lt-actions a.lt-revise").count() == 0 and card(p, 2).locator(".lt-actions button.lt-next").count() == 1)
            p.reload(); p.wait_for_timeout(400)
            expect(f"{tag}: after a reload the test goes on from the first task not answered, the count kept", p.evaluate("[...document.querySelectorAll('details.lt-mod details.opt[open] .activity')].map(e => e.id).join()") == "testi-3"
                   and p.locator("details.lt-mod").first.locator(".lt-count").inner_text() == "2/3" and card(p, 1).locator(".lt-actions a.lt-revise").count() == 1)
            answer(p, 3, True)
            sm = p.locator("details.lt-mod").first.locator(".lt-sum")
            expect(f"{tag}: the module's end says what to revise (the chapter of the wrong answer) and where to go on", sm.is_visible() and L["lt_review"] in sm.inner_text() and sm.locator("a[href='fy1-3.html']").count() == 1 and sm.locator("button.lt-next").inner_text() == L["lt_next"], sm.inner_text())
            sm.locator("button.lt-next").click(); p.wait_for_timeout(200)
            expect(f"{tag}: it leads to the first task of the next module", p.evaluate("[...document.querySelectorAll('details.lt-mod[open]')].map(e => e.dataset.mod).join()") == "FY2" and p.evaluate("[...document.querySelectorAll('details.lt-mod details.opt[open] .activity')].map(e => e.id).join()") == "testi-4")
            answer(p, 4, False)   # a wrong number: the revision link is the task's own chapter although the feedback may not name one
            expect(f"{tag}: a wrong number also has '{L['lt_revise']}'", card(p, 4).locator(".lt-actions a.lt-revise").count() == 1, card(p, 4).inner_text()[-200:])
            expect(f"{tag}: no new storage key; no error; no overflow", not errs and p.evaluate("document.scrollingElement.scrollWidth - innerWidth") <= 1 and all((k.startswith("fl:") or k.startswith("ruukkilabra:")) and "lahtotaso" not in k and "-lt" not in k for k in p.evaluate("Object.keys(localStorage)")), (errs, p.evaluate("Object.keys(localStorage)")))
            expect(f"{tag}: buttons and links 44 px high", all(e.bounding_box()["height"] >= 44 for e in p.locator(".lt-actions a, .lt-actions button").all() if e.is_visible()))
            c.close()
        # a student who answered before this change: the same keys are read and the test goes on after them
        c = b.new_context(viewport={"width": 360, "height": 740}); p = c.new_page(); p.goto(BASE + pre + "fy9-koe.html")
        right = [i for i, ch in enumerate(ACTS["testi-1"]["choices"]) if ch.get("correct")]
        p.evaluate("""([k, v, lk, lv]) => { localStorage.setItem(k, v); localStorage.setItem(lk, lv); }""", ["fl:fy9-koe.html:testi-1", json.dumps({"choice": 0, "text": "x", "html": "x", "why": ""}),
                   "ruukkilabra:fy9-valmentaja", json.dumps({"v": 1, "log": [["2026-11-20T18:04Z", "fy9-koe#testi-1", "a", "no", 1, 0, 0, "p"]]})])
        p.goto("about:blank"); p.goto(BASE + pre + "fy9-koe.html#testi-ohje"); p.wait_for_timeout(400)
        expect(f"{lang}: answered under the earlier page: counted, with its revision link, and the first task not answered is open", p.locator("details.lt-mod").first.locator(".lt-count").inner_text() == "1/3"
               and card(p, 1).locator(".lt-actions a.lt-revise").count() == 1 and p.evaluate("[...document.querySelectorAll('details.lt-mod details.opt[open] .activity')].map(e => e.id).join()") == "testi-2")
        p.goto("about:blank"); p.goto(BASE + pre + "fy9-koe.html#testi-5"); p.wait_for_timeout(300)
        expect(f"{lang}: a link to one task (#testi-5) opens it", p.evaluate("document.getElementById('testi-5').closest('details.opt').open && document.getElementById('testi-5').closest('details.lt-mod').open"))
        c.close()
    b.close()
srv.shutdown()
print("all ok" if not fails else f"{fails} FAILED"); sys.exit(1 if fails else 0)
