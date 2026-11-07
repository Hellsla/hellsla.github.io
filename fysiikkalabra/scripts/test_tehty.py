"""Oma eteneminen and Oma itsearvio on the module pages (teacher 2026-11-07; templates/tehty.js, omaarvio.js,
build.py progress_view). Usage: python scripts/test_tehty.py [site]

FY1-FY9 all in one way since 2026-11-07 evening ("Muut FY3 tähän formaattiin"): no task is highlighted, the counter
behind "Näytä edistyminen" counts every task of the module. A task is done when its own solution is saved or every
Tarkista and Vastaa of it has been checked. annetut.json keeps the earlier FY3 list under _FY3, not in use.
In a browser on the built pages:
  - no module has assigned tasks; the chapter pages have no marks, no Tehty boxes, no counter
  - a solution's first save and a task's checked answers are remembered with their time
  - the module page (FY1, FY3, FY9): closed button, the counter over every task, the bar, the graph, Oma itsearvio with
    the themes over the columns; the work file buttons on FY1-FY8 only
  - the work file carries the progress to another browser; solutions cleared in the browser drop the count
  - no horizontal overflow at 360, 768 and 1280 px
Exit status 1 on any failure."""
import functools, http.server, json, pathlib, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
import assigned
from playwright.sync_api import sync_playwright

args = sys.argv[1:]
SITE = ROOT / (args[0] if args and (ROOT / args[0]).is_dir() else "site")
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


data = assigned.load()
expect("annetut.json: no module has assigned tasks (FY3's list kept under _FY3)", data == {} and not assigned.check(data), list(data))
pages = [p for i in range(1, 10) for p in SITE.glob(f"fy{i}-*.html")]
expect("no chapter page FY1-FY9 loads tehty.js or marks a task", len(pages) > 100 and not [p.name for p in pages if "tehty.js" in (t := p.read_text()) or 'class="assigned' in t or "ex-given" in t])


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/"
OPEN = "document.querySelectorAll('#exercises details.level').forEach((d) => { d.open = true; })"
WRAP = "document.querySelectorAll('.my-wrap').forEach((d) => { d.open = true; })"
PADSTORE = "() => new Promise((ok) => { if (window.flPadStore) return ok(); const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = ok; document.head.append(s); })"
COUNT = "document.querySelector('.pm-count').textContent"

with sync_playwright() as p:
    b = launch(p)
    ctx = b.new_context(accept_downloads=True, viewport={"width": 1280, "height": 900})
    q = ctx.new_page()
    errors = []
    q.on("pageerror", lambda e: errors.append(str(e)))
    q.on("dialog", lambda d: d.accept())
    for lang in ("", "en/", "fi-easy/"):
        q.goto(BASE + lang + "fy3-1.html"); q.evaluate(OPEN)
        expect(f"{lang or 'fi/'}fy3-1: no Annettu marks, no Tehty boxes, no counter", q.locator("li.assigned, .ex-given, .ex-done, .done-count").count() == 0
               and q.locator("script[src*='tehty.js']").count() == 0)
    # a saved solution: its first save is remembered for the graph (and kept on a later save)
    q.goto(BASE + "fy3-1.html"); q.evaluate(OPEN); q.evaluate(PADSTORE)
    t1 = q.evaluate("document.querySelector('#exercises li[id]').id")
    q.evaluate("(id) => window.flPadStore.put(id, 'Oma ratkaisu', 'fy3-1.html')", t1)
    first = q.evaluate("JSON.parse(localStorage.getItem('ruukkilabra:ratkaistu') || '{}')")
    expect("a solution's first save is remembered (and kept on a later save)", isinstance(first.get(t1), str) and q.evaluate("(id) => window.flPadStore.put(id, 'Muutettu', 'fy3-1.html').then(() => JSON.parse(localStorage.getItem('ruukkilabra:ratkaistu'))[id])", t1) == first[t1])
    # an answer-only task counts once every Tarkista of it has been checked, right or wrong ("Tee molemmat", 2026-11-07)
    t2 = q.evaluate("(t1) => { const li = [...document.querySelectorAll('#exercises li[id]')].find((l) => l.id !== t1 && l.querySelector('form.check') && !l.querySelector('fieldset')); if (!li) return '';"
                    " li.querySelectorAll('form.check').forEach((f) => { f.querySelector('input').value = '1'; f.requestSubmit(); }); return li.id; }", t1)
    chk = q.evaluate("JSON.parse(localStorage.getItem('ruukkilabra:tarkistettu') || '{}')")
    expect("a task whose every number answer is checked is remembered as checked", bool(t2) and isinstance(chk.get(t2, {}).get("done"), str), (t2, chk))
    # a task with a choice: Vastaa counts it once every part is answered
    t3 = q.evaluate("(skip) => { const li = [...document.querySelectorAll('#exercises li[id]')].find((l) => !skip.includes(l.id) && l.querySelector('fieldset.choice') && !l.querySelector('form.check, fieldset.tf, fieldset.order')); if (!li) return '';"
                    " li.querySelectorAll('fieldset.choice').forEach((fs) => { fs.querySelector('input[type=radio]').checked = true; fs.querySelector('button').click(); }); return li.id; }", [t1, t2])
    chk = q.evaluate("JSON.parse(localStorage.getItem('ruukkilabra:tarkistettu') || '{}')")
    expect("a multiple-choice task answered with Vastaa is remembered as checked", bool(t3) and isinstance(chk.get(t3, {}).get("done"), str), (t3, chk))
    # the module pages
    for code, done, goal, has_work in (("FY1", 0, 45, True), ("FY3", 3, 90, True), ("FY9", 0, 90, False)):
        q.goto(BASE + code + ".html"); q.wait_for_timeout(600)
        n_all = sum(len(c["tasks"]) for c in json.loads(q.evaluate("document.getElementById('fl-course').textContent"))["chapters"])
        closed = q.is_visible(".my-wrap > summary") and q.inner_text(".my-wrap > summary") == "Näytä edistyminen" and not q.evaluate("document.querySelector('.my-wrap').open")
        q.click(".my-wrap > summary"); q.wait_for_timeout(300)
        cnt = q.inner_text(".pm-count")
        expect(f"{code}: behind a closed 'Näytä edistyminen', the counter over every task with the goal 45 per op ({cnt}), Oma itsearvio beside it", closed and n_all > 50 and cnt == f"{done}/{n_all} tehtävää tehty · tavoite {goal}"
               and q.is_visible("#oma-itsearvio") and q.locator("#oma-itsearvio .sm-cell:not(.sm-gap)").count() > 20 and (q.locator("#oma-tyo").count() == 1) == has_work, (cnt, n_all))
    q.goto(BASE + "FY3.html"); q.evaluate(WRAP)
    total = sum(len(c["tasks"]) for c in json.loads(q.evaluate("document.getElementById('fl-course').textContent"))["chapters"])
    pos = q.evaluate("(() => { const s = document.getElementById('oma-eteneminen'), h = document.querySelector('main h1'), l = [...document.querySelectorAll('main h2')].find((x) => !s.contains(x)); return !s.hidden && !!(h.compareDocumentPosition(s) & 4) && !!(s.compareDocumentPosition(l) & 4); })()")
    expect("FY3: Oma eteneminen after the heading, before the chapters", pos)
    expect("FY3: the bar follows the counter", q.get_attribute(".pm-bar", "aria-valuenow") == "3" and abs(float(q.evaluate("document.querySelector('.pm-bar > span').style.width").rstrip("%")) - 100 * 3 / total) < 0.01)
    q.click(".pm-graph > summary"); q.wait_for_selector(".pm-chart svg", timeout=3000)
    g = q.evaluate("(() => { const s = document.querySelector('.pm-chart svg'); return s && { dots: s.querySelectorAll('.pm-dot').length, path: s.querySelector('.pm-line').getAttribute('d'), ticks: [...s.querySelectorAll('.pm-tick')].map((t) => t.textContent), goal: !!s.querySelector('line.pm-goal') }; })()")
    expect(f"FY3: the graph by date, cumulative up to {total}, the goal line at 90 (2 op)", g and g["dots"] == 1 and str(total) in g["ticks"] and "90" in g["ticks"] and "tavoite 90" in g["ticks"] and g["goal"] and g["path"].startswith("M"), g)
    # Oma itsearvio: the verbal statements assessed and the fingerprint under the themes
    q.evaluate("localStorage.setItem('ruukkilabra:itsearvio:fy3-1', JSON.stringify({ items: { 'tavoite-1': { level: 'a' }, 'tavoite-3': { level: 'd' }, 'tehtava-x': { level: 'b' } } }))")
    q.reload(); q.evaluate(WRAP)
    goals = sum(len(c.get("goals", [])) for c in json.loads(q.evaluate("document.getElementById('fl-course').textContent"))["chapters"])
    cells = q.evaluate("[...document.querySelectorAll('#oma-itsearvio .sm-grid .sm-cell:not(.sm-gap)')].map((c) => c.dataset.level || '')")
    themes = q.evaluate("[...document.querySelectorAll('#oma-itsearvio .sm-theme')].map((t) => t.textContent)")
    expect("FY3: Oma itsearvio counts the verbal statements only (2/N) and colours their cells; the themes above the columns",
           goals >= 40 and q.inner_text(".sm-count") == f"2/{goals} väitettä arvioitu" and len(cells) == goals and sorted(c for c in cells if c) == ["a", "d"]
           and themes[0] == "Voima, työ ja lämpötila" and len(themes) == 4, (q.inner_text(".sm-count"), goals, themes))
    # the work file carries the progress to another browser
    with q.expect_download(timeout=15000) as d: q.click("#oma-tyo button >> nth=0")
    work = pathlib.Path(d.value.path())
    f = json.loads(work.read_text())
    expect("FY3 work file: the module's solutions and checked answers, no assigned-task progress", f.get("format") == "ruukkilabra-tyo" and f.get("course") == "FY3" and f.get("progress") is None
           and any(r["id"] == t1 for r in f["store"]["solutions"]) and "ruukkilabra:tarkistettu" in f["store"]["local"], {k: f.get(k) for k in ("format", "course", "progress")})
    c2 = b.new_context(viewport={"width": 1280, "height": 900}); p2 = c2.new_page(); p2.on("dialog", lambda d: d.accept()); p2.on("pageerror", lambda e: errors.append(str(e)))
    p2.goto(BASE + "FY3.html"); p2.evaluate(WRAP)
    with p2.expect_file_chooser() as fc: p2.click("#oma-tyo button >> nth=1")
    with p2.expect_navigation(): fc.value.set_files(str(work))
    p2.wait_for_timeout(800); p2.evaluate(WRAP); p2.wait_for_timeout(300)
    expect("another browser: opening the work file brings the count back", p2.evaluate(COUNT) == f"3/{total} tehtävää tehty · tavoite 90", p2.evaluate(COUNT))
    c2.close()
    # solutions cleared in the browser: the saved-solution task drops, the checked ones stay
    q.evaluate("""() => new Promise((ok) => { const r = indexedDB.deleteDatabase('ruukkilabra-ratkaisut'); r.onsuccess = r.onerror = r.onblocked = () => ok(); })""")
    q.reload(); q.wait_for_timeout(800)
    expect("solutions cleared from the browser: only the checked tasks count", q.evaluate(COUNT) == f"2/{total} tehtävää tehty · tavoite 90", q.evaluate(COUNT))
    q.evaluate("localStorage.removeItem('ruukkilabra:itsearvio:fy3-1')")
    # layout
    for w in (360, 768, 1280):
        for page in ("fy3-1.html", "FY1.html", "FY3.html", "FY9.html"):
            q.set_viewport_size({"width": w, "height": 900}); q.goto(BASE + page)
            if page.startswith("FY"): q.evaluate(WRAP); q.click(".pm-graph > summary"); q.wait_for_timeout(200)
            else: q.evaluate(OPEN)
            over = q.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
            expect(f"{page} at {w} px: no horizontal overflow", over <= 0, over)
    expect("no script errors", not errors, errors)
    b.close()
srv.shutdown()
sys.exit(1 if fails else 0)
