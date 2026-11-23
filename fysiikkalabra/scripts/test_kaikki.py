#!/usr/bin/env python3
"""The whole work in one file (work queue 17b PR 1): "ruukkilabra-kaikki" v1, Tallenna kaikki työni tiedostoon / Avaa kaikki
työni tiedostosta on Tietosuoja (templates/kaikki.js, padstore.js work()).
Usage: python scripts/test_kaikki.py [site]     (default site/; a preview build: preview)

One browser profile gets work in two modules (FY3 and FY10 must not mix), the card deck and the chapter opened last, ticks
and a solution; the file is saved and opened in a second profile, which then holds the same. A broken, foreign or newer file
changes nothing; a module work file and a submission are refused with the right message; the teacher's grading page rejects the
backup. Exit status 1 on any failure."""
import functools, http.server, json, pathlib, re, subprocess, sys, tempfile, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

SITE = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "site")
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {str(detail)[:600]}"))
    fails += not ok


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def end_headers(self):
        self.send_header("Cache-Control", "no-store"); super().end_headers()


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/"
TMP = pathlib.Path(tempfile.mkdtemp())

for lang, pre in (("fi", ""), ("en", "en/"), ("fi-easy", "fi-easy/")):
    t = (SITE / pre / "tietosuoja.html").read_text()
    expect(f"{lang}: Tietosuoja has the host, the texts and both scripts (padstore.js before kaikki.js)",
           'id="kaikki-tyo"' in t and 'id="fl-kaikki"' in t and re.search(r'padstore\.js[^>]*></script><script src="(\.\./)?kaikki\.js', t) is not None)
    k = json.loads(re.search(r'<script id="fl-kaikki" type="application/json">(.*?)</script>', t, re.S).group(1).replace("<\\/", "</"))
    expect(f"{lang}: the new texts are there", all(k.get(x) for x in ("kaikki_save", "kaikki_open", "kaikki_wrong", "palautus_conflict")), list(k))

SEED = r"""async () => {
  await new Promise((ok, no) => { const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = ok; s.onerror = no; document.head.append(s); });
  const ps = window.flPadStore;
  await ps.put('fy3-4-L1-02', '<p>ratkaisu <b>fy3</b></p>', 'fy3-4');
  await ps.put('fy10-sahko-1', '<p>fy10</p>', 'fy10-sahko');
  await ps.put('fy1-2-L1-01', '<p>fy1</p>', 'fy1-2');
  const set = (k, v) => localStorage.setItem(k, typeof v === 'string' ? v : JSON.stringify(v));
  set('ruukkilabra:vastaukset:fy3-4', { v: 1, items: { 'x:num1': '12,5' } });
  set('ruukkilabra:vastaukset:fy10-sahko', { v: 1, items: { 'y:num1': '7' } });
  set('ruukkilabra:itsearvio:fy3-4', { v: 1, items: { 'tavoite-1': { level: 'b' } } });
  set('ruukkilabra:kortit', { 'fy3-voima': { tila: 'osasin', osasinPutki: 3, muokattu: '2026-11-20T10:00:00.000Z' } });
  set('ruukkilabra:kortit-suunta', 'kaanteinen');
  set('ruukkilabra:viimeisin', { pre: '', file: 'fy3-4.html', title: 'x', num: 'FY3 · Luku 4' });
  set('ruukkilabra:readaloud:speed', '1.2');                 // not in the file
  set('ruukkilabra:palautus:FY3', { sha: 'x', id: 'y' });    // not in the file
  set('ruukkilabra:ratkaistu', { 'fy3-4-L1-02': '2026-11-20T10:05:00.000Z', 'fy10-sahko-1': '2026-11-21T10:05:00.000Z' });
  ps.mergeDone({ v: 1, done: { 'fy3-4-L1-02': '2026-11-20T10:06:00.000Z' }, log: [['fy3-4-L1-02', '2026-11-20T10:06:00.000Z', 1]] }, true);
  return true;
}"""
STATE = r"""async () => {
  const ps = window.flPadStore, out = { keys: {}, sols: (await ps.all()).solutions.map((r) => r.id + '=' + r.html).sort(), done: ps.readDone() };
  for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (/^(fl:|ruukkilabra:)/.test(k) && !k.startsWith('ruukkilabra:avattu')) out.keys[k] = localStorage.getItem(k); }
  return out;
}"""


def new_page(b, url, **kw):
    ctx = b.new_context(accept_downloads=True, **kw)
    p = ctx.new_page(); p.on("dialog", lambda d: d.accept()); p.goto(BASE + url)
    p.wait_for_selector("#kaikki-tyo .palautus-btn", state="attached")
    return ctx, p


def load(p):   # padstore is loaded by the page; keep tests independent of order
    return p.evaluate("() => !!window.flPadStore")


def open_file(p, path):
    p.set_input_files("#kaikki-tyo input[type=file]", str(path))


def wait_status(p):   # after "Tallennetaan…" (busy) the result, or the message carried over the reload
    p.wait_for_function("() => { const s = document.querySelector('#kaikki-tyo .palautus-status'); return s && s.textContent && !s.textContent.startsWith('Tallennetaan'); }")


def say(p): return p.eval_on_selector("#kaikki-tyo .palautus-status", "e => e.textContent")


with sync_playwright() as pw:
    b = launch(pw)
    ctx, p = new_page(b, "tietosuoja.html")
    btns = p.eval_on_selector_all("#kaikki-tyo .palautus-btn", "es => es.map(e => e.textContent)")
    expect("two buttons on Tietosuoja, under the browser-storage section", len(btns) == 2 and btns[0].startswith("Tallenna") and btns[1].startswith("Avaa"), btns)
    pos = p.evaluate("() => { const h = [...document.querySelectorAll('article h2')]; const host = document.getElementById('kaikki-tyo'); "
                     "const i = h.findIndex((x) => x.compareDocumentPosition(host) & 4 && !(h.some((y) => y !== x && x.compareDocumentPosition(y) & 4 && y.compareDocumentPosition(host) & 4))); return h[i] && h[i].textContent; }")
    expect("the buttons are in the section 'Mitä selaimeesi tallentuu?'", pos == "Mitä selaimeesi tallentuu?", pos)
    p.evaluate(SEED)
    before = p.evaluate(STATE)
    with p.expect_download() as dl:
        p.click("#kaikki-tyo .palautus-btn:first-child")
    path = TMP / dl.value.suggested_filename; dl.value.save_as(path)
    expect("file name Ruukkilabra_kaikki_<date>_<time>.json", re.fullmatch(r"Ruukkilabra_kaikki_\d{4}-\d\d-\d\d_\d{6}\.json", path.name), path.name)
    d = json.loads(path.read_text())
    expect("format and version", d["format"] == "ruukkilabra-kaikki" and d["version"] == 1 and d["lang"] == "fi" and re.fullmatch(r"[0-9a-f]{64}", d["content_sha256"]))
    expect("modules FY1, FY3 and FY10 each with their own records", sorted(d["modules"]) == ["FY1", "FY10", "FY3"]
           and [r["id"] for r in d["modules"]["FY3"]["store"]["solutions"]] == ["fy3-4-L1-02"]
           and [r["id"] for r in d["modules"]["FY10"]["store"]["solutions"]] == ["fy10-sahko-1"]
           and [r["id"] for r in d["modules"]["FY1"]["store"]["solutions"]] == ["fy1-2-L1-01"], list(d["modules"]))
    expect("FY1 and FY10 keys do not mix", all("fy10" not in k for k in d["modules"]["FY1"]["store"]["local"]) and all("fy3" not in k for k in d["modules"]["FY10"]["store"]["local"]))
    expect("the module's local store is what the work file would hold (answers, self-assessment, counter map)",
           "ruukkilabra:vastaukset:fy3-4" in d["modules"]["FY3"]["store"]["local"] and "ruukkilabra:itsearvio:fy3-4" in d["modules"]["FY3"]["store"]["local"]
           and list(json.loads(d["modules"]["FY3"]["store"]["local"]["ruukkilabra:ratkaistu"])) == ["fy3-4-L1-02"])
    expect("site keys: cards, card direction, chapter opened last", sorted(d["site"]) == ["ruukkilabra:kortit", "ruukkilabra:kortit-suunta", "ruukkilabra:viimeisin"], list(d["site"]))
    expect("progress (Tehty ticks) in the file", d["progress"] and "fy3-4-L1-02" in d["progress"]["done"])
    blob = path.read_text()
    expect("nothing else: no read-aloud setting, no palautus id", "readaloud" not in blob and "ruukkilabra:palautus:" not in blob)
    ctx.close()

    # second profile: open
    ctx, p = new_page(b, "tietosuoja.html")
    open_file(p, path); wait_status(p)
    msg = say(p)
    p.evaluate("() => new Promise((ok, no) => { const s = document.createElement('script'); s.src = 'padstore.js'; s.onload = ok; s.onerror = no; if (window.flPadStore) ok(); else document.head.append(s); })")
    after = p.evaluate(STATE)
    expect("a fresh browser gets everything back: solutions, answers, self-assessment, cards, last chapter, ticks",
           after["sols"] == before["sols"] and after["done"]["done"] == before["done"]["done"]
           and all(after["keys"].get(k) == v for k, v in before["keys"].items() if k.startswith(("ruukkilabra:vastaukset", "ruukkilabra:itsearvio", "ruukkilabra:kortit", "ruukkilabra:viimeisin"))),
           {k: (before["keys"].get(k), after["keys"].get(k)) for k in set(before["keys"]) | set(after["keys"]) if before["keys"].get(k) != after["keys"].get(k)})
    expect("the page said how much came back", "ratkaisua" in msg, msg)
    expect("the read-aloud setting did not travel", "ruukkilabra:readaloud:speed" not in after["keys"])
    # opening it again: nothing to add
    open_file(p, path); wait_status(p)
    expect("opening the same file again adds nothing", "ei ollut mitään uutta" in say(p), say(p))

    # conflicts: this browser's own differing data stays on Cancel, the file's wins on OK
    ctx.close()

    # a profile with different data: Cancel keeps its own, OK replaces
    for accept in (False, True):
        ctx = b.new_context(accept_downloads=True); p = ctx.new_page()
        seen = []
        p.on("dialog", lambda dlg, acc=accept: (seen.append(dlg.message), dlg.accept() if acc else dlg.dismiss()))
        p.goto(BASE + "tietosuoja.html"); p.wait_for_selector("#kaikki-tyo .palautus-btn", state="attached")
        p.evaluate("() => localStorage.setItem('ruukkilabra:kortit', JSON.stringify({ 'oma': { tila: 'uusi' } }))")
        open_file(p, path); wait_status(p)
        cards = p.evaluate("() => localStorage.getItem('ruukkilabra:kortit')")
        expect(f"a differing deck: one question; {'OK: the file wins' if accept else 'Cancel: this browser keeps its own'}",
               len(seen) == 1 and (json.loads(cards).get("fy3-voima") is not None if accept else json.loads(cards) == {"oma": {"tila": "uusi"}}), (seen, cards))
        ctx.close()

    # files that must change nothing
    cases = {}
    good = json.loads(path.read_text())
    cases["not JSON"] = "{{{"
    cases["a foreign JSON"] = json.dumps({"hello": 1})
    t = dict(good); t["content_sha256"] = "0" * 64; cases["wrong checksum"] = json.dumps(t)
    t = json.loads(path.read_text()); t["modules"]["FY3"]["store"]["solutions"][0]["html"] = "<p>muokattu</p>"; cases["edited content"] = json.dumps(t)
    t = json.loads(path.read_text()); t["version"] = 2; cases["newer version"] = json.dumps(t)
    t = json.loads(path.read_text()); t["site"]["ruukkilabra:salaisuus"] = "1"; cases["a key that is not allowed"] = json.dumps(t)
    t = json.loads(path.read_text()); t["modules"]["FY3"]["store"]["solutions"][0]["id"] = "fy4-1-L1-01"; cases["a record of another module under FY3"] = json.dumps(t)
    cases["a module work file"] = json.dumps({"format": "ruukkilabra-tyo", "version": 1, "course": "FY3"})
    cases["a chapter submission"] = json.dumps({"format": "ruukkilabra-palautus", "version": 3})
    msgs = {}
    for name, txt in cases.items():
        ctx, p = new_page(b, "tietosuoja.html")
        pre = p.evaluate("() => JSON.stringify(Object.keys(localStorage).sort())")
        f = TMP / "x.json"; f.write_text(txt); open_file(p, f)
        wait_status(p)
        post = p.evaluate("() => JSON.stringify(Object.keys(localStorage).sort())")
        msgs[name] = say(p)
        expect(f"refused, nothing changed: {name}", pre == post and p.evaluate("() => new Promise((ok) => { const r = indexedDB.open('ruukkilabra-ratkaisut'); r.onsuccess = () => ok(true); r.onerror = () => ok(true); })"), (pre, post, msgs[name]))
        ctx.close()
    expect("a module work file and a submission get their own message", "opintojakson työtiedosto" in msgs["a module work file"] and msgs["a module work file"] == msgs["a chapter submission"], msgs)
    expect("a broken file gets the broken-file message", all("ei ole Ruukkilabran työtiedosto" in msgs[k] for k in ("not JSON", "a foreign JSON", "wrong checksum", "edited content", "a key that is not allowed")), msgs)
    expect("a newer file gets the newer-version message", "uudemmalla versiolla" in msgs["newer version"], msgs["newer version"])

    # the module work file is unchanged by the refactor: a module page still saves one
    ctx = b.new_context(accept_downloads=True); p = ctx.new_page(); p.on("dialog", lambda dlg: dlg.accept())
    p.goto(BASE + "FY3.html"); p.wait_for_selector("#oma-tyo .palautus-btn", state="attached")
    p.evaluate(SEED)
    with p.expect_download() as dl:
        p.click("#oma-tyo .palautus-btn:first-child")
    w = json.loads(pathlib.Path(dl.value.path()).read_text())
    expect("module work file: still ruukkilabra-tyo v1 with the module's store only", w["format"] == "ruukkilabra-tyo" and w["version"] == 1 and w["course"] == "FY3"
           and [r["id"] for r in w["store"]["solutions"]] == ["fy3-4-L1-02"] and "site" not in w and "modules" not in w and not any("kortit" in k for k in w["store"]["local"]), list(w))
    ctx.close()
    b.close()

# the teacher's grading page: the backup is not a submission
gs = (ROOT / "palautus/apps-script/Code.gs").read_text()
expect("the grading page's validation names the backup and rejects it before the submission checks",
       "'ruukkilabra-kaikki'" in gs and gs.index("'ruukkilabra-kaikki'") < gs.index("data.format !== RL_FORMAT"))
node = subprocess.run(["node", "-e", r"""
const fs = require('fs'); const gs = fs.readFileSync(process.argv[1], 'utf8');
const m = /function rlError_\(([^)]*)\)\s*\{[\s\S]*?\n\}/.exec(gs);
let thrown = null;
try { eval(m[0] + '\n' + /function rlValidate_[\s\S]*?(?=\n  var v3)/.exec(gs)[0].replace(/^function rlValidate_\(text, deep, work\) \{/, 'function t(text, deep, work) { var RL_WORK_FORMAT = "ruukkilabra-tyo", RL_FORMAT = "x", RL_VERSION = 1; function rlValidateWork_(){ return "work"; }') + '\n}\n t(JSON.stringify({ format: "ruukkilabra-kaikki", version: 1 }), false);'); }
catch (e) { thrown = String(e.message || e); }
console.log(thrown);
""", str(ROOT / "palautus/apps-script/Code.gs")], capture_output=True, text=True)
expect("rlValidate_ throws the backup message for a ruukkilabra-kaikki file", "koko työn varmuuskopio" in node.stdout, node.stdout + node.stderr)

print(f"\n{fails} failure(s)" if fails else "\nall ok")
sys.exit(1 if fails else 0)
