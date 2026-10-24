"""Shared Chromium launcher. Set PW_CHROMIUM=/path/to/chrome when the pip playwright version
does not match the installed browser (e.g. a pre-installed browser in a cloud sandbox)."""
import os
def launch(pw, **kw):
    exe = os.environ.get("PW_CHROMIUM")
    return pw.chromium.launch(executable_path=exe, **kw) if exe else pw.chromium.launch(**kw)
