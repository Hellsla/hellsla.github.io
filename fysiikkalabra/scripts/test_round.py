"""round.py's summary agrees with the commands it runs (work queue 0a). Usage: python scripts/test_round.py

1. parse_carry reads every form of reviews.py carry's lines (carried now, already current, delta/full needed, and a
   reviewer whose scope says delta although its PASS is for the current content).
2. For a published lesson in every language, the reviews round.py calls needed are exactly those reviews.py carry
   and reviews.py status report when run on their own (carry writes nothing for a lesson whose reviews are current).
3. preflight. 4. Course units (work queue 0j): round.py recognises a unit id, parse_item_carry reads reviews.py
   carry-item's lines, and for fy9-liike in every language the reviews round.py calls needed are exactly those
   units.status reports not PASS."""
import pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, round as rnd

ROOT = courses.ROOT
bad = 0
def check(cond, what):
    global bad
    print(("ok   " if cond else "FAIL ") + what); bad += not cond

res, state = rnd.parse_carry(["science: carried over (a calculation chain re-broken into rows)", "pedagogy: already current",
                              "visual: delta review needed", "fy0-1: reviewed (science=PASS (carried over: reflow), pedagogy=PASS, visual=PASS)"])
check(res == {"science": ("none", True), "pedagogy": ("none", False), "visual": ("none", False)}, "parse_carry: a current visual PASS needs no review")
res, _ = rnd.parse_carry(["science: full review needed", "pedagogy: delta review needed", "visual: delta review needed",
                          "fy0-1: draft (science=stale, pedagogy=stale, visual=PASS)"])
check(res == {"science": ("full", False), "pedagogy": ("delta", False), "visual": ("none", False)}, "parse_carry: stale reviews are needed with their mode")

# 3. preflight (work queue 0d): missing packages are named with the install command, a shallow clone is deepened
import unittest.mock as mock
with mock.patch.object(rnd, "missing_packages", return_value=(["markdown"], [])), mock.patch.object(rnd, "shallow", return_value=False):
    check(rnd.preflight() == 1, "preflight: a missing package stops the round")
calls = []
def fake_run(args, **kw):
    calls.append(args); return subprocess.CompletedProcess(args, 0, "", "")
states = iter([True, False])
with mock.patch.object(rnd, "missing_packages", return_value=([], [])), mock.patch.object(rnd, "shallow", side_effect=lambda: next(states)), mock.patch.object(rnd.subprocess, "run", fake_run):
    check(rnd.preflight() == 0 and calls == [["git", "fetch", "--unshallow", "origin"]], "preflight: a shallow clone is deepened with git fetch --unshallow")
with mock.patch.object(rnd, "missing_packages", return_value=([], [])), mock.patch.object(rnd, "shallow", return_value=True), mock.patch.object(rnd.subprocess, "run", fake_run):
    check(rnd.preflight() == 1, "preflight: a failed unshallow stops the round")
with mock.patch.object(rnd, "missing_packages", return_value=([], [])), mock.patch.object(rnd, "shallow", return_value=False):
    check(rnd.preflight() == 0, "preflight: nothing to do in a complete clone")

lid = "fy8-8"
for lang in rnd.languages(lid, []):
    for part in ("lesson", "exercises"):
        extra = rnd.lang_args(lang) + (["--exercises"] if part == "exercises" else [])
        out = subprocess.run([sys.executable, "scripts/reviews.py", "carry", lid, *extra], capture_output=True, text=True, cwd=ROOT).stdout.splitlines()
        st = subprocess.run([sys.executable, "scripts/reviews.py", "status", lid, *rnd.lang_args(lang)], capture_output=True, text=True, cwd=ROOT).stdout
        res, line = rnd.parse_carry(out)
        need = {n for n, (m, _) in res.items() if m != "none"}
        half = st.split("; exercises: ")[1 if part == "exercises" else 0]
        stale = {n for n in rnd.ROLES if f"{n}=PASS" not in half}
        check(need == stale, f"{lid} [{lang}] {part}: round needs {sorted(need) or 'nothing'}, status says {sorted(stale) or 'nothing'} stale")

# 4. course units (work queue 0j)
check(rnd.parse_item_carry(["science: carried over (a figure)", "pedagogy: already current", "visual: no earlier PASS, review needed", "fi/fy9-liike: draft"])
      == {"science": ("none", True), "pedagogy": ("none", False), "visual": ("full", False)}, "parse_item_carry: carried, current and needed")
check(rnd.parse_item_carry(["visual: more than teacher-approved figures changed, review needed"]) == {"visual": ("full", False)}, "parse_item_carry: a changed item needs a full review")
check(rnd.is_unit("fy9-liike") and not rnd.is_unit("fy8-8"), "is_unit: fy9-liike is a unit, fy8-8 is a lesson")
import units
uid = "fy9-liike"
check(set(rnd.unit_languages(uid, [])) >= {"fi", "en", "fi-easy"} and rnd.unit_languages(uid, ["en"]) == ["en"], "unit_languages: every language of the unit, --lang limits them")
check(rnd.has_sovella(uid, "fi"), "has_sovella: fy9-liike has a Sovella task set")
for lang in rnd.unit_languages(uid, []):
    out = subprocess.run([sys.executable, "scripts/reviews.py", "carry-item", "unit", uid, "--lang", lang], capture_output=True, text=True, cwd=ROOT).stdout.splitlines()
    need = {n for n, (m, _) in rnd.parse_item_carry(out).items() if m != "none"}
    stale = {n for n, v in units.status(uid, lang)["reports"].items() if v != "PASS"}
    check(need == stale, f"{uid} [{lang}]: round needs {sorted(need) or 'nothing'}, units.status says {sorted(stale) or 'nothing'} not PASS")
# a unit round makes no lesson calls: with every command faked, the unit's steps are the ones listed in the docstring
calls = []
def fake(args, log):
    calls.append(args); return 0, (["science: full review needed"] if args[0] == "reviews.py" else ["ok"])
with mock.patch.object(rnd, "run", fake):
    n = rnd.unit_round([uid], ["en"], False, None, lambda s: None)
names = [(c[0], c[1] if c[0] in ("practice.py", "reviews.py") else "") for c in calls]
check(n == 0 and ("reviews.py", "carry-item") in names and ("screenshot.py", "") not in names and ("practice.py", "packet") in names
      and calls[-1][:4] == ["practice.py", "packet", f"units/{uid}", "--role"] and calls[-1][4] == "science", "unit_round: checks, carry-item and one science packet, no captures when visual is current")
sys.exit(1 if bad else 0)
