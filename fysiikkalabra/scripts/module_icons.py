"""The module icons (teacher 2026-10-31, "moduuli-ikonit"): one hand-drawn SVG per module in
assets/shared/module-icons/<code>.svg, published as site/module-icons/ and shown on the front page's module rows
(the catalogue, the school-specific courses, Tulossa) and beside the title of the module's own page, never on a chapter.

One family: a 48 x 48 tile (cream, a thin line), forest green strokes of 2.5–2.75 units with round caps, one terracotta
accent for the physics (the force, the photon, the data points), no text, recognisable at 40–48 px. Each picture is the
module's physics, drawn correctly: FY4 a force acting on a body (its point of application marked), FY5 a mass on a
spring at its turning point beside the sinusoidal trace of its position, FY7 closed field lines from pole to pole, FY8 an
electron's transition between energy levels and the emitted photon.

An icon beside its module's name is decorative (alt=""): the name is already text, a screen reader says it once.
Usage: python scripts/module_icons.py check"""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT

DIR = ROOT / "assets/shared/module-icons"
PUBLISHED = "module-icons"          # site/module-icons/<code>.svg
# the registry: module code -> what the icon shows (the SVG's own <title>, for anyone opening the file)
ICONS = {
    "FY1": "työntömitta mittaa kappaleen paksuutta",
    "FY2": "tuulivoimala",
    "FY3": "lämpömittari",
    "FY4": "kappale ja siihen vaikuttava voima",
    "FY5": "jousivärähtelijä ja sen paikan kuvaaja",
    "FY6": "virtapiiri, jossa paristo ja lamppu",
    "FY7": "sauvamagneetti ja kenttäviivat",
    "FY8": "energiatasot ja fotonin emissio",
    "FY10": "mittauskuvaaja",
}


def file(code): return DIR / f"{code.lower()}.svg"


def src(code):
    """The icon's path relative to a page in site/ (build.rebase adds ../ for site/<lang>/), or None."""
    return f"{PUBLISHED}/{code.lower()}.svg" if code in ICONS and file(code).is_file() else None


def img(code, size=44, cls="mod-icon"):
    """A decorative <img> (the module's name is text beside it), or "" for a code without an icon."""
    s = src(code)
    return f'<img class="{cls}" src="{s}" alt="" width="{size}" height="{size}" aria-hidden="true">' if s else ""


def check():
    """Every registered icon exists, is one 48 x 48 SVG with no scripts, external references, text or emoji."""
    errs = []
    for code in ICONS:
        f = file(code)
        if not f.is_file(): errs.append(f"{code}: {f.relative_to(ROOT)} missing"); continue
        t = f.read_text()
        if 'viewBox="0 0 48 48"' not in t: errs.append(f"{code}: viewBox must be 0 0 48 48")
        if re.search(r"<script|<text|href=|url\(|@import|<image", t): errs.append(f"{code}: no scripts, text, links or images in an icon")
        if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", t): errs.append(f"{code}: no emoji")
        if "<title>" not in t: errs.append(f"{code}: the SVG needs a <title>")
    extra = {p.stem.upper() for p in DIR.glob("*.svg")} - set(ICONS)
    if extra: errs.append(f"icons without a registry entry: {sorted(extra)}")
    return errs


if __name__ == "__main__":
    errs = check()
    print("\n".join(errs) or f"ok: {len(ICONS)} module icons")
    sys.exit(1 if errs else 0)
