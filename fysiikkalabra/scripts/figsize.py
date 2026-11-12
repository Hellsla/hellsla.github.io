"""A figure is never drawn larger than it was designed (teacher 2026-11-12, "osa kuvista on ihan turhan isoja", FY9
and FY14). An inline figure (`<svg ... viewBox="0 0 W H" style="max-width:100%...">`, or `max-width:min(100%,440px)`, with no width of its own) used to
stretch to the whole reading column: a 380- or 420-unit-wide diagram became 1,3–1,6 times its size, its labels about
32 px. `natural(html)` gives each such figure `width="W"`, so it shows at its own size and `max-width:100%` still
shrinks it on a narrow screen. The opening illustration (`fig-hero`) and anything with a width of its own are left
alone; the zoom dialog removes the width (lesson.js). Build step only: the figure sources stay as they are."""
import re

OPEN = re.compile(r'<svg\b[^>]*>')
VIEWBOX = re.compile(r'\sviewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+[\d.]+\s*"')


def _one(m):
    tag = m.group(0)
    if re.search(r'\swidth=', tag) or 'fig-hero' in tag or 'max-width:' not in tag: return tag
    vb = VIEWBOX.search(tag)
    if not vb: return tag
    w = vb.group(1).rstrip("0").rstrip(".") if "." in vb.group(1) else vb.group(1)
    return tag[:4] + f' width="{w}"' + tag[4:]


def natural(html):
    return OPEN.sub(_one, html)
