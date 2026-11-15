"""PNG of a unit's recognition chart (data-fig="kartta") at 360 and 1280 px, from the built preview/ page.
Usage: python scripts/kartta_shot.py <unit> [fi|en|fi-easy ...]   (default: all three; run `build.py <unit>` first)
Writes docs/figures/fy9-tunnistus/<unit>-<lang>-<width>.png and prints the page's scrollWidth."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from playwright.sync_api import sync_playwright
from _browser import launch
unit = sys.argv[1]; langs = sys.argv[2:] or ["fi", "en", "fi-easy"]
out = pathlib.Path("docs/figures/fy9-tunnistus"); out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = launch(p)
    for lang in langs:
        path = pathlib.Path("preview") / ("" if lang == "fi" else lang) / f"{unit}.html"
        for w in (360, 1280):
            pg = b.new_page(viewport={"width": w, "height": 900}, device_scale_factor=2)
            pg.goto("file://" + str(path.resolve())); pg.wait_for_timeout(1200)
            el = pg.locator('svg[data-fig="kartta"]').first
            el.scroll_into_view_if_needed()
            print(unit, lang, w, "scrollWidth", pg.evaluate("document.documentElement.scrollWidth"))
            el.screenshot(path=str(out / f"{unit}-{lang}-{w}.png")); pg.close()
    b.close()
