"""General common-mistake recognition (work queue 17c PR 1, K5; templates/virhe.js, used by templates/lesson.js part 1).
Usage: python scripts/test_virhe.py

In a browser, on a small page that loads the two scripts as they are:
  - window.flMistake(value, answer, tol, unit, step) names the sign, the order of magnitude (10^±1…±9), time and speed
    (3,6, 60, 3600 and the inverses) and kelvin/celsius (273,15, only for the unit K or °C) with the check's own tolerance,
    and never when the answer or the value is 0
  - over every published numeric task (exercises.json and inquiry.json of every lesson): the model answer itself never
    names a mistake, and the answer × 1000 names the order of magnitude
  - the page: a wrong number names what to check (the four texts of lang js check_mistake_*), event fl:attempt carries the
    string in detail.mistake, a correct or "Lähellä" number names nothing; a task's own `mistakes` wins (test_inquiry.py)
Exit status 1 on any failure."""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


# (value, answer, tol, unit, step, expected)
RULES = [(-12.0, 12.0, 0.02, "N", 0, "sign"), (12.0, -12.0, 0.02, "N", 0, "sign"), (-11.9, 12.0, 0.02, "N", 0, "sign"), (-10, 12.0, 0.02, "N", 0, None),
         (120, 12.0, 0.02, "N", 0, "magnitude"), (1.2, 12.0, 0.02, "N", 0, "magnitude"), (12000, 12.0, 0.02, "N", 0, "magnitude"), (0.012, 12.0, 0.02, "N", 0, "magnitude"),
         (1.2e9, 12.0, 0.02, "N", 0, "magnitude"), (-120, 12.0, 0.02, "N", 0, None), (130, 12.0, 0.02, "N", 0, None),
         (43.2, 12.0, 0.02, "m/s", 0, "time"), (3.333, 12.0, 0.02, "m/s", 0, "time"), (720, 12.0, 0.02, "s", 0, "time"), (0.2, 12.0, 0.02, "h", 0, "time"), (43200, 12.0, 0.02, "s", 0, "time"),
         (285.15, 12.0, 0.02, "K", 0, "kelvin"), (-261.15, 12.0, 0.02, "°C", 0, "kelvin"), (285.15, 12.0, 0.02, "m", 0, None), (300, 12.0, 0.02, "K", 0, None),
         (5, 0, 0.02, "N", 0, None), (0, 5, 0.02, "N", 0, None), (-5, 5, 0.02, "N", 0, "sign"), (float("nan"), 5, 0.02, "N", 0, None),
         (60.2, 1.0, 0.02, "", 0.1, "time"), (7.0, 1.0, 0.02, "", 0, None), (-1.05, 1.0, 0.02, "", 0.1, "sign")]


def main():
    page = ('<!doctype html><html lang="fi"><head><meta charset="utf-8"></head><body><main>'
            '<script type="application/json" id="fl-strings">' + json.dumps({"js": {k: k for k in ("correct", "check_near", "check_number", "check_retry", "check_give_up", "check_magnitude", "check_mistake_sign", "check_mistake_magnitude", "check_mistake_time", "check_mistake_kelvin")}}) + '</script>'
            '<form class="check" id="f" data-answer="12" data-tol="0.02" data-unit="N" novalidate><input type="text"><button>Tarkista</button><output></output></form>'
            '<form class="check" id="g" data-answer="300" data-tol="0.02" data-unit="K" novalidate><input type="text"><button>Tarkista</button><output></output></form>'
            "</main></body></html>")
    virhe = (ROOT / "templates" / "virhe.js").read_text(encoding="utf-8")
    lesson = (ROOT / "templates" / "lesson.js").read_text(encoding="utf-8")
    tasks = []
    for p in sorted((ROOT / "content" / "fi").glob("*/*/exercises/exercises.json")):
        for lvl in json.loads(p.read_text(encoding="utf-8")).values():
            tasks += [(t["answer"], t.get("tolerance", 0.02), t.get("unit", ""), t["id"]) for t in lvl if isinstance(t.get("answer"), (int, float)) and not isinstance(t.get("answer"), bool)]
    for p in sorted((ROOT / "content" / "fi").glob("*/*/inquiry.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        tasks += [(a["answer"], a.get("tolerance", 0.02), a.get("unit", ""), f"{p.parent.name}/{a.get('id')}") for a in d.get("activities", []) if a.get("type") == "numeric" and isinstance(a.get("answer"), (int, float))]
    with sync_playwright() as pw:
        b = launch(pw); pg = b.new_page(); errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.route("https://test.invalid/p.html", lambda r: r.fulfill(status=200, content_type="text/html", body=page))
        pg.route("https://test.invalid/virhe.js", lambda r: r.fulfill(status=200, content_type="text/javascript", body=virhe))
        pg.route("https://test.invalid/lesson.js", lambda r: r.fulfill(status=200, content_type="text/javascript", body=lesson))
        pg.goto("https://test.invalid/p.html"); pg.add_script_tag(url="https://test.invalid/virhe.js"); pg.add_script_tag(url="https://test.invalid/lesson.js")
        expect("the scripts load without errors", not errors, "; ".join(errors))
        for v, a, t, u, s, want in RULES:
            got = pg.evaluate("([v, a, t, u, s]) => window.flMistake(v, a, t, u, s)", [v, a, t, u, s])
            expect(f"value {v} for answer {a} ({u or 'no unit'}): {want}", got == want, f"got {got}")
        bad = pg.evaluate("(ts) => ts.filter(([a, t, u]) => window.flMistake(a, a, t, u, 0) !== null).map((x) => x[3])", tasks)
        expect(f"the model answer of none of the {len(tasks)} numeric tasks names a mistake", not bad, str(bad[:5]))
        bad = pg.evaluate("(ts) => ts.filter(([a, t, u]) => a !== 0 && window.flMistake(a * 1000, a, t, u, 0) !== 'magnitude').map((x) => x[3])", tasks)
        expect("the answer × 1000 names the order of magnitude for every task", not bad, str(bad[:5]))
        def run(sel, typed):
            events = pg.evaluate("""([sel, typed]) => new Promise((res) => { const f = document.querySelector(sel); const seen = [];
                f.addEventListener('fl:attempt', (e) => seen.push(e.detail)); f.querySelector('input').value = typed; f.querySelector('button').click();
                setTimeout(() => res([f.querySelector('output').textContent, f.querySelector('output').dataset.state, seen[0] || null]), 20); })""", [sel, typed])
            return events
        for sel, typed, text, state, mist in [("#f", "-12", "check_mistake_sign", "no", "sign"), ("#f", "1200", "check_mistake_magnitude", "no", "magnitude"),
                                              ("#f", "43,2", "check_mistake_time", "no", "time"), ("#g", "573,15", "check_mistake_kelvin", "no", "kelvin"),
                                              ("#f", "12", "correct", "ok", None), ("#f", "12,5", "check_near", "close", None), ("#f", "5", "check_retry", "no", None)]:
            out, st, det = run(sel, typed)
            expect(f"page: {typed} in {sel} says {text}", out in (text, "check_give_up") if text == "check_retry" else out == text, out)
            expect(f"page: {typed} in {sel} is {state} and its attempt carries mistake {mist}", st == state and (det or {}).get("mistake") == mist, f"{st} {det}")
        b.close()
    print("ok" if not fails else f"{fails} failure(s)")
    sys.exit(1 if fails else 0)


main()
