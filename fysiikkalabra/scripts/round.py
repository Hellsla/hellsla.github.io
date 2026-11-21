"""One review round's deterministic steps in one command (work queue 0a, teacher 2026-11-17).

  python scripts/round.py <id>[,<id>…] [--exercises] [--lang fi,en,…] [--batch] [--skip-checks]
  python scripts/round.py <id>[,<id>…] --finish [--exercises] [--lang …]
  python scripts/round.py <unit id>[,…] [--sovella] [--lang …] [--finish]     a course unit (FY9, scripts/units.py)

Runs, in this order, what /lesson, /exercises and /quality-audit used to run one command (one orchestrator turn) at a time:
  1. the generated files CI compares: docs/figures/catalog.json (figcat.py build), docs/assessment/<COURSE>.md and
     docs/coverage/<COURSE>.md of every course the ids belong to (their --check fails CI when they are stale);
  2. check_lesson.py <id> for every id (every language of the lesson), then the quick site-wide checks CI runs that a
     lesson's text can break (test_notation, answers_shown, objectives, exercise_bank, test_physics_phrases); an id
     whose checks fail gets no packets: fix it first (--skip-checks skips this step, e.g. to remake a packet after an
     ESCALATE when nothing changed);
  3. per id, language and part (lesson and exercises; --exercises: the exercise set only): reviews.py carry, which
     records every reviewer whose scope is none and says which reviews are needed (delta or full);
  4. screenshot.py <id> --lang <lang> --if-stale for every language in which a visual review is needed (a language
     without captures was what sent visual packets back in fy8-5…fy8-8);
  5. review_packet.py for every needed review (with --batch: one review_packet.py --batch per role and language for
     the lesson diffs; an exercise set still gets its own packet).
--finish instead regenerates the files of step 1, runs reviews.py verify (as CI does; a few minutes), prints each id's
status in every language and rebuilds site/ (build.py --all, build.py) and palautus/ (palautus_tasks.py).

A course unit id (fy9-liike; work queue 0j, 2026-11-18) is recognised by its folder content/<lang>/units/<id>/ and runs the
same round for the unit's Sovella task set, which is part of the unit's hash and reviews (--sovella is accepted and
changes nothing: a unit has no other review packet): figcat.py build; units.py check, practice.py check and figures
--check; per language reviews.py carry-item unit <id> --lang <l> (a unit's reviews are full or carried, no delta);
screenshot.py <id> --lang <l> --if-stale where the visual review is needed; practice.py packet units/<id> --role
science|pedagogy|visual --lang <l> for every needed review; the units.py hash of every language is printed for the
reviewers' reports. --finish: verify, each language's unit status, build.py --all, build.py, palautus_tasks.py. The
assessment and coverage files belong to a course, so a unit alone regenerates only the figure catalogue. Lesson ids and
unit ids can be mixed in one call.

Before anything else it checks the environment (work queue 0d): a shallow clone (a cloud session clones with limited
history, and reviews.py scope then answers FULL for "not in git history") is deepened with git fetch --unshallow, and a
missing Python package (markdown, numpy, playwright) stops the round with the install command, pip install -r
requirements-ci.txt. The browser checks themselves run in CI's image through ci_env.py, so a session's own Playwright
version (the cloud image has 1.63, the repository pins 1.65) only warns.

Prints a short summary: the failing check lines only, each reviewer's mode, the carries recorded, the packet paths and
the generated files that changed. Every command's full output is in preview/round.log. --lang limits the languages
(default: every language that has the lesson). Exit status 1 if a check, a step or verify failed."""
import pathlib, re, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n

ROOT = courses.ROOT
PY = sys.executable
LOG = ROOT / "preview" / "round.log"
QUICK = [["test_notation.py"], ["answers_shown.py"], ["objectives.py"], ["test_physics_phrases.py"]]
GENERATED = ["docs/figures/catalog.json", "docs/assessment", "docs/coverage"]
ROLES = ("science", "pedagogy", "visual")


def run(args, log):
    """(exit status, output lines) of python scripts/<args>, the output appended to the log."""
    r = subprocess.run([PY, str(ROOT / "scripts" / args[0]), *map(str, args[1:])], capture_output=True, text=True, cwd=ROOT)
    out = (r.stdout + r.stderr).rstrip()
    log.write(f"$ python scripts/{' '.join(map(str, args))}  (exit {r.returncode})\n{out}\n\n"); log.flush()
    return r.returncode, out.splitlines()


def languages(lid, only):
    langs = [l for l in i18n.languages() if any((f / "meta.json").exists() for f in (ROOT / "content" / l).glob(f"*/{lid}"))]
    return [l for l in langs if not only or l in only]


def is_unit(uid):
    import units
    return any((units.folder(uid, l) / "unit.json").is_file() for l in units.languages())


def unit_languages(uid, only):
    import units
    return [l for l in units.languages() if (units.folder(uid, l) / "unit.json").is_file() and (not only or l in only)]


def has_sovella(uid, lang):
    import units
    return (units.folder(uid, lang) / "sovella" / "tasks.json").is_file()


def parse_item_carry(lines):
    """{reviewer: (mode, carried now?)} from reviews.py carry-item's lines: an item review is full or none (no delta)."""
    res = {}
    for l in lines:
        m = re.match(r"(science|pedagogy|visual): (.*)", l)
        if m:
            t = m.group(2)
            res[m.group(1)] = ("none", True) if t.startswith("carried over") else ("none", False) if t == "already current" else ("full", False)
    return res


def lang_args(lang):
    return [] if lang == courses.SOURCE_LANG else ["--lang", lang]


def changed_generated():
    r = subprocess.run(["git", "status", "--short", "--", *GENERATED], capture_output=True, text=True, cwd=ROOT)
    return [l[3:] for l in r.stdout.splitlines()]


def generate(ids, log, say):
    bad = 0
    for args in [["figcat.py", "build"]] + [[s, c] for c in sorted({courses.course_of(i) for i in ids if not is_unit(i)}) for s in ("assessment.py", "coverage.py")]:
        rc, out = run(args, log)
        if rc: bad += 1; say(f"FAIL {' '.join(args)}: " + (out[-1] if out else f"exit {rc}"))
    ch = changed_generated()
    say("generated: " + (", ".join(ch) + " changed: commit them" if ch else "up to date"))
    return bad


def parse_carry(lines):
    """{reviewer: (mode, carried now?)} and the status line, from reviews.py carry's output."""
    res, state = {}, ""
    for l in lines:
        m = re.match(r"(science|pedagogy|visual): (.*)", l)
        if m:
            t = m.group(2)
            res[m.group(1)] = ("none", True) if t.startswith("carried over") else ("none", False) if t == "already current" \
                else (t.split()[0], False)
        elif l.strip(): state = l
    # a reviewer whose PASS is already for the current content needs nothing, whatever its scope says
    for name in res:
        if res[name][0] != "none" and re.search(rf"\b{name}=PASS\b", state): res[name] = ("none", False)
    return res, state


def shallow():
    r = subprocess.run(["git", "rev-parse", "--is-shallow-repository"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() == "true"


IMPORT_NAMES = {"pillow": "PIL"}   # requirements-ci.txt names a package by its pip name; a few import under another name


def import_name(pkg):
    """The module to import for a requirements-ci.txt package name (Pillow → PIL); its own metadata first, then IMPORT_NAMES."""
    import importlib.metadata as md
    try:
        tops = (md.distribution(pkg).read_text("top_level.txt") or "").split()
        if tops: return tops[0]
    except md.PackageNotFoundError: pass
    return IMPORT_NAMES.get(pkg.lower(), pkg.replace("-", "_"))


def missing_packages():
    """The packages of requirements-ci.txt that this Python cannot import, and a version warning for playwright."""
    import importlib.util, importlib.metadata as md
    req = (ROOT / "requirements-ci.txt").read_text() if (ROOT / "requirements-ci.txt").is_file() else ""
    names = [m.group(1) for m in re.finditer(r"^([A-Za-z0-9_.-]+)", req, re.M)]
    gone = [n for n in names if importlib.util.find_spec(import_name(n)) is None]
    warn = []
    pin = re.search(r"^playwright==([0-9.]+)", req, re.M)
    if pin and "playwright" not in gone:
        have = md.version("playwright")
        if have != pin.group(1): warn.append(f"playwright {have} here, requirements-ci.txt pins {pin.group(1)}: browser checks run in CI's image (ci_env.py), pip install -r requirements-ci.txt matches the session")
    return gone, warn


def preflight():
    """0 when the round can start; 1 with a message that says what to do."""
    gone, warn = missing_packages()
    for w in warn: print("note: " + w)
    if gone:
        print(f"round.py: missing Python package(s): {', '.join(gone)}. Run: pip install -r requirements-ci.txt (in fysiikkalabra/)")
        return 1
    if shallow():
        print("shallow clone: reviews.py scope would answer FULL for a version not in the history; running git fetch --unshallow", flush=True)
        r = subprocess.run(["git", "fetch", "--unshallow", "origin"], cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0 or shallow():
            print("round.py: git fetch --unshallow failed" + (": " + r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "") + ". Run it yourself before the round")
            return 1
    return 0


def unit_round(uids, only, skip_checks, log, say):
    """The round's steps 2–5 for course units (work queue 0j): checks, carry, captures, packets of the Sovella task set.
    Returns the number of failures."""
    bad, failed, needed = 0, set(), {}
    if uids and not skip_checks:
        rc, out = run(["units.py", "check"], log)
        for uid in uids:
            hits = [l for l in out if uid in l]
            say(f"{uid} unit checks: " + ("FAIL" if hits else "ok")); [say("  " + l) for l in hits[:30]]
            if hits: failed.add(uid)
        if rc and not failed: bad += 1; say("FAIL units.py check (another unit): " + (out[-1] if out else f"exit {rc}"))
        for uid in uids:
            for lang in unit_languages(uid, only):
                if not has_sovella(uid, lang): continue
                for args in (["practice.py", "check", f"units/{uid}"], ["practice.py", "figures", f"units/{uid}", "--check", "--lang", lang]):
                    rc, out = run(args, log)
                    if rc: failed.add(uid); say(f"FAIL {' '.join(args)}"); [say("  " + l) for l in [l for l in out if l.strip() and not l.startswith("OK")][:10]]
        bad += len(failed)
        if failed: say(f"no packets for {', '.join(sorted(failed))}: fix the failing checks first")
    for uid in [u for u in uids if u not in failed]:
        for lang in unit_languages(uid, only):
            rc, out = run(["reviews.py", "carry-item", "unit", uid, "--lang", lang], log)
            if rc: bad += 1; say(f"FAIL carry-item {uid} {lang}: {out[-1] if out else rc}"); continue
            res = parse_item_carry(out)
            need = {n: m for n, (m, _) in res.items() if m != "none"}
            carried = [n for n, (_, c) in res.items() if c]
            _, hout = run(["units.py", "hash", uid, "--lang", lang], log)
            say(f"{uid} [{lang}] hash {hout[-1] if hout else '?'}: " + (", ".join(sorted(need, key=ROLES.index)) + " review needed" if need else "nothing to review")
                + (f"; carried now: {', '.join(carried)}" if carried else ""))
            if need and not has_sovella(uid, lang): say(f"  {uid} [{lang}] has no Sovella task set: no packet to make (unit text packets do not exist)"); continue
            if need: needed[(uid, lang)] = need
    for (uid, lang), need in sorted(needed.items()):
        if "visual" in need:
            rc, out = run(["screenshot.py", uid, "--lang", lang, "--if-stale"], log)
            say(f"captures {uid} [{lang}]: " + ("ok" if rc == 0 else "FAIL " + (out[-1] if out else "")) + (f" ({out[-1]})" if rc == 0 and out else ""))
            if rc: bad += 1; need.pop("visual")
    for role in ROLES:
        for (uid, lang), need in sorted(needed.items()):
            if role not in need: continue
            rc, out = run(["practice.py", "packet", f"units/{uid}", "--role", role, "--lang", lang], log)
            say(f"packet {role} {uid} [{lang}]: " + (out[-1] if rc == 0 and out else f"FAIL {out[-1] if out else rc}")); bad += rc != 0
    return bad


def main(a):
    if not a or a[0].startswith("-"): sys.exit(__doc__)
    if preflight(): return 1
    ids = a[0].split(",")
    uids = [i for i in ids if is_unit(i)]
    ids = [i for i in ids if i not in uids]             # lesson ids; the units run their own round
    only = a[a.index("--lang") + 1].split(",") if "--lang" in a else []
    parts = ["exercises"] if "--exercises" in a else ["lesson", "exercises"]
    LOG.parent.mkdir(exist_ok=True)
    summary, bad = [], 0
    def say(s): summary.append(s); print(s, flush=True)
    with LOG.open("w") as log:
        for lid in ids: courses.find_lesson(lid)        # exits with its own message for an unknown id
        bad += generate(ids + uids, log, say)
        if "--finish" in a:
            rc, out = run(["reviews.py", "verify"], log)
            errs = [l for l in out if l.startswith("ERROR")]
            say("verify: " + ("ok" if rc == 0 else f"FAIL ({len(errs)} error(s))")); [say("  " + e) for e in errs[:20]]
            bad += rc != 0
            for lid in ids:
                for lang in languages(lid, only):
                    _, out = run(["reviews.py", "status", lid, *lang_args(lang)], log)
                    say(f"[{lang}] " + (out[-1] if out else "?"))
            import units
            for uid in uids:
                for lang in unit_languages(uid, only):
                    st = units.status(uid, lang)
                    say(f"[{lang}] {uid}: {st['state']} ({', '.join(f'{k}={v}' for k, v in st['reports'].items())})")
            for args in (["build.py", "--all"], ["build.py"], ["palautus_tasks.py"]):   # palautus/ is generated from the built pages (8s)
                rc, out = run(args, log)
                warn = [l for l in out if "WARNING" in l]
                say(f"{' '.join(args)}: " + ("ok" if rc == 0 else "FAIL " + (out[-1] if out else "")) + (f", {len(warn)} WARNING line(s) (in the log)" if warn else ""))
                bad += rc != 0
            say(f"full output: {LOG.relative_to(ROOT)}"); return 1 if bad else 0

        failed = set()
        if "--skip-checks" not in a:
            for lid in ids:
                rc, out = run(["check_lesson.py", lid], log)
                fails = [l for l in out if not l.startswith(("ok ", "browser for", lid + ":"))]
                say(f"{lid} checks: " + ("ok" if rc == 0 else "FAIL"))
                if rc: failed.add(lid); [say("  " + l) for l in fails[:30]]
            for args in QUICK + [["exercise_bank.py", c] for c in sorted({courses.course_of(i) for i in ids})]:
                rc, out = run(args, log)
                if rc: bad += 1; say(f"FAIL {' '.join(args)}"); [say("  " + l) for l in [l for l in out if "FAIL" in l or "ERROR" in l][:10] or out[-5:]]
            bad += len(failed)
            if failed: say(f"no packets for {', '.join(sorted(failed))}: fix the failing checks first")

        needed = {}                                     # (lid, lang, part) -> {role: mode}
        for lid in [i for i in ids if i not in failed]:
            for lang in languages(lid, only):
                for part in parts:
                    rc, out = run(["reviews.py", "carry", lid, *lang_args(lang), *(["--exercises"] if part == "exercises" else [])], log)
                    if rc: bad += 1; say(f"FAIL carry {lid} {lang} {part}: {out[-1] if out else rc}"); continue
                    res, _ = parse_carry(out)
                    carried = [n for n, (_, c) in res.items() if c]
                    need = {n: m for n, (m, _) in res.items() if m != "none"}
                    say(f"{lid} [{lang}] {part}: " + (", ".join(f"{n} {m}" for n, m in need.items()) or "nothing to review")
                        + (f"; carried now: {', '.join(carried)}" if carried else ""))
                    if need: needed[(lid, lang, part)] = need

        shots = sorted({(lid, lang) for (lid, lang, _), need in needed.items() if "visual" in need})
        for lid, lang in shots:
            rc, out = run(["screenshot.py", lid, *lang_args(lang), "--if-stale"], log)
            say(f"captures {lid} [{lang}]: " + ("ok" if rc == 0 else "FAIL " + (out[-1] if out else "")) + (f" ({out[-1]})" if rc == 0 and out else ""))
            if rc: bad += 1; needed = {k: {r: m for r, m in v.items() if not (k[:2] == (lid, lang) and r == "visual")} for k, v in needed.items()}

        packets = []
        batch = "--batch" in a and len(ids) > 1
        for role in ROLES:
            if batch:
                for lang in sorted({k[1] for k, v in needed.items() if k[2] == "lesson" and role in v}):
                    lids = [k[0] for k, v in needed.items() if k[1] == lang and k[2] == "lesson" and role in v]
                    rc, out = run(["review_packet.py", "--batch", ",".join(lids), "--role", role, *lang_args(lang)], log)
                    packets.append((rc, f"{role} [{lang}] batch {','.join(lids)}", out))
            for (lid, lang, part), need in needed.items():
                if role not in need or (batch and part == "lesson"): continue
                rc, out = run(["review_packet.py", lid, "--role", role, *(["--exercises"] if part == "exercises" else []), *lang_args(lang)], log)
                also = part == "exercises" and need[role] == "full" and needed.get((lid, lang, "lesson"), {}).get(role) == "full"
                packets.append((rc, f"{role} {need[role]} {lid} [{lang}] {part}" + (" (the lesson packet asks for this report too)" if also else ""), out))
        for rc, what, out in packets:
            path = next((l for l in reversed(out) if re.match(r"\S+\.md: ", l)), out[-1] if out else "")
            say(f"packet {what}: " + (path if rc == 0 else "FAIL " + path)); bad += rc != 0
        if not needed and not failed and not uids: say("no review needed: every PASS holds for the current content")
        bad += unit_round(uids, only, "--skip-checks" in a, log, say)
        say(f"full output: {LOG.relative_to(ROOT)}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
