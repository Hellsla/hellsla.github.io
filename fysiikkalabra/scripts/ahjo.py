"""Ahjo Makerspace (teacher 2026-11-08; docs/PORTAL_ARCHITECTURE.md section C): Kiviruukin lukio's makerspace inside
Ruukkilabra, in the school's colours (navy #012169, pink #fca5c7, Lato headings, Work Sans text; site.css "Ahjo") under
the site's common header, with the original Ahjo Makerspace logo (assets/shared/brand/ahjo-makerspace-logo.svg, the
teacher's file byte for byte: never redrawn, recoloured or cropped; LOGO_SHA256 pins it). The front page's course list
shows only the mark (rays and anvil, teacher 2026-11-08) on the same white rounded square as the module icons: MARK,
cut from the logo by mark_svg() with its paths copied unchanged and the name's two paths left out.

ahjo.json is the source (Finnish); content/<lang>/ahjo.json has the same ids in another language, and a language
without one shows the Finnish (fi-easy). build.py renders three pages in every language:
  ahjo.html               the start page: what Ahjo is, Ahjo 1 and Ahjo 2, the bank's topics, the equipment, safety,
                          and the studies linked to Ahjo
  ahjo-materiaalit.html   the resource bank: every resource under its one category, with the courses that use it
  ahjo-turvallisuus.html  the safety section: its topics and their status
  ahjo-projektit.html     the project bank: project cards, approved first, then proposals

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
                                                                    coming and has no page; "draft" and "ready" need
                                                                    their text in content/<lang>/ahjo/<id>.md and become
                                                                    <id>.html. "draft" (teacher 2026-11-08) is a written
                                                                    guide nobody has yet tried on Ahjo's own devices: the
                                                                    page and every list mark it "Luonnos", and only the
                                                                    teacher sets "ready". A guide's text has the twelve
                                                                    sections of ui.guide_sections as its ## headings, in
                                                                    that order (one structure for every guide, after
                                                                    SparkFun's experiment guide and Prusa's project
                                                                    template; docs: the benchmark report)
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
  projects                 [{id, status, title, summary, problem, skills, materials, success, next, level, lessons, courses,
                           subjects, inspiration: [{source, title, url}]}]: the project bank's cards (teacher 2026-11-08),
                           original texts with a link to the page that inspired each (https on a site in SOURCE_HOSTS;
                           checked by hand when written). level 1–3, lessons about how many 75-minute lessons. Status
                           "ehdotus" (a proposal) until the teacher sets "hyvaksytty" with approved_by and date
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
MARK = ROOT / "assets/shared/brand/ahjo-makerspace-merkki.svg"
MARK_SRC = "brand/ahjo-makerspace-merkki.svg"


TAB_ICONS = {"brand/ruukkilabra-32.png": "brand/ahjo-32.png", "brand/ruukkilabra-symboli.svg": MARK_SRC, "brand/ruukkilabra-180.png": "brand/ahjo-180.png"}


SITE_MARK = ROOT / "assets/shared/brand/ruukkilabra-symboli.svg"
SITE_MARK_KR = ROOT / "assets/shared/brand/ruukkilabra-symboli-kiviruukki.svg"
SITE_MARK_KR_SRC = "brand/ruukkilabra-symboli-kiviruukki.svg"
KIVIRUUKKI_COLOURS = {"#1A4B2E": "#012169", "#D76A10": "#FCA5C7", "#FFC914": "#FDD0E1", "#B5D92D": "#9AA6CF",
                      "#44AF4D": "#4D63A8", "#B85F2A": "#FCA5C7"}   # Ruukkilabra's colours -> navy, pink and their tints


def site_mark_kiviruukki():
    """Ruukkilabra's symbol in Kiviruukin lukio's colours for the Ahjo pages' header (teacher 2026-11-08): the same shapes,
    only the fills changed (green -> navy, the spectrum -> pink and navy tints, the copper door -> pink)."""
    s = SITE_MARK.read_text()
    for a, b in KIVIRUUKKI_COLOURS.items():
        assert a in s, a
        s = s.replace(a, b)
    return s.replace("Ruukkilabra – ahjo ja valoprisma", "Ruukkilabra – ahjo ja valoprisma Kiviruukin lukion väreissä")


COURSE_ICON_TITLES = {"AHJO1": "3D-tulostin Ahjon alasimella", "AHJO2": "Idean hehkulamppu Ahjon alasimella"}


def course_icon_svg(code):
    """Ahjo 1's and Ahjo 2's icons (teacher 2026-11-08 chose 1a and 2a): the logo's anvil and arch (its paths copied
    unchanged) on the module icons' tile, with a 3D printer (Ahjo 1) or an idea's light bulb (Ahjo 2) above it."""
    paths = re.findall(r"<path\b.*?/>", LOGO.read_text(), re.S)
    N, P, PL = "#012169", "#FCA5C7", "#FDD0E1"
    s = f'stroke="{N}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    if code == "AHJO1":
        top = (f'<path d="M230 410V60H712V410" {s}/><path d="M230 120H712" {s}/>'
               f'<rect x="400" y="90" width="142" height="110" rx="18" fill="{N}"/><path d="M445 200h52l-26 50z" fill="{N}"/>'
               + "".join(f'<rect x="380" y="{412 - (i + 1) * 34}" width="182" height="26" rx="8" fill="{P if i % 2 == 0 else PL}"/>' for i in range(4)))
    else:
        top = (f'<path d="M471 70a120 120 0 0 1 70 218v52H401v-52A120 120 0 0 1 471 70z" fill="{P}" stroke="{N}" stroke-width="30" stroke-linejoin="round"/>'
               f'<path d="M411 380h120" {s}/><path d="M440 236l31 34 31-34" stroke="{N}" stroke-width="22" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
               + "".join(f'<path d="M{a}" stroke="{P}" stroke-width="26" stroke-linecap="round"/>' for a in ("300 120 340 150", "642 120 602 150", "260 230 310 230", "682 230 632 230")))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48"><title>{COURSE_ICON_TITLES[code]}</title>'
            '<rect x="0.5" y="0.5" width="47" height="47" rx="12" fill="#fffdf8" stroke="#e3dccb"/>'
            '<svg x="5" y="5" width="38" height="38" viewBox="121 -50 700 700">' + top + paths[1] + paths[2] + '</svg></svg>\n')


def tab_icons(html):
    """An Ahjo page's browser tab and home screen icon is Ahjo's mark, not Ruukkilabra's, and the header shows Ruukkilabra's
    symbol in Kiviruukin lukio's colours (teacher 2026-11-08). The PNGs
    (32 px, and 180 px filling its square) are the mark rendered by scripts/ahjo_tab_icons.js and committed beside it."""
    html = re.sub(r'(<img class="brand-mark" src="(?:\.\./)*)brand/ruukkilabra-symboli\.svg"', rf'\g<1>{SITE_MARK_KR_SRC}"', html, count=1)
    for a, b in TAB_ICONS.items():
        assert f'href="{a}"' in html or f'/{a}"' in html, a
        html = re.sub(rf'(<link rel="(?:icon|apple-touch-icon)" href="(?:\.\./)*){re.escape(a)}"', rf'\g<1>{b}"', html)
    return html


def mark_svg():
    """The logo's mark (its first three paths: the rays, the anvil and its arch, byte for byte) on the module icons'
    48 px white rounded square; the paths "Ahjo" and "Kiviruukin Makerspace" (the last two) are left out."""
    paths = re.findall(r"<path\b.*?/>", LOGO.read_text(), re.S)
    assert len(paths) == 5, "the Ahjo logo changed: check which paths are the mark"
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48"><title>Ahjo Makerspace</title>'
            '<rect x="0.5" y="0.5" width="47" height="47" rx="12" fill="#fffdf8" stroke="#e3dccb"/>'
            '<svg x="5" y="5" width="38" height="38" viewBox="153 9 636 636">' + "".join(paths[:3]) + '</svg></svg>\n')
PAGE, BANK, SAFETY, PROJECTS = "ahjo.html", "ahjo-materiaalit.html", "ahjo-turvallisuus.html", "ahjo-projektit.html"
PROJECT_STATUSES = ("ehdotus", "hyvaksytty")
# the sites a project card may name as its inspiration (each link checked by hand when the card was written)
SOURCE_HOSTS = ("projecthub.arduino.cc", "microbit.org", "www.jpl.nasa.gov", "www.teachengineering.org", "www.instructables.com",
                "projects.raspberrypi.org", "fabacademy.org", "www.prusa3d.com", "dschool.stanford.edu", "learn.sparkfun.com")
EQUIPMENT_STATUSES = ("tuleva", "kaytossa")
RES_STATUSES = ("planned", "draft", "ready")
PAGED = ("draft", "ready")        # a guide with its own page
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
                       [len(g["items"]) for g in d["equipment"]], [(len(c.get("goals", [])), len(c.get("lessons", [])), [(l.get("guides", []), bool(l.get("milestone"))) for l in c.get("lessons", [])], len(c.get("deepening", []))) for c in d["courses"]], [s["id"] for s in d["safety"]], [l["course"] for l in d["links"]], sorted(d["ui"]),
                       [(p["id"], p["status"], p["level"], p["lessons"], p["courses"], [i["url"] for i in p["inspiration"]], len(p["skills"]), len(p["materials"]), len(p["subjects"])) for p in d.get("projects", [])])
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
            ahjo_ids = {r["id"] for r in d["resources"] if "id" in r}
            for i, l in enumerate(c.get("lessons", []), 1):
                if not l.get("output"): errs.append(f"{name}: {c['code']} lesson {i}: no output (what the lesson produces)")
                for gid in l.get("guides", []):
                    if gid not in ahjo_ids | lessons | investigations | guides: errs.append(f"{name}: {c['code']} lesson {i}: no such guide or chapter {gid!r}")
            if sum(1 for l in c.get("lessons", []) if l.get("milestone")) not in (0, 5) and c["code"] == "AHJO2":
                errs.append(f"{name}: AHJO2: the five hand-ins are marked on five lessons")
            if any(not x.get("title") or not x.get("text") for x in c.get("deepening", [])): errs.append(f"{name}: {c['code']}: a deepening item without a title or text")
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
                if r.get("status") in PAGED:
                    lang = "fi" if f == SOURCE else f.parent.name
                    g = guide_file(rid, lang)
                    if not g: errs.append(f"{name}: {rid}: {r['status']} but content/fi/ahjo/{rid}.md is missing"); continue
                    if g.parent.parent.name != lang: continue     # falls back to the Finnish text
                    heads = re.findall(r"^## (.+?)\s*$", g.read_text(), re.M)
                    if heads != d["ui"]["guide_sections"]:
                        errs.append(f"{g.relative_to(ROOT)}: its ## headings must be the twelve guide sections in order: {d['ui']['guide_sections']}, not {heads}")
                    if FORBIDDEN.search(g.read_text()): errs.append(f"{g.relative_to(ROOT)}: names equipment Ahjo will not have ({FORBIDDEN.search(g.read_text()).group(0)})")
                    names = FIG_REF.findall(g.read_text()); mod = figure_module(rid) if names else None
                    for fig in names:
                        if not mod or fig not in mod.FIGURES: errs.append(f"{g.relative_to(ROOT)}: no figure {fig!r} in lessons/ahjo/{rid}/figures.py"); continue
                        if lang != i18n.SOURCE:
                            miss = draw(rid, fig, lang, mod)[1]
                            if miss: errs.append(f"{g.relative_to(ROOT)}: figure {fig}: no translation in {rid}.figures.json for {miss}")
        if d["equipment_status"] not in EQUIPMENT_STATUSES: errs.append(f"{name}: equipment_status must be one of {EQUIPMENT_STATUSES}")
        for g in d["equipment"]:
            for it in g["items"]:
                if not isinstance(it, str) and it.get("status") not in EQUIPMENT_STATUSES: errs.append(f"{name}: {g['id']}: {it}: unknown status")
        for s in d["safety"]:
            st = s.get("status", "valmisteilla")
            if st not in SAFETY_STATUSES: errs.append(f"{name}: safety {s['id']}: status must be one of {SAFETY_STATUSES}")
            if st == "hyvaksytty" and not (s.get("approved_by") and s.get("date") and safety_file(s["id"], i18n.SOURCE)):
                errs.append(f"{name}: safety {s['id']}: approved needs approved_by, date and content/fi/ahjo/turvallisuus/{s['id']}.md")
        pids = [p.get("id") for p in d.get("projects", [])]
        if len(set(pids)) != len(pids): errs.append(f"{name}: repeated project ids")
        for p in d.get("projects", []):
            pid = p.get("id") or "?"
            if not re.fullmatch(r"[a-z0-9-]+", pid): errs.append(f"{name}: project {pid}: id must be lowercase-with-hyphens")
            for k in ("title", "summary", "problem", "skills", "materials", "success", "next", "courses", "inspiration"):
                if not p.get(k): errs.append(f"{name}: project {pid}: no {k}")
            if p.get("status") not in PROJECT_STATUSES: errs.append(f"{name}: project {pid}: status must be one of {PROJECT_STATUSES}")
            if p.get("status") == "hyvaksytty" and not (p.get("approved_by") and p.get("date")):
                errs.append(f"{name}: project {pid}: only the teacher approves a card: approved_by and date")
            if p.get("level") not in (1, 2, 3): errs.append(f"{name}: project {pid}: level 1, 2 or 3")
            if not isinstance(p.get("lessons"), int) or not 1 <= p["lessons"] <= 16: errs.append(f"{name}: project {pid}: lessons 1–16")
            for code in p.get("courses", []):
                if code not in known_codes: errs.append(f"{name}: project {pid}: unknown course {code}")
            for i in p.get("inspiration", []):
                host = re.match(r"https://([^/]+)/", i.get("url", ""))
                if not host or host.group(1) not in SOURCE_HOSTS: errs.append(f"{name}: project {pid}: inspiration {i.get('url')!r} is not https on a known source site")
                if not i.get("title") or not i.get("source"): errs.append(f"{name}: project {pid}: inspiration needs title and source")
        for l in d["links"]:
            if l["course"] not in known_codes: errs.append(f"{name}: link to unknown course {l['course']}")
            for c in l.get("categories", []):
                if c not in cats: errs.append(f"{name}: link {l['course']}: unknown category {c}")
    return errs


# --- rendering ---------------------------------------------------------------------------------------------------

def count(ui, key, n): return ui[key]["one" if n == 1 else "other"].replace("{n}", str(n))


def nav(d, current):
    u = d["ui"]
    items = [(PAGE, u["nav_home"]), (PAGE + "#opintojaksot", u["nav_courses"]), (BANK, u["nav_bank"]), (PROJECTS, u["nav_projects"]),
             (PAGE + "#laitteisto", u["nav_equipment"]), (SAFETY, u["nav_safety"])]
    return (f'<nav class="ahjo-nav" aria-label="{esc(u["nav_label"])}"><ul>'
            + "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{esc(t)}</a></li>' for h, t in items)
            + '</ul></nav>')


def hero(d, title, lead, current, big=False, extra="", logo=None):
    """The section's own banner: the original logo (large on the start page), the school's line, the heading. A course
    page passes its own logo (the course icon, large) and shows Ahjo's logo in its shared section (teacher 2026-11-08)."""
    size = 168 if big else 124
    return (f'<header class="ahjo-hero{" ahjo-hero-big" if big else ""}">'
            + (logo or f'<img class="ahjo-logo" src="{LOGO_SRC}" alt="{esc(d["ui"]["logo_alt"])}" width="{size}" height="{size}">') +
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
    if p and code.startswith("AHJO"): return p["title"], course_page(code), True   # Ahjo 1 and 2 have their own pages here
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
            ready, draft = r["status"] == "ready", r["status"] == "draft"
            e.update(title=r["title"], kind=u["kind_ahjo"], href=f'{r["id"]}.html' if ready or draft else None, text=r["text"], ready=ready,
                     draft=draft, badge=u["res_draft"] if draft else None)
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
        title, text, _ = course_info(c["code"], planned, local)
        href = course_page(c["code"])
        badges = (f'<p class="ahjo-badge planned">{esc(u["course_status_planned"])}</p>'
                  + (f'<p class="ahjo-badge ahjo-license-badge">{esc(u["license_badge"])}</p>' if c.get("license") else ""))
        cards.append(f'<article class="ahjo-course" id="{c["code"].lower()}" aria-labelledby="h-{c["code"].lower()}">'
                     f'<div class="ahjo-course-art">{art(c["code"].lower())}</div><div class="ahjo-course-head"><h3 id="h-{c["code"].lower()}"><span class="ahjo-course-name"><img class="ahjo-course-icon" src="module-icons/{c["code"].lower()}.svg" alt="" width="40" height="40" aria-hidden="true"><a href="{href}">{esc(title)}</a></span>'
                     f'<span class="ahjo-course-sub">{esc(c["subtitle"])}</span></h3><div class="ahjo-badges">{badges}</div></div>'
                     f'<p class="ahjo-course-text">{esc(text)}</p>'
                     f'<h4 class="visually-hidden">{esc(u["course_contents"])}</h4>'
                     f'<ul class="ahjo-topics">' + "".join(f'<li>{esc(t)}</li>' for t in c["topics"]) + '</ul>'
                     f'<p class="ahjo-more"><a href="{href}">{esc(u["course_page_open"])}<span class="visually-hidden">: {esc(title)}</span><span aria-hidden="true"> →</span></a></p></article>')
    courses = (f'<section class="ahjo-sec" id="opintojaksot" aria-labelledby="h-ahjo-courses"><h2 id="h-ahjo-courses">{esc(u["courses_h"])}</h2>'
               f'<p class="ahjo-sec-lead">{esc(u["courses_lead"])}</p><div class="ahjo-courses">{"".join(cards)}</div></section>')
    # the bank's topics with what is ready and what is coming
    cats = []
    for c in d["categories"]:
        mine = [e for cat, e in res if cat == c["id"]]
        ready, draft = sum(e["ready"] for e in mine), sum(bool(e.get("draft")) for e in mine)
        coming = len(mine) - ready - draft
        n = " · ".join(([count(u, "bank_ready", ready)] if ready else []) + ([count(u, "bank_draft", draft)] if draft else [])
                       + ([count(u, "bank_coming", coming)] if coming else [])) or u["bank_none"]
        cats.append(f'<li><a href="{BANK}#{c["id"]}">{icon(c["icon"])}<span class="ahjo-cat-t">{esc(c["title"])}</span>'
                    f'<span class="ahjo-cat-n">{esc(n)}</span></a></li>')
    bank = (f'<section class="ahjo-sec" id="materiaalipankki" aria-labelledby="h-ahjo-bank"><h2 id="h-ahjo-bank">{esc(u["bank_h"])}</h2>'
            f'<p class="ahjo-sec-lead">{esc(u["bank_lead"])}</p><ul class="ahjo-cats">{"".join(cats)}</ul>'
            f'<p class="ahjo-more"><a href="{BANK}">{esc(u["bank_all"])}<span aria-hidden="true"> →</span></a></p></section>')
    return (hero(d, d["title"], d["lead"], PAGE, big=True, extra=f'<p class="ahjo-opening">{esc(d["opening"])}</p>')
            + courses + bank + projects_teaser(d) + equipment_section(d)
            + (f'<section class="ahjo-sec ahjo-safety-teaser" id="turvallisuus" aria-labelledby="h-ahjo-safety">{icon("shield", "ahjo-icon ahjo-icon-big")}'
               f'<div><h2 id="h-ahjo-safety">{esc(u["safety_h"])}</h2><p>{esc(u["safety_lead"])}</p><p class="ahjo-draft-short">{esc(u["safety_draft_note"].split(". ")[0])}.</p>'
               f'<p class="ahjo-more"><a href="{SAFETY}">{esc(u["safety_open"])}<span aria-hidden="true"> →</span></a></p></div></section>')
            + links_section(d, names))


def course_page(code): return f"ahjo-{code[4:].lower()}.html"     # AHJO1 -> ahjo-1.html


def lesson_links(d, l, ref):
    """A lesson's guides and chapters: an Ahjo guide once it has a page (draft or ready), a chapter or TVT guide once
    published (in Finnish only where the language has none); nothing is linked before its page exists."""
    u = d["ui"]; out = []
    for gid in l.get("guides", []):
        r = next((r for r in d["resources"] if r.get("id") == gid), None)
        if r:
            if r["status"] in PAGED: out.append(f'<a href="{gid}.html">{esc(r["title"])}</a>')
            continue
        got = ref(gid)
        if got: out.append(f'<a href="{gid}.html">{esc(got[0])}</a>' + (f' <span class="ahjo-tag">{esc(u["res_in_finnish"])}</span>' if got[2] else ""))
    return out


def lessons_list(d, c, ref):
    """The lesson outline with a picture for each lesson (scripts/ahjo_art.py), what each lesson produces, the guides it
    uses and, in Ahjo 2, the hand-ins."""
    u = d["ui"]; rows = []
    for i, l in enumerate(c["lessons"], 1):
        links = lesson_links(d, l, ref)
        rows.append(f'<li><div class="ahjo-lesson"><span class="ahjo-lesson-art">{art(c["code"].lower() + "-" + str(i))}</span><span class="ahjo-lesson-b">'
                    + (f'<span class="ahjo-badge ahjo-milestone">{esc(l["milestone"])}</span>' if l.get("milestone") else "")
                    + f'<span class="ahjo-lesson-t">{esc(l["title"])}</span> <span class="ahjo-lesson-x">{esc(l["text"])}</span>'
                    + (f'<span class="ahjo-lesson-e"><span class="ahjo-meta-l">{esc(u["lesson_example"])}:</span> {esc(l["example"])}</span>' if l.get("example") else "")
                    + (f'<span class="ahjo-lesson-e ahjo-lesson-o"><span class="ahjo-meta-l">{esc(u["lesson_output"])}:</span> {esc(l["output"])}</span>' if l.get("output") else "")
                    + (f'<span class="ahjo-lesson-g"><span class="ahjo-meta-l">{esc(u["lesson_guides"])}:</span> {", ".join(links)}</span>' if links else "")
                    + '</span></div></li>')
    return '<ol class="ahjo-lessons">' + "".join(rows) + '</ol>'


def deepening_section(u, c, k):
    if not c.get("deepening"): return ""
    return (f'<section class="ahjo-sec" id="syventavat" aria-labelledby="h-{k}-deep"><h2 id="h-{k}-deep">{esc(u["deepening_h"])}</h2>'
            f'<p class="ahjo-sec-lead">{esc(u["deepening_lead"])}</p><ul class="ahjo-deep">'
            + "".join(f'<li><span class="ahjo-lesson-t">{esc(x["title"])}</span> {esc(x["text"])}</li>' for x in c["deepening"]) + '</ul></section>')


def course_body(d, c, planned, local, modules, ref):
    """Ahjo 1 or Ahjo 2 on its own page (teacher 2026-11-08): the licence (Ahjo 1), contents, goals, the 16 lessons with
    their pictures, and links to Ahjo's shared materials, which stay in the bank (linked, never copied)."""
    u = d["ui"]; title, text, _ = course_info(c["code"], planned, local); k = c["code"].lower()
    # the course's own logo large in the banner; Ahjo's logo heads the shared section below (teacher 2026-11-08)
    out = hero(d, title, c["subtitle"], PAGE + "#opintojaksot", big=True, extra=f'<p class="ahjo-opening">{esc(text)}</p>',
               logo=f'<img class="ahjo-logo ahjo-course-logo" src="module-icons/{k}.svg" alt="" width="168" height="168">')
    eq = "#laitteisto"
    tiles = [(BANK, icon("box", "ahjo-icon ahjo-shared-icon"), u["bank_h"], u["shared_bank"]),
             (PROJECTS, icon("cube", "ahjo-icon ahjo-shared-icon"), u["projects_h"], u["projects_teaser"]),
             (PAGE + eq, icon("tools", "ahjo-icon ahjo-shared-icon"), u["equipment_h_" + d["equipment_status"]], u["shared_equipment"]),
             (SAFETY, icon("shield", "ahjo-icon ahjo-shared-icon"), u["safety_h"], u["shared_safety"])]
    out += (f'<section class="ahjo-sec ahjo-shared" aria-labelledby="h-{k}-shared"><div class="ahjo-shared-head">'
            f'<a class="ahjo-shared-home" href="{PAGE}"><img class="ahjo-logo ahjo-shared-logo" src="{LOGO_SRC}" alt="{esc(u["logo_alt"])}" width="104" height="104"></a>'
            f'<div><h2 id="h-{k}-shared">{esc(u["shared_h"])}</h2><p class="ahjo-sec-lead">{esc(u["shared_lead"])}</p></div></div><ul class="ahjo-shared-list">'
            + "".join(f'<li><a href="{h}">{ic}<span class="ahjo-shared-t">{esc(t)}</span><span class="ahjo-shared-x">{esc(x)}</span></a></li>' for h, ic, t, x in tiles)
            + '</ul></section>')
    if c.get("license"):
        out += (f'<section class="ahjo-sec ahjo-safety-teaser ahjo-license" aria-labelledby="h-{k}-license">{icon("shield", "ahjo-icon ahjo-icon-big")}'
                f'<div><h2 id="h-{k}-license">{esc(u["license_h"])}</h2><p>{esc(u["license_text"])}</p></div></section>')
    out += (f'<section class="ahjo-sec" aria-labelledby="h-{k}-contents"><div class="ahjo-course-art ahjo-course-page-art">{art(k)}</div>'
            f'<h2 id="h-{k}-contents">{esc(u["course_contents"])}</h2><ul class="ahjo-topics">' + "".join(f'<li>{esc(t)}</li>' for t in c["topics"]) + '</ul></section>')
    note = f'<p class="ahjo-plan-note">{esc(u["plan_draft"])}</p>' if c.get("plan_status") == "draft" and (c.get("goals") or c.get("lessons")) else ""
    if c.get("goals"):
        out += (f'<section class="ahjo-sec" id="tavoitteet" aria-labelledby="h-{k}-goals"><h2 id="h-{k}-goals">{esc(u["course_goals"])}</h2>{note}'
                f'<p class="ahjo-sec-lead">{esc(u["course_goals_lead"])}</p><ul class="ahjo-goals">' + "".join(f'<li>{esc(g)}</li>' for g in c["goals"]) + '</ul></section>')
        note = ""
    if c.get("lessons"):
        out += (f'<section class="ahjo-sec" id="oppitunnit" aria-labelledby="h-{k}-lessons"><h2 id="h-{k}-lessons">{esc(u["course_lessons"].replace("{n}", str(len(c["lessons"]))))}</h2>{note}'
                + lessons_list(d, c, ref) + '</section>' + deepening_section(u, c, k))
    mine = [e for _, e in resolve(d, ref) if c["code"] in e["courses"] and e["href"] and (e["ready"] or e.get("draft"))]
    rows = "".join(f'<li><a href="{e["href"]}"><span class="ahjo-res-t">{esc(e["title"])}</span></a> <span class="ahjo-res-k">{esc(e["kind"])}</span>'
                   + (f' <span class="ahjo-badge planned">{esc(e["badge"])}</span>' if e.get("draft") else "")
                   + f'<span class="ahjo-res-x">{esc(e["text"])}</span></li>' for e in mine)
    out += (f'<section class="ahjo-sec" id="materiaalit" aria-labelledby="h-{k}-materials"><h2 id="h-{k}-materials">{esc(u["course_materials_h"])}</h2>'
            f'<p class="ahjo-sec-lead">{esc(u["course_materials_lead"])}</p>'
            + (f'<ul class="ahjo-course-res">{rows}</ul>' if rows else f'<p>{esc(u["course_materials_none"])}</p>')
            + f'<p class="ahjo-more"><a href="{BANK}">{esc(u["bank_all"])}<span aria-hidden="true"> →</span></a></p>'
            f'<p class="ahjo-more"><a href="{SAFETY}">{esc(u["safety_open"])}<span aria-hidden="true"> →</span></a></p></section>')
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
        mine = sorted((e for cat, e in res if cat == c["id"]), key=lambda e: (not e["ready"], not e.get("draft")))
        items = []
        for e in mine:
            title = (f'<a href="{e["href"]}">{esc(e["title"])}</a>' if e["href"] else f'<span>{esc(e["title"])}</span>')
            lang_tag = f' <span class="ahjo-tag">{esc(u["res_in_finnish"])}</span>' if e["fi_only"] else ""
            badge = e.get("badge") or (None if e["ready"] else u["res_coming"])
            meta = []
            if e["courses"]: meta.append(f'<span class="ahjo-meta-l">{esc(u["res_used_by"])}:</span> {chips(e["courses"], names)}')
            if e["subjects"]: meta.append(f'<span class="ahjo-meta-l">{esc(u["res_subjects"])}:</span> {esc(", ".join(e["subjects"]))}')
            items.append(f'<li class="ahjo-res{"" if e["ready"] or e.get("draft") else " coming"}"><p class="ahjo-res-head"><span class="ahjo-res-title">{title}</span>{lang_tag}'
                         f' <span class="ahjo-kind">{esc(e["kind"])}</span>' + (f' <span class="ahjo-badge planned">{esc(badge)}</span>' if badge else "") + '</p>'
                         f'<p class="ahjo-res-text">{esc(e["text"])}</p>' + "".join(f'<p class="ahjo-res-meta">{m}</p>' for m in meta) + '</li>')
        body = f'<ul class="ahjo-res-list">{"".join(items)}</ul>' if items else f'<p class="ahjo-empty">{esc(u["bank_none"])}</p>'
        secs.append(f'<section class="ahjo-sec ahjo-cat" id="{c["id"]}" aria-labelledby="h-cat-{c["id"]}">'
                    f'<div class="ahjo-cat-top"><div><h2 id="h-cat-{c["id"]}">{icon(c["icon"])}{esc(c["title"])}</h2><p class="ahjo-sec-lead">{esc(c["text"])}</p></div>'
                    f'<div class="ahjo-cat-art">{art(c["id"])}</div></div>{body}</section>')
    return hero(d, u["bank_h"], u["bank_page_lead"], BANK) + "".join(secs)


def project_card(u, p, names):
    """One project card: what it is, the problem, what you learn and need, how success is measured, where it can go,
    and the page that inspired it (a link out of Ruukkilabra, marked as such; the card's text is our own)."""
    ok = p["status"] == "hyvaksytty"
    meta = (f'<span class="ahjo-chip">{esc(u["proj_levels"][p["level"] - 1])}</span>'
            f'<span class="ahjo-chip">{esc(count(u, "proj_lessons", p["lessons"]))}</span>' + chips(p["courses"], names))
    src = "; ".join(f'<a href="{esc(i["url"])}" rel="external noopener">{esc(i["title"])}</a> ({esc(i["source"])})' for i in p["inspiration"])
    rows = [(u["proj_problem"], esc(p["problem"])), (u["proj_skills"], esc(", ".join(p["skills"]))), (u["proj_materials"], esc(", ".join(p["materials"]))),
            (u["proj_success"], esc(p["success"])), (u["proj_next"], esc(p["next"]))]
    if p.get("subjects"): rows.append((u["proj_subjects"], esc(", ".join(p["subjects"]))))
    rows.append((u["proj_inspiration"], f'{src} <span class="ahjo-ext">{esc(u["proj_external"])}</span>'))
    return (f'<article class="ahjo-proj{" approved" if ok else ""}" id="{p["id"]}" aria-labelledby="h-proj-{p["id"]}">'
            f'<div class="ahjo-proj-head"><h3 id="h-proj-{p["id"]}">{esc(p["title"])}</h3>'
            f'<p class="ahjo-badge{"" if ok else " planned"}">{esc(u["proj_status_" + p["status"]])}</p></div>'
            f'<p class="ahjo-proj-sum">{esc(p["summary"])}</p><p class="ahjo-proj-meta">{meta}</p>'
            f'<dl class="ahjo-proj-dl">' + "".join(f'<dt>{esc(k)}</dt><dd>{v}</dd>' for k, v in rows) + '</dl></article>')


def projects_teaser(d):
    """The start page's pointer to the project bank, with how many topics it has."""
    u = d["ui"]; ps = d.get("projects", [])
    if not ps: return ""
    return (f'<section class="ahjo-sec" id="projektit" aria-labelledby="h-ahjo-projects"><h2 id="h-ahjo-projects">{esc(u["projects_h"])}'
            f' <span class="ahjo-count">{esc(count(u, "projects_count", len(ps)))}</span></h2><p class="ahjo-sec-lead">{esc(u["projects_teaser"])}</p>'
            f'<p class="ahjo-more"><a href="{PROJECTS}">{esc(u["projects_all"])}<span aria-hidden="true"> →</span></a></p></section>')


def projects_body(d, planned, local, modules):
    """The project bank (ahjo-projektit.html): the approved topics first, then the proposals; every card a proposal
    ("ehdotus") until the teacher marks it approved ("hyvaksytty", with approved_by and date)."""
    u = d["ui"]; names = lambda c: course_name(c, planned, local, modules)
    ps = d.get("projects", [])
    ok = [p for p in ps if p["status"] == "hyvaksytty"]; prop = [p for p in ps if p["status"] != "hyvaksytty"]
    sec = lambda sid, h, items, empty: (f'<section class="ahjo-sec" id="{sid}" aria-labelledby="h-{sid}"><h2 id="h-{sid}">{esc(h)}'
                                        f' <span class="ahjo-count">{esc(count(u, "projects_count", len(items)))}</span></h2>'
                                        + (f'<div class="ahjo-proj-grid">{"".join(project_card(u, p, names) for p in items)}</div>' if items else f'<p class="ahjo-empty">{esc(empty)}</p>')
                                        + '</section>')
    return (hero(d, u["projects_h"], u["projects_page_lead"], PROJECTS)
            + f'<p class="ahjo-draft" role="note">{icon("notebook")}<span>{esc(u["projects_note"])}</span></p>'
            + sec("hyvaksytyt", u["projects_approved_h"], ok, u["projects_none_approved"])
            + (sec("ehdotukset", u["projects_proposed_h"], prop, "") if prop else ""))


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


# --- a guide's figures: lessons/ahjo/<id>/figures.py (scripts/figlib.py), drawn when the page is built -----------------
FIG_REF = re.compile(r'<svg data-fig="([A-Za-z0-9_-]+)"></svg>')   # an empty placeholder in a guide's markdown


def figure_module(gid):
    import importlib.util
    f = ROOT / "lessons" / "ahjo" / gid / "figures.py"
    if not f.is_file(): return None
    spec = importlib.util.spec_from_file_location(f"ahjo_figures_{gid.replace('-', '_')}", f)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def figure_texts(gid, lang):
    """{Finnish text: translation} of a guide's figures in `lang` (content/<lang>/ahjo/<id>.figures.json), or None."""
    f = ROOT / "content" / lang / "ahjo" / f"{gid}.figures.json"
    return json.loads(f.read_text()) if lang != i18n.SOURCE and f.is_file() else None


def draw(gid, name, lang, mod=None):
    """(svg, Finnish texts drawn without a translation) of one figure of a guide, in `lang`."""
    import figlib
    mod = mod or figure_module(gid); texts = figure_texts(gid, lang)
    if texts is not None: figlib.set_language(texts, i18n.T(lang)("format.decimal"))
    try: return mod.FIGURES[name](), list(figlib.MISSING)
    finally:
        if texts is not None: figlib.set_language({}, ",")


def guide_md(gid, lang):
    """A guide's markdown with each `<svg data-fig="name"></svg>` as a token paragraph; (text, {token: name})."""
    figs = {}
    def sub(m):
        tok = f"AHJOFIGTOKEN{len(figs)}X"; figs[tok] = m.group(1); return f"\n\n{tok}\n\n"
    return FIG_REF.sub(sub, guide_file(gid, lang).read_text()), figs


def guide_body(d, gid, lang, render_md):
    """An Ahjo guide's page: a draft says so first, in a note nobody can miss; then the twelve sections, with the
    figures drawn in the page's language."""
    r = next(r for r in d["resources"] if r.get("id") == gid); u = d["ui"]
    note = (f'<p class="ahjo-draft" role="note">{icon("notebook")}<span><strong>{esc(u["res_draft"])}.</strong> {esc(u["guide_draft_note"])}</span></p>'
            if r["status"] == "draft" else "")
    text, figs = guide_md(gid, lang); body = render_md(text)
    mod = figure_module(gid) if figs else None
    for tok, name in figs.items():
        body = re.sub(rf"(?:<p>)?{tok}(?:</p>)?", lambda m, name=name: f'<div class="fig ahjo-fig">{draw(gid, name, lang, mod)[0]}</div>', body)
    return hero(d, r["title"], r["text"], BANK) + note + f'<article class="ahjo-guide">{body}</article>'


def front_page_planned(planned, d):
    """The front page's planned courses without Ahjo's own (teacher 2026-11-08: Ahjo 1 and Ahjo 2 only on the Ahjo page)."""
    codes = {c["code"] for c in d["courses"]} if d else set()
    return [p for p in planned if p.get("icon") not in codes]


def ready_guides(d): return [r["id"] for r in d["resources"] if r.get("id") and r.get("status") in PAGED]   # every guide with a page, drafts too


if __name__ == "__main__":
    import courses as _c, investigations, guides, local_courses
    cur = json.loads((ROOT / "curriculum.json").read_text())
    lessons = {l["id"] for k, m in cur.items() if not k.startswith("_") for l in m.get("lessons", [])}
    errs = validate(lessons, set(investigations.ids()), set(guides.ids()), [p["icon"] for p in local_courses.planned()],
                    list(local_courses.load()), {k: m["title"] for k, m in cur.items() if not k.startswith("_")})
    print("\n".join(errs) or "ahjo.json OK")
    sys.exit(1 if errs else 0)
