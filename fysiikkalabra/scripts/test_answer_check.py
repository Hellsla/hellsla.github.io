"""The answer check of the lesson pages (templates/lesson.js part 1; teacher 2026-11-10, FY6 fixes 1-2).
Usage: python scripts/test_answer_check.py

In a browser, on a small page that loads templates/lesson.js as it is:
  - reading a typed number: decimal comma and point, a power of ten in every usual form (9,99e17, 9,99 · 10^17,
    9,99×10^{17}, 9,99*10^17, 1,602 · 10^-19, 3,73 × 10⁻¹⁹), a unit after it; 2/3 and other non-numbers are never read as a number
  - accepting: within 2 % of the answer, the task's own tolerance (data-tol) or half a unit in the shown answer's last
    digit (data-step is one unit), whichever is largest; a correctly rounded answer is always accepted, the next
    rounded value is not; 2-5 % away is "Lähellä"; negative, zero, very small and very large answers
Exit status 1 on any failure."""
import json, math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


PARSE = [("9,99e17", 9.99e17), ("9.99e17", 9.99e17), ("9,99 · 10^17", 9.99e17), ("9,99×10^17", 9.99e17),
         ("9,99*10^17", 9.99e17), ("9,99×10^{17}", 9.99e17), ("9,99 \\cdot 10^{17}", 9.99e17), ("1,602 · 10^-19", 1.602e-19),
         ("1,602 · 10^−19", 1.602e-19), ("-1,2e-17", -1.2e-17), ("3,73e-19", 3.73e-19), ("3,73 · 10^-19", 3.73e-19), ("3,73 × 10⁻¹⁹", 3.73e-19), ("3,73·10⁻¹⁹ J", 3.73e-19), ("9,99 × 10¹⁷", 9.99e17), ("10⁻³", 1e-3), ("2⁵", None), ("−1,2E−17", -1.2e-17), ("10^-3", 1e-3),
         ("3", 3), ("2,5", 2.5), ("2.5", 2.5), ("−0,50", -0.5), ("+4", 4), (",5", 0.5), ("12,", 12), ("10 000", 10000),
         ("3 Ω", 3), ("2,5 m/s", 2.5), ("9,81 m/s^2", 9.81), ("30 %", 30), ("5 eV", 5), ("R = 2,9 Ω", 2.9),
         ("2/3", None), ("2 / 3", None), ("2,5,3", None), ("3^2", None), ("2-1", None), ("2:3", None), ("", None),
         ("abc", None), ("Ω", None), ("9,99 10^17", None)]
# (answer, data-tol, data-step, typed, expected state)
CHECK = [(2.8995, 0.03, 1, "3", "ok"), (2.8995, 0.03, 1, "2", "no"), (2.8995, 0.03, 1, "2,9", "ok"),
         (4, 0.02, 1, "4", "ok"), (4, 0.02, 1, "3", "no"), (4, 0.02, 1, "5", "no"),
         (1.68, 0.02, 0.1, "1,7", "ok"), (1.68, 0.02, 0.1, "1,68", "ok"), (1.68, 0.02, 0.1, "1,6", "close"), (1.68, 0.02, 0.1, "1,5", "no"),
         (-1.5, 0.02, 0.1, "-1,5", "ok"), (-1.5, 0.02, 0.1, "−1,5", "ok"), (-1.5, 0.02, 0.1, "1,5", "no"), (-1.5, 0.02, 0.1, "-1,7", "no"),
         (0, 0.02, 0.1, "0", "ok"), (0, 0.02, 0.1, "0,04", "ok"), (0, 0.02, 0.1, "0,2", "no"),
         (1.602e-19, 0.02, 1e-22, "1,602 · 10^-19", "ok"), (1.602e-19, 0.02, 1e-22, "1,7e-19", "no"),
         (9.99e17, 0.02, 1e15, "9,99e17", "ok"), (9.99e17, 0.02, 1e15, "9,99 · 10^17", "ok"), (9.99e17, 0.02, 1e15, "9,0e17", "no"), (3.73e-19, 0.02, 1e-21, "3,73 × 10⁻¹⁹", "ok"),
         (100, 0.02, 1, "100", "ok"), (100, 0.02, 1, "102", "ok"), (100, 0.02, 1, "104", "close"), (100, 0.02, 1, "110", "no"),
         (2.8995, 0.03, 1, "2/3", "hint")]


def main():
    js = (ROOT / "templates" / "lesson.js").read_text(encoding="utf-8")
    forms = "".join(f'<form class="check" id="f{i}" data-answer="{a}" data-tol="{t}" data-step="{s:g}" novalidate><input type="text">'
                    f'<button>Tarkista</button><output></output></form>' for i, (a, t, s, _, _) in enumerate(CHECK))
    page = ('<!doctype html><html lang="fi"><head><meta charset="utf-8"></head><body><main>'
            '<script type="application/json" id="fl-strings">' + json.dumps({"js": {k: k for k in ("correct", "check_near", "check_number", "check_retry", "check_give_up", "check_magnitude")}}) + '</script>'
            + forms + "</main></body></html>")
    with sync_playwright() as pw:
        b = launch(pw); pg = b.new_page(); errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.route("https://test.invalid/fy0-0.html", lambda r: r.fulfill(status=200, content_type="text/html", body=page))
        pg.route("https://test.invalid/lesson.js", lambda r: r.fulfill(status=200, content_type="text/javascript", body=js))
        pg.goto("https://test.invalid/fy0-0.html"); pg.add_script_tag(url="https://test.invalid/lesson.js")
        expect("lesson.js loads without errors", not errors, "; ".join(errors))
        for s, want in PARSE:
            got = pg.evaluate("(s) => { const v = window.flParse(s); return Number.isFinite(v) ? v : null; }", s)
            ok = (got is None) if want is None else (got is not None and math.isclose(got, want, rel_tol=1e-12))
            expect(f"reads {s!r} as {want}", ok, f"got {got}")
        for i, (a, t, s, typed, want) in enumerate(CHECK):
            pg.fill(f"#f{i} input", typed); pg.click(f"#f{i} button")
            got = pg.eval_on_selector(f"#f{i} output", "(o) => o.dataset.state")
            expect(f"answer {a:g} (tol {t:g}, step {s:g}): {typed!r} is {want}", got == want, f"got {got}")
        b.close()
    print("ok" if not fails else f"{fails} failure(s)")
    sys.exit(1 if fails else 0)


main()
