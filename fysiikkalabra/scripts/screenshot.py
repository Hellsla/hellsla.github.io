"""Screenshot a built page at phone and laptop widths into the lesson's review/ folder (git-ignored). Usage: python scripts/screenshot.py <id>"""
import sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch; from reviews import find_lesson
ROOT = pathlib.Path(__file__).resolve().parents[1]
f = ROOT / "preview" / f"{sys.argv[1]}.html"
if not f.exists(): f = ROOT / "site" / f"{sys.argv[1]}.html"
OUT = find_lesson(sys.argv[1]) / "review"; OUT.mkdir(exist_ok=True)
with sync_playwright() as pw:
    b = launch(pw)
    for w in (390, 1280):
        p = b.new_page(viewport={"width": w, "height": 900}); p.goto(f.resolve().as_uri())
        p.evaluate("document.getElementById('sim') && document.getElementById('sim').scrollIntoView()"); p.wait_for_timeout(700)   # let the sim draw once
        p.evaluate("window.scrollTo(0, 0)"); p.wait_for_timeout(300)
        p.screenshot(path=str(OUT / f"{sys.argv[1]}-{w}.png"), full_page=True); print("wrote", (OUT / f"{sys.argv[1]}-{w}.png").relative_to(ROOT))
    b.close()
