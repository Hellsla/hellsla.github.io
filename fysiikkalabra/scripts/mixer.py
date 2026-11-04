"""YO-sekoitin: one page that mixes every published exam-style task of the site (teacher 2026-11-04, FY9 plan,
docs/FY9_PLAN.md). The page lists the Sovella itsenäisesti tasks of the modules and the task sets of the review units of
a local course that has `"mixer": true` in local-courses.json (FY9). Each task is a card: its title, where it is, its
points, and the chapters whose skills it uses (`skills`, shown by chapter name). A search field and three selects
(module, competency, kind of part) narrow the list in place, and "Arvo kolme tehtävää" picks a random set among the
matching tasks (templates/invfilter.js, the same component as the investigation bank). Nothing is written by hand:
the list comes from the published task sets, so a task appears here once its own page is published.

  build.py calls page_body(T, items(...)) for every language whose local courses include one with "mixer".
"""
import sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, practice, units

PAGE = "yo-sekoitin.html"
KINDS = ("calc", "graph", "word")
esc = lambda s: _h.escape(str(s), quote=True)


def _entry(task, href, where, own_module, fw):
    tags = sorted({c.get("tag") or fw["criteria"].get(c.get("key"), "") for p in task["parts"] for c in p["criteria"]} - {""})
    mods = sorted(({own_module} | {courses.course_of(l) for l in task.get("skills", [])}) - {None}, key=lambda m: int(m[2:]) if m[2:].isdigit() else 99)
    return {"id": task["id"], "title": task["title"], "href": href, "where": where, "points": practice.total(task),
            "modules": mods, "tags": tags, "kinds": sorted({p["kind"] for p in task["parts"]} & set(KINDS)),
            "skills": task.get("skills", []), "text": task.get("text", "")}


def items(lang, T, course_codes, unit_pub):
    """[entry] of every published task: the modules' Sovella sets (course_codes: the courses whose set this build
    published) and the review units' task sets (unit_pub: {unit id: language} of the published units)."""
    fw = practice.framework(); out = []
    for code in course_codes:
        for n, t in enumerate(practice.load(code, lang)["tasks"], 1):   # n: the task's number on its page (practice.number)
            if t.get("kind") == "own": continue
            out.append(_entry(t, f"{practice.page_name(code)}#{t['id']}", f"{code} · {T('practice.title')} · {T('practice.task_n', n=practice.number(n))}", code, fw))
    for uid, ul in unit_pub.items():
        if ul != lang or not units.has_tasks(uid, lang): continue
        d = units.load(uid, lang)
        for n, t in enumerate(practice.load(units.task_key(uid), lang)["tasks"], 1):
            if t.get("kind") == "own": continue
            out.append(_entry(t, f"{uid}.html#{t['id']}", f"{d['course']} · {d['title']} · {T('practice.task_n', n=practice.number(n, units.number(uid)))}", None, fw))
    return out


def page_body(T, entries):
    """The page: heading, lead, the filter form and the list of task cards (each a link to the task on its page)."""
    mods = sorted({m for e in entries for m in e["modules"]}, key=lambda m: int(m[2:]) if m[2:].isdigit() else 99)
    def opt(name, label, values):
        return (f'<div class="bank-field"><label for="bank-{name}">{label}</label><select id="bank-{name}" name="{name}">'
                f'<option value="">{T("investigation.filter_all")}</option>'
                + "".join(f'<option value="{v}">{esc(t)}</option>' for v, t in values) + "</select></div>")
    form = (f'<form class="bank-filter" id="bank-filter" hidden role="search" aria-label="{T("mixer.filter_label")}">'
            f'<div class="bank-field bank-search"><label for="bank-q">{T("mixer.search")}</label>'
            f'<input id="bank-q" name="q" type="search" autocomplete="off"></div>'
            + opt("module", T("mixer.module"), [(m, m) for m in mods])
            + opt("tag", T("mixer.competency"), [(c, T("competency." + c)) for c in practice.framework()["competencies"]])
            + opt("kind", T("mixer.kind"), [(k, T("mixer.kind_" + k)) for k in KINDS])
            + f'<button type="button" class="bank-reset bank-random" data-random="3">{T("mixer.random")}</button>'
            f'<button type="reset" class="bank-reset">{T("investigation.filter_reset")}</button>'
            f'<p class="bank-count" id="bank-count" aria-live="polite" data-template="{esc(T("mixer.count"))}"></p></form>')
    rows = ""
    for e in entries:
        words = " ".join([e["title"], e["where"], e["text"]] + [practice.chapter(l) for l in e["skills"]]).lower()
        skills = (f'<span class="bank-mods">{T("practice.skills")} ' + ", ".join(esc(practice.chapter(l)) for l in e["skills"]) + "</span>") if e["skills"] else ""
        meta = (f'<span class="bank-topic">{esc(e["where"])}</span><span class="bank-level">{T.count("practice.task_points", e["points"])}</span>'
                f'<span class="bank-modes">{", ".join(T("competency." + t) for t in e["tags"])}</span>{skills}')
        rows += (f'<li class="live bank-item" data-module="{" ".join(e["modules"])}" data-tag="{" ".join(e["tags"])}" data-kind="{" ".join(e["kinds"])}" '
                 f'data-words="{esc(words)}"><a href="{e["href"]}">{esc(e["title"])}</a><span class="bank-meta">{meta}</span></li>')
    return (f'<h1>{T("mixer.title")}</h1><p class="lead">{T("mixer.lead")}</p><p class="section-lead">{T("mixer.howto")}</p>'
            + form + f'<p class="bank-none" id="bank-none" hidden>{T("mixer.none")}</p>'
            f'<ol class="lessons local-inv bank-list" id="bank-list">{rows}</ol>')
