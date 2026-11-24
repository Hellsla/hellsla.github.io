"""FY9-valmentaja, the hardest solution step and the repeated mistakes (work queue 11b PR 5; templates/valmentaja.js, docs/FY9_ADAPTIVE_PLAN.md 4.3, 6.2.3, 6.3).
Usage: python scripts/test_valmentaja_steps.py [site|preview]   (default: site, else preview)

On a FY9 unit page (fi, and the texts of en and fi-easy):
  - no row before a solution is open; opening a number task's solution or a long task's model answer adds one row "Mikä vaihe oli vaikein?" with
    nine chips from the fixed list (a button each, aria-pressed), the long task's before the points it gives
  - a chip pressed is kept in the key's steps ({task key: [step ids]}, the list's order), the log is untouched; pressed again it is gone, and the
    last one takes the steps field away; the keyboard (Tab, Space, Enter) works; a reload and the next opening show the state again
  - nothing to store (blocked storage, a damaged or newer log): no row, the page is as before, the log is not overwritten
  - the row sits inside the task's details, so the teacher's grading view (palautus_tasks.py) does not hold it
On the coach page: "Vaikeat vaiheet" shows only with a choice, the step's tasks as links; "Toistuvat virheet" only when the same option was hit
  twice or more, with the existing feedback; one hit shows nothing; Tyhjennä takes both away
Golden cases (window.flCoach.repeated, hardSteps): two hits of one option, one of another, a side-file group, rows of tasks the index does not know
Exit status 1 on any failure."""
import functools, http.server, json, pathlib, re, sys, tempfile, threading
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

args = sys.argv[1:]
SITE = ROOT / (args[0] if args and (ROOT / args[0]).is_dir() else ("site" if (ROOT / "site" / "FY9-valmentaja.html").is_file() else "preview"))
KEY = "ruukkilabra:fy9-valmentaja"
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


if not (SITE / "fy9-voimat.html").is_file() or not (SITE / "FY9-valmentaja.html").is_file():
    print("FAIL fy9-voimat.html or FY9-valmentaja.html is not built in", SITE); sys.exit(1)


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_port}/"
PAGE = BASE + "fy9-voimat.html?ratkaisut=1"
STORE = f"() => {{ const v = localStorage.getItem('{KEY}'); return v === null ? null : JSON.parse(v); }}"
OPEN = "(sel) => { const d = document.querySelector(sel); d.open = true; return !!d; }"
STEP_IDS = ["tulkinta", "annettu", "periaate", "kaava", "muunnokset", "sijoitus", "vastaus", "jarkevyys", "kuvaaja"]

# the texts: every language has the same keys, the step names are the solution's own
for lang in ("fi", "en", "fi-easy"):
    c = json.loads((ROOT / "lang" / f"{lang}.json").read_text(encoding="utf-8"))["coach"]
    expect(f"{lang}: the new texts are there", all(c.get(k) for k in ("hard_q", "step_tulkinta", "steps_h", "mistakes_h", "mistakes_n")) and "{n}" in c["mistakes_n"])
for lang, prefix in (("en", "en/"), ("fi-easy", "fi-easy/")):
    h = (SITE / prefix / "fy9-voimat.html").read_text() if (SITE / prefix / "fy9-voimat.html").is_file() else ""
    expect(f"{lang}: the unit page carries the row's texts", not h or bool(re.search(r'<script src="valmentaja.js" data-t="[^"]*hard|<script src="valmentaja.js" data-t="[^"]*steps', h)) or "&quot;q&quot;" in h)
src = (SITE / "valmentaja.js").read_text()
code = re.sub(r"//.*", "", re.sub(r"/\*.*?\*/", "", src, flags=re.S))
expect("still no network call", not [w for w in ("fetch", "XMLHttpRequest", "sendBeacon", "WebSocket", "EventSource", "importScripts", "new Image") if w in code])

with sync_playwright() as p:
    b = launch(p)
    ctx = b.new_context(viewport={"width": 1280, "height": 900})
    pg = ctx.new_page(); errors = []; pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(PAGE)
    expect("before a solution is opened the page has no row", pg.locator(".hardstep").count() == 0)
    pg.evaluate(OPEN, '[id="nosturi"] details.solution'); pg.wait_for_timeout(100)
    expect("opening a number task's solution adds one row with the question", pg.locator('[id="nosturi"] .hardstep').count() == 1 and pg.locator('[id="nosturi"] .hardstep-q').inner_text() == "Mikä vaihe oli vaikein?")
    chips = pg.locator('[id="nosturi"] .hardstep-chip')
    expect("nine chips from the fixed list, none pressed, in the solution's own words", chips.count() == 9 and [chips.nth(i).get_attribute("data-step") for i in range(9)] == STEP_IDS
           and all(chips.nth(i).get_attribute("aria-pressed") == "false" for i in range(9)) and chips.nth(5).inner_text() == "Sijoitus" and chips.nth(0).inner_text() == "Tehtävän tulkinta", chips.all_inner_texts())
    expect("the row is inside the solution box, after its steps", pg.evaluate("(() => { const r = document.querySelector('[id=\"nosturi\"] .hardstep'); return r.parentElement.matches('details.solution') && !!r.previousElementSibling; })()"))
    expect("an open solution alone writes nothing", pg.evaluate(STORE) is None)
    chips.nth(5).click()
    expect("a chip pressed: pressed, and kept in steps (the log untouched)", chips.nth(5).get_attribute("aria-pressed") == "true" and pg.evaluate(STORE) == {"v": 1, "log": [], "steps": {"fy9-voimat#nosturi": ["sijoitus"]}}, pg.evaluate(STORE))
    chips.nth(2).focus(); pg.keyboard.press("Space")
    chips.nth(8).focus(); pg.keyboard.press("Enter")
    expect("the keyboard works (Space, Enter); the steps are in the list's order", pg.evaluate(STORE)["steps"] == {"fy9-voimat#nosturi": ["periaate", "sijoitus", "kuvaaja"]}, pg.evaluate(STORE))
    pg.keyboard.press("Tab")
    expect("every chip is a real button reached by Tab and 40 px or more", all(chips.nth(i).evaluate("e => e.tagName === 'BUTTON' && e.tabIndex === 0 && e.getBoundingClientRect().height >= 40") for i in range(9)))
    pg.reload(); pg.evaluate(OPEN, '[id="nosturi"] details.solution'); pg.wait_for_timeout(100)
    chips = pg.locator('[id="nosturi"] .hardstep-chip')
    expect("after a reload the opened solution shows the same chips pressed", [chips.nth(i).get_attribute("aria-pressed") for i in range(9)] == ["false", "false", "true", "false", "false", "true", "false", "false", "true"])
    for i in (2, 5, 8): chips.nth(i).click()
    expect("pressed again, a chip is taken back; with none left the steps field goes", pg.evaluate(STORE) == {"v": 1, "log": []}, pg.evaluate(STORE))
    # a long task: before the points it gives
    pg.evaluate("(() => { for (let d = document.querySelector('.rubric[data-id=\"fy9-voimat-s1\"]').closest('details'); d; d = d.parentElement.closest('details')) d.open = true; })()"); pg.wait_for_timeout(100)
    expect("a long task's model answer has the row before its points", pg.evaluate("(() => { const r = document.querySelector('#fy9-voimat-s1 .hardstep'); return !!r && r.nextElementSibling && r.nextElementSibling.matches('.rubric'); })()"))
    pg.locator("#fy9-voimat-s1 .hardstep-chip").nth(3).click()
    expect("its choice is kept under its own key", pg.evaluate(STORE)["steps"] == {"fy9-voimat-s1": ["kaava"]}, pg.evaluate(STORE))
    pg.evaluate("document.querySelector('[id=\"nosturi\"] form.check input').value = '1'; document.querySelector('[id=\"nosturi\"] form.check button').click()"); pg.wait_for_timeout(100)
    d = pg.evaluate(STORE)
    expect("an attempt next to it adds its row and keeps the steps", d["steps"] == {"fy9-voimat-s1": ["kaava"]} and len(d["log"]) == 1, d)
    expect("no script error", not errors, errors)
    # the teacher's view takes every details out of a task
    expect("the row is in a details, which the grading view strips (palautus_tasks.py EXTRACT)", "details" in (ROOT / "scripts" / "palautus_tasks.py").read_text().split("const strip")[1][:200])
    # no storage, damaged, newer
    ctx3 = b.new_context(); ctx3.add_init_script("Storage.prototype.setItem = function () { throw new Error('QuotaExceededError'); }; Storage.prototype.getItem = function () { throw new Error('blocked'); };")
    t = ctx3.new_page(); e3 = []; t.on("pageerror", lambda e: e3.append(str(e))); t.goto(PAGE); t.evaluate(OPEN, '[id="nosturi"] details.solution'); t.wait_for_timeout(100)
    expect("blocked storage: no row, no error", t.locator(".hardstep").count() == 0 and not e3, e3)
    ctx3.close()
    for bad in ("{not json", json.dumps({"v": 2, "log": [], "x": 1})):
        c4 = b.new_context(); t = c4.new_page(); t.goto(PAGE); t.evaluate(f"localStorage.setItem('{KEY}', {json.dumps(bad)})")
        t.evaluate(OPEN, '[id="nosturi"] details.solution'); t.wait_for_timeout(100)
        expect(f"a log that cannot be read ({bad[:8]}…): no row, the log stays as it is", t.locator(".hardstep").count() == 0 and t.evaluate(f"localStorage.getItem('{KEY}')") == bad)
        c4.close()
    # the coach page
    CP = BASE + "FY9-valmentaja.html"
    c5 = b.new_context(viewport={"width": 1280, "height": 900}); t = c5.new_page(); e5 = []; t.on("pageerror", lambda e: e5.append(str(e))); t.goto(CP)
    expect("with no data neither box shows", t.locator("#coach-steps").is_hidden() and t.locator("#coach-mistakes").is_hidden())
    index = t.evaluate("JSON.parse(document.getElementById('fy9-index').textContent)")
    ids = {x["id"] for x in index["tasks"]}
    tid = "fy9-voimat#nosturi"
    expect("the index has the task and the page the feedback of its mistakes", tid in ids and t.evaluate("JSON.parse(document.getElementById('fy9-mistakes').textContent)['fy9-voimat#nosturi'].length") == 3)
    row = lambda i, m: ["2026-11-20T18:0%dZ" % i, tid, "a", "no", 1 if i == 0 else 0, 0, m, "p"]
    t.evaluate(f"localStorage.setItem('{KEY}', JSON.stringify({{ v: 1, log: {json.dumps([row(0, 1)])}, steps: {{ '{tid}': ['sijoitus', 'jarkevyys'], 'fy9-voimat-s1': ['kaava'], 'gone#x': ['kaava'] }} }}))"); t.reload()
    t.locator("#coach-steps summary").click()
    expect("hard steps show, grouped by step in the list's order, each task a link; a task the index does not know is left out",
           t.locator("#coach-steps").is_visible() and t.locator("#coach-steps .coach-steplist li").count() == 3 and t.locator("#coach-steps li").first.inner_text().startswith("Kaava")
           and t.locator("#coach-steps li a").count() == 3 and "#nosturi" in t.locator("#coach-steps li a").nth(1).get_attribute("href"), t.locator("#coach-steps").inner_text())
    expect("one hit of a mistake shows no repeated-mistakes box", t.locator("#coach-mistakes").is_hidden())
    t.evaluate(f"(() => {{ const d = JSON.parse(localStorage.getItem('{KEY}')); d.log.push({json.dumps(row(1, 1))}, {json.dumps(row(2, 2))}); localStorage.setItem('{KEY}', JSON.stringify(d)); }})()"); t.reload()
    t.locator("#coach-mistakes summary").click()
    expect("the same option twice: the box shows, once, with the task's link and the number of hits", t.locator("#coach-mistakes").is_visible() and t.locator("#coach-mistakes .coach-misslist li").count() == 1
           and "2" in t.locator("#coach-mistakes .coach-min").inner_text(), t.locator("#coach-mistakes").inner_text())
    fb = t.evaluate("JSON.parse(document.getElementById('fy9-mistakes').textContent)['fy9-voimat#nosturi'][1]")
    expect("its text is the existing feedback of that option", t.locator("#coach-mistakes .coach-feedback").inner_text().replace("\n", " ").startswith(fb[:20].replace("*", "")), (fb, t.locator("#coach-mistakes").inner_text()))
    for w in (360, 1280):
        t.set_viewport_size({"width": w, "height": 900})
        expect(f"at {w} px the boxes do not overflow and the links are 40 px or more", t.evaluate("document.documentElement.scrollWidth <= window.innerWidth") and t.evaluate("[...document.querySelectorAll('#coach-steps a, #coach-mistakes a')].every(a => a.getBoundingClientRect().height >= 40)"))
    t.once("dialog", lambda dlg: dlg.accept()); t.locator(".coach-clear").click(); t.wait_for_timeout(300)
    expect("Tyhjennä removes the steps with the log", t.evaluate(STORE) is None and t.locator("#coach-steps").is_hidden() and t.locator("#coach-mistakes").is_hidden())
    expect("no script error on the coach page", not e5, e5)
    # golden cases of the pure functions
    g = t.evaluate("""() => {
      const idx = { tasks: [{ id: 'u#a' }, { id: 'u#b' }, { id: 'u#c' }], misconceptions: { dir: { items: ['u#b/0', 'u#c/1'] } } };
      const r = (task, m) => ['2026-11-20T18:00Z', task, 'a', 'no', 0, 0, m, 'p'];
      const log = [r('u#a', 0), r('u#a', 0), r('u#a', 1), r('u#b', 0), r('u#c', 1), r('u#zz', 0), r('u#zz', 0), r('u#a', null)];
      return { rep: window.flCoach.repeated(log, idx).map((h) => [h.task, h.mistake, h.n]),
               hs: window.flCoach.hardSteps({ steps: { 'u#a': ['kaava', 'sijoitus'], 'u#b': ['kaava'], 'zz': ['kaava'] } }, idx) };
    }""")
    expect("golden: same option twice counts, a grouped pair counts together (a tie: the latest hit first), an unknown task and a null do not", g["rep"] == [["u#c", 1, 2], ["u#a", 0, 2]], g["rep"])
    expect("golden: hard steps by step, known tasks only", g["hs"] == [["kaava", ["u#a", "u#b"]], ["sijoitus", ["u#a"]]], g["hs"])
    c5.close(); b.close()
print("FAILED" if fails else "all ok")
sys.exit(1 if fails else 0)
