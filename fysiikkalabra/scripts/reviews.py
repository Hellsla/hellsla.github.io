"""Review state of a lesson: one content hash, two reviews, no status fields.

  python scripts/reviews.py hash <id>        the lesson's content hash (reviewers put it in their report)
  python scripts/reviews.py status [<id>]    reviewed | legacy | draft for one lesson or all, with the reason
  python scripts/reviews.py legacy <id>      write review/legacy.md: prototype content the teacher keeps visible
  python scripts/reviews.py verify           CI: print every lesson's state; exit 1 on a malformed report

A lesson is *reviewed* when review/science.md and review/pedagogy.md both start with `VERDICT: PASS` and carry
the current CONTENT-HASH. It is *legacy* when review/legacy.md does (a prototype lesson published before the
two-review pipeline, kept visible by the teacher's approval of the migration PR until it is reworked). Anything
else is a *draft*: the build leaves it out of site/ and warns if it was on the live site.

The hash is taken over the lesson's content with formatting normalised (`normalized`): line endings, trailing
whitespace, blank-line runs and JSON layout do not change it, so a purely mechanical cleanup keeps the reviews
valid. Any other change (a word, a number, a space inside a line, an indentation, a LaTeX command, a line of
sim.js) changes the hash and both reviews must run again. The rule is deliberately conservative: it never
guesses what a change means.
"""
import datetime, hashlib, json, os, pathlib, re, sys

ROOT = pathlib.Path(os.environ.get("FYSIIKKALABRA_ROOT") or pathlib.Path(__file__).resolve().parents[1])
REVIEWS = ("science", "pedagogy")
CONTENT = ("meta.json", "lesson.md", "exercises.json", "solutions.md", "answers.py", "exit-ticket.json", "sim.js", "sim-spec.md")


def find_lesson(lid):
    for f in sorted((ROOT / "content").glob(f"*/{lid}")):
        if f.parent.name != "_gold" and (f / "meta.json").exists(): return f
    sys.exit(f"no lesson folder for {lid!r}")


def normalized(text, name):
    """Formatting-free view of a content file that cannot hide a change of meaning: JSON is re-serialised
    canonically (same data, same hash); in text only line endings, trailing whitespace and runs of blank lines are
    dropped. Indentation and the spaces inside a line stay, because they carry meaning in Python, Markdown
    (nested lists, code blocks), LaTeX (`\\text{}`) and JavaScript strings."""
    if name.endswith(".json"):
        return json.dumps(json.loads(text), sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    out = []
    for l in text.replace("\r\n", "\n").split("\n"):
        l = l.rstrip()
        if l == "" and out and out[-1] == "": continue
        out.append(l)
    while out and out[-1] == "": out.pop()
    return "\n".join(out)


def content_hash(folder):
    h = hashlib.sha256()
    files = [(n, folder / n) for n in CONTENT] + [(f"tests/sims/{folder.name}.json", ROOT / "tests/sims" / f"{folder.name}.json")]
    for name, f in files:
        if f.exists(): h.update(name.encode() + b"\0" + normalized(f.read_text(), name).encode() + b"\0")
    return h.hexdigest()[:16]


def report(folder, name):
    """(verdict, hash) from review/<name>.md, or None when there is no report. A malformed report raises."""
    f = folder / "review" / f"{name}.md"
    if not f.exists(): return None
    lines = f.read_text().splitlines()[:3]
    verdict = lines[0].split(":", 1)[1].strip() if lines and lines[0].startswith("VERDICT:") else None
    h = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("CONTENT-HASH:")), None)
    if verdict not in ("PASS", "FAIL") or not h:
        raise ValueError(f"{f.relative_to(ROOT)}: line 1 must be `VERDICT: PASS|FAIL`, line 2 `CONTENT-HASH: <hash>`")
    return verdict, h


def status(folder):
    """{'state': reviewed|legacy|draft, 'hash': ..., 'reports': {name: PASS|FAIL|stale|missing}}."""
    h = content_hash(folder)
    reports = {}
    for name in REVIEWS + ("legacy",):
        r = report(folder, name)
        reports[name] = "missing" if r is None else "stale" if r[1] != h else r[0]
    state = ("reviewed" if all(reports[n] == "PASS" for n in REVIEWS)
             else "legacy" if reports["legacy"] == "PASS" else "draft")
    return {"state": state, "hash": h, "reports": reports}


def describe(folder):
    s = status(folder)
    why = ", ".join(f"{n}={v}" for n, v in s["reports"].items() if not (n == "legacy" and v == "missing"))
    return f"{folder.name}: {s['state']} ({why or 'no reports'})"


def write_legacy(folder):
    s = status(folder)
    if s["state"] == "reviewed": sys.exit(f"{folder.name} is reviewed by the two-review pipeline; it needs no legacy marker")
    review = folder / "review"; review.mkdir(exist_ok=True)
    (review / "legacy.md").write_text(
        f"VERDICT: PASS\nCONTENT-HASH: {s['hash']}\n\n"
        f"Prototype lesson, published before the two-review pipeline. Kept visible by the teacher's approval of the\n"
        f"migration pull request ({datetime.date.today()}). Not reviewed by the science and pedagogy reviewers: the page\n"
        f"says so. Any content change retires this marker; the lesson then returns only after both reviews pass.\n")
    print(describe(folder))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    lessons = [f.parent for f in sorted((ROOT / "content").glob("*/*/meta.json")) if f.parent.parent.name != "_gold"]
    if a[0] == "hash": print(content_hash(find_lesson(a[1])))
    elif a[0] == "status": print("\n".join(describe(f) for f in ([find_lesson(a[1])] if len(a) > 1 else lessons)))
    elif a[0] == "legacy": write_legacy(find_lesson(a[1]))
    elif a[0] == "verify":
        bad = 0
        for f in lessons:
            try: print(describe(f))
            except ValueError as e: print("ERROR", e); bad += 1
        sys.exit(1 if bad else 0)
    else: sys.exit(__doc__)
