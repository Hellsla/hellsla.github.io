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

# static: the script is on the trial page only
pages_with = [p.relative_to(SITE).as_posix() for p in SITE.rglob("*.html") if "palautus.js" in p.read_text(errors="ignore")]
expect("palautus.js is loaded on the Finnish FY3-1 page only", pages_with == ["fy3-1.html"], pages_with)

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
        pg.click(".palautus-btn")
    return d.value.suggested_filename, json.loads(pathlib.Path(d.value.path()).read_text())


def no_download(pg):
    got = []
    pg.once("download", lambda d: got.append(d))
    pg.click(".palautus-btn")
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
    expect("only the button 'Lataa kaikki ratkaisut', no long instructions (teacher 2026-11-05)", ptext == "Lataa kaikki ratkaisut", ptext)
    expect("no separate image button (Ctrl+V only)", pg.locator(".pad-image").count() == 0)
    tasks = pg.evaluate("[...document.querySelectorAll('#exercises li[id]')].filter((li) => li.querySelector(':scope > .task')).map((li) => li.id)")
    # another chapter's solution in the same store must stay out
    pg.evaluate("""() => new Promise((ok) => { const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = ok; document.head.append(s); })""")
    pg.evaluate("window.flPadStore.put('fy3-2-L1-01', 'toisen luvun ratkaisu', 'fy3-2.html')")
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
    expect("format, version, chapter and a 32-hex submission id", f1.get("format") == "ruukkilabra-palautus" and f1.get("version") == 1 and f1.get("chapter") == "fy3-1"
           and re.fullmatch(r"[0-9a-f]{32}", f1.get("submission_id", "")) and f1.get("exported"), {k: v for k, v in f1.items() if k != "answers"})
    expect("every exercise once, in page order", [a["task"] for a in f1["answers"]] == tasks)
    expect("only this chapter (no fy3-2 solution)", "fy3-2" not in json.dumps(f1))
    expect("no name or e-mail fields", not set(f1) - {"format", "version", "chapter", "lang", "submission_id", "exported", "includes", "content_sha256", "answers"}, set(f1))
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
    expect("the page says to return the file with Forms", "Palauta ladattu tiedosto opettajan Google Forms -lomakkeella." in pg.inner_text(".palautus-status"))
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
        canon = json.dumps([{"task": a["task"], "status": a["status"], "content": [{"type": "math", "latex": i["latex"]} if i["type"] == "math" else i for i in a["content"]]} for a in g["answers"]], ensure_ascii=False, separators=(",", ":"))
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
           ("a newer version", modify(files["v1"], lambda g: g.update(version=2)), None, None, A, "uudempi"),
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
    tp.wait_for_selector("#tasks tbody tr")
    shot(tp, "arviointi-aloitus", full_page=True)
    home = tp.inner_text("#home")
    first = tp.locator("#tasks tbody tr").first.inner_text().split("\t")
    expect("task list: number, submissions, empty, graded (no class-size ratio)", first[0].strip() == "Tehtävä 1-1" and first[2:] == ["3", "0", "0"] and not re.search(r"\b\d+/\d+\b", home), (first, home[:300]))
    expect("the processing state lists invalid, duplicate and to-be-checked rows", all(w in tp.inner_text("#problems") for w in ["Virheellinen", "Kaksoiskappale", "Tarkistettava"]), tp.inner_text("#problems")[:200])
    tp.locator("#tasks tbody tr").first.click()
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
    tp.focus("body"); tp.evaluate("document.activeElement.blur()")
    tp.keyboard.press("2"); tp.keyboard.press("ArrowDown")
    tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 2/3'")
    sc = scores()
    expect("points are saved before moving, with student, version and task", sc == [[A, files["v2"]["submission_id"], tasks[0], 2]], sc)
    tp.wait_for_function("document.querySelector('#gAnswer .t, #gAnswer .empty')")
    tp.keyboard.press("ArrowUp"); tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 1/3'")
    tp.wait_for_function("!document.getElementById('points').disabled")
    expect("going back shows the saved points", tp.input_value("#points") == "2" and "Tallennettu" in tp.inner_text("#state"))
    # 0 and ungraded
    tp.fill("#points", "0"); tp.press("#points", "Enter"); tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 2/3'")
    tp.wait_for_function("!document.getElementById('points').disabled")
    expect("Enter keeps the cursor in the points field of the next student", tp.evaluate("document.activeElement.id") == "points")
    tp.keyboard.press("Escape"); tp.keyboard.press("ArrowUp"); tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 1/3'")
    expect("0 is a given score", scores()[0][3] == 0 and tp.input_value("#points") == "0", scores())
    tp.wait_for_function("!document.getElementById('points').disabled")
    tp.fill("#points", ""); tp.evaluate("document.activeElement.blur()"); tp.wait_for_function("document.getElementById('state').textContent.indexOf('arvioimaton') >= 0")
    expect("an emptied field is saved as ungraded (empty), not 0", scores()[0][3] == "", scores())
    # an invalid value
    tp.fill("#points", "5"); tp.evaluate("document.activeElement.blur()"); tp.keyboard.press("ArrowDown"); tp.wait_for_timeout(200)
    expect("a value outside 0–3 is refused and keeps the student", tp.inner_text("#gPos") == "Opiskelija 1/3" and "kokonaisluku 0–3" in tp.inner_text("#state") and scores()[0][3] == "", (tp.inner_text("#state"), scores()))
    # a save error keeps the student in place
    tp.fill("#points", "3"); E("() => { MOCK.fail.rlSaveScore = 2; }"); tp.evaluate("document.activeElement.blur()"); tp.wait_for_timeout(100)
    tp.keyboard.press("ArrowDown"); tp.wait_for_timeout(300)
    expect("a save error shows and stops the move", tp.inner_text("#gPos") == "Opiskelija 1/3" and "Tallennus epäonnistui" in tp.inner_text("#state") and scores()[0][3] == "", (tp.inner_text("#state"), scores()))
    E("() => { MOCK.fail.rlSaveScore = 0; MOCK.delay.rlSaveScore = 400; }")
    # rapid presses: one move, the points to the student shown when they were given
    tp.keyboard.press("ArrowDown"); tp.keyboard.press("ArrowDown"); tp.keyboard.press("ArrowDown")
    tp.wait_for_timeout(900)
    sc = scores()
    expect("rapid arrows move once and save to the right student", tp.inner_text("#gPos") == "Opiskelija 2/3" and sc[0][:4] == [A, files["v2"]["submission_id"], tasks[0], 3] and len(sc) == 1, (tp.inner_text("#gPos"), sc))
    E("() => { MOCK.delay.rlSaveScore = 0; }")
    tp.wait_for_function("!document.getElementById('points').disabled")
    tp.click("#points"); tp.keyboard.press("ArrowDown"); tp.wait_for_timeout(200)
    expect("arrows inside the points field do not move", tp.inner_text("#gPos") == "Opiskelija 2/3")
    tp.keyboard.press("Escape"); tp.click("#next"); tp.wait_for_function("document.getElementById('gPos').textContent === 'Opiskelija 3/3'")
    expect("the buttons move too", True)
    # B's file in task 1: v1 content; check student 2 is C (empty there? no: C has v1 = answered)
    tp.click("#back"); tp.wait_for_selector("#tasks tbody tr")
    first = tp.locator("#tasks tbody tr").first.inner_text().split("\t")
    expect("graded count in the list", first[4] == "1", first)
    # "Vain arvioimattomat"
    tp.check("#onlyOpen"); tp.locator("#tasks tbody tr").first.click(); tp.wait_for_function("document.getElementById('gPos').textContent !== ''")
    expect("Vain arvioimattomat leaves out graded students", tp.inner_text("#gPos") == "Opiskelija 1/2" and tp.inner_text("#gEmail") != A, (tp.inner_text("#gPos"), tp.inner_text("#gEmail")))
    tp.click("#back"); tp.wait_for_selector("#tasks tbody tr"); tp.uncheck("#onlyOpen")
    # older version keeps its own points; the latest is the default
    tp.locator("#tasks tbody tr").first.click(); tp.wait_for_function("!document.getElementById('points').disabled")
    tp.select_option("#gVer", "0"); tp.wait_for_function("document.getElementById('gTime').textContent.indexOf('versio 1/2') >= 0")
    tp.wait_for_function("!document.getElementById('points').disabled")
    expect("the older version has no points of the newer", tp.input_value("#points") == "")
    tp.fill("#points", "1"); tp.evaluate("document.activeElement.blur()"); tp.wait_for_function("document.getElementById('state').textContent.indexOf('Tallennettu') >= 0")
    sc = {(r[1], r[2]): r[3] for r in scores()}
    expect("points are kept per version", sc.get((files["v1"]["submission_id"], tasks[0])) == 1 and sc.get((files["v2"]["submission_id"], tasks[0])) == 3, sc)
    # reorder the score sheet: points stay with their student and version
    E("() => { const d = MOCK.sheet('RL Pisteet').data; const head = d.shift(); d.reverse(); d.unshift(head); }")
    tp.click("#back"); tp.wait_for_selector("#tasks tbody tr"); tp.locator("#tasks tbody tr").first.click(); tp.wait_for_function("!document.getElementById('points').disabled")
    expect("after reordering the rows the latest version still shows its own points", tp.input_value("#points") == "3", tp.input_value("#points"))
    # an empty task
    tp.click("#back"); tp.wait_for_selector("#tasks tbody tr"); tp.locator("#tasks tbody tr").nth(1).click()
    tp.wait_for_function("document.querySelector('#gAnswer .empty, #gAnswer .t')")
    expect("an unanswered task says so", "jätti tehtävän tyhjäksi" in tp.inner_text("#gAnswer"), tp.inner_text("#gAnswer"))
    expect("no formulas were written to the sheets", not E("MOCK.formulas"), E("MOCK.formulas"))
    expect("no script errors in the grading view", not terr, terr)
    b.close()
srv.shutdown()
print("all ok" if not fails else f"{fails} failure(s)")
sys.exit(1 if fails else 0)
