"""Lähtötasotesti (work queue 33.2): the 24 diagnostic tasks of the unit fy9-koe (testi-1 … testi-24, three of each module FY1–FY8) shown as one
test named "Lähtötasotesti", grouped by module, numbered once as "FY1 · 1/3 · Virheen laji". Presentation only: no task text, answer, id, storage key
or review hash changes (the tasks stay on fy9-koe.html under their own ids, which is what the answers kept in the browser and the coach's log are keyed by).
The module is read from the activity's own `fold` tag ("Kertaustesti FY1"), the number inside the module from the order, the name from the title
without its running number ("1. Virheen laji"). templates/valmentaja.js part (g) does the behaviour (first task open, next task, summary)."""
import json, re
from collections import Counter

UNIT = "fy9-koe"
INTRO = "testi-ohje"
TASK = re.compile(r"testi-\d+")


def is_task(lid, a):
    return lid == UNIT and bool(TASK.fullmatch(a["id"]))


def in_test(lid, a):
    return lid == UNIT and (a["id"] == INTRO or TASK.fullmatch(a["id"]) is not None)


LINK = re.compile(r"\[\*?([^\]\[*]+?)\*?\]\(([\w-]+\.html)\)")


def revisit(a):
    """(chapter title, page) the task's own feedback sends to ("Kertaa luvussa [*Tiheys*](fy1-7.html)"): the one named most often; None without one."""
    c = Counter(LINK.findall(json.dumps(a, ensure_ascii=False)))
    return (c.most_common(1)[0][0] if c else None)


def plan(lid, activities):
    """{activity id: (module, k, n, name, revisit)} for the diagnostic tasks, in page order; {} for any other unit."""
    if lid != UNIT: return {}
    rows = [a for a in activities if TASK.fullmatch(a["id"])]
    mods = {}
    for a in rows:
        m = re.search(r"FY\d", a.get("fold") or "")
        mods.setdefault(m.group(0) if m else "FY?", []).append(a)
    out = {}
    for mod, xs in mods.items():
        for k, a in enumerate(xs, 1):
            out[a["id"]] = (mod, k, len(xs), re.sub(r"^\d+\.\s*", "", a.get("title") or a["id"]), revisit(a))
    return out


def label(p):
    """"FY1 · 1/3 · Virheen laji" (the coach names the task the same way)."""
    return f"{p[0]} · {p[1]}/{p[2]} · {p[3]}"


def wrap(T, esc, intro_html, cards):
    """The test's section: heading, the existing instruction, one closed box per module with its three cards (cards: [(module, card html)])."""
    mods = []
    for mod, html in cards:
        if not mods or mods[-1][0] != mod: mods.append((mod, []))
        mods[-1][1].append(html)
    body = "".join(f'<details class="lt-mod" data-mod="{esc(m)}"><summary><span class="lt-name">{esc(m)}</span> <span class="lt-count" aria-hidden="true"></span></summary>'
                   + "".join(h) + '<div class="lt-sum" hidden></div></details>' for m, h in mods)
    return (f'<section class="lt" id="lahtotasotesti" data-revise="{esc(T("inquiry.lt_revise"))}" data-next="{esc(T("inquiry.lt_next"))}" '
            f'data-review="{esc(T("inquiry.lt_review"))}" data-coach="FY9-valmentaja.html" data-coach-t="{esc(T("coach.title"))}">'
            f'<h3 class="lt-h">{esc(T("inquiry.lt_title"))}</h3>{intro_html}{body}</section>')
