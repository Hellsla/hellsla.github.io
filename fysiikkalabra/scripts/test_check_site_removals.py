"""check_site_removals.py: finds a deleted site/ page, accepts none, honours docs/site-removals.tsv (work queue 20).
Usage: python scripts/test_check_site_removals.py. Exit status 1 on any failure."""
import pathlib, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check_site_removals as c

fails = 0


def check(name, ok):
    global fails
    print(("ok   " if ok else "FAIL ") + name)
    fails += 0 if ok else 1


with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    (root / "fysiikkalabra/docs").mkdir(parents=True)
    got = ["site/en/a.html", "site/en/b.html"]
    check("message lists the pages and the usual cause", "site/en/a.html" in c.message(got) and "CONTENT-HASH" in c.message(got))
    allowed = c.parse_allowlist("# c\n\nsite/en/a.html\tintended, teacher\n")
    check("allowlist ignores comments and blank lines", allowed == {"site/en/a.html": "intended, teacher"})
    check("a row excuses only its own page", c.unexcused(got, allowed) == ["site/en/b.html"])
    check("all rows: nothing unexcused", c.unexcused(got, {p: "x" for p in got}) == [])
    try:
        c.parse_allowlist("site/en/a.html\n"); check("a row without a reason is rejected", False)
    except ValueError:
        check("a row without a reason is rejected", True)
    # two renders: the pages the head lacks
    bd, hd = root / "bd", root / "hd"
    for d, files in ((bd, ["a.html", "en/b.html", "x.css"]), (hd, ["a.html", "en/c.html"])):
        for f in files: (d / f).parent.mkdir(parents=True, exist_ok=True); (d / f).write_text("x")
    check("removed_built: a page the head render lacks, not css or additions", c.removed_built(bd, hd) == ["site/en/b.html"])
    c.ALLOW = root / "fysiikkalabra/docs/none.tsv"
    check("main() without --built is a usage error", c.main([]) == 2)
    check("main(--built) fails without a row", c.main(["--built", str(bd), str(hd)]) == 1)
    c.ALLOW = root / "fysiikkalabra/docs/site-removals.tsv"; c.ALLOW.write_text("site/en/b.html\tx\n")
    check("main(--built) passes with a row", c.main(["--built", str(bd), str(hd)]) == 0)
sys.exit(1 if fails else 0)
