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
  authors                                optional: the course's authors, shown under its title
  language                               optional: the language its units are written in (FY14: "en"); the course page
                                         of every language says so and links to the units in that language's folder
  translations                           optional: the languages its units are also published in, each unit translated
                                         into content/<lang>/units/<id>/ and reviewed there (FY9: ["en", "fi-easy"],
                                         teacher 2026-11-04 "tunnit pitää olla en ja selkosuomi"; scripts/units.py); the
                                         course page of such a language links each unit's own version once it is
                                         published, the source language's page until then
  chapters                               optional: [{title, question, units: [{id, title}]}], the course's chapters and
                                         their units (scripts/units.py) in teaching order, shown as chapter cards (scripts/cardgrid.py);
                                         a unit not yet published is named as coming; a unit with "optional": true is marked ★ (optional extra material)
  sessions                               optional: about how many lessons the course is taught in; the front page
                                         says "about N lessons" instead of counting the units (FY14: 16)
  overview                               optional: one paragraph after the chapters' lead (FY14: sessions, ★, Fotoni)
  mixer                                  optional: true links the YO-sekoitin page (scripts/mixer.py) from the course
                                         page and has build.py build it in every language that publishes the course
  quotes                                 optional: [{author, paragraphs, lang?}], students' own words about the course,
                                         shown after the description as written (only typos fixed, teacher 2026-11-08);
                                         lang marks a quote kept in its own language on a page of another
  photos                                 optional: [{src, alt, width, height, caption?, wide?}], pictures in assets/pics/<code>/ (src
                                         "pics/<code>/<file>"), faces cropped out (teacher 2026-11-08); photos_heading
                                         optional, the section's heading (default site.local_photos)
  kind_note                              optional: false leaves out the note "Tämä on lukiokohtainen opintojakso …"
                                         (Kilparobotiikka, teacher 2026-11-08 "poista tuo kappale")
  theme                                  optional: "kiviruukki" = the page in Kiviruukin lukio's colours and fonts with
                                         the header symbol in them, like the Ahjo pages (Kilparobotiikka, teacher 2026-11-08)
  pathway                                investigation ids in the course's order; the course page lists its published
                                         investigations in this order, any others after them by title
  python scripts/local_courses.py        validate the registry (also run by build.py and test_home.py)
"""
import json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n

REGISTRY = "local-courses.json"
STATUSES = ("planning", "building", "ready")        # add one (and its lang key site.local_status_<status>) when a course needs it; "ready" shows no status box (teacher 2026-11-01)
TEXT_FIELDS = ("title", "subtitle", "school", "description")
esc = lambda s: _h.escape(str(s), quote=True)


def order(code):
    """Sort key of a course code: its letters, then its number as a number (FY9 < FY10 < FY14)."""
    m = re.fullmatch(r"([A-Za-z]*)(\d*)", code)
    return (m.group(1), int(m.group(2) or 0)) if m else (code, 0)


def label(code):
    """The code shown beside a course's name: a real course code (FY10) only, never an internal one (KILPAROBO), as
    Ahjo's course_name does."""
    return code if code.startswith("FY") else ""


def load(lang=i18n.SOURCE):
    """{code: course} published in lang: the Finnish registry with that language's texts over it. A test copy of the
    project without the registry has no local courses."""
    src = ROOT / REGISTRY
    if not src.is_file(): return {}
    # In course-number order (teacher 2026-11-04 "kurssit numeroiden mukaisessa järjestyksessä"): FY9 before FY10, FY14
    base = dict(sorted(((k, v) for k, v in json.loads(src.read_text()).items() if not k.startswith("_")), key=lambda kv: order(kv[0])))
    if lang == i18n.SOURCE: return base
    tr = ROOT / "content" / lang / REGISTRY
    tr = {k: v for k, v in json.loads(tr.read_text()).items() if not k.startswith("_")} if tr.is_file() else {}
    return {k: dict(base[k], **tr[k]) for k in base if k in tr}


def planned(lang=i18n.SOURCE):
    """The school's planned courses (teacher 2026-11-04): [{icon, title, text}] from the registry's "_planned", shown greyed
    out and unlinked on the front page under the school's own courses, as they have no content yet. A language's own
    content/<lang>/local-courses.json "_planned" replaces the Finnish list; a language without one shows the Finnish."""
    for f in ([ROOT / "content" / lang / REGISTRY] if lang != i18n.SOURCE else []) + [ROOT / REGISTRY]:
        if f.is_file() and "_planned" in (d := json.loads(f.read_text())): return d["_planned"]
    return []


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
        lang = c.get("language")
        if lang is not None and lang not in i18n.languages(): errs.append(f"{REGISTRY} {code}: language {lang!r} is not a site language")
        tr = c.get("translations", [])
        if tr and not (isinstance(tr, list) and lang): errs.append(f"{REGISTRY} {code}: translations is a list of languages, beside the course's language")
        errs += [f"{REGISTRY} {code}: translation {t!r} is not a site language other than {lang!r}" for t in (tr if isinstance(tr, list) else []) if t == lang or t not in i18n.languages()]
        seen = set()
        for i, ch in enumerate(c.get("chapters", []), 1):
            if not (ch.get("title") and ch.get("question") and isinstance(ch.get("units"), list)): errs.append(f"{REGISTRY} {code}: chapter {i} needs title, question and units")
            for u in ch.get("units", []):
                if not (u.get("id") and u.get("title")): errs.append(f"{REGISTRY} {code}: chapter {i}: a unit needs id and title")
                elif u["id"] in seen: errs.append(f"{REGISTRY} {code}: unit {u['id']} is listed twice")
                seen.add(u.get("id"))
        if c.get("chapters") and not lang: errs.append(f"{REGISTRY} {code}: a course with chapters of units names their language")
        for i, q in enumerate(c.get("quotes", [])):
            if not (q.get("author") and q.get("paragraphs") and all(str(x).strip() for x in q["paragraphs"])): errs.append(f"{REGISTRY} {code}: quotes[{i}] needs author and paragraphs")
            if q.get("lang") is not None and q["lang"] not in i18n.languages(): errs.append(f"{REGISTRY} {code}: quotes[{i}] lang {q['lang']!r} is not a site language")
        for i, ph in enumerate(c.get("photos", [])):
            if not (ph.get("src") and ph.get("alt") and ph.get("width") and ph.get("height")): errs.append(f"{REGISTRY} {code}: photos[{i}] needs src, alt, width and height")
            elif not (ROOT / "assets" / ph["src"]).is_file(): errs.append(f"{REGISTRY} {code}: photos[{i}] {ph['src']} is not in assets/")
        if c.get("theme") not in (None, "kiviruukki"): errs.append(f"{REGISTRY} {code}: theme {c['theme']!r} is not 'kiviruukki'")
        for f in ("modes", "report"):
            errs += [f"{REGISTRY} {code}: {f}[{i}] needs title and text" for i, x in enumerate(c.get(f, [])) if not (x.get("title") and x.get("text"))]
    from module_icons import ICONS
    for lang in i18n.languages():
        for i, x in enumerate(planned(lang)):
            if not (x.get("title") and x.get("text")): errs.append(f"{REGISTRY} _planned[{i}] ({lang}): needs title and text")
            if x.get("icon") not in ICONS: errs.append(f"{REGISTRY} _planned[{i}] ({lang}): icon {x.get('icon')!r} is not in module_icons.ICONS")
    return errs


def page_body(code, c, T, chapters, published, investigations=(), guides_html="", course_units=()):
    """The course landing page. chapters: lesson id -> (module code, title) in this language; published: the page
    names this language built. Planned parts say so, and a chapter not published here is named without a link."""
    status = c["status"]
    import module_icons
    out = (f'<div class="mod-head">{module_icons.img(code, 56, "mod-head-icon")}<div><span class="eyebrow">{label(code) + " · " if label(code) else ""}{T("site.local_course_kind")}</span><h1>{esc(c["title"])}</h1></div></div>'
           f'<p class="lead">{esc(c["subtitle"])}</p>'
           + (f'<p class="notice local-kind" role="note">{T("site.local_distinct", school=esc(c["school"]))}</p>' if c.get("kind_note", True) else "")
           + (f'<p class="notice local-status" role="note"><strong>{T("site.local_status_" + status)}.</strong> {T("site.local_status_note_" + status)}</p>' if status != "ready" else "")
           + (f'<p class="local-authors">{T("units.authors")}: {esc(", ".join(c["authors"][:-1]) + " " + T("units.and") + " " + c["authors"][-1] if len(c["authors"]) > 1 else c["authors"][0])}</p>' if c.get("authors") else "")
           + (f'<p class="notice local-language" role="note">{T("units.language_note_" + c["language"])}</p>' if c.get("language") and c["language"] != T.lang and T.lang not in c.get("translations", []) else "")
           + f'<p class="local-desc">{esc(c["description"])}</p>')
    if c.get("photos"):                  # pictures of the course's events, cropped so that no face shows (teacher 2026-11-08)
        out += (f'<h2 id="kuvia">{esc(c.get("photos_heading") or T("site.local_photos"))}</h2><div class="local-photos">'
                + "".join(f'<figure class="local-photo{" wide" if p.get("wide") else ""}"><img src="{esc(p["src"])}" alt="{esc(p["alt"])}" width="{p["width"]}" height="{p["height"]}" loading="lazy" decoding="async">'
                          + (f'<figcaption>{esc(p["caption"])}</figcaption>' if p.get("caption") else "") + '</figure>' for p in c["photos"])
                + '</div>')
    if c.get("quotes"):                  # students' own words (teacher 2026-11-08), a Finnish quote marked so on other pages
        out += f'<h2 id="kokemuksia">{T("site.local_quotes")}</h2>'
        for q in c["quotes"]:
            lang = f' lang="{q["lang"]}"' if q.get("lang") and q["lang"] != T.lang else ""
            out += (f'<figure class="local-quote"><blockquote{lang}>{"".join(f"<p>{esc(x)}</p>" for x in q["paragraphs"])}</blockquote>'
                    f'<figcaption>– {esc(q["author"])}</figcaption></figure>')
    if c.get("chapters"):                # the course's chapters and their units (scripts/units.py) as cards (scripts/cardgrid.py,
        import cardgrid, units           # teacher 2026-11-04): a section per chapter with its question, a card per unit with
        hrefs = {u: (ul, href) for u, ul, href in course_units}   # its opening illustration and question; a unit still coming is dashed
        lang_attr = f' lang="{c["language"]}"' if c.get("language") and c["language"] != T.lang and T.lang not in c.get("translations", []) else ""
        css = ROOT / "assets" / "units" / code.lower() / "units.css"
        if css.is_file(): out += f'<link rel="stylesheet" href="units/{code.lower()}/units.css">'
        out += (f'<h2 id="chapters">{T("units.chapters")}</h2><p class="section-lead">{T("units.chapters_lead")}</p>'
                + (f'<p class="section-lead local-overview">{esc(c["overview"])}</p>' if c.get("overview") else ""))
        items = ""
        for i, ch in enumerate(c["chapters"], 1):
            for j, u in enumerate(ch["units"], 1):
                lab = cardgrid.label(f'{i} · {esc(ch["title"])}', lang_attr) if j == 1 else ""   # the heading only, no question under it (teacher 2026-11-08)
                num = T("site.chapter_n", n=f"{i}.{j}"); title = f'<span{lang_attr}>{esc(u["title"])}</span>' if lang_attr else esc(u["title"])
                star = (f'<span class="tag">★ {T("units.optional_mark")}</span>') if u.get("optional") else ""
                if u["id"] in hrefs:             # the version linked: this language's, else the source language's (units.py)
                    ul, href = hrefs[u["id"]]; src = units.folder(u["id"], ul) / "unit.md"
                    text = src.read_text() if src.is_file() else ""
                    why = cardgrid.md_question(text); q_attr = f' lang="{ul}"' if ul != T.lang else ""
                    items += cardgrid.card(num, title, href, f'<span{q_attr}>{why}</span>' if q_attr and why else why, cardgrid.hero(text), star, lab=lab)
                else:
                    items += cardgrid.card(num, title, None, tags=star + f'<span class="tag">{T("site.lesson_coming")}</span>', lab=lab)
        out += cardgrid.grid(items, ' id="unit-cards"')
        if T.lang in c.get("translations", []):      # where a language link from a unit this language lacks lands (build.py link_languages)
            out += "".join(f'<p class="unavailable" id="unavailable-{u["id"]}" role="note" tabindex="-1">{T("site.unavailable_note", title=esc(u["title"]))}</p>'
                           for ch in c["chapters"] for u in ch["units"] if hrefs.get(u["id"], (T.lang,))[0] != T.lang)
    if c.get("mixer"):                   # the YO-sekoitin: every exam-style task of the site (scripts/mixer.py)
        out += (f'<h2 id="sekoitin">{T("mixer.course_heading")}</h2><p class="section-lead">{T("mixer.course_lead")}</p>'
                f'<ul class="lessons practice-link"><li class="live"><a href="yo-sekoitin.html">{T("mixer.title")}</a></li></ul>')
    if investigations:                   # the course's published investigations: canonical pages it refers to, never copies
        import investigations as inv     # the bank with its filter (teacher 2026-10-31)
        order = {i: n for n, i in enumerate(c.get("pathway", []))}
        investigations = sorted(investigations, key=lambda x: (order.get(x[0], len(order)), x[1]["title"]))
        out += (f'<h2 id="tutkimukset">{T("investigation.course_heading")}</h2><p class="section-lead">{T.count("investigation.course_lead_n", len(investigations))} '
                f'{T("investigation.bank_note")}</p>' + inv.bank(T, investigations, T.lang))
    out += guides_html                   # the TVT-ohjeet the investigations link to (scripts/guides.py), right after them
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
