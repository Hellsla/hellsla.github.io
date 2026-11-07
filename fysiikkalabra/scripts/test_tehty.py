"""Annetut tehtävät, Tehty and Oma eteneminen (teacher 2026-11-07; templates/tehty.js, build.py assigned_block,
scripts/assigned.py). Usage: python scripts/test_tehty.py [site]

In a browser on the built FY3 pages:
  - annetut.json: counts per module, unique ids, no extension task, no FY9/FY10/FY14 (assigned.py check)
  - the chapter's assigned exercises (and only they) have the green left edge and "Annettu" beside the number, and the
    "Tehty" box at the right end of the head row before "Avaa isoksi"; fi, en, fi-easy
  - the whole chain: an empty editor, a number in Tarkista or an opened model solution do not allow Tehty; a saved
    solution does; the ISO time is kept; the chapter's counter and the module page (counter, bar, graph) follow at once;
    a reload keeps it; an untick, a new tick (a new time), Poista ratkaisu and an emptied editor take it off; a task
    counts once; storage cleared in the browser leaves no stale tick
  - the submission file (version 4) has the module's assigned tasks, the ticks with their times and the history
  - the backup of Tallennetut ratkaisut carries the ticks to another browser
  - no horizontal overflow at 360, 768 and 1280 px
Exit status 1 on any failure."""
import functools, http.server, json, pathlib, re, sys, threading
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
errs = assigned.check(data)
expect("annetut.json: counts, unique ids, no extension tasks, FY1-FY8 only", not errs, errs)
main = {k: len([i for i in v if i not in assigned.shorts("FY3", k)]) for k, v in data["FY3"].items()}   # short answer-only tasks on top (teacher 2026-11-07)
expect("FY3 has 70-75 assigned tasks, 4-5 per chapter, short answer-only tasks on top", 70 <= sum(main.values()) <= 75 and set(main.values()) <= {4, 5}, main)
for code in ("FY9", "FY10", "FY14"):
    expect(f"{code} has no assigned tasks and its pages no tracker", code not in data and not any("tehty.js" in p.read_text() for p in SITE.glob(f"{code.lower()}-*.html")))
FY3 = [i for v in data["FY3"].values() for i in v]
CH = data["FY3"]["fy3-1"]


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/"
OPEN = "document.querySelectorAll('#exercises details.level').forEach((d) => { d.open = true; })"
STATE = "JSON.parse(localStorage.getItem('ruukkilabra:tehty') || 'null')"

with sync_playwright() as p:
    b = launch(p)
    ctx = b.new_context(accept_downloads=True, viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.on("dialog", lambda d: d.accept())
    for lang in ("", "en/", "fi-easy/"):
        pg.goto(BASE + lang + "fy3-1.html"); pg.evaluate(OPEN)
        marks = pg.evaluate("""() => [...document.querySelectorAll('#exercises li[id]')].filter((li) => li.classList.contains('assigned')).map((li) => {
            const h = li.querySelector(':scope > .ex-head'), kids = [...h.children];
            return { id: li.id, tag: kids[1] && kids[1].matches('.ex-given') ? kids[1].textContent : '', border: getComputedStyle(li).borderLeftWidth,
                     done: kids.findIndex((k) => k.matches('.ex-done')), big: kids.findIndex((k) => k.matches('.ex-big')), bg: getComputedStyle(kids[1]).backgroundColor }; })""")
        others = pg.evaluate("[...document.querySelectorAll('#exercises li[id]:not(.assigned)')].filter((li) => li.querySelector('.ex-given, .ex-done') || getComputedStyle(li).borderLeftWidth !== '0px').length")
        word = "Assigned" if lang == "en/" else "Annettu"
        expect(f"{lang or 'fi/'}fy3-1: exactly the assigned tasks are marked: '{word}' right after the number, a 3 px green edge, no tinted tag", [m["id"] for m in marks] == CH and others == 0
               and all(m["tag"] == word and m["border"] == "3px" and m["bg"] == "rgba(0, 0, 0, 0)" for m in marks), (marks, others))
        expect(f"{lang or 'fi/'}fy3-1: 'Tehty' at the right end of the head row, before 'Avaa isoksi'", all(0 < m["done"] < m["big"] for m in marks), marks)
        expect(f"{lang or 'fi/'}fy3-1: Tehtävät opens with the chapter's counter", pg.inner_text("#exercises .done-count") == (f"0/{len(CH)} assigned tasks done" if lang == "en/" else f"0/{len(CH)} annettua tehtävää tehty"), pg.inner_text("#exercises .done-count"))

    pg.goto(BASE + "fy3-1.html"); pg.evaluate(OPEN)
    num_task = next(i for i in CH if pg.evaluate(f"!!document.querySelector('[id=\"{i}\"] form.check')"))
    box = lambda i: pg.locator(f'[id="{i}"] .ex-done input')
    msg = lambda i: pg.inner_text(f'[id="{i}"] .ex-done-msg') if pg.locator(f'[id="{i}"] .ex-done-msg').is_visible() else ""

    def tick(i):
        box(i).click()
        pg.wait_for_function(f"!document.querySelector('[id=\"{i}\"] .ex-done input').disabled")
        pg.wait_for_timeout(100)

    # 1. an empty editor, a number in Tarkista, the model solution opened: no Tehty
    tick(num_task)
    expect("an empty editor: Tehty is refused with the reason", not box(num_task).is_checked() and "Kirjoita ensin" in msg(num_task), msg(num_task))
    pg.fill(f'[id="{num_task}"] form.check input', "12"); pg.click(f'[id="{num_task}"] form.check button')
    pg.evaluate(f"document.querySelectorAll('[id=\"{num_task}\"] details').forEach((d) => d.open = true)")
    tick(num_task)
    expect("a number in Tarkista and the model solution opened are not enough", not box(num_task).is_checked() and (pg.evaluate(STATE) or {"done": {}})["done"] == {}, pg.evaluate(STATE))
    # 2. a saved solution: Tehty with an ISO time; counter, reload
    pg.click(f'[id="{num_task}"] .pad-open'); pg.wait_for_selector(f'[id="{num_task}"] .rich-text-editor')
    pg.locator(f'[id="{num_task}"] .rich-text-editor').click(); pg.keyboard.type("Oma ratkaisu: m = 4,0 kg")
    tick(num_task)
    st = pg.evaluate(STATE)
    t1 = (st or {}).get("done", {}).get(num_task, "")
    expect("a saved solution (written just before, saved before the tick): Tehty with an ISO 8601 time", box(num_task).is_checked() and len(t1) == 24 and t1.endswith("Z") and t1[10] == "T", st)
    expect("the chapter's counter follows at once", pg.inner_text("#exercises .done-count") == f"1/{len(CH)} annettua tehtävää tehty")
    pg.reload(); pg.evaluate(OPEN); pg.wait_for_timeout(400)
    expect("a reload keeps the tick", box(num_task).is_checked() and pg.inner_text("#exercises .done-count") == f"1/{len(CH)} annettua tehtävää tehty")
    # 3. a picture alone is a solution (a formula or a picture is an image in the editor's HTML); a second task
    other = next(i for i in CH if i != num_task)
    pg.evaluate(f"""() => new Promise((ok) => {{ const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = ok; document.head.append(s); }})""")
    pg.evaluate(f"window.flPadStore.put('{other}', '<img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAEElEQVR4nGP4z8AARAwQCgAf7gP9i18U1AAAAABJRU5ErkJggg==\">', 'fy3-1.html')")
    tick(other)
    expect("a solution of a picture only counts too", box(other).is_checked())
    # 4. the module page
    mp = ctx.new_page(); mp.on("pageerror", lambda e: errors.append(str(e)))
    mp.goto(BASE + "FY3.html")
    total = len(FY3)
    expect("module page: the progress is behind one button 'Näytä edistyminen', closed (teacher 2026-11-07)", mp.is_visible(".my-wrap > summary") and mp.inner_text(".my-wrap > summary") == "Näytä edistyminen"
           and not mp.evaluate("document.querySelector('.my-wrap').open"))
    mp.click(".my-wrap > summary")
    pos = mp.evaluate("(() => { const s = document.getElementById('oma-eteneminen'), h = document.querySelector('main h1'), l = [...document.querySelectorAll('main h2')].find((x) => !s.contains(x)); return !s.hidden && !!(h.compareDocumentPosition(s) & 4) && !!(s.compareDocumentPosition(l) & 4); })()")
    expect("module page: Oma eteneminen after the heading, before the chapters", pos)
    # Oma itsearvio beside it (teacher 2026-11-07): the verbal statements assessed and the fingerprint under the themes
    mp.evaluate("localStorage.setItem('ruukkilabra:itsearvio:fy3-1', JSON.stringify({ items: { 'tavoite-1': { level: 'a' }, 'tavoite-3': { level: 'd' }, 'tehtava-x': { level: 'b' } } }))")
    mp.reload(); mp.evaluate("document.querySelectorAll('.my-wrap').forEach((d) => { d.open = true; })")
    goals = sum(len(c.get("goals", [])) for c in json.loads(mp.evaluate("document.getElementById('fl-course').textContent"))["chapters"])
    cells = mp.evaluate("[...document.querySelectorAll('#oma-itsearvio .sm-grid .sm-cell:not(.sm-gap)')].map((c) => c.dataset.level || '')")
    themes = mp.evaluate("[...document.querySelectorAll('#oma-itsearvio .sm-theme')].map((t) => t.textContent)")
    expect("module page: Oma itsearvio counts the verbal statements only (2/N) and colours their cells; the themes above the columns",
           goals >= 40 and mp.inner_text(".sm-count") == f"2/{goals} väitettä arvioitu" and len(cells) == goals and sorted(c for c in cells if c) == ["a", "d"]
           and themes[0] == "Voima, työ ja lämpötila" and len(themes) == 4, (mp.inner_text(".sm-count"), goals, themes))
    mp.evaluate("localStorage.removeItem('ruukkilabra:itsearvio:fy3-1')")
    expect(f"module page: '2/{total} tehtävää tehty' and the bar", mp.evaluate("document.querySelector('.pm-count').textContent") == f"2/{total} tehtävää tehty" and mp.get_attribute(".pm-bar", "aria-valuenow") == "2"
           and abs(float(mp.evaluate("document.querySelector('.pm-bar > span').style.width").rstrip("%")) - 100 * 2 / total) < 0.01, mp.evaluate("document.querySelector('.pm-count').textContent"))
    mp.click(".pm-graph > summary"); mp.wait_for_selector(".pm-chart svg", timeout=3000)
    g = mp.evaluate("(() => { const s = document.querySelector('.pm-chart svg'); return s && { dots: s.querySelectorAll('.pm-dot').length, path: s.querySelector('.pm-line').getAttribute('d'), ticks: [...s.querySelectorAll('.pm-tick')].map((t) => t.textContent) }; })()")
    expect(f"module page: the graph by date, cumulative up to {total}", g and g["dots"] == 1 and str(total) in g["ticks"] and g["path"].startswith("M"), g)
    # 5. untick, a new tick gets a new time; counted once
    tick(num_task)
    expect("an untick takes the mark off and the module page follows (another tab)", not box(num_task).is_checked() and mp.evaluate("document.querySelector('.pm-count').textContent") == f"1/{total} tehtävää tehty", mp.evaluate("document.querySelector('.pm-count').textContent"))
    pg.wait_for_timeout(20); tick(num_task)
    st = pg.evaluate(STATE); t2 = st["done"].get(num_task, "")
    expect("a new tick gets a new time; the task counts once; the log keeps tick, untick, tick", t2 > t1 and list(st["done"]).count(num_task) == 1
           and [x[2] for x in st["log"] if x[0] == num_task] == [1, 0, 1] and pg.inner_text("#exercises .done-count") == f"2/{len(CH)} annettua tehtävää tehty", st)
    # 6. the module's work file (teacher 2026-11-07): the same from a chapter and from the module page
    pg.fill('[id="fy3-2-L1-01"] form.check input', "1") if pg.locator('[id="fy3-2-L1-01"]').count() else None
    btns = pg.evaluate("[...document.querySelectorAll('#exercises .split-head > button, #exercises .split-head > a')].map((e) => e.textContent.trim())")
    expect("chapter: Tallenna työ tiedostoon, Palauta, then the side view button; no 'Lataa kaikki ratkaisut'", btns[:2] == ["Tallenna työ tiedostoon", "Palauta"] and len(btns) == 3 and "Lataa kaikki ratkaisut" not in pg.inner_text("#exercises"), btns)
    pg.evaluate("localStorage.setItem('ruukkilabra:itsearvio:fy3-2', JSON.stringify({v: 1, items: {'tavoite-1': {level: 'b', history: [['b', '2026-11-06T10:00:00.000Z']]}}}))")
    pg.evaluate("window.flPadStore.put('fy3-2-L2-01', 'Toisen luvun ratkaisu', 'fy3-2.html')")
    try:
        with pg.expect_download(timeout=15000) as d: pg.click("#exercises button.palautus-btn >> nth=0")
    except Exception:
        print("status:", pg.inner_text(".palautus-status")); raise
    name = d.value.suggested_filename
    f = json.loads(pathlib.Path(d.value.path()).read_text())
    work_path = pathlib.Path(d.value.path())
    pr = f.get("progress") or {}
    chs = {c["chapter"]: c for c in f.get("chapters", [])}
    expect("the file is Ruukkilabra_FY3_<date>_<time>.json", bool(re.fullmatch(r"Ruukkilabra_FY3_\d{4}-\d\d-\d\d_\d{6}\.json", name)), name)
    expect("one file for the whole module: every chapter with work (fy3-1 and fy3-2), not only this one", f.get("format") == "ruukkilabra-tyo" and f.get("course") == "FY3" and {"fy3-1", "fy3-2"} <= set(chs)
           and "fy3-2-L2-01" in [a["task"] for a in chs["fy3-2"]["answers"]] and chs["fy3-2"]["selfassessment"]["goals"] == [{"id": "tavoite-1", "text": "", "level": "b"}], list(chs))
    expect("the file has the ticks with their times, the history, the creation time and what this browser keeps", pr.get("course") == "FY3" and pr.get("assigned") == FY3
           and dict(pr.get("done", [])) == {num_task: t2, other: st["done"][other]} and [x[2] for x in pr.get("history", []) if x[0] == num_task] == [1, 0, 1]
           and f.get("created", "").endswith("Z") and any(r["id"] == num_task for r in f["store"]["solutions"]) and any(k.startswith("ruukkilabra:vastaukset:") for k in f["store"]["local"]), {k: v for k, v in pr.items() if k != "assigned"})
    expect("only this module's data in the file", all(r["id"].startswith("fy3-") for r in f["store"]["solutions"]) and not any("fy4-" in k for k in f["store"]["local"]))
    # the module page: the same file and Avaa tallennettu työ
    mp.goto(BASE + "FY3.html"); mp.evaluate("document.querySelectorAll('.my-wrap').forEach((d) => { d.open = true; })")
    mb = mp.evaluate("[...document.querySelectorAll('#oma-tyo button')].map((b) => b.textContent)")
    expect("module page: Tallenna työ tiedostoon and Avaa tallennettu työ, no text under them", mb == ["Tallenna työ tiedostoon", "Avaa tallennettu työ"] and mp.inner_text("#oma-tyo").strip() == "Tallenna työ tiedostoon\nAvaa tallennettu työ".replace("\n", "\n"), (mb, mp.inner_text("#oma-tyo")))
    with mp.expect_download(timeout=15000) as d2: mp.click("#oma-tyo button >> nth=0")
    f2 = json.loads(pathlib.Path(d2.value.path()).read_text())
    expect("module page: the same file (same content and checksum, a new creation time)", f2["content_sha256"] == f["content_sha256"] and f2["store"] == f["store"] and f2["chapters"] == f["chapters"])
    # 7. another computer: open the work on the module page, then continue in a chapter
    ctx2 = b.new_context(viewport={"width": 1280, "height": 900}); p2 = ctx2.new_page(); mode = ["accept"]; asked = []
    p2.on("dialog", lambda d: (asked.append(d.message), d.accept() if mode[0] == "accept" else d.dismiss())); p2.on("pageerror", lambda e: errors.append(str(e)))
    p2.goto(BASE + "FY3.html"); p2.evaluate("document.querySelectorAll('.my-wrap').forEach((d) => { d.open = true; })")
    def open_work(page, path):
        with page.expect_file_chooser() as fc: page.click("#oma-tyo button >> nth=1")
        with page.expect_navigation(): fc.value.set_files(str(path))
        page.wait_for_timeout(600)
    bad = work_path.with_name("muutettu.json"); g = json.loads(work_path.read_text()); g["store"]["solutions"][0]["html"] += "x"; bad.write_text(json.dumps(g))
    with p2.expect_file_chooser() as fc: p2.click("#oma-tyo button >> nth=1")
    fc.value.set_files(str(bad)); p2.wait_for_timeout(600)
    expect("a changed or damaged file is refused before anything is written", "vioittunut" in p2.inner_text("#oma-tyo") and p2.evaluate("localStorage.getItem('ruukkilabra:tehty')") is None, p2.inner_text("#oma-tyo"))
    open_work(p2, work_path)
    expect("another browser: the module page shows the progress back and says what was opened", p2.evaluate("document.querySelector('.pm-count').textContent") == f"2/{total} tehtävää tehty" and "avattiin" in p2.inner_text("#oma-tyo"), (p2.evaluate("document.querySelector('.pm-count').textContent"), p2.inner_text("#oma-tyo")))
    p2.goto(BASE + "fy3-1.html"); p2.evaluate(OPEN); p2.wait_for_timeout(400)
    p2.click(f'[id="{num_task}"] .pad-open'); p2.wait_for_selector(f'[id="{num_task}"] .rich-text-editor')
    expect("another browser: the solutions, the ticks and the chapter's counter are back", "Oma ratkaisu" in p2.inner_text(f'[id="{num_task}"] .rich-text-editor') and p2.locator(f'[id="{num_task}"] .ex-done input').is_checked()
           and p2.inner_text("#exercises .done-count") == f"2/{len(CH)} annettua tehtävää tehty", p2.inner_text("#exercises .done-count"))
    # a newer solution in this browser is not overwritten by accident: Cancel keeps it
    p2.locator(f'[id="{num_task}"] .rich-text-editor').click(); p2.keyboard.press("End"); p2.keyboard.type(" UUSI"); p2.wait_for_timeout(1300)
    mode[0] = "dismiss"
    p2.goto(BASE + "FY3.html"); p2.evaluate("document.querySelectorAll('.my-wrap').forEach((d) => { d.open = true; })")
    open_work(p2, work_path)
    p2.goto(BASE + "fy3-1.html"); p2.evaluate(OPEN); p2.click(f'[id="{num_task}"] .pad-open'); p2.wait_for_selector(f'[id="{num_task}"] .rich-text-editor')
    expect("opening an older file asks first; Peruuta keeps this browser's newer solution", asked and "uudempia" in asked[-1] and "UUSI" in p2.inner_text(f'[id="{num_task}"] .rich-text-editor'), (asked, p2.inner_text(f'[id="{num_task}"] .rich-text-editor')))
    ctx2.close()
    # 8. deleting the saved solution takes the tick off
    pg.click(f'[id="{num_task}"] .pad-open'); pg.wait_for_selector(f'[id="{num_task}"] .pad-delete')
    pg.click(f'[id="{num_task}"] .pad-delete'); pg.wait_for_timeout(400)
    expect("Poista ratkaisu takes the tick off, with a note", not box(num_task).is_checked() and "poistui" in msg(num_task) and num_task not in pg.evaluate(STATE)["done"], msg(num_task))
    # an emptied editor too
    pg.locator(f'[id="{num_task}"] .rich-text-editor').click(); pg.keyboard.type("uusi ratkaisu"); pg.wait_for_timeout(1200); tick(num_task)
    pg.locator(f'[id="{num_task}"] .rich-text-editor').click(); pg.keyboard.press("Control+a"); pg.keyboard.press("Delete"); pg.wait_for_timeout(1500)
    expect("an editor emptied by the student takes the tick off", not box(num_task).is_checked() and num_task not in pg.evaluate(STATE)["done"], pg.evaluate(STATE)["done"])
    # 9. the browser's saved solutions cleared: no stale tick when a page opens
    mp.evaluate("""() => new Promise((ok) => { const r = indexedDB.deleteDatabase('ruukkilabra-ratkaisut'); r.onsuccess = r.onerror = r.onblocked = () => ok(); })""")
    pg.close()
    mp.reload(); mp.wait_for_timeout(800)
    expect("solutions cleared from the browser: the module page drops the ticks", mp.evaluate("document.querySelector('.pm-count').textContent") == f"0/{total} tehtävää tehty", mp.evaluate("document.querySelector('.pm-count').textContent"))
    # 10. layout
    for w in (360, 768, 1280):
        for page in ("fy3-1.html", "FY3.html"):
            mp.set_viewport_size({"width": w, "height": 900}); mp.goto(BASE + page)
            if page == "FY3.html": mp.evaluate("document.querySelectorAll('.my-wrap').forEach((d) => { d.open = true; })"); mp.click(".pm-graph > summary"); mp.evaluate("localStorage.setItem('ruukkilabra:tehty', JSON.stringify({v:1, done:{'%s':'2026-11-01T10:00:00.000Z','%s':'2026-11-05T10:00:00.000Z'}, log:[]}))" % (FY3[0], FY3[7])); mp.wait_for_timeout(200)
            else: mp.evaluate(OPEN)
            over = mp.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
            heads = mp.evaluate("[...document.querySelectorAll('#exercises li.assigned .ex-head')].filter((h) => h.scrollWidth > h.clientWidth + 1).length") if page != "FY3.html" else 0
            expect(f"{page} at {w} px: no horizontal overflow, the head row fits", over <= 0 and heads == 0, (over, heads))
    # 11. FY1-FY9 but FY3 (teacher 2026-11-07): the same view on the module page only, over every task of the module, a task
    # with a saved solution counting as done; no marks or Tehty boxes on the tasks; FY9 has it too (no work file)
    c3 = b.new_context(viewport={"width": 1280, "height": 900}); q = c3.new_page(); q.on("pageerror", lambda e: errors.append(str(e)))
    q.goto(BASE + "fy1-1.html"); q.evaluate(OPEN)
    expect("FY1 chapter page: no Annettu marks, no Tehty boxes, no counter", q.locator("li.assigned, .ex-done, .done-count").count() == 0 and q.locator("script[src*='tehty.js']").count() == 0)
    t1 = q.evaluate("document.querySelector('#exercises li[id]').id")
    q.evaluate("(id) => new Promise((ok) => { const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = () => window.flPadStore.put(id, 'Oma ratkaisu', 'fy1-1.html').then(ok); document.head.append(s); })", t1)
    first = q.evaluate("JSON.parse(localStorage.getItem('ruukkilabra:ratkaistu') || '{}')")
    expect("a solution's first save is remembered for the graph (and kept on a later save)", isinstance(first.get(t1), str) and q.evaluate("(id) => window.flPadStore.put(id, 'Muutettu', 'fy1-1.html').then(() => JSON.parse(localStorage.getItem('ruukkilabra:ratkaistu'))[id])", t1) == first[t1])
    # an answer-only task counts once every Tarkista of it has been checked, right or wrong ("Tee molemmat", 2026-11-07)
    t2 = q.evaluate("(t1) => { const li = [...document.querySelectorAll('#exercises li[id]')].find((l) => l.id !== t1 && l.querySelector('form.check') && !l.querySelector('fieldset')); if (!li) return '';"
                    " li.querySelectorAll('form.check').forEach((f) => { f.querySelector('input').value = '1'; f.requestSubmit(); }); return li.id; }", t1)
    chk = q.evaluate("JSON.parse(localStorage.getItem('ruukkilabra:tarkistettu') || '{}')")
    expect("a task whose every number answer is checked is remembered as checked", bool(t2) and isinstance(chk.get(t2, {}).get("done"), str), (t2, chk))
    for code, has_work in (("FY1", True), ("FY9", False)):
        q.goto(BASE + code + ".html"); q.wait_for_timeout(600)
        n_all = sum(len(c["tasks"]) for c in json.loads(q.evaluate("document.getElementById('fl-course').textContent"))["chapters"])
        q.click(".my-wrap > summary"); q.wait_for_timeout(300)
        cnt = q.inner_text(".pm-count")
        expect(f"{code}: Näytä edistyminen counts every task of the module ({cnt}), Oma itsearvio beside it", n_all > 50 and cnt == f"{2 if code == 'FY1' else 0}/{n_all} tehtävää tehty"
               and q.is_visible("#oma-itsearvio") and q.locator("#oma-itsearvio .sm-cell:not(.sm-gap)").count() > 20 and (q.locator("#oma-tyo").count() == 1) == has_work, (cnt, n_all))
    q.evaluate("(id) => window.flPadStore ? window.flPadStore.remove(id) : null", t1)
    c3.close()
    expect("no script errors", not errors, errors)
    b.close()
srv.shutdown()
sys.exit(1 if fails else 0)
