"""The browser of CI, locally (work queue 5, 2026-11-16). Usage:

  python scripts/ci_env.py run [--] <command ...>   run a command in CI's container: the same Playwright, Chromium and fonts
  python scripts/ci_env.py image                    print the image (from requirements-ci.txt)
  python scripts/ci_env.py check                    requirements-ci.txt and every image tag and pip line of the workflow agree (CI)

CI runs the browser checks in mcr.microsoft.com/playwright/python:v<version>-noble, the <version> that
requirements-ci.txt pins. A session's own Chromium is another build with other fonts: a formula that fits at 360 px
locally was cut 4-9 px in CI (en/fy1-1, 2026-11-13; FY4, FY5 and FY7 2026-11-16). `run` mounts the repository in that
image, installs requirements-ci.txt there and runs the command in fysiikkalabra/, so a layout, simulation or inquiry
check gives CI's verdict before the push:

  python scripts/ci_env.py run python scripts/check_layout.py fy8-1 --width 360
  python scripts/ci_env.py run python scripts/test_inquiry.py fy8-1

Run check_lesson.py itself in the session, not through `run`: it sends its layout checks to this image by itself, and
its KaTeX check needs Node, which the image does not have (CI installs it with setup-node), so inside `run` the latex
line always fails (FY1, 2026-11-16).

It needs Docker. In a Claude Code cloud session the daemon is installed but not started: `run` starts it (dockerd) when
it can; the image (about 2 GB) is pulled once per session. The session's HTTPS proxy and its CA bundle are passed in."""
import os, pathlib, re, shutil, subprocess, sys, time

ROOT = pathlib.Path(__file__).resolve().parent.parent          # fysiikkalabra/
REPO = ROOT.parent
REQ = ROOT / "requirements-ci.txt"
WORKFLOW = REPO / ".github" / "workflows" / "fysiikkalabra-ci.yml"


def version():
    m = re.search(r"^playwright==([0-9.]+)\s*$", REQ.read_text(), re.M)
    if not m: sys.exit(f"{REQ.name}: no line playwright==<version>")
    return m.group(1)


def image():
    return f"mcr.microsoft.com/playwright/python:v{version()}-noble"


def check():
    v, wf, bad = version(), WORKFLOW.read_text(), []
    tags = re.findall(r"mcr\.microsoft\.com/playwright/python:v([0-9.]+)-noble", wf)
    if not tags: bad.append("the workflow names no Playwright image")
    bad += [f"image v{t}, requirements-ci.txt playwright=={v}" for t in sorted(set(tags)) if t != v]
    for n, line in enumerate(wf.splitlines(), 1):
        if re.search(r"\bpip install\b", line) and "playwright" in line and "-r requirements-ci.txt" not in line:
            bad.append(f"line {n}: installs playwright without -r requirements-ci.txt")
    for f in sorted((REPO / ".claude").rglob("*.md")) + sorted(ROOT.glob("*.md")) + sorted((ROOT / "docs").glob("*.md")):
        for n, line in enumerate(f.read_text().splitlines(), 1):
            for p in re.findall(r"playwright==([0-9.]+)", line):
                if p != v: bad.append(f"{f.relative_to(REPO)}:{n}: playwright=={p}, requirements-ci.txt {v}")
    print("\n".join(bad) or f"ok: playwright {v} in requirements-ci.txt, the workflow's {len(tags)} images and the instructions")
    return 1 if bad else 0


def available():
    """True when Docker runs here or can be started (check_lesson.py then runs its layout checks in CI's image)."""
    if not shutil.which("docker") or os.environ.get("CI") or not REQ.is_file(): return False   # CI itself is already in the image; a copied test project has no requirements-ci.txt
    if subprocess.run(["docker", "info"], capture_output=True).returncode == 0: return True
    if shutil.which("dockerd") and os.geteuid() == 0:
        log = open(os.environ.get("TMPDIR", "/tmp") + "/dockerd.log", "a")
        subprocess.Popen(["dockerd"], stdout=log, stderr=log, start_new_session=True)
        for _ in range(60):
            time.sleep(1)
            if subprocess.run(["docker", "info"], capture_output=True).returncode == 0: return True
    return False


def docker_up():
    if not shutil.which("docker"): sys.exit("ci_env.py: Docker is not installed here; run the check in CI or where Docker is")
    if not available(): sys.exit("ci_env.py: the Docker daemon is not running and could not be started")


def run(cmd):
    if not cmd: sys.exit(__doc__)
    docker_up()
    img = image()
    if subprocess.run(["docker", "image", "inspect", img], capture_output=True).returncode != 0:
        print(f"pulling {img} (once)", file=sys.stderr)
        subprocess.run(["docker", "pull", "-q", img], check=True)
    args = ["docker", "run", "--rm", "--ipc=host", "--network", "host", "-v", f"{REPO}:{REPO}", "-w", str(ROOT),
            "-e", "PYTHONDONTWRITEBYTECODE=1"]
    for k in ("HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy", "NO_PROXY", "no_proxy", "CHECK_LAYOUT_NO_CLIPPED", "CLIPPED_KNOWN"):
        if os.environ.get(k): args += ["-e", k]   # the proxy of a cloud session, and the switches the tests give check_layout.py
    known = os.environ.get("CLIPPED_KNOWN")
    if known and pathlib.Path(known).is_file() and not pathlib.Path(known).resolve().is_relative_to(REPO): args += ["-v", f"{known}:{known}:ro"]
    ca = os.environ.get("PIP_CERT") or os.environ.get("SSL_CERT_FILE")
    if ca and pathlib.Path(ca).is_file(): args += ["-v", f"{ca}:/ci-env-ca.crt:ro", "-e", "PIP_CERT=/ci-env-ca.crt"]
    # git in the container (root) reads a checkout owned by another user; the packages go into a cache volume so a second run is quick
    inner = ("git config --global --add safe.directory '*' && "
             "python -m pip install -q --root-user-action=ignore --disable-pip-version-check -r requirements-ci.txt >&2 && "
             "exec \"$@\"")
    args += ["-v", "ruukkilabra-ci-pip:/root/.cache/pip", img, "bash", "-c", inner, "ci_env"] + cmd
    return subprocess.run(args).returncode


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["check"]: sys.exit(check())
    if a[:1] == ["image"]: print(image()); sys.exit(0)
    if a[:1] == ["run"]: sys.exit(run(a[2:] if a[1:2] == ["--"] else a[1:]))
    sys.exit(__doc__)
