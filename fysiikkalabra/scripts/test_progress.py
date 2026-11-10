"""The progress bar of a lesson page (templates/lesson.js part 2 and site.css nav.toc; teacher 2026-11-03: "kiinteä
etenemispalkki").
Usage: python scripts/test_progress.py [site] [page ...]

In a browser, on fy4-4 in every language (or the pages named), at 360, 768 and 1280 px:
  - the stage navigation sticks under the top edge at every width and stays in view when the page is scrolled
  - the stage on screen is marked (aria-current) as the page is scrolled (IntersectionObserver)
  - below 700 px the chips are folded into one button that names the stage on screen ("4/7 Teoria") and opens every
    stage on its own row under the bar; choosing one goes there and closes the list (design audit 2026-11-10; the bar
    scrolled sideways inside itself until then, and still does without JavaScript); the page never scrolls sideways
  - every stage but the last ends with a Seuraavaksi link to the next one
  - a stage is marked done (a tick and a hidden "(tehty)") once its required answers are given (Vastaa / Tarkista),
    optional tasks do not count, and the state is kept in localStorage under ruukkilabra:<page> and restored on reload
  - without JavaScript the bar is a plain list of links and there is no Kuuntele button
Exit status 1 on any failure."""
import functools, http.server, json, sys, threading, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n
from _browser import launch

args = sys.argv[1:]
SITE = ROOT / (args.pop(0) if args and (ROOT / args[0]).is_dir() else "site")
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


targets = args or [p for p in ("fy4-4.html", "en/fy4-4.html", "fi-easy/fy4-4.html") if (SITE / p).is_file()]


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_address[1]}/"

CURRENT = "[...document.querySelectorAll('nav.toc a[aria-current]')].map(a => a.getAttribute('href'))"
DONE = "[...document.querySelectorAll('nav.toc a.is-done')].map(a => a.getAttribute('href'))"

from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = launch(pw)
    for page in targets:
        lang = page.split("/")[0] if "/" in page else i18n.SOURCE
        T = i18n.T(lang)
        key = "ruukkilabra:" + page[:-5]
        for w in (1280, 768, 360):
            tag = f"{page} {w}px"
            ctx = b.new_context(viewport={"width": w, "height": 800})
            pg = ctx.new_page(); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.goto(BASE + page); pg.wait_for_timeout(400)
            expect(f"{tag}: Pohdinta is marked at the top", pg.evaluate(CURRENT) == ["#herata"], pg.evaluate(CURRENT))
            for sid in ("selita", "sovella", "exercises"):
                pg.evaluate(f"document.getElementById('{sid}').scrollIntoView()"); pg.wait_for_timeout(350)
                st = pg.evaluate(f"""() => {{ const n = document.querySelector('nav.toc'), r = n.getBoundingClientRect(), a = n.querySelector('a[aria-current]');
                    const tools = n.querySelector('.toc-tools'), right = tools && !tools.hidden ? tools.getBoundingClientRect().left : r.right;
                    const ar = a && a.getBoundingClientRect();
                    // under 700 px the chips give way to one button that names the stage on screen, "4/7 Teoria" (2026-11-10)
                    const now = n.querySelector('.toc-now'), nr = now && now.getBoundingClientRect(), all = [...n.querySelectorAll('a[href^="#"]')];
                    const compact = !!now && getComputedStyle(now).display !== 'none';
                    const named = compact && !!a && now.querySelector('.toc-now-n').textContent === (all.indexOf(a) + 1) + '/' + all.length
                      && now.querySelector('.toc-now-l').textContent === a.querySelector('.toc-label').textContent && nr.left >= r.left - 1 && nr.right <= right + 1 && nr.height >= 44;
                    return {{ cur: {CURRENT}, top: Math.round(r.top), pos: getComputedStyle(n).position, compact,
                      seen: compact ? named : !!ar && ar.left >= r.left - 1 && ar.right <= right + 1, sw: document.documentElement.scrollWidth, iw: innerWidth }}; }}""")
                expect(f"{tag}: at {sid} the bar is stuck at the top, marks {sid}, shows it, and the page does not scroll sideways",
                       st["cur"] == ["#" + sid] and st["top"] == 0 and st["pos"] == "sticky" and st["seen"] and st["sw"] <= st["iw"], st)
            if w < 700:
                # the bar no longer scrolls sideways under 700 px (design audit 2026-11-10: three of seven chips showed, with
                # no sign of the rest): one button names the stage, and opens every stage on its own row under the bar
                st = pg.evaluate("""() => { const n = document.querySelector('nav.toc'), links = [...n.querySelectorAll('a[href^="#"]')];
                    const vis = () => links.filter(a => a.offsetParent).length; const before = vis();
                    n.querySelector('.toc-now').click(); const open = vis(), rows = links.every(a => a.getBoundingClientRect().height >= 44 && a.getBoundingClientRect().right <= innerWidth);
                    const exp = n.querySelector('.toc-now').getAttribute('aria-expanded');
                    return { before, open, total: links.length, rows, exp, sw: document.documentElement.scrollWidth, iw: innerWidth }; }""")
                expect(f"{tag}: the chips are folded into one button; it opens every stage on a 44 px row, and the page does not scroll sideways",
                       st["before"] == 0 and st["open"] == st["total"] >= 5 and st["rows"] and st["exp"] == "true" and st["sw"] <= st["iw"], st)
                pg.click('nav.toc a[href="#selita"]'); pg.wait_for_timeout(700)
                st = pg.evaluate(f"""() => {{ const n = document.querySelector('nav.toc'); return {{ cur: {CURRENT}, open: n.classList.contains('is-open'),
                    shown: [...n.querySelectorAll('a[href^="#"]')].filter(a => a.offsetParent).length, top: Math.round(document.getElementById('selita').getBoundingClientRect().top), bar: Math.round(n.getBoundingClientRect().bottom) }}; }}""")
                expect(f"{tag}: choosing a stage goes there, closes the list, and the stage's heading is not under the bar",
                       st["cur"] == ["#selita"] and not st["open"] and st["shown"] == 0 and st["top"] >= st["bar"] - 2, st)
                pg.click(".toc-now"); pg.keyboard.press("Escape")
                expect(f"{tag}: Esc closes the list", pg.evaluate("!document.querySelector('nav.toc').classList.contains('is-open')"))
            else:
                expect(f"{tag}: from 700 px the chips show and there is no stage button", pg.evaluate("getComputedStyle(document.querySelector('.toc-now')).display === 'none' && [...document.querySelectorAll('nav.toc a[href^=\"#\"]')].every(a => a.offsetParent)"))
            nx = pg.evaluate("""() => { const links = [...document.querySelectorAll('nav.toc a[href^="#"]')].map(a => a.getAttribute('href'));
                const rows = [...document.querySelectorAll('nav.next-stage a')].map(a => [a.closest('nav').previousElementSibling.id, a.getAttribute('href'), a.getBoundingClientRect().height >= 44]);
                return { links, rows, waiting: !!document.querySelector('#ennusta + nav.next-stage.is-waiting') }; }""")
            # after Ennusta the link waits for the predictions (teacher 2026-11-10): until then it points back at the stage
            want = [[a[1:], ("#ennusta" if a == "#ennusta" and nx["waiting"] else b)] for a, b in zip(nx["links"], nx["links"][1:])]
            expect(f"{tag}: every stage but the last ends with a Seuraavaksi link to the next one (44 px)", [[r[0], r[1]] for r in nx["rows"]] == want and all(r[2] for r in nx["rows"]), nx["rows"])
            if w == 1280:
                pg.evaluate("scrollTo(0, 0)"); pg.wait_for_timeout(200)
                # optional tasks do not count: answering the optional Pohdinta question marks nothing
                pg.evaluate("document.querySelectorAll('#herata details.opt fieldset.choice').forEach(fs => { fs.querySelector('input[type=radio]').checked = true; fs.querySelector('button.commit').click(); })")
                pg.wait_for_timeout(100)
                expect(f"{tag}: an optional task does not mark a stage done", "#herata" not in pg.evaluate(DONE), pg.evaluate(DONE))
                pg.evaluate("document.querySelector('#ennusta details.fold').open = true")
                n = pg.evaluate("document.querySelectorAll('#ennusta fieldset.choice:not(details.opt *)').length")
                pg.evaluate("[...document.querySelectorAll('#ennusta fieldset.choice:not(details.opt *)')].slice(0, -1).forEach(fs => { fs.querySelector('input[type=radio]').checked = true; fs.querySelector('button.commit').click(); })")
                pg.wait_for_timeout(100)
                # the prediction at its experiment (teacher 2026-11-10): the experiment a prediction waits for shows it under its heading
                pe = pg.evaluate("""() => [...document.querySelectorAll('#ennusta fieldset.choice[data-reveal]')].map(fs => { const box = document.querySelector('[id="' + fs.dataset.reveal + '"] .exp-pred');
                    const sel = fs.querySelector('input:checked'), given = !!fs.dataset.committed; const txt = box ? box.textContent : null;
                    return { box: !!box, given, shows: given && !!sel && !!txt && txt.includes(sel.parentElement.textContent.trim().slice(0, 25)), asks: !given && !!box && !!box.querySelector('a[href="#' + fs.closest('.activity').id + '"]') }; })""")
                expect(f"{tag}: each experiment shows the prediction made for it, and a link to make the one still missing", all(x["box"] and (x["shows"] if x["given"] else x["asks"]) for x in pe), pe)
                expect(f"{tag}: Ennusta is not done before every prediction is given", n < 2 or "#ennusta" not in pg.evaluate(DONE), pg.evaluate(DONE))
                wait = pg.evaluate("(() => { const r = document.querySelector('#ennusta + nav.next-stage'), a = r.querySelector('a'); return [r.classList.contains('is-waiting'), a.getAttribute('href'), a.textContent.trim() === document.querySelector('#ennusta .fold-title').textContent.trim(), !!document.querySelector('nav.toc a[href=\"#tutki\"]').offsetParent]; })()")
                expect(f"{tag}: until then the row after Ennusta asks for the predictions and does not lead on, while the stage bar still does", wait == [True, "#ennusta", True, True], wait)
                pg.evaluate("[...document.querySelectorAll('#ennusta fieldset.choice:not(details.opt *)')].slice(-1).forEach(fs => { fs.querySelector('input[type=radio]').checked = true; fs.querySelector('button.commit').click(); })")
                pg.evaluate("document.querySelectorAll('#exercises li.core form.check').forEach(f => { f.querySelector('input').value = '1'; f.requestSubmit(); })")
                # a core exercise can be a multiple choice (core path by skill, 2026-11-05): commit it with Vastaa
                pg.evaluate("document.querySelectorAll('#exercises li.core fieldset.choice').forEach(fs => { fs.querySelector('input[type=radio]').checked = true; fs.querySelector('button.commit').click(); })")
                pg.wait_for_timeout(150)
                done = pg.evaluate(DONE)
                expect(f"{tag}: Ennusta and Tehtävät are done once their required answers are checked", "#ennusta" in done and "#exercises" in done, done)
                go = pg.evaluate("(() => { const r = document.querySelector('#ennusta + nav.next-stage'), a = r.querySelector('a'); return [r.classList.contains('is-waiting'), a.getAttribute('href')]; })()")
                expect(f"{tag}: with the predictions given the row leads to Tutki", go == [False, "#tutki"], go)
                sr = pg.evaluate("document.querySelector('nav.toc a[href=\"#ennusta\"] .visually-hidden')?.textContent || ''")
                expect(f"{tag}: a done stage says so to a screen reader", T("js.stage_done") in sr, sr)
                saved = pg.evaluate(f"(() => {{ try {{ return JSON.parse(localStorage.getItem('{key}')); }} catch (e) {{ return null; }} }})()")
                expect(f"{tag}: the state is kept under {key}", bool(saved) and "ennusta" in saved.get("done", []), saved)
                pg.reload(); pg.wait_for_timeout(400)
                expect(f"{tag}: the done stages come back after a reload", set(done) <= set(pg.evaluate(DONE)), pg.evaluate(DONE))
                pg.evaluate("localStorage.clear()")
            expect(f"{tag}: no script errors", not errs, errs[:3])
            ctx.close()
        # without JavaScript: the links, no button
        ctx = b.new_context(viewport={"width": 360, "height": 800}, java_script_enabled=False)
        pg = ctx.new_page(); pg.goto(BASE + page)
        links = pg.locator("nav.toc a[href^='#']").count()
        expect(f"{page}: without JavaScript the bar is a list of links and there is no Kuuntele button", links >= 5 and pg.locator(".ra-start").count() == 0, links)
        ctx.close()
    b.close()
srv.shutdown()
print("FAIL" if fails else "PASS", f"({fails} failures)" if fails else "")
sys.exit(1 if fails else 0)
