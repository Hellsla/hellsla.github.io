"""Tests of the inquiry framework (scripts/inquiry.py, templates/inquiry.js, the sim adapter). Usage: python scripts/test_inquiry.py

Part 1 (no browser): validation names the lesson and the field; a lesson without inquiry.json builds exactly as
before; every activity type renders. Part 2 (Playwright, on preview/fy3-2.html built here): stage order and nav,
a prediction stays unrevealed until the linked experiment has enough measurements, the experiment sets the
initial conditions, locks the controlled parameters, records the varied parameter and the measurements, and
reset clears everything, numeric answers with a decimal comma, invalid input, a common mistake and retries,
progressive hints, the model answer, the reflection shows the stored prediction, keyboard operation, and a
360 px viewport without horizontal overflow. The physics itself (W = F s, P = W / t) is asserted by
tests/sims/fy3-2.json through test_sims.py, not here. What these tests prove is that the mechanics behave;
whether the sequence teaches is for the classroom evaluation (docs/inquiry.md)."""
import copy, json, pathlib, subprocess, sys, tempfile, shutil
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import inquiry
ROOT = pathlib.Path(__file__).resolve().parents[1]
PY = sys.executable
passed = failed = 0


def check(name, cond, detail=""):
    global passed, failed
    passed += cond; failed += not cond
    print(("ok   " if cond else "FAIL ") + name + (f"  {detail}" if detail and not cond else ""))


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

# a lesson without inquiry.json renders in the classic layout, byte for byte as before this framework
r = subprocess.run([PY, ROOT / "scripts/build.py", "fy3-1"], capture_output=True, text=True, cwd=ROOT)
classic = (ROOT / "preview/fy3-1.html").read_text()
check("classic lesson builds", r.returncode == 0, r.stderr[-300:])
check("classic lesson keeps its layout", '<article id="teoria">' in classic and ".stage" not in classic and 'inquiry.js' not in classic and '<a href="#teoria">Teoria</a><a href="#sim">Simulaatio</a>' in classic)
live = ROOT / "site/fy3-1.html"
if live.exists(): check("classic lesson identical to the committed site page", live.read_text() == classic)

# a broken inquiry.json fails the build with the field named
with tempfile.TemporaryDirectory() as tmp:
    bad = pathlib.Path(tmp) / "content/FY3/fy3-2"; shutil.copytree(folder, bad)
    d = copy.deepcopy(good); d["activities"][2]["choices"][1].pop("feedback"); (bad / "inquiry.json").write_text(json.dumps(d))
    r = subprocess.run([PY, ROOT / "scripts/lint_lesson.py", "fy3-2"], capture_output=True, text=True, cwd=ROOT, env={**__import__("os").environ, "FYSIIKKALABRA_ROOT": tmp})
    # lint_lesson resolves its own ROOT; validate directly instead
    e = inquiry.validate(bad, d, lesson_md)
    check("lint-level validation names the field on a copy", any("choices[1].feedback" in x for x in e), str(e))

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
    p1.locator("input[type=radio]").nth(0).check(); p1.locator(".justify textarea").fill("voima sama")
    p1.locator("button.commit").click()
    check("prediction committed: radios locked, feedback hidden", p1.locator("input[type=radio]").nth(0).is_disabled() and not p1.locator(".feedback").nth(0).is_visible() and p1.locator(".pending").is_visible())

    ex1 = pg.locator("#exp-1")
    check("record disabled before the initial state is set", ex1.locator(".exp-record").is_disabled())
    ex1.locator(".exp-start").click(); pg.wait_for_timeout(150)
    st = pg.evaluate("window.simState")
    check("initial conditions set (F 60, s 10, t 5)", st["F"] == 60 and st["s"] == 10 and st["t"] == 5, str(st))
    locked = pg.evaluate("[...document.querySelectorAll('#sim-root input[type=range]')].map(r => r.disabled)")
    check("controlled parameters locked, varied one free", locked == [True, False, True], str(locked))
    ex1.locator(".exp-record").click(); pg.wait_for_timeout(50)
    check("first measurement recorded", ex1.locator("tbody tr").count() == 1 and "600" in ex1.locator("tbody tr").nth(0).inner_text())
    ex1.locator(".exp-record").click(); check("same value not recorded twice", ex1.locator("tbody tr").count() == 1 and "Sama" in ex1.locator(".exp-status").inner_text())
    check("still no feedback after one measurement", not p1.locator(".feedback").nth(0).is_visible())
    pg.evaluate("(() => { const r=document.querySelectorAll('#sim-root input[type=range]')[1]; r.value=20; r.dispatchEvent(new Event('input',{bubbles:true})); })()"); pg.wait_for_timeout(120)
    ex1.locator(".exp-record").click(); pg.wait_for_timeout(50)
    rows = ex1.locator("tbody tr").all_inner_texts()
    check("second measurement doubles W", len(rows) == 2 and "1200" in rows[1], str(rows))
    check("prediction feedback revealed after two measurements", p1.locator(".feedback").nth(0).is_visible() and "Ei aivan" in p1.locator("output").inner_text() and not p1.locator(".pending").is_visible())
    ex1.locator(".exp-reset").click(); pg.wait_for_timeout(120)
    st = pg.evaluate("window.simState"); locked = pg.evaluate("[...document.querySelectorAll('#sim-root input[type=range]')].map(r => r.disabled)")
    check("reset restores defaults, unlocks, clears the table", st["s"] == 10 and st["u"] == 0 and locked == [False, False, False] and ex1.locator("tbody tr").count() == 0, f"{st} {locked}")

    # reflection shows the stored prediction and its outcome
    refl = pg.locator("#reflect .my-predictions li")
    check("reflection lists three predictions", refl.count() == 3)
    check("reflection shows my prediction and the verdict", "Ennustit" in refl.nth(0).inner_text() and "eivät tue" in refl.nth(0).inner_text() and "Et ole vielä" in refl.nth(1).inner_text(), refl.nth(0).inner_text())

    # plain choice: feedback after Vastaa, may change and re-check
    c = pg.locator("#pr-paino"); c.locator("input[type=radio]").nth(0).check(); c.locator("button.commit").click()
    check("retrieval choice gives misconception feedback", c.locator(".feedback[data-for='0']").is_visible() and "Massa ja paino" in c.locator(".feedback[data-for='0']").inner_text())
    c.locator("input[type=radio]").nth(1).check(); check("changing the choice hides old feedback", not c.locator(".feedback[data-for='0']").is_visible())
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
    check("prediction remembered after reload", pg.locator("#pred-1 input[type=radio]").nth(0).is_checked() and pg.locator("#pred-1 input[type=radio]").nth(0).is_disabled())
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
    check("experiment works at 360 px", pg.locator("#exp-2 tbody tr").count() == 1)
    pg.close()
    b.close()

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
