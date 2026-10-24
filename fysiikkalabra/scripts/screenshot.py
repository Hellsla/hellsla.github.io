"""Screenshot a built page at phone and laptop widths for the web-designer agent."""
import sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
ROOT = pathlib.Path(__file__).resolve().parents[1]
f = ROOT / "preview" / f"{sys.argv[1]}.html"
if not f.exists(): f = ROOT / "site" / f"{sys.argv[1]}.html"
(ROOT / "review").mkdir(exist_ok=True)
with sync_playwright() as pw:
    b = launch(pw)
    for w in (390, 1280):
        p = b.new_page(viewport={"width": w, "height": 900}); p.goto(f.resolve().as_uri()); p.wait_for_timeout(1000)
        p.screenshot(path=str(ROOT / f"review/{sys.argv[1]}-{w}.png"), full_page=True); print("wrote", f"review/{sys.argv[1]}-{w}.png")
    b.close()
