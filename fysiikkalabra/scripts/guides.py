"""TVT-ohjeet: reusable guides to the skills and tools that experimental work needs (teacher's brief 2026-10-31):
plotting measured points, fitting a line, reading its slope and constant term, the slope's uncertainty, video
analysis, spreadsheets, sensors and their software, speed and distance from data, graphs in the report.

  python scripts/guides.py check              validate every guide and every link to one (CI)
  python scripts/guides.py hash <id>          the content hash a reviewer puts in its report
  python scripts/guides.py status             reviewed | draft of every guide
  python scripts/guides.py figures <id> [--check]   lessons/tvt/<id>/figures.py into guide.md

One guide is written once and linked from every investigation that needs the skill, never copied into them.

  content/<lang>/tvt/<id>/guide.json   id, title, description (one sentence), learn (1–3 goals completing "Tässä
        ohjeessa opit"), kind: "taito" (a general skill, any tool) | "ohjelma" (a tool: spreadsheet, sensor software,
        video analysis), order (its place in the list)
  content/<lang>/tvt/<id>/guide.md     `## ` sections: what the skill is for, the steps, the common mistakes; inline
        figures as `<svg data-fig="name"></svg>` filled from figures.py; `[[ohje:<id>|label]]` links another guide;
        a screenshot as `<figure class="shot"><img src="pics/tvt/<file>" alt="…" width=".." height=".."><figcaption>…`
        on a line of its own, the file in assets/pics/tvt/ (part of the content hash, copied to the site by build.py)
  content/<lang>/tvt/<id>/review/      science.md and pedagogy.md, as an investigation's
  lessons/tvt/<id>/figures.py          the figures (scripts/figlib.py); example data on a figure is labelled as an
        example, never presented as a measurement

An investigation names the guides of a tvt prerequisite with "guides": [ids] (investigations.py), and its text
links one with `[[ohje:<id>|label]]`. build.py publishes site/<id>.html when both reviews PASS for the current hash,
lists the published guides on the course page of FY10, and on each guide the published investigations that use it.
A link to a guide this language has not published is shown as plain text, never as a broken link.
"""
import hashlib, importlib.util, json, re, sys, pathlib, html as _h
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n

ROOT = courses.ROOT
DIR = "tvt"
TEXTS = ("guide.json", "guide.md")
KINDS = ("taito", "ohjelma")
esc = lambda s: _h.escape(str(s), quote=True)


def folder(gid, lang=i18n.SOURCE): return ROOT / "content" / lang / DIR / gid
def code_folder(gid): return ROOT / "lessons" / DIR / gid


def ids(lang=i18n.SOURCE):
    base = ROOT / "content" / lang / DIR
    found = [p.name for p in base.iterdir() if (p / "guide.json").is_file()] if base.is_dir() else []
    return sorted(found, key=lambda g: (load(g, lang).get("order", 99), g))


def load(gid, lang=i18n.SOURCE): return json.loads((folder(gid, lang) / "guide.json").read_text())


def content_hash(gid, lang=i18n.SOURCE):
    from reviews import normalized
    h = hashlib.sha256()
    for name in TEXTS:
        p = folder(gid, lang) / name
        if p.is_file(): h.update(name.encode() + b"\0" + normalized(p.read_text(), name).encode() + b"\0")
    p = code_folder(gid) / "figures.py"
    if p.is_file(): h.update(b"figures.py\0" + p.read_bytes() + b"\0")
    for ref in pic_refs(gid, lang):                          # a changed screenshot needs a new review like changed text
        src = courses.pic_source(ref)
        h.update(ref.encode() + b"\0" + (src.read_bytes() if src.is_file() else b"missing") + b"\0")
    return h.hexdigest()[:16]


def pic_refs(gid, lang=i18n.SOURCE):
    """Pictures (pics/tvt/x.png) the guide's text refers to, in order."""
    return courses.pic_refs_in([(folder(gid, lang) / "guide.md").read_text()])


def status(gid, lang=i18n.SOURCE):
    """{'state': reviewed|draft, 'hash', 'reports': {science|pedagogy|visual: PASS|FAIL|stale|missing}, 'baseline'}: the gate
    of reviews.item_status (three reviews; a visual baseline row for exactly this hash stands in for the visual one)"""
    from reviews import item_status
    return item_status("guide", gid, lang, folder(gid, lang), content_hash(gid, lang))


def check(gid, lang=i18n.SOURCE):
    """Error lines: required fields, known kind, links to guides that exist, figures in place, no lesson id."""
    errs = []; d = load(gid, lang); where = f"{DIR}/{gid}"
    cur = {k: v for k, v in json.loads((ROOT / "curriculum.json").read_text()).items() if not k.startswith("_")}
    lessons = {l["id"] for m in cur.values() for l in m.get("lessons", [])}
    if d.get("id") != gid: errs.append(f"{where}: id {d.get('id')!r} is not the folder name")
    if gid in lessons or not gid.startswith("tvt-"): errs.append(f"{where}: a guide id starts with tvt- and is no lesson id")
    for f in ("title", "description", "learn", "kind"):
        if not d.get(f): errs.append(f"{where}: no {f}")
    if not 1 <= len(d.get("learn", [])) <= 3: errs.append(f"{where}: learn has 1–3 goals")
    if d.get("kind") not in KINDS: errs.append(f"{where}: kind is one of {KINDS}")
    md = (folder(gid, lang) / "guide.md").read_text()
    known = set(ids(i18n.SOURCE))
    errs += [f"{where}: link to guide {t}, which does not exist" for t in re.findall(r"\[\[ohje:([\w-]+)", md) if t not in known]
    if re.search(r'<svg data-fig="[^"]*"></svg>', md): errs.append(f"{where}: empty figure: run guides.py figures {gid}")
    if "\\vec" in md or "\\mathbf" in md: errs.append(f"{where}: vectors are \\overline{{F}} (teacher 2026-10-29)")
    if "×" in md: errs.append(f"{where}: multiplication is \\cdot (teacher's rule 8)")
    errs += [f"{where}: {m}: write the menu name in bold as the school's Graphical Analysis shows it in Finnish; a name no screenshot confirms is described, with the English name in brackets once (teacher 2026-10-31)"
             for m in sorted(set(re.findall(r"\{\{ga:[^}]*\}\}", md)))]
    errs += [f"{where}: picture {r} not found (expected assets/{r})" for r in pic_refs(gid, lang) if not courses.pic_source(r).is_file()]
    for img in re.findall(r"<img\b[^>]*>", md):
        if not re.search(r'\balt="[^"]{10,}"', img): errs.append(f"{where}: {img[:60]}…: a picture needs an alt text that says what it shows")
        if not re.search(r'\bwidth="\d+"', img) or not re.search(r'\bheight="\d+"', img): errs.append(f"{where}: {img[:60]}…: width and height keep the page from jumping while it loads")
    return errs


def figures(gid, write=True):
    """Fill every <svg data-fig="name"> of guide.md from figures.py; returns True when it was up to date."""
    src = code_folder(gid) / "figures.py"
    if not src.is_file(): return True
    spec = importlib.util.spec_from_file_location("figures", src)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    md = folder(gid) / "guide.md"; text = md.read_text(); new = text
    for name, fn in mod.FIGURES.items():
        pat = re.compile(r'<svg\b[^>]*\bdata-fig="' + re.escape(name) + r'"[^>]*>.*?</svg>', re.S)
        if not pat.search(new): print(f"no <svg data-fig=\"{name}\"> in guide.md"); continue
        svg = fn()
        if "data-fig=" not in svg: svg = svg.replace("<svg ", f'<svg data-fig="{name}" ', 1)
        new = pat.sub(lambda m: svg, new, count=1)
    if write and new != text: md.write_text(new)
    return new == text


def link(gid, label, published, lang=i18n.SOURCE):
    """A guide as a link where this language published it, else its name as plain text."""
    return f'<a class="tvt-link" href="{gid}.html">{esc(label)}</a>' if f"{gid}.html" in published else esc(label)


def inline_links(text, published, lang=i18n.SOURCE):
    """`[[ohje:<id>|label]]` in a guide's or an investigation's markdown: a link where published, else the label."""
    return re.sub(r"\[\[ohje:([\w-]+)\|([^\]]+)\]\]", lambda m: link(m.group(1), m.group(2), published, lang), text)


def render(gid, lang, T, md, published, users):
    """(body html, toc html) of a guide page. md renders markdown with maths; published: the page names this language
    built; users: [(investigation id, title)] of the published investigations that name this guide."""
    d = load(gid, lang)
    text = inline_links((folder(gid, lang) / "guide.md").read_text(), published, lang)
    html = re.sub(r"<p>\s*(<figure\b.*?</figure>)\s*</p>", r"\1", md(text), flags=re.S)   # a figure is no paragraph
    sections = re.split(r"(?=<h2>)", html)
    intro, rest = sections[0], sections[1:]
    def anchor(h): return re.sub(r"[^a-z0-9äö]+", "-", h.lower()).strip("-").replace("ä", "a").replace("ö", "o")
    toc = []; parts = []
    for s in rest:
        h = re.sub(r"<[^>]+>", "", re.match(r"<h2>(.*?)</h2>", s).group(1)); a = anchor(h); toc.append((a, h))
        parts.append(f'<section class="inv-section" id="{a}">' + s.replace("<h2>", f'<h2 id="h-{a}">', 1) + "</section>")
    learn = "".join(f"<li>{esc(g)}</li>" for g in d["learn"])
    used = ""
    if users:
        used = (f'<p class="tvt-used"><strong>{T("guides.used_by")}</strong> '
                + ", ".join(f'<a href="{i}.html">{esc(t)}</a>' for i, t in users) + "</p>")
    opening = (f'<p class="notice tvt-kind" role="note">{T("guides.kind_" + d["kind"])}</p>'
               f'<div class="inv-learn"><h2 id="h-tavoitteet">{T("guides.learn")}</h2><ul>{learn}</ul></div>')
    # the investigations that use the guide close the page (up to 27 links would push the steps far down on a phone)
    body = f'<article id="teoria" class="investigation guide">{intro}{opening}{"".join(parts)}{used}</article>'
    return body, "".join(f'<a href="#{a}">{esc(t)}</a>' for a, t in toc)


def course_section(T, published, lang=i18n.SOURCE):
    """The list of published guides for a course page (FY10): title and one sentence each."""
    items = "".join(f'<li class="live"><a href="{g}.html">{esc(load(g, lang)["title"])}</a>'
                    f'<span class="local-why">{esc(load(g, lang)["description"])}</span></li>'
                    for g in ids(lang) if f"{g}.html" in published)
    if not items: return ""
    return (f'<h2 id="tvt-ohjeet">{T("guides.course_heading")}</h2><p class="section-lead">{T("guides.course_lead")}</p>'
            f'<ul class="lessons local-inv tvt-list">{items}</ul>')


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "check":
        errs = [e for lang in i18n.languages() for gid in ids(lang) for e in check(gid, lang)]
        errs += [f"{DIR}/{gid}: figures differ from figures.py (guides.py figures {gid})" for gid in ids() if not figures(gid, write=False)]
        print("\n".join(errs) or f"{len(ids())} guide(s) ok"); sys.exit(1 if errs else 0)
    if cmd == "hash": print(content_hash(sys.argv[2], sys.argv[sys.argv.index("--lang") + 1] if "--lang" in sys.argv else i18n.SOURCE))
    if cmd == "status":
        for lang in i18n.languages():
            for gid in ids(lang): print(lang, gid, status(gid, lang))
    if cmd == "figures":
        ok = figures(sys.argv[2], write="--check" not in sys.argv)
        print("figures up to date" if ok else ("figures differ" if "--check" in sys.argv else "figures written")); sys.exit(0 if ok or "--check" not in sys.argv else 1)
