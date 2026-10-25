"""Shared Chromium launcher. Set PW_CHROMIUM=/path/to/chrome when the pip playwright version
does not match the installed browser (e.g. a pre-installed browser in a cloud sandbox).
Without PW_CHROMIUM it tries playwright's own browser first, then a pre-installed
/opt/pw-browsers/chromium, so the gate also runs in the cloud sandbox without the variable."""
import os, pathlib

FALLBACKS = ["/opt/pw-browsers/chromium/chrome-linux64/chrome", "/opt/pw-browsers/chromium/chrome-linux/chrome"]


def launch(pw, **kw):
    exe = os.environ.get("PW_CHROMIUM")
    if exe:
        return pw.chromium.launch(executable_path=exe, **kw)
    try:
        return pw.chromium.launch(**kw)
    except Exception:
        for f in FALLBACKS + sorted(str(p) for p in pathlib.Path("/opt/pw-browsers").glob("chromium-*/chrome-linux*/chrome")):
            if pathlib.Path(f).exists():
                return pw.chromium.launch(executable_path=f, **kw)
        raise
