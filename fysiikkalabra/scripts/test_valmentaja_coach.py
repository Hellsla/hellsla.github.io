"""FY9-valmentaja, the competence view and the recommendations (work queue 11b PR 4; templates/valmentaja.js, docs/FY9_ADAPTIVE_PLAN.md 5, 6, 7.3).
Usage: python scripts/test_valmentaja_coach.py [site|preview]   (default: site, else preview)

Golden cases (window.flCoach, the pure functions, on a small fixed index and fixed logs; a change of a weight shows as a change here):
  empty log, only self-assessment, a guesser, one weak topic, a revisit that is due, everything strong, a log of rows this index does not know,
  a tie, a follow-up task, the minutes left, no stuck topic, over the night, a day in the student's own time zone, folding old rows into cells,
  a second attempt that is not evidence
The pages (fi, en, fi-easy): the coach page and the row on the course page, without a script, with no data, with a log, with blocked storage,
  Tyhjennä, no network request, at 360 and 1280 px no overflow and every control 40 px or more
Exit status 1 on any failure."""
import functools, http.server, json, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

args = sys.argv[1:]
SITE = ROOT / (args[0] if args and (ROOT / args[0]).is_dir() else ("site" if (ROOT / "site" / "FY9-valmentaja.html").is_file() else "preview"))
KEY = "ruukkilabra:fy9-valmentaja"
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


if not (SITE / "FY9-valmentaja.html").is_file():
    print("FAIL FY9-valmentaja.html is not built in", SITE); sys.exit(1)


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/"


def task(i, unit, kind, comp, minutes, **kw):
    t = {"id": i, "unit": unit, "kind": kind, "check": "auto" if kind in ("choice", "numeric") else "self", "comp": comp, "min": minutes, "href": f"{unit}.html#{i.split('#')[-1]}", "title": i}
    t.update(kw); return t


INDEX = {"units": [{"id": u, "chapter": 1, "title": u, "n": f"1.{k}"} for k, u in enumerate(("fy9-a", "fy9-b", "fy9-c"), 1)], "tasks": [
    task("fy9-a#c1", "fy9-a", "choice", ["concept"], 2), task("fy9-a#n1", "fy9-a", "numeric", ["math"], 4, followups=["fy9-c#n1"]),
    task("fy9-a#n2", "fy9-a", "numeric", ["math"], 4), task("fy9-a#n3", "fy9-a", "numeric", ["math"], 4), task("fy9-a#e1", "fy9-a", "explain", ["communication"], 5),
    task("fy9-a-s1", "fy9-a", "long", {"math": 6, "concept": 4}, 30),
    task("fy9-b#n1", "fy9-b", "numeric", ["math"], 4), task("fy9-b#c1", "fy9-b", "choice", ["concept"], 2), task("fy9-b#c2", "fy9-b", "choice", ["concept"], 2),
    task("fy9-c#n1", "fy9-c", "numeric", ["math"], 4), task("fy9-c#c1", "fy9-c", "choice", ["concept"], 2)]}


def row(day, tid, way="a", result="ok", first=1, hints=0, mistake=None, mode="p", hour="10:00"):
    return [f"{day}T{hour}Z", tid, way, result, first, hints, mistake, mode]


def D(log, cells=None): return {"v": 1, "log": log, "cells": cells or {}}


with sync_playwright() as pw:
    b = launch(pw)
    ctx = b.new_context(timezone_id="Europe/Helsinki")
    pg = ctx.new_page()
    pg.goto(BASE + "FY9-valmentaja.html")
    ev = lambda f, *a: pg.evaluate(f, list(a))
    recommend = lambda d, today, o=None: ev("([i, d, t, o]) => window.flCoach.recommend(i, d, t, o)", INDEX, d, today, o)
    cells = lambda d, today: ev("([i, d, t]) => window.flCoach.cells(d.log, i, t, d.cells)", INDEX, d, today)
    ids = lambda r: [x["id"] for x in r["recs"]]

    # 1 an empty log: only the diagnostic is offered
    r = recommend(D([]), "2026-11-23")
    expect("an empty log: no recommendation, the diagnostic is offered", r["diag"] and r["recs"] == [], r)
    r = recommend(D([row("2026-11-01", "unknown#x")]), "2026-11-23")
    expect("rows of tasks this index does not know are no evidence", r["diag"], r)

    # 2 only self-assessment never gives Vahva and says so
    log = [row(f"2026-11-{d:02d}", "fy9-a-s1", "s", 0.9) for d in (10, 12, 14)] + [row("2026-11-16", "fy9-a-s1", "s", 0.9, first=1, hour="11:00")]
    c = cells(D(log), "2026-11-23")["fy9-a|math"]
    expect("four own assessments of 0.9 (weight 0.6): Kehittyy, by the student's own assessment, never Vahva", c["state"] == "growing" and c["own"], c)

    # 3 a guesser: right choices, one day, are not Vahva
    log = [row("2026-11-20", t) for t in ("fy9-b#c1", "fy9-b#c2", "fy9-a#c1")]
    c = cells(D(log), "2026-11-23")["fy9-b|concept"]
    expect("two right choices in one day: Näyttöä vähän (weight 0.7 each)", c["state"] == "few" and abs(c["W"] - 1.4) < 1e-9, c)
    log = [row("2026-11-18", "fy9-b#n1"), row("2026-11-19", "fy9-a#n1"), row("2026-11-20", "fy9-a#n2"), row("2026-11-21", "fy9-a#n3")]
    cs = cells(D(log), "2026-11-23")
    expect("right numbers on four days: fy9-a math is Vahva, 3 tasks on 3 days, not due yet", cs["fy9-a|math"]["state"] == "strong" and cs["fy9-a|math"]["n"] == 3 and cs["fy9-a|math"]["days"] == 3 and not cs["fy9-a|math"]["due"], cs["fy9-a|math"])
    expect("a topic with one right number is Näyttöä vähän", cs["fy9-b|math"]["state"] == "few", cs["fy9-b|math"])
    expect("a cell with no attempt is Ei vielä näyttöä", cs["fy9-c|math"]["state"] == "none", cs["fy9-c|math"])

    # 4 a second attempt is practice, not evidence
    log = [row("2026-11-20", "fy9-a#n1", result="no"), row("2026-11-20", "fy9-a#n1", first=0), row("2026-11-21", "fy9-a#n1", first=0)]
    c = cells(D(log), "2026-11-23")["fy9-a|math"]
    expect("only the first attempt counts: one wrong number, then two right ones that are practice", abs(c["W"] - 1) < 1e-9 and c["M"] == 0, c)

    # 5 one weak topic
    log = [row("2026-11-21", "fy9-a#n1", result="no", mistake=1), row("2026-11-22", "fy9-a#n2", result="no")]
    c = cells(D(log), "2026-11-23")["fy9-a|math"]
    expect("two wrong numbers: Harjoittele", c["state"] == "practise" and c["M"] == 0, c)
    r = recommend(D(log), "2026-11-23")
    expect("the follow-up of a task that went wrong is among the three, with that reason", any(x["id"] == "fy9-c#n1" and x["reason"]["key"] == "wrong" for x in r["recs"]), r["recs"])
    expect("the tasks touched in the last 7 days are not recommended", not {"fy9-a#n1", "fy9-a#n2"} & set(ids(r)), ids(r))
    expect("at most one task per cell and two per unit, three in all", len(r["recs"]) <= 3 and len({x["cell"] for x in r["recs"]}) == len(r["recs"]) and all(sum(x["task"]["unit"] == u for x in r["recs"]) <= 2 for u in ("fy9-a", "fy9-b", "fy9-c")), r["recs"])
    expect("with a weak cell the three include a task the page checks", any(x["task"]["check"] == "auto" for x in r["recs"]))

    # 6 a revisit that is due, and over the night
    log = [row("2026-11-10", "fy9-a#n1"), row("2026-11-11", "fy9-a#n2"), row("2026-11-12", "fy9-a#n3")]
    c1 = cells(D(log), "2026-11-13")["fy9-a|math"]
    expect("Vahva after three right numbers on three days (the revisit is 2 -> 5 -> 10 days: next 2026-11-22)", c1["state"] == "strong" and c1["next"] == "2026-11-22" and not c1["due"], c1)
    c2 = cells(D(log), "2026-11-22")["fy9-a|math"]
    expect("the day the revisit falls: Vahva, kertaa pian", c2["state"] == "strongdue" and c2["due"], c2)
    c3 = cells(D(log), "2026-11-21")["fy9-a|math"]
    expect("the day before: still Vahva (over the night the state changes)", c3["state"] == "strong", c3)
    r = recommend(D(log), "2026-11-22")
    first = next((x for x in r["recs"] if x["cell"] == "fy9-a|math"), None)
    expect("a due cell's task is recommended with 'Kertaus: edellisestä kerrasta N pv'", first and first["reason"]["key"] == "stale" and first["reason"]["days"] == 10, r["recs"])

    # 7 everything strong
    log = []
    for t in INDEX["tasks"]:
        if t["id"] == "fy9-a-s1": continue
        for k, day in enumerate(("2026-11-01", "2026-11-02", "2026-11-03")): log.append(row(day, t["id"], hour=f"1{k}:00"))
    r = recommend(D(log), "2026-11-05")
    expect("everything strong, nothing due, every task but one done this week: only the untouched task is offered", ids(r) == ["fy9-a-s1"], r["recs"])
    r = recommend(D(log), "2026-11-20")
    expect("a fortnight later (all strong, revisits due 2026-11-13): the due cells' tasks come back, three at most", 1 <= len(r["recs"]) <= 3 and any(x["reason"]["key"] == "stale" for x in r["recs"]), r["recs"])

    # 8 a tie goes by the course's order, then the page's
    r = recommend(D([row("2026-11-22", "fy9-c#c1")]), "2026-11-23")
    expect("equal scores: the earlier unit first, one task per cell, two per unit", ids(r) == ["fy9-a#c1", "fy9-a#n1", "fy9-b#n1"], ids(r))
    r1 = recommend(D([row("2026-11-20", "fy9-b#c1", result="no")]), "2026-11-23"); r2 = recommend(D([row("2026-11-20", "fy9-b#c1", result="no")]), "2026-11-23")
    expect("the recommendation is deterministic", r1 == r2)

    # 9 the minutes left
    r = recommend(D([row("2026-11-20", "fy9-b#c1", result="no")]), "2026-11-23", {"budget": 3})
    expect("with 3 minutes left only tasks of 3 minutes or less", r["recs"] and all(x["task"]["min"] <= 3 for x in r["recs"]), r["recs"])
    r = recommend(D([row("2026-11-20", "fy9-b#c1", result="no")]), "2026-11-23", {"budget": 0})
    expect("with no minutes left nothing is recommended", r["recs"] == [], r["recs"])

    # 10 no stuck topic: many tasks of one weak cell
    log = [row("2026-11-22", "fy9-a#n1", result="no")]
    r = recommend(D(log), "2026-11-23")
    expect("a weak topic does not fill the list: no two tasks of one cell", len({x["cell"] for x in r["recs"]}) == len(r["recs"]) and sum(x["cell"] == "fy9-a|math" for x in r["recs"]) <= 1, r["recs"])

    # 11 the student's own day (Pacific/Auckland is a day ahead of UTC at 23:30 UTC)
    ctx2 = b.new_context(timezone_id="Pacific/Auckland"); pg2 = ctx2.new_page(); pg2.goto(BASE + "FY9-valmentaja.html")
    day = pg2.evaluate("([i, d]) => window.flCoach.evidence(d.log, i).map((e) => e.day)", [INDEX, D([row("2026-11-20", "fy9-a#n1", hour="23:30")])])
    expect("a row at 23:30 UTC is the student's next day in New Zealand", day and day[0] == "2026-11-21", day)
    ctx2.close()

    # 12 old rows folded into the cells: the state is the same
    log = [row(f"2026-{m:02d}-{d:02d}", t) for m, d in ((9, 1), (9, 5), (9, 9)) for t in ("fy9-a#n1", "fy9-a#n2")]
    log += [row("2026-11-20", "fy9-a#n3"), row("2026-11-21", "fy9-b#c1")]
    before = cells(D(log), "2026-11-23")
    folded = pg.evaluate("""([i, d]) => { d.log = d.log.concat(Array.from({length: 2100}, (_, k) => ['2026-11-22T10:00Z', 'fy9-c#c1', 'a', 'ok', 0, 0, null, 'p'])); window.flCoach.compact(d, i); return d; }""", [INDEX, D(log)])
    expect("more than 2000 rows are folded: the log is cut to 1500 and the oldest evidence is kept in cells", len(folded["log"]) == 1500 and "fy9-a|math" in folded["cells"] and len(folded["cells"]["fy9-a|math"]["ev"]) <= 6, {k: (len(v) if hasattr(v, "__len__") else v) for k, v in folded.items()})
    after = cells(folded, "2026-11-23")
    expect("the state of a cell is the same after folding", after["fy9-a|math"]["state"] == before["fy9-a|math"]["state"] and abs(after["fy9-a|math"]["M"] - before["fy9-a|math"]["M"]) < 1e-9, (before["fy9-a|math"], after["fy9-a|math"]))

    # a task whose rows show no result: a written solution marked done carries none
    c = cells(D([row("2026-11-20", "fy9-a-s1", "s", None)]), "2026-11-23")["fy9-a|math"]
    expect("a written solution marked done (no result) is no evidence", c["state"] == "none", c)
    ctx.close()

    # ---- the pages ----
    for lang in ("fi", "en", "fi-easy"):
        base = BASE + ("" if lang == "fi" else lang + "/")
        if not (SITE / ("" if lang == "fi" else lang) / "FY9-valmentaja.html").is_file(): expect(f"{lang}: the coach page is built", False); continue
        for w, h in ((360, 800), (1280, 900)):
            c = b.new_context(viewport={"width": w, "height": h}, timezone_id="Europe/Helsinki"); p = c.new_page()
            reqs = []
            p.on("request", lambda r: reqs.append(r.url))
            p.goto(base + "FY9-valmentaja.html")
            T = p.evaluate("() => JSON.parse(document.getElementById('fy9-coach').dataset.t)")
            idx = p.evaluate("() => JSON.parse(document.getElementById('fy9-index').textContent)")
            if w == 360:
                expect(f"{lang}: no data: the diagnostic is offered, no recommendation, no competency list, no Tyhjennä",
                       p.locator("#coach-recs a.coach-go").count() == 1 and p.locator("#coach-recs a").first.get_attribute("href") == "fy9-koe.html" and p.locator("li.coach-rec").count() == 0
                       and not p.locator("#coach-areas").is_visible() and p.locator(".coach-clear").count() == 0)
                expect(f"{lang}: free practice is always linked", p.locator('a[href="yo-sekoitin.html"]').count() >= 1 and p.locator(f'a[href="FY9.html"]').count() >= 1)
                expect(f"{lang}: the page makes no request but to itself and its own files", all(u.startswith(BASE) for u in reqs), [u for u in reqs if not u.startswith(BASE)])
                q = b.new_context(java_script_enabled=False).new_page(); q.goto(base + "FY9-valmentaja.html")
                expect(f"{lang}: without a script the page says so and still links to the mixer and the course", "JavaScript" in q.locator("noscript").inner_text() and q.locator('a[href="yo-sekoitin.html"]').count() == 1, q.content()[:200])
                q.context.close()
            # a log of real tasks: three days, a mix of right and wrong
            auto = [t for t in idx["tasks"] if t["check"] == "auto"][:40]
            log = [row(f"2026-11-{10 + k % 6:02d}", t["id"], result=("ok", "no", "ok", "close")[k % 4], mistake=0 if k % 4 == 1 else None) for k, t in enumerate(auto)]
            p.evaluate("([k, d]) => localStorage.setItem(k, JSON.stringify(d))", [KEY, {"v": 1, "log": log}])
            p.reload()
            recs = p.locator("li.coach-rec")
            n = recs.count()
            expect(f"{lang} {w}px: with a log one to three recommendations, each with a task link, its chapter, minutes and one reason", 1 <= n <= 3 and all(
                recs.nth(i).locator("a.coach-task").get_attribute("href") and recs.nth(i).locator(".coach-where").inner_text() and "min" in recs.nth(i).locator(".coach-min").inner_text() and recs.nth(i).locator(".coach-why").inner_text()
                for i in range(n)), n)
            reasons = {T["why_wrong"], T["why_new"], T["why_more"]}
            expect(f"{lang} {w}px: every reason is one of the fixed texts", all(recs.nth(i).locator(".coach-why").inner_text() in reasons or re.fullmatch(T["why_stale"].replace("{n}", r"\d+"), recs.nth(i).locator(".coach-why").inner_text()) for i in range(n)), [recs.nth(i).locator(".coach-why").inner_text() for i in range(n)])
            hrefs = [recs.nth(i).locator("a.coach-task").get_attribute("href") for i in range(n)]
            expect(f"{lang} {w}px: every recommended task exists on its page", all(f'id="{h.split("#")[1]}"' in (SITE / ("" if lang == "fi" else lang) / h.split("#")[0]).read_text(errors="ignore") for h in hrefs), hrefs)
            p.locator("#coach-areas > summary").click()
            comps = p.locator("details.coach-comp")
            expect(f"{lang} {w}px: the competency list has the six areas, each opening to its units with a word and a mark", comps.count() == 6, comps.count())
            comps.first.locator("summary").click()
            body = p.locator("#coach-areas").inner_text()
            expect(f"{lang} {w}px: no percentage and no grade anywhere on the page", "%" not in p.locator("main").inner_text() and not re.search(r"\b\d+\s*/\s*\d+\b", p.locator(".coach-table").first.inner_text()), body[:200])
            expect(f"{lang} {w}px: the basis of a state says it is from this device", T["note"] in body)
            over = p.evaluate("() => document.scrollingElement.scrollWidth - document.scrollingElement.clientWidth")
            small = p.evaluate("() => [...document.querySelectorAll('main a, main button, main summary')].filter((e) => e.checkVisibility() && e.getBoundingClientRect().height < 40 && !e.closest('p') && !e.closest('td')).map((e) => e.textContent.trim().slice(0, 30))")
            expect(f"{lang} {w}px: no horizontal overflow and every control 40 px or more", over <= 1 and not small, (over, small))
            if lang == "fi" and w == 360: p.screenshot(path="/tmp/coach-360.png", full_page=True)
            if lang == "fi" and w == 1280: p.screenshot(path="/tmp/coach-1280.png", full_page=True)
            # the row on the course page
            p.goto(base + "FY9.html")
            row_el = p.locator("#fy9-coach-row")
            expect(f"{lang} {w}px: the course page shows the row with the number of tasks and minutes, and a button to the coach", row_el.is_visible() and re.search(r"\d", row_el.inner_text()) and row_el.locator("a").get_attribute("href") == "FY9-valmentaja.html", row_el.inner_text())
            tile = p.locator("#valmentaja-laatta a")
            expect(f"{lang} {w}px: the Valmentaja tile is on the course page", tile.count() == 1 and tile.get_attribute("href") == "FY9-valmentaja.html" and tile.inner_text().strip() == T["go"] or tile.inner_text().strip() == T["go"], tile.count())
            over = p.evaluate("() => document.scrollingElement.scrollWidth - document.scrollingElement.clientWidth")
            expect(f"{lang} {w}px: the course page does not overflow", over <= 1, over)
            if lang == "fi" and w == 360: p.screenshot(path="/tmp/fy9-360-after.png", full_page=False)
            if lang == "fi" and w == 1280: p.screenshot(path="/tmp/fy9-1280-after.png", full_page=False)
            # Tyhjennä
            if w == 360:
                p.goto(base + "FY9-valmentaja.html"); p.on("dialog", lambda dlg: dlg.dismiss())
                p.locator(".coach-clear").click()
                expect(f"{lang}: Tyhjennä asks first: cancelling keeps the data", p.evaluate("(k) => localStorage.getItem(k) !== null", KEY))
                p.remove_listener("dialog", p.listeners("dialog")[0]) if hasattr(p, "listeners") else None
                p2 = c.new_page(); p2.on("dialog", lambda dlg: dlg.accept()); p2.goto(base + "FY9-valmentaja.html")
                other = "ruukkilabra:vastaukset:fy9-voimat"
                p2.evaluate("(k) => localStorage.setItem(k, '{\"a\":1}')", other)
                with p2.expect_navigation(): p2.locator(".coach-clear").click()
                expect(f"{lang}: confirming removes the coach's key and nothing else; the diagnostic is offered again",
                       p2.evaluate("(k) => localStorage.getItem(k)", KEY) is None and p2.evaluate("(k) => localStorage.getItem(k)", other) is not None and p2.locator("#coach-recs a.coach-go").count() == 1)
                p2.close()
            c.close()
    # blocked storage
    c = b.new_context(); c.add_init_script("Object.defineProperty(window, 'localStorage', { get() { throw new Error('blocked'); } });")
    p = c.new_page(); errs = []; p.on("pageerror", lambda e: errs.append(str(e))); p.goto(BASE + "FY9-valmentaja.html")
    expect("blocked storage: the page works, says the data cannot be saved and offers the diagnostic", p.locator("#coach-data .notice").count() == 1 and p.locator("#coach-recs a.coach-go").count() == 1 and not errs, errs)
    p.goto(BASE + "FY9.html")
    expect("blocked storage: the course page has no row and no error", not p.locator("#fy9-coach-row").is_visible())
    c.close()
    # a damaged log: the page works and Tyhjennä repairs
    c = b.new_context(); p = c.new_page(); p.goto(BASE + "FY9-valmentaja.html")
    p.evaluate("(k) => localStorage.setItem(k, '{not json')", KEY); p.reload()
    expect("a damaged log: the diagnostic is offered and Tyhjennä is there to repair it", p.locator("#coach-recs a.coach-go").count() == 1 and p.locator(".coach-clear").count() == 1)
    expect("a damaged log is never rewritten by the page", p.evaluate("(k) => localStorage.getItem(k)", KEY) == "{not json")
    c.close()
    b.close()
print("FAILED" if fails else "all ok")
sys.exit(1 if fails else 0)
