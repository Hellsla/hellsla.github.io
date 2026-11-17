"""Every deterministic check of one lesson in one command. Usage: python scripts/check_lesson.py <id>

Runs the lint, the KaTeX parse check, the translation check of the lesson's own pages (check_i18n.py --lesson: every
language that has it translated; teacher 2026-11-17), a preview build, the simulation tests (when the lesson has a sim), the
inquiry tests and the answer-position check (when it has inquiry.json) and the layout check at 360, 390, 768 and 1280 px
(every state: closed, hints open, everything open; every language; in CI's browser image when Docker is here,
scripts/ci_env.py). Prints one
line per check and the output only of the ones that fail, then the lesson's review state. Exit status 1 if any
check fails. The developer runs it until everything is ok before asking for a review, so the reviewers are paid
only for what scripts cannot see; CI runs the same scripts over every lesson of every course."""
import os, pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from reviews import find_lesson, describe
import courses, ci_env
SCRIPTS = pathlib.Path(__file__).resolve().parent
PY = sys.executable
if len(sys.argv) != 2: sys.exit(__doc__)
lid = sys.argv[1]; folder = find_lesson(lid)
steps = [("lint", [PY, SCRIPTS / "lint_lesson.py", lid]),
         ("latex", [PY, SCRIPTS / "check_latex.py", folder]),
         ("i18n", [PY, SCRIPTS / "check_i18n.py", "--lesson", lid]),
         ("build", [PY, SCRIPTS / "build.py", lid])]
if courses.sim_dir(folder): steps.append(("sims", [PY, SCRIPTS / "test_sims.py", lid]))
if (folder / "inquiry.json").exists():
    steps.append(("inquiry", [PY, SCRIPTS / "test_inquiry.py", lid]))
    steps.append(("answer positions", [PY, SCRIPTS / "check_choices.py", lid]))
# the layout in CI's own browser and fonts when Docker is here (scripts/ci_env.py, work queue 5: a session's Chromium cut
# 4-9 px less than CI's); CHECK_LESSON_LOCAL_BROWSER=1 uses the session's browser instead. 360 and 390 px are the phones
# whose clipped solution formulas the reviewers kept finding (fy8-1-L2-08 en, #590); check_layout.py opens every
# solution in every language.
in_ci_image = not os.environ.get("CHECK_LESSON_LOCAL_BROWSER") and ci_env.available()
for w in (360, 390, 768, 1280):                  # closed, with hints and with everything open (check_layout.py, NOTES §8)
    cmd = ["scripts/check_layout.py", lid, "--width", str(w)]
    steps.append((f"layout {w} px", [PY, SCRIPTS / "ci_env.py", "run", "python", *cmd] if in_ci_image else [PY, *cmd]))
failed = 0; lines = []
for name, cmd in steps:
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, cwd=courses.ROOT)
    ok = r.returncode == 0
    failed += not ok
    out = (r.stdout + r.stderr).strip().splitlines()
    detail = next((l for l in reversed(out) if " passed, " in l), "") if ok and name == "inquiry" else out[-1].split(": ", 1)[-1] if ok and name == "i18n" and out else ""
    lines.append(("ok   " if ok else "FAIL ") + name + (f" ({detail.strip()})" if detail else "")); print(lines[-1])
    if not ok: print("     " + "\n     ".join([l for l in out if l.startswith(("FAIL", "ERROR", "  FAIL"))][:25] or out[-25:]))
lines.append(f"browser for the layout: {ci_env.image() if in_ci_image else 'this session, not the CI image (no Docker)'}"); print(lines[-1])
lines.append(describe(folder)); print(lines[-1])
(folder / "review").mkdir(exist_ok=True); (folder / "review/checks.txt").write_text("\n".join(lines) + "\n")   # read by review_packet.py
sys.exit(1 if failed else 0)
