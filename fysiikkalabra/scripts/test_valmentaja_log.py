"""FY9-valmentaja, the evidence log (work queue 11b PR 3; templates/valmentaja.js, docs/FY9_ADAPTIVE_PLAN.md 4.4, 7.1, 7.3).
Usage: python scripts/test_valmentaja_log.py [site]   (default: site, else preview with fy9-voimat built)

Static:  valmentaja.js is on the FY9 unit pages only; it makes no network call (R5: no fetch, XMLHttpRequest, sendBeacon, WebSocket,
         EventSource, Image, importScripts, form submit); the old fl:attempt fields are still in lesson.js
In a browser on fy9-voimat (fi):
  - a wrong number matching a common mistake -> one row "<unit>#<id>", way a, result no, first 1, hints 0, the mistake's number
  - a second attempt is a row with first 0 (no new result); also after a reload
  - an opened hint counts for the next attempt; a wrong choice logs the option's number; a right one null
  - a long task's rubric: one row of points got/max, 0 to 1, only when every criterion has points, changed points revise it
  - fl:attempt still carries id, kind and state; the page looks as before (no new element)
  - blocked or full storage does not break the page; a damaged or newer log is never overwritten
  - two tabs add to the same log; the module's work file carries the key to another browser
Exit status 1 on any failure."""
import functools, http.server, json, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

args = sys.argv[1:]
SITE = ROOT / (args[0] if args and (ROOT / args[0]).is_dir() else ("site" if (ROOT / "site" / "fy9-voimat.html").is_file() else "preview"))
KEY = "ruukkilabra:fy9-valmentaja"
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


src = (ROOT / "templates" / "valmentaja.js").read_text()
code = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
code = re.sub(r"//.*", "", code)
bad = [w for w in ("fetch", "XMLHttpRequest", "sendBeacon", "WebSocket", "EventSource", "importScripts", "new Image", "submit(", "navigator.", "document.cookie", "indexedDB") if w in code]
uses = sorted(set(re.findall(r"localStorage\.(\w+)", code)))
expect("valmentaja.js makes no network call and keeps nothing but its own key (R5)", not bad and uses == ["getItem", "removeItem", "setItem"] and KEY in code and "localStorage.removeItem(V.KEY)" in code, (bad, uses))
expect("the old fl:attempt fields id, kind and state are still sent (lesson.js)", "{ id: taskId(el), kind, state }" in (ROOT / "templates" / "lesson.js").read_text())
pages = sorted(SITE.rglob("*.html"))
with_js = sorted(p.relative_to(SITE).as_posix() for p in pages if "valmentaja.js" in p.read_text(errors="ignore"))
units = sorted(p.name for p in SITE.glob("fy9-*.html"))
expect("valmentaja.js is on FY9 unit pages with tasks, the coach page and the FY9 course page (its row), nowhere else", with_js and all(re.fullmatch(r"(?:(?:en|fi-easy)/)?(?:fy9-[a-z0-9-]+|FY9|FY9-valmentaja)\.html", n) for n in with_js), with_js[:6])
expect("a FY3 chapter and the front page do not load it", not any("valmentaja.js" in (SITE / n).read_text() for n in ("fy3-1.html", "index.html") if (SITE / n).is_file()))
if not (SITE / "fy9-voimat.html").is_file():
    print("FAIL fy9-voimat.html is not built in", SITE); sys.exit(1)


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/"
PAGE = BASE + "fy9-voimat.html"
LOG = f"() => {{ const v = localStorage.getItem('{KEY}'); return v === null ? null : JSON.parse(v).log; }}"
PADSTORE = "() => new Promise((ok) => { if (window.flPadStore) return ok(); const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = ok; document.head.append(s); })"


def check(pg, tid, value):
    f = pg.locator(f'[id="{tid}"] form.check').first
    f.locator("input").fill(value); f.locator("button").click(); pg.wait_for_timeout(60)


with sync_playwright() as p:
    b = launch(p)
    ctx = b.new_context(viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(PAGE)
    expect("the unit page defines flValmentaja and shows no new element", pg.evaluate("!!window.flValmentaja && document.querySelectorAll('[class*=valmentaja], [id*=valmentaja]').length === 0"))
    expect("no log before the first attempt", pg.evaluate(LOG) is None)
    ans = pg.evaluate("(() => { const f = document.querySelector('[id=\"nosturi\"] form.check'); return { a: Number(f.dataset.answer), m: JSON.parse(f.dataset.mistakes || '[]') }; })()")
    expect("the test task has a common mistake to hit", len(ans["m"]) >= 1, ans)
    pg.evaluate("window.__d = []; document.addEventListener('fl:attempt', (e) => window.__d.push(Object.assign({}, e.detail)))")
    check(pg, "nosturi", str(ans["m"][0]["value"]).replace(".", ","))
    log = pg.evaluate(LOG)
    expect("a wrong number that is a common mistake: one row, a, no, first 1, no hints, mistake 0, practice",
           log and len(log) == 1 and log[0][1:] == ["fy9-voimat#nosturi", "a", "no", 1, 0, 0, "p"] and re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\dZ", log[0][0]), log)
    d0 = pg.evaluate("document.querySelector('[id=\"nosturi\"] form.check').flLast")   # the detail object, filled in by inquiry.js a moment after the event
    expect("fl:attempt keeps id, kind and state and adds first and mistake", d0["id"] == "nosturi" and d0["kind"] == "check" and d0["state"] == "no" and d0["first"] is True and d0["mistake"] == 0, d0)
    check(pg, "nosturi", str(ans["a"]).replace(".", ","))
    log = pg.evaluate(LOG)
    expect("the second attempt is a row with first 0, result ok, no new first result", len(log) == 2 and log[1][1:] == ["fy9-voimat#nosturi", "a", "ok", 0, 0, None, "p"] and sum(r[4] for r in log) == 1, log)
    pg.reload(); pg.wait_for_timeout(200)
    check(pg, "nosturi", str(ans["a"]).replace(".", ","))
    log = pg.evaluate(LOG)
    expect("after a reload a new attempt is still not a first one", len(log) == 3 and log[2][4] == 0, log)
    # hints: opened ones count
    pg.evaluate("document.querySelectorAll('[id=\"vinoveto\"] details.hint').forEach((h, i) => { if (i < 2) h.open = true; })"); pg.wait_for_timeout(60)
    va = pg.evaluate("Number(document.querySelector('[id=\"vinoveto\"] form.check').dataset.answer)")
    check(pg, "vinoveto", str(va).replace(".", ","))
    log = pg.evaluate(LOG)
    expect("two opened hints are counted in the attempt after them (first 1, ok)", log[-1][1:] == ["fy9-voimat#vinoveto", "a", "ok", 1, 2, None, "p"], log[-1])
    # choice
    ch = pg.evaluate("(() => { const fs = document.querySelector('[id=\"lt-1\"] fieldset.choice'); const r = [...fs.querySelectorAll('input[type=radio]')]; return { right: r.findIndex((x) => x.dataset.correct === '1'), n: r.length }; })()")
    wrong = 0 if ch["right"] != 0 else 1
    pg.locator('[id="lt-1"] fieldset.choice input[type=radio]').nth(wrong).check()
    pg.locator('[id="lt-1"] fieldset.choice button').first.click(); pg.wait_for_timeout(60)
    log = pg.evaluate(LOG)
    expect("a wrong choice: the option's number is the mistake, first 1", log[-1][1:] == ["fy9-voimat#lt-1", "a", "no", 1, 0, wrong, "p"], log[-1])
    if pg.locator('[id="lt-1"] fieldset.choice button').first.is_visible():
        pg.locator('[id="lt-1"] fieldset.choice input[type=radio]').nth(ch["right"]).check()
        pg.locator('[id="lt-1"] fieldset.choice button').first.click(); pg.wait_for_timeout(60)
        log = pg.evaluate(LOG)
        expect("the right option on the second try: ok, first 0, no mistake", log[-1][1:] == ["fy9-voimat#lt-1", "a", "ok", 0, 0, None, "p"], log[-1])
    # rubric of a long task
    pg.evaluate("(() => { for (let d = document.querySelector('.rubric[data-id=\"fy9-voimat-s1\"]').closest('details'); d; d = d.parentElement.closest('details')) d.open = true; })()")
    n = pg.locator('.rubric[data-id="fy9-voimat-s1"] fieldset.crit').count()
    before = len(pg.evaluate(LOG))
    for i in range(n - 1):
        pg.locator('.rubric[data-id="fy9-voimat-s1"] fieldset.crit').nth(i).locator("label").last.click()
    expect("a rubric not yet complete logs nothing", len(pg.evaluate(LOG)) == before)
    pg.locator('.rubric[data-id="fy9-voimat-s1"] fieldset.crit').nth(n - 1).locator("label").first.click(); pg.wait_for_timeout(60)
    mx = pg.evaluate("Number(document.querySelector('.rubric[data-id=\"fy9-voimat-s1\"]').dataset.max)")
    got = pg.evaluate("[...document.querySelectorAll('.rubric[data-id=\"fy9-voimat-s1\"] input:checked')].reduce((a, i) => a + Number(i.value), 0)")
    log = pg.evaluate(LOG)
    expect("a complete rubric: one row, s, points got / max, first 1", len(log) == before + 1 and log[-1][1:4] == ["fy9-voimat-s1", "s", round(got / mx, 2)] and log[-1][4] == 1, (log[-1], got, mx))
    pg.locator('.rubric[data-id="fy9-voimat-s1"] fieldset.crit').nth(n - 1).locator("label").last.click(); pg.wait_for_timeout(60)
    got2 = pg.evaluate("[...document.querySelectorAll('.rubric[data-id=\"fy9-voimat-s1\"] input:checked')].reduce((a, i) => a + Number(i.value), 0)")
    log2 = pg.evaluate(LOG)
    expect("changed points revise the same row (the time and first stay)", len(log2) == before + 1 and log2[-1][3] == round(got2 / mx, 2) and log2[-1][0] == log[-1][0] and log2[-1][4] == 1, log2[-1])
    expect("no script error", not errors, errors)
    # two tabs
    pg2 = ctx.new_page(); pg2.goto(PAGE)
    n0 = len(pg.evaluate(LOG))
    check(pg2, "pulkkamaki", "1")
    check(pg, "lentopallo", "1")
    log = pg.evaluate(LOG)
    expect("two tabs: both attempts are in the one log", len(log) == n0 + 2 and {r[1] for r in log[-2:]} == {"fy9-voimat#pulkkamaki", "fy9-voimat#lentopallo"}, log[-2:])
    # the whole-work file (Tietosuoja, kaikki.js; FY9 has no module work file): the key goes with the FY9 work and comes back elsewhere
    import tempfile
    tmp = pathlib.Path(tempfile.mkdtemp())
    ctx_s = b.new_context(accept_downloads=True, viewport={"width": 1280, "height": 900})
    sp = ctx_s.new_page(); sp.goto(PAGE); sp.evaluate(f"localStorage.setItem('{KEY}', {json.dumps(json.dumps({'v': 1, 'log': log}))})")
    sp.goto(BASE + "tietosuoja.html"); sp.wait_for_selector("#kaikki-tyo .palautus-btn", state="attached")
    with sp.expect_download() as dl:
        sp.click("#kaikki-tyo .palautus-btn:first-child")
    path = tmp / dl.value.suggested_filename; dl.value.save_as(path)
    fd = json.loads(path.read_text())
    carried = ((fd.get("modules", {}).get("FY9") or {}).get("store") or {}).get("local", {})
    expect("the whole-work file holds the key in the FY9 module, whole", KEY in carried and json.loads(carried[KEY]) == {"v": 1, "log": log}, list(carried))
    ctx_s.close()
    ctx2 = b.new_context(accept_downloads=True); q = ctx2.new_page(); q.on("dialog", lambda d: d.accept()); q.goto(BASE + "tietosuoja.html")
    q.wait_for_selector("#kaikki-tyo input[type=file]", state="attached")
    q.set_input_files("#kaikki-tyo input[type=file]", str(path)); q.wait_for_timeout(800)
    q.goto(PAGE)
    back = q.evaluate(LOG)
    expect("opened in another browser the log is back, row for row", back == log, back)
    ctx2.close()
    # no storage
    ctx3 = b.new_context()
    ctx3.add_init_script("Storage.prototype.setItem = function () { throw new Error('QuotaExceededError'); }; Storage.prototype.getItem = function () { throw new Error('blocked'); };")
    t = ctx3.new_page(); e3 = []; t.on("pageerror", lambda e: e3.append(str(e))); t.goto(PAGE)
    check(t, "nosturi", str(ans["a"]).replace(".", ","))
    expect("blocked storage: the answer is still checked and the page works, the coach says it cannot keep",
           t.locator('[id="nosturi"] form.check output').inner_text() != "" and t.evaluate("window.flValmentaja.canStore()") is False and not e3, e3)
    ctx3.close()
    # a damaged log, and one of a newer version, are not overwritten
    for bad_value in ("{not json", json.dumps({"v": 2, "log": [], "x": 1})):
        ctx4 = b.new_context(); t = ctx4.new_page(); t.goto(PAGE); t.evaluate(f"localStorage.setItem('{KEY}', {json.dumps(bad_value)})")
        check(t, "nosturi", str(ans["a"]).replace(".", ","))
        expect(f"a log that cannot be read ({bad_value[:10]}…) stays as it is", t.evaluate(f"localStorage.getItem('{KEY}')") == bad_value)
        ctx4.close()
    # rows of the wrong shape are dropped on reading, the rest kept
    ctx5 = b.new_context(); t = ctx5.new_page(); t.goto(PAGE)
    t.evaluate(f"localStorage.setItem('{KEY}', JSON.stringify({{ v: 1, log: [['2026-11-20T18:04Z', 'fy9-voimat#nosturi', 'a', 'ok', 1, 0, null, 'p'], ['junk'], 'x', ['t', 'a', 'a', 'ok', 1, 0, null, 'p', 'extra']], cells: {{ k: 1 }} }}))")
    check(t, "nosturi", str(ans["a"]).replace(".", ","))
    d = t.evaluate(f"JSON.parse(localStorage.getItem('{KEY}'))")
    expect("rows of the wrong shape are dropped, the good one and the other fields kept", len(d["log"]) == 2 and d["log"][0][0] == "2026-11-20T18:04Z" and d["log"][1][4] == 0 and d["cells"] == {"k": 1}, d)
    ctx5.close()
    # the log is capped
    ctx6 = b.new_context(); t = ctx6.new_page(); t.goto(PAGE)
    t.evaluate(f"localStorage.setItem('{KEY}', JSON.stringify({{ v: 1, log: Array.from({{ length: 3000 }}, (_, i) => ['2026-11-20T18:04Z', 'fy9-koe#t' + i, 'a', 'ok', 1, 0, null, 'p']) }}))")
    check(t, "nosturi", str(ans["a"]).replace(".", ","))
    d = t.evaluate(f"JSON.parse(localStorage.getItem('{KEY}'))")
    expect("the log keeps at most 3000 rows, the newest", len(d["log"]) == 3000 and d["log"][-1][1] == "fy9-voimat#nosturi" and d["log"][0][1] == "fy9-koe#t1", len(d["log"]))
    ctx6.close()
    b.close()
print("FAILED" if fails else "all ok")
sys.exit(1 if fails else 0)
