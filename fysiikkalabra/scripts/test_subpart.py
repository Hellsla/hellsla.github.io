"""Part feedback of a multi-part task (work queue 29.9). Usage: python scripts/test_subpart.py   (after build.py fy4-10 fy8-13)
In preview/: fy4-10-L2-06 (fi, fi-easy, en) says which part was accepted and what to compare with the model solution; a second
course's task (fy8-13-L2-05) does the same; a single-part task (fy4-10-L2-01) says only "Oikein."; a wrong answer says no part.
Also the unit of scripts/subpart.py. Exit status 1 on any failure."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
import subpart
from playwright.sync_api import sync_playwright

fails = 0


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


expect("no box sentence: unchanged", subpart.info("a) x\n\nb) y") is None)
expect("one part: unchanged", subpart.info("a) x\n\nVastauslaatikkoon tulee kohdan a) tulos.") is None)
expect("en box sentence, graph", subpart.info("a) Draw the graph.\n\nb) Find x.\n\nThe answer box takes the result of part b).") == {"part": "b", "compare": [("a", "graph")]})

P = ROOT / "preview"
CASES = [(P / "fy4-10.html", "fy4-10-L2-06", "46,7", "C-kohdan lukuarvo on oikein. Vertaa vielä b-kohdan perusteluasi malliratkaisuun."),
         (P / "fi-easy/fy4-10.html", "fy4-10-L2-06", "46,7", "C-kohdan luku on oikein. Katso vielä B-kohdan perustelu. Vertaa sitä malliratkaisuun."),
         (P / "en/fy4-10.html", "fy4-10-L2-06", "46.7", "The number in part C is correct. Now compare your reasoning in part b with the model solution."),
         (P / "fy8-13.html", "fy8-13-L2-05", None, "B-kohdan lukuarvo on oikein. Vertaa vielä a-kohtaa malliratkaisuun."),
         (P / "fy4-10.html", "fy4-10-L2-01", None, "Oikein.")]
with sync_playwright() as pw:
    b = launch(pw)
    for page, tid, typed, want in CASES:
        pg = b.new_page(viewport={"width": 1000, "height": 900}); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(page.as_uri()); pg.evaluate("document.querySelectorAll('details').forEach(d => { d.open = true; })")
        if typed is None: typed = pg.eval_on_selector(f"#{tid} form.check", "f => f.dataset.answer").replace(".", ",")
        pg.fill(f"#{tid} form.check input", typed); pg.click(f"#{tid} form.check button")
        got = pg.eval_on_selector(f"#{tid} form.check output", "o => o.textContent.trim()")
        expect(f"{page.parent.name}/{tid} {typed}", got == want or got == want.replace("B-kohdan", "b-kohdan"), f"got {got!r}")
        if tid == "fy4-10-L2-06":
            pg.fill(f"#{tid} form.check input", "12"); pg.click(f"#{tid} form.check button")
            got = pg.eval_on_selector(f"#{tid} form.check output", "o => o.textContent.trim()")
            expect(f"{page.parent.name}/{tid} wrong answer names no part", "kohdan" not in got.split(".")[0] and "part" not in got, got)
        expect("no page errors", not errs, "; ".join(errs))
        pg.close()
    b.close()
print("ok" if not fails else f"{fails} failure(s)")
sys.exit(1 if fails else 0)
