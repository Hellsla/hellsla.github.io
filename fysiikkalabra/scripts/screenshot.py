"""Readable screenshots of a built page for the reviewers. Usage: python scripts/screenshot.py <id> [--if-stale] [--no-build]

<id> is a lesson, an investigation (fy10-jousivakio), a TVT guide (tvt-kuvaaja) or a Sovella set (FY3-sovella). The
page is built first (build.py <id>, into preview/) so the captures show the content as it is now. review/shots/
stamp.txt records what they show (the content hashes, the built page, the templates): with --if-stale an unchanged
page keeps its captures and nothing is taken again. contact-N.png sheets show every capture small and numbered, for
the visual reviewer's triage before it opens the ones it needs at full size.

A full page is 15 000–20 000 px tall; scaled to what a model can read it is a 30 px wide strip. So the page is
captured in parts, each at most TILE px tall, into review/shots/ (git-ignored), and review/shots.md lists them
with what each shows, its size and its approximate image cost (w·h/750 tokens), so a reviewer opens only the
captures its questions need:

  top-390, top-1280           the first screen on a phone and a laptop (overview)
  fig-N-390                   every figure of the text (inline SVG), with its section and aria-label
  example-390[-k]             the worked example with every stage revealed
  sim-390, sim-1280           the simulation with its controls and readout
  lab-1280, fig-row-1280      the wide layout: the sim beside the experiments, the first figure beside its paragraph
  intro-1280                  the opening: title, Miksi question, illustration beside the goals, Pohjatiedot
  theory-1280[-k]             Teoriatiivistelmä: long theory with its figures on one screen width
  open-ennusta-1280           the Ennusta box open, the predictions answered (feedback showing)
  open-tarkista-1280[-k]      Tarkista osaamisesi with every hint and solution open: does an opened card leave gaps?
  open-exit-1280              the exit ticket with its answers open
  open-exercises[-Ln]-1280[-k]  every exercise level with every solution open
(the open-* captures are what check_layout.py measures in its "open" state; look at them after a layout change)
  stage-<id>-390[-k]          every inquiry stage, in tiles
  exp-<id>-390                every experiment after "Aseta alkutila": the sim beside its buttons and table

What a static picture cannot show (does the sim make sense when you move it, does a sequence teach) still needs
the browser; scripts/test_inquiry.py and scripts/test_sims.py already prove the routine mechanics."""
import hashlib, pathlib, shutil, subprocess, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from _browser import launch
import courses
TILE = 1400

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if len(args) != 1: sys.exit(__doc__)
lid = args[0]


def target(pid):
    """(kind, review folder, content hashes) of a page id: a lesson, an investigation, a TVT guide or <COURSE>-sovella."""
    import guides, investigations, practice, reviews
    if pid.endswith("-sovella"):
        code = pid[:-len("-sovella")]; return "sovella", practice.folder(code) / "review", practice.content_hash(code)
    if pid in investigations.ids(): return "investigation", investigations.folder(pid) / "review", investigations.content_hash(pid)
    if pid in guides.ids(): return "guide", guides.folder(pid) / "review", guides.content_hash(pid)
    f = courses.find_lesson(pid)
    return "lesson", f / "review", f"{reviews.content_hash(f)} exercises {reviews.content_hash(f, 'exercises')}"


kind, review, hashes = target(lid)
if "--no-build" not in sys.argv:                       # the captures show the content as it is now, never an older preview
    r = subprocess.run([sys.executable, str(courses.ROOT / "scripts/build.py"), lid], cwd=courses.ROOT, capture_output=True, text=True)
    if r.returncode: sys.exit(f"build.py {lid} failed:\n{r.stdout[-800:]}{r.stderr[-800:]}")
page_file = courses.ROOT / "preview" / f"{lid}.html"
if not page_file.exists(): page_file = courses.ROOT / "site" / f"{lid}.html"
if not page_file.exists(): sys.exit(f"no built page for {lid}: run python scripts/build.py {lid}")


def stamp():
    """What the captures depend on: the content hashes, the built page and the shared templates (its rendering)."""
    h = hashlib.sha256(page_file.read_bytes())
    for f in sorted((courses.ROOT / "templates").rglob("*")):
        if f.is_file(): h.update(f.name.encode() + f.read_bytes())
    return f"{hashes} page {h.hexdigest()[:16]}"


OUT = review / "shots"
STAMP = OUT / "stamp.txt"
if "--if-stale" in sys.argv and STAMP.is_file() and STAMP.read_text().strip() == stamp() and (review / "shots.md").is_file():
    print(f"captures of {lid} are current ({STAMP.relative_to(courses.ROOT)}): reused"); sys.exit(0)
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
for old in review.glob(f"{lid}-*.png"): old.unlink()          # the full-page captures of the earlier script
rows = []


def save(pg, name, what, box=None, locator=None):
    """One capture (a locator, or a clip box in page coordinates), split into tiles when it is taller than TILE."""
    if locator is not None:
        if not locator.is_visible(): return          # e.g. a task's figure inside a closed exercise level
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
        if kind != "lesson":                          # an investigation, a guide or a Sovella set: the whole text, every box open, in tiles
            pg.evaluate("document.querySelectorAll('main details').forEach((d) => { d.open = true; })"); pg.wait_for_timeout(300)
            art = pg.locator("main article").first if pg.locator("main article").count() else pg.locator("main").first
            save(pg, f"page-{w}", f"the whole page at {w} px, every box open (teacher's notes included)", locator=art)
        if pg.locator("#sim").count(): save(pg, f"sim-{w}", f"simulation with controls and readout at {w} px", locator=pg.locator("#sim"))
        if w != 390:
            if pg.locator(".lab").count(): save(pg, f"lab-{w}", f"Tutki at {w} px: the simulation beside the experiments", locator=pg.locator(".lab").first)
            if pg.locator(".fig-row").count(): save(pg, f"fig-row-{w}", f"the first theory figure beside its paragraph at {w} px", locator=pg.locator(".fig-row").first)
            if pg.locator(".intro").count(): save(pg, f"intro-{w}", f"the opening at {w} px", locator=pg.locator(".intro").first)
            if pg.locator("#selita .act-theory").count(): save(pg, f"theory-{w}", f"Teoriatiivistelmä at {w} px: theory and figures", locator=pg.locator("#selita .act-theory").first)
            pg.evaluate("""() => { document.querySelectorAll('details.fold, .hints details, details.solution, details.answer').forEach((d) => { d.open = true; });
              document.querySelectorAll('fieldset.choice').forEach((f) => { const r = f.querySelector('input[type=radio]'); const b = f.querySelector('button.commit');
                if (r && b && !f.dataset.reveal) { r.checked = true; b.click(); } }); }""")
            pg.wait_for_timeout(400)
            for sid in ("ennusta", "tarkista"):
                if pg.locator(f"#{sid}").count(): save(pg, f"open-{sid}-{w}", f"{sid} at {w} px with hints, solutions and feedback open", locator=pg.locator(f"#{sid}"))
            if pg.locator("#exit").count(): save(pg, f"open-exit-{w}", f"the exit ticket at {w} px, answers open", locator=pg.locator("#exit"))
            for k, lvl in enumerate(pg.locator("#exercises details.level").all()):   # every level: the visual reviewer reads every solution
                lvl.evaluate("(d) => { d.open = true; d.querySelectorAll('details').forEach((x) => { x.open = true; }); }"); pg.wait_for_timeout(300)
                save(pg, f"open-exercises{'' if k == 0 else '-L' + str(k + 1)}-{w}", f"exercise level {k + 1} at {w} px, every solution open", locator=lvl)
            pg.close(); continue
        pg.evaluate("document.querySelectorAll('details.fold').forEach((d) => { d.open = true; })")   # the Ennusta box starts closed; reviewers read its predictions
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
            ex.evaluate("(e) => { for (let d = e.closest('details'); d; d = d.parentElement && d.parentElement.closest('details')) d.open = true; }")   # an optional experiment sits in a closed box
            start = ex.locator(".exp-start")
            if start.count() and start.is_visible(): start.click(); pg.wait_for_timeout(1500)   # the sim redraws its canvas after the reset
            save(pg, f"exp-{aid}-390", f"experiment {aid} after Aseta alkutila: the sim next to its buttons and table", locator=ex.locator("xpath=ancestor::div[contains(@class,'activity')][1]"))
        pg.close()
    b.close()



def contact_sheets(per=12, cols=4, thumb=300):
    """contact-N.png: the captures small and numbered (the # column of shots.md), for triage. Needs Pillow; without
    it the list alone serves."""
    try: from PIL import Image, ImageDraw
    except ImportError: return []
    out = []
    for k in range(0, len(rows), per):
        chunk = rows[k:k + per]; ims = []
        for f, *_ in chunk:
            im = Image.open(OUT / f).convert("RGB"); im.thumbnail((thumb, thumb * 2)); ims.append(im)
        rh = max(i.height for i in ims) + 28; n_rows = -(-len(ims) // cols)
        sheet = Image.new("RGB", (cols * (thumb + 12) + 12, n_rows * (rh + 12) + 12), "white"); d = ImageDraw.Draw(sheet)
        for j, im in enumerate(ims):
            x, y = 12 + (j % cols) * (thumb + 12), 12 + (j // cols) * (rh + 12)
            d.rectangle([x - 1, y + 27, x + im.width, y + 28 + im.height], outline="#9aa1a9"); sheet.paste(im, (x, y + 28))
            d.text((x, y + 6), f"#{k + j + 1}", fill="#c92a2a")
        name = f"contact-{k // per + 1}.png"; sheet.save(OUT / name); out.append((name, f"contact sheet: captures #{k + 1}–#{k + len(chunk)}", sheet.width, sheet.height))
    return out


sheets = contact_sheets()
lines = [f"# Screenshots of {lid} ({page_file.parent.name}/{page_file.name})", "",
         f"Captured for: {stamp()} (review/shots/stamp.txt). Open the contact sheets first, then only the captures your questions need (Read tool). Cost ≈ width·height/750 tokens each.", "",
         "| file | shows | px | ≈ tokens |", "|---|---|---|---|"]
lines += [f"| review/shots/{f} | {what} | {w}×{h} | {w * h // 750} |" for f, what, w, h in sheets]
lines += [f"| review/shots/{f} | #{i + 1} {what} | {w}×{h} | {w * h // 750} |" for i, (f, what, w, h) in enumerate(rows)]
(review / "shots.md").write_text("\n".join(lines) + "\n")
STAMP.write_text(stamp() + "\n")
print(f"wrote {len(rows)} captures and {len(sheets)} contact sheet(s) to {OUT.relative_to(courses.ROOT)}/ and the list to {(review / 'shots.md').relative_to(courses.ROOT)}")
