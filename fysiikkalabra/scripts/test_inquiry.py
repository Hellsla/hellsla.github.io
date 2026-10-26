"""Tests of the inquiry framework (scripts/inquiry.py, templates/inquiry.js, the sim adapter).
Usage: python scripts/test_inquiry.py            the framework suite on the fy3-2 pilot (below)
       python scripts/test_inquiry.py <id>       generic checks of one lesson (check_lesson.py and CI run it for every
                                                 lesson with inquiry.json): validation, build, stage order and the page
                                                 navigation, every option's correct flag and feedback as rendered,
                                                 plain choices answer right and wrong, predictions commit without
                                                 feedback and are revealed by their experiment, every experiment runs
                                                 on the adapter (its parameters and measured keys exist, initial state
                                                 set, controlled parameters locked, two measurements, reset), forms
                                                 present, no console errors, 360 px fit

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
  if (b && !b.disabled && !/…$/.test(b.textContent.trim())) { b.click(); return b.textContent.trim(); } return null; }"""
CONTROL = "(k) => { const p = window.simAdapter.params[k]; return typeof p.input === 'string' ? document.querySelector(p.input) : p.input; }"


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
    shown = [s for s, _ in inquiry.STAGES if s in stages]
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
        errors = []; pg.on("pageerror", lambda x: errors.append(str(x))); pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        pg.goto(url); pg.evaluate("try { localStorage.clear() } catch (e) {}"); pg.goto(url)
        has_sim = 'id="sim-root"' in page
        if has_sim: pg.wait_for_function("window.simState", timeout=3000)
        if exps: pg.wait_for_function("window.simAdapter", timeout=4000)
        pg.wait_for_timeout(300)
        check("no console errors", not errors, str(errors[:2]))
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
        wrongs = {}
        for pr in preds:
            loc = pg.locator(f"#{pr['id']}"); wrong = int(loc.locator("input[data-correct='0']").first.get_attribute("value")); wrongs[pr["id"]] = str(wrong)
            loc.locator("input[type=radio]").nth(wrong).check(); loc.locator("button.commit").click()
            check(f"{pr['id']}: committed without feedback", loc.locator("fieldset").get_attribute("data-committed") == "1" and not loc.locator(".feedback").nth(wrong).is_visible())
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
            loc.locator(".exp-reset").click(); pg.wait_for_timeout(150)
            unlocked = pg.evaluate(f"(ks) => ks.every((k) => !({CONTROL})(k).disabled)", ex["locked"])
            check(f"{ex['id']}: reset unlocks and clears", unlocked and rows.count() == 0)
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
folder = ROOT / "content/FY3/fy3-2"
good = json.loads((folder / "inquiry.json").read_text()); lesson_md = (folder / "lesson.md").read_text()
check("pilot validates", inquiry.validate(folder, good, lesson_md) == [], str(inquiry.validate(folder, good, lesson_md)))

def errs_of(mutate):
    d = copy.deepcopy(good); mutate(d); return inquiry.validate(folder, d, lesson_md)

e = errs_of(lambda d: d.__setitem__("version", 2)); check("wrong version named", any("version" in x and x.startswith("fy3-2 inquiry.json") for x in e), str(e))
e = errs_of(lambda d: d["activities"][2]["choices"][1].pop("feedback")); check("missing feedback names lesson, activity and choice", any("activities[2].choices[1].feedback" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"][2].__setitem__("reveal", {"after": "nope"})); check("reveal must point at an experiment", any("reveal.after" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"][6]["locked"].append("s")); check("varied parameter cannot be locked", any("locked" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"][9]["sections"].append("Ei ole")); check("theory section must exist in lesson.md", any("Ei ole" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"][9]["sections"].append("Esimerkki")); check("a section placed twice is an error", any("more than once" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"].append(dict(d["activities"][0]))); check("duplicate id is an error", any("used twice" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"][0].__setitem__("stage", "lopuksi")); check("unknown stage is an error", any("stage" in x for x in e), str(e))
e = errs_of(lambda d: [c.__setitem__("correct", False) for c in d["activities"][1]["choices"]]); check("a choice needs one correct option", any('"correct": true' in x for x in e), str(e))
e = errs_of(lambda d: d["activities"][13].__setitem__("hints", ["a", "b", "c", "d"])); check("at most three hints", any("hints" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"][13].__setitem__("answer", "240")); check("numeric answer must be a number", any("answer" in x for x in e), str(e))
e = errs_of(lambda d: d["activities"][17].pop("model")); check("explain needs a model answer", any("model" in x for x in e), str(e))
types = {a["type"] for a in good["activities"]}
check("pilot exercises every implemented type but text", types >= set(inquiry.TYPES) - {"text"}, str(set(inquiry.TYPES) - types))

# a lesson without inquiry.json renders in the classic layout: build a copy of fy3-2 without the file in a temporary root
with tempfile.TemporaryDirectory() as tmp:
    troot = pathlib.Path(tmp)
    for n in ("templates", "curriculum.json", "glossary.json"):
        src = ROOT / n
        if src.is_dir(): shutil.copytree(src, troot / n)
        elif src.exists(): shutil.copy(src, troot / n)
    shutil.copytree(folder, troot / "content/FY3/fy3-2", ignore=shutil.ignore_patterns("review", "packet-*"))
    (troot / "content/FY3/fy3-2/inquiry.json").unlink()
    env = {**os.environ, "FYSIIKKALABRA_ROOT": tmp}
    r = subprocess.run([PY, ROOT / "scripts/build.py", "fy3-2"], capture_output=True, text=True, cwd=ROOT, env=env)
    classic = (troot / "preview/fy3-2.html").read_text() if r.returncode == 0 else ""
    check("classic lesson builds", r.returncode == 0, (r.stdout + r.stderr)[-300:])
    check("classic lesson keeps its layout", '<article id="teoria">' in classic and 'class="stage"' not in classic and 'inquiry.js' not in classic
          and '<a href="#teoria">Teoria</a><a href="#sim">Simulaatio</a><a href="#exercises">Tehtävät</a><a href="#exit">Lähtölippu</a>' in classic
          and '<section id="sim"><h2>Simulaatio</h2>' in classic and classic.index('<section id="sim">') < classic.index('<h2>Esimerkki</h2>'))

# a broken inquiry.json fails the build with the field named
with tempfile.TemporaryDirectory() as tmp:
    bad = pathlib.Path(tmp) / "content/FY3/fy3-2"; shutil.copytree(folder, bad)
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
check("theory sections placed once", page_html.count('class="theory-h">Ydinajatus') == 1 and page_html.count('class="theory-h">Esimerkki') == 1)
check("unplaced sections land in Selitä", page_html.index('class="theory-h">Tiivistelmä') < page_html.index('id="sovella"'))
check("exercises and exit ticket kept (5/4/3, 3 items)", page_html.count('class="level"') == 3 and page_html.count("<li>Nostat 10") == 1 and '<span class="count">5 tehtävää' in page_html and '<span class="count">3 tehtävää' in page_html)
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

    # prediction: commit first, no feedback until the experiment has two measurements
    p1 = pg.locator("#pred-1")
    p1.locator("button.commit").click(); check("empty commit asks for a choice", "Valitse" in p1.locator("output").inner_text())
    w1 = int(p1.locator("input[data-correct='0']").first.get_attribute("value"))   # a wrong option; options are shown shuffled
    p1.locator("input[type=radio]").nth(w1).check(); p1.locator(".justify textarea").fill("voima sama")
    p1.locator("button.commit").click()
    check("prediction committed: radios locked, feedback hidden", p1.locator("input[type=radio]").nth(w1).is_disabled() and not p1.locator(".feedback").nth(w1).is_visible() and p1.locator(".pending").is_visible())

    ex1 = pg.locator("#exp-1")
    check("record disabled before the initial state is set", ex1.locator(".exp-record").is_disabled())
    ex1.locator(".exp-start").click(); pg.wait_for_timeout(150)
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
    check("prediction feedback revealed after two measurements", p1.locator(".feedback").nth(w1).is_visible() and "Ei aivan" in p1.locator("output").inner_text() and not p1.locator(".pending").is_visible())
    ex1.locator(".exp-reset").click(); pg.wait_for_timeout(120)
    st = pg.evaluate("window.simState"); locked = pg.evaluate("[...document.querySelectorAll('#sim-root input[type=range]')].map(r => r.disabled)")
    check("reset restores defaults, unlocks, clears the table", st["s"] == 10 and st["u"] == 0 and locked == [False, False, False] and ex1.locator(".exp-table tbody tr").count() == 0, f"{st} {locked}")

    # reflection shows the stored prediction and its outcome
    refl = pg.locator("#reflect .my-predictions li")
    check("reflection lists three predictions", refl.count() == 3)
    check("reflection shows my prediction and the verdict", "Ennustit" in refl.nth(0).inner_text() and "ei tue" in refl.nth(0).inner_text() and "Et ole vielä" in refl.nth(1).inner_text(), refl.nth(0).inner_text())

    # plain choice: feedback after Vastaa, may change and re-check
    c = pg.locator("#pr-paino"); w = c.locator("label").filter(has=pg.get_by_text("10 N", exact=True))   # the mass-for-weight option
    wv = w.locator("input").get_attribute("value"); w.locator("input").check(); c.locator("button.commit").click()
    check("retrieval choice gives misconception feedback", c.locator(f".feedback[data-for='{wv}']").is_visible() and "Massa ja paino" in c.locator(f".feedback[data-for='{wv}']").inner_text())
    c.locator("input[data-correct='1']").check(); check("changing the choice hides old feedback", not c.locator(f".feedback[data-for='{wv}']").is_visible())
    c.locator("button.commit").click(); check("correct choice marked", "Oikein" in c.locator("output").inner_text())

    # numeric: comma, invalid, mistake feedback, retries, hints progressive
    n = pg.locator("#siirto"); inp = n.locator("form.check input"); out = n.locator("form.check output")
    inp.fill("abc"); n.locator("form.check button").click(); check("invalid input asks for a number", "Kirjoita luku" in out.inner_text())
    inp.fill("9,6"); n.locator("form.check button").click(); check("common mistake gets its feedback", "Jaoit voiman" in out.inner_text(), out.inner_text())
    inp.fill("1e400"); n.locator("form.check button").click(); check("non-finite input does not crash", not errors and out.inner_text() != "", str(errors[:1]))
    inp.fill("240,0"); n.locator("form.check button").click(); check("decimal comma accepted", "Oikein" in out.inner_text())
    inp.fill("0,24"); n.locator("form.check button").click(); check("after a correct answer a later mistake does not override", "Oikein" in out.inner_text() or "kilowat" in out.inner_text())
    hints = n.locator(".hints details")
    check("only the first hint offered at first", hints.nth(0).is_visible() and not hints.nth(1).is_visible())
    hints.nth(0).locator("summary").click(); pg.wait_for_timeout(80); check("second hint appears after the first is opened", hints.nth(1).is_visible() and not hints.nth(2).is_visible())
    n2 = pg.locator("#check-2"); i2 = n2.locator("form.check input"); o2 = n2.locator("form.check output")
    i2.fill("100"); n2.locator("form.check button").click(); i2.fill("100"); n2.locator("form.check button").click()
    check("second wrong try points to the solution", "Ei vielä" in o2.inner_text() or "Vastaus" in o2.inner_text(), o2.inner_text())

    # explanation: model answer and criteria on request
    ex = pg.locator("#check-3"); ex.locator("textarea").fill("Työ ei riipu ajasta."); check("model answer hidden until asked", not ex.locator(".model").is_visible())
    ex.locator(".show-model").click(); check("model answer and criteria shown", ex.locator(".model").is_visible() and ex.locator("ul.criteria input[type=checkbox]").count() == 4)

    # persistence survives a reload (per-device convenience only)
    pg.reload(); pg.wait_for_function("window.simState && window.simAdapter", timeout=3000)
    check("prediction remembered after reload", pg.locator("#pred-1 input[type=radio]").nth(w1).is_checked() and pg.locator("#pred-1 input[type=radio]").nth(w1).is_disabled())
    check("explanation remembered after reload", "Työ ei riipu" in pg.locator("#check-3 textarea").input_value())

    # keyboard: a choice answered with arrows and Enter
    pg.evaluate("try { localStorage.clear() } catch (e) {}"); pg.reload(); pg.wait_for_function("window.simState", timeout=3000)
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
    pg.locator("#exp-2 .exp-start").click(); pg.locator("#exp-2 .exp-record").click(); pg.wait_for_timeout(50)
    check("experiment works at 360 px", pg.locator("#exp-2 .exp-table tbody tr").count() == 1)
    pg.close()
    b.close()

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
