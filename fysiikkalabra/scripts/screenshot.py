"""Readable screenshots of a built lesson page for the reviewers. Usage: python scripts/screenshot.py <id>

A full page is 15 000–20 000 px tall; scaled to what a model can read it is a 30 px wide strip. So the page is
captured in parts, each at most TILE px tall, into review/shots/ (git-ignored), and review/shots.md lists them
with what each shows, its size and its approximate image cost (w·h/750 tokens), so a reviewer opens only the
captures its questions need:

  top-390, top-1280           the first screen on a phone and a laptop (overview)
  fig-N-390                   every figure of the text (inline SVG), with its section and aria-label
  example-390[-k]             the worked example with every stage revealed
  sim-390, sim-1280           the simulation with its controls and readout
  stage-<id>-390[-k]          every inquiry stage, in tiles
  exp-<id>-390                every experiment after "Aseta alkutila": the sim beside its buttons and table

What a static picture cannot show (does the sim make sense when you move it, does a sequence teach) still needs
the browser; scripts/test_inquiry.py and scripts/test_sims.py already prove the routine mechanics."""
import pathlib, shutil, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
import courses
TILE = 1400

if len(sys.argv) != 2: sys.exit(__doc__)
lid = sys.argv[1]
page_file = courses.ROOT / "preview" / f"{lid}.html"
if not page_file.exists(): page_file = courses.ROOT / "site" / f"{lid}.html"
if not page_file.exists(): sys.exit(f"no built page for {lid}: run python scripts/build.py {lid}")
review = courses.find_lesson(lid) / "review"
OUT = review / "shots"
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
for old in review.glob(f"{lid}-*.png"): old.unlink()          # the full-page captures of the earlier script
rows = []


def save(pg, name, what, box=None, locator=None):
    """One capture (a locator, or a clip box in page coordinates), split into tiles when it is taller than TILE."""
    if locator is not None:
        locator.scroll_into_view_if_needed(); pg.wait_for_timeout(150)
        b = locator.bounding_box()
        if not b or b["width"] < 2 or b["height"] < 2: return
        sy = pg.evaluate("window.scrollY"); box = {"x": b["x"], "y": b["y"] + sy, "width": b["width"], "height": b["height"]}
    parts = max(1, -(-int(box["height"]) // TILE))
    for k in range(parts):
        h = min(TILE, box["height"] - k * TILE)
        clip = {"x": max(0, box["x"] - 4), "y": max(0, box["y"] + k * TILE - 4), "width": box["width"] + 8, "height": h + 8}
        fname = f"{lid}-{name}" + (f"-{k + 1}" if parts > 1 else "") + ".png"
        pg.screenshot(path=str(OUT / fname), clip=clip, full_page=True)
        w, hh = int(clip["width"]), int(clip["height"])
        rows.append((fname, what + (f" (part {k + 1}/{parts})" if parts > 1 else ""), w, hh))


with sync_playwright() as pw:
    b = launch(pw)
    for w, hgt in ((390, 844), (1280, 900)):
        pg = b.new_page(viewport={"width": w, "height": hgt}); pg.goto(page_file.resolve().as_uri())
        pg.evaluate("try { localStorage.clear() } catch (e) {}"); pg.reload(); pg.wait_for_timeout(700)
        pg.evaluate("window.scrollTo(0, 0)"); pg.wait_for_timeout(200)
        pg.screenshot(path=str(OUT / f"{lid}-top-{w}.png")); rows.append((f"{lid}-top-{w}.png", f"first screen at {w} px", w, hgt))
        pg.add_style_tag(content="header.top, nav.toc, nav.crumbs { position: static !important; }")   # sticky bars would be drawn into part captures
        if pg.locator("#sim").count(): save(pg, f"sim-{w}", f"simulation with controls and readout at {w} px", locator=pg.locator("#sim"))
        if w != 390: pg.close(); continue
        figs = pg.locator("main svg:not(#sim-root svg)")
        for i in range(figs.count()):
            f = figs.nth(i)
            label = f.get_attribute("aria-label") or ""
            section = f.evaluate("(e) => { const h = document.evaluate('preceding::*[self::h2 or self::h3][1]', e, null, 9, null).singleNodeValue; "
                                 "return h ? h.textContent.trim() : ''; }")
            save(pg, f"fig-{i + 1}-390", f"figure {i + 1} in “{section}”: {label[:90]}", locator=f)
        if pg.locator(".worked").count():
            all_btn = pg.locator(".worked .all-steps")
            if all_btn.count(): all_btn.first.click(); pg.wait_for_timeout(200)
            save(pg, "example-390", "worked example, every stage revealed", locator=pg.locator(".worked").first.locator("xpath=.."))
        for s in pg.locator("section.stage").all():
            sid = s.get_attribute("id"); title = " ".join(s.locator("h2").inner_text().split()[1:])   # without the stage number
            save(pg, f"stage-{sid}-390", f"inquiry stage {title}", locator=s)
        for ex in pg.locator(".experiment").all():
            aid = ex.evaluate("(e) => e.closest('.activity').id")
            start = ex.locator(".exp-start")
            if start.count() and start.is_visible(): start.click(); pg.wait_for_timeout(500)
            save(pg, f"exp-{aid}-390", f"experiment {aid} after Aseta alkutila: the sim next to its buttons and table", locator=ex.locator("xpath=ancestor::div[contains(@class,'activity')][1]"))
        pg.close()
    b.close()

lines = [f"# Screenshots of {lid} ({page_file.parent.name}/{page_file.name})", "",
         "Open only the captures your questions need (Read tool). Cost ≈ width·height/750 tokens each.", "",
         "| file | shows | px | ≈ tokens |", "|---|---|---|---|"]
lines += [f"| review/shots/{f} | {what} | {w}×{h} | {w * h // 750} |" for f, what, w, h in rows]
(review / "shots.md").write_text("\n".join(lines) + "\n")
print(f"wrote {len(rows)} captures to {OUT.relative_to(courses.ROOT)}/ and the list to {(review / 'shots.md').relative_to(courses.ROOT)}")
