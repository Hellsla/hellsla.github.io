"""FY9 exam mode and the minikokeet (work queue 11b PR 6; templates/koetila.js, scripts/koetila.py, docs/FY9_ADAPTIVE_PLAN.md 6.4).
Usage: python scripts/test_koetila.py [site|preview]   (default: site, else preview)

Static: the texts of the three languages, the minikoe pages (one per set of kertaus/FY9.json, cut out of the unit pages), the sidecar budgets.
In the browser (fi; the texts of en and fi-easy):
  - locks: before the exam is started and while it runs, the page holds no hint, no feedback, no model answer, no solution and nothing a check
    compares with; the practice exam page is as it was until the exam mode is started
  - the clock: counts down, is plain text (no live region), is not stopped by a reload, is stopped by Tauko (also over a reload), and the exam ends
    when the time is out; a polite status says only 10, 5 and 1 minute
  - choices: a task in a group is chosen before it can be answered, at most the group's number, and not taken back once it has an answer
  - ending: the answers are back, the numbers and choices are checked once, the points never pass the maximum, the unchosen are marked, the
    time per task and one summary row ("exams") are kept, the attempts are logged with the mode k, and a second load checks nothing again
  - nothing to store: the exam mode is not offered; the page does not break
  - the coach page lists the sets in the order of the goal (B-A 30 min first, L-E 60 min and the practice exam first)
Exit status 1 on any failure."""
import functools, http.server, json, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import koetila, valmentaja
from _browser import launch
from playwright.sync_api import sync_playwright

args = sys.argv[1:]
SITE = ROOT / (args[0] if args and (ROOT / args[0]).is_dir() else ("site" if (ROOT / "site" / "fy9-minikoe-m60-osa2-1.html").is_file() else "preview"))
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


# ---- static ----
for lang in ("fi", "en", "fi-easy"):
    d = json.loads((ROOT / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
    k = d.get("koetila", {})
    need = set(koetila.UI_KEYS) | {"eyebrow", "mini_lead", "nojs", "panel_lead", "title_osa1", "title_aihe", "title_osa2", "title_aineisto", "choose_rule", "answer_rule"}
    expect(f"{lang}: every text of the exam mode is there", need <= set(k), sorted(need - set(k)))
    expect(f"{lang}: the page's texts use {{{{name}}}}, the script's {{name}}", "{{minutes}}" in k["mini_lead"] and "{{name}}" in k["title_aihe"] and "{t}" in k["left"] and "{got}" in k["points"] and "{n}" in k["warn"])
    expect(f"{lang}: the coach list has its texts", all(d["coach"].get(x) for x in ("mini_h", "mini_item", "mini_exam")))
expect("the sidecar's budgets hold", not koetila.check(), koetila.check())
src = (SITE / "koetila.js").read_text()
code = re.sub(r"//.*", "", re.sub(r"/\*.*?\*/", "", src, flags=re.S))
expect("no network call", not [w for w in ("fetch", "XMLHttpRequest", "sendBeacon", "WebSocket", "EventSource", "importScripts", "new Image") if w in code])
expect("the clock is no live region", "'aria-live', 'off'" in src and "setAttribute('role', 'timer')" in src and not re.search(r"time\.setAttribute\('aria-live', 'polite'", src))
expect("no sound and no animation", "Audio" not in code and "animation" not in code and "requestAnimationFrame" not in code)

index = json.loads((SITE / "valmentaja" / "fy9.json").read_text(encoding="utf-8"))
minis = index["minikokeet"]
expect("the index has the sets and the practice exam's exam mode", len(minis) == 12 and index["koetila"]["fy9-harjoituskoe"] == {"minutes": 360, "points": 120}, index.get("koetila"))
for m in minis:
    f = SITE / f"fy9-minikoe-{m['id']}.html"
    h = f.read_text(encoding="utf-8") if f.is_file() else ""
    n = h.count('data-kt="')
    expect(f"{m['id']}: a page with its {len(m.get('short', [])) + len(m.get('long', []))} cards", n == len(m.get("short", [])) + len(m.get("long", [])) and 'id="koetila"' in h and "<noscript>" in h)
    spec = json.loads(re.search(r"data-spec='([^']*)'", h).group(1).replace("&quot;", '"').replace("&#x27;", "'")) if h else {}
    expect(f"{m['id']}: {m['points']} points and {m['minutes']} min", spec.get("pts") == m["points"] and spec.get("minutes") == m["minutes"], (spec.get("pts"), spec.get("minutes")))
for lang in ("en", "fi-easy"):
    expect(f"{lang}: a minikoe page", (SITE / lang / "fy9-minikoe-m30-osa1-1.html").is_file())


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/"
EKEY, VKEY, SKEY = "ruukkilabra:fy9-koetila", "ruukkilabra:fy9-valmentaja", "ruukkilabra:fy9-tavoite"
LOCKED = ".hints, details.solution, details.reveal, .feedback, .model, .solution-text, .practice-hint, .pending, .commit, .mc-score, [data-correct], [data-answer], [data-mistakes], [data-tol]"
OSA2, OSA1 = "fy9-minikoe-m60-osa2-1.html", "fy9-minikoe-m30-osa1-1.html"
read = lambda pg, key: pg.evaluate("(k) => { const v = localStorage.getItem(k); return v === null ? null : JSON.parse(v); }", key)


def tamper(pg, page, mid, fields):
    """Change the stored record while the exam page is not open (its own pagehide would write its state over the change), then open the page."""
    pg.goto(BASE + "index.html")
    pg.evaluate("([k, id, f]) => { const o = JSON.parse(localStorage.getItem(k)); Object.assign(o.exams[id], eval('(' + f + ')')); localStorage.setItem(k, JSON.stringify(o)); }", [EKEY, mid, fields])
    pg.goto(BASE + page)


def secs(text):
    m = re.match(r"(?:(\d+):)?(\d+):(\d\d)", text.strip())
    return (int(m.group(1) or 0) * 3600 + int(m.group(2)) * 60 + int(m.group(3))) if m else None


with sync_playwright() as p:
    br = launch(p)

    def fresh(width=390, **kw):
        ctx = br.new_context(viewport={"width": width, "height": 900}, **kw)
        pg = ctx.new_page(); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("dialog", lambda d: d.accept())
        return ctx, pg, errs

    # ---- the locks, the clock, the choices, the ending (a 60 minute Osa II set) ----
    ctx, pg, errs = fresh()
    pg.goto(BASE + OSA2); pg.wait_for_timeout(500)
    expect("before the start: the cards are hidden and hold nothing that helps", pg.locator("#kt-tasks").is_hidden() and pg.locator(LOCKED).count() == 0, pg.locator(LOCKED).count())
    expect("before the start: one Aloita button", pg.locator(".kt-go").count() == 1)
    pg.click(".kt-go"); pg.wait_for_timeout(1200)
    expect("running: no hint, feedback, model answer or solution is in the page", pg.locator(LOCKED).count() == 0, pg.locator(LOCKED).count())
    body = pg.inner_text("body")
    expect("running: the words of the locked parts are not on the page", not re.search(r"Näytä ratkaisu|Vihje \d|Näytä mallivastaus", body), body[:200])
    t0 = secs(pg.inner_text(".kt-time"))
    expect("running: the clock counts down from the set's time", t0 is not None and 3590 <= t0 <= 3600, pg.inner_text(".kt-time"))
    expect("running: the clock is a timer without a live region", pg.get_attribute(".kt-time", "role") == "timer" and pg.get_attribute(".kt-time", "aria-live") == "off" and pg.locator(".kt-bar [aria-live]:not([aria-live=off])").count() == 0)
    expect("running: one polite status, empty until a minute mark", pg.locator(".kt-live[role=status][aria-live=polite]").count() == 1 and (pg.text_content(".kt-live") or "").strip() == "")
    longs = pg.locator("[data-kt][data-unit] .kt-pick")
    expect("running: both long tasks have Valitse tämä, answers are blocked until chosen",
           longs.count() == 2 and all(pg.evaluate("(i) => document.querySelectorAll('.kt-body')[i].inert", i) for i in (0, 1)))
    longs.nth(0).click()
    expect("a chosen task opens; the other one cannot be chosen too (1 of 2)", pg.evaluate("() => !document.querySelectorAll('.kt-body')[0].inert") and longs.nth(1).is_disabled() and pg.evaluate("() => document.querySelectorAll('.kt-body')[1].inert"))
    longs.nth(0).click()
    expect("a chosen task with no answer can be taken back, and then the other can be chosen", longs.nth(1).is_enabled())
    longs.nth(0).click()
    pg.fill('[data-kt="fy9-liike#potkulauta"] input[type=text]', "22,5")
    pg.locator('[data-kt="fy9-koe#testi-2"] input[type=radio]').first.click()
    pg.wait_for_timeout(700)
    pg.reload(); pg.wait_for_timeout(1200)
    t1 = secs(pg.inner_text(".kt-time"))
    expect("a reload keeps the answers and the choice", pg.input_value('[data-kt="fy9-liike#potkulauta"] input[type=text]') == "22,5" and pg.locator('[data-kt="fy9-koe#testi-2"] input[type=radio]:checked').count() == 1
           and longs.nth(0).get_attribute("aria-pressed") == "true")
    expect("a reload does not restart the clock", t1 is not None and t1 < t0 and t0 - t1 < 15, (t0, t1))
    expect("the locks hold after the reload", pg.locator(LOCKED).count() == 0)
    pg.click(".kt-pause"); pg.wait_for_timeout(300)
    a = secs(pg.inner_text(".kt-time")); pg.wait_for_timeout(2300)
    expect("Tauko stops the clock", secs(pg.inner_text(".kt-time")) == a and pg.inner_text(".kt-pause") == "Jatka")
    pg.reload(); pg.wait_for_timeout(1000)
    expect("a pause survives a reload", pg.inner_text(".kt-pause") == "Jatka" and secs(pg.inner_text(".kt-time")) == a)
    pg.click(".kt-pause"); pg.wait_for_timeout(2300)
    expect("Jatka starts it again", secs(pg.inner_text(".kt-time")) < a)
    pg.locator('[data-kt="fy9-liike#potkulauta"] input[type=text]').focus(); pg.wait_for_timeout(1500)
    pg.click(".kt-end"); pg.wait_for_selector(".kt-result", timeout=8000); pg.wait_for_timeout(3500)
    expect("ended: the page is the practice page again, with its feedback and solutions", pg.locator("details.solution").count() > 0 and pg.locator(".feedback").count() > 0)
    pts = re.search(r"([\d,]+) / (\d+)", pg.inner_text(".kt-points"))
    got, mx = float(pts.group(1).replace(",", ".")), int(pts.group(2))
    expect("ended: the number was checked and its two points counted; the total is within the maximum", mx == 21 and 2 <= got <= mx, pg.inner_text(".kt-points"))
    expect("ended: the answers are back", pg.input_value('[data-kt="fy9-liike#potkulauta"] input[type=text]') == "22,5")
    expect("ended: the task that was not chosen is marked and its points are not counted", pg.locator(".kt-tag").count() == 1)
    expect("ended: the time table has a row per task", pg.locator(".kt-table tbody tr").count() == 5)
    v = read(pg, VKEY)
    rows = [r for r in v["log"] if r[1] == "fy9-liike#potkulauta"]
    expect("the number's attempt is logged once, as an exam attempt, the first, with its key", len(rows) == 1 and rows[0][2:5] == ["a", "ok", 1] and rows[0][7] == "k", rows)
    expect("one summary row of the exam, with the chosen tasks and the time per task",
           len(v.get("exams", [])) == 1 and "fy9-liike#potkulauta" in v["exams"][0]["chosen"] and v["exams"][0]["id"] == "m60-osa2-1" and "fy9-liike#potkulauta" in v["exams"][0]["times"], v.get("exams"))
    n_before = len(v["log"])
    pg.reload(); pg.wait_for_selector(".kt-result"); pg.wait_for_timeout(2500)
    expect("a second load of the ended page checks and logs nothing again", len(read(pg, VKEY)["log"]) == n_before and len(read(pg, VKEY)["exams"]) == 1)
    expect("no script error", not errs, errs)
    # the long task: the student's own points, the total stays within the maximum
    pg.evaluate("() => { const c = document.querySelector('[data-kt][data-written]'); if (c) c.dispatchEvent(new CustomEvent('fl:written')); }")
    pg.evaluate("() => document.querySelectorAll('[data-kt] details.reveal').forEach((d) => { d.removeAttribute('data-locked'); d.open = true; })")
    pg.evaluate("() => { const seen = new Set(); document.querySelectorAll('.rubric input').forEach((i) => { if (i.disabled) return; const k = i.name; const same = [...document.querySelectorAll(`.rubric input[name=\"${k}\"]`)]; if (seen.has(k)) return; seen.add(k); const top = same.reduce((a, b) => (Number(b.value) > Number(a.value) ? b : a)); top.click(); }); }")
    pg.wait_for_timeout(500)
    pts = re.search(r"([\d,]+) / (\d+)", pg.inner_text(".kt-points"))
    expect("the best own points of the chosen long task count, the total never passes the maximum", float(pts.group(1).replace(",", ".")) <= int(pts.group(2)) == 21 and float(pts.group(1).replace(",", ".")) > got, pg.inner_text(".kt-points"))
    pg.click(".kt-again"); pg.wait_for_timeout(1000)
    expect("Tee uudelleen takes the result away and the exam can be started again", pg.locator(".kt-go").count() == 1 and (read(pg, EKEY) or {"exams": {}})["exams"].get("m60-osa2-1") is None)
    ctx.close()

    # ---- a group of short tasks: 5 of 6 (Osa I) ----
    ctx, pg, errs = fresh()
    pg.goto(BASE + OSA1); pg.click(".kt-go"); pg.wait_for_timeout(1200)
    picks = pg.locator(".kt-pick")
    expect("Osa I: six tasks to choose from", picks.count() == 6)
    for i in range(5): picks.nth(i).click()
    expect("Osa I: at most five can be chosen", picks.nth(5).is_disabled() and all(picks.nth(i).is_enabled() for i in range(5)))
    pg.locator('[data-kt] input[type=radio]').first.click()
    first = pg.locator("[data-kt]").first
    pg.wait_for_timeout(600)
    expect("Osa I: a task with an answer cannot be taken back", picks.nth(0).is_disabled())
    expect("Osa I: the five are the exam's; the sixth is blocked until one is free", picks.nth(5).is_disabled() and picks.nth(1).is_enabled())
    ctx.close()

    # ---- the time runs out ----
    ctx, pg, errs = fresh()
    pg.goto(BASE + OSA1); pg.click(".kt-go"); pg.wait_for_timeout(1000)
    tamper(pg, OSA1, "m30-osa1-1", "{spent: 1800000 - 2500, tick: Date.now()}")
    pg.wait_for_selector(".kt-result", timeout=10000)
    expect("the time out ends the exam and says so", "Aika loppui" in pg.inner_text(".kt-line") and read(pg, EKEY)["exams"]["m30-osa1-1"]["reason"] == "time")
    expect("the time out is in the summary", read(pg, VKEY)["exams"][0]["id"] == "m30-osa1-1")
    ctx.close()
    ctx, pg, errs = fresh()
    pg.goto(BASE + OSA1); pg.click(".kt-go"); pg.wait_for_timeout(800)
    tamper(pg, OSA1, "m30-osa1-1", "{spent: 1800000 - 1000, tick: Date.now() - 5 * 3600000}")
    pg.wait_for_selector(".kt-result", timeout=8000)
    expect("a tab closed past the time: the exam is over when the page opens again", "Aika loppui" in pg.inner_text(".kt-line"))
    ctx.close()

    # ---- the minute marks, once each, said politely ----
    ctx, pg, errs = fresh()
    pg.goto(BASE + OSA1); pg.click(".kt-go"); pg.wait_for_timeout(800)
    tamper(pg, OSA1, "m30-osa1-1", "{spent: 1800000 - 600000 + 1500, tick: Date.now()}")
    pg.wait_for_timeout(2600)
    expect("ten minutes left: the status says so", "10" in (pg.text_content(".kt-live") or ""), pg.text_content(".kt-live"))
    ctx.close()

    # ---- the practice exam: as before until started, then the same locks ----
    ctx, pg, errs = fresh(1280)
    pg.goto(BASE + "fy9-harjoituskoe.html"); pg.wait_for_timeout(700)
    expect("the practice exam: a panel with one button, the page as before (the solutions and model answers are there)", pg.locator("#koetila .kt-go").is_visible() and pg.locator("details.solution").count() > 0 and pg.locator("details.reveal").count() > 0)
    pg.click("#koetila .kt-go"); pg.wait_for_timeout(1500)
    expect("the practice exam, running: the locks hold", pg.locator(LOCKED).count() == 0, pg.locator(LOCKED).count())
    spec = json.loads(pg.get_attribute("#koetila", "data-spec"))
    expect("the practice exam: 360 min, 120 points, Osa II 4 of 7, Osa III 2 of 3", spec["minutes"] == 360 and spec["pts"] == 120 and {g["id"]: g["choose"] for g in spec["groups"]} == {"osa-ii": 4, "osa-iii": 2}, spec["groups"])
    picks = pg.locator(".kt-pick")
    expect("the practice exam: ten tasks to choose from", picks.count() == 10, picks.count())
    for i in range(4): picks.nth(i).click()
    expect("the practice exam: the fifth of Osa II is blocked", picks.nth(4).is_disabled() and picks.nth(7).is_enabled())
    pg.click(".kt-end"); pg.wait_for_selector(".kt-result", timeout=8000); pg.wait_for_timeout(3500)
    pts = re.search(r"([\d,]+) / (\d+)", pg.inner_text(".kt-points"))
    expect("the practice exam, ended: the page is as before again, the total within 120", int(pts.group(2)) == 120 and float(pts.group(1).replace(",", ".")) <= 120 and pg.locator("details.solution").count() > 0 and pg.locator("details.reveal").count() > 0)
    ctx.close()

    # ---- the three languages ----
    for lang, start, left in (("en", "Start the exam", "left"), ("fi-easy", "Aloita koe", "jäljellä")):
        ctx, pg, errs = fresh()
        pg.goto(BASE + f"{lang}/{OSA1}"); pg.wait_for_timeout(600)
        ok = pg.inner_text(".kt-go") == start
        pg.click(".kt-go"); pg.wait_for_timeout(1200)
        expect(f"{lang}: the page starts, locks and counts", ok and pg.locator(LOCKED).count() == 0 and pg.inner_text(".kt-time").endswith(left) and not errs, (pg.inner_text(".kt-time"), errs))
        ctx.close()

    # ---- nothing to store ----
    ctx, pg, errs = fresh()
    pg.add_init_script("Object.defineProperty(window, 'localStorage', { get() { throw new Error('blocked'); } });")
    pg.goto(BASE + OSA1); pg.wait_for_timeout(700)
    expect("no storage: no start button, a note, no script error, the cards stay hidden", pg.locator(".kt-go").count() == 0 and pg.locator(".koetila .notice").count() == 1 and pg.locator("#kt-tasks").is_hidden())
    ctx.close()

    # ---- the coach page: the order of the goal ----
    ctx, pg, errs = fresh()
    pg.goto(BASE + "FY9-valmentaja.html"); pg.wait_for_timeout(600)
    kinds = lambda goal: pg.evaluate("(g) => window.flCoach.miniOrder(JSON.parse(document.getElementById('fy9-index').textContent), g).map((x) => x.kind)", goal)
    dedup = lambda xs: [x for i, x in enumerate(xs) if i == 0 or xs[i - 1] != x]
    expect("the order without a goal and for M-C: Osa I, Osa II, topics, data, the practice exam", dedup(kinds(None)) == ["osa1", "osa2", "aihe", "aineisto", "exam"] and dedup(kinds("MC")) == dedup(kinds(None)), kinds(None))
    expect("the order for B-A: the 30 minute sets first", dedup(kinds("BA")) == ["osa1", "aihe", "osa2", "aineisto", "exam"], kinds("BA"))
    expect("the order for L-E: the 60 minute sets and the practice exam earlier", dedup(kinds("LE")) == ["osa2", "aineisto", "exam", "osa1", "aihe"], kinds("LE"))
    expect("the order keeps each kind's own order and lists every set once", len(kinds("LE")) == 13 and len(set(pg.evaluate("() => window.flCoach.miniOrder(JSON.parse(document.getElementById('fy9-index').textContent), 'LE').map((x) => x.id)"))) == 13)
    expect("the list is a closed box on the coach page", pg.locator("#coach-mini").count() == 1 and pg.get_attribute("#coach-mini", "open") is None and pg.locator("#coach-mini a").count() == 13)
    for goal, first in (("LE", "fy9-minikoe-m60-osa2-1.html"), ("BA", "fy9-minikoe-m30-osa1-1.html")):
        pg.evaluate("(g) => localStorage.setItem('" + SKEY + "', JSON.stringify({ v: 1, goal: g, courses: [] }))", goal)
        pg.reload(); pg.wait_for_timeout(500)
        expect(f"the coach page lists {goal}'s first set first", pg.get_attribute("#coach-mini a >> nth=0", "href") == first, pg.get_attribute("#coach-mini a >> nth=0", "href"))
    pg.evaluate(f"() => localStorage.setItem('{EKEY}', JSON.stringify({{ v: 1, exams: {{}} }}))")
    pg.evaluate(f"() => localStorage.setItem('{VKEY}', JSON.stringify({{ v: 1, log: [] }}))")
    pg.reload(); pg.wait_for_timeout(500)
    pg.click(".coach-clear"); pg.wait_for_timeout(800)
    expect("Tyhjennä takes the exam mode's key away too", pg.evaluate(f"() => localStorage.getItem('{EKEY}')") is None)
    ctx.close()
    br.close()

print(f"\n{fails} failure(s)" if fails else "\nkoetila: all checks passed")
sys.exit(1 if fails else 0)
