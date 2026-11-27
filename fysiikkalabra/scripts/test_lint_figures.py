"""check_figures (lint_lesson.py): a figure with a picture as its base is not a "monochrome figure", however long the
alt text before the <image> tag is (work queue 32); a currentColor-only SVG still is.
Usage: python scripts/test_lint_figures.py"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import lint_lesson


class Fake:
    def __init__(self): self.found = []
    def page(self, f, line, msg): self.found.append(msg)
    warn = page


def mono(svg):
    L = Fake(); lint_lesson.check_figures(L, svg)
    return [m for m in L.found if m.startswith("monochrome figure")]


ALT = "Pitkä kuvaus " * 80
WEBP = f'<svg viewBox="0 0 600 400" role="img" aria-label="{ALT}"><title>{ALT}</title><image href="pics/FY4/x.webp" width="600" height="400"/></svg>'
SHORT = '<svg viewBox="0 0 600 400"><image href="pics/FY4/x.webp"/></svg>'
PLAIN = '<svg viewBox="0 0 600 400"><line x1="0" y1="0" x2="9" y2="9" stroke="currentColor"/></svg>'
LONG_PLAIN = PLAIN.replace('<svg viewBox="0 0 600 400">', f'<svg viewBox="0 0 600 400" aria-label="{ALT}">')
assert WEBP.index("<image ") > 600
assert not mono(WEBP), "WebP base with a long alt must not be monochrome"
assert not mono(SHORT)
assert mono(PLAIN) and mono(LONG_PLAIN), "a currentColor-only SVG is monochrome"
print("test_lint_figures: ok")
