"""Tests of ci_scope.py's built mode (work queue 0g, PR 1): the pages to test from two renders of the site instead of the
committed site/ diff. No browser, no build.

  python scripts/test_ci_scope_built.py
"""
import pathlib, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ci_scope as cs

passed = failed = 0


def check(name, ok, detail=""):
    global passed, failed
    if ok: passed += 1
    else: failed += 1; print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def make(root, files):
    for rel, text in files.items():
        f = pathlib.Path(root) / rel; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(text)


BASE = {"fy3-4.html": '<link href="site.css?v=aaaa1111"><p>a</p>', "en/fy3-4.html": '<link href="../site.css?v=aaaa1111">x',
        "fy1-1.html": '<link href="site.css?v=aaaa1111">y', "site.css": "a{}", "pics/fy3/x.svg": "<svg/>", "FY3.html": "course"}
with tempfile.TemporaryDirectory() as tmp:
    a, b = pathlib.Path(tmp) / "base", pathlib.Path(tmp) / "head"
    make(a, BASE)

    def run(changes, removed=()):
        import shutil
        if b.exists(): shutil.rmtree(b)
        make(b, {**BASE, **changes})
        for r in removed: (b / r).unlink()
        return cs.built_names(a, b)

    check("identical renders: no name", run({}) == [])
    check("only ?v= tokens differ: equal", run({"fy3-4.html": '<link href="site.css?v=bbbb2222"><p>a</p>'}) == [])
    check("a page that differs", run({"fy3-4.html": "<p>b</p>"}) == ["site/fy3-4.html"])
    check("a language page that differs", run({"en/fy3-4.html": "z"}) == ["site/en/fy3-4.html"])
    check("a new page", run({"fy9-1.html": "n"}) == ["site/fy9-1.html"])
    check("a removed page", run({}, removed=["fy1-1.html"]) == ["site/fy1-1.html"])
    check("a changed shared file", run({"site.css": "b{}"}) == ["site/site.css"])
    # the same names go through scope() as the committed site/ diff did (base = HEAD: no source change)
    for changes, want, label in (({}, set(), "nothing changed"), ({"fy3-4.html": '<link href="site.css?v=bbbb2222"><p>a</p>'}, set(), "a ?v=-only change tests nothing"),
                                 ({"fy3-4.html": "<p>b</p>"}, {"fy3-4"}, "a changed page tests that page"),
                                 ({"en/fy3-4.html": "z", "FY3.html": "c"}, {"fy3-4"}, "a course page tests nothing of its own"),
                                 ({"pics/fy3/x.svg": "<svg>1</svg>"}, set(), "a copied picture tests nothing of its own")):
        run(changes)
        kind, what = cs.scope("HEAD", (a, b))
        check(f"scope: {label}", kind == "pages" and set(what) == want, f"{kind} {sorted(what) if kind == 'pages' else what}")
    run({"site.css": "b{}"})
    kind, what = cs.scope("HEAD", (a, b))
    check("scope: a shared file tests the smoke sample", kind == "pages" and set(what) == set(cs.SMOKE), f"{kind} {what if kind != 'pages' else sorted(what)}")

print(f"test_ci_scope_built: {passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
