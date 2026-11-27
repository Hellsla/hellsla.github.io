"""Exact answer check of whole-number answers (work queue 29.1, teacher's change list 2026-11-27 item 1; templates/virhe.js `exact`).
Usage: python scripts/test_tarkka.py

An exercise or an inquiry task with "exact": true accepts only its answer (a mass number, an atomic number, a number of neutrons,
the order of a diffraction maximum); the shared check's 2 % band, half a unit and "Lähellä" do not apply to it.
  1. data (no browser): `exact` is true only on a whole-number answer; every exact task is exact in every language of
     the lesson and the languages agree on `answer`; fy8-8-L1-02 has its own feedback for 222 in every language
  2. the page (Playwright, on the built fy8-8 and fy7-13 in fi, fi-easy and en): 218 is accepted, 217, 219 and 222 are not
     (222 shows the task's hint, 217 and 219 are never "Lähellä"); fy7-13-L1-08: 4 is accepted, 3 and 5 are not; a task
     that is not exact (fy8-8-L2-03) keeps its band
Exit status 1 on any failure."""
import json, pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
from _browser import launch
from playwright.sync_api import sync_playwright

fails = 0
LANGS = ("fi", "fi-easy", "en")
HINT = {"fi": "Kuinka monta nukleonia emoytimestä poistuu alfahiukkasen mukana?", "en": "How many nucleons leave the parent nucleus with the alpha particle?"}


def expect(name, ok, detail=""):
    global fails
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"\n     {detail}"))
    fails += not ok


def tasks(path):
    out = {}
    def walk(o):
        if isinstance(o, dict):
            if "answer" in o and o.get("id") is not None: out[o["id"]] = o
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    if path.is_file(): walk(json.loads(path.read_text()))
    return out


def data():
    exact = {}
    for f in sorted((ROOT / "content/fi").glob("*/*/exercises/exercises.json")) + sorted((ROOT / "content/fi").glob("*/*/inquiry.json")):
        rel = f.relative_to(ROOT / "content/fi")
        per = {l: tasks(ROOT / "content" / l / rel) for l in LANGS}
        for tid, t in per["fi"].items():
            flags = {l: bool(per[l].get(tid, {}).get("exact")) for l in LANGS}
            if any(flags.values()):
                exact[tid] = t
                expect(f"{tid}: exact in every language", all(flags.values()), str(flags))
                expect(f"{tid}: the same whole-number answer in every language", all(per[l][tid]["answer"] == t["answer"] and float(t["answer"]) == int(t["answer"]) and not isinstance(t["answer"], bool) for l in LANGS if tid in per[l]))
    expect("there are exact tasks", len(exact) >= 20, str(len(exact)))
    for l in LANGS:
        m = tasks(ROOT / "content" / l / "FY8/fy8-8/exercises/exercises.json").get("fy8-8-L1-02", {}).get("mistakes") or []
        expect(f"fy8-8-L1-02 ({l}) has feedback for 222", any(x.get("value") == 222 and x.get("feedback") for x in m), str(m))
    fi = {x["value"]: x["feedback"] for x in tasks(ROOT / "content/fi/FY8/fy8-8/exercises/exercises.json")["fy8-8-L1-02"]["mistakes"]}
    expect("fy8-8-L1-02 (fi) hint is the teacher's wording", fi.get(222) == HINT["fi"], str(fi))
    expect("fy8-8-L1-02 (en) hint", {x["value"]: x["feedback"] for x in tasks(ROOT / "content/en/FY8/fy8-8/exercises/exercises.json")["fy8-8-L1-02"]["mistakes"]}.get(222) == HINT["en"])


def state(pg, tid, typed):
    sel = f"#{tid} form.check"
    pg.evaluate("() => document.querySelectorAll('details').forEach((d) => { d.open = true; })")
    pg.fill(sel + " input", typed); pg.click(sel + " button[type=submit]")
    return pg.eval_on_selector(sel + " output", "(o) => [o.dataset.state, o.textContent.trim()]")


def pages():
    for lid in ("fy8-8", "fy7-13"):
        r = subprocess.run([sys.executable, str(ROOT / "scripts/build.py"), lid], cwd=ROOT, capture_output=True, text=True)
        expect(f"build.py {lid}", r.returncode == 0, r.stderr[-400:])
    with sync_playwright() as pw:
        b = launch(pw)
        for lang in LANGS:
            base = ROOT / "preview" / ("" if lang == "fi" else lang)
            pg = b.new_page(); errors = []
            pg.on("pageerror", lambda e: errors.append(str(e)))
            pg.goto((base / "fy8-8.html").as_uri()); pg.evaluate("try { localStorage.clear() } catch (e) {}"); pg.goto((base / "fy8-8.html").as_uri())
            for typed, want in (("218", "ok"), ("218,0", "ok"), ("217", "no"), ("219", "no"), ("222", "no"), ("221", "no"), ("2,18e2", "ok")):
                st, txt = state(pg, "fy8-8-L1-02", typed)
                expect(f"{lang} fy8-8-L1-02: {typed} is {want}", st == want, f"{st} {txt!r}")
            st, txt = state(pg, "fy8-8-L1-02", "222")
            want_hint = tasks(ROOT / "content" / lang / "FY8/fy8-8/exercises/exercises.json")["fy8-8-L1-02"]["mistakes"][0]["feedback"]
            expect(f"{lang} fy8-8-L1-02: 222 shows the task's hint", txt == want_hint, txt)
            st, txt = state(pg, "fy8-8-L1-02", "217")
            expect(f"{lang} fy8-8-L1-02: 217 shows no hint", "nukleon" not in txt and "nucleon" not in txt, txt)
            for typed, want in (("143", "ok"), ("142", "no"), ("144", "no"), ("140", "no"), ("145", "no")):
                expect(f"{lang} fy8-8-L1-01: {typed} is {want}", state(pg, "fy8-8-L1-01", typed)[0] == want)
            expect(f"{lang} fy8-8-L2-03 (not exact): 295000 stays accepted", state(pg, "fy8-8-L2-03", "295000")[0] == "ok")
            expect(f"{lang} fy8-8 has no script errors", not errors, "; ".join(errors))
            pg.close()
            pg = b.new_page(); pg.goto((base / "fy7-13.html").as_uri()); pg.evaluate("try { localStorage.clear() } catch (e) {}"); pg.goto((base / "fy7-13.html").as_uri())
            for typed, want in (("4", "ok"), ("3", "no"), ("5", "no"), ("4,0", "ok"), ("4,05", "no")):
                expect(f"{lang} fy7-13-L1-08: {typed} is {want}", state(pg, "fy7-13-L1-08", typed)[0] == want)
            pg.close()
        b.close()


data()
pages()
print("ok" if not fails else f"{fails} failure(s)")
sys.exit(1 if fails else 0)
