"""FY9-valmentaja, the revision path (work queue 11b PR 7; templates/valmentaja.js (f), docs/FY9_ADAPTIVE_PLAN.md 5.5, 6.2.4).
Usage: python scripts/test_valmentaja_polku.py [site|preview]   (default: site, else preview)

Golden cases (window.flCoach.path and trainDays, pure, on a small fixed index; a change of a rule shows as a change here):
  the dates: 14 and 28 days, 3 to 7 days a week, a leap day, the change of the clock to summer and to winter time, an exam day
  the minutes: no day over 20, 40 or 60 minutes, in every combination; no task twice; nothing a day cannot hold
  the order: the diagnostic first (up to 30 minutes), then the weakest chapters, then the rest in the order of the course, the last week
  only revisions and minikokeet; the same with a goal and with courses ticked
  a missed day piles nothing up: the path moves; a revisit that is due goes first; the end of the path
  the key: written, read, changed, removed; a damaged or a foreign one is ignored
The page (fi, en, fi-easy): the box, the three choices, the days of the week as a list, change and delete, Tyhjennä, the row on the course
  page, no request, no overflow and every control 40 px or more at 360 and 1280 px, blocked storage
Exit status 1 on any failure."""
import functools, http.server, json, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

args = sys.argv[1:]
SITE = ROOT / (args[0] if args and (ROOT / args[0]).is_dir() else ("site" if (ROOT / "site" / "FY9-valmentaja.html").is_file() else "preview"))
KEY, PKEY, SKEY = "ruukkilabra:fy9-valmentaja", "ruukkilabra:fy9-polku", "ruukkilabra:fy9-tavoite"
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


U = [f"fy9-u{k}" for k in range(1, 7)]
units = [{"id": "fy9-koe", "chapter": 1, "title": "koe", "n": "1.1"}] + [{"id": u, "chapter": 2, "title": u, "n": f"2.{k}", **({"course": 1 if k <= 3 else 2})} for k, u in enumerate(U, 1)] + [{"id": "fy9-harjoituskoe", "chapter": 7, "title": "koe", "n": "7.1"}]
tasks = []
for k, u in enumerate(U, 1):
    tasks += [task(f"{u}#c1", u, "choice", ["concept"], 2), task(f"{u}#c2", u, "choice", ["graph"], 2), task(f"{u}#n1", u, "numeric", ["math"], 4), task(f"{u}#n2", u, "numeric", ["math"], 4),
              task(f"{u}#e1", u, "explain", ["communication"], 5), task(f"{u}-s1", u, "long", {"math": 6, "concept": 4}, 30)]
    tasks += [task(f"fy9-koe#testi-{2 * k - 1}", u, "choice", ["concept"], 2), task(f"fy9-koe#testi-{2 * k}", u, "choice", ["math"], 2)]   # the diagnostic: two tasks of each chapter
INDEX = {"units": units, "tasks": tasks, "plans": {"2": {"days": 14}, "4": {"days": 28}}, "koetila": {"fy9-harjoituskoe": {"minutes": 360, "points": 120}},
         "minikokeet": [{"id": "m30-osa1", "kind": "osa1", "minutes": 30, "points": 10, "short": [f"{u}#c1" for u in U[:3]]}, {"id": "m30-aihe-1", "kind": "aihe", "minutes": 30, "points": 10, "short": [f"{u}#c2" for u in U[:3]]},
                        {"id": "m30-aihe-2", "kind": "aihe", "minutes": 30, "points": 10, "short": [f"{u}#c2" for u in U[3:]]}, {"id": "m60-osa2", "kind": "osa2", "minutes": 60, "points": 21, "short": [f"{u}#n1" for u in U[:4]]}]}


def row(day, tid, result="ok", first=1, hour="10:00"):
    return [f"{day}T{hour}Z", tid, "a", result, first, 0, None, "p"]


def P(start="2026-11-24", days=14, per=5, mins=40, exam=None):
    return {"v": 1, "start": start, "days": None if exam else days, "exam": exam, "per": per, "min": mins}


with sync_playwright() as pw:
    b = launch(pw)
    ctx = b.new_context(timezone_id="Europe/Helsinki")
    pg = ctx.new_page()
    pg.goto(BASE + "FY9-valmentaja.html")
    plan = lambda p, today, log=None, o=None: pg.evaluate("([i, p, t, l, o]) => window.flCoach.path(i, { v: 1, log: l, cells: {} }, p, t, o)", [INDEX, p, today, log or [], o or {}])
    days_of = lambda p: pg.evaluate("(p) => window.flCoach.trainDays(p).map((n) => new Date(n * 86400000).toISOString().slice(0, 10))", p)
    ids = lambda r: [it["task"]["id"] for d in r["days"] for it in d["items"] if "task" in it]
    units_in_order = lambda r: [u for u in dict.fromkeys(next(t["unit"] for t in tasks if t["id"] == i) for d in r["days"] for it in d["items"] if "task" in it and not d["last"] for i in [it["task"]["id"]] if not i.startswith("fy9-koe#"))]

    # 1 the dates
    for days in (14, 28):
        for per in (3, 4, 5, 6, 7):
            ds = days_of(P(days=days, per=per))
            weeks = [sum(1 for k, d in enumerate(ds) if 0 <= (pg.evaluate("([a, b]) => Math.round((Date.parse(b) - Date.parse(a)) / 86400000)", ["2026-11-24", d])) // 7 == w) for w in range(days // 7)]
            expect(f"{days} days, {per} a week: every week of seven days holds exactly {per} practice days, the first day is the start", all(x == per for x in weeks) and ds[0] == "2026-11-24" and len(set(ds)) == len(ds), weeks)
    expect("3 days a week are spread (day 1, 3, 5 of each week), 5 days a week (1, 2, 3, 5, 6)", days_of(P(per=3))[:3] == ["2026-11-24", "2026-11-26", "2026-11-28"] and days_of(P(per=5))[:5] == ["2026-11-24", "2026-11-25", "2026-11-26", "2026-11-28", "2026-11-29"], days_of(P(per=3))[:3])
    expect("the path of 14 days ends on the 14th day, of 28 days on the 28th", pg.evaluate("() => [window.flCoach.pathEnd({ start: '2026-11-24', days: 14 }) - window.flCoach.pathEnd({ start: '2026-11-24', days: 14 }) + 13, 0].join()") == "13,0" and
           pg.evaluate("(p) => new Date(window.flCoach.pathEnd(p) * 86400000).toISOString().slice(0, 10)", {"start": "2026-11-24", "days": 14}) == "2026-12-07" and pg.evaluate("(p) => new Date(window.flCoach.pathEnd(p) * 86400000).toISOString().slice(0, 10)", {"start": "2026-11-24", "days": 28}) == "2026-12-21")
    leap = days_of(P(start="2028-02-27", per=7)); common = days_of(P(start="2027-02-27", per=7))
    expect("a leap year has its 29 February, a common year goes from 28 February to 1 March, the path ends on the right day", "2028-02-29" in leap and leap[-1] == "2028-03-11" and "2027-02-29" not in common and common[2] == "2027-03-01" and common[-1] == "2027-03-12", (leap, common))
    for start, clock in (("2027-03-27", "summer time starts 2027-03-28"), ("2026-10-24", "winter time starts 2026-10-25"), ("2028-03-25", "summer time 2028-03-26")):
        ds = days_of(P(start=start, per=7))
        d2 = pg.evaluate("(a) => a.map((s, i) => i && Math.round((Date.parse(s) - Date.parse(a[i - 1])) / 86400000))", ds)
        expect(f"{clock}: 14 consecutive days, none twice and none lost", len(ds) == 14 and all(x == 1 for x in d2[1:]), ds)
    # the same in the student's own clock: the browser runs in Europe/Helsinki, a path plan on the day the clock changes is the same day
    r = plan(P(start="2027-03-27", per=7, mins=20), "2027-03-28")
    expect("on the day the clock changes the plan starts that very day and holds the rest of the days", r["days"][0]["date"] == "2027-03-28" and len(r["days"]) == 13, [d["date"] for d in r["days"]][:3])
    r = plan(P(start="2026-10-24", per=7, mins=20), "2026-10-25")
    expect("on the day the clock goes back the plan starts that very day (25 hours do not make two days)", r["days"][0]["date"] == "2026-10-25" and len(r["days"]) == 13)
    ex = days_of(P(start="2026-11-24", exam="2026-12-04", per=7))
    expect("an exam day: the path ends the day before it", ex[-1] == "2026-12-03" and len(ex) == 10, ex)
    expect("a path longer than an exam allows or too short is not valid", pg.evaluate("([a, b, c, d]) => [window.flCoach.validPath(a), window.flCoach.validPath(b), window.flCoach.validPath(c), window.flCoach.validPath(d)].join()", [P(exam="2026-11-30"), P(exam="2026-12-01"), P(exam="2027-03-24"), P(exam="2027-03-25")]) == "false,true,true,false")

    # 2 the minutes: in every combination
    bad, dup, empty = [], [], []
    for days in (14, 28):
        for per in (3, 4, 5, 6, 7):
            for mins in (20, 40, 60):
                r = plan(P(days=days, per=per, mins=mins), "2026-11-24")
                for d in r["days"]:
                    over = sum(it["mini"]["minutes"] if "mini" in it else it["task"]["min"] for it in d["items"])
                    if over > mins or over != d["minutes"]: bad.append((days, per, mins, d["date"], over))
                    if not d["items"]: empty.append((days, per, mins, d["date"]))
                if len(ids(r)) != len(set(ids(r))): dup.append((days, per, mins))
    expect("every combination (2 lengths x 5 days a week x 3 minute choices): no day over its minutes, and the minutes told are the sum", not bad, bad[:3])
    expect("no task twice in a path, and no day without anything to do", not dup and not empty, (dup[:3], empty[:3]))
    r = plan(P(mins=20, per=7, days=28), "2026-11-24")
    expect("20 minutes a day: no task of more than 20 minutes and no minikoe (they last 30 and 60)", all(it["task"]["min"] <= 20 for d in r["days"] for it in d["items"] if "task" in it) and not any("mini" in it for d in r["days"] for it in d["items"]))
    r = plan(P(mins=60, per=5, days=28), "2026-11-24")
    expect("60 minutes: minikokeet appear, only in the last week, never one that is longer than the day", any("mini" in it for d in r["days"] for it in d["items"]) and all(d["last"] for d in r["days"] if any("mini" in it for it in d["items"])) and all(it["mini"]["minutes"] <= 60 for d in r["days"] for it in d["items"] if "mini" in it))
    r = plan(P(mins=40, per=5, days=28), "2026-11-24")
    expect("40 minutes: the 30 minute sets only", all(it["mini"]["minutes"] == 30 for d in r["days"] for it in d["items"] if "mini" in it) and any("mini" in it for d in r["days"] for it in d["items"]))

    # 3 the order
    r = plan(P(mins=40, per=7, days=28), "2026-11-24")
    first = [it["task"]["id"] for it in r["days"][0]["items"]]
    expect("with nothing done the first day is the diagnostic, only its short tasks, and the diagnostic is at most 30 minutes in all", first and all(i.startswith("fy9-koe#") for i in first) and sum(it["task"]["min"] for d in r["days"] for it in d["items"] if it["task"]["id"].startswith("fy9-koe#")) <= 30, first)
    expect("with nothing done the chapters follow the order of the course", units_in_order(r) == U, units_in_order(r))
    expect("the last week holds revisions and minikokeet only, and that is the last seven days of the path", [d["date"] for d in r["days"] if d["last"]][0] >= "2026-12-15" and all(d["last"] == (d["date"] >= "2026-12-15") for d in r["days"]))
    # the diagnostic with different results (done the day before)
    diag = lambda res: [row("2026-11-24", f"fy9-koe#testi-{i}", result=res.get((i + 1) // 2, "ok"), hour=f"1{i % 10}:00") for i in range(1, 13)]
    cases = {"u3 and u5 weak (u3 worse)": ({3: "no", 5: "no"}, ["fy9-u3", "fy9-u5", "fy9-u1", "fy9-u2", "fy9-u4", "fy9-u6"]), "only u6 weak": ({6: "no"}, ["fy9-u6", "fy9-u1", "fy9-u2", "fy9-u3", "fy9-u4", "fy9-u5"]), "all right": ({}, U)}
    for name, (res, want) in cases.items():
        log = diag(res)
        if name.startswith("u3"):
            log = [x for x in log if x[1] != "fy9-koe#testi-10"] + [row("2026-11-24", "fy9-koe#testi-10", "ok", hour="19:00")]   # u5: one wrong, one right: less weak than u3
        r = plan(P(mins=40, per=7, days=28), "2026-11-25", log)
        expect(f"diagnostic result: {name}: the chapters come weakest first, then the rest in the order of the course", units_in_order(r) == want, units_in_order(r))
    expect("a diagnostic done: no diagnostic task is in the plan again", not any(i.startswith("fy9-koe#") for i in ids(plan(P(mins=40, per=7, days=28), "2026-11-25", diag({3: "no"})))))
    r = plan(P(mins=40, per=7, days=28), "2026-11-25", diag({}))
    expect("a chapter that is Vahva is not left out of the path, it follows the others", set(units_in_order(r)) == set(U))
    # a goal
    base = plan(P(mins=60, per=5, days=28), "2026-11-24"); ba = plan(P(mins=60, per=5, days=28), "2026-11-24", None, {"goal": "BA"}); le = plan(P(mins=60, per=5, days=28), "2026-11-24", None, {"goal": "LE"})
    longs = lambda r: sum(1 for d in r["days"] if not d["last"] for it in d["items"] if "task" in it and it["task"]["kind"] == "long")
    expect("B-A: no long task while short ones are left; L-E: long and explaining tasks in; a different path for each goal", longs(ba) == 0 and longs(le) >= 1 and ids(ba) != ids(le), (longs(base), longs(ba), longs(le)))
    expect("a goal never takes a task or a day out for the minutes: still no day over", all(d["minutes"] <= 60 for r in (ba, le) for d in r["days"]))
    # the courses taken
    c1 = plan(P(mins=40, per=7, days=28), "2026-11-24", None, {"courses": [1]})
    expect("courses ticked: a chapter of a course not ticked is in no day, not even a minikoe of those chapters alone", set(units_in_order(c1)) == set(U[:3]) and not any(next(t["unit"] for t in tasks if t["id"] == i) in U[3:] for i in ids(c1)) and not any(it["mini"]["id"] == "m30-aihe-2" for d in c1["days"] for it in d["items"] if "mini" in it), units_in_order(c1))
    # the revision: only what has been done and is due
    done = [row("2026-11-10", "fy9-u1#n1"), row("2026-11-11", "fy9-u1#n2"), row("2026-11-12", "fy9-u1#c1"), row("2026-11-12", "fy9-u1#c2", hour="11:00")]
    r = plan(P(start="2026-11-13", mins=40, per=7, days=28), "2026-11-24", done)
    ff = [it for it in r["days"][0]["items"]]
    expect("a revisit that has come due goes first and says why", ff and ff[0].get("why") == "stale" and ff[0]["task"]["unit"] == "fy9-u1", ff[:2])

    # 4 a missed day piles nothing up
    p = P(start="2026-11-24", per=7, mins=20, days=28)
    a, c = plan(p, "2026-11-24"), plan(p, "2026-12-01")
    expect("seven days missed: the path moves, it does not pile up (no day holds more than its 20 minutes) and the first day after is what the first day was", all(d["minutes"] <= 20 for d in c["days"]) and [i["task"]["id"] for i in c["days"][0]["items"]] == [i["task"]["id"] for i in a["days"][0]["items"]], [d["minutes"] for d in c["days"]][:4])
    expect("the days that were missed are not in the plan, and the end of the path stays where it was", c["days"][0]["date"] == "2026-12-01" and c["end"] == a["end"], (c["days"][0]["date"], c["end"], a["end"]))
    expect("a plan keeps the same days whatever was done before today, and the log of today does not change today's list", plan(p, "2026-11-24", [row("2026-11-24", a["days"][0]["items"][0]["task"]["id"])])["days"][0]["items"] == a["days"][0]["items"])
    expect("after the end of the path there is nothing and it says it has ended", (lambda e: e["ended"] and e["days"] == [])(plan(p, "2026-12-22")) and not plan(p, "2026-12-21")["ended"])
    r = plan(P(start="2026-11-24", exam="2026-12-04", per=7, mins=40), "2026-11-24")
    expect("an exam path: the last seven days before the exam are the revision, nothing after the day before the exam", r["days"][-1]["date"] == "2026-12-03" and r["days"][-1]["last"] and all(d["date"] < "2026-12-04" for d in r["days"]))

    # 5 the key
    st = lambda f, *a: pg.evaluate(f, list(a))
    expect("the key: written, read back, changed and removed", st("""([p, q]) => { const f = window.flCoach; localStorage.removeItem(f.PATH_KEY); const a = f.writePath(p), r1 = JSON.stringify(f.readPath()), b = f.writePath(q), r2 = JSON.stringify(f.readPath()), c = f.writePath(null);
        return [f.PATH_KEY, a, r1 === JSON.stringify(p), b, r2 === JSON.stringify(q), c, f.readPath()].join('|'); }""", P(), P(per=3, mins=20, days=28)) == f"{PKEY}|true|true|true|true|true|")
    expect("a damaged or a foreign path is ignored, an invalid one is never written", st("""() => { const f = window.flCoach, out = [];
        for (const v of ['{no', '{"v":2,"start":"2026-11-24","days":14,"per":5,"min":40}', '{"v":1,"start":"2026-11-31","days":14,"per":5,"min":40}', '{"v":1,"start":"2026-11-24","days":15,"per":5,"min":40}', '{"v":1,"start":"2026-11-24","days":14,"per":8,"min":40}', '{"v":1,"start":"2026-11-24","days":14,"per":5,"min":30}']) { localStorage.setItem(f.PATH_KEY, v); out.push(String(f.readPath())); }
        localStorage.removeItem(f.PATH_KEY); out.push(String(f.writePath({ v: 1, start: '2026-11-24', days: 14, per: 9, min: 40 })), String(localStorage.getItem(f.PATH_KEY))); return out.join('|'); }""") == "null|null|null|null|null|null|false|null")
    ctx.close()

    # ---- the pages ----
    for lang in ("fi", "en", "fi-easy"):
        base = BASE + ("" if lang == "fi" else lang + "/")
        d = SITE / ("" if lang == "fi" else lang)
        if not (d / "FY9-valmentaja.html").is_file(): expect(f"{lang}: the coach page is built", False); continue
        for w, h in ((360, 800), (1280, 900)):
            c = b.new_context(viewport={"width": w, "height": h}, timezone_id="Europe/Helsinki"); p = c.new_page()
            reqs = []; p.on("request", lambda r: reqs.append(r.url))
            p.goto(base + "FY9-valmentaja.html")
            T = p.evaluate("() => JSON.parse(document.getElementById('fy9-coach').dataset.t)")
            idx = p.evaluate("() => JSON.parse(document.getElementById('fy9-index').textContent)")
            expect(f"{lang} {w}px: the revision path is there, closed, with the three choices and no path yet (nothing saved)", p.locator("#coach-path").is_visible() and not p.locator("#coach-path").evaluate("e => e.open") and p.locator("#coach-path > summary").inner_text() == T["path_h"] and p.evaluate("(k) => localStorage.getItem(k)", PKEY) is None)
            p.locator("#coach-path > summary").click()
            expect(f"{lang} {w}px: the choices: 14, 28 days or an exam day; 3 to 7 days a week; 20, 40 or 60 minutes; one save button, no delete button before a path", p.locator("#coach-path input[name=path-len]").count() == 3 and p.locator("#coach-path input[name=path-per]").count() == 5 and p.locator("#coach-path input[name=path-min]").count() == 3 and p.locator(".coach-save").count() == 1 and p.locator(".coach-pathdel").count() == 0 and p.locator(".coach-pathdays").count() == 0)
            small = p.evaluate("() => [...document.querySelectorAll('#coach-path label, #coach-path button, #coach-path input[type=date], #coach-path summary')].filter((e) => e.checkVisibility() && e.getBoundingClientRect().height < 40).length")
            expect(f"{lang} {w}px: every control of the path is 40 px or higher", small == 0, small)
            p.locator("#coach-path label", has_text=T["path_28"]).click(); p.locator("#coach-path label", has_text="4").first.click()
            p.locator("#coach-path input[name=path-per][value='4']").check(); p.locator("#coach-path input[name=path-min][value='40']").check()
            p.locator(".coach-save").click()
            saved = json.loads(p.evaluate("(k) => localStorage.getItem(k)", PKEY))
            expect(f"{lang} {w}px: saving writes the one key on this device (28 days, 4 a week, 40 minutes, from today) and nothing else is written", saved["days"] == 28 and saved["per"] == 4 and saved["min"] == 40 and saved["exam"] is None and re.fullmatch(r"\d{4}-\d\d-\d\d", saved["start"]) and p.evaluate("() => Object.keys(localStorage).filter((k) => k.startsWith('ruukkilabra:')).sort().join()") == PKEY, saved)
            lis = p.locator(".coach-pathday")
            n = lis.count()
            expect(f"{lang} {w}px: the days of this week are a list, with the date, the minutes, tasks with a link, the chapter and the minutes; today is marked", 1 <= n <= 4 and all(lis.nth(i).locator(".coach-pathitems a").count() >= 1 and lis.nth(i).locator(".coach-pathdate").inner_text() for i in range(n)) and p.locator(".coach-today").count() <= 1 and (p.locator(".coach-today").count() == 0 or p.locator(".coach-today").inner_text() == T["path_today"]), n)
            hrefs = [lis.nth(i).locator(".coach-pathitems a").nth(j).get_attribute("href") for i in range(n) for j in range(lis.nth(i).locator(".coach-pathitems a").count())]
            expect(f"{lang} {w}px: every task of the path exists on its page", all(f'id="{h.split("#")[1]}"' in (d / h.split("#")[0]).read_text(errors="ignore") for h in hrefs if "#" in h and "minikoe" not in h) and hrefs, hrefs[:4])
            mins = [int(re.search(r"\d+", lis.nth(i).locator(".coach-pathdate .coach-min").inner_text()).group()) for i in range(n)]
            expect(f"{lang} {w}px: no day is over the 40 minutes chosen", all(m <= 40 for m in mins), mins)
            expect(f"{lang} {w}px: the page says the path stays on this device and sends nothing", T["path_note"] in p.locator("#coach-path").inner_text() and "%" not in p.locator("#coach-path").inner_text())
            over = p.evaluate("() => document.scrollingElement.scrollWidth - document.scrollingElement.clientWidth")
            small = p.evaluate("() => [...document.querySelectorAll('main a, main button, main summary')].filter((e) => e.checkVisibility() && e.getBoundingClientRect().height < 40 && !e.closest('p') && !e.closest('td')).map((e) => e.textContent.trim().slice(0, 30))")
            expect(f"{lang} {w}px: no horizontal overflow and every control 40 px or more with a path on the page", over <= 1 and not small, (over, small))
            if lang == "fi": p.screenshot(path=f"/tmp/polku-{w}.png", full_page=True)
            p.reload(); p.locator("#coach-path > summary").click()
            expect(f"{lang} {w}px: the path comes back after a reload with its choices filled in, and the delete button is there", p.locator("#coach-path input[name=path-len]:checked").get_attribute("value") == "28" and p.locator("#coach-path input[name=path-per]:checked").get_attribute("value") == "4" and p.locator(".coach-pathdel").count() == 1)
            p.locator("#coach-path input[name=path-min][value='20']").check(); p.locator(".coach-save").click()
            s2 = json.loads(p.evaluate("(k) => localStorage.getItem(k)", PKEY))
            expect(f"{lang} {w}px: changing the minutes keeps the start; the path is changed, not made again", s2["min"] == 20 and s2["start"] == saved["start"] and s2["days"] == 28)
            p.locator("#coach-path input[name=path-len][value=exam]").check()
            p.locator(".coach-save").click()
            expect(f"{lang} {w}px: an exam day with no date is not saved", json.loads(p.evaluate("(k) => localStorage.getItem(k)", PKEY))["days"] == 28)
            p.locator("#coach-path input[type=date]").fill(p.evaluate("() => { const e = document.querySelector('#coach-path input[type=date]'); return e.min; }"))
            p.locator(".coach-save").click()
            s3 = json.loads(p.evaluate("(k) => localStorage.getItem(k)", PKEY))
            expect(f"{lang} {w}px: an exam day 7 days ahead is saved, and the path has no 14 or 28 any more", s3["exam"] and s3["days"] is None and s3["start"] != "")
            # the row on the course page uses the day of the path
            log = [row("2026-11-10", t["id"]) for t in idx["tasks"][:3]]
            p.evaluate("([k, d]) => localStorage.setItem(k, JSON.stringify(d))", [KEY, {"v": 1, "log": log}])
            p.goto(base + "FY9.html")
            expect(f"{lang} {w}px: the course page row follows the path's day (tasks and minutes) when today is a practice day", p.locator("#fy9-coach-row").is_visible() and re.search(r"\d", p.locator("#fy9-coach-row").inner_text()), p.locator("#fy9-coach-row").inner_text())
            p.goto(base + "FY9-valmentaja.html"); p.locator("#coach-path > summary").click()
            p.locator(".coach-pathdel").click()
            expect(f"{lang} {w}px: Poista polku removes the path at once and nothing else of the coach", p.evaluate("(k) => localStorage.getItem(k)", PKEY) is None and p.evaluate("(k) => localStorage.getItem(k) !== null", KEY) and p.locator(".coach-pathdays").count() == 0)
            expect(f"{lang} {w}px: the page makes no request but to itself", all(u.startswith(BASE) for u in reqs), [u for u in reqs if not u.startswith(BASE)])
            c.close()
        # Tyhjennä removes the path too
        c = b.new_context(timezone_id="Europe/Helsinki"); p = c.new_page(); p.on("dialog", lambda dlg: dlg.accept()); p.goto(base + "FY9-valmentaja.html")
        p.evaluate("([k, v]) => localStorage.setItem(k, v)", [PKEY, json.dumps(P())])
        p.reload()
        with p.expect_navigation(): p.locator(".coach-clear").click()
        expect(f"{lang}: Tyhjennä removes the path with the rest of the coach's data", p.evaluate("(k) => localStorage.getItem(k)", PKEY) is None)
        c.close()
    # blocked storage
    c = b.new_context(); c.add_init_script("Object.defineProperty(window, 'localStorage', { get() { throw new Error('blocked'); } });")
    p = c.new_page(); errs = []; p.on("pageerror", lambda e: errs.append(str(e))); p.goto(BASE + "FY9-valmentaja.html")
    p.locator("#coach-path > summary").click(); p.locator(".coach-save").click()
    expect("blocked storage: the path box works without an error, says it cannot save, and shows no path", not errs and p.locator("#coach-path .notice:visible").count() == 1 and p.locator(".coach-pathdays").count() == 0, errs)
    c.close()
    b.close()
print("FAILED" if fails else "all ok")
sys.exit(1 if fails else 0)
