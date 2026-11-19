"""check_site_removals.py: finds a deleted site/ page, accepts none, honours docs/site-removals.tsv (work queue 20).
Usage: python scripts/test_check_site_removals.py. Exit status 1 on any failure."""
import pathlib, subprocess, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check_site_removals as c

fails = 0


def check(name, ok):
    global fails
    print(("ok   " if ok else "FAIL ") + name)
    fails += 0 if ok else 1


def git(d, *a):
    subprocess.run(["git", "-C", d, "-c", "user.email=t@t", "-c", "user.name=t", *a], check=True, capture_output=True)


with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    (root / "fysiikkalabra/site/en").mkdir(parents=True)
    for p in ("site/a.html", "site/en/a.html", "site/en/b.html", "site/style.css"):
        (root / "fysiikkalabra" / p).write_text(p)
    git(tmp, "init", "-q", "-b", "main"); git(tmp, "add", "-A"); git(tmp, "commit", "-qm", "base")
    c.ROOT = root / "fysiikkalabra"
    git(tmp, "checkout", "-qb", "pr")
    check("no change: empty list", c.removed_pages("main") == [])
    (root / "fysiikkalabra/site/en/a.html").unlink()
    (root / "fysiikkalabra/site/style.css").unlink()                       # not a page
    (root / "fysiikkalabra/site/b.html").write_text("new")                  # an addition is no removal
    (root / "fysiikkalabra/site/en/b.html").rename(root / "fysiikkalabra/site/en/c.html")   # a move removes the old address
    git(tmp, "add", "-A"); git(tmp, "commit", "-qm", "pr")
    got = c.removed_pages("main")
    check("deleted and moved pages found, css and additions not", got == ["site/en/a.html", "site/en/b.html"])
    check("main() fails without a row", c.main(["main"]) == 1)
    check("message lists the pages and the usual cause", "site/en/a.html" in c.message(got) and "CONTENT-HASH" in c.message(got))
    allowed = c.parse_allowlist("# c\n\nsite/en/a.html\tintended, teacher\n")
    check("allowlist ignores comments and blank lines", allowed == {"site/en/a.html": "intended, teacher"})
    check("a row excuses only its own page", c.unexcused(got, allowed) == ["site/en/b.html"])
    check("all rows: nothing unexcused", c.unexcused(got, {p: "x" for p in got}) == [])
    try:
        c.parse_allowlist("site/en/a.html\n"); check("a row without a reason is rejected", False)
    except ValueError:
        check("a row without a reason is rejected", True)
    (root / "fysiikkalabra/docs").mkdir()
    c.ALLOW = root / "fysiikkalabra/docs/site-removals.tsv"
    c.ALLOW.write_text("site/en/a.html\tx\nsite/en/b.html\ty\n")
    check("main() passes when every removal has a row", c.main(["main"]) == 0)
sys.exit(1 if fails else 0)
