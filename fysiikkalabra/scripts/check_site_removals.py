"""A pull request must not remove a published page from site/ without a row saying so (work queue 20).

Usage: python scripts/check_site_removals.py --built <base site dir> <head site dir>      (CI's plan job, on a pull request)
       python scripts/check_site_removals.py [base]                                       (the committed site/ diff, until work queue 0g PR 3)

Since work queue 0g PR 2 a pull request no longer builds or commits site/, so the removal is read from two renders: the pages
the base commit's build has and this commit's build lacks.

A page leaves site/ when its lesson's reviews stop matching the content hash (a wrong hash in a report, reviews
still open): build.py then only warns and the page quietly disappears from the published site. This check lists the
.html files the branch deletes from site/ (git diff --diff-filter=D --no-renames base...HEAD) and fails unless every
one has a row in docs/site-removals.tsv: `<path relative to fysiikkalabra/>\t<reason>` (for example
`site/en/fy9-lampo.html<TAB>replaced by site/en/fy9-lampo/index.html, teacher 2026-11-20`), `#` starts a comment.
The row is added in the pull request that makes the intended removal, so the teacher sees it there; once the removal is
merged the row is dead and is deleted. A moved page counts as a removal (the old address stops working)."""
import pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ALLOW = ROOT / "docs" / "site-removals.tsv"


def removed_built(base_dir: str, head_dir: str) -> list[str]:
    """The .html pages (`site/<path>`) two renders differ in by the head lacking them."""
    b, h = pathlib.Path(base_dir), pathlib.Path(head_dir)
    return sorted(f"site/{p.relative_to(b).as_posix()}" for p in b.rglob("*.html") if not (h / p.relative_to(b)).is_file())


def removed_pages(base: str) -> list[str]:
    out = subprocess.run(["git", "diff", "--diff-filter=D", "--no-renames", "--name-only", "--relative", f"{base}...HEAD", "--", "site/"],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return sorted(p for p in out.splitlines() if p.endswith(".html"))


def parse_allowlist(text: str) -> dict[str, str]:
    """path -> reason; a row without a reason is an error (ValueError)."""
    rows = {}
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        path, _, reason = line.partition("\t")
        if not path.strip() or not reason.strip():
            raise ValueError(f"docs/site-removals.tsv line {n}: needs `<path><TAB><reason>`")
        rows[path.strip()] = reason.strip()
    return rows


def unexcused(removed: list[str], allowed: dict[str, str]) -> list[str]:
    return [p for p in removed if p not in allowed]


def message(pages: list[str]) -> str:
    return ("This pull request removes published pages from site/ without a row in docs/site-removals.tsv:\n"
            + "".join(f"  - {p}\n" for p in pages)
            + "Usual cause: a lesson's review report CONTENT-HASH does not match that language's own content (a Finnish hash in an\n"
              "en or fi-easy report; `python scripts/units.py hash <id> --lang <lang>`), or its reviews are still open, so build.py\n"
              "left the page out with a WARNING. Fix the reviews (`python scripts/reviews.py status <id>`; a local `python scripts/build.py` shows the WARNING).\n"
              "If the removal is intended, add `<path><TAB><reason>` to docs/site-removals.tsv in this pull request and say so in its description.")


def main(argv: list[str]) -> int:
    built = argv[1:3] if argv[:1] == ["--built"] and len(argv) == 3 else None
    base = argv[0] if argv and not built else "origin/main"
    try:
        allowed = parse_allowlist(ALLOW.read_text(encoding="utf-8")) if ALLOW.exists() else {}
        bad = unexcused(removed_built(*built) if built else removed_pages(base), allowed)
    except (ValueError, subprocess.CalledProcessError) as e:
        print(f"check_site_removals.py: {e}")
        return 1
    if bad:
        print(message(bad))
        return 1
    print("no published page removed from site/ (or every removal has a row in docs/site-removals.tsv)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
