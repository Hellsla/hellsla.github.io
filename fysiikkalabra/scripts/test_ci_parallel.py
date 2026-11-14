"""Tests of scripts/ci_parallel.py: the plan, the shards, a unit's verdict and the gate. No browser.

  python scripts/test_ci_parallel.py

The gate is what the required check `qa` rests on, so these tests show that it fails when a page was not tested, was
tested twice, failed, when a job's report is missing or when the jobs disagree on the pages, and that the lists of a
full run are the ones test_sims.py, check_layout.py and the old inquiry loop of the workflow walk."""
import json, pathlib, re, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ci_parallel as cp
from ci_parallel import ROOT

passed = failed = 0


def check(name, ok, detail=""):
    global passed, failed
    if ok: passed += 1
    else: failed += 1; print(f"FAIL {name}" + (f": {detail}" if detail else ""))


# the plan
full, few, many, none = cp.plan("full"), cp.plan("fy3-4 fy1-1"), cp.plan(" ".join(f"p-{i}" for i in range(60))), cp.plan("")
check("a full run has every width in LAYOUT_SHARDS jobs, shards 0/n … n-1/n", [(j["widths"], j["shard"]) for j in full["layout"]] == [(w, f"{i}/{cp.LAYOUT_SHARDS}") for w in cp.WIDTHS.split() for i in range(cp.LAYOUT_SHARDS)])
check("a full run's inquiry shards are 0/n … n-1/n", full["inquiry"] == [f"{i}/{cp.INQUIRY_SHARDS}" for i in range(cp.INQUIRY_SHARDS)])
check("job names of a matrix are unique", len({j["name"] for j in full["layout"]}) == len(full["layout"]))
check("the widths are the eight of NOTES.md §8", cp.WIDTHS.split() == "360 390 640 768 1024 1280 1440 1920".split())
check("a full run's simulation shards are 0/n … n-1/n", full["sims"] == [f"{i}/{cp.SIMS_SHARDS}" for i in range(cp.SIMS_SHARDS)])
check("a few pages: one job per check, all eight widths in it", few == {"sims": ["0/1"], "layout": [{"name": "all widths", "widths": cp.WIDTHS, "shard": "0/1"}], "inquiry": ["0/1"], "simtext": ["0/1"]})
check("many pages: every width still planned", sorted(w for j in many["layout"] for w in j["widths"].split()) == sorted(cp.WIDTHS.split()) and len(many["sims"]) == 5 and len(many["inquiry"]) == 2)
check("no page: no browser job", none == {"sims": [], "layout": [], "inquiry": [], "simtext": []})
check("a full run's picture-text shards are 0/n … n-1/n", full["simtext"] == [f"{i}/{cp.SIMTEXT_SHARDS}" for i in range(cp.SIMTEXT_SHARDS)] and many["simtext"] == ["0/1"])
check("picture-text: the verdict lines are PASS|FAIL <page>", cp.verdict("simtext", ["preview/fy4-1"], None, 0, "PASS preview/fy4-1 23 labels\n")[0] and not cp.verdict("simtext", ["preview/fy4-1"], None, 1, "FAIL preview/fy4-1\n")[0])

# the shards: every unit exactly once, for any number of shards
units = {f"fy{c}-{i}": [] for c in range(1, 9) for i in range(1, 17)}
for n in (1, 2, 3, 4, 7):
    got = [u for i in range(n) for u in cp.select(units, "full", f"{i}/{n}")[1]]
    check(f"{n} shards cover every unit once", sorted(got) == sorted(units))
    sizes = [len(cp.select(units, "full", f"{i}/{n}")[1]) for i in range(n)]
    check(f"{n} shards are even", max(sizes) - min(sizes) <= 1, str(sizes))
check("a page list is the scripts' own filter: unknown ids are no units", cp.select(units, "fy1-1 fy9-99 fy3-2", "0/1")[0] == ["fy1-1", "fy3-2"])

# the universe of a full run is the scripts' own walk
src_s, src_l = (HERE / "test_sims.py").read_text(), (HERE / "check_layout.py").read_text()
walk = 'sorted(OUT.glob("*.html")) + [f for lang in i18n.languages()[1:] for f in sorted((OUT / lang).glob("*.html"))]'
check("test_sims.py and check_layout.py still walk the pages as ci_parallel.py lists them", walk in src_s and walk in src_l)
check("test_sims.py still tests the pages with id=\"sim-root\" and prints PASS/FAIL <folder>/<page>",
      """if 'id="sim-root"' not in page_file.read_text(): continue""" in src_s and """print("PASS" if ok else "FAIL", f"{OUT.name}/{page_file.relative_to(OUT).with_suffix('').as_posix()}\"""" in src_s)
check("check_layout.py still tests the pages with a hyphen and prints OK/FAIL <folder>/<page> at <w> px",
      'if lid == "index" or "-" not in lid: continue' in src_l and """tag = f"{OUT.name}/{page_file.relative_to(OUT).with_suffix('').as_posix()} at {width} px\"""" in src_l)
check("test_sims.py still marks an assertion it did not judge with the words the second run looks for", cp.SLOW in src_s)
lay = cp.universe("layout")
site = [f for f in cp.page_files(ROOT / "site") if f.stem != "index" and "-" in f.stem]
check("layout: every lesson page of site/ in every language is in a unit", sum(len(v) for v in lay.values()) == len(site) and len(site) > 300, f"{sum(len(v) for v in lay.values())} of {len(site)}")
inq = cp.universe("inquiry")
want = sorted(f.parent.name for f in (ROOT / "content/fi").glob("*/*/inquiry.json") if f.parts[-3] != "units")
check("inquiry: every content/fi/<COURSE>/<id>/inquiry.json outside units/", sorted(inq) == want and len(want) > 100, f"{len(inq)} of {len(want)}")
sims = cp.universe("sims")
check("sims: units are the pages with a simulation", len(sims) > 80 and all(k.count("/") >= 1 for v in sims.values() for k in v))

# a unit's verdict
V = cp.verdict
check("sims: exit 0 and a line per page passes", V("sims", ["preview/fy1-1", "preview/en/fy1-1"], None, 0, "PASS preview/fy1-1 2 assertions\nPASS preview/en/fy1-1 x\n")[0])
check("sims: a failing exit status fails", not V("sims", ["preview/fy1-1"], None, 1, "FAIL preview/fy1-1 2 assertions\n     x\n")[0])
check("sims: a page without its line fails although the script exits 0", not V("sims", ["preview/fy1-1", "preview/en/fy1-1"], None, 0, "PASS preview/fy1-1 2 assertions\n")[0])
check("sims: fy1-1 is not answered by fy1-10's line", not V("sims", ["preview/fy1-1"], None, 0, "PASS preview/fy1-10 2 assertions\n")[0])
check("layout: a line per page at the width passes", V("layout", ["site/fy1-1", "site/en/fy1-1"], 360, 0, "OK   site/fy1-1 at 360 px\nOK   site/en/fy1-1 at 360 px\n")[0])
check("layout: a line at another width does not count", not V("layout", ["site/fy1-1"], 360, 0, "OK   site/fy1-1 at 390 px\n")[0])
check("layout: a finding fails", not V("layout", ["site/fy1-1"], 360, 1, "FAIL site/fy1-1 at 360 px\n  overflow   12 px  [open]  x\n")[0])
check("inquiry: the summary line with no failure passes", V("inquiry", [], None, 0, "\n97 passed, 0 failed\n")[0])
check("inquiry: no summary line fails", not V("inquiry", [], None, 0, "fy3-4: no inquiry.json\n")[0])
check("inquiry: a failure fails", not V("inquiry", [], None, 1, "FAIL x\n\n96 passed, 1 failed\n")[0])
check("inquiry: nothing checked fails", not V("inquiry", [], None, 0, "\n0 passed, 0 failed\n")[0])


# the gate
def unit(i, w=None, ok=True, alone=False): return {"id": i, "width": w, "rc": 0 if ok else 1, "ok": ok, "seconds": 1.0, "problems": [], "pages": 3, "slow": 0, "alone": alone, "hung": False}


def reports(pages="a-1 a-2 a-3"):
    uni = sorted(pages.split()); p = cp.plan(pages)
    out = {}
    for kind in ("sims", "simtext", "inquiry"):
        for k, sh in enumerate(p[kind]):
            out[f"{kind}-{k}"] = {"kind": kind, "shard": sh, "pages": pages, "widths": [], "universe": uni, "units": [unit(i) for i in uni[k::len(p[kind])]], "wall": 5}
    for k, j in enumerate(p["layout"]):
        ws = [int(w) for w in j["widths"].split()]; i0, n = (int(x) for x in j["shard"].split("/"))
        out[f"layout-{k}"] = {"kind": "layout", "shard": j["shard"], "pages": pages, "widths": ws, "universe": uni, "units": [unit(i, w) for w in ws for i in uni[i0::n]], "wall": 5}
    return out


def gate(reps, pages="a-1 a-2 a-3"):
    with tempfile.TemporaryDirectory() as d:
        for name, r in reps.items(): (pathlib.Path(d) / name).mkdir(); (pathlib.Path(d) / name / f"{name}.json").write_text(json.dumps(r))
        r = subprocess.run([sys.executable, HERE / "ci_parallel.py", "gate", d, "--pages", pages], capture_output=True, text=True, env={k: v for k, v in __import__("os").environ.items() if k != "GITHUB_STEP_SUMMARY"})
        return r.returncode, r.stdout + r.stderr


rc, text = gate(reports()); check("gate: complete reports pass", rc == 0, text[-300:])
check("gate: the summary counts 3 units and 9 page checks per check and width", re.search(r"\| layout 360 px \| 1 \| 3 \| 9 \| 0 \|", text) is not None, text[:400])
r = reports(); r["sims-0"]["units"].pop(); rc, text = gate(r); check("gate: a page no job tested fails", rc == 1 and "not tested: a-3" in text, text[-300:])
r = reports(); r["sims-0"]["units"].append(unit("a-1")); rc, text = gate(r); check("gate: a page tested twice fails", rc == 1 and "twice: a-1" in text)
r = reports(); r["layout-0"]["units"] = [u for u in r["layout-0"]["units"] if not (u["id"] == "a-2" and u["width"] == 1024)]; rc, text = gate(r)
check("gate: a page missing at one width fails, and names the width", rc == 1 and "layout 1024 px" in text and "not tested: a-2" in text)
r = reports(); r["inquiry-0"]["units"][1]["ok"] = False; rc, text = gate(r); check("gate: a failed unit fails", rc == 1 and "inquiry: failed: a-2" in text)
r = reports(); r["sims-0"]["units"].append(unit("a-2", ok=False, alone=True)); rc, text = gate(r); check("gate: a unit that failed when run again alone fails", rc == 1 and "sims: failed: a-2" in text)
r = reports(); del r["inquiry-0"]; rc, text = gate(r); check("gate: a missing report fails", rc == 1 and "inquiry: reports of shards []" in text)
r = reports(); del r["layout-0"]; rc, text = gate(r); check("gate: a missing layout report fails at every width", rc == 1 and text.count("reports of shards []") == 8)
r = reports(); r["sims-0"]["units"][0].update(ok=False, rc=124, hung=True); rc, text = gate(r); check("gate: a unit that hung and was not run again fails", rc == 1 and "sims: failed: a-1" in text, text[-300:])
r = reports(); r["sims-0"]["units"][0].update(ok=False, rc=124, hung=True); r["sims-0"]["units"].append(unit("a-1", alone=True)); rc, text = gate(r)
check("gate: a unit that hung and passed when run again passes, and the summary names it", rc == 0 and "note: sims: no verdict at first (hung), run again alone: a-1" in text, text[-300:])
r = reports(); r["sims-0"]["units"][0].update(ok=False, rc=124, hung=True); r["sims-0"]["units"].append(dict(unit("a-1", ok=False, alone=True), hung=True)); rc, text = gate(r)
check("gate: a unit that hung twice fails", rc == 1 and "sims: failed: a-1" in text)
r = reports(); r["sims-0"]["units"][0].update(ok=False, rc=124, hung=True); r["sims-0"]["units"].append(unit("a-1", ok=False, alone=True)); rc, text = gate(r)
check("gate: a unit that hung and failed when run again fails", rc == 1 and "sims: failed: a-1" in text)
rc, text = gate({}); check("gate: no report at all fails", rc == 1)
rc, text = gate({}, pages=""); check("gate: no page changed and no report passes", rc == 0 and "nothing to test" in text, text[-200:])
rc, text = gate(reports(), pages=""); check("gate: a report although nothing was planned fails", rc == 1)
rc, text = gate(reports(), pages="a-1 a-2 a-3 a-4"); check("gate: reports of another page list fail", rc == 1 and "another page list" in text)
big = " ".join(f"p-{i:02}" for i in range(60))
rc, text = gate(reports(big), big); check("gate: five simulation shards, two inquiry shards and a layout job per width pass", rc == 0, text[-300:])
r = reports(big); del r["sims-1"]; rc, text = gate(r, big); check("gate: a missing shard fails", rc == 1 and "sims: reports of shards ['0/5', '2/5', '3/5', '4/5']" in text, text[-300:])
r = reports(big); r["sims-1"]["universe"] = r["sims-1"]["universe"][:-1]; rc, text = gate(r, big); check("gate: jobs that list different pages fail", rc == 1 and "different pages" in text)
r = reports("full"); rc, text = gate(r, "full"); check("gate: a full run whose list is not the checkout's fails", rc == 1 and "the checkout has" in text)
huge = " ".join(f"p-{i:03}" for i in range(300))
rc, text = gate(reports(huge), huge); check("gate: two layout shards per width pass", rc == 0 and len(cp.plan(huge)["layout"]) == 16, text[-300:])
r = reports(huge); del r["layout-5"]; rc, text = gate(r, huge); check("gate: a missing layout shard of one width fails", rc == 1 and "layout 640 px: reports of shards ['0/2']" in text, text[-300:])

# which pages a pull request tests (scripts/ci_scope.py): the workflow file lies outside fysiikkalabra/
import ci_scope


def scoped(names, workflow=()):
    """ci_scope.scope() of a pull request that changed these files of fysiikkalabra/ and these of .github/."""
    real = ci_scope.git
    def fake(*a):
        if a[0] == "rev-parse": return "/repo\n"
        if a[0] == "diff" and "--relative" in a: return "\n".join(names)
        if a[0] == "diff": return "\n".join(workflow)
        return real(*a)
    ci_scope.git = fake
    try: return ci_scope.scope("origin/main")
    finally: ci_scope.git = real


WF = ".github/workflows/fysiikkalabra-ci.yml"
# teacher 2026-11-11: a shared change tests the fixed sample, never the whole site (that is the weekly and the manual run)
SM = set(ci_scope.SMOKE)
k, w = scoped([], [WF]); check("scope: the workflow file alone is not skipped: it tests the sample", k == "pages" and set(w) == SM, f"{k} {sorted(w)}")
k, w = scoped(["content/fi/FY3/fy3-1/lesson.md"], [WF]); check("scope: the workflow file with a lesson tests the sample and that lesson", k == "pages" and set(w) == SM | {"fy3-1"}, f"{k} {sorted(w)}")
k, w = scoped(["templates/site.css"] + [f"site/{p}.html" for p in ("fy1-2", "fy4-3", "fy6-5", "index")]); check("scope: a style sheet change tests the sample, not every page it re-rendered", k == "pages" and set(w) == SM, f"{k} {sorted(w)}")
k, w = scoped(["templates/sim-embed.js", "assets/sims/fy4/fy4-1/sim.js", "site/fy6-5.html"]); check("scope: a shared file with one simulation tests the sample and that simulation's lesson", k == "pages" and set(w) == SM | {"fy4-1"}, f"{k} {sorted(w)}")
check("scope: the sample fits one job per check", 0 < len(ci_scope.SMOKE) <= 12 and len(SM) == len(ci_scope.SMOKE))
check("scope: the review system's own files test no page", scoped(["scripts/reviews.py", "scripts/test_reviews.py", "docs/presentation-only.tsv"]) == ("pages", {}), str(scoped(["scripts/reviews.py"])))
k, w = scoped(["scripts/reviews.py", "assets/sims/fy4/fy4-1/sim.js", "site/sims/fy4/fy4-1/sim.js", "site/fy4-1.html"]); check("scope: a review rule with one simulation tests that lesson only", k == "pages" and set(w) == {"fy4-1"}, f"{k} {sorted(w)}")
check("scope: the file that decides what publishes is still a full run", scoped(["docs/visual-baseline.tsv"])[0] == "full")
k, w = scoped(["site/fy4-3.html", "site/en/fy4-3.html"]); check("scope: without a shared change a re-rendered page is tested", k == "pages" and set(w) == {"fy4-3"}, f"{k} {sorted(w)}")
check("scope: a document alone tests no page", scoped(["docs/audits/2026-11-10-vaiheiden-kayttoliittyma.md"]) == ("pages", {}), str(scoped(["docs/audits/2026-11-10-vaiheiden-kayttoliittyma.md"])))
check("scope: nothing changed tests no page", scoped([]) == ("pages", {}))
k, w = scoped(["content/fi/FY3/fy3-1/lesson.md"]); check("scope: a lesson's text tests that lesson only", k == "pages" and list(w) == ["fy3-1"], f"{k} {w}")
k, w = scoped(["scripts/build.py"]); check("scope: a script shared by every page tests the sample", k == "pages" and set(w) == SM, f"{k} {sorted(w)}")

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
