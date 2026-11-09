"""LUMA-tutor (teacher's brief 2026-11-09): Kiviruukin lukio's science-tutor course, done flexibly over the school year
along Perehdy → Tutustu → Suunnittele → Toteuta → Arvioi, in the school's colours like Kilparobotiikka (local-courses.json
LUMATUTOR, "theme": "kiviruukki"). Its own job: science education, guiding, events and science communication; not
tutoring in mathematics or physics.

Sources (Finnish first; a language without its own file shows the Finnish, as fi-easy does):
  lumatutor.json                                  the course: sections and their workload, the start page, the five
                                                  parts and the toolkit's ten templates
  content/<lang>/lumatutor.json                   the same shape in another language
  content/<lang>/lumatutor/tyopajat/<id>.json     one file per workshop: a new workshop is one new file and no code.
                                                  "status": "ready" (a whole guiding card with a page of its own,
                                                  not yet piloted) or "idea" (a development proposal, never shown
                                                  as ready)
  lessons/lumatutor/figures.py                    the workshops' figures (scripts/figlib.py), drawn in the page's
                                                  language (content/<lang>/lumatutor/figures.json)
  lessons/lumatutor/ilmastodata.json              the climate workshop's measurements as published by NOAA and NASA
                                                  (its graphs and the tutor's answers are computed from it)

build.py renders, in every language that has the course: LUMATUTOR.html (the start page), a page per part
(lumatutor-perehdy/-tutustu/-suunnittele/-toteuta/-arvioi.html), the toolkit (lumatutor-tyokalut.html) and a page per
ready workshop (lumatutor-tyopaja-<id>.html). Nothing is stored: the templates are copied, downloaded as text or
printed, and the portfolio is returned in the school's own learning environment. No participant's personal data is
asked anywhere. In texts, [label](page.html#id) is a link and $...$ is LaTeX.

  python scripts/lumatutor.py   validate (also run by build.py)
"""
import json, re, sys, pathlib, html as _h
from urllib.parse import quote
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT
import i18n

SOURCE = ROOT / "lumatutor.json"
CODE = "LUMATUTOR"
PAGE, TOOLS = "LUMATUTOR.html", "lumatutor-tyokalut.html"
WS_DIR = "lumatutor/tyopajat"
FIG_FILE = ROOT / "lessons" / "lumatutor" / "figures.py"
DATA_FILE = ROOT / "lessons" / "lumatutor" / "ilmastodata.json"
SECTION_IDS = ["perehdy", "tutustu", "suunnittele", "toteuta", "arvioi"]
LESSONS_TOTAL = 23                 # 23 x 75 min, the brief's rounding of 38 x 45 min
EXACT_MINUTES, ROUNDED_MINUTES = 38 * 45, 23 * 75
STATUSES = ("ready", "idea")
READY_FIELDS = ("goals", "materials", "prep", "safety", "steps", "background", "questions", "problems", "variations", "closing", "self", "participant")
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
esc = lambda s: _h.escape(str(s), quote=True)

ICONS = {
    "compass": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM15.5 8.5l-2 5-5 2 2-5z",
    "ticket": "M4 7h16v3a2 2 0 0 0 0 4v3H4v-3a2 2 0 0 0 0-4zM14 7v10",
    "flask": "M9 3h6M10 3v6L4.5 18.5A1.7 1.7 0 0 0 6 21h12a1.7 1.7 0 0 0 1.5-2.5L14 9V3M7 15h10",
    "people": "M9 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM3 20v-1a6 6 0 0 1 12 0v1M16 11a2.5 2.5 0 1 0 0-5M17.5 14a4.5 4.5 0 0 1 3.5 4.4V20",
    "notebook": "M6 3h11a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H6zM9 3v18M12 8h3.5M12 12h3.5",
    "tools": "M14.5 5.5a4 4 0 0 0 4.9 4.9L21 12l-2 2-1.6-1.6L8 21.8a2 2 0 0 1-2.8-2.8l9.4-9.4L13 8l2-2z",
    "shield": "M12 3l7 3v5c0 4.5-3 8.4-7 10-4-1.6-7-5.5-7-10V6zM9 12l2 2 4-4",
    "clock": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 7v5l3 2",
    "copy": "M8 8h11v12H8zM5 16V4h11",
    "download": "M12 4v11M7 10l5 5 5-5M5 20h14",
    "print": "M7 9V3h10v6M7 17H4v-7h16v7h-3M7 14h10v7H7z",
    "ext": "M14 4h6v6M20 4l-9 9M18 14v6H4V6h6",
    "spark": "M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6",
    "bulb": "M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z",
}


def icon(name, cls="ahjo-icon"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">'
            f'<path d="{ICONS[name]}"/></svg>')


# --- data ------------------------------------------------------------------------------------------------------------
def data_file(lang=i18n.SOURCE):
    f = ROOT / "content" / lang / "lumatutor.json"
    return f if lang != i18n.SOURCE and f.is_file() else SOURCE


def load(lang=i18n.SOURCE):
    return json.loads(data_file(lang).read_text()) if SOURCE.is_file() else None


def ws_files(lang=i18n.SOURCE):
    """{id: path} of the workshops in `lang`, each falling back to the Finnish file."""
    src = sorted((ROOT / "content" / i18n.SOURCE / WS_DIR).glob("*.json"))
    out = {}
    for f in src:
        t = ROOT / "content" / lang / WS_DIR / f.name
        out[f.stem] = t if lang != i18n.SOURCE and t.is_file() else f
    return out


def workshops(lang=i18n.SOURCE):
    return sorted((json.loads(f.read_text()) for f in ws_files(lang).values()), key=lambda w: w["order"])


def ws_page(wid): return f"lumatutor-tyopaja-{wid}.html"


def section_pages(d): return [s["page"] for s in d["sections"]]


def all_pages(d, ws):
    return [PAGE] + section_pages(d) + [TOOLS] + [ws_page(w["id"]) for w in ws if w["status"] == "ready"]


def climate(): return json.loads(DATA_FILE.read_text())


# --- text ------------------------------------------------------------------------------------------------------------
LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def tx(s):
    """A text with its [label](href) links; LaTeX between $ stays as it is for KaTeX."""
    out, pos = [], 0
    for m in LINK.finditer(s):
        out.append(esc(s[pos:m.start()]))
        out.append(f'<a href="{esc(m.group(2))}">{esc(m.group(1))}</a>'); pos = m.end()
    return "".join(out) + esc(s[pos:])


def plain(s):
    """The same text without link markup or LaTeX dollars, for a .txt template."""
    s = LINK.sub(r"\1", s)
    return re.sub(r"\$([^$]*)\$", lambda m: re.sub(r"\\[a-z]+\{([^{}]*)\}|\\[,;]|[{}\\]", lambda k: k.group(1) or " " if k.group(0).startswith("\\") else "", m.group(1)), s)


def ul(items, cls=""):
    return f'<ul{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>' + "".join(f"<li>{tx(x)}</li>" for x in items) + "</ul>"


def sec(id_, title, inner, lead="", cls=""):
    return (f'<section class="ahjo-sec kr-sec lt-sec{" " + cls if cls else ""}" id="{id_}" aria-labelledby="h-{id_}"><h2 id="h-{id_}">{esc(title)}</h2>'
            + (f'<p class="ahjo-sec-lead">{tx(lead)}</p>' if lead else "") + inner + '</section>')


def ext_link(d, title, url):
    return (f'<a href="{esc(url)}" rel="external noopener" target="_blank">{esc(title)}{icon("ext", "ahjo-icon kr-ext")}'
            f'<span class="visually-hidden"> ({esc(d["ui"]["external"])})</span></a>')


def nav(d, current):
    u = d["ui"]
    items = [(PAGE, u["nav_home"])] + [(s["page"], s["title"]) for s in d["sections"]] + [(TOOLS, u["nav_tools"])]
    return (f'<nav class="ahjo-nav kr-nav lt-nav" aria-label="{esc(u["nav_label"])}"><ul>'
            + "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{esc(t)}</a></li>' for h, t in items)
            + '</ul></nav>')


def page_head(d, title, lead, current, eyebrow=None):
    return (f'<header class="kr-head lt-head"><p class="ahjo-eyebrow">{esc(eyebrow or d["_course_title"])}</p><h1>{esc(title)}</h1>'
            f'<p class="lead">{tx(lead)}</p></header>' + nav(d, current))


def pager(d, current):
    """Edellinen osa / Seuraava osa at a page's end, along the course's order."""
    u = d["ui"]
    order = [(PAGE, u["nav_home"])] + [(s["page"], s["title"]) for s in d["sections"]] + [(TOOLS, u["nav_tools"])]
    i = [h for h, _ in order].index(current)
    prev = order[i - 1] if i > 0 else None
    nxt = order[i + 1] if i + 1 < len(order) else None
    return ('<nav class="lt-pager" aria-label="' + esc(u["nav_label"]) + '">'
            + (f'<a class="lt-pager-prev" href="{prev[0]}"><span class="lt-pager-k">{esc(u["prev"])}</span><span>{esc(prev[1])}</span></a>' if prev else '<span></span>')
            + (f'<a class="lt-pager-next" href="{nxt[0]}"><span class="lt-pager-k">{esc(u["next"])}</span><span>{esc(nxt[1])}</span></a>' if nxt else '')
            + '</nav>')


def done_box(d, part):
    return (f'<div class="lt-done"><h2 id="valmis">{esc(part["done_h"])}</h2>'
            + '<ul class="lt-checks">' + "".join(f"<li>{tx(x)}</li>" for x in part["done"]) + '</ul></div>')


def time_box(part):
    return f'<p class="lt-time">{icon("clock")}<span><strong>{esc(part["time_h"])}.</strong> {tx(part["time"])}</span></p>'


def lessons_label(d, n): return d["ui"]["lessons_value"].replace("{n}", str(n))


# --- templates: one source, shown as a fill-in form, copied or downloaded as text --------------------------------------
def form_html(blocks, fig=None, extra=None):
    """A template's blocks as a printable form. Lines: '# title' (print only), '## heading', '? field', '?? field with
    room', '[ ] check', '. text', '- item', '> monospace', '= a | b | c' (a table; following '- x' are its first cells,
    none gives blank rows), '{figure:name}' (fig(name)), any other '{token}' (extra(token))."""
    out, i, items = [], 0, []
    def flush():
        if items: out.append('<ul class="lt-form-list">' + "".join(items) + '</ul>'); items.clear()
    while i < len(blocks):
        b = blocks[i]
        if b.startswith("- "):
            items.append(f"<li>{tx(b[2:])}</li>"); i += 1; continue
        flush()
        if b.startswith("## "): out.append(f'<h3 class="lt-form-h">{tx(b[3:])}</h3>')
        elif b.startswith("# "): out.append(f'<p class="lt-form-title">{tx(b[2:])}</p>')
        elif b.startswith("?? "): out.append(f'<div class="lt-field lt-field-big"><span class="lt-field-q">{tx(b[3:])}</span><span class="lt-lines" aria-hidden="true"></span></div>')
        elif b.startswith("? "): out.append(f'<div class="lt-field"><span class="lt-field-q">{tx(b[2:])}</span><span class="lt-line" aria-hidden="true"></span></div>')
        elif b.startswith("[ ] "): out.append(f'<p class="lt-check"><span class="lt-box" aria-hidden="true"></span>{tx(b[4:])}</p>')
        elif b.startswith(". "): out.append(f'<p class="lt-form-p">{tx(b[2:])}</p>')
        elif b.startswith("> "): out.append(f'<p class="lt-mono">{esc(b[2:])}</p>')
        elif b.startswith("= "):
            cols = [c.strip() for c in b[2:].split("|")]
            rows = []
            while i + 1 < len(blocks) and blocks[i + 1].startswith("- "):
                i += 1; rows.append(blocks[i][2:])
            body = "".join(f'<tr><td>{tx(r)}</td>' + "<td></td>" * (len(cols) - 1) + '</tr>' for r in rows) if rows else \
                "".join('<tr>' + "<td></td>" * len(cols) + '</tr>' for _ in range(10))
            out.append(f'<table class="lt-table{"" if rows else " lt-table-log"}"><thead><tr>' + "".join(f'<th scope="col">{tx(c)}</th>' for c in cols)
                       + f'</tr></thead><tbody>{body}</tbody></table>')
        elif b.startswith("{figure:") and fig: out.append(fig(b[8:-1]))
        elif b.startswith("{") and extra: out.append(extra(b[1:-1]))
        else: out.append(f"<p>{tx(b)}</p>")
        i += 1
    flush()
    return "".join(out)


def form_text(blocks, extra=None):
    """The same blocks as a plain text file to copy or download (no LaTeX, no links)."""
    out, i = [], 0
    while i < len(blocks):
        b = blocks[i]
        if b.startswith("## "): out += ["", b[3:].upper(), ""]
        elif b.startswith("# "): out += [plain(b[2:]).upper(), "=" * len(b[2:]), ""]
        elif b.startswith("?? "): out += [plain(b[3:]), "", "", ""]
        elif b.startswith("? "): out += [plain(b[2:]) + ": ", ""]
        elif b.startswith("[ ] "): out.append("[ ] " + plain(b[4:]))
        elif b.startswith(". "): out += [plain(b[2:]), ""]
        elif b.startswith("- "): out.append("- " + plain(b[2:]))
        elif b.startswith("> "): out += [b[2:], ""]
        elif b.startswith("= "):
            cols = [plain(c.strip()) for c in b[2:].split("|")]
            out.append(" | ".join(cols))
            rows = []
            while i + 1 < len(blocks) and blocks[i + 1].startswith("- "):
                i += 1; rows.append(plain(blocks[i][2:]))
            out += [r + " |" * (len(cols) - 1) for r in rows] or [" |" * (len(cols) - 1) for _ in range(10)]
            out.append("")
        elif b.startswith("{figure:"): pass
        elif b.startswith("{") and extra: out += [extra(b[1:-1]), ""]
        else: out.append(plain(b))
        i += 1
    return re.sub(r"\n{3,}", "\n\n\n", "\n".join(out)).strip() + "\n"


def actions(d, tid, text, filename):
    u = d["ui"]
    return (f'<div class="lt-actions"><button type="button" class="kr-btn lt-btn" data-copy="lt-txt-{tid}" data-copied="{esc(u["copied"])}" hidden>{icon("copy")}{esc(u["copy"])}</button>'
            f'<a class="kr-btn lt-btn" href="data:text/plain;charset=utf-8,{quote(text)}" download="{esc(filename)}">{icon("download")}{esc(u["download"])}</a>'
            f'<button type="button" class="kr-btn lt-btn" data-print="{tid}" hidden>{icon("print")}{esc(u["print"])}</button>'
            f'<span class="kr-copied lt-copied" role="status" aria-live="polite"></span></div>'
            f'<pre id="lt-txt-{tid}" class="lt-src" hidden>{esc(text)}</pre>')


def cards_html(blocks):
    """The question cards: a card per question under its category, to cut out."""
    out, cat = [], ""
    for b in blocks:
        if b.startswith("## "): cat = b[3:]
        elif b.startswith("- "): out.append(f'<li class="lt-qcard"><span class="lt-qcard-k">{esc(cat)}</span><span class="lt-qcard-q">{tx(b[2:])}</span></li>')
    return '<ul class="lt-qcards">' + "".join(out) + '</ul>'


def template_section(d, t):
    text = form_text(t["blocks"])
    inner = (f'<p class="lt-tpl-use"><strong>{esc(d["ui"]["template_use"])}:</strong> {tx(t["use"])}</p>' + actions(d, t["id"], text, t["file"])
             + f'<div class="lt-form">{cards_html(t["blocks"]) if t.get("cards") else form_html(t["blocks"])}</div>')
    return (f'<section class="lt-tpl lt-printable" id="{t["id"]}" aria-labelledby="h-{t["id"]}"><h2 id="h-{t["id"]}">{esc(t["title"])}</h2>{inner}</section>')


def template_ref(d, tid):
    t = next(t for t in d["tyokalut"]["templates"] if t["id"] == tid)
    text = form_text(t["blocks"])
    return (f'<div class="lt-tpl-ref"><p><a href="{TOOLS}#{tid}">{icon("notebook")}{esc(t["title"])}</a> <span class="kr-note">{esc(d["ui"]["toolkit_lead_short"])}</span></p>'
            + re.sub(r'<button type="button" class="kr-btn lt-btn" data-print=.*?</button>', "", actions(d, f"{tid}-ref", text, t["file"])) + '</div>')


# --- the start page --------------------------------------------------------------------------------------------------
def hub_body(d, head, ws):
    u, h = d["ui"], d["hub"]
    head = head.replace('<p class="local-desc">', '<p class="local-desc lt-desc">', 1)
    glance = ('<section class="lt-glance" aria-labelledby="h-glance"><h2 id="h-glance">' + esc(h["glance_h"]) + '</h2><ul class="lt-glance-list">'
              + "".join(f'<li><a href="{esc(g["href"])}"><span class="lt-glance-q">{esc(g["q"])}</span><span class="lt-glance-a">{tx(g["a"])}</span></a></li>' for g in h["glance"])
              + '</ul></section>')
    plan = (f'<p class="ahjo-draft lt-plan" role="note">{icon("notebook")}<span><span class="ahjo-badge planned">{esc(u["plan_badge"])}</span> {tx(h["plan_note"])} '
            f'{esc(u["status_ready"])}: ' + ", ".join(esc(w["title"]) for w in ws if w["status"] == "ready") + '.</span></p>')
    intro = sec("mika", h["intro_h"], "".join(f"<p>{tx(p)}</p>" for p in h["intro"])
                + f'<figure class="lt-idea"><blockquote><p>{esc(h["idea"])}</p></blockquote><figcaption>{tx(h["idea_text"])}</figcaption></figure>')
    steps = ('<ol class="lt-path">' + "".join(
        f'<li class="lt-path-step"><a href="{s["page"]}"><span class="lt-path-n" aria-hidden="true">{i}</span>{icon(s["icon"], "ahjo-icon lt-path-icon")}'
        f'<span class="lt-path-t">{esc(s["title"])}</span><span class="lt-path-x">{tx(s["text"])}</span>'
        f'<span class="lt-path-w">{esc(u["lessons"])}: {tx(lessons_label(d, s["lessons"]))}</span></a></li>' for i, s in enumerate(d["sections"], 1)) + '</ol>'
        + f'<p class="lt-start"><a class="ahjo-cta lt-cta" href="{d["sections"][0]["page"]}">{esc(u["start"])}<span aria-hidden="true"> →</span></a> '
        f'<a class="lt-tools-link" href="{TOOLS}">{icon("tools")}{esc(u["nav_tools"])}</a></p>')
    path = sec("polku", h["path_h"], steps, h["path_lead"])
    goals = sec("tavoitteet", h["goals_h"], f'<p>{esc(h["goals_lead"])}</p>' + ul(h["goals"], "lt-goals"))
    rows = "".join(f'<tr><th scope="row"><a href="{s["page"]}">{esc(s["workload"])}</a></th><td>{s["lessons"]}</td><td>{s["lessons"] * 75}</td></tr>' for s in d["sections"])
    total = sum(s["lessons"] for s in d["sections"])
    table = (f'<table class="lt-table lt-workload"><thead><tr><th scope="col">{esc(u["time_part"])}</th><th scope="col">{esc(u["time_lessons"])}</th>'
             f'<th scope="col">{esc(u["time_minutes"])}</th></tr></thead><tbody>{rows}</tbody><tfoot><tr><th scope="row">{esc(u["time_total"])}</th>'
             f'<td>{total}</td><td>{big(total * 75)}</td></tr></tfoot></table>')
    work = sec("tyomaara", h["workload_h"], table + f'<p class="kr-note">{tx(h["workload_rounding"])}</p>' + ul(h["workload_points"]), h["workload_lead"])
    crit = '<ul class="kr-cards lt-criteria">' + "".join(f'<li class="kr-card"><h3>{esc(c["title"])}</h3><p>{tx(c["text"])}</p></li>' for c in h["criteria"]) + '</ul>'
    req = sec("suoritus", h["requirements_h"], f'<p>{esc(h["requirements_lead"])}</p><ol class="lt-req">' + "".join(f"<li>{tx(x)}</li>" for x in h["requirements"]) + '</ol>'
              + f'<h3 id="arviointi">{esc(h["assessment_h"])}</h3><p>{tx(h["assessment_lead"])}</p>{crit}')
    safety = sec("vastuu", h["safety_h"], f'<p class="notice lt-safety-note" role="note">{icon("shield")}<span>{tx(h["safety"])}</span></p>')
    cols = "".join(f'<div class="kr-ahjo-col"><h3>' + (f'<a href="{c["href"]}">{esc(c["title"])}</a>' if c["href"] else esc(c["title"])) + f'</h3>{ul(c["items"])}</div>' for c in h["links"])
    links = sec("yhteydet", h["links_h"], f'<div class="kr-ahjo">{cols}</div>', h["links_lead"])
    models = sec("esikuvat", h["models_h"], '<ul class="lt-models">' + "".join(
        f'<li>{ext_link(d, m["name"], m["url"])} <span class="lt-model-org">{esc(m["org"])}</span><span class="lt-model-idea">{tx(m["idea"])}</span></li>' for m in h["models"])
        + f'</ul><p class="kr-note">{esc(h["models_checked"])}</p>', h["models_lead"])
    return head + nav(d, PAGE) + glance + plan + intro + path + goals + work + req + safety + links + models + pager(d, PAGE)


# --- the five parts --------------------------------------------------------------------------------------------------
def section_of(d, sid): return next(s for s in d["sections"] if s["id"] == sid)


def part_head(d, sid, title, lead):
    s = section_of(d, sid); i = SECTION_IDS.index(sid) + 1
    eyebrow = f'{d["_course_title"]} · {d["ui"]["part_n"].replace("{n}", str(i))} · {lessons_label(d, s["lessons"])}'
    return page_head(d, title, lead, s["page"], eyebrow)


def perehdy_body(d):
    p = d["perehdy"]; u = d["ui"]
    out = part_head(d, "perehdy", p["title"], p["lead"])
    out += sec("miten", p["how_h"], "".join(f"<p>{tx(x)}</p>" for x in p["how"]))
    titles = {t["id"]: t["title"] for t in p["topics"]}
    meet = '<ol class="lt-meetings">' + "".join(
        f'<li class="kr-card"><h3>{esc(m["title"])}</h3><p>{tx(m["text"])}</p><ul class="lt-meet-topics">'
        + "".join(f'<li><a href="#{t}">{esc(titles[t])}</a></li>' for t in m["topics"]) + '</ul></li>' for m in p["meetings"]) + '</ol>'
    out += sec("tapaamiset", p["meetings_h"], meet)
    out += '<ol class="kr-stage-index lt-topic-index">' + "".join(f'<li><a href="#{t["id"]}">{esc(t["title"])}</a></li>' for t in p["topics"]) + '</ol>'
    for i, t in enumerate(p["topics"], 1):
        out += (f'<section class="kr-stage lt-topic" id="{t["id"]}" aria-labelledby="h-{t["id"]}"><header class="kr-stage-head"><span class="kr-stage-n" aria-hidden="true">{i}</span>'
                f'<h2 id="h-{t["id"]}">{esc(t["title"])}</h2></header>'
                + "".join(f"<p>{tx(x)}</p>" for x in t["text"])
                + f'<div class="kr-stage-grid"><div class="lt-points">{ul(t["points"], "lt-keypoints")}</div><div class="kr-stage-do">'
                f'<div class="kr-box kr-box-practice"><h3>{esc(t["practice"]["title"])}</h3><p>{tx(t["practice"]["text"])}</p></div>'
                f'<div class="kr-box kr-box-mentor"><h3>{icon("bulb")}{esc(t["case"]["title"])}</h3><p>{tx(t["case"]["text"])}</p></div></div></div></section>')
    return out + done_box(d, p) + pager(d, section_of(d, "perehdy")["page"])


def tutustu_body(d):
    p = d["tutustu"]
    out = part_head(d, "tutustu", p["title"], p["lead"])
    out += sec("miksi", p["why_h"], "".join(f"<p>{tx(x)}</p>" for x in p["why"]))
    out += sec("tapahtumat", p["kinds_h"], ul(p["kinds"], "lt-tags") + f'<p class="kr-note">{tx(p["kinds_note"])}</p>', p["kinds_lead"])
    out += sec("tavat", p["modes_h"], '<ul class="kr-cards lt-modes">' + "".join(f'<li class="kr-card"><h3>{esc(m["title"])}</h3><p>{tx(m["text"])}</p></li>' for m in p["modes"]) + '</ul>')
    out += sec("vaiheet", p["steps_h"], '<div class="lt-steps3">' + "".join(f'<div class="lt-step3"><h3>{esc(s["title"])}</h3>{ul(s["items"])}</div>' for s in p["steps"]) + '</div>')
    out += sec("havainnointi", p["observe_h"], '<ol class="lt-observe">' + "".join(f"<li>{tx(q)}</li>" for q in p["observe"]) + '</ol>'
               + f'<p>{esc(p["template_note"])}</p>' + template_ref(d, "havainnointi"), p["observe_lead"])
    out += time_box(p)
    return out + done_box(d, p) + pager(d, section_of(d, "tutustu")["page"])


def ws_meta(d, w, tax):
    u = d["ui"]
    dur = u["minutes"].replace("{n}", str(w["minutes"]))
    return ('<dl class="lt-meta">'
            f'<div><dt>{esc(u["audience"])}</dt><dd>{esc(tax["audience"][w["audience"]])}</dd></div>'
            f'<div><dt>{esc(u["topic"])}</dt><dd>{esc(tax["topic"][w["topic"]])}</dd></div>'
            f'<div><dt>{esc(u["duration"])}</dt><dd>{tx(dur)}{(" (" + esc(u["w_planned"]) + ")") if w["status"] == "idea" else ""}</dd></div>'
            f'<div><dt>{esc(u["equipment"])}</dt><dd>{esc(", ".join(tax["equipment"][e] if i == 0 else tax["equipment"][e][0].lower() + tax["equipment"][e][1:] for i, e in enumerate(w["equipment"])))}</dd></div></dl>')


def duration_key(m): return "short" if m <= 20 else "mid" if m <= 30 else "long"


def lesson_links(w, ref):
    refs = [r for r in (ref(x) for x in w.get("lessons", [])) if r]
    return refs


def suunnittele_body(d, ws, ref):
    p, u, tax = d["suunnittele"], d["ui"], d["taxonomy"]
    out = part_head(d, "suunnittele", p["title"], p["lead"])
    def opts(key, values):
        return (f'<label class="lt-f"><span>{esc(u["filter_" + key])}</span><select data-f="{key}"><option value="">{esc(u["filter_all"])}</option>'
                + "".join(f'<option value="{k}">{esc(v)}</option>' for k, v in values) + '</select></label>')
    used = lambda key: [k for k in tax[key] if any(w[key] == k for w in ws)]
    filt = (f'<div class="lt-filter" hidden role="group" aria-labelledby="lt-filter-h"><p id="lt-filter-h" class="lt-filter-h">{esc(u["filter_h"])}</p><div class="lt-filter-row">'
            + opts("topic", [(k, tax["topic"][k]) for k in used("topic")])
            + opts("audience", [(k, tax["audience"][k]) for k in used("audience")])
            + opts("duration", [(k, u["duration_" + k]) for k in ("short", "mid", "long")])
            + opts("equipment", [(k, v) for k, v in tax["equipment"].items() if any(k in w["equipment"] for w in ws)])
            + f'<button type="button" class="kr-btn lt-btn lt-reset">{esc(u["filter_reset"])}</button></div>'
            f'<p class="lt-filter-n" role="status" aria-live="polite" data-shown="{esc(u["filter_shown"])}" data-none="{esc(u["filter_none"])}"></p></div>')
    def card(w):
        attrs = f'data-topic="{w["topic"]}" data-audience="{w["audience"]}" data-duration="{duration_key(w["minutes"])}" data-equipment="{" ".join(w["equipment"])}"'
        badge = f'<span class="ahjo-badge{"" if w["status"] == "ready" else " planned"}">{esc(u["status_ready_short"] if w["status"] == "ready" else u["status_idea"])}</span>'
        if w["status"] == "ready":
            return (f'<li class="lt-wcard lt-ready" id="tp-{w["id"]}" {attrs}><a class="lt-wcard-link" href="{ws_page(w["id"])}"><span class="lt-wcard-head">{badge}</span>'
                    f'<span class="lt-wcard-t">{esc(w["title"])}</span><span class="lt-wcard-x">{tx(w["short"])}</span>{ws_meta(d, w, tax)}'
                    f'<span class="lt-wcard-go">{esc(u["open_card"])}<span aria-hidden="true"> →</span></span></a></li>')
        refs = lesson_links(w, ref)
        more = ([f'<a href="{esc(w["link"]["href"])}">{esc(w["link"]["title"])}</a>'] if w.get("link") else []) + [f'<a href="{href}">{esc(t)}</a>' for t, href in refs]
        return (f'<li class="lt-wcard lt-idea-card" id="tp-{w["id"]}" {attrs}><div class="lt-wcard-head">{badge}</div><h4 class="lt-wcard-t">{esc(w["title"])}</h4>'
                f'<p class="lt-wcard-x">{tx(w["short"])}</p>{ws_meta(d, w, tax)}<p><strong>{esc(u["w_idea"])}:</strong> {tx(w["idea"])}</p>'
                f'<p class="lt-wcard-sub">{esc(u["w_open"])}</p>{ul(w["open"])}<p class="lt-wcard-sub">{esc(u["w_safety_notes"])}</p>{ul(w["safety"])}'
                + (f'<p class="kr-note">' + " · ".join(more) + '</p>' if more else "") + '</li>')
    ready = [w for w in ws if w["status"] == "ready"]; ideas = [w for w in ws if w["status"] == "idea"]
    bank = (filt + f'<div class="lt-wgroup"><h3 id="valmiit">{esc(p["ready_h"])}</h3><ul class="lt-wcards">' + "".join(card(w) for w in ready) + '</ul></div>'
            + f'<div class="lt-wgroup"><h3 id="jatkokehitys">{esc(p["ideas_h"])}</h3><p>{tx(p["ideas_lead"])}</p><ul class="lt-wcards lt-ideas">' + "".join(card(w) for w in ideas) + '</ul></div>'
            + f'<p class="lt-filter-none kr-note" hidden>{esc(u["filter_none"])}</p>')
    out += sec("pankki", p["bank_h"], bank, p["bank_lead"], cls="lt-bank")
    own = '<ol class="lt-own">' + "".join(f'<li><h3>{esc(s["title"])}</h3><p>{tx(s["text"])}</p></li>' for s in p["own_steps"]) + '</ol>' + template_ref(d, "suunnittelu")
    out += sec("oma", p["own_h"], own, p["own_lead"])
    out += time_box(p) + sec("lisaa", p["add_h"], f'<p>{tx(p["add"])}</p>')
    return out + done_box(d, p) + pager(d, section_of(d, "suunnittele")["page"]) + '<script src="lumatutor.js"></script>'


def toteuta_body(d):
    p = d["toteuta"]
    out = part_head(d, "toteuta", p["title"], p["lead"])
    out += sec("tapahtumat", p["kinds_h"], ul(p["kinds"], "lt-tags") + f'<p class="kr-note">{tx(p["kinds_note"])}</p>', p["kinds_lead"])
    out += sec("tehtava", p["task_h"], '<ol class="lt-task">' + "".join(f'<li><h3>{esc(t["q"])}</h3><p>{tx(t["a"])}</p></li>' for t in p["task"]) + '</ol>'
               + template_ref(d, "valmistelu"), p["task_lead"])
    out += sec("roolit", p["roles_h"], '<ul class="kr-cards lt-roles">' + "".join(f'<li class="kr-card"><h3>{esc(r["title"])}</h3><p>{tx(r["text"])}</p></li>' for r in p["roles"]) + '</ul>'
               + f'<p class="kr-note">{tx(p["roles_note"])}</p>')
    out += sec("vastuu", p["responsibility_h"], f'<div class="notice lt-safety-note" role="note">{icon("shield")}{ul(p["responsibility"])}</div>' + template_ref(d, "turvallisuus"))
    out += sec("vertaisohjaus", p["peer_h"], ul(p["peer"], "lt-tags") + f'<p class="kr-note">{tx(p["peer_note"])}</p>', p["peer_lead"])
    out += time_box(p)
    return out + done_box(d, p) + pager(d, section_of(d, "toteuta")["page"])


def arvioi_body(d):
    p, h = d["arvioi"], d["hub"]
    out = part_head(d, "arvioi", p["title"], p["lead"])
    parts = '<ol class="lt-portfolio">' + "".join(
        f'<li class="kr-card"><h3>{esc(x["title"])}</h3><p class="lt-when">{icon("clock")}{esc(x["when"])}</p>{ul(x["items"])}</li>' for x in p["parts"]) + '</ol>'
    out += sec("portfolio", p["portfolio_h"], parts + f'<p>{tx(p["portfolio_template"])}</p>' + template_ref(d, "portfolio"), p["portfolio_lead"])
    rows = "".join(f'<tr><th scope="row">{esc(s["title"])}</th><td>{s["lessons"] * 75}</td></tr>' for s in d["sections"])
    table = (f'<table class="lt-table lt-targets"><caption>{esc(p["time_targets_h"])}</caption><thead><tr><th scope="col">{esc(d["ui"]["time_part"])}</th>'
             f'<th scope="col">{esc(d["ui"]["time_minutes"])}</th></tr></thead><tbody>{rows}</tbody><tfoot><tr><th scope="row">{esc(d["ui"]["time_total"])}</th>'
             f'<td>{big(sum(s["lessons"] for s in d["sections"]) * 75)}</td></tr></tfoot></table>')
    out += sec("tyoaika", p["time_h"], table + f'<p class="kr-note">{tx(h["workload_rounding"])}</p><p>{tx(p["time_template"])}</p>' + template_ref(d, "tyoaika"), p["time_lead"])
    crit = '<ul class="kr-cards lt-criteria">' + "".join(f'<li class="kr-card"><h3>{esc(c["title"])}</h3><p>{tx(c["text"])}</p></li>' for c in h["criteria"]) + '</ul>'
    out += sec("itsearviointi", p["self_h"], crit + template_ref(d, "itsearviointi"), p["self_lead"])
    out += sec("palautus", p["return_h"], "".join(f"<p>{tx(x)}</p>" for x in p["return"]) + f'<p class="ahjo-draft lt-plan" role="note">{icon("notebook")}<span>{tx(h["assessment_lead"])}</span></p>')
    out += (f'<div class="lt-done"><h2 id="tarkista">{esc(p["check_h"])}</h2><ul class="lt-checks">' + "".join(f"<li>{tx(x)}</li>" for x in p["check"]) + '</ul></div>')
    return out + pager(d, section_of(d, "arvioi")["page"])


def tyokalut_body(d):
    p = d["tyokalut"]
    out = page_head(d, p["title"], p["lead"], TOOLS)
    out += f'<p class="lt-how">{tx(p["how"])}</p>'
    out += ('<ol class="lt-tpl-index">' + "".join(f'<li><a href="#{t["id"]}">{esc(t["title"])}</a></li>' for t in p["templates"]) + '</ol>')
    out += "".join(template_section(d, t) for t in p["templates"])
    return out + pager(d, TOOLS) + '<script src="lumatutor.js"></script>'


# --- a workshop's own page -------------------------------------------------------------------------------------------
def encrypt(s, k):
    return "".join(ALPHABET[(ALPHABET.index(c) + k) % len(ALPHABET)] if c in ALPHABET else c for c in s)


def top_letters(s, n=3):
    from collections import Counter
    c = Counter(ch for ch in s if ch in ALPHABET)
    return [k for k, _ in sorted(c.items(), key=lambda kv: (-kv[1], ALPHABET.index(kv[0])))[:n]]


def decimal(lang): return i18n.T(lang)("format.decimal")


def num(v, digits, lang, sign=False):
    s = f"{v:+.{digits}f}" if sign else f"{v:.{digits}f}"
    return s.replace(".", "{,}" if decimal(lang) == "," else ".")


def join_and(items, d):
    items = list(items)
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + f' {d["ui"]["and"]} ' + items[-1]


def decade_means(lang=None):
    import importlib
    s = climate()["temp"]["series"]; out = {}
    for y, v in s:
        if y >= 1880: out.setdefault(y // 10 * 10, []).append(v)
    return {k: (round(sum(v) / len(v), 2), len(v), min(y for y, _ in s if y // 10 * 10 == k), max(y for y, _ in s if y // 10 * 10 == k)) for k, v in sorted(out.items())}


def tokens(w, d, lang):
    """{token: value} of a workshop's computed texts: ciphers from their plain texts, climate answers from the data."""
    t = {"retrieved": climate()["retrieved"]}
    for c in w.get("ciphers", []):
        enc = encrypt(c["plain"], c["shift"])
        t[f"cipher:{c['id']}"] = enc; t[f"plain:{c['id']}"] = c["plain"]; t[f"shift:{c['id']}"] = str(c["shift"])
        top = top_letters(enc)
        t[f"top:{c['id']}"] = join_and(top, d)
        t[f"topplain:{c['id']}"] = join_and([encrypt(x, -c["shift"]) for x in top], d)
    if w.get("data"):
        cd = climate(); co2 = dict((y, v) for y, v in cd["co2"]["series"]); temp = dict((y, v) for y, v in cd["temp"]["series"])
        ppm = lambda v: f"${round(v)}\\,\\text{{ppm}}$"
        deg = lambda v, sign=True: f"${num(v, 2, lang, sign)}\\,^\\circ\\text{{C}}$"
        for y in co2: t[f"co2:{y}"] = ppm(co2[y])
        for a in co2:
            for b in (1990, 2020):
                if a < b and b in co2: t[f"co2diff:{a}-{b}"] = ppm(co2[b] - co2[a])
        warm = sorted(temp, key=temp.get, reverse=True)
        t["warmest:3"] = join_and([str(y) for y in warm[:3]], d)
        cool = max(y for y in temp if y - 1 in temp and temp[y] < temp[y - 1])
        t["cooler"] = d["ui"]["cooler"].replace("{y}", str(cool)).replace("{p}", str(cool - 1))
        dm = decade_means()
        for k, (m, _, _, _) in dm.items(): t[f"decade:{k}"] = deg(m)
        t["decadediff:1960-2010"] = deg(dm[2010][0] - dm[1960][0], False)
    return t


TOKEN = re.compile(r"\{((?:retrieved|cooler)|(?:cipher|plain|shift|top|topplain|co2|co2diff|warmest|decade|decadediff):[A-Za-z0-9-]+)\}")


def fill(s, t):
    def sub(m):
        if m.group(1) not in t: raise KeyError(f"unknown token {{{m.group(1)}}}")
        return t[m.group(1)]
    return TOKEN.sub(sub, s)


def figure_module():
    import importlib.util
    spec = importlib.util.spec_from_file_location("lumatutor_figures", FIG_FILE)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def figure_texts(lang):
    f = ROOT / "content" / lang / "lumatutor" / "figures.json"
    return json.loads(f.read_text()) if lang != i18n.SOURCE and f.is_file() else None


def draw(name, lang, mod=None):
    """(svg, Finnish texts drawn without a translation) of a figure in `lang`."""
    import figlib
    mod = mod or figure_module(); texts = figure_texts(lang)
    if texts is not None: figlib.set_language(texts, decimal(lang))
    try: return mod.FIGURES[name](), list(figlib.MISSING)
    finally:
        if texts is not None: figlib.set_language({}, ",")


def csv_text(series, header):
    return header + "\n" + "\n".join(f"{y},{v}" for y, v in series) + "\n"


def decades_table(d, lang):
    u = d["ui"]; rows = ""
    for k, (m, n_, a, b) in decade_means().items():
        label = u["decade_label"].replace("{d}", str(k)) if n_ == 10 else u["decade_partial"].replace("{a}", str(a)).replace("{b}", str(b))
        rows += f'<tr><th scope="row">{esc(label)}</th><td>${num(m, 2, lang, True)}\\,^\\circ\\text{{C}}$</td></tr>'
    return (f'<table class="lt-table lt-decades"><caption>{esc(u["decade_h"])}</caption><thead><tr><th scope="col">{esc(u["decade_col"])}</th>'
            f'<th scope="col">{esc(u["mean_col"])}</th></tr></thead><tbody>{rows}</tbody></table>')


def decades_text(d, lang):
    u = d["ui"]; out = [u["decade_h"], f'{u["decade_col"]} | {u["mean_col"]}']
    for k, (m, n_, a, b) in decade_means().items():
        label = u["decade_label"].replace("{d}", str(k)) if n_ == 10 else u["decade_partial"].replace("{a}", str(a)).replace("{b}", str(b))
        out.append(f'{label} | {f"{m:+.2f}".replace(".", decimal(lang))} °C')
    return "\n".join(out)


def tl_time(t):
    a, b = t.split("–")
    return f"${a}\\text{{–}}{b}\\,\\text{{min}}$"


def big(n): return f"{n:,}".replace(",", "\u00a0")


def workshop_body(d, w, lang, ref):
    u, tax = d["ui"], d["taxonomy"]
    t = tokens(w, d, lang); F = lambda s: tx(fill(s, t))
    mod = figure_module()
    fig = lambda name: f'<div class="fig lt-fig">{draw(name, lang, mod)[0]}</div>'
    head = (f'<header class="kr-head lt-head lt-ws-head"><p class="ahjo-eyebrow"><a href="{section_of(d, "suunnittele")["page"]}#tp-{w["id"]}">{esc(d["suunnittele"]["bank_h"])}</a></p>'
            f'<h1>{esc(w["title"])}</h1><p class="lead">{F(w["short"])}</p>'
            f'<p class="lt-status"><span class="ahjo-badge planned">{esc(u["status_ready"])}</span></p>{ws_meta(d, w, tax)}'
            f'<p class="lt-group">{icon("people")}{esc(w["group"])}</p></header>' + nav(d, section_of(d, "suunnittele")["page"]).replace(' aria-current="page"', ' aria-current="true"'))
    parts = [("tavoitteet", u["w_goals"]), ("valineet", u["w_materials"]), ("valmistelut", u["w_prep"]), ("turvallisuus", u["w_safety"]), ("toteutus", u["w_steps"]),
             ("tausta", u["w_background"]), ("kysymykset", u["w_questions"]), ("ongelmat", u["w_problems"]), ("eriyttaminen", u["w_variations"]),
             ("lopetus", u["w_closing"]), ("itsearviointi", u["w_self"]), ("osallistujille", u["participant_side"])]
    toc = (f'<nav class="lt-toc" aria-labelledby="h-toc"><h2 id="h-toc" class="lt-toc-h">{esc(u["card_parts_h"])}</h2><ol>'
           + "".join(f'<li><a href="#{i}">{esc(n_)}</a></li>' for i, n_ in parts) + '</ol>'
           + f'<p class="lt-toc-print"><button type="button" class="kr-btn lt-btn" data-print-all hidden>{icon("print")}{esc(u["print_page"])}</button> '
           f'<button type="button" class="kr-btn lt-btn" data-print="osallistujille" hidden>{icon("print")}{esc(u["print"])}: {esc(u["participant_side"])}</button></p></nav>')
    s = lambda id_, title, inner, cls="": f'<section class="lt-part{" " + cls if cls else ""}" id="{id_}" aria-labelledby="h-{id_}"><h3 id="h-{id_}">{esc(title)}</h3>{inner}</section>'
    lst = lambda xs, cls="": f'<ul{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>' + "".join(f"<li>{F(x)}</li>" for x in xs) + "</ul>"
    steps = '<ol class="lt-timeline">' + "".join(
        f'<li><span class="lt-tl-time">{tl_time(st["time"])}</span><div class="lt-tl-body"><h4>{esc(st["title"])}</h4><p>{F(st["do"])}</p>'
        + (f'<p class="lt-say"><span class="lt-say-k">{esc(u["w_say"])}:</span> ”{F(st["say"])}”</p>' if st.get("say") else "") + '</div></li>' for st in w["steps"]) + '</ol>'
    refs = lesson_links(w, ref)
    bg = "".join(f"<p>{F(x)}</p>" for x in w["background"]) + "".join(fig(f) for f in w.get("figures", []))
    if refs: bg += f'<p class="kr-note">Ruukkilabra: ' + ", ".join(f'<a href="{href}">{esc(ti)}</a>' for ti, href in refs) + '</p>'
    if w.get("data"):
        cd = climate()
        bg += (f'<div class="lt-data"><h4>{esc(u["data_h"])}</h4><ul>'
               + "".join(f'<li>{esc(u["data_title_" + k])}. {ext_link(d, u["data_source_" + k], cd[k]["source_url"])} '
                         f'<a class="kr-btn lt-btn" href="data:text/csv;charset=utf-8,{quote(csv_text(cd[k]["series"], u["csv_" + k]))}" download="{esc(u["csv_file_" + k])}">{icon("download")}{esc(u["data_download"])}</a></li>'
                         for k in ("co2", "temp")) + f'</ul><p class="kr-note">{esc(u["data_retrieved"].replace("{d}", cd["retrieved"]))}</p></div>')
    probs = '<dl class="lt-problems">' + "".join(f'<div><dt>{F(x["p"])}</dt><dd>{F(x["f"])}</dd></div>' for x in w["problems"]) + '</dl>'
    var = '<ul class="kr-cards lt-vars">' + "".join(f'<li class="kr-card"><h4>{esc(v["title"])}</h4><p>{F(v["text"])}</p></li>' for v in w["variations"]) + '</ul>'
    answers = (f'<details class="lt-answers"><summary>{esc(u["w_answers"])}</summary>{lst(w["answers"])}</details>' if w.get("answers") else "")
    srcs = ("".join(f"<li>{ext_link(d, x['title'], x['url'])}</li>" for x in w.get("sources", [])))
    tutor = (f'<section class="lt-side lt-tutor" aria-labelledby="h-tutor"><h2 id="h-tutor"><span class="lt-side-badge">{esc(u["tutor_side"])}</span></h2>'
             f'<p class="lt-side-note">{esc(u["tutor_side_note"])}</p>'
             + s("tavoitteet", u["w_goals"], lst(w["goals"]))
             + '<div class="kr-two">' + s("valineet", u["w_materials"], lst(w["materials"])) + s("valmistelut", u["w_prep"], lst(w["prep"], "lt-checks")) + '</div>'
             + s("turvallisuus", u["w_safety"], f'<div class="lt-safety-box">{icon("shield")}{lst(w["safety"])}</div>', "lt-part-safety")
             + s("toteutus", u["w_steps"], steps)
             + s("tausta", u["w_background"], bg + answers)
             + s("kysymykset", u["w_questions"], '<ol class="lt-q3">' + "".join(f"<li>{F(q)}</li>" for q in w["questions"]) + '</ol>')
             + s("ongelmat", u["w_problems"], probs)
             + s("eriyttaminen", u["w_variations"], var)
             + s("lopetus", u["w_closing"], lst(w["closing"]))
             + s("itsearviointi", u["w_self"], lst(w["self"]) + f'<p class="kr-note"><a href="{TOOLS}#itsearviointi">{esc(next(x["title"] for x in d["tyokalut"]["templates"] if x["id"] == "itsearviointi"))}</a></p>')
             + (s("lahteet", u["w_sources"], f'<ul>{srcs}</ul>') if srcs else "") + '</section>')
    pb = [fill(b, t) for b in w["participant"]["blocks"]]
    extra = lambda tok: decades_table(d, lang) if tok == "decades" else ""
    ptext = form_text(pb, lambda tok: decades_text(d, lang) if tok == "decades" else "")
    part = (f'<section class="lt-side lt-participant lt-printable" id="osallistujille" aria-labelledby="h-osallistujille"><h2 id="h-osallistujille"><span class="lt-side-badge">{esc(u["participant_side"])}</span> {esc(w["participant"]["title"])}</h2>'
            f'<p class="lt-side-note">{esc(u["participant_side_note"])}</p>' + actions(d, "osallistujille", ptext, f'{w["id"]}-osallistujille.txt').replace(' data-print="osallistujille" hidden', ' data-print="osallistujille" hidden')
            + f'<div class="lt-form lt-handout">{form_html(pb, fig, extra)}</div></section>')
    back = f'<p class="lt-back"><a href="{section_of(d, "suunnittele")["page"]}#pankki"><span aria-hidden="true">← </span>{esc(u["back_bank"])}</a></p>'
    return head + toc + tutor + part + back + '<script src="lumatutor.js"></script>'


# --- what build.py writes --------------------------------------------------------------------------------------------
def subpages(d, ws, lang, ref):
    """[(file name, title, body, lead)] of the course's pages after its start page."""
    out = [(section_of(d, "perehdy")["page"], d["perehdy"]["title"], perehdy_body(d), d["perehdy"]["lead"]),
           (section_of(d, "tutustu")["page"], d["tutustu"]["title"], tutustu_body(d), d["tutustu"]["lead"]),
           (section_of(d, "suunnittele")["page"], d["suunnittele"]["title"], suunnittele_body(d, ws, ref), d["suunnittele"]["lead"]),
           (section_of(d, "toteuta")["page"], d["toteuta"]["title"], toteuta_body(d), d["toteuta"]["lead"]),
           (section_of(d, "arvioi")["page"], d["arvioi"]["title"], arvioi_body(d), d["arvioi"]["lead"]),
           (TOOLS, d["tyokalut"]["title"], tyokalut_body(d), d["tyokalut"]["lead"])]
    out += [(ws_page(w["id"]), w["title"], workshop_body(d, w, lang, ref), w["short"]) for w in ws if w["status"] == "ready"]
    return out


# --- validation ------------------------------------------------------------------------------------------------------
def _shape(a, b, path=""):
    if isinstance(a, dict):
        if not isinstance(b, dict) or set(a) != set(b): return [path or "/"]
        return [p for k in a for p in _shape(a[k], b[k], f"{path}/{k}")]
    if isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b): return [path]
        return [p for i, (x, y) in enumerate(zip(a, b)) for p in _shape(x, y, f"{path}[{i}]")]
    return []


def _strings(x):
    if isinstance(x, dict):
        for v in x.values(): yield from _strings(v)
    elif isinstance(x, list):
        for v in x: yield from _strings(v)
    elif isinstance(x, str): yield x


KEEP = ("id", "order", "status", "audience", "topic", "minutes", "equipment", "lessons", "data", "figures", "href", "page", "icon", "lessons", "url", "shift", "file", "section", "cards", "log", "topics")


def _same_keys(a, b, path=""):
    """The fields a translation keeps as they are (ids, numbers, links)."""
    errs = []
    if isinstance(a, dict):
        for k in a:
            text = path.startswith("/ui") or isinstance(a[k], dict) or (isinstance(a[k], list) and a[k] and isinstance(a[k][0], dict))
            if k in KEEP and not text and a[k] != b.get(k): errs.append(f"{path}/{k}")
            elif isinstance(a[k], (dict, list)): errs += _same_keys(a[k], b[k], f"{path}/{k}")
    elif isinstance(a, list):
        for i, (x, y) in enumerate(zip(a, b)): errs += _same_keys(x, y, f"{path}[{i}]")
    return errs


def validate(lesson_ids):
    """Errors in lumatutor.json, the workshops and their translations."""
    if not SOURCE.is_file(): return []
    errs, d = [], load()
    ws = workshops()
    if [s["id"] for s in d["sections"]] != SECTION_IDS: errs.append(f"lumatutor.json: sections must be {SECTION_IDS} in this order (the brief)")
    if sum(s["lessons"] for s in d["sections"]) != LESSONS_TOTAL: errs.append(f"lumatutor.json: the sections' lessons add up to {sum(s['lessons'] for s in d['sections'])}, not {LESSONS_TOTAL}")
    for s in d["sections"]:
        if s["icon"] not in ICONS: errs.append(f"lumatutor.json: unknown icon {s['icon']}")
    tpl_ids = [t["id"] for t in d["tyokalut"]["templates"]]
    if len(tpl_ids) != 10 or len(set(tpl_ids)) != 10: errs.append("lumatutor.json: the toolkit has ten templates with their own ids (the brief)")
    for t in d["tyokalut"]["templates"]:
        if not t["file"].endswith(".txt"): errs.append(f"lumatutor.json: template {t['id']} file must be .txt")
        for b in t["blocks"]:
            if not re.match(r"(#|##|\?|\?\?|\[ \]|\.|-|>|=) |\{", b): errs.append(f"lumatutor.json: template {t['id']}: a block without a known prefix: {b[:40]!r}")
    pages = set(all_pages(d, ws))
    for s in _strings(d):
        for m in LINK.finditer(s):
            page, _, frag = m.group(2).partition("#")
            if page.startswith("lumatutor") or page == PAGE:
                if page not in pages: errs.append(f"lumatutor.json: link to {m.group(2)} (no such LUMA-tutor page)")
                if page == TOOLS and frag and frag not in tpl_ids: errs.append(f"lumatutor.json: link to {m.group(2)} (no such template)")
    ids = [w["id"] for w in ws]
    if len(set(ids)) != len(ids): errs.append("lumatutor workshops: ids repeat")
    tax = d["taxonomy"]; figs = set(figure_module().FIGURES) if FIG_FILE.is_file() else set()
    for w in ws:
        where = f"content/fi/{WS_DIR}/{w['id']}.json"
        if w["status"] not in STATUSES: errs.append(f"{where}: status must be one of {STATUSES}")
        if w["audience"] not in tax["audience"] or w["topic"] not in tax["topic"] or any(e not in tax["equipment"] for e in w["equipment"]):
            errs.append(f"{where}: audience, topic or equipment not in lumatutor.json taxonomy")
        bad = [r for r in w.get("lessons", []) if r not in lesson_ids]
        if bad: errs.append(f"{where}: lessons names unknown chapters {bad}")
        if w["status"] == "ready":
            miss = [f for f in READY_FIELDS if not w.get(f)]
            if miss: errs.append(f"{where}: a ready workshop needs {miss}")
            if len(w.get("questions", [])) != 3: errs.append(f"{where}: exactly three questions for the participants (the brief)")
            t0 = 0
            for st in w.get("steps", []):
                m = re.fullmatch(r"(\d+)–(\d+)", st["time"])
                if not m or int(m.group(1)) != t0: errs.append(f"{where}: step {st['title']!r} should start at {t0} min"); break
                t0 = int(m.group(2))
            if t0 != w["minutes"]: errs.append(f"{where}: the steps end at {t0} min, the workshop lasts {w['minutes']} min")
            for f in w.get("figures", []) + [b[8:-1] for b in w.get("participant", {}).get("blocks", []) if b.startswith("{figure:")]:
                if f not in figs: errs.append(f"{where}: no figure {f!r} in lessons/lumatutor/figures.py")
            try:
                t = tokens(w, d, i18n.SOURCE)
                for s in _strings({k: w[k] for k in w if k != "ciphers"}): fill(s, t) if "{" in s and not s.startswith("{figure:") and s != "{decades}" else None
            except KeyError as e: errs.append(f"{where}: {e}")
            for c in w.get("ciphers", []):
                if any(ch.isalpha() and ch not in ALPHABET for ch in c["plain"]): errs.append(f"{where}: cipher {c['id']} plain text must be in capitals A–Ö")
        else:
            for f in ("idea", "open", "safety", "short"):
                if not w.get(f): errs.append(f"{where}: an idea needs {f}")
        for x in w.get("sources", []):
            if not x.get("url", "").startswith("https://"): errs.append(f"{where}: source {x.get('title')!r} needs an https url")
    if sum(w["status"] == "ready" for w in ws) < 5 or sum(w["status"] == "idea" for w in ws) < 5: errs.append("lumatutor workshops: at least five ready and five ideas (the brief)")
    for m in d["hub"]["models"]:
        if not m["url"].startswith("https://"): errs.append(f"lumatutor.json: model {m['name']} needs an https url")
    for lang in i18n.languages():
        f = data_file(lang)
        if f != SOURCE:
            t = json.loads(f.read_text())
            errs += [f"{f.relative_to(ROOT)}: differs from lumatutor.json at {p}" for p in _shape(d, t)]
            errs += [f"{f.relative_to(ROOT)}: {p} must stay as in lumatutor.json" for p in _same_keys(d, t)]
        for wid, wf in ws_files(lang).items():
            if wf.parent.parts[-3] == i18n.SOURCE: continue
            a = json.loads((ROOT / "content" / i18n.SOURCE / WS_DIR / f"{wid}.json").read_text()); b = json.loads(wf.read_text())
            errs += [f"{wf.relative_to(ROOT)}: differs from the Finnish at {p}" for p in _shape(a, b)]
            errs += [f"{wf.relative_to(ROOT)}: {p} must stay as in the Finnish" for p in _same_keys(a, b)]
            for c in b.get("ciphers", []):
                if any(ch.isalpha() and ch not in ALPHABET for ch in c["plain"]): errs.append(f"{wf.relative_to(ROOT)}: cipher {c['id']} plain text must be in capitals A–Ö")
    return errs


if __name__ == "__main__":
    cur = json.loads((ROOT / "curriculum.json").read_text())
    ids = {l["id"] for k, m in cur.items() if not k.startswith("_") for l in m.get("lessons", [])}
    e = validate(ids)
    print("\n".join(e) or "lumatutor.json OK")
    sys.exit(1 if e else 0)
