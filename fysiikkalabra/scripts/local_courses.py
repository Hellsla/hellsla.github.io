"""Lukiokohtaiset opintojaksot: school-specific optional courses (teacher's brief 2026-10-30, docs/PORTAL_ARCHITECTURE.md).

local-courses.json is their registry, apart from curriculum.json (the national LOPS 2019 modules FY1–FY8), so a
local course never has to fake national goals and new_course.py never validates one. Finnish is the source; a
translation is content/<lang>/local-courses.json with the same codes and a course is published only in the
languages that have it. build.py renders each course to <CODE>.html beside the module pages and a row for it in
the front page's own section after the national modules; nothing else names a course.

A course's fields (all texts in the language of the file):
  title, subtitle, school, status        required; status "planning" = the teacher's working version, shown as such
  description                            required, one paragraph
  goals, themes                          lists of one line each (goals complete "Opintojaksolla opit …")
  modes                                  [{title, text}]: how much guidance the investigations give
  report                                 [{title, text}]: the sections of the course's report template
  prepare                                [{id, why}]: published Ruukkilabra chapters to study first, by lesson id;
                                         linked only where the language published the chapter, never a broken link
  pathway                                investigation ids in the course's order; the course page lists its published
                                         investigations in this order, any others after them by title
  python scripts/local_courses.py        validate the registry (also run by build.py and test_home.py)
"""
import json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n

REGISTRY = "local-courses.json"
STATUSES = ("planning",)                 # add one (and its lang key site.local_status_<status>) when a course needs it
TEXT_FIELDS = ("title", "subtitle", "school", "description")
esc = lambda s: _h.escape(str(s), quote=True)


def load(lang=i18n.SOURCE):
    """{code: course} published in lang: the Finnish registry with that language's texts over it. A test copy of the
    project without the registry has no local courses."""
    src = ROOT / REGISTRY
    if not src.is_file(): return {}
    base = {k: v for k, v in json.loads(src.read_text()).items() if not k.startswith("_")}
    if lang == i18n.SOURCE: return base
    tr = ROOT / "content" / lang / REGISTRY
    tr = {k: v for k, v in json.loads(tr.read_text()).items() if not k.startswith("_")} if tr.is_file() else {}
    return {k: dict(base[k], **tr[k]) for k in base if k in tr}


def validate(curriculum):
    """Error lines for the Finnish registry: codes apart from the national modules, required texts, known statuses,
    prepare ids that are lessons of curriculum.json."""
    errs = []; lessons = {l["id"] for k, m in curriculum.items() if not k.startswith("_") for l in m.get("lessons", [])}
    for code, c in load().items():
        if not re.fullmatch(r"[A-Z][A-Za-z]*\d*", code): errs.append(f"{REGISTRY} {code}: a code is letters then digits (FY10, MS1)")
        if code in curriculum: errs.append(f"{REGISTRY} {code}: the code of a national module in curriculum.json")
        errs += [f"{REGISTRY} {code}: no {f}" for f in TEXT_FIELDS + ("status",) if not str(c.get(f, "")).strip()]
        if c.get("status") not in STATUSES: errs.append(f"{REGISTRY} {code}: status {c.get('status')!r} is not one of {STATUSES}")
        for p in c.get("prepare", []):
            if p.get("id") not in lessons: errs.append(f"{REGISTRY} {code}: prepare id {p.get('id')!r} is not a lesson of curriculum.json")
            if not p.get("why"): errs.append(f"{REGISTRY} {code}: prepare {p.get('id')} has no why")
        for f in ("modes", "report"):
            errs += [f"{REGISTRY} {code}: {f}[{i}] needs title and text" for i, x in enumerate(c.get(f, [])) if not (x.get("title") and x.get("text"))]
    return errs


def home_row(code, c, T):
    """The front page row: the same anatomy as a national module's row, one link stretched over it."""
    return (f'<li class="mod-row local-row"><span class="mod-code">{code}</span>'
            f'<div class="mod-main"><h3 class="mod-title"><a class="mod-link" href="{code}.html">'
            f'<span class="visually-hidden">{code} </span>{esc(c["title"])}</a></h3>'
            f'<p class="mod-q">{esc(c["subtitle"])}</p></div>'
            f'<p class="mod-meta"><span class="mod-avail">{T("site.local_status_" + c["status"])}</span>'
            f'<span class="mod-credits">{esc(c["school"])}</span></p>'
            f'<span class="mod-go" aria-hidden="true">{T("site.open_course")}</span></li>')


def page_body(code, c, T, chapters, published, investigations=()):
    """The course landing page. chapters: lesson id -> (module code, title) in this language; published: the page
    names this language built. Planned parts say so, and a chapter not published here is named without a link."""
    status = c["status"]
    out = (f'<span class="eyebrow">{code} · {T("site.local_course_kind")}</span><h1>{esc(c["title"])}</h1>'
           f'<p class="lead">{esc(c["subtitle"])}</p>'
           f'<p class="notice local-kind" role="note">{T("site.local_distinct", school=esc(c["school"]))}</p>'
           f'<p class="notice local-status" role="note"><strong>{T("site.local_status_" + status)}.</strong> {T("site.local_status_note_" + status)}</p>'
           f'<p class="local-desc">{esc(c["description"])}</p>')
    if investigations:                   # the course's published investigations: canonical pages it refers to, never copies
        order = {i: n for n, i in enumerate(c.get("pathway", []))}
        investigations = sorted(investigations, key=lambda x: (order.get(x[0], len(order)), x[1]["title"]))
        out += (f'<h2 id="tutkimukset">{T("investigation.course_heading")}</h2><p class="section-lead">{T("investigation.course_lead")}</p><ol class="lessons local-inv">'
                + "".join(f'<li class="live"><a href="{i}.html">{esc(d["title"])}</a><span class="local-why">{esc(d["question"])}</span></li>' for i, d in investigations) + "</ol>")
    if c.get("goals"):
        out += (f'<h2 id="tavoitteet">{T("site.local_goals")}</h2><p class="section-lead">{T("site.local_goals_note")}</p>'
                '<ul class="local-goals">' + "".join(f"<li>{esc(g)}</li>" for g in c["goals"]) + "</ul>")
    if c.get("themes"):
        out += (f'<h2 id="eteneminen">{T("site.local_themes")}</h2><p class="section-lead">{T("site.local_themes_lead")}</p><ol class="lessons">'
                + "".join(f'<li class="soon"><span class="l-num">{i}</span><span>{esc(t)}</span></li>'
                          for i, t in enumerate(c["themes"], 1)) + "</ol>")
    if c.get("modes"):
        out += (f'<h2 id="tyotavat">{T("site.local_modes")}</h2><p class="section-lead">{T("site.local_modes_lead")}</p><dl class="local-modes">'
                + "".join(f'<dt>{esc(m["title"])}</dt><dd>{esc(m["text"])}</dd>' for m in c["modes"]) + "</dl>")
    if c.get("report"):
        out += (f'<h2 id="tyoselostus">{T("site.local_report")}</h2><p class="section-lead">{T("site.local_report_lead")}</p><ol class="local-report">'
                + "".join(f'<li><strong>{esc(r["title"])}</strong>: {esc(r["text"])}</li>' for r in c["report"]) + "</ol>")
    if c.get("prepare"):
        items = ""
        for p in c["prepare"]:
            mod, title = chapters[p["id"]]
            name = (f'<a href="{p["id"]}.html">{esc(title)}</a>' if f'{p["id"]}.html' in published
                    else f'<span>{esc(title)}</span> <span class="tag">{T("site.lesson_coming")}</span>')
            items += f'<li><span class="mod-code">{mod}</span> {name}<span class="local-why">{esc(p["why"])}</span></li>'
        out += f'<h2 id="valmistaudu">{T("site.local_prepare")}</h2><p class="section-lead">{T("site.local_prepare_lead")}</p><ul class="local-prepare">{items}</ul>'
    return out


if __name__ == "__main__":
    errs = validate(json.loads((ROOT / "curriculum.json").read_text()))
    print("\n".join(errs) or f"{REGISTRY}: {len(load())} course(s) ok")
    sys.exit(1 if errs else 0)
