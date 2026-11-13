"""Tests of the inquiry framework (scripts/inquiry.py, templates/inquiry.js, the sim adapter).
Usage: python scripts/test_inquiry.py            the framework suite on the fy3-2 pilot (below)
       python scripts/test_inquiry.py <id>       generic checks of one lesson (check_lesson.py and CI run it for every
                                                 lesson with inquiry.json): validation, build, stage order and the page
                                                 navigation, every option's correct flag and feedback as rendered,
                                                 plain choices answer right and wrong, predictions commit without
                                                 feedback and are revealed by their experiment, every experiment runs
                                                 on the adapter (its parameters and measured keys exist, initial state
                                                 set, controlled parameters locked, two measurements, reset), forms
                                                 present, no console errors, 360 px fit, and the page form of
                                                 2026-10-26 (page_form): stage and section names, the Ennusta box
                                                 closed at first and keeping its answers, the exercises last, the sim's
                                                 controls in view and its explanations behind closed boxes, and the
                                                 wide layout at 1280 and 1920 px (sim beside the experiments, figures
                                                 beside their text, text no wider than a reading column)

Part 1 (no browser): validation names the lesson and the field; a lesson without inquiry.json builds exactly as
before; every activity type renders. Part 2 (Playwright, on preview/fy3-2.html built here): stage order and nav,
a prediction stays unrevealed until the linked experiment has enough measurements, the experiment sets the
initial conditions, locks the controlled parameters, records the varied parameter and the measurements, and
reset clears everything, numeric answers with a decimal comma, invalid input, a common mistake and retries,
progressive hints, the model answer, the reflection shows the stored prediction, keyboard operation, and a
360 px viewport without horizontal overflow. The physics itself (W = F s, P = W / t) is asserted by
tests/sims/fy3-2.json through test_sims.py, not here. What these tests prove is that the mechanics behave;
whether the sequence teaches is for the classroom evaluation (docs/inquiry.md)."""
import copy, html as _h, json, os, pathlib, re, subprocess, sys, tempfile, shutil
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import inquiry
ROOT = pathlib.Path(__file__).resolve().parents[1]
LROOT = pathlib.Path(os.environ.get("FYSIIKKALABRA_ROOT") or ROOT)   # where the lesson of a generic run lives (tests use a copy)
PY = sys.executable
passed = failed = 0


def check(name, cond, detail=""):
    global passed, failed
    passed += cond; failed += not cond
    print(("ok   " if cond else "FAIL ") + name + (f"  {detail}" if detail and not cond else ""))


def _letters(s, n=40):
    """The first n letters of a text with markup, maths and punctuation removed: enough to tell two options apart."""
    s = re.sub(r"<[^>]+>", " ", re.sub(r"\$[^$]*\$", " ", _h.unescape(s)))   # maths first: "$W < 0$" is not a tag
    return "".join(ch for ch in s.lower() if ch.isalpha())[:n]


def choice_items(acts):
    """(activity id, radio name = shuffle seed, choice spec) for every choice on the page, questions of experiments and interpret items included."""
    out = []
    for a in acts:
        if a["type"] == "choice": out.append((a["id"], a["id"], a))
        q = a.get("question")
        if a["type"] in ("experiment", "interpret") and isinstance(q, dict) and q.get("type") == "choice": out.append((a["id"], f"{a['id']}-q", q))
    return out


SETTLE = "(ks) => { const S = (window.simAdapter && window.simAdapter.get()) || {}; return ks.every(k => S[k] !== undefined && S[k] !== null); }"
FASTEST = """() => { const own = new Set(Object.values(window.simAdapter.params).map((p) => typeof p.input === 'string' ? document.querySelector(p.input) : p.input));
  [...document.querySelectorAll('#sim-root label')].filter((l) => /^\\s*Nopeus/.test(l.textContent)).map((l) => l.querySelector('select')).forEach((s) => {
    const i = s ? [...s.options].findIndex((o) => /nopea/i.test(o.text)) : -1;     // the speed control (NOTES 4), never a physics parameter
    if (i >= 0 && !own.has(s) && !s.disabled) { s.selectedIndex = i; s.dispatchEvent(new Event('input', {bubbles: true})); s.dispatchEvent(new Event('change', {bubbles: true})); } }); }"""
RUN = """() => { const b = document.querySelector('#sim-root button');   // the sim's main button comes first (NOTES 4)
  const label = b ? b.textContent.trim() : '', free = b && !b.disabled && !/…$/.test(label);
  if ((window.simState || {}).running === true) {
    // a run in progress is left alone when the same button pauses it (fy4-14: the 40 s jump was paused every other wait and
    // did not finish on a busy machine, 2026-11-11). A button that now names the run's next step is pressed once, as the
    // experiment's intro tells the student (fy5-3: Käynnistä, then Katkaise naru; without it α and v_irti never come, 2026-11-12).
    if (!free || /^(Tauko|Pysäytä|Pause|Stop)$/.test(label) || label === window.__flRunStart || label === window.__flRunStep) return null;
    window.__flRunStep = label; b.click(); return label;
  }
  if (free) { window.__flRunStart = label; window.__flRunStep = null; b.click(); return label; } return null; }"""
RUN_STUB = """<div id="sim-root"><button id="b">Käynnistä</button></div>
<script>window.simState = { running: false }; window.clicks = 0;
document.getElementById('b').addEventListener('click', () => { window.clicks++; window.simState.running = !window.simState.running; });</script>"""
RUN_STUB_PAUSE = """<div id="sim-root"><button id="b">Käynnistä</button></div>
<script>window.simState = { running: false }; window.clicks = 0; const b = document.getElementById('b');
b.addEventListener('click', () => { window.clicks++; window.simState.running = !window.simState.running; b.textContent = window.simState.running ? 'Tauko' : 'Jatka'; });</script>"""
RUN_STUB_STEP = """<div id="sim-root"><button id="b">Käynnistä</button></div>
<script>window.simState = { running: false, released: false }; window.clicks = 0; const b = document.getElementById('b');
b.addEventListener('click', () => { window.clicks++;
  if (!window.simState.running) { window.simState = { running: true, released: false }; b.textContent = 'Katkaise naru'; }
  else window.simState.released = true; });</script>"""


def run_helper_selftest(browser):
    """The helper that presses a sim's main button for the student: it starts a sim that stands still, never presses
    the button of one that reports simState.running when that button would stop or pause it, and presses once a
    button that names the run's next step (fy5-3: Katkaise naru)."""
    q = browser.new_page(); q.set_content(RUN_STUB)
    first = q.evaluate(RUN); second = q.evaluate(RUN); third = q.evaluate(RUN)
    state = q.evaluate("[window.clicks, window.simState.running]")
    check("the run helper starts a sim once and leaves a running sim alone", first == "Käynnistä" and second is None and third is None and state == [1, True], f"{first!r} {second!r} {third!r} {state}")
    q.close(); q = browser.new_page(); q.set_content(RUN_STUB_PAUSE)   # a page of its own: set_content keeps the window and its globals
    first = q.evaluate(RUN); second = q.evaluate(RUN); third = q.evaluate(RUN)
    state = q.evaluate("[window.clicks, window.simState.running]")
    check("the run helper never presses a running sim's pause button", first == "Käynnistä" and second is None and third is None and state == [1, True], f"{first!r} {second!r} {third!r} {state}")
    q.close(); q = browser.new_page(); q.set_content(RUN_STUB_STEP)
    first = q.evaluate(RUN); second = q.evaluate(RUN); third = q.evaluate(RUN)
    state = q.evaluate("[window.clicks, window.simState.running, window.simState.released]"); q.close()
    check("the run helper presses a running sim's next-step button once", first == "Käynnistä" and second == "Katkaise naru" and third is None and state == [2, True, True], f"{first!r} {second!r} {third!r} {state}")
CONTROL = "(k) => { const p = window.simAdapter.params[k]; return typeof p.input === 'string' ? document.querySelector(p.input) : p.input; }"
OLD_NAMES = ("Herätä kiinnostus", "Lähtölippu", "Selitä", "Teoriatiivistelmä", "Theory summary", "Exit ticket", "Tarkista osaamisesi")     # replaced by Pohdinta, Exit ticket, Teoriatiivistelmä (2026-10-26), then Teoria (2026-11-05), Pohdintatehtävä and Itsearvio (2026-11-06)
SPLIT = """async () => {   // lesson.js part 9: the exercises beside the theory, opened by the button, closed again (teacher 2026-11-05)
  const ex = document.getElementById('exercises'), b = ex && ex.querySelector('.split-toggle');
  if (!ex) return { none: true };
  if (!b || !b.offsetParent) return { button: false };
  const wait = () => new Promise((r) => setTimeout(r, 300));
  const before = getComputedStyle(ex).position;
  b.click(); await wait();
  const r = ex.getBoundingClientRect(), m = document.querySelector('main').getBoundingClientRect();
  const open = { position: getComputedStyle(ex).position, right: Math.round(window.innerWidth - r.right), beside: m.right <= r.left + 1,
                 scrolls: getComputedStyle(ex).overflowY, over: document.documentElement.scrollWidth - document.documentElement.clientWidth };
  b.click(); await wait();
  return { button: true, before, open, after: getComputedStyle(ex).position };
}"""
NAMES = """() => [...document.querySelectorAll('nav.toc a, main h2, main h3, main summary')].map((e) => e.textContent.replace(/^\\d+/, '').trim())"""
WIDE = """() => {      // the wide layout as rendered: which blocks sit side by side, and the widest paragraph
  const R = (e) => e.getBoundingClientRect(), beside = (a, b) => R(b).left >= R(a).right - 1 && Math.abs(R(a).top - R(b).top) < 400;
  const lab = document.querySelector('.lab'), rows = [...document.querySelectorAll('.act-theory > .fig-row, article#teoria > .fig-row')];
  const text = [...document.querySelectorAll('main p, main li')].filter((e) => e.offsetParent && !e.closest('#sim-root, .katex-display, table'));
  const cells = [...document.querySelectorAll('.lab > *, .fig-row > *, .intro-row > *')].filter((e) => e.scrollWidth > e.clientWidth + 1).map((e) => e.className);
  return { over: document.documentElement.scrollWidth - document.documentElement.clientWidth,
           lab: lab ? beside(lab.querySelector('.lab-main'), lab.querySelector('.lab-side')) : null,
           figs: rows.map((r) => beside(r.querySelector('.fig-text'), r.querySelector('.fig')) === r.classList.contains('side')),
           sides: rows.map((r) => r.classList.contains('side')), widest: Math.max(0, ...text.map((e) => R(e).width)), rem: parseFloat(getComputedStyle(document.documentElement).fontSize), cells };
}"""



def list_tasks(pg, url):
    """The exercises answered as a list (teacher 2026-11-05, inquiry.js 2b–2c): true-or-false statements and order tasks.
    Every item wrong: the wrong ones are marked and one change is offered; wrong again: every right answer is shown and the
    task locks. Reloaded and answered right: "Oikein", every item marked right."""
    sets = pg.locator("fieldset.tf, fieldset.order")
    if not sets.count(): return
    pg.evaluate("document.querySelectorAll('#exercises details').forEach((d) => { d.open = true; })")
    js_wrong = """(fs) => { const tf = fs.classList.contains('tf');
        fs.querySelectorAll(tf ? '.tf-list > li' : '.order-list > li').forEach((li, j, all) => {
          if (tf) li.querySelector(`input[value="${li.dataset.true === '1' ? '0' : '1'}"]`).checked = true;
          else li.querySelector('select').value = String(((Number(li.dataset.rank)) % all.length) + 1); }); }"""
    js_right = """(fs) => { const tf = fs.classList.contains('tf');
        fs.querySelectorAll(tf ? '.tf-list > li' : '.order-list > li').forEach((li) => {
          if (tf) li.querySelector(`input[value="${li.dataset.true}"]`).checked = true; else li.querySelector('select').value = li.dataset.rank; }); }"""
    ids = [x.get_attribute("data-id") for x in sets.all()]
    for i in ids:
        fs = pg.locator(f'fieldset[data-id="{i}"]'); rows = fs.locator("ol.tf-list > li, ul.order-list > li"); n = rows.count()
        fs.locator("button.commit").click()
        check(f"{i}: Vastaa asks for every item first", fs.locator("output").get_attribute("data-state") == "hint")
        fs.evaluate(js_wrong); fs.locator("button.commit").click()
        marked = fs.locator('li[data-state="no"]').count()
        check(f"{i}: the first wrong answer marks the wrong items and offers one change", marked == n and f"{n}/{n}" in fs.locator("output").inner_text() and fs.locator("button.commit").is_visible(), f"{marked}/{n}")
        fs.locator("button.commit").click()
        shown = fs.locator(".feedback:visible, .ord-right:visible").count()
        check(f"{i}: the second wrong answer shows every right answer and locks", shown == n and not fs.locator("button.commit").is_visible(), f"{shown}/{n} shown")
    q = pg.context.browser.new_page(viewport={"width": 1280, "height": 900}); q.goto(url); q.wait_for_timeout(300)   # a fresh page: the run's own page keeps its open boxes
    q.evaluate("document.querySelectorAll('#exercises details').forEach((d) => { d.open = true; })")
    for i in ids:
        fs = q.locator(f'fieldset[data-id="{i}"]'); n = fs.locator("ol.tf-list > li, ul.order-list > li").count()
        fs.evaluate(js_right); fs.locator("button.commit").click()
        check(f"{i}: the right answers are marked right", fs.locator("output").get_attribute("data-state") == "ok" and fs.locator('li[data-state="ok"]').count() == n)
    q.close()

def page_form(pg, b, url, acts, page):
    """The lesson page form of 2026-10-26 (CLAUDE.md "Lesson page"), checked on the rendered page. pg is a 1280 px page."""
    names = pg.evaluate(NAMES)
    old = [n for n in names if any(n == o or n.startswith(o + " ") for o in OLD_NAMES)]
    check("no old stage or section names in the nav or headings (Pohdinta, Teoria, Exit ticket)", not old, str(old))
    check("the old stage names of the texts are shown as Teoria / Theory (inquiry.current_stage_names)",
          not pg.evaluate("/Teoriatiivistelm|Theory summary/i.test(document.querySelector('main').textContent)"))
    sp = pg.evaluate(SPLIT)
    check("1280 px: 'Avaa tehtävät teorian viereen' puts the exercises in a panel on the right that scrolls on its own, beside the lesson, and closes back",
          sp.get("none") or (sp.get("button") and sp["before"] == "static" and sp["open"]["position"] == "fixed" and sp["open"]["right"] == 0
                             and sp["open"]["beside"] and sp["open"]["scrolls"] == "auto" and sp["open"]["over"] <= 0 and sp["after"] == "static"), str(sp))
    toc = pg.evaluate("[...document.querySelectorAll('nav.toc a')].map((a) => { const l = (a.querySelector('.toc-label') || a).cloneNode(true); l.querySelectorAll('.toc-rest').forEach((e) => e.remove()); return l.textContent; })")   # the short name; the side column adds the rest of a long title
    want = []
    for sid, t in inquiry.STAGES:
        here = [a for a in acts if a["stage"] == sid and a["type"] != "exercises"]
        if here: want += [inquiry.NAV.get(sid, t)]          # the exit ticket has no link of its own: it opens Tarkista osaamisesi (teacher 2026-11-04)
    if inquiry.NAV.get("tarkista", "") in want: want.remove(inquiry.NAV.get("tarkista")); want += [inquiry.EXERCISES_TITLE, inquiry.NAV.get("tarkista")]   # Itsearvio after the exercises (teacher 2026-11-06 evening)
    else: want.append(inquiry.EXERCISES_TITLE)
    check("nav names the stages and the exercises (no link of their own for the exit ticket or the concept cards)", toc == want, f"{toc} != {want}")
    check("the concept cards close Esimerkit (teacher 2026-11-05)", pg.evaluate("(() => { const k = document.getElementById('kertaa-kasitteet'); if (!k) return true; const s = k.closest('section.stage'); const box = k.closest('details.kc-fold'); return !!s && (s.id === 'sovella' || !document.getElementById('sovella')) && !!box && s.lastElementChild === box && !box.hasAttribute('open'); })()"))
    check("Palaa ennusteisiisi is a closed box, required or not (teacher 2026-11-06)", pg.evaluate("[...document.querySelectorAll('.act-reflect')].every((r) => { const d = r.closest('details'); return d && !d.hasAttribute('open'); })"))
    check("the exit ticket opens Testaa ja arvioi, and the goals' card closes it (teacher 2026-11-10: tasks first; the goals first until then)", pg.evaluate("(() => { const x = document.getElementById('exit'); if (!x) return true; const a = x.closest('.activity'), s = x.closest('#tarkista'); const g = s && s.querySelector('.act-selfgoals'), acts = s ? [...s.querySelectorAll(':scope > .activity, :scope > * > .activity')] : []; return !!s && s.querySelector('.activity') === a && (!g || acts[acts.length - 1] === g); })()"))
    order = pg.evaluate("[...document.querySelectorAll('article > section, article > .intro')].map((e) => e.id || e.className)")
    order = [o for o in order if o != "credits"]          # the photo credits (build.photo_credits) follow as the page's colophon
    check("Itsearvio closes the page, after the exercises (teacher 2026-11-06 evening)", order[-1:] == (["tarkista"] if "tarkista" in order else ["exercises"]) and order.index("exercises") == len(order) - 1 - ("tarkista" in order)
          and pg.evaluate("(() => { const x = document.getElementById('exit'), e = document.getElementById('exercises'); return !x || !!(e.compareDocumentPosition(x) & 4); })()"), str(order))
    if any(a["stage"] == "ennusta" for a in acts):
        fold = pg.locator("#ennusta details.fold")
        check("Ennusta sits in a box that starts closed", fold.count() == 1 and not fold.evaluate("(d) => d.open") and pg.locator("#ennusta .fold-body").is_hidden())
    sim_act = next((a for a in acts if a["type"] == "sim"), None)
    if sim_act:
        hidden = pg.evaluate("[...document.querySelectorAll('#sim-root canvas, #sim-root input, #sim-root select, #sim-root button')].filter((e) => e.closest('details:not([open])')).length")
        check("the simulation's picture and controls are never behind a closed box", hidden == 0, f"{hidden} hidden")
        boxes = pg.evaluate("[...document.querySelectorAll('#sim details')].map((d) => [d.querySelector('summary').textContent.trim(), d.open])")
        check("the simulation's explanations sit behind closed, named boxes", all(t and not o for t, o in boxes), str(boxes))
        words = pg.evaluate("""() => { const a = document.querySelector('.act-sim'); if (!a) return 0; const c = a.cloneNode(true);
          c.querySelectorAll('label, .readout, .controls, button, select, summary, table, canvas, script, h3, details:not([open]) > :not(summary), .sim-moved, .sim-context').forEach((e) => e.remove());
          return c.textContent.trim().split(/\\s+/).filter(Boolean).length; }""")
        check("the simulation shows little text: picture, controls and values first", words <= 50, f"{words} visible words beside the controls and the readout")
    for w in (1280, 1920):
        q = b.new_page(viewport={"width": w, "height": 900}); q.goto(url); q.wait_for_timeout(500)
        L = q.evaluate(WIDE)
        check(f"{w} px: no horizontal overflow, no column spilling into its neighbour", L["over"] <= 0 and not L["cells"], str(L))
        check(f"{w} px: text no wider than a reading column (44rem)", L["widest"] <= 44 * L["rem"] + 1, f"{L['widest']:.0f} px")
        if L["lab"] is not None: check(f"{w} px: the simulation beside the experiments", L["lab"])
        if L["figs"]: check(f"{w} px: a theory figure beside its paragraph when the two are about as tall (.side), under it otherwise", all(L["figs"]), str(L["figs"]))
        q.close()
    q = b.new_page(viewport={"width": 360, "height": 740}); q.goto(url); q.wait_for_timeout(500)
    L = q.evaluate(WIDE)
    check("360 px: one column", not L["lab"] and not any(L["figs"][i] and side for i, side in enumerate(L["sides"])), str(L))
    q.close()



def restore_checks(pg, url, lid, ex, loc, want):
    """The table of an earlier visit (2026-11-05): another tab of the same page shows the same rows, typeset, and does not
    write the unchanged table back to localStorage."""
    eid = ex["id"]
    store = pg.evaluate("() => { const o = {}; try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); o[k] = localStorage.getItem(k); } } catch (e) {} return o; }")
    q = pg.context.browser.new_page(viewport={"width": 1280, "height": 900})   # a later visit on the same device: the same localStorage
    q.add_init_script("((s) => { try { localStorage.clear(); for (const k in s) localStorage.setItem(k, s[k]); } catch (e) {} window.__flWrites = []; const set = Storage.prototype.setItem;"
                      " Storage.prototype.setItem = function (k, v) { window.__flWrites.push(k); return set.call(this, k, v); }; })(" + json.dumps(store) + ")")
    q.goto(url)
    try: q.wait_for_function("window.simAdapter", timeout=4000)
    except Exception: pass
    q.wait_for_timeout(300)
    qloc = q.locator(f"#{eid}")
    got = qloc.locator(".exp-table tbody tr").all_text_contents()
    n = q.evaluate("(id) => [...document.querySelectorAll('.experiment')].indexOf(document.querySelector('#' + id + ' .experiment')) + 1", eid)
    writes = q.evaluate(f"window.__flWrites.filter((k) => k === 'ruukkilabra:{lid}:koe{n}').length")
    check(f"{eid}: the stored measurements come back on a new visit, the same rows", got == want, f"{got} != {want}")
    check(f"{eid}: a restored table is not written back to localStorage", writes == 0, f"{writes} writes")
    check(f"{eid}: Kopioi taulukko is on for a restored table", qloc.locator(".exp-copy").is_enabled())
    # the icon buttons (teacher 2026-11-13): found by their aria-label, 40 px square at least, all four buttons on one row
    for cls in ("exp-reset", "exp-copy"):
        b = qloc.locator("." + cls); box = b.bounding_box()
        check(f"{eid}: .{cls} is an icon button with aria-label, title and an svg, at least 40x40",
              bool(b.get_attribute("aria-label")) and b.get_attribute("title") == b.get_attribute("aria-label") and b.locator("svg").count() == 1
              and box and box["width"] >= 39.5 and box["height"] >= 39.5, str(box))
    tops = qloc.locator(".exp-controls button").evaluate_all("(bs) => bs.map((b) => Math.round(b.getBoundingClientRect().top))")
    check(f"{eid}: the four buttons share one row at 1280 px", len(set(tops)) == 1, str(tops))
    check(f"{eid}: Alkutila, Vakiona and Muutetaan are three rows of their own", qloc.locator(".exp-setup > div").count() == 3)
    cap = qloc.locator(".exp-table caption").evaluate("(c) => c.getBoundingClientRect().height")
    check(f"{eid}: the table's caption stays on one row at 1280 px (teacher 2026-11-13)", cap < 36, str(cap))
    q.wait_for_timeout(1500)   # inquiry.js promote() runs at 300 and 1500 ms
    stray = q.evaluate("() => [...document.querySelectorAll('#tutki details.opt')].filter((d) => !d.closest('details.more')).length")
    in_more = q.evaluate("() => document.querySelectorAll('#tutki details.more details.opt').length")
    check(f"{eid}: an optional investigation never leaves Lisää tutkittavaa ({in_more} inside, {stray} outside)", stray == 0 or not in_more, str(stray))
    q.close()


def export_checks(pg, lid, ex, loc):
    """The table's export after two measurements (teacher 2026-11-03; Lataa CSV dropped 2026-11-04): the copy button on, the rows kept in localStorage as
    ruukkilabra:<page>:koe<n>, plain headings (th[data-plain]), numbers with a decimal comma, the copy
    either on the clipboard ("Kopioitu") or shown in a text field to select."""
    eid = ex["id"]
    check(f"{eid}: export button enabled with measurements", loc.locator(".exp-copy").is_enabled() and not loc.locator(".exp-csv").count())
    n = pg.evaluate("(id) => [...document.querySelectorAll('.experiment')].indexOf(document.querySelector('#' + id + ' .experiment')) + 1", eid)
    stored = pg.evaluate(f"() => {{ try {{ return JSON.parse(localStorage.getItem('ruukkilabra:{lid}:koe{n}')) }} catch (e) {{ return null }} }}")
    check(f"{eid}: measurements stored as ruukkilabra:{lid}:koe{n}", bool(stored) and len(stored.get("rows", [])) == 2, str(stored)[:200])
    heads = loc.locator(".exp-table thead th").evaluate_all("(ts) => ts.map((t) => t.dataset.plain)")
    check(f"{eid}: every heading has a plain form without LaTeX", all(h and not re.search(r"[$\\{}_^]", h) for h in heads), str(heads))
    vals = loc.locator(".exp-table tbody td[data-value]").evaluate_all("(ts) => ts.map((t) => t.dataset.value)")
    check(f"{eid}: exported numbers with a decimal comma", all("." not in v for v in vals if re.fullmatch(r"-?[\\d.,]+", v)), str(vals[:8]))
    loc.locator(".exp-copy").click(); pg.wait_for_timeout(200)
    said = loc.locator(".exp-export-status").inner_text(); field = loc.locator(".exp-export-text")
    shown = field.count() and field.is_visible() and field.input_value().split("\n")[0] == "\t".join(heads)
    check(f"{eid}: Kopioi taulukko copies (or shows the table to select)", said.strip() in ("Kopioitu", "Copied") or shown, said)


def generic(lid):
    """Mechanics of one lesson's inquiry.json on its preview page. Exit 1 on any failure."""
    from playwright.sync_api import sync_playwright
    from _browser import launch
    from reviews import find_lesson
    folder = find_lesson(lid)
    data = inquiry.load(folder)
    if data is None: print(f"{lid}: no inquiry.json"); sys.exit(1)
    e = inquiry.validate(folder, data, (folder / "lesson.md").read_text()); check("validates", not e, "\n".join(e))
    r = subprocess.run([PY, ROOT / "scripts/build.py", lid], capture_output=True, text=True, cwd=LROOT); check("builds", r.returncode == 0, (r.stdout + r.stderr)[-300:])
    if failed: return
    acts = data["activities"]
    exps = [a for a in acts if a["type"] == "experiment"]; preds = [a for a in acts if a["type"] == "choice" and a.get("reveal")]
    stages = [a["stage"] for a in acts]
    check("ennusta before tutki before selita", all(stages.index(s) <= stages.index(t) for s, t in (("ennusta", "tutki"), ("tutki", "selita")) if s in stages and t in stages))
    check("every stage used has an activity, Tarkista has three checks", sum(1 for a in acts if a["stage"] == "tarkista" and a["type"] in ("choice", "numeric", "explain")) >= 3)
    evidence = next((i for i, a in enumerate(acts) if a["type"] in ("experiment", "interpret")), None)
    if evidence is not None:
        check("a committed choice comes before the first investigation", any(a["type"] == "choice" for a in acts[:evidence]), "the student meets the evidence before deciding anything")
    if exps: check("a prediction is tied to an experiment", bool(preds), "experiments exist but no choice has reveal")
    if exps: check("the sim activity precedes the experiments", any(a["type"] == "sim" for a in acts) and acts.index(next(a for a in acts if a["type"] == "sim")) < acts.index(exps[0]))
    page_file = LROOT / "preview" / f"{lid}.html"
    page = page_file.read_text()
    # the page as built: navigation, stage order, and every option with its own correct flag and feedback (options are shuffled)
    toc = re.search(r'<nav class="toc"[^>]*>(.*?)</nav>', page, re.S)
    links = re.findall(r'href="#([^"]+)"', toc.group(1)) if toc else []
    shown = [s for s, _ in inquiry.STAGES if any(a["stage"] == s and a["type"] != "exercises" for a in acts)]
    shown = [s for s in shown if s != "tarkista"] + ["exercises"] + (["tarkista"] if "tarkista" in shown else [])   # Itsearvio after the exercises (teacher 2026-11-06 evening)
    check("navigation lists every stage in order and each link has a target", links == shown and all(f'id="{x}"' in page for x in links), f"nav {links}, stages {shown}")
    for aid, seed, spec in choice_items(acts):
        want = inquiry.choice_order(spec["choices"], lid, seed)
        got = re.findall(rf'<input type="radio" name="{re.escape(seed)}" value="(\d+)" data-correct="([01])"><span>(.*?)</span></label><div class="feedback" data-for="(\d+)" hidden>(.*?)</div></li>', page, re.S)
        ok = len(got) == len(want) and all(int(v) == i == int(f) and (c == "1") == bool(w.get("correct")) and _letters(t) == _letters(w["text"]) and _letters(fb) == _letters(w["feedback"])
                                           for i, ((v, c, t, f, fb), w) in enumerate(zip(got, want)))
        check(f"{seed}: every option keeps its correct flag and feedback", ok, f"{len(got)} rendered, {len(want)} in inquiry.json")
    url = page_file.as_uri()
    with sync_playwright() as pw:
        b = launch(pw); pg = b.new_page(viewport={"width": 1280, "height": 900})
        run_helper_selftest(b)
        errors = []; pg.on("pageerror", lambda x: errors.append(str(x))); pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        pg.goto(url); pg.evaluate("try { localStorage.clear() } catch (e) {}"); pg.goto(url)
        has_sim = 'id="sim-root"' in page
        if has_sim: pg.wait_for_function("window.simState", timeout=3000)
        if exps: pg.wait_for_function("window.simAdapter", timeout=4000)
        pg.wait_for_timeout(300)
        check("no console errors", not errors, str(errors[:2]))
        page_form(pg, b, url, acts, page)
        if pg.locator("#ennusta details.fold").count(): pg.locator("#ennusta details.fold > summary").first.click(); pg.wait_for_timeout(100)   # open the Ennusta box as a student does
        # predictions first, as a student makes them: the tasks further down scroll past the theory section that
        # reveals a theory-linked prediction (fy5-17), and its feedback would then rightly show at once
        wrongs = {}
        def commit_preds(late):
            for pr in preds:
                loc = pg.locator(f"#{pr['id']}")
                if bool(loc.evaluate("(e) => !!e.closest('details.opt')")) != late: continue   # an optional prediction waits until its box is open
                wrong = int(loc.locator("input[data-correct='0']").first.get_attribute("value")); wrongs[pr["id"]] = str(wrong)
                loc.locator("input[type=radio]").nth(wrong).check(); loc.locator("button.commit").click()
                check(f"{pr['id']}: committed without feedback", loc.locator("fieldset").get_attribute("data-committed") == "1" and not loc.locator(".feedback").nth(wrong).is_visible())
        commit_preds(False)
        more = pg.locator('#tutki details[data-fold="tutki-more"]')   # Tutki's other tasks wait in a closed box (teacher 2026-11-06)
        if more.count(): more.evaluate("(d) => { d.open = true; }"); pg.wait_for_timeout(100)
        n_opt = pg.locator("details.opt").count()
        if n_opt:                                         # optional activities: closed, named boxes that open from the keyboard
            st = pg.evaluate("[...document.querySelectorAll('details.opt')].map((d) => [d.open, /Valinnainen|Syventävä|Lisätiedoksi/.test(d.querySelector('summary').textContent) || !d.querySelector('.opt-tag'), !!d.querySelector('.activity[id]')])")
            check("optional activities start closed, are named Valinnainen (or Syventävä, Lisätiedoksi: LOPS 2019 extension, teacher 2026-11-07) and keep their ids (closed required boxes carry no tag)", all(not o and v and i for o, v, i in st), str(st))
            pg.locator("details.opt > summary").first.focus(); pg.keyboard.press("Enter")
            check("an optional box opens from the keyboard", pg.locator("details.opt").first.evaluate("(d) => d.open"))
            pg.evaluate("document.querySelectorAll('details.opt').forEach((d) => { d.open = true; })")   # the rest of the run treats them like the others
        commit_preds(True)
        for a in acts:                                    # plain choices: a wrong option gets its own feedback, the right one "Oikein"
            if a["type"] != "choice" or a.get("reveal"): continue
            loc = pg.locator(f"#{a['id']}")
            wrong = loc.locator("input[data-correct='0']")
            if wrong.count():
                wv = wrong.first.get_attribute("value"); wrong.first.check(); loc.locator("button.commit").click()
                vis = [x.get_attribute("data-for") for x in loc.locator(".feedback").all() if x.is_visible()]
                check(f"{a['id']}: a wrong choice shows its own feedback", vis == [wv] and "Ei aivan" in loc.locator("output").inner_text(), f"visible {vis}, chose {wv}")
            loc.locator("input[data-correct='1']").first.check(); loc.locator("button.commit").click()
            check(f"{a['id']}: the correct choice is marked right", "Oikein" in loc.locator("output").inner_text())
        list_tasks(pg, url)
        if preds and pg.locator("#ennusta details.fold").count():   # closing the box keeps the answers; reopened, they are there
            pg.locator("#ennusta details.fold > summary").first.click(); pg.wait_for_timeout(80); pg.locator("#ennusta details.fold > summary").first.click(); pg.wait_for_timeout(80)
            kept = all(pg.locator(f"#{pr['id']} input[type=radio]").nth(int(wrongs[pr["id"]])).is_checked() for pr in preds)
            check("the Ennusta box keeps the committed predictions when closed and reopened", kept and "vastattu" in pg.locator("#ennusta details.fold .fold-status").inner_text(), pg.locator("#ennusta details.fold .fold-status").inner_text())
        for ex in exps:
            loc = pg.locator(f"#{ex['id']}"); rows = loc.locator(".exp-table tbody tr")
            keys = [m["key"] if isinstance(m, dict) else m for m in ex["measure"]]
            params = sorted(set(ex["initial"]) | set(ex["locked"]) | {ex["vary"]})
            missing = pg.evaluate("(ks) => ks.filter((k) => !(window.simAdapter && window.simAdapter.params[k]))", params)
            check(f"{ex['id']}: the adapter declares {', '.join(params)}", not missing, f"missing {missing}")
            if missing: continue
            loc.locator(".exp-start").click(); pg.wait_for_timeout(200); pg.evaluate(FASTEST)
            st = pg.evaluate("window.simAdapter.get()")
            bad = [k for k, v in ex["initial"].items() if k not in st or abs(float(st[k]) - float(v)) > 1e-6 * max(1, abs(float(v)))] if all(isinstance(v, (int, float)) for v in ex["initial"].values()) else [k for k, v in ex["initial"].items() if k in st and str(st[k]) != str(v)]
            check(f"{ex['id']}: initial state set", not bad, f"{bad} state={ {k: st.get(k) for k in ex['initial']} }")
            locked = pg.evaluate(f"(ks) => ks.map((k) => ({CONTROL})(k).disabled)", ex["locked"])
            check(f"{ex['id']}: controlled parameters locked", all(locked), str(locked))
            check(f"{ex['id']}: varied parameter free", pg.evaluate(f"(k) => !({CONTROL})(k).disabled", ex["vary"]))

            def settle():
                """Let the sim run on screen until every measured key has a value. A sim whose measurement needs a run
                (Lämmitä, then Palauta mäntä) gets its main button pressed, as the experiment's intro tells the student."""
                pg.evaluate("document.getElementById('sim') && document.getElementById('sim').scrollIntoView({block: 'center'})")
                for _ in range(8):
                    try: pg.wait_for_function(SETTLE, arg=keys, timeout=4000, polling=200); return True
                    except Exception: pass
                    if pg.evaluate(RUN) is None: pg.wait_for_timeout(2000)
                return False
            check(f"{ex['id']}: simState gives {', '.join(keys)}", settle())
            loc.locator(".exp-record").click(); pg.wait_for_timeout(100)
            loc.locator(".exp-table tbody tr").first.evaluate("(tr) => { tr.__flFirst = true; }")   # the row node must survive the next measurement
            # move the varied control to another value: a range to its max (or min when already there), a select to the next option
            pg.evaluate(f"""(k) => {{ const e = ({CONTROL})(k);
                if (e.tagName === 'SELECT') e.selectedIndex = (e.selectedIndex + 1) % e.options.length;
                else e.value = (Number(e.value) === Number(e.max)) ? e.min : e.max;
                e.dispatchEvent(new Event('input', {{bubbles: true}})); e.dispatchEvent(new Event('change', {{bubbles: true}})); }}""", ex["vary"])
            pg.wait_for_timeout(300); settle(); loc.locator(".exp-record").click(); pg.wait_for_timeout(100)
            got = rows.all_inner_texts()
            check(f"{ex['id']}: two measurements recorded", len(got) == 2 and got[0] != got[1], f"{got} / {loc.locator('.exp-status').inner_text()}")
            for pr in preds:
                if pr["reveal"]["after"] == ex["id"] and pr["reveal"].get("min", 1) <= 2:
                    loc2 = pg.locator(f"#{pr['id']}"); vis = [x.get_attribute("data-for") for x in loc2.locator(".feedback").all() if x.is_visible()]
                    check(f"{pr['id']}: revealed by {ex['id']}, with the feedback of the committed option", vis == [wrongs[pr["id"]]] and not loc2.locator(".pending").is_visible() and "Ei aivan" in loc2.locator("output").inner_text(), f"visible {vis}")
            kept = loc.locator(".exp-table tbody tr").evaluate_all("(trs) => trs.length === 2 && trs[0].__flFirst === true && !trs[1].__flFirst")
            check(f"{ex['id']}: a new measurement adds its own row, the earlier row is not rebuilt (2026-11-05)", kept)
            typeset_ok = loc.locator(".exp-table tbody tr").nth(1).evaluate("(tr) => ![...tr.querySelectorAll('td')].some((td) => /\\$/.test(td.textContent))")
            check(f"{ex['id']}: the new row's formulas are typeset", typeset_ok)
            export_checks(pg, lid, ex, loc)
            restore_checks(pg, url, lid, ex, loc, rows.all_text_contents())
            loc.locator(".exp-reset").click(); pg.wait_for_timeout(150)
            unlocked = pg.evaluate(f"(ks) => ks.every((k) => !({CONTROL})(k).disabled)", ex["locked"])
            check(f"{ex['id']}: reset unlocks and clears", unlocked and rows.count() == 0)
            n = pg.evaluate("(id) => [...document.querySelectorAll('.experiment')].indexOf(document.querySelector('#' + id + ' .experiment')) + 1", ex["id"])
            check(f"{ex['id']}: Nollaa clears the stored table and disables the export",
                  pg.evaluate(f"() => {{ try {{ return localStorage.getItem('ruukkilabra:{lid}:koe{n}') }} catch (e) {{ return null }} }}") is None
                  and loc.locator(".exp-copy").is_disabled())
        for a in acts:
            if a["type"] == "numeric": check(f"{a['id']}: numeric form", pg.locator(f"#{a['id']} form.check input").count() == 1)
            if a["type"] == "explain": check(f"{a['id']}: explain form", pg.locator(f"#{a['id']} textarea").count() == 1 and pg.locator(f"#{a['id']} .show-model").count() == 1)
        check("no console errors after the run", not errors, str(errors[:2]))
        pg.close()
        pg = b.new_page(viewport={"width": 360, "height": 740}); pg.goto(url); pg.wait_for_timeout(600)
        over = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth"); check("no horizontal overflow at 360 px", over <= 0, str(over))
        wide = pg.evaluate("[...document.querySelectorAll('fieldset.choice, .experiment, .reflect, .explain, .activity > .katex-display')].filter(e => e.getBoundingClientRect().right > 361).length"); check("activity boxes fit at 360 px", wide == 0, str(wide))
        pg.close(); b.close()


if len(sys.argv) > 1:
    generic(sys.argv[1]); print(f"\n{passed} passed, {failed} failed"); sys.exit(1 if failed else 0)


# ---------------------------------------------------------------- part 1: validation and rendering
folder = ROOT / "content/fi/FY3/fy3-2"
good = json.loads((folder / "inquiry.json").read_text()); lesson_md = (folder / "lesson.md").read_text()
check("pilot validates", inquiry.validate(folder, good, lesson_md) == [], str(inquiry.validate(folder, good, lesson_md)))

def errs_of(mutate):
    d = copy.deepcopy(good); mutate(d); return inquiry.validate(folder, d, lesson_md)
def act(d, aid): return next(a for a in d["activities"] if a["id"] == aid)   # by id: inserting an activity must not shift the tests

e = errs_of(lambda d: d.__setitem__("version", 2)); check("wrong version named", any("version" in x and x.startswith("fy3-2 inquiry.json") for x in e), str(e))
# the source line (teacher 2026-11-13): no pill; a short "Lähde: …" for measured and statistics (a link when the note names an address),
# "Esimerkkiaineisto." for example and simulated, nothing for a model; the long method note only in the title
_long = "Tilastokeskus: Sähkön ja lämmön tuotanto 2024 (ydinvoiman ja bioperäisten polttoaineiden luvut johdettu prosenttiosuuksista, pyöristetty; muut lähteet = …)."
_ln = inquiry.source_line("statistics", _long, lambda x: x)
check("source line: statistics shows a short Lähde: line without the method note", "Lähde: Tilastokeskus: Sähkön ja lämmön tuotanto 2024<" in _ln and "ydinvoiman" in _ln.split(">")[0] and "ydinvoiman" not in _ln.split(">", 1)[1], _ln)
check("source line: example and simulated say Esimerkkiaineisto., a model nothing", all(inquiry.source_line(k, "x", lambda x: x).endswith("Esimerkkiaineisto.</p>") for k in ("example", "simulated")) and inquiry.source_line("model", "x", lambda x: x) == "")
check("source line: an address in the note makes a link; a cut never splits a formula", 'href="https://nrel.github.io/turbine-models"' in inquiry.source_line("statistics", "Teho, $82\\,\\text{m}$: NREL (nrel.github.io/turbine-models), luettu 2026. " + "sana " * 40, lambda x: x) and inquiry.source_short("a $b c$ " * 30, 20)[0].count("$") % 2 == 0)
check("source line: no pill classes or tag text left in the rendered markup", "<strong>" not in _ln)
e = errs_of(lambda d: d["activities"][2]["choices"][1].pop("feedback")); check("missing feedback names lesson, activity and choice", any("activities[2].choices[1].feedback" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"][2].__setitem__("reveal", {"after": "nope"})); check("reveal must point at an experiment", any("reveal.after" in x for x in e), str(e))
e = errs_of(lambda d: act(d, "exp-1")["locked"].append("s")); check("varied parameter cannot be locked", any("locked" in x for x in e), str(e))
e = errs_of(lambda d: act(d, "theory")["sections"].append("Ei ole")); check("theory section must exist in lesson.md", any("Ei ole" in x for x in e), str(e))
e = errs_of(lambda d: act(d, "theory")["sections"].append("Esimerkki")); check("a section placed twice is an error", any("more than once" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"].append(dict(d["activities"][0]))); check("duplicate id is an error", any("used twice" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"][0].__setitem__("stage", "lopuksi")); check("unknown stage is an error", any("stage" in x for x in e), str(e))
e = errs_of(lambda d: [c.__setitem__("correct", False) for c in d["activities"][1]["choices"]]); check("a choice needs one correct option", any('"correct": true' in x for x in e), str(e))
e = errs_of(lambda d: act(d, "siirto").__setitem__("hints", ["a", "b", "c", "d"])); check("at most three hints", any("hints" in x for x in e), str(e))
e = errs_of(lambda d: act(d, "siirto").__setitem__("answer", "240")); check("numeric answer must be a number", any("answer" in x for x in e), str(e))
e = errs_of(lambda d: act(d, "check-3").pop("model")); check("explain needs a model answer", any("model" in x for x in e), str(e))
e = errs_of(lambda d: act(d, "check-3")["criteria"].__setitem__(0, "Osaan selittää työn.")); check("a confidence statement is not a criterion", any("how sure" in x for x in e), str(e))
e = errs_of(lambda d: act(d, "check-3").__setitem__("figure", "fy3-9/hero")); check("a task's figure must carry information", any("figure" in x for x in e), str(e))
types = {a["type"] for a in good["activities"]}
check("pilot exercises every implemented type but text", types >= set(inquiry.TYPES) - {"text"}, str(set(inquiry.TYPES) - types))
named = lesson_md.replace("\n## Kaava\n", "\n## Kaava: Työ ja teho\n")
check("a formula section named after its law is still the section Kaava", inquiry.heading("Kaava: Työ ja teho") == ("Kaava", "Työ ja teho") and inquiry.validate(folder, good, named) == [] and "Kaava" in inquiry.section_keys(named))
md_id = lambda t: f"<p>{t}</p>"
lead, info = inquiry.sim_parts({"text": "Kokeile vapaasti.", "howto": "Säädä.", "model": "Ei kitkaa.", "calc": "W = Fs."}, md_id)
check("sim activity: a short visible lead and three closed, named boxes", lead == "<p>Kokeile vapaasti.</p>" and info.count("<details class=\"sim-box\">") == 3
      and [x for x in ("Käyttöohje", "Mallin oletukset", "Laskennan selitys") if f"<summary>{x}</summary>" in info] == ["Käyttöohje", "Mallin oletukset", "Laskennan selitys"] and " open" not in info)
lead, info = inquiry.sim_parts({"text": " ".join(["sana"] * 40)}, md_id)
check("sim activity: a long text from before 2026-10-26 goes behind one box", lead == "" and f"<summary>{inquiry.LEGACY_INFO}</summary>" in info)

# a lesson without inquiry.json renders in the classic layout: build a copy of fy3-2 without the file in a temporary root
with tempfile.TemporaryDirectory() as tmp:
    troot = pathlib.Path(tmp)
    for n in ("templates", "lang", "curriculum.json", "competencies.json", "glossary.json"):
        src = ROOT / n
        if src.is_dir(): shutil.copytree(src, troot / n)
        elif src.exists(): shutil.copy(src, troot / n)
    shutil.copytree(folder, troot / "content/fi/FY3/fy3-2", ignore=shutil.ignore_patterns("review", "packet-*"))
    shutil.copytree(ROOT / "lessons/FY3/fy3-2", troot / "lessons/FY3/fy3-2", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(ROOT / "assets/pics/fy3", troot / "assets/pics/fy3")   # the lesson's photograph and its credit (photos.json)
    (troot / "content/fi/FY3/fy3-2/inquiry.json").unlink(); (troot / "content/fi/FY3/fy3-2/lesson.md").write_text(named)
    env = {**os.environ, "FYSIIKKALABRA_ROOT": tmp}
    r = subprocess.run([PY, ROOT / "scripts/build.py", "fy3-2"], capture_output=True, text=True, cwd=ROOT, env=env)
    classic = (troot / "preview/fy3-2.html").read_text() if r.returncode == 0 else ""
    check("classic lesson builds", r.returncode == 0, (r.stdout + r.stderr)[-300:])
    check("classic lesson keeps its layout", '<article id="teoria">' in classic and 'class="stage"' not in classic and 'inquiry.js' not in classic
          and '<a href="#teoria">Teoria</a><a href="#sim">Simulaatio</a><a href="#exit">Pohdintatehtävä</a><a href="#exercises">Tehtävät</a>' in classic
          and '<section id="sim"><h2>Simulaatio</h2>' in classic and classic.index('<section id="sim">') < classic.index('<h2>Esimerkki</h2>'))
    check("classic lesson: the formula section shows its law's name, the exercises come after the exit ticket",
          '<h2 data-section="Kaava">Työ ja teho</h2>' in classic and "Kaava: Työ" not in classic and classic.index('<section id="exit"><h2>Pohdintatehtävä</h2>') < classic.index('<section id="exercises">'))

# a broken inquiry.json fails the build with the field named
with tempfile.TemporaryDirectory() as tmp:
    bad = pathlib.Path(tmp) / "content/fi/FY3/fy3-2"; shutil.copytree(folder, bad)
    d = copy.deepcopy(good); d["activities"][2]["choices"][1].pop("feedback"); (bad / "inquiry.json").write_text(json.dumps(d))
    r = subprocess.run([PY, ROOT / "scripts/lint_lesson.py", "fy3-2"], capture_output=True, text=True, cwd=ROOT, env={**__import__("os").environ, "FYSIIKKALABRA_ROOT": tmp})
    # lint_lesson resolves its own ROOT; validate directly instead
    e = inquiry.validate(bad, d, lesson_md)
    check("lint-level validation names the field on a copy", any("choices[1].feedback" in x for x in e), str(e))

# options are shown in a seeded order: the same on every build, the correct one not always in the same place
opts = [{"text": f"v{i}", "feedback": "f", **({"correct": True} if i == 1 else {})} for i in range(4)] + [{"text": "Laskussa ei ole virhettä.", "feedback": "f"}]
o1, o2 = inquiry.choice_order(opts, "fy3-2", "virhe"), inquiry.choice_order(opts, "fy3-2", "virhe")
check("option order is deterministic and keeps every option", o1 == o2 and sorted(c["text"] for c in o1) == sorted(c["text"] for c in opts))
check("'ei ole virhettä' stays last", o1[-1]["text"].startswith("Laskussa ei ole"))
places = {[c.get("correct", False) for c in inquiry.choice_order(opts, "fy3-2", f"q{k}")].index(True) for k in range(20)}
check("the correct option moves from question to question", len(places) >= 3, str(places))

r = subprocess.run([PY, ROOT / "scripts/build.py", "fy3-2"], capture_output=True, text=True, cwd=ROOT)
check("pilot builds", r.returncode == 0, (r.stdout + r.stderr)[-300:])
page_html = (ROOT / "preview/fy3-2.html").read_text()
for sid, title in inquiry.STAGES: check(f"stage {sid} rendered", f'<section class="stage" id="{sid}"' in page_html and title in page_html)
order = [page_html.index(f'id="{sid}"') for sid, _ in inquiry.STAGES]; check("stages in order", order == sorted(order))
check("theory sections placed once", page_html.count('class="theory-h">Ydinajatus') == 1 and page_html.count('class="example-title">Esimerkki 1: ') == 1)
check("the worked example's box says 'Esimerkki 1: <name>', with no heading above it (teacher 2026-11-06)", 'class="theory-h">Esimerkki' not in page_html and 'class="example-label"' not in page_html
      and f'Esimerkki 1: {inquiry.example_name("fy3-2")}</h3>' in page_html)
check("the other boxes of Esimerkit are numbered examples too", re.search(r'id="sovella".*?Esimerkki 2: ', page_html, re.S) is not None)
check("Itsearvio numbers its tasks from the exit ticket on: 1. Pohdintatehtävä, 2. … (teacher 2026-11-06)", re.search(r'id="tarkista".*?<h3>1\. Pohdintatehtävä</h3>.*?<h3>2\. (?:Käsite|Lasku|Selitys)tehtävä', page_html, re.S) is not None)
check("Itsearvio names its tasks by kind (Käsitetehtävä, Laskutehtävä, Selitystehtävä)", re.search(r'id="tarkista".*?(?:Käsitetehtävä|Laskutehtävä|Selitystehtävä)', page_html, re.S) is not None)
check("unplaced sections land in Teoriatiivistelmä", page_html.index('class="theory-h">Tiivistelmä') < page_html.index('id="sovella"'))
tk = page_html[page_html.index('<section class="stage" id="tarkista"'):]
check("the exit ticket opens Tarkista osaamisesi, with no nav link of its own", tk.index('id="exit"') < tk.index('</section>') and tk.index('id="exit"') < tk.index('class="activity act-choice')
      and '<a href="#exit"' not in page_html)
check("Itsearvio closes the page, after the exercises (teacher 2026-11-06 evening)", page_html.index('<section class="stage stage-practice" id="exercises"') < page_html.index('<section class="stage" id="tarkista"') < page_html.index('id="exit"') and page_html.count('id="exercises"') == 1
      and re.search(r'<a href="#exercises"[^>]*>(?:(?!</a>).)*Tehtävät(?:(?!</a>).)*</a><a href="#tarkista"[^>]*>(?:(?!</a>).)*</a></nav>', page_html) is not None)
nav_html = re.search(r'<nav class="toc".*?</nav>', page_html, re.S).group(0)
nos = [int(x) for x in re.findall(r'<span class="toc-no" aria-hidden="true">(\d+)</span>', nav_html)]
heads = [int(x) for x in re.findall(r'<section class="stage[^"]*" id="[^"]+"[^>]*><h2><span class="stage-no" aria-hidden="true">(\d+)</span>', page_html)]
check("every chip in the bar, Tehtävät too, has its number, and the numbers run 1, 2, 3 … in page order like the stage headings (teacher 2026-11-06)",
      nos == list(range(1, len(nos) + 1)) and nos == heads and nav_html.count('<a href="#') == len(nos) and '<a href="#exercises"><span class="toc-no"' in nav_html, (nos, heads))
check("Ennusta is a closed box", re.search(r'<section class="stage" id="ennusta"[^>]*><h2>.*?</h2><details class="fold" data-fold="ennusta">', page_html) is not None)
check("no old names on the page", not any(x in page_html for x in ("Herätä kiinnostus", "Lähtölippu", ">Selitä<")))
_ex = json.loads((ROOT / "content/fi/FY3/fy3-2/exercises/exercises.json").read_text()); _lv = [len(_ex[f"level{k}"]) for k in (1, 2, 3)]
check(f"exercises and exit ticket kept ({'/'.join(map(str, _lv))}, 1 item)", page_html.count('class="level"') == 3 and page_html.count("<li>$(s, F)$-kuvaajassa") == 1
      and re.findall(r'<span class="count">(\d+) tehtävää', page_html) == [str(n) for n in _lv])
check("no answer disclosed before commitment", 'class="feedback" data-for="0" hidden' in page_html)
check("nav lists the stages", '<a href="#herata">' in page_html and '<a href="#tarkista">' in page_html)

# ---------------------------------------------------------------- part 2: browser
try:
    from playwright.sync_api import sync_playwright
    from _browser import launch
except Exception as ex:
    print("skipped browser tests:", ex); print(f"\n{passed} passed, {failed} failed, browser part skipped"); sys.exit(1 if failed else 0)

url = (ROOT / "preview/fy3-2.html").as_uri()
with sync_playwright() as pw:
    b = launch(pw)
    pg = b.new_page(viewport={"width": 1280, "height": 900})
    errors = []; pg.on("pageerror", lambda e: errors.append(str(e))); pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    pg.goto(url); pg.evaluate("try { localStorage.clear() } catch (e) {}"); pg.goto(url)
    pg.wait_for_function("window.simState && window.simAdapter", timeout=3000)
    check("no console errors on load", not errors, str(errors[:2]))
    check("adapter declares capabilities", pg.evaluate("JSON.stringify(window.simAdapter.capabilities.set) === '[\"F\",\"s\",\"t\"]' && window.simAdapter.capabilities.reset === true"))

    # the Ennusta box: closed at first, opened by its summary
    fold = pg.locator("#ennusta details.fold")
    check("predictions hidden in a closed box at first", not fold.evaluate("(d) => d.open") and not pg.locator("#pred-1 button.commit").is_visible())
    fold.locator(":scope > summary").click(); check("the summary opens the box", fold.evaluate("(d) => d.open") and pg.locator("#pred-2 button.commit").is_visible())
    opt1 = pg.locator("details.opt:has(#pred-1)")   # pred-1 is optional in the pilot: closed until the student opens it
    check("an optional prediction waits in its closed box", not opt1.evaluate("(d) => d.open") and not pg.locator("#pred-1 button.commit").is_visible())
    opt1.locator(":scope > summary").click(); check("the optional box opens", pg.locator("#pred-1 button.commit").is_visible())
    pg.evaluate("document.querySelectorAll('details.opt').forEach((d) => { d.open = true; })")   # the rest of the run treats optional items like the others
    # prediction: commit first, no feedback until the experiment has two measurements
    p1 = pg.locator("#pred-1")
    p1.locator("button.commit").click(); check("empty commit asks for a choice", "Valitse" in p1.locator("output").inner_text())
    w1 = int(p1.locator("input[data-correct='0']").first.get_attribute("value"))   # a wrong option; options are shown shuffled
    p1.locator("input[type=radio]").nth(w1).check(); p1.locator(".justify textarea").fill("voima sama")
    p1.locator("button.commit").click()
    check("prediction committed: radios locked, feedback hidden", p1.locator("input[type=radio]").nth(w1).is_disabled() and not p1.locator(".feedback").nth(w1).is_visible() and p1.locator(".pending").is_visible())
    check("the box counts the answers", "vastattu 1/" in fold.locator(".fold-status").inner_text(), fold.locator(".fold-status").inner_text())
    fold.locator(":scope > summary").click(); fold.locator(":scope > summary").click()
    check("closing and reopening the box keeps the prediction and its reason", p1.locator("input[type=radio]").nth(w1).is_checked() and p1.locator(".justify textarea").input_value() == "voima sama")
    fold.locator(":scope > summary").click()

    ex1 = pg.locator("#exp-1")
    check("record disabled before the initial state is set", ex1.locator(".exp-record").is_disabled())
    ex1.locator(".exp-start").click(); pg.wait_for_timeout(150)
    check("1280 px: the simulation stays in its column beside the experiment", pg.locator(".lab-side #sim").count() == 1 and not pg.locator(".sim-moved").is_visible())
    side = pg.evaluate("(() => { const s = document.querySelector('.lab-side'); return [getComputedStyle(s).overflowY, s.scrollHeight - s.clientHeight]; })()")
    check("1280 px: the simulation column has no scrollbar of its own (Lauri 2026-11-04)", side[0] == "visible" and side[1] <= 1, str(side))
    st = pg.evaluate("window.simState")
    check("initial conditions set (F 60, s 10, t 5)", st["F"] == 60 and st["s"] == 10 and st["t"] == 5, str(st))
    locked = pg.evaluate("[...document.querySelectorAll('#sim-root input[type=range]')].map(r => r.disabled)")
    check("controlled parameters locked, varied one free", locked == [True, False, True], str(locked))
    ex1.locator(".exp-record").click(); pg.wait_for_timeout(50)
    check("first measurement recorded", ex1.locator(".exp-table tbody tr").count() == 1 and "600" in ex1.locator(".exp-table tbody tr").nth(0).inner_text())
    ex1.locator(".exp-record").click(); check("same value not recorded twice", ex1.locator(".exp-table tbody tr").count() == 1 and "Sama" in ex1.locator(".exp-status").inner_text())
    check("still no feedback after one measurement", not p1.locator(".feedback").nth(w1).is_visible())
    pg.evaluate("(() => { const r=document.querySelectorAll('#sim-root input[type=range]')[1]; r.value=20; r.dispatchEvent(new Event('input',{bubbles:true})); })()"); pg.wait_for_timeout(120)
    ex1.locator(".exp-record").click(); pg.wait_for_timeout(50)
    rows = ex1.locator(".exp-table tbody tr").all_inner_texts()
    check("second measurement doubles W", len(rows) == 2 and "1200" in rows[1], str(rows))
    check("the closed box tells that feedback is ready", "palaute 1/" in fold.locator(".fold-status").inner_text(), fold.locator(".fold-status").inner_text())
    fold.locator(":scope > summary").click()
    check("prediction feedback revealed after two measurements", p1.locator(".feedback").nth(w1).is_visible() and "Ei aivan" in p1.locator("output").inner_text() and not p1.locator(".pending").is_visible())
    fold.locator(":scope > summary").click()
    ex1.locator(".exp-reset").click(); pg.wait_for_timeout(120)
    st = pg.evaluate("window.simState"); locked = pg.evaluate("[...document.querySelectorAll('#sim-root input[type=range]')].map(r => r.disabled)")
    check("reset restores defaults, unlocks, clears the table", st["s"] == 10 and st["u"] == 0 and locked == [False, False, False] and ex1.locator(".exp-table tbody tr").count() == 0, f"{st} {locked}")

    # reflection shows the stored prediction and its outcome
    refl = pg.locator("#reflect .my-predictions li")
    check("reflection lists three predictions", refl.count() == 3)
    check("reflection shows my prediction and the verdict", "Ennustit" in refl.nth(0).inner_text() and "ei tue" in refl.nth(0).inner_text() and "Et ole vielä" in refl.nth(1).inner_text(), refl.nth(0).inner_text())
    refl.nth(1).locator("a").click(); pg.wait_for_timeout(150)
    check("a link to a prediction opens the closed box", fold.evaluate("(d) => d.open") and pg.locator("#pred-2 button.commit").is_visible())

    # plain choice: feedback after Vastaa, may change and re-check
    c = pg.locator("#pr-paino"); w = c.locator("label").filter(has=pg.get_by_text("10 N", exact=True))   # the mass-for-weight option
    wv = w.locator("input").get_attribute("value"); w.locator("input").check(); c.locator("button.commit").click()
    check("retrieval choice gives misconception feedback", c.locator(f".feedback[data-for='{wv}']").is_visible() and "Massa ja paino" in c.locator(f".feedback[data-for='{wv}']").inner_text())
    c.locator("input[data-correct='1']").check(); check("changing the choice hides old feedback", not c.locator(f".feedback[data-for='{wv}']").is_visible())
    c.locator("button.commit").click(); check("correct choice marked, and final", "Oikein" in c.locator("output").inner_text() and c.locator("input[type=radio]").first.is_disabled())

    # plain choice, two wrong tries: why the choice is wrong, one change, then the correct option with its reasoning
    c1 = pg.locator("#check-c2"); wr = c1.locator("input[data-correct='0']")
    wr.nth(0).check(); c1.locator("button.commit").click()
    check("first wrong try: its own feedback and one more change", c1.locator(f".feedback[data-for='{wr.nth(0).get_attribute('value')}']").is_visible() and "vielä kerran" in c1.locator("output").inner_text())
    wr.nth(1).check(); c1.locator("button.commit").click()
    cv = c1.locator("input[data-correct='1']").get_attribute("value")
    check("second wrong try: the correct option shown with its reasoning, the choice closed", c1.locator(f".feedback[data-for='{cv}']").is_visible()
          and "Oikea vastaus" in c1.locator(f".feedback[data-for='{cv}']").inner_text() and wr.nth(0).is_disabled() and not c1.locator("button.commit").is_visible())

    # numeric: comma, invalid, mistake feedback, retries, hints progressive
    n = pg.locator("#siirto"); inp = n.locator("form.check input"); out = n.locator("form.check output")
    sol = n.locator("details.solution")
    check("the solution is locked, in view, until a try", sol.is_visible() and sol.get_attribute("data-locked") == "1" and "yrittänyt kerran" in sol.locator("summary").inner_text())
    sol.locator("summary").click(); check("a locked solution does not open", not sol.evaluate("(d) => d.open"))
    inp.fill("abc"); n.locator("form.check button").click(); check("invalid input asks for a number", "Kirjoita luku" in out.inner_text())
    check("a non-number is not a try", sol.get_attribute("data-locked") == "1")
    inp.fill("9,6"); n.locator("form.check button").click(); check("common mistake gets its feedback", "Jaoit voiman" in out.inner_text(), out.inner_text())
    inp.fill("1e400"); n.locator("form.check button").click(); check("non-finite input does not crash", not errors and out.inner_text() != "", str(errors[:1]))
    check("a number checked once opens the solution", sol.get_attribute("data-locked") is None)
    inp.fill("250"); n.locator("form.check button").click(); check("2–5 % away is close, not wrong", "Lähellä" in out.inner_text() and out.get_attribute("data-state") == "close", out.inner_text())
    inp.fill("244"); n.locator("form.check button").click(); check("within 2 % is accepted", "Oikein" in out.inner_text(), out.inner_text())
    inp.fill("240,0"); n.locator("form.check button").click(); check("decimal comma accepted", "Oikein" in out.inner_text())
    inp.fill("0,24"); n.locator("form.check button").click(); check("after a correct answer a later mistake does not override", "Oikein" in out.inner_text() or "kilowat" in out.inner_text())
    hints = n.locator(".hints details")
    check("every hint in view and unlocked", hints.count() >= 2 and all(hints.nth(k).is_visible() and hints.nth(k).get_attribute("data-locked") is None for k in range(hints.count())))
    hints.nth(1).locator("summary").click(); pg.wait_for_timeout(80); check("a later hint opens without the first (teacher 2026-11-04)", hints.nth(1).evaluate("(d) => d.open"))
    n2 = pg.locator("#check-2"); i2 = n2.locator("form.check input"); o2 = n2.locator("form.check output")
    i2.fill("100"); n2.locator("form.check button").click(); i2.fill("100"); n2.locator("form.check button").click()
    check("second wrong try points to the solution", "Ei vielä" in o2.inner_text() or "Vastaus" in o2.inner_text(), o2.inner_text())

    # explanation: model answer and criteria on request
    ex = pg.locator("#check-3"); ex.locator(".show-model").click(force=True)
    check("the model answer waits for the student's own answer", not ex.locator(".model").is_visible() and ex.locator(".show-model").get_attribute("aria-disabled") == "true"
          and "Kirjoita ensin" in ex.locator(".explain-status").inner_text() and ex.locator(".drew").count() == 0)
    ex.locator("textarea").fill("Työ ei riipu ajasta.")
    check("model answer hidden until asked", not ex.locator(".model").is_visible() and ex.locator(".show-model").get_attribute("aria-disabled") is None)
    ex.locator(".show-model").click(); check("model answer and criteria shown", ex.locator(".model").is_visible() and ex.locator("ul.criteria input[type=checkbox]").count() == 4)
    boxes = ex.locator("ul.criteria input[type=checkbox]"); boxes.nth(0).check(); boxes.nth(1).check(); ex.locator(".check-criteria").click()
    check("what is missing: the two unticked criteria and where to practise", ex.locator(".crit-missing li").count() == 2 and ex.locator(".crit-practice").is_visible()
          and ex.locator(".crit-practice a[href='#exercises']").count() == 1, ex.locator(".crit-result").inner_text())
    boxes.nth(2).check(); boxes.nth(3).check(); ex.locator(".check-criteria").click()
    check("all criteria ticked: nothing missing, no practice pointer", ex.locator(".crit-missing li").count() == 0 and not ex.locator(".crit-practice").is_visible())
    check("no chapter-level Osaan / Tarvitsen self-assessment", pg.locator(".selfcheck, #arvioi").count() == 0)

    # persistence survives a reload (per-device convenience only)
    pg.reload(); pg.wait_for_function("window.simState && window.simAdapter", timeout=3000)
    check("prediction remembered after reload", pg.locator("#pred-1 input[type=radio]").nth(w1).is_checked() and pg.locator("#pred-1 input[type=radio]").nth(w1).is_disabled())
    check("explanation remembered after reload", "Työ ei riipu" in pg.locator("#check-3 textarea").input_value())

    # keyboard: a choice answered with arrows and Enter
    pg.evaluate("try { localStorage.clear() } catch (e) {}"); pg.goto(url); pg.wait_for_function("window.simState", timeout=3000)   # without the #pred-2 the link left, which would open the box
    check("the box starts closed again on a new visit", not pg.locator("#ennusta details.fold").evaluate("(d) => d.open"))
    pg.locator("#ennusta details.fold > summary").focus(); pg.keyboard.press("Enter")
    check("keyboard opens the Ennusta box", pg.locator("#ennusta details.fold").evaluate("(d) => d.open"))
    pg.locator("#pred-2 input[type=radio]").nth(0).focus(); pg.keyboard.press("ArrowDown"); pg.keyboard.press("Tab")
    pg.keyboard.press("Tab"); pg.keyboard.press("Enter")   # textarea (justify), then the Vastaa button
    check("keyboard commit works", pg.locator("#pred-2 fieldset").get_attribute("data-committed") == "1" and pg.locator("#pred-2 .pending").is_visible())
    pg.close()

    # 360 px: no horizontal overflow, experiment table and fieldsets fit
    pg = b.new_page(viewport={"width": 360, "height": 740}); pg.goto(url); pg.wait_for_function("window.simState", timeout=3000)
    over = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    check("no horizontal page overflow at 360 px", over <= 0, str(over))
    wide = pg.evaluate("[...document.querySelectorAll('fieldset.choice, .experiment, .reflect, .explain')].filter(e => e.getBoundingClientRect().right > 361).length")
    check("activity boxes fit at 360 px", wide == 0, str(wide))
    more = pg.locator('#tutki details[data-fold="tutki-more"]')   # Tutki: one task in view, the rest in a closed box (teacher 2026-11-06)
    check("Tutki shows one task, the rest wait in a closed box", more.count() == 1 and not more.evaluate("(d) => d.open") and more.locator("#exp-2").count() == 1
          and pg.locator("#tutki .activity:not(.act-sim)").filter(visible=True).count() == 1, str(more.count()))
    more.locator(":scope > summary").click()
    pg.locator("#exp-2 .exp-start").click(); pg.locator("#exp-2 .exp-record").click(); pg.wait_for_timeout(50)
    check("experiment works at 360 px, the simulation brought beside its buttons", pg.locator("#exp-2 .exp-table tbody tr").count() == 1 and pg.locator("#exp-2 #sim").count() == 1 and pg.locator(".sim-moved").is_visible())
    pg.close()
    b.close()

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
