"""Submission and grading trial (teacher 2026-11-05; palautus/README.md). Usage: python scripts/test_palautus.py [site]

End to end with made-up answers, in a browser:
  Student side, on the built Finnish FY3-1 page (templates/palautus.js):
  - only the button "Lataa kaikki ratkaisut" at the top of Tehtävät (no long instructions, no image button: a
    screenshot is pasted with Ctrl+V; teacher 2026-11-05), and only on the trial page
  - the file fy3-1.ratkaisut.json: format and version, chapter, random submission id, every exercise once in page
    order, unanswered ones "empty"; text, formula (LaTeX + PNG) and a picture in their order in the right task; the
    last keystrokes of an open editor are in it; a solution of another chapter and any name or e-mail are not
  - the same solutions keep the submission id; a changed text, an added, replaced or removed picture give a new one
  - a failed save, a picture from the web, an SVG picture and a picture over the limit stop the download with a
    message
  - the panel and an open editor fit at 360, 768 and 1280 px
  Teacher side, palautus/apps-script/ with palautus/test/gas-mock.js standing in for Sheets, Drive and google.script.run:
  - import: normal, duplicate (same file again), the same id from two students (both to be checked), a corrected
    version, a broken, an over-size, a tampered and a malicious file (SVG/HTML as a picture), a file outside the
    submission folder, a missing e-mail; a re-run adds nothing; a read error is retried in place; a busy lock refuses;
    nothing is ever written as a formula; the Forms response sheet is never changed
  - grading view: the task list (submissions and graded, no class-size ratio), one student at a time with the
    statement, text, formula and picture (zoom on click), points saved before moving, 0 apart from ungraded, a save
    error that keeps the student in place, rapid arrow presses that move once and save to the right student, arrows
    inside the points field, "Vain arvioimattomat", the latest version by default with older points kept on their
    version, and points that stay with their student when the score sheet's rows are reordered
Exit status 1 on any failure."""
import base64, functools, http.server, json, pathlib, re, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

import os
args = sys.argv[1:]
SHOTS = os.environ.get("PALAUTUS_SHOTS")   # a folder: screenshots of the panel and the grading view for a look
SITE = ROOT / (args[0] if args and (ROOT / args[0]).is_dir() else "site")
GAS = ROOT / "palautus/apps-script"
fails = 0


def go_back(pg):
    """Back to the task list, waiting until the list is reloaded (the old rows stay visible meanwhile)."""
    pg.click("#back")
    pg.wait_for_function("!document.getElementById('home').hidden && document.getElementById('homeState').textContent !== 'Ladataan…'")
    pg.wait_for_selector("#tasks tr.task-row")


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


def png_bytes(w, h, rgb=(240, 200, 40)):
    """A plain one-colour PNG (no Pillow needed)."""
    import struct, zlib
    chunk = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    raw = b"".join(b"\0" + bytes(rgb) * w for _ in range(h))
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")


tmp = ROOT / "preview" / "palautus-test"; tmp.mkdir(parents=True, exist_ok=True)
small = tmp / "pieni.png"; small.write_bytes(png_bytes(40, 30))
other = tmp / "toinen.png"; other.write_bytes(png_bytes(30, 40, (40, 90, 200)))

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/"

# static: the script is on the FY3 chapter pages only
pages_with = sorted(p.relative_to(SITE).as_posix() for p in SITE.rglob("*.html") if "palautus.js" in p.read_text(errors="ignore"))
chapters = sorted(p.name for p in SITE.glob("fy*-*.html") if re.fullmatch(r"fy[1-8]-\d+\.html", p.name))
want = sorted(f"{d}{n}" for d in ("", "en/", "fi-easy/") for n in chapters if (SITE / d / n).is_file())   # teacher 2026-11-06: also English (and Selkeä suomi), every course FY1-FY8
expect("palautus.js is loaded on every FY1-FY8 chapter page (fi, en, fi-easy) and nowhere else", len([c for c in chapters if c.startswith("fy3-")]) >= 16 and {c.split("-")[0] for c in chapters} == {f"fy{i}" for i in range(1, 9)} and pages_with == want, sorted(set(pages_with) ^ set(want)))

OPEN = "document.querySelectorAll('#exercises details.level').forEach((d) => { d.open = true; })"


def open_pad(pg, tid):
    pg.click(f'[id="{tid}"] .pad-open')
    pg.wait_for_selector(f'[id="{tid}"] .rich-text-editor')


def paste_png(pg, tid, path):
    """A screenshot pasted with Ctrl+V: a paste event carrying a PNG file, as the clipboard gives it."""
    pg.locator(f'[id="{tid}"] .rich-text-editor').click(); pg.keyboard.press("End")
    pg.evaluate("""([tid, b64]) => { const bin = atob(b64), u = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i);
        const dt = new DataTransfer(); dt.items.add(new File([u], 'kuva.png', { type: 'image/png' }));
        document.querySelector(`[id="${tid}"] .rich-text-editor`).dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true })); }""",
        [tid, base64.b64encode(path.read_bytes()).decode()])
    pg.wait_for_timeout(300)


def download(pg):
    with pg.expect_download(timeout=15000) as d:
        pg.click("button.palautus-btn")
    return d.value.suggested_filename, json.loads(pathlib.Path(d.value.path()).read_text())


def no_download(pg):
    got = []
    pg.once("download", lambda d: got.append(d))
    pg.click("button.palautus-btn")
    pg.wait_for_function("document.querySelector('.palautus-status').dataset.state === 'no' || document.querySelector('.palautus-status').dataset.state === 'ok'", timeout=15000)
    pg.wait_for_timeout(300)
    return not got, pg.inner_text(".palautus-status")


def shot(page, name, **kw):
    if SHOTS:
        pathlib.Path(SHOTS).mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(pathlib.Path(SHOTS) / f"{name}.png"), **kw)


files = {}
with sync_playwright() as p:
    b = launch(p)
    # ---------------- student side ----------------
    ctx = b.new_context(accept_downloads=True, viewport={"width": 1280, "height": 900})
    pg = ctx.new_page()
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(BASE + "fy3-1.html"); pg.evaluate(OPEN)
    panel = pg.locator("#exercises .palautus")
    expect("the panel is at the top of Tehtävät", panel.count() == 1 and pg.evaluate("(() => { const p = document.querySelector('#exercises .palautus').previousElementSibling; return !!p && (p.matches('h2') || p.matches('.split-head')); })()"))
    ptext = panel.inner_text().strip()
    expect("only the button 'Lataa kaikki ratkaisut', no long instructions (teacher 2026-11-05)", ptext == "" and pg.locator("#exercises button.palautus-btn").count() == 1 and pg.inner_text("#exercises button.palautus-btn") == "Lataa kaikki ratkaisut", ptext)
    expect("the buttons are in the heading row: Lataa kaikki ratkaisut, Palauta, then 'Avaa tehtävät teorian viereen' (teacher 2026-11-05/06)", pg.evaluate("(() => { const b = document.querySelector('#exercises button.palautus-btn'); const a = b && b.nextElementSibling; return !!b && b.parentElement.matches('.split-head') && !!a && a.matches('a.palautus-link') && a.textContent === 'Palauta' && a.getAttribute('href') === 'palautukset.html' && !!a.nextElementSibling && a.nextElementSibling.matches('.split-toggle'); })()"))
    expect("the heading row's buttons are on one line at 1280 px", pg.evaluate("(() => { const t = [...document.querySelectorAll('#exercises .split-head > button, #exercises .split-head > a')].map((e) => Math.round(e.getBoundingClientRect().top)); return t.length === 3 && new Set(t).size === 1; })()"))
    pg.goto(BASE + "palautukset.html")
    links = pg.evaluate("[...document.querySelectorAll('main a.return-form')].map((a) => [a.textContent, a.getAttribute('href')])")
    expect("Palautukset page: period title and one button per group linking to its form", pg.inner_text("h1") == "Palautukset · 1. periodi · lv 2026-27" and ["FY3.2", "https://forms.gle/1JEQYSTidBPETrxbA"] in links and all(h.startswith(("https://forms.gle/", "https://docs.google.com/forms/")) for _, h in links), links)
    secs = pg.evaluate("[...document.querySelectorAll('main .return-course')].map((s) => [s.querySelector('h2').textContent.split(' ')[0], s.querySelectorAll('a.return-form').length, s.querySelectorAll('.return-none').length])")
    expect("Palautukset page: every course FY1-FY8 in order, a grey placeholder where a course has no forms (teacher 2026-11-06)", [c for c, *_ in secs][:8] == [f"FY{i}" for i in range(1, 9)] and all((n > 0) != (e > 0) for _, n, e in secs) and dict((c, n) for c, n, _ in secs).get("FY3", 0) >= 1, secs)
    expect("Palautukset page loads nothing from Google (links only)", not pg.evaluate("[...document.querySelectorAll('script[src],link[href],img[src],iframe')].some((e) => /google|gle/.test(e.src || e.href || ''))"))
    # English (teacher 2026-11-06: "onhan nämä samat painikkeet myös EN julkaisussa?") and Selkeä suomi
    for lang, dl, ret in (("en", "Download all solutions", "Submit"), ("fi-easy", "Lataa kaikki ratkaisut", "Palauta")):
        pg.goto(BASE + f"{lang}/fy3-4.html"); pg.evaluate(OPEN)
        row = pg.evaluate("[...document.querySelectorAll('#exercises .split-head > button.palautus-btn, #exercises .split-head > a.palautus-link')].map((e) => [e.textContent, e.getAttribute('href')])")
        expect(f"{lang}: the heading row has '{dl}' and '{ret}' (to palautukset.html)", row == [[dl, None], [ret, "palautukset.html"]], row)
        pg.goto(BASE + f"{lang}/palautukset.html")
        links = pg.evaluate("[...document.querySelectorAll('main a.return-form')].map((a) => [a.textContent, a.getAttribute('href')])")
        expect(f"{lang}: Palautukset page in its language with the same form links", ["FY3.2", "https://forms.gle/1JEQYSTidBPETrxbA"] in links and pg.evaluate("document.documentElement.lang") == ("en" if lang == "en" else "fi") and (lang != "en" or pg.inner_text("h1").startswith("Submissions")), links)
    pg.goto(BASE + "en/fy3-1.html"); pg.evaluate(OPEN)
    name, fe = download(pg)
    expect("en: the file is fy3-1.ratkaisut.json with lang 'en' and the same task ids as Finnish (one grading page for both)", name == "fy3-1.ratkaisut.json" and fe.get("lang") == "en" and fe.get("chapter") == "fy3-1" and [a["task"] for a in fe["answers"]][:1] == ["fy3-1-L1-01"], {k: v for k, v in fe.items() if k != "answers"})
    expect("en: the status after the download is English", pg.inner_text(".palautus-status").startswith("Submit the downloaded file"), pg.inner_text(".palautus-status"))
    pg.goto(BASE + "fy3-1.html"); pg.evaluate(OPEN)
    expect("no separate image button (Ctrl+V only)", pg.locator(".pad-image").count() == 0)
    tasks = pg.evaluate("[...document.querySelectorAll('#exercises li[id]')].filter((li) => li.querySelector(':scope > .task')).map((li) => li.id)")
    # another chapter's solution in the same store must stay out
    pg.evaluate("""() => new Promise((ok) => { const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = ok; document.head.append(s); })""")
    pg.evaluate("window.flPadStore.put('fy3-2-L1-01', 'toisen luvun ratkaisu', 'fy3-2.html')")
    # guided self-assessment of Tarkista osaamisesi (teacher 2026-11-06): a colour scale under every task and goal
    sa = pg.evaluate("[...document.querySelectorAll('#tarkista fieldset.sa-rate')].map((f) => [f.dataset.sa, f.querySelectorAll('input[type=radio]').length])")
    expect("self-assessment: five levels under every Tarkista task and every goal of the chapter, no separate key (teacher 2026-11-06)", len(sa) >= 5 and all(n == 5 for _, n in sa) and any(i.startswith("tavoite-") for i, _ in sa) and pg.locator("#tarkista .sa-key").count() == 0, sa)
    sa_task = sa[1][0]
    pg.click(f'fieldset[data-sa="{sa_task}"] .sa-opt[data-level="b"]')
    pg.click('fieldset[data-sa="tavoite-1"] .sa-opt[data-level="d"]'); pg.click('fieldset[data-sa="tavoite-1"] .sa-opt[data-level="c"]')
    expect("self-assessment: the chosen level's text shows under the scale", pg.inner_text(f'fieldset[data-sa="{sa_task}"] .sa-desc') == "Koen oivaltaneeni tämän asian", pg.inner_text(f'fieldset[data-sa="{sa_task}"] .sa-desc'))
    t1, t2 = tasks[0], tasks[3]
    open_pad(pg, t1)
    ed = pg.locator(f'[id="{t1}"] .rich-text-editor'); ed.click()
    pg.keyboard.type("Paino on "); pg.keyboard.press("Control+e"); pg.wait_for_timeout(300); pg.keyboard.type("G=mg"); pg.keyboard.press("Escape"); pg.wait_for_timeout(300)
    pg.keyboard.type(" eli")
    pg.keyboard.press("Enter"); pg.keyboard.type("toinen rivi")
    paste_png(pg, t1, small)
    pg.keyboard.type(" viimeinen")   # typed just before the download: must be in the file
    name, f1 = download(pg)
    files["v1"] = f1
    expect("the file is fy3-1.ratkaisut.json", name == "fy3-1.ratkaisut.json", name)
    expect("format, version (2: with the self-assessment), chapter and a 32-hex submission id", f1.get("format") == "ruukkilabra-palautus" and f1.get("version") == 2 and f1.get("chapter") == "fy3-1"
           and re.fullmatch(r"[0-9a-f]{32}", f1.get("submission_id", "")) and f1.get("exported"), {k: v for k, v in f1.items() if k != "answers"})
    expect("every exercise once, in page order", [a["task"] for a in f1["answers"]] == tasks)
    expect("only this chapter (no fy3-2 solution)", "fy3-2" not in json.dumps(f1))
    expect("no name or e-mail fields", not set(f1) - {"format", "version", "chapter", "lang", "submission_id", "exported", "includes", "content_sha256", "answers", "selfassessment"}, set(f1))
    sitems = (f1.get("selfassessment") or {}).get("items", [])
    expect("self-assessment in the same file: the rated items in page order, level and history with times", [(i["id"], i["level"], [h[0] for h in i["history"]]) for i in sitems] == [(sa_task, "b", ["b"]), ("tavoite-1", "c", ["d", "c"])]
           and all(re.fullmatch(r"\d{4}-\d\d-\d\dT[\d:.]+Z", h[1]) for i in sitems for h in i["history"]), sitems)
    a1 = f1["answers"][0]
    kinds = [i["type"] for i in a1["content"]]
    expect("text, formula, picture keep their order in the right task", a1["status"] == "answered" and kinds == ["text", "math", "text", "image", "text"], kinds)
    expect("the line break is kept", "\ntoinen rivi" in a1["content"][2]["text"], a1["content"][2])
    expect("the open editor's last keystrokes are in the file", a1["content"][-1]["text"].endswith("viimeinen"), a1["content"][-1])
    m = a1["content"][1]
    expect("the formula is its LaTeX with a PNG for the teacher", m["latex"] == "G=mg" and base64.b64decode(m["png"])[:4] == b"\x89PNG" and m["w"] > 0, {k: str(v)[:40] for k, v in m.items()})
    img = a1["content"][3]
    expect("the picture is embedded PNG data, not a blob or link", img["mime"] == "image/png" and base64.b64decode(img["data"]) == small.read_bytes() and (img["w"], img["h"]) == (40, 30))
    expect("unanswered tasks are 'empty' with no content", all(a["status"] == "empty" and a["content"] == [] for a in f1["answers"][1:]))
    expect("the page says to return the file with Forms", "Palauta ladattu tiedosto Palauta-napista oman ryhmäsi lomakkeella." in pg.inner_text(".palautus-status"))
    _, f1b = download(pg)
    expect("the same solutions keep the submission id", f1b["submission_id"] == f1["submission_id"] and f1b["content_sha256"] == f1["content_sha256"])
    # a second task with a picture, then change text / replace / remove the picture
    open_pad(pg, t2)
    pg.locator(f'[id="{t2}"] .rich-text-editor').click(); pg.keyboard.type("F = 7,0 N")
    _, f2 = download(pg)
    expect("a changed answer gives a new submission id", f2["submission_id"] != f1["submission_id"])
    files["v2"] = f2
    paste_png(pg, t2, small)
    _, f3 = download(pg)
    expect("an added picture gives a new id", f3["submission_id"] != f2["submission_id"])
    expect("the picture is in the second task", [i["type"] for i in f3["answers"][3]["content"]] == ["text", "image"], f3["answers"][3]["content"])
    pg.evaluate(f"""(src) => {{ const i = document.querySelector('[id="{t2}"] .rich-text-editor img:not([data-math-image])'); i.src = src; i.dispatchEvent(new Event('input', {{ bubbles: true }})); }}""",
                "data:image/png;base64," + base64.b64encode(other.read_bytes()).decode())
    pg.locator(f'[id="{t2}"] .rich-text-editor').click(); pg.keyboard.press("End"); pg.keyboard.type(" ")
    pg.keyboard.press("Backspace"); pg.wait_for_timeout(200)
    _, f4 = download(pg)
    expect("a replaced picture gives a new id", f4["submission_id"] != f3["submission_id"] and base64.b64decode(f4["answers"][3]["content"][1]["data"]) == other.read_bytes())
    pg.evaluate(f"""() => {{ document.querySelector('[id="{t2}"] .rich-text-editor img:not([data-math-image])').remove(); }}""")
    pg.locator(f'[id="{t2}"] .rich-text-editor').click(); pg.keyboard.type("!")
    _, f5 = download(pg)
    expect("a removed picture gives a new id", f5["submission_id"] != f4["submission_id"] and [i["type"] for i in f5["answers"][3]["content"]] == ["text"], f5["answers"][3]["content"])
    # failed save: no download, a message
    pg.evaluate("() => { window.__put = window.flPadStore.put; window.flPadStore.put = () => Promise.reject(Object.assign(new Error('x'), { code: 'failed' })); }")
    pg.locator(f'[id="{t1}"] .rich-text-editor').click(); pg.keyboard.press("End"); pg.keyboard.type(" lisää")
    none, msg = no_download(pg)
    expect("a failed save stops the download with a message", none and "ei saatu tallennettua" in msg, msg)
    pg.evaluate("() => { window.flPadStore.put = window.__put; }")
    pg.evaluate("() => window.flPads.flush()")
    # pictures that cannot be returned, put straight into the store as if pasted
    big_b64 = pg.evaluate("""() => { const c = document.createElement('canvas'); c.width = 1500; c.height = 1500; const g = c.getContext('2d'); const d = g.createImageData(1500, 1500);
        for (let i = 0; i < d.data.length; i++) d.data[i] = (Math.random() * 256) | 0; g.putImageData(d, 0, 0); return c.toDataURL('image/png'); }""")
    for label, html, want in [("a picture from the web", '<img src="https://example.org/kuva.png">', "verkkosivulta"),
                              ("an SVG picture", '<img src="data:image/svg+xml;base64,' + base64.b64encode(b'<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script></svg>').decode() + '">', "muoto ei kelpaa"),
                              ("a GIF picture", '<img src="data:image/gif;base64,R0lGODlhAQABAAAAACw=">', "muoto ei kelpaa"),
                              ("a picture over 2 MB", f'<img src="{big_b64}">', "liian suuri")]:
        pg.goto(BASE + "fy3-1.html"); pg.evaluate(OPEN)
        pg.evaluate("""() => new Promise((ok) => { const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = ok; document.head.append(s); })""")
        pg.evaluate("([id, h]) => window.flPadStore.put(id, h, 'fy3-1.html')", [tasks[5], "teksti " + html])
        none, msg = no_download(pg)
        ok = none and want in msg
        expect(f"{label}: never embedded, stops the download with a message", ok, msg)
        pg.evaluate("(id) => window.flPadStore.remove(id)", tasks[5])
    for w in (360, 768, 1280):
        pg.set_viewport_size({"width": w, "height": 900}); pg.wait_for_timeout(200)
        over = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        btn = pg.evaluate("document.querySelector('.palautus-btn').getBoundingClientRect().height")
        expect(f"{w} px: no horizontal scroll, button at least 40 px", over <= 0 and btn >= 40, (over, btn))
        if SHOTS:
            pg.evaluate("document.querySelector('#exercises .palautus').scrollIntoView()"); pg.wait_for_timeout(200); shot(pg, f"opiskelija-{w}")
    expect("no script errors on the page", not errors, errors)
    ctx.close()

    # ---------------- teacher side ----------------
    head = "".join(f"<script>{(GAS.parent / 'test/gas-mock.js' if n == 'mock' else GAS / n).read_text()}</script>" for n in ["mock", "Tehtavat.gs", "Code.gs"])
    tp = b.new_page(viewport={"width": 1400, "height": 900})
    terr = []
    tp.on("pageerror", lambda e: terr.append(str(e)))
    tp.set_content("<!doctype html><html><head>" + head + "</head><body></body></html>")
    E = lambda js, arg=None: tp.evaluate(js, arg)
    FOLDER = "kansio-palautukset"
    E("(f) => { RL_CONFIG.SUBMISSION_FOLDER_ID = f; }", FOLDER)
    resp_head = ["Aikaleima", "Sähköpostiosoite", "Palauta vastaukset"]
    E("(h) => { MOCK.addSheet('Lomakevastaukset 1', [h]); }", resp_head)
    n = [0]

    def submit(email, text, when, size=None, parent=None, fid=None):
        n[0] += 1
        fid = fid or f"tiedosto-{n[0]:02d}-abcdefghijklmnopqrstu"
        E("([id, text, size, parent]) => { MOCK.files[id] = { text, size: size === null ? undefined : size, parent: parent || undefined }; }", [fid, text, size, parent])
        E("([email, id, when]) => { MOCK.sheet('Lomakevastaukset 1').data.push([new Date(when), email, 'https://drive.google.com/open?id=' + id]); }", [email, fid, when])
        return fid

    def run_import():
        return E("() => { try { return { ok: rlImport_() }; } catch (e) { return { err: e.message }; } }")

    def subs():
        return E("() => (MOCK.sheet('RL Palautukset') || { data: [] }).data.slice(1).map((r) => ({ email: r[2], sub: r[3], status: r[4], reason: r[5] }))")

    def modify(f, fn):
        g = json.loads(json.dumps(f)); fn(g); return json.dumps(g)

    def reseal(g):   # recompute content_sha256 the way the page does (for a deliberately changed file that is otherwise valid)
        canon = [{"task": a["task"], "status": a["status"], "content": [{"type": "math", "latex": i["latex"]} if i["type"] == "math" else i for i in a["content"]]} for a in g["answers"]]
        canon = json.dumps({"answers": canon, "selfassessment": g["selfassessment"]["items"]} if g.get("version") == 2 else canon, ensure_ascii=False, separators=(",", ":"))
        import hashlib
        g["content_sha256"] = hashlib.sha256(canon.encode()).hexdigest(); return g

    va, vb = json.dumps(files["v1"]), json.dumps(files["v2"])
    A, B, C = "aino.opiskelija@koulu.example", "bertta.opiskelija@koulu.example", "cecilia.opiskelija@koulu.example"
    resp_before = None
    submit(A, va, "2026-11-05T08:00:00Z")                                   # normal
    submit(A, va, "2026-11-05T08:05:00Z")                                   # duplicate (same file again)
    submit(C, modify(files["v1"], lambda g: g.update(submission_id="c" * 32)), "2026-11-05T08:06:00Z")   # same content, own id (sha check: id is not in the hash)
    r = run_import()
    s = subs()
    expect("import: normal, duplicate and a second student", r.get("ok") and [x["status"] for x in s] == ["Hyväksytty", "Kaksoiskappale", "Hyväksytty"], (r, s))
    resp_before = E("() => JSON.stringify(MOCK.sheet('Lomakevastaukset 1').data)")
    r2 = run_import()
    expect("a re-run adds nothing and changes nothing", r2.get("ok") and r2["ok"]["added"] == 0 and subs() == s, (r2, subs()))
    # same id from another student
    submit(B, va, "2026-11-05T08:10:00Z")
    run_import(); s = subs()
    expect("the same id from two students: both to be checked, none lost", [x["status"] for x in s] == ["Tarkistettava", "Kaksoiskappale", "Hyväksytty", "Tarkistettava"]
           and B in s[0]["reason"] and A in s[3]["reason"], s)
    # corrected version from A (new id, new content)
    submit(A, vb, "2026-11-05T09:00:00Z")
    E("() => { const d = MOCK.sheet('RL Palautukset').data; d[1][6] = 'Hyväksy'; }")   # the teacher accepts A's first version
    # broken, too big, tampered, malicious, outside the folder, no e-mail, unknown task, newer version
    bad = [("not JSON", "{ei json", None, None, A, "ei ole JSON"),
           ("another format", json.dumps({"format": "muu", "version": 1}), None, None, A, "ei ole RuukkiLabran"),
           ("a newer version", modify(files["v1"], lambda g: g.update(version=3)), None, None, A, "uudempi"),
           ("a changed self-assessment", modify(files["v1"], lambda g: g["selfassessment"]["items"][0].update(level="a")), None, None, A, "tarkistussumma"),
           ("an unknown self-assessment level", json.dumps(reseal(json.loads(modify(files["v1"], lambda g: g["selfassessment"]["items"][0].update(level="e"))))), None, None, A, "tuntematon taso"),
           ("over the size limit", va, 9_500_000, None, A, "liian suuri"),
           ("a tampered answer", modify(files["v1"], lambda g: g["answers"][0]["content"][0].update(text="muutettu")), None, None, A, "tarkistussumma"),
           ("HTML as a PNG picture", json.dumps(reseal(json.loads(modify(files["v1"], lambda g: g["answers"][0]["content"][3].update(data=base64.b64encode(b"<html><script>alert(1)</script></html>").decode()))))), None, None, A, "ei ole PNG"),
           ("an SVG picture", json.dumps(reseal(json.loads(modify(files["v1"], lambda g: g["answers"][0]["content"][3].update(mime="image/svg+xml", data=base64.b64encode(b"<svg onload='alert(1)'/>").decode()))))), None, None, A, "kuvamuoto"),
           ("an HTML item", json.dumps(reseal(json.loads(modify(files["v1"], lambda g: g["answers"][0]["content"].append({"type": "html", "html": "<script>alert(1)</script>"}))))), None, None, A, "tuntematon sisältötyyppi"),
           ("an unknown task", json.dumps(reseal(json.loads(modify(files["v1"], lambda g: g["answers"].append({"task": "fy9-9", "status": "empty", "content": []}))))), None, None, A, "tuntematon tehtävä"),
           ("a missing task", json.dumps(reseal(json.loads(modify(files["v1"], lambda g: g["answers"].pop())))), None, None, A, "puuttuu tiedostosta"),
           ("outside the submission folder", va, None, "muu-kansio", A, "palautuskansiossa"),
           ("no e-mail", va, None, None, "", "sähköpostiosoite puuttuu")]
    for label, text, size, parent, email, _ in bad: submit(email, text, "2026-11-05T10:00:00Z", size, parent)
    E("() => { MOCK.sheet('Lomakevastaukset 1').data.push([new Date('2026-11-05T10:30:00Z'), '=HYPERLINK(\"https://example.org\")@x.fi', 'https://drive.google.com/open?id=tiedosto-kaava-abcdefghijklmnop']); MOCK.files['tiedosto-kaava-abcdefghijklmnop'] = { text: '{' }; }")
    retry = submit(B, vb.replace(files["v2"]["submission_id"], "b" * 32), "2026-11-05T11:00:00Z")
    E("(id) => { MOCK.failOnce[id] = true; }", retry)
    run_import(); s = subs()
    expect("the corrected version is a new accepted version", s[4]["status"] == "Hyväksytty" and s[4]["sub"] == files["v2"]["submission_id"], s[4])
    for i, (label, *_, want) in enumerate(bad):
        row = s[5 + i]
        expect(f"invalid: {label} → Virheellinen ({want})", row["status"] == "Virheellinen" and want in row["reason"], row)
    expect("a formula in the e-mail is stored as text, never as a formula", s[5 + len(bad)]["email"].startswith("=hyperlink") and not E("MOCK.formulas"), (s[5 + len(bad)], E("MOCK.formulas")))
    expect("a read error is recorded as Lukuvirhe", s[-1]["status"] == "Lukuvirhe", s[-1])
    r3 = run_import(); s2 = subs()
    expect("a re-run retries the read error in place, adds nothing else", r3["ok"]["added"] == 0 and r3["ok"]["retried"] == 1 and s2[-1]["status"] == "Hyväksytty" and len(s2) == len(s), (r3, s2[-1]))
    expect("the Forms response sheet is never changed by the import", E("() => JSON.stringify(MOCK.sheet('Lomakevastaukset 1').data)").startswith(resp_before[:-1]))
    E("() => { MOCK.locked = true; }"); r4 = run_import(); E("() => { MOCK.locked = false; }")
    expect("a busy lock refuses a second import with a message", "käynnissä" in r4.get("err", ""), r4)
    hdr = E("() => { MOCK.sheet('Lomakevastaukset 1').data[0] = ['Timestamp', 'Jotain', 'Palauta vastaukset']; try { rlImport_(); return ''; } catch (e) { return e.message; } }")
    E("(h) => { MOCK.sheet('Lomakevastaukset 1').data[0] = h; }", resp_head)
    expect("a missing e-mail column is reported with the headers seen", "sähköposti" in hdr and "Jotain" in hdr, hdr)

    # the grading view, in a page of its own with the same sheets and files
    state = E("() => MOCK.dump()")
    js = lambda n: (GAS.parent / "test/gas-mock.js" if n == "mock" else GAS / n).read_text()
    rhead = (f"<script>{js('mock')}</script><script>MOCK.load({json.dumps(state)});</script>".replace("</script><script>MOCK", "</script><script>MOCK").replace(json.dumps(state), json.dumps(state).replace("</", "<\\/"))
             + f"<script>{js('Tehtavat.gs')}</script><script>{js('Code.gs')}</script><script>RL_CONFIG.SUBMISSION_FOLDER_ID = {json.dumps(FOLDER)};</script>")
    tp.set_content((GAS / "Review.html").read_text().replace("<head>", "<head>" + rhead, 1))
    tp.wait_for_selector("#tasks tr.task-row")
    shot(tp, "arviointi-aloitus", full_page=True)
    home = tp.inner_text("#tasks tr.task-row")
    first = tp.locator("#tasks tr.task-row").first.inner_text().split("\t")
    expect("task list: number, solutions, graded, ungraded (no class-size ratio)", first[0].strip() == "Tehtävä 1-1" and first[2:] == ["3", "0", "3"] and not re.search(r"\b\d+/\d+\b", home), (first, home[:300]))
    fp = tp.evaluate("""() => { const t = document.getElementById('fingerprint'); return { cols: [...t.tHead.rows[0].cells].slice(1).map((c) => c.textContent),
      chapters: [...t.querySelectorAll('tbody th.ch')].map((c) => c.textContent), rows: [...t.tBodies[0].rows].filter((r) => r.cells[0].tagName === 'TD').map((r) => [...r.cells].slice(1).map((c) => c.dataset.level)) }; }""")
    flat = [k for r in fp["rows"] for k in r]
    expect("grading view: one fingerprint of the group, items by chapter as rows and students as columns (teacher 2026-11-06)", tp.is_visible("#selfSec") and len(fp["cols"]) >= 3
           and fp["chapters"] and fp["chapters"][0].startswith("Luku 1") and all(len(r) == len(fp["cols"]) for r in fp["rows"]) and "b" in flat and "c" in flat and "none" in flat, fp)
    expect("grading view: fingerprint colours: not answered white, 'not yet studied' grey", tp.evaluate("""() => [getComputedStyle(document.querySelector('#fingerprint td.sa-none')).backgroundColor,
      getComputedStyle(document.querySelector('.sa-legend .sa-x')).backgroundColor]""") == ["rgb(255, 255, 255)", "rgb(154, 154, 154)"])
    shot(tp, "osaamisen-sormenjalki", clip=tp.locator("#selfSec").bounding_box()) if SHOTS else None
    avg = tp.evaluate("[...document.querySelectorAll('#summary tbody tr')].map((tr) => tr.cells[4].textContent.trim())")
    expect("grading view: the summary shows each student's self-assessment average (required items only)", any(re.fullmatch(r"\d(,\d)?", a) for a in avg), avg)
    tp.click("#hideNames")
    hid = tp.evaluate("[...document.getElementById('fingerprint').tHead.rows[0].cells].slice(1).map((c) => c.textContent).concat([...document.querySelectorAll('#fingerprint td.c')].map((c) => c.title))")
    expect("grading view: 'Piilota nimet' hides the names in the fingerprint too", hid and all(h.startswith("Opiskelija ") for h in hid) and not any(n in "".join(hid) for n in fp["cols"]), hid[:5])
    tp.click("#hideNames")
    expect("the processing state lists invalid, duplicate and to-be-checked rows", all(w in tp.inner_text("#problems") for w in ["Virheellinen", "Kaksoiskappale", "Tarkistettava"]), tp.inner_text("#problems")[:200])
    tp.locator("#tasks tr.task-row").first.click()
    tp.wait_for_function("document.querySelector('#gAnswer .t')")
    tp.wait_for_timeout(200); shot(tp, "arviointi-vastaus", full_page=True)
    expect("one student at a time: 'Opiskelija 1/3', e-mail, time and version", tp.inner_text("#gPos") == "Opiskelija 1/3" and tp.inner_text("#gEmail") == A and "versio 2/2 (uusin)" in tp.inner_text("#gTime"), (tp.inner_text("#gPos"), tp.inner_text("#gEmail"), tp.inner_text("#gTime")))
    expect("the statement is shown with its formulas (MathML)", "Kappaleen massa" in tp.inner_text("#gStatement") and tp.locator("#gStatement math").count() > 0)
    # A's latest (v2) has task 1 answered with formula and picture
    expect("the answer: text, formula image with LaTeX, picture", tp.locator("#gAnswer img.math").count() == 1 and tp.get_attribute("#gAnswer img.math", "alt") == "G=mg" and tp.locator("#gAnswer img.shot").count() == 1)
    expect("the picture fits the width", tp.evaluate("(() => { const i = document.querySelector('#gAnswer img.shot'); return i.getBoundingClientRect().width <= document.getElementById('gAnswer').clientWidth; })()"))
    tp.click("#gAnswer img.shot"); expect("a click enlarges the picture", tp.evaluate("document.getElementById('zoom').style.display") == "block"); tp.keyboard.press("Escape")
    expect("no external loads in the answer", tp.evaluate("[...document.querySelectorAll('#gAnswer img')].every((i) => i.src.startsWith('data:image/png;base64,') || i.src.startsWith('data:image/jpeg;base64,'))"))
    tp.check("#showTex"); tp.wait_for_timeout(100)
    expect("formulas can be shown as LaTeX", tp.inner_text("#gAnswer code.math") == "G=mg"); tp.uncheck("#showTex")

    def scores():
        return E("() => (MOCK.sheet('RL Pisteet') || { data: [] }).data.slice(1).map((r) => [r[1], r[2], r[3], r[5]])")
    saved = lambda: tp.wait_for_function("document.getElementById('state').textContent.indexOf('Tallennettu') === 0")
    tp.focus("body"); tp.evaluate("document.activeElement.blur()")
    expect("points 0–1 per task (teacher 2026-11-05)", tp.inner_text("#range") == "0–1", tp.inner_text("#range"))
    tp.keyboard.press("1"); saved()
    expect("a digit gives the points and saves at once, with student, version and task", scores() == [[A, files["v2"]["submission_id"], tasks[0], 1]], scores())
    tp.keyboard.press("ArrowDown"); tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 2/3'")
    tp.wait_for_function("document.querySelector('#gAnswer .t, #gAnswer .empty')")
    tp.keyboard.press("ArrowUp"); tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 1/3'")
    tp.wait_for_function("!document.getElementById('points').disabled")
    expect("↓ next, ↑ previous; going back shows the saved points", tp.input_value("#points") == "1" and "Tallennettu" in tp.inner_text("#state"))
    tp.keyboard.press("ArrowLeft"); tp.wait_for_function("document.getElementById('points').value === '0'"); saved()
    expect("← takes a point off and saves at once; 0 is a given score", scores()[0][3] == 0, scores())
    tp.keyboard.press("ArrowLeft"); tp.wait_for_timeout(100)
    expect("← never goes below 0", tp.input_value("#points") == "0" and scores()[0][3] == 0, scores())
    tp.keyboard.press("ArrowRight"); tp.keyboard.press("ArrowRight"); tp.wait_for_timeout(200); saved()
    expect("→ adds a point and saves at once, never above the maximum 1", tp.input_value("#points") == "1" and scores()[0][3] == 1, (tp.input_value("#points"), scores()))
    # a decimal typed in the field
    tp.fill("#points", "0,5"); tp.press("#points", "Enter"); tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 2/3'")
    expect("0,5 typed in the field is saved; Enter moves on", scores()[0][3] == 0.5, scores())
    tp.wait_for_function("!document.getElementById('points').disabled")
    expect("Enter leaves the field, so the arrows work again", tp.evaluate("document.activeElement.id") != "points")
    tp.keyboard.press("ArrowUp"); tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 1/3'")
    tp.wait_for_function("!document.getElementById('points').disabled")
    expect("a decimal is shown with a comma", tp.input_value("#points") == "0,5", tp.input_value("#points"))
    tp.keyboard.press("Backspace"); tp.wait_for_function("document.getElementById('state').textContent.indexOf('arvioimaton') >= 0")
    expect("Backspace saves ungraded (empty), not 0", scores()[0][3] == "", scores())
    # an invalid value
    tp.fill("#points", "2"); tp.press("#points", "ArrowDown"); tp.wait_for_timeout(200)
    expect("a value outside 0–1 is refused and keeps the student", tp.inner_text("#gPos") == "Opiskelija 1/3" and "0–1" in tp.inner_text("#state") and scores()[0][3] == "", (tp.inner_text("#state"), scores()))
    tp.fill("#points", "0,333"); tp.press("#points", "ArrowDown"); tp.wait_for_timeout(200)
    expect("more than two decimals is refused", tp.inner_text("#gPos") == "Opiskelija 1/3" and scores()[0][3] == "", (tp.inner_text("#state"), scores()))
    # a save error keeps the student in place
    tp.fill("#points", "1"); E("() => { MOCK.fail.rlSaveScore = 2; }"); tp.evaluate("document.activeElement.blur()"); tp.wait_for_timeout(100)
    tp.keyboard.press("ArrowDown"); tp.wait_for_timeout(300)
    expect("a save error shows and stops the move", tp.inner_text("#gPos") == "Opiskelija 1/3" and "Tallennus epäonnistui" in tp.inner_text("#state") and scores()[0][3] == "", (tp.inner_text("#state"), scores()))
    E("() => { MOCK.fail.rlSaveScore = 0; MOCK.delay.rlSaveScore = 400; }")
    # rapid presses: one move, the points to the student shown when they were given
    tp.keyboard.press("ArrowDown"); tp.keyboard.press("ArrowDown"); tp.keyboard.press("ArrowDown")
    tp.wait_for_timeout(900)
    sc = scores()
    expect("rapid arrows move once and save to the right student", tp.inner_text("#gPos") == "Opiskelija 2/3" and sc[0][:4] == [A, files["v2"]["submission_id"], tasks[0], 1] and len(sc) == 1, (tp.inner_text("#gPos"), sc))
    E("() => { MOCK.delay.rlSaveScore = 0; }")
    tp.wait_for_function("!document.getElementById('points').disabled")
    tp.click("#points"); tp.keyboard.press("ArrowDown"); tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 3/3'")
    expect("↓ in the points field moves on too", tp.evaluate("document.activeElement.id") != "points")
    tp.wait_for_function("!document.getElementById('points').disabled")
    tp.keyboard.press("ArrowDown"); tp.wait_for_timeout(200)
    expect("↓ on the last student says the task is done", tp.inner_text("#gPos") == "Opiskelija 3/3" and "viimeinen" in tp.inner_text("#state"), tp.inner_text("#state"))
    tp.click("#prev"); tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 2/3'")
    expect("the buttons move too", True)
    # B's file in task 1: v1 content; check student 2 is C (empty there? no: C has v1 = answered)
    go_back(tp)
    first = tp.locator("#tasks tr.task-row").first.inner_text().split("\t")
    expect("graded and ungraded counts in the list", first[3] == "1" and first[4] == "2", first)
    # "Vain arvioimattomat"
    tp.check("#onlyOpen"); tp.locator("#tasks tr.task-row").first.click(); tp.wait_for_function("document.getElementById('gPos').textContent !== ''")
    expect("Vain arvioimattomat leaves out graded students", tp.inner_text("#gPos") == "Opiskelija 1/2" and tp.inner_text("#gEmail") != A, (tp.inner_text("#gPos"), tp.inner_text("#gEmail")))
    go_back(tp); tp.uncheck("#onlyOpen")
    # older version keeps its own points; the latest is the default
    tp.locator("#tasks tr.task-row").first.click(); tp.wait_for_function("!document.getElementById('points').disabled")
    tp.select_option("#gVer", "0"); tp.wait_for_function("document.getElementById('gTime').textContent.indexOf('versio 1/2') >= 0")
    tp.wait_for_function("!document.getElementById('points').disabled")
    expect("the older version has no points of the newer", tp.input_value("#points") == "")
    tp.fill("#points", "0,5"); tp.evaluate("document.activeElement.blur()"); tp.wait_for_function("document.getElementById('state').textContent.indexOf('Tallennettu') >= 0")
    sc = {(r[1], r[2]): r[3] for r in scores()}
    expect("points are kept per version", sc.get((files["v1"]["submission_id"], tasks[0])) == 0.5 and sc.get((files["v2"]["submission_id"], tasks[0])) == 1, sc)
    # reorder the score sheet: points stay with their student and version
    E("() => { const d = MOCK.sheet('RL Pisteet').data; const head = d.shift(); d.reverse(); d.unshift(head); }")
    go_back(tp); tp.locator("#tasks tr.task-row").first.click(); tp.wait_for_function("!document.getElementById('points').disabled")
    expect("after reordering the rows the latest version still shows its own points", tp.input_value("#points") == "1", tp.input_value("#points"))
    # an empty task
    go_back(tp); tp.uncheck("#onlyOpen"); tp.locator("#tasks tr.task-row").nth(1).click()
    tp.wait_for_function("document.getElementById('gAnswer').textContent !== 'Ladataan…'")
    expect("a task everyone left empty has no queue (teacher 2026-11-06: empty ones are not shown)", "ei ole ratkaisuja" in tp.inner_text("#gAnswer"), tp.inner_text("#gAnswer"))
    expect("no formulas were written to the sheets", not E("MOCK.formulas"), E("MOCK.formulas"))
    expect("no script errors in the grading view", not terr, terr)

    # ---------------- the local grading page (eduespoo blocks Apps Script; teacher 2026-11-05) ----------------
    # The whole course on one page; one Forms form, so one Drive folder and one zip, per group.
    import zipfile, hashlib
    gs = (GAS / "Tehtavat.gs").read_text()
    course = json.loads(gs[gs.index("{"):gs.rindex(";")])
    ch2 = [c for c in course["chapters"] if c["id"] == "fy3-2"][0]

    def chapter_file(ch, text, text2=None):
        given = {0: text} if text2 is None else {0: text, 1: text2}
        answers = [{"task": t["id"], "status": "answered" if i in given else "empty", "content": [{"type": "text", "text": given[i]}] if i in given else []} for i, t in enumerate(ch["tasks"])]
        text = text + "|" + (text2 or "")
        canon = json.dumps(answers, ensure_ascii=False, separators=(",", ":"))
        return json.dumps({"format": "ruukkilabra-palautus", "version": 1, "chapter": ch["id"], "lang": "fi", "submission_id": hashlib.md5(text.encode()).hexdigest(),
                           "exported": "2026-11-05T12:00:00.000Z", "includes": "solution-editor", "content_sha256": hashlib.sha256(canon.encode()).hexdigest(), "answers": answers})

    def make_zip(path, form, entries):
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            for name, text, when in entries:
                zi = zipfile.ZipInfo(f"{form} (File responses)/Palauta vastaukset (File responses)/" + name, date_time=when); zi.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(zi, text)
    zpath, zpath2 = tmp / "ryhma-a.zip", tmp / "ryhma-b.zip"
    FA, FB = "FY3.1 lv 2026-27 Palauta ratkaisut", "FY3.2 lv 2026-27 Palauta ratkaisut"   # Forms names (palautus/forms-ilme)
    make_zip(zpath, FA, [
        ("fy3-1.ratkaisut - Aino Opiskelija.json", json.dumps(files["v1"]), (2026, 11, 5, 10, 0, 0)),
        ("fy3-1.ratkaisut (1) - Aino Opiskelija.json", json.dumps(files["v1"]), (2026, 11, 5, 10, 5, 0)),
        ("fy3-1.ratkaisut - Bertta Opiskelija.json", json.dumps(files["v1"]), (2026, 11, 5, 10, 10, 0)),
        ("fy3-1.ratkaisut (2) - Aino Opiskelija.json", json.dumps(files["v2"]), (2026, 11, 5, 11, 0, 0)),
        ("fy3-2.ratkaisut - Aino Opiskelija.json", chapter_file(ch2, "Ainon työ ja energia"), (2026, 11, 5, 11, 15, 0)),
        ("kuva - Cecilia Opiskelija.json", "<html><script>alert(1)</script></html>", (2026, 11, 5, 11, 30, 0))])
    make_zip(zpath2, FB, [("fy3-2.ratkaisut - Daniel Opiskelija.json", chapter_file(ch2, "Danielin työ ja energia"), (2026, 11, 6, 9, 0, 0))])
    zcopy, zfy5, zanon = tmp / "kopio.zip", tmp / "fy5.zip", tmp / "nimeton.zip"
    make_zip(zcopy, FA + " (kopio)", [("fy3-2.ratkaisut - Eero Opiskelija.json", chapter_file(ch2, "Eeron työ"), (2026, 11, 6, 9, 0, 0))])
    make_zip(zfy5, "FY5.1 lv 2026-27 Palauta ratkaisut", [("fy5-1.ratkaisut - Eero Opiskelija.json", "{}", (2026, 11, 6, 9, 0, 0))])
    make_zip(zanon, "Palautukset", [("fy3-2.ratkaisut - Eero Opiskelija.json", chapter_file(ch2, "Eeron työ"), (2026, 11, 6, 9, 0, 0))])
    pages_ = sorted((ROOT / "palautus").glob("arviointi-*.html"))
    expect("one grading page, the running period's (teacher 2026-11-06: not one file per course)", [f.name for f in pages_] == ["arviointi-2026-27-p1.html"], [f.name for f in pages_])
    page = pages_[0]
    lctx = b.new_context(accept_downloads=True, viewport={"width": 1400, "height": 900}, bypass_csp=True)   # the test itself evaluates scripts; the page keeps its CSP for the teacher
    lp = lctx.new_page(); lerr = []; net = []
    lp.on("pageerror", lambda e: lerr.append(str(e)))
    lp.on("request", lambda r: net.append(r.url) if not r.url.startswith(("file:", "data:", "blob:")) else None)
    lp.on("dialog", lambda d: d.accept())
    lmsg = lambda: lp.inner_text("#localMsg")

    def load(zp, want="tiedostoa"):
        lp.evaluate("document.getElementById('localMsg').textContent = ''")
        lp.set_input_files("#pick", str(zp))
        lp.wait_for_function("(w) => document.getElementById('localMsg').textContent.indexOf(w) >= 0", arg=want)
        lp.wait_for_function("document.getElementById('homeState').textContent !== 'Ladataan…'")

    lp.goto(page.as_uri())
    lp.wait_for_selector("#import")
    expect("local page: one button 'Tuo tiedosto', no group fields (teacher 2026-11-06)", lp.inner_text("#import") == "Tuo tiedosto" and lp.locator("#newGroup, #addGroup").count() == 0
           and lp.is_hidden("#groupWrap") and lp.is_hidden("#more") and "Tuo tiedosto" in lmsg(), lmsg())
    expect("local page: the whole course, chapters in teaching order", lp.locator("details.chapter").count() == len(course["chapters"]) >= 16
           and lp.locator("details.chapter").nth(3).get_attribute("data-chapter") == "fy3-13", lp.locator("details.chapter").count())
    load(zpath)
    expect("local page: the group comes from the zip (form 'FY3.1 lv 2026-27 ...')", "ryhmä FY3.1" in lp.inner_text("#title"), lp.inner_text("#title"))
    msg = lmsg()
    expect("local page: reads the group's Drive zip and imports (name from the Forms file name)", "Ryhmä FY3.1: luettu 6 tiedostoa" in msg and "hyväksyttyjä 3" in msg and "kaksoiskappaleita 1" in msg and "tarkistettavia 1" in msg and "virheellisiä 1" in msg, msg)
    expect("local page: problems list with chapter, names and an accept button", "Bertta Opiskelija" in lp.inner_text("#problems") and "Luku 1" in lp.inner_text("#problems") and lp.locator("#problems button").count() >= 2, lp.inner_text("#problems")[:300])
    lp.evaluate("[...document.querySelectorAll('#problems tbody tr')].find((r) => r.cells[2].textContent === 'Bertta Opiskelija').querySelector('button').click()")
    lp.wait_for_function("document.querySelector('#problems') && document.querySelector('#problems').innerText.indexOf('Hyväksy · peru') >= 0")
    first = lp.locator("#tasks tr.task-row").first.inner_text().split("\t")
    expect("local page: accepted student joins the queue (Aino v2 + Bertta)", first[2] == "2", first)
    c2 = lp.inner_text('details.chapter[data-chapter="fy3-2"] > summary')
    expect("local page: chapters show their own submissions (chapter 2: Aino only), unsubmitted chapters closed", "palautuksia 1" in c2 and lp.evaluate("document.querySelector('details.chapter[data-chapter=\"fy3-2\"]').open")
           and not lp.evaluate("document.querySelector('details.chapter[data-chapter=\"fy3-3\"]').open"), c2)
    lp.locator("#tasks tr.task-row").first.click(); lp.wait_for_function("document.querySelector('#gAnswer .t')")
    expect("local page: grading title names the chapter", lp.inner_text("#gTitle") == "FY3 · Luku 1 · Tehtävä 1-1", lp.inner_text("#gTitle"))
    expect("local page: students in the order of their first accepted submission; picture and formula shown", lp.inner_text("#gEmail") == "Bertta Opiskelija" and "versio 1/1" in lp.inner_text("#gTime")
           and lp.locator("#gAnswer img.shot").count() == 1 and lp.locator("#gAnswer img.math").count() == 1, (lp.inner_text("#gEmail"), lp.inner_text("#gTime")))
    lp.evaluate("document.activeElement.blur()"); lp.keyboard.press("1"); lp.keyboard.press("ArrowDown")
    lp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 2/2'")
    lp.wait_for_function("!document.getElementById('points').disabled"); lp.keyboard.press("ArrowLeft"); lp.keyboard.press("ArrowUp")
    lp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 1/2'")
    go_back(lp)
    # chapter 2, task 1: only Aino
    lp.locator('details.chapter[data-chapter="fy3-2"] tr.task-row').first.click(); lp.wait_for_function("document.querySelector('#gAnswer .t')")
    expect("local page: a chapter's queue has only the students who returned it", lp.inner_text("#gPos") == "Opiskelija 1/1" and lp.inner_text("#gEmail") == "Aino Opiskelija" and "Ainon työ" in lp.inner_text("#gAnswer"), (lp.inner_text("#gPos"), lp.inner_text("#gAnswer")))
    lp.fill("#points", "0,5"); lp.press("#points", "Enter")
    lp.wait_for_function("document.getElementById('state').textContent.indexOf('Tallennettu') === 0")
    go_back(lp)
    # a task left empty is no solution: not in the queue, not counted (teacher 2026-11-06)
    row2 = lp.locator('details.chapter[data-chapter="fy3-1"] tr.task-row').nth(1)
    expect("local page: an empty task shows no solutions", row2.inner_text().split("\t")[2:] == ["0", "0", "0"], row2.inner_text())
    row2.click(); lp.wait_for_function("document.getElementById('gAnswer').textContent !== 'Ladataan…'")
    expect("local page: an empty task's queue is empty, nothing shown as 'jätti tyhjäksi'", "ei ole ratkaisuja" in lp.inner_text("#gAnswer") and "jätti tehtävän tyhjäksi" not in lp.inner_text("#grade"), lp.inner_text("#gAnswer"))
    go_back(lp)
    # Vain arvioimattomat: only the chapters and tasks that have a solution without points (teacher 2026-11-06)
    lp.check("#onlyOpen")
    open_rows = lp.evaluate("[...document.querySelectorAll('#tasks tr.task-row')].map((r) => [r.closest('details').dataset.chapter, r.cells[4].textContent])")
    expect("local page: 'Vain arvioimattomat' lists only chapters and tasks with unscored solutions", open_rows and all(n != "0" for _, n in open_rows) and lp.locator("#tasks details.chapter").count() < len(course["chapters"])
           and not any(t.startswith("fy3-3") for t, _ in open_rows), open_rows[:5])
    lp.uncheck("#onlyOpen")
    expect("local page: unticked, every chapter is listed again", lp.locator("#tasks details.chapter").count() == len(course["chapters"]))
    shot(lp, "arviointi-kooste", full_page=False)
    n1 = lambda f: sum(1 for a in f["answers"] if a["status"] == "answered")
    a_v2, b_v1 = n1(files["v2"]), n1(files["v1"])
    rows = lambda: lp.evaluate("JSON.stringify([...document.querySelectorAll('#summary tbody tr')].map((tr) => [...tr.cells].map((c) => c.textContent)))")
    # the chapters' task counts come from the generated file (the exercise bank grows: fy3-1 and fy3-2 have 21 since #345)
    m1, m2 = (len([c for c in course["chapters"] if c["id"] == k][0]["tasks"]) for k in ("fy3-1", "fy3-2"))
    want = [["Aino Opiskelija", f"{a_v2 + 1} / {m1 + m2}", str(a_v2 - 1), f"0,5 / {m1 + m2}", "2,5"], ["Bertta Opiskelija", f"{b_v1} / {m1 + m2}", str(b_v1 - 1), f"1 / {m1 + m2}", "2,5"]]
    expect("local page: summary with names on the left: done, unchecked, points (all returned chapters)", rows() == json.dumps(want, ensure_ascii=False, separators=(",", ":"))
           and [c.strip() for c in lp.inner_text("#summary thead").split("\t")][:1] == ["OPISKELIJA ▲"], (rows(), lp.inner_text("#summary thead")))
    lp.click('#summary button[data-key="points"]')
    expect("local page: a click on a heading sorts (points, highest first)", json.loads(rows())[0][0] == "Bertta Opiskelija" and "▼" in lp.inner_text("#summary thead"), rows())
    lp.select_option("#from", "fy3-2"); lp.select_option("#to", "fy3-2")
    expect("local page: chapters from–to: the summary of one chapter", json.loads(rows()) == [["Aino Opiskelija", f"1 / {m2}", "0", f"0,5 / {m2}", "–"], ["Bertta Opiskelija", f"0 / {m2}", "0", f"0 / {m2}", "–"]], rows())
    expect("local page: chapters from–to limit the task list too (teacher 2026-11-06)", lp.evaluate("[...document.querySelectorAll('#tasks details.chapter')].map((d) => d.dataset.chapter)") == ["fy3-2"])
    lp.select_option("#from", course["chapters"][0]["id"]); lp.select_option("#to", course["chapters"][-1]["id"])
    expect("local page: the whole course again", lp.locator("#tasks details.chapter").count() == len(course["chapters"]))
    lp.click('#summary button[data-key="name"]')
    gc = lp.inner_text("#groupChart")
    expect("local page: chart of the group: done and points out of the maximum (teacher 2026-11-06)", lp.is_visible("#groupChart") and "Tehty" in gc and "Pisteet" in gc and f"({a_v2 + 1 + b_v1} / {2 * (m1 + m2)})" in gc
           and lp.locator("#summary tbody .meter").count() == 4 and lp.evaluate("document.querySelector('#summary tbody .meter.pts > span').style.width") not in ("", "0%"), gc)
    # names hidden for showing the points to the class (teacher 2026-11-06)
    lp.click("#hideNames")
    hidden_txt = lp.inner_text("#home")
    expect("local page: 'Piilota nimet' leaves no name on the home view (summary numbered, problems hidden, not alphabetical)", "Aino" not in hidden_txt and "Bertta" not in hidden_txt and "Cecilia" not in hidden_txt
           and json.loads(rows())[0][0] == "Opiskelija 1" and json.loads(rows())[0][3].startswith("1 /") and lp.inner_text("#hideNames") == "Näytä nimet", hidden_txt[:300])
    lp.locator("#tasks tr.task-row").first.click(); lp.wait_for_function("document.querySelector('#gAnswer .t')")
    expect("local page: names hidden in the grading view too", lp.inner_text("#gEmail").startswith("Opiskelija ") and "Opiskelija" not in lp.inner_text("#gEmail")[11:], lp.inner_text("#gEmail"))
    go_back(lp)
    lp.click("#hideNames")
    expect("local page: 'Näytä nimet' brings the names back", "Aino Opiskelija" in lp.inner_text("#summary") and lp.is_visible("#probSec"), lp.inner_text("#summary")[:200])
    lp.click("#more > summary")
    with lp.expect_download() as d: lp.click("#csv")
    csv = [r.split(";") for r in pathlib.Path(d.value.path()).read_text(encoding="utf-8-sig").splitlines()]
    n_ch = len(course["chapters"])
    expect("local page: CSV per group: chapters, total, returned chapters, done, unchecked (decimal comma; 0 kept apart from not returned)", d.value.suggested_filename == "FY3-FY3.1-pisteet.csv" and csv[0][:3] == ["Opiskelija", f"Luku 1 (max {m1})", f"Luku 2 (max {m2})"]
           and csv[0][n_ch + 1:] == ["Yhteensä", "Palautettuja lukuja", "Tehty", "Tarkistamatta"] and csv[1][:4] == ["Aino Opiskelija", "0", "0,5", ""] and csv[1][n_ch + 1:] == ["0,5", "2", str(a_v2 + 1), str(a_v2 - 1)]
           and csv[2][:3] == ["Bertta Opiskelija", "1", ""] and csv[2][n_ch + 1:n_ch + 3] == ["1", "1"], (d.value.suggested_filename, csv[:3]))
    # another form named for the same group is not read into it; another course, and a form with no group, neither
    load(zcopy, "Mitään ei luettu")
    expect("local page: a zip from another form of the same group name is refused", "(kopio)" in lmsg() and "Eero" not in lp.inner_text("#home"), lmsg())
    load(zfy5, "ei ole tällä arviointisivulla")
    load(zanon, "Ryhmää ei tunnistettu")
    expect("local page: neither another course nor a nameless form adds a group", lp.is_hidden("#groupWrap") and "Eero" not in lp.inner_text("#home"), lmsg())
    # reopen: group, points and imports kept in this browser, files read again without duplicates
    lp.reload(); lp.wait_for_selector("#tasks tr.task-row"); lp.wait_for_function("document.getElementById('homeState').textContent !== 'Ladataan…'")
    first = lp.locator("#tasks tr.task-row").first.inner_text().split("\t")
    expect("local page: after reopening the group, points and imports are kept", lp.input_value("#group") == "FY3.1" and first[2] == "2" and first[3] == "2" and first[4] == "0", (lp.input_value("#group"), first))
    lp.locator("#tasks tr.task-row").first.click(); lp.wait_for_function("document.querySelector('#gAnswer .err, #gAnswer .t')")
    expect("local page: after reopening, the answers are still shown without a new import (IndexedDB, teacher 2026-11-06)", lp.locator("#gAnswer .t").count() >= 1 and lp.locator("#gAnswer .err").count() == 0 and lp.locator("#gAnswer img.shot").count() == 1, lp.inner_text("#gAnswer"))
    go_back(lp)
    load(zpath)
    expect("local page: reading the same zip again adds nothing", "Uusia palautuksia 0" in lmsg(), lmsg())
    # a new version of a chapter: an unchanged task solution keeps its points, a new or changed one is to be graded (teacher 2026-11-06)
    zre, zre2 = tmp / "uusi-versio.zip", tmp / "muutettu.zip"
    make_zip(zre, FA, [("fy3-2.ratkaisut (1) - Aino Opiskelija.json", chapter_file(ch2, "Ainon työ ja energia", "Ainon uusi ratkaisu"), (2026, 11, 6, 12, 0, 0))])
    make_zip(zre2, FA, [("fy3-2.ratkaisut (2) - Aino Opiskelija.json", chapter_file(ch2, "Ainon korjattu työ", "Ainon uusi ratkaisu"), (2026, 11, 6, 13, 0, 0))])
    load(zre)
    t1 = lambda: lp.locator('details.chapter[data-chapter="fy3-2"] tr.task-row').nth(0).inner_text().split("\t")
    t2 = lambda: lp.locator('details.chapter[data-chapter="fy3-2"] tr.task-row').nth(1).inner_text().split("\t")
    expect("local page: new version, unchanged task 1 keeps its points, new task 2 is unscored", "Uusia palautuksia 1" in lmsg() and t1()[3:] == ["1", "0"] and t2()[2:] == ["1", "0", "1"], (lmsg(), t1(), t2()))
    lp.locator('details.chapter[data-chapter="fy3-2"] tr.task-row').first.click(); lp.wait_for_function("document.querySelector('#gAnswer .t')")
    expect("local page: the grading view tells where the points came from", lp.input_value("#points") == "0,5" and "versiosta 1" in lp.inner_text("#state") and "versio 2/2" in lp.inner_text("#gTime"), (lp.input_value("#points"), lp.inner_text("#state")))
    go_back(lp)
    load(zre2)
    expect("local page: a changed solution is to be graded again, the unchanged task 2 is not counted twice", t1()[3:] == ["0", "1"] and t2()[2:] == ["1", "0", "1"], (t1(), t2()))
    # a second group: its own form, students and points, made from the zip alone
    load(zpath2)
    expect("local page: the second group from its zip; a group menu appears", "ryhmä FY3.2" in lp.inner_text("#title") and lp.is_visible("#groupWrap"), lp.inner_text("#title"))
    expect("local page: the second group has only its own students", "Daniel Opiskelija" in lp.inner_text("#summary") and "Aino" not in lp.inner_text("#summary"), lp.inner_text("#summary"))
    lp.select_option("#group", "FY3.1"); lp.wait_for_function("document.getElementById('title').textContent.indexOf('ryhmä FY3.1') >= 0")
    lp.wait_for_function("document.getElementById('homeState').textContent !== 'Ladataan…'")
    expect("local page: switching back shows the first group's students and points only", "Aino Opiskelija" in lp.inner_text("#summary") and "Daniel" not in lp.inner_text("#summary"), lp.inner_text("#summary"))
    # both zips at once: each goes to its own group
    lp.reload(); lp.wait_for_selector("#import")
    lp.evaluate("document.getElementById('localMsg').textContent = ''")
    lp.set_input_files("#pick", [str(zpath), str(zpath2)])
    lp.wait_for_function("document.getElementById('localMsg').textContent.indexOf('Ryhmä FY3.2') >= 0")
    expect("local page: two zips at once, each read into its own group", "Ryhmä FY3.1: luettu 6" in lmsg() and "Ryhmä FY3.2: luettu 1" in lmsg(), lmsg())
    # groups made before 2026-11-06 (per course keys) are kept
    lp.evaluate("""() => { localStorage.setItem('ruukkilabra:arviointi:FY3:ryhmat', JSON.stringify(['FY03.9']));
      localStorage.setItem('ruukkilabra:arviointi:FY3:ryhma:FY03.9', JSON.stringify({format: 'ruukkilabra-arviointi', version: 1, course: 'FY3', group: 'FY03.9', forms: [], sheets: []})); }""")
    lp.reload(); lp.wait_for_selector("#import")
    expect("local page: an older group is moved to the new storage", "FY03.9" in lp.evaluate("[...document.querySelectorAll('#group option')].map((o) => o.value)"), lp.evaluate("[...document.querySelectorAll('#group option')].map((o) => o.value)"))
    lp.select_option("#group", "FY3.2"); lp.wait_for_function("document.getElementById('title').textContent.indexOf('ryhmä FY3.2') >= 0")
    lp.click("#more > summary"); lp.click("#clear"); lp.wait_for_function("document.getElementById('localMsg').textContent.indexOf('poistettu') >= 0")
    kept = lp.evaluate("""() => new Promise((ok) => { const r = indexedDB.open('ruukkilabra-arviointi'); r.onsuccess = () => {
      const q = r.result.transaction('palautukset').objectStore('palautukset').getAllKeys(); q.onsuccess = () => ok(q.result); }; })""")
    expect("local page: 'Poista ryhmä' removes the group's files from the browser too", "FY3.2" not in kept and "FY3.1" in kept, kept)
    expect("local page: nothing loaded from the network", not net, net)
    expect("local page: no script errors", not lerr, lerr)
    lctx.close()
    b.close()
srv.shutdown()
print("all ok" if not fails else f"{fails} failure(s)")
sys.exit(1 if fails else 0)
