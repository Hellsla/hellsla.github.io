"""The class summary of the grading page (work queue 17e, K8; palautus/apps-script/Code.gs rlClass, Review.html renderClass).
Usage: python scripts/test_luokka.py   (needs no built site: the generated palautus/apps-script/Tehtavat.gs and Virhe.gs)

In a browser, on Review.html with the test mock of Google's services (palautus/test/gas-mock.js) and made-up submissions:
  - rlClass counts per chapter: who returned, who answered, the points given (0 p, part, full) and their mean, the weakest task first
  - a typed number is judged with the lesson page's own rule (virhe.js window.flJudge): ok, close, wrong, and the common mistake of a
    wrong one (sign, order of magnitude)
  - the goals: the numbers of each self-assessment level a-d, x and not answered
  - no e-mail, name or submission id anywhere in the result or the view (K8: the view can be shown to the class)
  - an old row of the sheet without the new column reads as no numbers; without the rule (no Virhe.gs) no number table, nothing else changes
  - rlValidate_ keeps a task's single typed number for the sheet and nothing else of it
  - the view: the weakest tasks first, the cap and the button that shows all, the chapter range, the table of numbers
With LUOKKA_SHOTS=<folder> the test saves screenshots of the section (wide, 360 px) and of the page at 360 px.
Exit status 1 on any failure."""
import json, os, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

GAS = ROOT / "palautus/apps-script"
fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


# the made-up group, built in the page from the course's own tasks (Tehtavat.gs): five students returned the first chapter that has two
# typed-number tasks; the sixth returned nothing
SETUP = r"""() => {
  const ch = RL_COURSE.chapters.find((c) => c.tasks.filter((t) => t.checks && t.checks.length === 1 && !t.lesson).length >= 2 && (c.self || []).length >= 2);
  const nums = ch.tasks.filter((t) => t.checks && t.checks.length === 1 && !t.lesson);
  const [T1, T2] = nums;
  const P = ch.tasks.find((t) => t.choice && !t.lesson);   // a task with one choice (17e PR 2)
  const pc = P.choice.correct[0], pw = (pc + 1) % P.choice.options.length;
  const people = ['a', 'b', 'c', 'd', 'e'].map((k) => k + '.opiskelija@koulu.example');
  const head = RL_SUB_HEAD.slice();
  MOCK.addSheet(RL_CONFIG.SUBMISSIONS_SHEET, [head]);
  MOCK.addSheet(RL_CONFIG.SCORES_SHEET, [RL_SCORE_HEAD.slice()]);
  const sub = MOCK.sheet(RL_CONFIG.SUBMISSIONS_SHEET), sc = MOCK.sheet(RL_CONFIG.SCORES_SHEET);
  const a1 = T1.checks[0].answer, a2 = T2.checks[0].answer;
  // typed values: T1 right, close (3 %), minus sign, ×1000, twice; T2 right, right, right, right, right
  const v1 = [String(a1), String(a1 * 1.03), String(-a1), String(a1 * 1000), String(a1 * 2)], v2 = [a2, a2, a2, a2, a2].map(String);
  const self = ['tavoite-1=a,tavoite-2=d', 'tavoite-1=a,tavoite-2=c', 'tavoite-1=b', 'tavoite-1=x,tavoite-2=x', ''];
  people.forEach((email, i) => {
    const subId = String(i).repeat(32);
    const row = RL_SUB_HEAD.map(() => '');
    row[RL_C.key] = 'k' + i; row[RL_C.time] = new Date(2026, 10, 5, 8, i); row[RL_C.email] = email; row[RL_C.sub] = subId; row[RL_C.status] = RL_STATUS.OK;
    row[RL_C.answered] = T1.id + ',' + T2.id + ',' + P.id; row[RL_C.chapter] = ch.id; row[RL_C.self] = self[i];
    row[RL_C.numbers] = i === 4 ? '' : JSON.stringify({ [T1.id]: v1[i], [T2.id]: v2[i] });   // student e: an old row without numbers
    row[RL_C.choices] = JSON.stringify({ [P.id]: [pc, pc, pw, pc, 0][i] });                  // choices: right, right, wrong, right
    if (i === 4) row.length = RL_C.numbers;                                                  // ... and without the column at all (nor the choices column)
    sub.data.push(row);
    // points: T1 1, 1, 0,5, 0, (not graded); T2 0, 0, 0,5, 0, 0
    const p1 = [1, 1, 0.5, 0, ''][i], p2 = [0, 0, 0.5, 0, 0][i];
    [[T1, p1], [T2, p2]].forEach(([t, p]) => { const r = RL_SCORE_HEAD.map(() => ''); r[RL_S.key] = rlScoreKey_(email, subId, t.id); r[RL_S.email] = email; r[RL_S.sub] = subId; r[RL_S.task] = t.id; r[RL_S.points] = p; sc.data.push(r); });
  });
  return { p: P.id, pc, pw, pn: P.choice.options.length, pnumber: P.number, chapter: ch.id, t1: T1.id, t2: T2.id, a1, a2, unit: T1.checks[0].unit, number1: T1.number, number2: T2.number };
}"""


def main():
    head = "".join(f"<script>{(GAS.parent / 'test/gas-mock.js' if n == 'mock' else GAS / n).read_text()}</script>" for n in ["mock", "Tehtavat.gs", "Virhe.gs", "Code.gs"])
    with sync_playwright() as pw:
        b = launch(pw)
        pg = b.new_page(viewport={"width": 1280, "height": 900})
        errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.set_content("<!doctype html><html><head>" + head + "</head><body></body></html>")
        info = pg.evaluate(SETUP)
        res = pg.evaluate("() => rlClass()")
        expect("rlOverview carries the same summary (the page reads the sheets once)", pg.evaluate("(r) => JSON.stringify(rlOverview().cls) === JSON.stringify(r)", res))
        ch = next(c for c in res["chapters"] if c["id"] == info["chapter"])
        t1 = next(t for t in ch["tasks"] if t["id"] == info["t1"]); t2 = next(t for t in ch["tasks"] if t["id"] == info["t2"])
        expect("the rule is the lesson page's own (Virhe.gs)", res["judged"] is True and res["maxPoints"] == 1)
        expect("returned and answered", ch["returned"] == 5 and t1["returned"] == 5 and t1["answered"] == 5 and t2["answered"] == 5, (ch["returned"], t1))
        expect("points given: 0 p, part, full, and the mean of the graded ones; the ungraded one is left out", t1["dist"] == {"zero": 1, "part": 1, "full": 2} and t1["scored"] == 4 and t1["avg"] == 0.63, t1)
        expect("a task with no points above zero has mean 0", t2["avg"] == 0.1 and t2["dist"]["zero"] == 4 and t2["dist"]["part"] == 1, t2)
        tp = next(t for t in ch["tasks"] if t["id"] == info["p"])
        want = [0] * info["pn"]; want[info["pc"]] = 3; want[info["pw"]] += 1
        expect("choices: the number of each option, the old row has none; the correct options come from Tehtavat.gs",
               tp["pick"]["answered"] == 4 and tp["pick"]["n"] == want and tp["pick"]["correct"] == [info["pc"]] and len(tp["pick"]["options"]) == info["pn"], tp.get("pick"))
        expect("a task with no choice part has no distribution", "pick" not in t1, t1.get("pick"))
        n1 = t1["num"]
        expect("the number judged by the page's rule: right, close, wrong; the old row has no number", n1["answered"] == 4 and n1["ok"] == 1 and n1["close"] == 1 and n1["wrong"] == 2, n1)
        expect("the wrong numbers' common mistakes: the sign and the order of magnitude", n1["mistakes"] == {"sign": 1, "magnitude": 1, "time": 0, "kelvin": 0}, n1["mistakes"])
        expect("a task everyone got right has no wrong", t2["num"]["ok"] == 4 and t2["num"]["wrong"] == 0 and t2["num"]["answered"] == 4, t2["num"])
        g = {x["id"]: x["n"] for x in ch["goals"]}
        expect("goals: the number of each level, x and not answered, newest submission of each student",
               g["tavoite-1"] == {"a": 2, "b": 1, "c": 0, "d": 0, "x": 1, "none": 1} and g["tavoite-2"] == {"a": 0, "b": 0, "c": 1, "d": 1, "x": 1, "none": 2}, g)
        text = json.dumps(res)
        expect("an option outside the task's options is not counted",
               pg.evaluate("(i) => { const m = rlModel_(); m.students.forEach((s, k) => { s.chapters[i.chapter].forEach((v) => { if (k === 0) v.choices[i.p] = 99; }); }); const c = rlClass_(m).chapters.find((x) => x.id === i.chapter).tasks.find((x) => x.id === i.p); return c.pick.answered; }", info) == 3)
        expect("no e-mail, no submission id in the result (K8)", "@" not in text and "opiskelija" not in text and "00000000" not in text, [w for w in ("@", "opiskelija") if w in text])
        # without the rule (the Apps Script copy without Virhe.gs): no number table, the rest as before
        no = pg.evaluate("() => { const f = window.flJudge; window.flJudge = undefined; try { return rlClass(); } finally { window.flJudge = f; } }")
        nc = next(c for c in no["chapters"] if c["id"] == info["chapter"])
        expect("without the rule there is no table of numbers and nothing else changes", no["judged"] is False and all("num" not in t for t in nc["tasks"]) and nc["tasks"][0]["dist"] == ch["tasks"][0]["dist"], no["judged"])
        # the sheet keeps the single typed number of a task (rlValidate_), nothing else of it
        v = pg.evaluate("""(i) => {
          const ch = RL_COURSE.chapters.find((c) => c.id === i.chapter);
          const answers = ch.tasks.map((t) => t.id === i.t1 ? { task: t.id, status: 'answered', content: [], responses: [{ type: 'number', value: '6,0', unit: 'cm' }] }
            : t.id === i.p ? { task: t.id, status: 'answered', content: [], responses: [{ type: 'choice', question: 'k', answer: 'v', option: i.pw }, { type: 'text', label: 'p', text: 'koska' }] } : { task: t.id, status: 'empty', content: [], responses: [] });
          const goals = (ch.self || []).map((s) => ({ id: s.id, text: '', level: null }));
          const r = rlValidate_({ format: RL_FORMAT, version: 3, chapter: i.chapter, submission_id: 'f'.repeat(32), answers, selfassessment: { goals } }, true, true);
          return { numbers: r.numbers, cell: rlNumbersParse_(r.numbers), choices: r.choices, picked: rlChoicesParse_(r.choices) };
        }""", info)
        expect("rlValidate_ gives the sheet the task's number as typed, JSON by task id", v["numbers"] == json.dumps({info["t1"]: "6,0"}, separators=(",", ":")) and v["cell"][info["t1"]] == "6,0", v)
        expect("rlValidate_ gives the sheet the task's choice as the option's place on the page, nothing else of it", v["choices"] == json.dumps({info["p"]: info["pw"]}, separators=(",", ":")) and v["picked"][info["p"]] == info["pw"], v)
        # a task whose English page shows the options in another order (Tehtavat.gs choice.skip_en) takes no English choice; a Finnish file counts it
        skip = pg.evaluate("""(i) => { const ch = RL_COURSE.chapters.find((c) => c.id === i.chapter), t = ch.tasks.find((x) => x.id === i.p), was = t.choice.skip_en; t.choice.skip_en = true;
          const run = (lang) => { const answers = ch.tasks.map((x) => x.id === i.p ? { task: x.id, status: 'answered', content: [], responses: [{ type: 'choice', question: 'k', answer: 'v', option: 0 }] } : { task: x.id, status: 'empty', content: [], responses: [] });
            return rlValidate_({ format: RL_FORMAT, version: 3, chapter: i.chapter, lang, submission_id: 'f'.repeat(32), answers, selfassessment: { goals: (ch.self || []).map((s) => ({ id: s.id, text: '', level: null })) } }, true, true).choices; };
          const out = [run('en'), run('fi')]; if (was === undefined) delete t.choice.skip_en; else t.choice.skip_en = was; return out; }""", info)
        expect("a task whose English options stand in another order takes no English choice", skip == ["{}", json.dumps({info["p"]: 0}, separators=(",", ":"))], skip)
        expect("a damaged or foreign choices cell reads as no choices", pg.evaluate("() => [rlChoicesParse_('{'), rlChoicesParse_('[1]'), rlChoicesParse_('{\"a b\":1}'), rlChoicesParse_('{\"x\":\"1\"}'), rlChoicesParse_('{\"x\":-1}'), rlChoicesParse_('{\"x\":99}')].map((o) => Object.keys(o).length)") == [0] * 6)
        expect("a damaged or foreign cell reads as no numbers", pg.evaluate("() => [rlNumbersParse_('{'), rlNumbersParse_('[1]'), rlNumbersParse_('{\"a b\":\"1\"}'), rlNumbersParse_('{\"x\":5}')].map((o) => Object.keys(o).length)") == [0, 0, 0, 0])

        # the view
        pg.set_content((GAS / "Review.html").read_text().replace("<head>", "<head>" + head + "<script>(" + SETUP + ")(); RL_CONFIG.SUBMISSION_FOLDER_ID = 'x';</script>", 1))
        pg.wait_for_selector("#classTasks tbody tr")
        expect("the section is shown with its three tables", pg.is_visible("#classSec") and pg.is_visible("#classTasks") and pg.is_visible("#classGoals") and pg.is_visible("#classNums"))
        rows = pg.evaluate("[...document.querySelectorAll('#classTasks tbody tr')].map((r) => [...r.cells].map((c) => c.textContent.trim()))")
        expect("the weakest task first: its mean is the smallest", rows[0][0] == "Tehtävä " + info["number2"] and rows[0][4] == "0,1 / 1" and rows[1][0] == "Tehtävä " + info["number1"] and rows[1][4] == "0,63 / 1", rows[:3])
        expect("returned and answered as numbers", rows[0][1:3] == ["5", "5"], rows[0])
        stack = pg.evaluate("[...document.querySelectorAll('#classTasks tbody tr')[1].querySelectorAll('.stack > span')].map((s) => [s.className, s.textContent])")
        expect("the points' bar: 0 p, part, full in the self-assessment colours", stack == [["sa sa-d", "1"], ["sa sa-c", "1"], ["sa sa-a", "2"]], stack)
        nums = pg.evaluate("[...document.querySelectorAll('#classNums tbody tr')].map((r) => [...r.cells].map((c) => c.textContent.trim()))")
        expect("numbers: the task with most wrong first, with its common mistakes in words", nums and nums[0][0] == "Tehtävä " + info["number1"] and "etumerkki 1" in nums[0][3] and "kertaluokka 1" in nums[0][3], nums[:2])
        expect("the view shows no e-mail, name or submission id", "@" not in pg.inner_text("#classSec") and "opiskelija" not in pg.inner_text("#classSec"), pg.inner_text("#classSec")[:200])
        card = pg.evaluate("(i) => { const c = document.querySelector('#classPicks .pick[data-task=\"' + i.p + '\"]'); return c && { h: c.querySelector('h4').textContent, q: c.querySelector('.q').textContent.trim(), ok: [...c.querySelectorAll('.opt.ok')].length, n: [...c.querySelectorAll('.opt .n')].map((x) => x.textContent), okAt: [...c.querySelectorAll('.opt')].findIndex((x) => x.classList.contains('ok')) }; }", info)
        wantn = [str(x) for x in want]
        expect("the choices: a box for the task with its options' numbers, the correct one marked", card and card["n"] == wantn and card["ok"] == 1 and card["okAt"] == info["pc"] and card["h"] == "Tehtävä " + info["pnumber"] and card["q"], card)
        expect("the choices have no e-mail or name either", "@" not in pg.inner_text("#classPickSec") and "opiskelija" not in pg.inner_text("#classPickSec"))
        pg.set_viewport_size({"width": 360, "height": 800})
        wide = pg.evaluate("""() => [...document.querySelectorAll('#classSec *')].filter((e) => !e.closest('.wide') && e.getBoundingClientRect().right > innerWidth + 1).map((e) => e.tagName + '.' + e.className)
          .concat([...document.querySelectorAll('#classSec .wide')].filter((d) => getComputedStyle(d).overflowX !== 'auto').map(() => 'wide box without scroll'))""")
        expect("at 360 px the section stays inside the screen (a table scrolls inside its own box)", wide == [], wide)
        pg.set_viewport_size({"width": 1280, "height": 900})
        n0 = pg.locator("#classTasks tbody tr").count()
        pg.click("#classAll")
        expect("the button shows every task and back (at most ten otherwise)", n0 <= 10 and pg.locator("#classTasks tbody tr").count() >= n0 and pg.inner_text("#classAll") == "Näytä heikoimmat" and pg.get_attribute("#classAll", "aria-pressed") == "true", (n0, pg.inner_text("#classAll")))
        pg.click("#classAll")
        expect("and back to the weakest", pg.inner_text("#classAll") == "Näytä kaikki" and pg.locator("#classTasks tbody tr").count() == n0)
        goals = pg.evaluate("[...document.querySelectorAll('#classGoals tbody tr')].slice(0, 2).map((r) => [r.cells[0].textContent.slice(0, 12), [...r.querySelectorAll('.stack > span')].map((s) => s.className.replace('sa sa-', '') + s.textContent)])")
        expect("goals: the levels in the order d c b a x and not answered, with their numbers", goals[0][1] == ["b1", "a2", "x1", "none1"] and goals[1][1] == ["d1", "c1", "x1", "none2"], goals)
        expect("no script errors", not errors, errors)
        if os.environ.get("LUOKKA_SHOTS"):
            out = pathlib.Path(os.environ["LUOKKA_SHOTS"]); out.mkdir(parents=True, exist_ok=True)
            for w, name in ((1280, "leveä"), (360, "360")):
                pg.set_viewport_size({"width": w, "height": 900})
                pg.wait_for_timeout(150)
                pg.locator("#classSec").screenshot(path=str(out / f"luokan-yhteenveto-{name}.png"))
        b.close()
    print("FAIL" if fails else "ok", "the class summary")
    sys.exit(1 if fails else 0)


main()
