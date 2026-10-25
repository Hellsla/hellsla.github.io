"""Every deterministic check of one lesson in one command. Usage: python scripts/check_lesson.py <id>

Runs the lint, the KaTeX parse check, a preview build, the simulation tests (when the lesson has a sim) and
the 360 px layout check. Prints one line per check and the output only of the ones that fail, then the
lesson's review state. Exit status 1 if any check fails. The developer runs it until everything is ok before
asking for a review; CI runs the same scripts over every lesson."""
import pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from reviews import find_lesson, describe
SCRIPTS = pathlib.Path(__file__).resolve().parent
PY = sys.executable
if len(sys.argv) != 2: sys.exit(__doc__)
lid = sys.argv[1]; folder = find_lesson(lid)
steps = [("lint", [PY, SCRIPTS / "lint_lesson.py", lid]),
         ("latex", [PY, SCRIPTS / "check_latex.py", folder]),
         ("build", [PY, SCRIPTS / "build.py", lid])]
if (folder / "sim.js").exists(): steps.append(("sims", [PY, SCRIPTS / "test_sims.py", lid]))
steps.append(("layout 360 px", [PY, SCRIPTS / "check_layout.py", lid]))
failed = 0
for name, cmd in steps:
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, cwd=SCRIPTS.parent)
    ok = r.returncode == 0
    failed += not ok
    print(("ok   " if ok else "FAIL ") + name)
    if not ok: print("     " + "\n     ".join((r.stdout + r.stderr).strip().splitlines()[-25:]))
print(describe(folder))
sys.exit(1 if failed else 0)
