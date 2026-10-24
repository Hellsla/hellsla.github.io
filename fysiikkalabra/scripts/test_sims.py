"""Headless check of every built simulation. Usage: python scripts/test_sims.py [lesson-id]

A sim passes when the page loads with no console errors, window.simState exists after 1.5 s,
and every assertion in tests/sims/<id>.json holds: |expr - expected| <= tol * max(1, |expected|).
An assertion may carry "setup": JS run before the expression (e.g. to set slider values)."""
import json, sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
ROOT = pathlib.Path(__file__).resolve().parents[1]
only = sys.argv[1] if len(sys.argv) > 1 else None
OUT = ROOT / "preview" if (ROOT / "preview" / "index.html").exists() else ROOT / "site"   # preview/ holds drafts + --all
fails = 0
with sync_playwright() as pw:
    b = launch(pw)
    for page_file in sorted(OUT.glob("*.html")):
        lid = page_file.stem
        if only and lid != only: continue
        if not (OUT / f"{lid}-sim.js").exists(): continue
        page = b.new_page(viewport={"width": 1280, "height": 900})   # fresh page: no leftover listeners
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(page_file.as_uri()); page.wait_for_timeout(1500)
        state = page.evaluate("window.simState")
        tests = ROOT / "tests/sims" / f"{lid}.json"
        checks = json.loads(tests.read_text()) if tests.exists() else []
        bad = []
        if state is not None:
            for c in checks:
                if c.get("setup"): page.evaluate(c["setup"]); page.wait_for_timeout(200)
                got = page.evaluate(c["expr"])
                if got is None or abs(got - c["expected"]) > c.get("tol", 0.01) * max(1, abs(c["expected"])):
                    bad.append(f"{c['expr']} = {got} (expected {c['expected']})")
        ok = not errors and state is not None and not bad
        fails += not ok
        print("PASS" if ok else "FAIL", f"{OUT.name}/{lid}", "no simState (p5 not loaded?)" if state is None else "", errors[:3], bad)
        page.close()
    b.close()
sys.exit(1 if fails else 0)
