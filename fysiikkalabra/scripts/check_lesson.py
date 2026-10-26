"""Every deterministic check of one lesson in one command. Usage: python scripts/check_lesson.py <id>

Runs the lint, the KaTeX parse check, a preview build, the simulation tests (when the lesson has a sim), the
inquiry tests and the answer-position check (when it has inquiry.json) and the 360 px layout check. Prints one
line per check and the output only of the ones that fail, then the lesson's review state. Exit status 1 if any
check fails. The developer runs it until everything is ok before asking for a review, so the reviewers are paid
only for what scripts cannot see; CI runs the same scripts over every lesson of every course."""
import pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from reviews import find_lesson, describe
import courses
SCRIPTS = pathlib.Path(__file__).resolve().parent
PY = sys.executable
if len(sys.argv) != 2: sys.exit(__doc__)
lid = sys.argv[1]; folder = find_lesson(lid)
steps = [("lint", [PY, SCRIPTS / "lint_lesson.py", lid]),
         ("latex", [PY, SCRIPTS / "check_latex.py", folder]),
         ("build", [PY, SCRIPTS / "build.py", lid])]
if courses.sim_dir(folder): steps.append(("sims", [PY, SCRIPTS / "test_sims.py", lid]))
if (folder / "inquiry.json").exists():
    steps.append(("inquiry", [PY, SCRIPTS / "test_inquiry.py", lid]))
    steps.append(("answer positions", [PY, SCRIPTS / "check_choices.py", lid]))
steps.append(("layout 360 px", [PY, SCRIPTS / "check_layout.py", lid]))
failed = 0; lines = []
for name, cmd in steps:
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, cwd=courses.ROOT)
    ok = r.returncode == 0
    failed += not ok
    out = (r.stdout + r.stderr).strip().splitlines()
    detail = next((l for l in reversed(out) if " passed, " in l), "") if ok and name == "inquiry" else ""
    lines.append(("ok   " if ok else "FAIL ") + name + (f" ({detail.strip()})" if detail else "")); print(lines[-1])
    if not ok: print("     " + "\n     ".join([l for l in out if l.startswith(("FAIL", "ERROR", "  FAIL"))][:25] or out[-25:]))
lines.append(describe(folder)); print(lines[-1])
(folder / "review").mkdir(exist_ok=True); (folder / "review/checks.txt").write_text("\n".join(lines) + "\n")   # read by review_packet.py
sys.exit(1 if failed else 0)
