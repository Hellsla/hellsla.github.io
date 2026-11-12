"""Kilparobotiikka (teacher's brief 2026-11-09): Kiviruukin lukio's VEX V5 competition team as a student-led learning and
working environment, in the school's colours like its course page (local-courses.json KILPAROBO, "theme": "kiviruukki").

jaksot/kilparobo/jakso.json is the source (Finnish; "kilparobo.json" below, the layout is scripts/jaksot.py's); jaksot/kilparobo/<lang>/jakso.json has the same shape in another language, and a
language without one shows the Finnish (fi-easy). build.py renders five pages in every language that has the course:
  KILPAROBO.html                 the start page: what the team is and how to join (five quick answers first), how the
                                 team works, the team's tools, what it is doing now, competitions and experiences (the
                                 course's photos and quotes from local-courses.json, never duplicated), Ahjo 1 and 2
  kilparobo-polku.html           the beginner's path: five stages, each with a goal, a practice, a mentor's tip and a way
                                 to show the skill; the official VEX technical guides and the Ruukkilabra chapters behind them
  kilparobo-kausi.html           the competition season in eight phases (no dates, no game: the game changes every season)
                                 and the team's development diary with a template to copy or download (nothing is stored)
  kilparobo-mentorointi.html     mentoring (students teach students) and a light model for making skills visible
  kilparobo-turvallisuus.html    safety: the mentor's and the teacher's parts kept apart; a draft until the school approves

Rules from the brief, checked by validate(): no dates, credits or season rules invented (now.text / now.updated are the
teacher's to fill; an empty now says so); every external link is https on VEX's or RECF's own sites (OFFICIAL_HOSTS);
a Ruukkilabra chapter (refs) is linked only where it is published; VEX only here, Ahjo's robotics is Arduino.

  python scripts/kilparobo.py   validate (also run by build.py)
"""
import json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n, jaksot

JAKSO = "kilparobo"                    # jaksot/kilparobo/ (scripts/jaksot.py)
SOURCE = jaksot.source(JAKSO)
CODE = "KILPAROBO"
PAGE, PATH, SEASON, MENTOR, SAFETY = "KILPAROBO.html", "kilparobo-polku.html", "kilparobo-kausi.html", "kilparobo-mentorointi.html", "kilparobo-turvallisuus.html"
SUBPAGES = (PATH, SEASON, MENTOR, SAFETY)
OFFICIAL_HOSTS = ("kb.vex.com", "www.vexrobotics.com", "api.vex.com", "www.robotevents.com", "www.roboticseducation.org", "kb.roboticseducation.org")
esc = lambda s: _h.escape(str(s), quote=True)

# 24 x 24 line icons in the text colour, decorative (the title beside each carries the meaning); the class is Ahjo's
ICONS = {
    "tools": "M14.5 5.5a4 4 0 0 0 4.9 4.9L21 12l-2 2-1.6-1.6L8 21.8a2 2 0 0 1-2.8-2.8l9.4-9.4L13 8l2-2zM3.5 3.5l4 4M6 3l-3 3",
    "code": "M8 7l-5 5 5 5M16 7l5 5-5 5M13.5 4l-3 16",
    "ruler": "M3 16.5L16.5 3 21 7.5 7.5 21zM7 12.5l2 2M10 9.5l2 2M13 6.5l2 2",
    "flag": "M5 21V4M5 4h11l-2 4 2 4H5",
    "notebook": "M6 3h11a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H6zM9 3v18M12 8h3.5M12 12h3.5",
    "path": "M5 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM19 9a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM7 17h6a3 3 0 0 0 0-6h-2a3 3 0 0 1 0-6h6",
    "calendar": "M4 6h16v14H4zM4 10h16M8 3v4M16 3v4",
    "people": "M9 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM3 20v-1a6 6 0 0 1 12 0v1M16 11a2.5 2.5 0 1 0 0-5M17.5 14a4.5 4.5 0 0 1 3.5 4.4V20",
    "shield": "M12 3l7 3v5c0 4.5-3 8.4-7 10-4-1.6-7-5.5-7-10V6zM9 12l2 2 4-4",
    "gear": "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1",
    "battery": "M3 8h15v8H3zM18 10.5h2.5v3H18M7 10.5v3M10 10.5v3",
    "power": "M12 3v8M7 6.3a7 7 0 1 0 10 0",
    "download": "M12 4v11M7 10l5 5 5-5M5 20h14",
    "copy": "M8 8h11v12H8zM5 16V4h11",
    "ext": "M14 4h6v6M20 4l-9 9M18 14v6H4V6h6",
}


def icon(name, cls="ahjo-icon"): return jaksot.icon_svg(ICONS, name, cls)
def data_file(lang=i18n.SOURCE): return jaksot.data_file(JAKSO, lang)
def load(lang=i18n.SOURCE): return jaksot.load(JAKSO, lang)
_shape, _urls = jaksot.shape_diff, jaksot.urls


def validate(lesson_ids):
    """Errors in kilparobo.json and its translations: structure, icons, links, ids."""
    if not SOURCE.is_file(): return []
    errs, d = [], load()
    for lang in i18n.languages():
        f = data_file(lang)
        if f == SOURCE: continue
        errs += [f"{f.relative_to(ROOT)}: differs from kilparobo.json at {p}" for p in _shape(d, json.loads(f.read_text()))]
        t = json.loads(f.read_text())
        for a, b in ((d["path"]["stages"], t["path"]["stages"]), (d["safety"]["topics"], t["safety"]["topics"])):
            errs += [f"{f.relative_to(ROOT)}: id {y.get('id')} should be {x.get('id')}" for x, y in zip(a, b) if x.get("id") != y.get("id")]
        errs += [f"{f.relative_to(ROOT)}: refs/href/icon differ from the source" for x, y in zip(d["path"]["stages"], t["path"]["stages"]) if x["refs"] != y["refs"]]
    for lang_d in [d] + [json.loads(data_file(l).read_text()) for l in i18n.languages() if data_file(l) != SOURCE]:
        for u in _urls(lang_d):
            m = re.match(r"https://([^/]+)/", u)
            if not m or m.group(1) not in OFFICIAL_HOSTS: errs.append(f"kilparobo.json: {u} is not https on an official VEX/RECF site (OFFICIAL_HOSTS)")
        for x in lang_d["hub"]["areas"] + lang_d["hub"]["pages"] + lang_d["safety"]["topics"]:
            if x["icon"] not in ICONS: errs.append(f"kilparobo.json: unknown icon {x['icon']}")
        n = lang_d["now"]
        if not (isinstance(n["phase"], int) and 0 <= n["phase"] <= len(lang_d["season"]["phases"])): errs.append("kilparobo.json: now.phase must be 0 (none) or a phase's number")
        if n["text"] and not re.fullmatch(r"\d{1,2}\.\d{1,2}\.\d{4}", n["updated"]): errs.append("kilparobo.json: now.text needs now.updated as d.m.yyyy")
        if len(lang_d["season"]["phases"]) != 8 or len(lang_d["path"]["stages"]) != 5: errs.append("kilparobo.json: 8 season phases and 5 path stages (the brief)")
    for s in d["path"]["stages"]:
        bad = [r for r in s["refs"] if r not in lesson_ids]
        if bad: errs.append(f"kilparobo.json: stage {s['id']} refs unknown chapters {bad}")
    if re.search(r"\bArduino\b", json.dumps(d["path"], ensure_ascii=False)): errs.append("kilparobo.json: the VEX path names Arduino (Ahjo's robotics is Arduino, VEX only here)")
    return errs


def nav(d, current):
    u = d["ui"]
    items = [(PAGE, u["nav_home"]), (PATH, u["nav_path"]), (SEASON, u["nav_season"]), (MENTOR, u["nav_mentor"]), (SAFETY, u["nav_safety"])]
    return (f'<nav class="ahjo-nav kr-nav" aria-label="{esc(u["nav_label"])}"><ul>'
            + "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{esc(t)}</a></li>' for h, t in items)
            + '</ul></nav>')


def ext_link(u, l):
    return (f'<a href="{esc(l["url"])}" rel="external noopener" target="_blank">{esc(l["title"])}{icon("ext", "ahjo-icon kr-ext")}'
            f'<span class="visually-hidden"> ({esc(u["external"])}, {esc(u["in_english"])})</span></a>')


def sec(id_, title, inner, lead="", cls=""):
    return (f'<section class="ahjo-sec kr-sec{" " + cls if cls else ""}" id="{id_}" aria-labelledby="h-{id_}"><h2 id="h-{id_}">{esc(title)}</h2>'
            + (f'<p class="ahjo-sec-lead">{esc(lead)}</p>' if lead else "") + inner + '</section>')


def ul(items, cls=""):
    return f'<ul{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>' + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>"


def page_head(d, title, lead, current):
    return (f'<header class="kr-head"><p class="ahjo-eyebrow">{esc(d["_course_title"])}</p><h1>{esc(title)}</h1>'
            f'<p class="lead">{esc(lead)}</p></header>' + nav(d, current))


def now_box(d):
    u, n, h = d["ui"], d["now"], d["hub"]
    phase = d["season"]["phases"][n["phase"] - 1]["title"] if n["phase"] else ""
    body = (f'<p>{esc(n["text"])}</p>' if n["text"] else f'<p class="kr-empty">{esc(u["now_empty"])}</p>')
    body += (f'<p class="kr-now-phase"><strong>{esc(u["now_phase"])}</strong> <a href="{SEASON}#vaihe-{n["phase"]}">{esc(phase)}</a></p>' if phase else "")
    body += (f'<p class="kr-now-date">{esc(u["now_updated"])} {esc(n["updated"])}</p>' if n["text"] else "")
    return sec("nyt", h["now_h"], f'<div class="kr-now">{body}</div>')


def hub_body(d, head, photos, quotes):
    """The start page. head: the course page's title block (local_courses.head); photos, quotes: its photo grid and the
    students' quotes (local_courses.photos_html, quotes_html), shown under Kilpailut ja kokemukset."""
    u, h = d["ui"], d["hub"]
    head = re.sub(r'<p class="local-desc">.*?</p>', "", head)   # the description is the page's meta line; the intro says it here
    quick = (f'<nav class="kr-quick" aria-labelledby="h-kr-quick"><h2 id="h-kr-quick" class="visually-hidden">{esc(u["quick_h"])}</h2><ol>'
             + "".join(f'<li><a href="{esc(q["href"])}"><span class="kr-quick-n" aria-hidden="true">{i}</span><span>{esc(q["q"])}</span></a></li>'
                       for i, q in enumerate(h["quick"], 1)) + '</ol></nav>')
    intro = sec("tule-mukaan", h["intro_h"], "".join(f"<p>{esc(p)}</p>" for p in h["intro"])
                + f'<div class="kr-join" id="mukaan"><h3>{esc(h["join_h"])}</h3><ol class="kr-steps">'
                + "".join(f"<li>{esc(x)}</li>" for x in h["join"]) + f'</ol><p class="kr-note">{esc(h["join_note"])}</p></div>', cls="kr-intro")
    areas = ('<ul class="kr-cards kr-areas">' + "".join(f'<li class="kr-card">{icon(a["icon"], "ahjo-icon kr-card-icon")}<h3>{esc(a["title"])}</h3><p>{esc(a["text"])}</p></li>'
                                             for a in h["areas"]) + '</ul>')
    team = sec("toiminta", h["team_h"], areas + ul(h["principles"], "kr-principles"), h["team_lead"])
    pages = sec("tyokalut", h["pages_h"], '<ul class="kr-cards kr-pages">' + "".join(
        f'<li class="kr-card kr-link-card"><a href="{p["href"]}">{icon(p["icon"], "ahjo-icon kr-card-icon")}<span class="kr-card-t">{esc(p["title"])}</span>'
        f'<span class="kr-card-x">{esc(p["text"])}</span></a></li>' for p in h["pages"]) + '</ul>')
    past = "".join(f'<article class="kr-past" id="{p["id"]}" aria-labelledby="h-{p["id"]}"><h4 id="h-{p["id"]}">{esc(p["title"])}</h4><p>{esc(p["text"])}</p>'
                   + (photos if p.get("photos") else "") + '</article>' for p in h["past"])
    comp = (f'<h3 id="aiemmat">{esc(h["past_h"])}</h3>{past}'
            + (f'<h3 id="kokemuksia">{esc(h["experiences_h"])}</h3>{quotes}' if quotes else "")
            + f'<h3 id="tulevat">{esc(h["upcoming_h"])}</h3><div class="kr-upcoming"><p>{esc(h["upcoming"])}</p><ul>'
            + "".join(f"<li>{ext_link(u, l)}</li>" for l in h["upcoming_links"]) + '</ul></div>')
    cols = "".join(f'<div class="kr-ahjo-col"><h3>' + (f'<a href="{c["href"]}">{esc(c["title"])}</a>' if c["href"] else esc(c["title"])) + f'</h3>{ul(c["items"])}</div>'
                   for c in h["ahjo_cols"])
    ahjo = sec("ahjo", h["ahjo_h"], f'<div class="kr-ahjo">{cols}</div><p class="kr-note">{esc(h["ahjo_note"])}</p>', h["ahjo_lead"])
    return (head + nav(d, PAGE) + quick + intro + team + pages + now_box(d)
            + sec("kilpailut", h["competitions_h"], comp, h["competitions_lead"]) + ahjo)


def path_body(d, ref):
    """ref(lesson id) -> (title, href) of a published Ruukkilabra chapter, None where it is not published."""
    u, p = d["ui"], d["path"]
    out = page_head(d, p["title"], p["lead"], PATH)
    out += (f'<p>{esc(p["how"])}</p><p class="notice kr-safety-first" role="note">{icon("shield")}<span>{esc(p["safety_first"])} '
            f'<a href="{SAFETY}">{esc(u["nav_safety"])}<span aria-hidden="true"> →</span></a></span></p>')
    out += ('<ol class="kr-stage-index">' + "".join(f'<li><a href="#{s["id"]}">{esc(s["title"])}</a></li>' for s in p["stages"]) + '</ol>')
    for i, s in enumerate(p["stages"], 1):
        refs = [r for r in (ref(x) for x in s["refs"]) if r]
        links = [ext_link(u, l) for l in s["links"]]
        inner = [f'<a href="{x["href"]}">{esc(x["title"])}</a>' for x in s.get("inner", [])]
        side = ((f'<h4>{esc(u["official"])}</h4><ul>' + "".join(f"<li>{x}</li>" for x in links) + '</ul>' if links else "")
                + (f'<h4>{esc(u["see_also"])}</h4><ul>' + "".join(f"<li>{x}</li>" for x in inner) + '</ul>' if inner else "")
                + (f'<h4>{esc(u["physics"])}</h4><ul>' + "".join(f'<li><a href="{href}">{esc(t)}</a></li>' for t, href in refs) + '</ul>' if refs else ""))
        out += (f'<section class="kr-stage" id="{s["id"]}" aria-labelledby="h-{s["id"]}"><header class="kr-stage-head"><span class="kr-stage-n" aria-hidden="true">{i}</span>'
                f'<h2 id="h-{s["id"]}"><span class="kr-stage-k">{esc(u["stage_n"].replace("{n}", str(i)))}</span> {esc(s["title"])}</h2></header>'
                f'<p class="kr-goal"><strong>{esc(u["goal"])}:</strong> {esc(s["goal"])}</p>'
                f'<div class="kr-stage-grid"><div><h3>{esc(u["topics"])}</h3>{ul(s["topics"])}'
                + (f'<p class="kr-note">{esc(s["note"])}</p>' if s.get("note") else "")
                + f'</div><div class="kr-stage-do"><div class="kr-box kr-box-practice"><h3>{esc(u["practice"])}</h3><p>{esc(s["practice"])}</p></div>'
                f'<div class="kr-box kr-box-mentor"><h3>{icon("people")}{esc(u["mentor_tip"])}</h3><p>{esc(s["mentor"])}</p></div>'
                f'<div class="kr-box kr-box-show"><h3>{esc(u["show"])}</h3><p>{esc(s["show"])}</p></div></div></div>'
                + (f'<div class="kr-stage-links">{side}</div>' if side else "") + '</section>')
    out += sec("ohjeet", p["guides_h"], '<ul class="kr-guides">' + "".join(f'<li>{ext_link(u, g)}<span>{esc(g["text"])}</span></li>' for g in p["guides"]) + '</ul>'
               + f'<p class="kr-note">{esc(p["hardware_note"])}</p>', p["guides_lead"])
    return out


def template_text(d): return "\n".join(d["season"]["template"]) + "\n"


def season_body(d, diary_href=None):
    """diary_href: Ahjo's project diary guide where it is built, for the longer guide and criteria."""
    from urllib.parse import quote
    u, s = d["ui"], d["season"]
    out = page_head(d, s["title"], s["lead"], SEASON)
    phases = '<ol class="kr-phases">' + "".join(
        f'<li class="kr-phase" id="vaihe-{i}"><h3><span class="kr-phase-n" aria-hidden="true">{i}</span>{esc(ph["title"])}</h3><p>{esc(ph["text"])}</p>'
        f'<p class="kr-phase-q"><strong>{esc(u["phase_questions"])}:</strong> {esc(" ".join(ph["questions"]))}</p>'
        f'<p class="kr-phase-o"><strong>{esc(u["phase_output"])}:</strong> {esc(ph["output"])}</p></li>' for i, ph in enumerate(s["phases"], 1)) + '</ol>'
    out += sec("kausi", s["h"], phases + f'<p class="kr-note">{esc(s["note"])}</p>')
    txt = template_text(d)
    diary = (f'<ol class="kr-diary-q">' + "".join(f"<li>{esc(q)}</li>" for q in s["diary_questions"]) + '</ol>'
             f'<div class="kr-template"><pre id="kr-pohja" tabindex="0">{esc(txt)}</pre><div class="kr-template-actions">'
             f'<button type="button" class="kr-btn" data-copy="kr-pohja" data-copied="{esc(u["copied"])}" hidden>{icon("copy")}{esc(u["copy"])}</button>'
             f'<a class="kr-btn" href="data:text/plain;charset=utf-8,{quote(txt)}" download="{esc(s["template_name"])}">{icon("download")}{esc(u["download"])} (.txt)</a>'
             f'<span class="kr-copied" role="status" aria-live="polite"></span></div></div>'
             f'<p>{esc(s["where"])}</p><p>{esc(s["notebook"])} {ext_link(u, s["notebook_link"])}</p>'
             + (f'<p>{esc(s["ahjo_diary"])} <a href="{diary_href}">{esc(s["ahjo_diary_link"])}<span aria-hidden="true"> →</span></a></p>' if diary_href else ""))
    return out + sec("paivakirja", s["diary_h"], diary, s["diary_lead"])


def mentor_body(d):
    u, m = d["ui"], d["mentor"]
    out = page_head(d, m["title"], m["lead"], MENTOR)
    out += f'<figure class="kr-principle"><blockquote><p>{esc(m["principle"])}</p></blockquote></figure>'
    out += ('<div class="kr-two">' + sec("tehtavat", m["duties_h"], ul(m["duties"]))
            + sec("muistilista", m["checklist_h"], ul(m["checklist"], "kr-check"), cls="kr-box") + '</div>')
    out += '<div class="kr-two">' + sec("kysymyksia", m["questions_h"], ul(m["questions"], "kr-q")) + sec("kaytanto", m["practical_h"], ul(m["practical"])) + '</div>'
    out += f'<p class="kr-growth">{esc(m["growth"])}</p>'
    skills = '<ul class="kr-cards kr-skills">' + "".join(
        f'<li class="kr-card"><h3>{esc(k["title"])}</h3><p class="kr-signs-h">{esc(u["signs"])}</p>{ul(k["signs"])}'
        f'<p class="kr-evidence"><strong>{esc(u["evidence"])}:</strong> {esc(k["evidence"])}</p></li>' for k in m["skills"]) + '</ul>'
    out += sec("osaaminen", m["skills_h"], skills + f'<p>{esc(m["skills_how"])}</p><p class="kr-note">{esc(m["skills_note"])}</p><p>{esc(m["diploma"])}</p>', m["skills_lead"])
    return out


def safety_body(d, ahjo_href=None):
    u, s = d["ui"], d["safety"]
    out = page_head(d, s["title"], s["lead"], SAFETY)
    out += (f'<p class="notice" role="note"><span class="ahjo-badge planned">{esc(u["draft_badge"])}</span> {esc(s["draft"])}</p>'
            f'<p class="kr-stop" role="note">{icon("power")}<strong>{esc(s["stop"])}</strong></p>')
    roles = "".join(f'<div class="kr-role kr-role-{r["who"]}"><h3>{esc(u["mentor_side"] if r["who"] == "mentor" else u["teacher_side"])}</h3>{ul(r["items"])}</div>' for r in s["roles"])
    out += sec("vastuut", s["roles_h"], f'<div class="kr-roles">{roles}</div><p class="kr-note"><strong>{esc(s["roles_note"])}</strong></p>')
    out += '<div class="kr-safety-grid">'
    for t in s["topics"]:
        out += (f'<section class="kr-safety" id="{t["id"]}" aria-labelledby="h-{t["id"]}"><h2 id="h-{t["id"]}">{icon(t["icon"])}{esc(t["title"])}</h2>{ul(t["do"])}'
                f'<p class="kr-teacher"><strong>{esc(u["teacher_side"])}:</strong> {esc(t["teacher"])}</p></section>')
    out += '</div>'
    out += (f'<p>{esc(s["ahjo"])}' + (f' <a href="{ahjo_href}">{esc(s["ahjo_link"])}<span aria-hidden="true"> →</span></a>' if ahjo_href else "") + '</p>'
            f'<p class="kr-links">{esc(u["official"])}: ' + ", ".join(ext_link(u, l) for l in s["links"]) + '</p>')
    return out


if __name__ == "__main__":
    import courses
    cur = json.loads((ROOT / "curriculum.json").read_text())
    ids = {l["id"] for k, m in cur.items() if not k.startswith("_") for l in m.get("lessons", [])}
    e = validate(ids)
    print("\n".join(e) or "kilparobo.json OK")
    sys.exit(1 if e else 0)
