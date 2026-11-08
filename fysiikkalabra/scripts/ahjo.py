"""Ahjo Makerspace (teacher 2026-11-08; docs/PORTAL_ARCHITECTURE.md section C): Kiviruukin lukio's makerspace inside
Ruukkilabra, in the school's colours (navy #012169, pink #fca5c7, Lato headings, Work Sans text; site.css "Ahjo") under
the site's common header, with the original Ahjo Makerspace logo (assets/shared/brand/ahjo-makerspace-logo.svg, the
teacher's file byte for byte: never redrawn, recoloured or cropped; LOGO_SHA256 pins it).

ahjo.json is the source (Finnish); content/<lang>/ahjo.json has the same ids in another language, and a language
without one shows the Finnish (fi-easy). build.py renders three pages in every language:
  ahjo.html               the start page: what Ahjo is, Ahjo 1 and Ahjo 2, the bank's topics, the equipment, safety,
                          and the studies linked to Ahjo
  ahjo-materiaalit.html   the resource bank: every resource under its one category, with the courses that use it
  ahjo-turvallisuus.html  the safety section: its topics and their status

Fields of ahjo.json (texts in the file's language):
  title, eyebrow, lead, opening, description   the start page's heading and its lines
  ui                       the section's interface texts; a count is {"one", "other"} with {n}
  courses                  [{code, subtitle, topics, goals?, lessons?, plan_status?}] (goals complete "Opintojaksolla
                           opit"; lessons: 16 x {title, text, example?}; plan_status "draft" until the teacher approves): Ahjo 1 and Ahjo 2. Their name and one-line description come
                           from local-courses.json ("_planned" by icon code, or the course itself once it is a real
                           local course with its own page, which is then linked): one source, never written twice
  categories               [{id, icon, title, text}]: the bank's main categories, in order (ICONS names the icon)
  resources                one entry per resource, each in exactly one category (its one home):
                             {ref, category, why, courses}         an existing Ruukkilabra page (a chapter, an
                                                                    investigation or a TVT-ohje) by its id, linked only
                                                                    where it is published, never copied
                             {id, category, title, text, status, courses, subjects?}
                                                                    an Ahjo guide "ahjo-<name>": "planned" is listed as
                                                                    coming and has no page; "ready" needs its text in
                                                                    content/<lang>/ahjo/<id>.md and becomes <id>.html
                             {safety: true, category, courses}     the safety section
                           courses: course codes that use the resource (a module, a local or a planned course);
                           subjects: other subjects it suits, as plain words (not courses)
  equipment_status         "tuleva" (coming, the heading says "Ahjon tuleva laitteisto") or "kaytossa"; an item
                           may be {"name", "status"} to differ from it, so no structure changes when devices arrive
  equipment                [{id, icon, title, items}]: equipment groups; what the school's list names, no models
  safety                   [{id, title, covers, status?, approved_by?, date?}]: the safety topics. Status
                           "valmisteilla" (default) shows the topic as being prepared; "hyvaksytty" needs approved_by,
                           date and the text in content/<lang>/ahjo/turvallisuus/<id>.md (the Finnish as fallback).
                           Only the school's responsible staff approve a topic; nothing here is an approval system
  links                    [{course, text, categories}]: Ruukkilabra studies linked to Ahjo (existing codes only)

  python scripts/ahjo.py   validate (also run by build.py)
"""
import hashlib, json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n

SOURCE = ROOT / "ahjo.json"
LOGO = ROOT / "assets/shared/brand/ahjo-makerspace-logo.svg"
LOGO_SRC = "brand/ahjo-makerspace-logo.svg"
LOGO_SHA256 = "53cb75c6c45b7adef3d57c59c75cdc2bb220d25ccf75faa71858a27d59823e26"   # Ahjo_Makerspace_logo.svg as the teacher gave it (2026-11-08)
PAGE, BANK, SAFETY = "ahjo.html", "ahjo-materiaalit.html", "ahjo-turvallisuus.html"
EQUIPMENT_STATUSES = ("tuleva", "kaytossa")
RES_STATUSES = ("planned", "ready")
SAFETY_STATUSES = ("valmisteilla", "hyvaksytty")
# Not part of Ahjo (teacher 2026-11-08): never in its equipment, guides, tasks or texts
FORBIDDEN = re.compile(r"laser|cnc|jyrsin|mill(ing)? machine", re.I)
esc = lambda s: _h.escape(str(s), quote=True)

# 24 x 24 line icons, drawn in the text colour; decorative only (the title beside them carries the meaning)
ICONS = {
    "cube": "M12 3l8 4.5v9L12 21l-8-4.5v-9zM4 7.5l8 4.5 8-4.5M12 12v9",
    "chip": "M7 7h10v10H7zM10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4",
    "robot": "M6 8h12a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1zM12 4v4M9.5 12.5h.01M14.5 12.5h.01M9.5 15.5h5M2.5 12v3M21.5 12v3",
    "vr": "M3.5 8h17a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1h-5l-2-2.5h-3L8.5 16h-5a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z",
    "scissors": "M6 8.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5zM6 20.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5zM8 7.5L20 18M8 16.5L20 6",
    "tools": "M14.5 5.5a4 4 0 0 0 4.9 4.9L21 12l-2 2-1.6-1.6L8 21.8a2 2 0 0 1-2.8-2.8l9.4-9.4L13 8l2-2zM3.5 3.5l4 4M6 3l-3 3",
    "shield": "M12 3l7 3v5c0 4.5-3 8.4-7 10-4-1.6-7-5.5-7-10V6zM9 12l2 2 4-4",
    "notebook": "M6 3h11a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H6zM9 3v18M12 8h3.5M12 12h3.5",
    "box": "M3 8l9-4 9 4v10l-9 4-9-4zM3 8l9 4 9-4M12 12v10",
}


ART = ROOT / "assets/shared/ahjo"   # the section's illustrations (scripts/ahjo_art.py), inlined


def art(name):
    f = ART / f"{name}.svg"
    return f.read_text().strip() if f.is_file() else ""


def icon(name, cls="ahjo-icon"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">'
            f'<path d="{ICONS[name]}"/></svg>')


def data_file(lang=i18n.SOURCE):
    f = ROOT / "content" / lang / "ahjo.json"
    return f if lang != i18n.SOURCE and f.is_file() else SOURCE


def load(lang=i18n.SOURCE):
    return json.loads(data_file(lang).read_text()) if SOURCE.is_file() else None


def guide_file(gid, lang): return next((f for f in (ROOT / "content" / lang / "ahjo" / f"{gid}.md", ROOT / "content" / i18n.SOURCE / "ahjo" / f"{gid}.md") if f.is_file()), None)
def safety_file(sid, lang): return next((f for f in (ROOT / "content" / lang / "ahjo" / "turvallisuus" / f"{sid}.md", ROOT / "content" / i18n.SOURCE / "ahjo" / "turvallisuus" / f"{sid}.md") if f.is_file()), None)


def item_name(it): return it if isinstance(it, str) else it["name"]


def texts_of(x):
    """Every string in a piece of the data, for the forbidden-equipment check."""
    if isinstance(x, str): yield x
    elif isinstance(x, dict):
        for k, v in x.items():
            if not k.startswith("_"): yield from texts_of(v)
    elif isinstance(x, list):
        for v in x: yield from texts_of(v)


def validate(lessons, investigations, guides, planned_codes, local_codes, modules):
    """Error lines for ahjo.json and its translations: known categories, icons and statuses, refs that exist, course
    codes that exist (a module, a local course or a planned one: no new courses here), unique ids, no equipment the
    school will not have, the logo unchanged, and every translation with the source's ids."""
    if not SOURCE.is_file(): return []
    errs = []
    if not LOGO.is_file() or hashlib.sha256(LOGO.read_bytes()).hexdigest() != LOGO_SHA256:
        errs.append(f"{LOGO.relative_to(ROOT)}: missing or not the teacher's original Ahjo Makerspace logo")
    known_codes = set(planned_codes) | set(local_codes) | set(modules)
    src = load()
    shape = lambda d: ([c["code"] for c in d["courses"]], [c["id"] for c in d["categories"]],
                       [r.get("ref") or r.get("id") or "safety" for r in d["resources"]], [g["id"] for g in d["equipment"]],
                       [len(g["items"]) for g in d["equipment"]], [(len(c.get("goals", [])), len(c.get("lessons", []))) for c in d["courses"]], [s["id"] for s in d["safety"]], [l["course"] for l in d["links"]], sorted(d["ui"]))
    files = [SOURCE] + sorted((ROOT / "content").glob("*/ahjo.json"))
    for f in files:
        name = f.relative_to(ROOT)
        try: d = json.loads(f.read_text())
        except Exception as e: errs.append(f"{name}: {e}"); continue
        for k in ("title", "eyebrow", "lead", "opening", "description", "ui", "courses", "categories", "resources", "equipment_status", "equipment", "safety", "links"):
            if k not in d: errs.append(f"{name}: no {k}")
        if any(k not in d for k in ("courses", "categories", "resources", "equipment", "safety", "links", "ui")): continue
        if f != SOURCE:
            try:
                if shape(d) != shape(src): errs.append(f"{name}: its ids, items or ui keys differ from ahjo.json")
            except (KeyError, TypeError) as e: errs.append(f"{name}: {e}")
        bad = sorted({m.group(0) for t in texts_of(d) for m in [FORBIDDEN.search(t)] if m})
        if bad: errs.append(f"{name}: names equipment that is not coming to Ahjo ({', '.join(bad)})")
        cats = [c["id"] for c in d["categories"]]
        if len(set(cats)) != len(cats): errs.append(f"{name}: repeated category ids")
        for c in d["categories"] + d["equipment"]:
            if c.get("icon") not in ICONS: errs.append(f"{name}: {c.get('id')}: unknown icon {c.get('icon')!r}")
        for c in d["courses"]:
            if c["code"] not in set(planned_codes) | set(local_codes): errs.append(f"{name}: course {c['code']} is neither a local nor a planned course")
            if not c.get("topics"): errs.append(f"{name}: {c['code']} has no topics")
            if c.get("lessons") and (len(c["lessons"]) != 16 or not all(l.get("title") and l.get("text") for l in c["lessons"])):
                errs.append(f"{name}: {c['code']}: 16 lessons, each with a title and a text (teacher 2026-11-08)")
            if c.get("plan_status", "draft") not in ("draft", "approved"): errs.append(f"{name}: {c['code']}: plan_status draft or approved")
        seen = set()
        for r in d["resources"]:
            rid = r.get("ref") or r.get("id") or ("safety" if r.get("safety") else None)
            if not rid: errs.append(f"{name}: a resource without ref, id or safety"); continue
            if rid in seen: errs.append(f"{name}: {rid} is listed twice (a resource has one home)")
            seen.add(rid)
            if r.get("category") not in cats: errs.append(f"{name}: {rid}: unknown category {r.get('category')!r}")
            for code in r.get("courses", []):
                if code not in known_codes: errs.append(f"{name}: {rid}: unknown course {code}")
            if "ref" in r:
                if rid not in lessons | investigations | guides: errs.append(f"{name}: {rid}: no such chapter, investigation or TVT-ohje")
                if not r.get("why"): errs.append(f"{name}: {rid}: no why")
            elif "id" in r:
                if not rid.startswith("ahjo-") or not re.fullmatch(r"[a-z0-9-]+", rid): errs.append(f"{name}: {rid}: an Ahjo guide's id is ahjo-<lowercase-name>")
                if r.get("status") not in RES_STATUSES: errs.append(f"{name}: {rid}: status must be one of {RES_STATUSES}")
                if not r.get("title") or not r.get("text"): errs.append(f"{name}: {rid}: no title or text")
                if r.get("status") == "ready" and not guide_file(rid, i18n.SOURCE): errs.append(f"{name}: {rid}: ready but content/fi/ahjo/{rid}.md is missing")
        if d["equipment_status"] not in EQUIPMENT_STATUSES: errs.append(f"{name}: equipment_status must be one of {EQUIPMENT_STATUSES}")
        for g in d["equipment"]:
            for it in g["items"]:
                if not isinstance(it, str) and it.get("status") not in EQUIPMENT_STATUSES: errs.append(f"{name}: {g['id']}: {it}: unknown status")
        for s in d["safety"]:
            st = s.get("status", "valmisteilla")
            if st not in SAFETY_STATUSES: errs.append(f"{name}: safety {s['id']}: status must be one of {SAFETY_STATUSES}")
            if st == "hyvaksytty" and not (s.get("approved_by") and s.get("date") and safety_file(s["id"], i18n.SOURCE)):
                errs.append(f"{name}: safety {s['id']}: approved needs approved_by, date and content/fi/ahjo/turvallisuus/{s['id']}.md")
        for l in d["links"]:
            if l["course"] not in known_codes: errs.append(f"{name}: link to unknown course {l['course']}")
            for c in l.get("categories", []):
                if c not in cats: errs.append(f"{name}: link {l['course']}: unknown category {c}")
    return errs


# --- rendering ---------------------------------------------------------------------------------------------------

def count(ui, key, n): return ui[key]["one" if n == 1 else "other"].replace("{n}", str(n))


def nav(d, current):
    u = d["ui"]
    items = [(PAGE, u["nav_home"]), (PAGE + "#opintojaksot", u["nav_courses"]), (BANK, u["nav_bank"]),
             (PAGE + "#laitteisto", u["nav_equipment"]), (SAFETY, u["nav_safety"])]
    return (f'<nav class="ahjo-nav" aria-label="{esc(u["nav_label"])}"><ul>'
            + "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{esc(t)}</a></li>' for h, t in items)
            + '</ul></nav>')


def hero(d, title, lead, current, big=False, extra=""):
    """The section's own banner: the original logo (large on the start page), the school's line, the heading."""
    size = 168 if big else 88
    return (f'<header class="ahjo-hero{" ahjo-hero-big" if big else ""}">'
            f'<img class="ahjo-logo" src="{LOGO_SRC}" alt="{esc(d["ui"]["logo_alt"])}" width="{size}" height="{size}">'
            f'<div class="ahjo-hero-text"><p class="ahjo-eyebrow">{esc(d["eyebrow"])}</p><h1>{esc(title)}</h1>'
            f'<p class="ahjo-lead">{esc(lead)}</p>{extra}</div></header>' + nav(d, current))


def course_info(code, planned, local):
    """(title, text, href or None) of an Ahjo course: a real local course links its page; a planned one is text."""
    if code in local: return local[code]["title"], local[code]["description"], f"{code}.html"
    p = next((p for p in planned if p.get("icon") == code), None)
    return (p["title"], p["text"], None) if p else (code, "", None)


def course_name(code, planned, local, modules):
    """(label, href or None, planned?) of any course code for the chips and the links section."""
    if code in modules: return f"{code} {modules[code]}", f"{code}.html", False
    if code in local: return f"{code} {local[code]['title']}" if code.startswith("FY") else local[code]["title"], f"{code}.html", False
    p = next((p for p in planned if p.get("icon") == code), None)
    return (p["title"] if p else code), None, True


def resolve(d, ref):
    """The bank's entries in display form: [(category, entry)] where entry = dict(kind, title, href, text, ready, fi_only,
    courses, subjects). ref(id) -> (title, kind, fi_only) for a published page, None otherwise."""
    u = d["ui"]; out = []
    for r in d["resources"]:
        e = {"courses": r.get("courses", []), "subjects": r.get("subjects", []), "fi_only": False}
        if "ref" in r:
            got = ref(r["ref"])
            if got: e.update(title=got[0], kind=u["kind_" + got[1]], href=f'{r["ref"]}.html', text=r["why"], ready=True, fi_only=got[2])
            else: continue                         # not published in any language yet: not listed (never a dead link)
        elif r.get("safety"):
            done = any(s.get("status") == "hyvaksytty" for s in d["safety"])
            e.update(title=u["safety_page_title"], kind=u["kind_safety"], href=SAFETY, text=u["safety_page_lead"], ready=done,
                     badge=None if done else u["safety_status_valmisteilla"])
        else:
            ready = r["status"] == "ready"
            e.update(title=r["title"], kind=u["kind_ahjo"], href=f'{r["id"]}.html' if ready else None, text=r["text"], ready=ready)
        out.append((r["category"], e))
    return out


def chips(codes, names):
    return "".join(f'<span class="ahjo-chip">{esc(names(c)[0])}</span>' for c in codes)


def start_body(d, planned, local, modules, ref):
    u = d["ui"]; names = lambda c: course_name(c, planned, local, modules)
    res = resolve(d, ref)
    # Ahjo 1 and Ahjo 2: name and line from the course registry, topics from ahjo.json
    cards = []
    for c in d["courses"]:
        title, text, href = course_info(c["code"], planned, local)
        status = u["course_status_ready"] if href else u["course_status_planned"]
        head = f'<a href="{href}">{esc(title)}</a>' if href else esc(title)
        cards.append(f'<article class="ahjo-course" id="{c["code"].lower()}" aria-labelledby="h-{c["code"].lower()}">'
                     f'<div class="ahjo-course-art">{art(c["code"].lower())}</div><div class="ahjo-course-head"><h3 id="h-{c["code"].lower()}"><span class="ahjo-course-name">{head}</span>'
                     f'<span class="ahjo-course-sub">{esc(c["subtitle"])}</span></h3>'
                     f'<p class="ahjo-badge{"" if href else " planned"}">{esc(status)}</p></div>'
                     f'<p class="ahjo-course-text">{esc(text)}</p>'
                     f'<h4 class="visually-hidden">{esc(u["course_contents"])}</h4>'
                     f'<ul class="ahjo-topics">' + "".join(f'<li>{esc(t)}</li>' for t in c["topics"]) + '</ul>' + course_plan(u, c) + '</article>')
    courses = (f'<section class="ahjo-sec" id="opintojaksot" aria-labelledby="h-ahjo-courses"><h2 id="h-ahjo-courses">{esc(u["courses_h"])}</h2>'
               f'<p class="ahjo-sec-lead">{esc(u["courses_lead"])}</p><div class="ahjo-courses">{"".join(cards)}</div></section>')
    # the bank's topics with what is ready and what is coming
    cats = []
    for c in d["categories"]:
        mine = [e for cat, e in res if cat == c["id"]]
        ready, coming = sum(e["ready"] for e in mine), sum(not e["ready"] for e in mine)
        n = " · ".join(([count(u, "bank_ready", ready)] if ready else []) + ([count(u, "bank_coming", coming)] if coming else [])) or u["bank_none"]
        cats.append(f'<li><a href="{BANK}#{c["id"]}">{icon(c["icon"])}<span class="ahjo-cat-t">{esc(c["title"])}</span>'
                    f'<span class="ahjo-cat-n">{esc(n)}</span></a></li>')
    bank = (f'<section class="ahjo-sec" id="materiaalipankki" aria-labelledby="h-ahjo-bank"><h2 id="h-ahjo-bank">{esc(u["bank_h"])}</h2>'
            f'<p class="ahjo-sec-lead">{esc(u["bank_lead"])}</p><ul class="ahjo-cats">{"".join(cats)}</ul>'
            f'<p class="ahjo-more"><a href="{BANK}">{esc(u["bank_all"])}<span aria-hidden="true"> →</span></a></p></section>')
    return (hero(d, d["title"], d["lead"], PAGE, big=True, extra=f'<p class="ahjo-opening">{esc(d["opening"])}</p>')
            + courses + bank + equipment_section(d)
            + (f'<section class="ahjo-sec ahjo-safety-teaser" id="turvallisuus" aria-labelledby="h-ahjo-safety">{icon("shield", "ahjo-icon ahjo-icon-big")}'
               f'<div><h2 id="h-ahjo-safety">{esc(u["safety_h"])}</h2><p>{esc(u["safety_lead"])}</p><p class="ahjo-draft-short">{esc(u["safety_draft_note"].split(". ")[0])}.</p>'
               f'<p class="ahjo-more"><a href="{SAFETY}">{esc(u["safety_open"])}<span aria-hidden="true"> →</span></a></p></div></section>')
            + links_section(d, names))


def course_plan(u, c):
    """A course's goals and lesson outline as two closed boxes under its topics; a draft says so (teacher 2026-11-08:
    "tavoitteet ja 16 oppituntia", written as a draft until the teacher approves it or gives the school's own text)."""
    out = ""
    if c.get("plan_status") == "draft" and (c.get("goals") or c.get("lessons")):
        out += f'<p class="ahjo-plan-note">{esc(u["plan_draft"])}</p>'
    if c.get("goals"):
        out += (f'<details class="ahjo-plan"><summary>{esc(u["course_goals"])}</summary><p>{esc(u["course_goals_lead"])}</p>'
                f'<ul>' + "".join(f'<li>{esc(g)}</li>' for g in c["goals"]) + '</ul></details>')
    if c.get("lessons"):
        out += (f'<details class="ahjo-plan"><summary>{esc(u["course_lessons"].replace("{n}", str(len(c["lessons"]))))}</summary><ol class="ahjo-lessons">'
                + "".join(f'<li><span class="ahjo-lesson-t">{esc(l["title"])}</span> <span class="ahjo-lesson-x">{esc(l["text"])}</span>'
                           + (f'<span class="ahjo-lesson-e"><span class="ahjo-meta-l">{esc(u["lesson_example"])}:</span> {esc(l["example"])}</span>' if l.get("example") else "") + '</li>' for l in c["lessons"])
                + '</ol></details>')
    return out


def equipment_section(d):
    u = d["ui"]; st = d["equipment_status"]
    groups = []
    for g in d["equipment"]:
        items = []
        for it in g["items"]:
            own = None if isinstance(it, str) else it.get("status")
            badge = f' <span class="ahjo-badge-s">{esc(u["status_" + own])}</span>' if own and own != st else ""
            items.append(f'<li>{esc(item_name(it))}{badge}</li>')
        groups.append(f'<section class="ahjo-eq" aria-labelledby="h-eq-{g["id"]}"><h3 id="h-eq-{g["id"]}">{icon(g["icon"])}{esc(g["title"])}</h3>'
                      f'<ul>{"".join(items)}</ul></section>')
    return (f'<section class="ahjo-sec" id="laitteisto" aria-labelledby="h-ahjo-eq"><h2 id="h-ahjo-eq">{esc(u["equipment_h_" + st])}</h2>'
            f'<p class="ahjo-sec-lead">{esc(u["equipment_lead_" + st])}</p><div class="ahjo-equip">{"".join(groups)}</div></section>')


def links_section(d, names):
    u = d["ui"]; cat = {c["id"]: c for c in d["categories"]}
    rows = []
    for l in d["links"]:
        label, href, planned = names(l["course"])
        head = f'<a href="{href}">{esc(label)}</a>' if href else f'<span>{esc(label)}</span> <span class="ahjo-tag">{esc(u["links_planned"])}</span>'
        cs = "".join(f'<li><a href="{BANK}#{c}">{esc(cat[c]["title"])}</a></li>' for c in l.get("categories", []))
        rows.append(f'<li><p class="ahjo-link-name">{head}</p><p class="ahjo-link-text">{esc(l["text"])}</p>'
                    + (f'<ul class="ahjo-link-cats">{cs}</ul>' if cs else "") + '</li>')
    return (f'<section class="ahjo-sec" id="yhteydet" aria-labelledby="h-ahjo-links"><h2 id="h-ahjo-links">{esc(u["links_h"])}</h2>'
            f'<p class="ahjo-sec-lead">{esc(u["links_lead"])}</p><ul class="ahjo-links">{"".join(rows)}</ul></section>')


def bank_body(d, planned, local, modules, ref):
    u = d["ui"]; names = lambda c: course_name(c, planned, local, modules)
    res = resolve(d, ref); secs = []
    for c in d["categories"]:
        mine = sorted((e for cat, e in res if cat == c["id"]), key=lambda e: not e["ready"])
        items = []
        for e in mine:
            title = (f'<a href="{e["href"]}">{esc(e["title"])}</a>' if e["href"] else f'<span>{esc(e["title"])}</span>')
            lang_tag = f' <span class="ahjo-tag">{esc(u["res_in_finnish"])}</span>' if e["fi_only"] else ""
            badge = e.get("badge") or (None if e["ready"] else u["res_coming"])
            meta = []
            if e["courses"]: meta.append(f'<span class="ahjo-meta-l">{esc(u["res_used_by"])}:</span> {chips(e["courses"], names)}')
            if e["subjects"]: meta.append(f'<span class="ahjo-meta-l">{esc(u["res_subjects"])}:</span> {esc(", ".join(e["subjects"]))}')
            items.append(f'<li class="ahjo-res{"" if e["ready"] else " coming"}"><p class="ahjo-res-head"><span class="ahjo-res-title">{title}</span>{lang_tag}'
                         f' <span class="ahjo-kind">{esc(e["kind"])}</span>' + (f' <span class="ahjo-badge planned">{esc(badge)}</span>' if badge else "") + '</p>'
                         f'<p class="ahjo-res-text">{esc(e["text"])}</p>' + "".join(f'<p class="ahjo-res-meta">{m}</p>' for m in meta) + '</li>')
        body = f'<ul class="ahjo-res-list">{"".join(items)}</ul>' if items else f'<p class="ahjo-empty">{esc(u["bank_none"])}</p>'
        secs.append(f'<section class="ahjo-sec ahjo-cat" id="{c["id"]}" aria-labelledby="h-cat-{c["id"]}">'
                    f'<div class="ahjo-cat-top"><div><h2 id="h-cat-{c["id"]}">{icon(c["icon"])}{esc(c["title"])}</h2><p class="ahjo-sec-lead">{esc(c["text"])}</p></div>'
                    f'<div class="ahjo-cat-art">{art(c["id"])}</div></div>{body}</section>')
    return hero(d, u["bank_h"], u["bank_page_lead"], BANK) + "".join(secs)


def safety_body(d, lang, render_md):
    u = d["ui"]; items = []
    for s in d["safety"]:
        st = s.get("status", "valmisteilla")
        text = ""
        if st == "hyvaksytty":
            text = (f'<div class="ahjo-safety-text">{render_md(safety_file(s["id"], lang).read_text())}</div>'
                    f'<p class="ahjo-approved">{esc(u["safety_approved_by"].replace("{who}", s["approved_by"]).replace("{date}", s["date"]))}</p>')
        items.append(f'<li class="ahjo-safety-item" id="{s["id"]}"><div class="ahjo-safety-head"><h2>{esc(s["title"])}</h2>'
                     f'<p class="ahjo-badge{"" if st == "hyvaksytty" else " planned"}">{esc(u["safety_status_" + st])}</p></div>'
                     f'<p class="ahjo-res-text"><span class="ahjo-meta-l">{esc(u["safety_covers"])}:</span> {esc(s["covers"])}</p>{text}</li>')
    draft = all(s.get("status", "valmisteilla") != "hyvaksytty" for s in d["safety"])
    return (hero(d, u["safety_page_title"], u["safety_page_lead"], SAFETY)
            + (f'<p class="ahjo-draft" role="note">{icon("shield")}<span>{esc(u["safety_draft_note"])}</span></p>' if draft else "")
            + f'<ol class="ahjo-safety">{"".join(items)}</ol>')


def guide_body(d, gid, lang, render_md):
    r = next(r for r in d["resources"] if r.get("id") == gid)
    return hero(d, r["title"], r["text"], BANK) + f'<article class="ahjo-guide">{render_md(guide_file(gid, lang).read_text())}</article>'


def front_page_planned(planned, d):
    """The front page's planned courses without Ahjo's own (teacher 2026-11-08: Ahjo 1 and Ahjo 2 only on the Ahjo page)."""
    codes = {c["code"] for c in d["courses"]} if d else set()
    return [p for p in planned if p.get("icon") not in codes]


def ready_guides(d): return [r["id"] for r in d["resources"] if r.get("id") and r.get("status") == "ready"]


if __name__ == "__main__":
    import courses as _c, investigations, guides, local_courses
    cur = json.loads((ROOT / "curriculum.json").read_text())
    lessons = {l["id"] for k, m in cur.items() if not k.startswith("_") for l in m.get("lessons", [])}
    errs = validate(lessons, set(investigations.ids()), set(guides.ids()), [p["icon"] for p in local_courses.planned()],
                    list(local_courses.load()), {k: m["title"] for k, m in cur.items() if not k.startswith("_")})
    print("\n".join(errs) or "ahjo.json OK")
    sys.exit(1 if errs else 0)
