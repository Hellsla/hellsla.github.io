"""Physics tests of the simulation models (README "Simulation models"). A simulation whose physics matters keeps it in
assets/sims/<course>/<name>/model.js, without drawing, loaded by the page before sim.js and by node here; its tests
are tests/models/<lesson-id>.test.js and sweep every setting the sim offers (masses, speeds, types), not only the
defaults: conservation laws, signs, energies, that the numerical solution does not create or lose momentum or energy.
Usage: python scripts/test_models.py [lesson-id]   (needs node; exit 1 on any failure)"""
import pathlib, shutil, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
only = sys.argv[1] if len(sys.argv) > 1 else None
node = shutil.which("node")
if not node: sys.exit("test_models.py needs node")
tests = sorted(p for p in (ROOT / "tests" / "models").glob("*.test.js") if not only or p.name == f"{only}.test.js")
bad = 0
for t in tests:
    r = subprocess.run([node, str(t)], capture_output=True, text=True, cwd=ROOT)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(f"{'ok  ' if r.returncode == 0 else 'FAIL'} {t.name[:-8]}: {out[-1] if out else ''}")
    if r.returncode: bad += 1; print("\n".join("     " + l for l in out[:-1][:40]))
# every model.js has its tests
for m in sorted((ROOT / "assets" / "sims").glob("*/*/model.js")):
    if not (ROOT / "tests" / "models" / f"{m.parent.name}.test.js").is_file():
        bad += 1; print(f"FAIL {m.relative_to(ROOT)} has no tests/models/{m.parent.name}.test.js")
print("all model tests passed" if not bad else f"{bad} model test files failed")
sys.exit(1 if bad else 0)
