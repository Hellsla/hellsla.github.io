"""FY9 exam mode and the minikokeet (work queue 11b PR 6; docs/FY9_ADAPTIVE_PLAN.md 6.4; templates/koetila.js).

The minikoe pages `fy9-minikoe-<id>.html` hold the fixed sets of kertaus/FY9.json `minikokeet` and are built from the
cards of the published unit pages themselves (no task text is copied anywhere): a task's card is cut out of the unit's
page and put into the minikoe page, so the same renderers, figures and checks produce it. The practice exam (the unit
fy9-harjoituskoe) gets the same exam mode as an optional start panel; its content does not change.

What the page does is in templates/koetila.js: until the student ends the exam (or the time ends) the hints, the
"Lähellä" and mistake feedback, the model answers and the solutions are taken out of the page; the clock only tells.
This module only prepares the data: the groups of tasks the student chooses between, the points and the minutes.

  python scripts/koetila.py check      the exam mode's sidecar data (kertaus/FY9.json "koetila") against the units (CI)
"""
import html as _h, json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import valmentaja
from courses import ROOT

PREFIX = "fy9-minikoe-"
EXAM_UNIT = "fy9-harjoituskoe"
SHORT_POINTS = valmentaja.SHORT_POINTS
MIN_PER_POINT = valmentaja.MIN_PER_POINT
UI_KEYS = ("start", "start_task", "choose", "chosen", "pause", "resume", "end", "end_confirm", "left", "over", "ended_user", "ended_time", "warn",
           "result_h", "points", "time_h", "planned", "used", "unchosen", "not_answered", "again", "again_confirm", "nostore", "min", "res_ok", "res_close", "res_no", "res_self")
KINDS = ("osa1", "aihe", "osa2", "aineisto")


def page_name(mid): return f"{PREFIX}{mid}.html"


def ui_json(T):
    """The texts koetila.js shows, as the JSON in data-t."""
    return _h.escape(json.dumps({k: T("koetila." + k) for k in UI_KEYS}, ensure_ascii=False), quote=True)


def card_of(page_html, cid):
    """The card <div ... id="cid"> of a built unit page, with everything inside it (balanced </div>), or None."""
    m = re.search(rf'<div class="activity[^>]*\bid="{re.escape(cid)}"', page_html)
    if not m: return None
    depth, start = 0, m.start()
    for t in re.finditer(r"<(/?)div\b[^>]*>", page_html[start:]):
        depth += -1 if t.group(1) else 1
        if depth == 0: return page_html[start:start + t.end()]
    return None


def _task_card(task):
    """(unit id, card id) of an index task: a short task's card is its activity id, a long task's its own id; both on the page of
    the unit in the task's href (a diagnostic task's "unit" field is the unit it revises, not the page it is on)."""
    uid, _, cid = task["href"].partition(".html#")
    return uid, cid


def groups_of(m, by_id):
    """[(group id or None, choose, [task id])] of a minikoe: the short tasks are one group when fewer are answered than listed
    (Osa I: 5 of 6), the long tasks one when the student chooses among them; every other task is required."""
    out = []
    short, long_ = m.get("short", []), m.get("long", [])
    ans = m.get("answer", len(short))
    if short: out.append(("short", ans, short) if ans < len(short) else (None, len(short), short))
    if long_: out.append(("long", m.get("choose") or len(long_), long_) if (m.get("choose") or len(long_)) < len(long_) else (None, len(long_), long_))
    return out


def spec_of(exam_id, minutes, parts, by_id):
    """The JSON koetila.js reads: the clock's length, the points, and per task its card, key, planned minutes, points and group.
    parts: [(group id or None, choose, [task id])]."""
    tasks, groups, pts = [], [], 0
    for gid, choose, ids in parts:
        if gid: groups.append({"id": gid, "choose": choose})
        each = [SHORT_POINTS if by_id[i]["kind"] != "long" else by_id[i]["points"] for i in ids]
        pts += sum(sorted(each, reverse=True)[:choose])
        for i in ids:
            t = by_id[i]; _, cid = _task_card(t)
            tasks.append({"id": cid, "key": i, "min": t["min"], "pts": SHORT_POINTS if t["kind"] != "long" else t["points"], "group": gid, "kind": "long" if t["kind"] == "long" else "short"})
    return {"id": exam_id, "minutes": minutes, "pts": pts, "tasks": tasks, "groups": groups}


def exam_spec(index):
    """The spec of the practice exam (unit fy9-harjoituskoe) from the sidecar's "koetila" and the index, or None."""
    cfg = valmentaja.side().get("koetila", {}).get(EXAM_UNIT)
    by = {t["id"]: t for t in index["tasks"] if _task_card(t)[0] == EXAM_UNIT}
    if not cfg or not by: return None
    short = [t["id"] for t in index["tasks"] if t["id"] in by and t["kind"] != "long"]
    parts = [(None, len(short), short)]
    for part, n in cfg["choose"].items():
        ids = [t["id"] for t in index["tasks"] if t["id"] in by and t["kind"] == "long" and t["part"] == part]
        parts.append((f"osa-{part.lower()}", n, ids))
    return spec_of(EXAM_UNIT, cfg["minutes"], parts, by)


def start_panel(T, spec):
    """The optional start of the exam mode on the practice exam page: one line and one button, shown by the script."""
    return (f'<div class="koetila koetila-panel" id="koetila" data-t="{ui_json(T)}" data-spec=\'{_h.escape(json.dumps(spec, ensure_ascii=False, separators=(",", ":")), quote=True)}\' hidden>'
            f'<p class="kt-lead">{T("koetila.panel_lead")}</p></div>')


def rules(T, m, by_id):
    out = []
    short, long_ = m.get("short", []), m.get("long", [])
    if short and m.get("answer", len(short)) < len(short): out.append(T("koetila.answer_rule", n=m["answer"], m=len(short)))
    if long_ and (m.get("choose") or len(long_)) < len(long_): out.append(T("koetila.choose_rule", n=m["choose"], m=len(long_)))
    return out


def title_of(T, m, chapters):
    if m["kind"] == "aihe": return T("koetila.title_aihe", name=chapters.get(m["chapter"], str(m["chapter"])))
    n = m["id"].rsplit("-", 1)[-1]          # the sets of one kind are told apart by their number: "Minikoe 60 min: Osa II (2)"
    return f'{T("koetila.title_" + m["kind"])} ({n})'


def mini_titles(T, index, chapters):
    """{minikoe id: title} for the coach page's list."""
    return {m["id"]: title_of(T, m, chapters) for m in index.get("minikokeet", [])}


def page_body(T, m, by_id, pages, chapters):
    """(body html, toc html) of one minikoe page, or None when a card is missing (a unit not built in this run). pages: {unit id: its built html}."""
    cards = []
    n = 0
    spec = spec_of(m["id"], m["minutes"], groups_of(m, by_id), by_id)
    order = [i for _, _, ids in groups_of(m, by_id) for i in ids]
    for i in order:
        t = by_id[i]; uid, cid = _task_card(t)
        card = card_of(pages.get(uid, ""), cid)
        if not card: return None
        n += 1
        pts = SHORT_POINTS if t["kind"] != "long" else t["points"]
        card = re.sub(r'(<div class="activity[^>]*\bid="[^"]+")', rf'\1 data-kt="{_h.escape(i, quote=True)}" data-unit="{uid}"', card, count=1)
        name = _h.escape(re.sub(r"^\d+\.\s*", "", t["title"])) if t["title"] != cid else T("lesson.exercise_word") + " " + str(n)   # a task with no title of its own is "Tehtävä 3"
        head = f'<h3>{n}. {name} <span class="pts">{T.count("practice.task_points", pts)}</span></h3>'
        if "<h3>" in card: card = re.sub(r"<h3>.*?</h3>", lambda _: head, card, count=1, flags=re.S)
        else: card = re.sub(r"(<div class=\"activity[^>]*>)", lambda m: m.group(1) + head, card, count=1)
        card = re.sub(r'<p class="act-core">.*?</p>', "", card, count=1, flags=re.S)
        cards.append(card)
    rule = "".join(f"<li>{r}</li>" for r in rules(T, m, by_id))
    title = title_of(T, m, chapters)
    head = (f'<header class="practice-head exam-head"><span class="eyebrow">{T("koetila.eyebrow")}</span><h1>{_h.escape(title)}</h1>'
            f'<p class="lead">{T("koetila.mini_lead", minutes=m["minutes"], points=m["points"])}</p>'
            + (f'<ul class="kt-rules">{rule}</ul>' if rule else "") + "</header>")
    root = (f'<div class="koetila" id="koetila" data-t="{ui_json(T)}" data-spec=\'{_h.escape(json.dumps(spec, ensure_ascii=False, separators=(",", ":")), quote=True)}\' data-page="mini">'
            f'<noscript><p class="notice" role="note">{T("koetila.nojs")}</p></noscript></div>')
    return head + root + f'<section class="stage kt-stage" id="kt-tasks">{"".join(cards)}</section>', ""


# ---- check ----------------------------------------------------------------------------------------------------------

def check():
    errs = []
    s = valmentaja.side(); cfg = s.get("koetila", {})
    tasks = valmentaja._all_tasks()
    for uid, c in cfg.items():
        if uid not in valmentaja.fy9_units(): errs.append(f"koetila.{uid}: not a FY9 unit"); continue
        extra = sorted(set(c) - {"minutes", "choose"})
        if extra: errs.append(f"koetila.{uid}: unknown field {extra}")
        mine = [t for t in tasks.values() if _task_card(t)[0] == uid]
        short = [t for t in mine if t["kind"] != "long"]
        pts = len(short) * SHORT_POINTS
        for part, n in c.get("choose", {}).items():
            same = [t for t in mine if t["kind"] == "long" and t["part"] == part]
            if not same or not 1 <= n <= len(same): errs.append(f"koetila.{uid}.choose.{part}: choose 1-{len(same)} of the part's tasks"); continue
            if len({t["points"] for t in same}) > 1: errs.append(f"koetila.{uid}.choose.{part}: the tasks of a part are worth the same"); continue
            pts += n * same[0]["points"]
        if not isinstance(c.get("minutes"), int) or abs(c["minutes"] - pts * MIN_PER_POINT) > max(3, pts * MIN_PER_POINT // 10):
            errs.append(f"koetila.{uid}: minutes {c.get('minutes')} differ from {pts} points x {MIN_PER_POINT} min = {pts * MIN_PER_POINT}")
    for m in s.get("minikokeet", []):    # a minikoe page needs a card id that is unique on the page (the unit pages repeat ids such as lt-1)
        ids = [_task_card(tasks[i])[1] for i in m.get("short", []) + m.get("long", []) if i in tasks]
        dup = sorted({i for i in ids if ids.count(i) > 1})
        if dup: errs.append(f"minikokeet.{m['id']}: card ids repeat on the page: {dup}")
    return errs


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd != "check": sys.exit(__doc__)
    e = check()
    for x in e: print("ERROR", x)
    print(f"koetila: {len(e)} error(s)" if e else "koetila: ok")
    sys.exit(1 if e else 0)
