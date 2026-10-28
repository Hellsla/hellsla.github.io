"""The figure catalog: every figure of every course, findable without reading a lesson, its HTML or an SVG body.

  python scripts/figcat.py find <words> [--course FY3] [--kind graph|diagram|illustration|photo] [--reusable]
                                                    one line per matching figure: id, kind, use, description
  python scripts/figcat.py show <id>                one figure's catalog entry and the source code that draws it
  python scripts/figcat.py list [<COURSE>]          every figure of a course, one line each
  python scripts/figcat.py build [--check]          write docs/figures/catalog.json (CI: --check, exit 1 if stale)
  python scripts/figcat.py render <id> [--lang en]  the SVG of one figure (what the page shows)

Where figures come from (nothing here is a second source): `lessons/<COURSE>/<id>/figures.py` and
`lessons/<COURSE>/sovella/figures.py` draw them (scripts/figlib.py, FIGURES = {name: function}); pictures are files in
`assets/pics/<course>/` and `assets/shared/pics/`. A figure's id is `<owner>/<name>`: `fy1-4/scatter`,
`fy3-sovella/fy3-s1-graph`, `pics/fy4/rata.webp`. What the catalog adds is derived: the description is the figure's
accessible label (Fig(..., label)), the kind is read from how it is drawn (Axes → graph; the chapter's opening
illustration and label-free scenes → illustration; anything else with labels → diagram; a picture file → photo or
image), its labels are the LaTeX it draws, its topics are the owner lesson's title and glossary (stored once per
lesson in "lessons"), and where it is used is found in every language's texts (`data-fig="name"` in the owner's
lesson.md or solutions.md, `"figure": "<id>"` in exercises.json, inquiry.json and tasks.json). A copy of a figure pasted
by hand somewhere (an SVG with the same description) is listed as such, so it can be replaced by a reference.

The one hand-written annotation is `REUSE = {name: note}` in figures.py, only where the default is not enough:
"safe" (shows no answer of any task that could use it), "reveals: <what>" (e.g. the fitted line and its slope), or
"decorative". Without a note an illustration is "decorative" and any other figure "unchecked" (read its
description before putting it into a task). A variant for a task, from the same data, is one more entry in
FIGURES: `"scatter-points": lambda: scatter(fit=False)`, with its own label that does not give the answer away.

SVGs in a lesson's texts that no figures.py draws (hand-made before figures.py existed) are listed with
"managed": false and an id `<owner>/~<file>-<n>`; they cannot be referenced until figures.py draws them.

The source slice (source_slice) is the code that draws one figure: its FIGURES entry and every function and constant
of figures.py it uses. reviews.py hashes the slice of each figure a task refers to, so changing another figure in
the same figures.py never stales that task, while changing this one's data or drawing does.
"""
import ast, functools, hashlib, html, importlib.util, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, figlib, i18n

ROOT = courses.ROOT
CATALOG = ROOT / "docs" / "figures" / "catalog.json"
KINDS = ("graph", "diagram", "illustration", "photo", "image")
REF = re.compile(r'"figure"\s*:\s*"([^"]+)"')
FIG_ID = re.compile(r"^([a-z0-9-]+)/([A-Za-z0-9_-]+)$")
PHOTO, IMAGE = (".jpg", ".jpeg", ".webp", ".avif"), (".png", ".svg", ".gif")


# --- owners: a lesson or a course's Sovella itsenäisesti, each with its figures.py and its texts --------------------
def owners():
    """[(owner id, code folder, text folders of the source language)] of every figures.py, in a stable order."""
    out = []
    for code in courses.codes():
        for folder in courses.lessons(code):
            out.append((folder.name, courses.code_dir(folder), folder))
        sov = ROOT / "lessons" / code / "sovella"
        if (sov / "figures.py").is_file(): out.append((f"{courses.slug(code)}-sovella", sov, ROOT / "content" / i18n.SOURCE / code / "sovella"))
    return [o for o in out if (o[1] / "figures.py").is_file()]


def owner(oid):
    """(code folder, text folder) of an owner id, or None."""
    m = re.match(r"^([a-z]+\d+)-sovella$", oid)
    if m:
        code = m.group(1).upper(); return ROOT / "lessons" / code / "sovella", ROOT / "content" / i18n.SOURCE / code / "sovella"
    lid = courses.LESSON_ID.match(oid)
    if not lid: return None
    for folder in courses.lessons():
        if folder.name == oid: return courses.code_dir(folder), folder
    return None


def text_folder(oid, lang):
    """The owner's texts in another language (content/<lang>/<COURSE>/<id>/ or …/sovella/)."""
    o = owner(oid)
    return o and ROOT / "content" / lang / o[1].relative_to(ROOT / "content" / i18n.SOURCE)


@functools.lru_cache(maxsize=None)
def module(code_folder):
    f = pathlib.Path(code_folder) / "figures.py"
    spec = importlib.util.spec_from_file_location(f"figures_{f.parent.parent.name}_{f.parent.name}".replace("-", "_"), f)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


# --- rendering: one figure as the page shows it, in any language -----------------------------------------------------
def split_id(fid):
    m = FIG_ID.match(fid or "")
    return (m.group(1), m.group(2)) if m else (None, None)


def exists(fid):
    oid, name = split_id(fid)
    o = oid and owner(oid)
    return bool(o and (o[0] / "figures.py").is_file() and name in module(str(o[0])).FIGURES)


@functools.lru_cache(maxsize=None)
def module_from(text):
    """figures.py as some commit had it (the exercises a page keeps while a newer version waits for review)."""
    mod = type(sys)("figures_at_commit"); exec(compile(text, "figures.py", "exec"), mod.__dict__)
    return mod


def render(fid, lang=i18n.SOURCE, read=None):
    """The SVG of figure `fid` (data-fig set to its id), its words in `lang` from the owner's figures.json there.
    read(relpath) gives figures.py as an earlier commit had it (reviews.Commit.read); default the working tree.
    Raises KeyError for an unknown id."""
    oid, name = split_id(fid)
    o = oid and owner(oid)
    code = read(code_rel(fid)) if (read and o) else None
    mod = module_from(code) if code else module(str(o[0])) if o and (o[0] / "figures.py").is_file() else None
    if mod is None or name not in mod.FIGURES: raise KeyError(f"no figure {fid!r} (python scripts/figcat.py find … lists them)")
    if lang != i18n.SOURCE:
        tr = text_folder(oid, lang) / "figures.json"
        figlib.set_language(json.loads(tr.read_text()) if tr.is_file() else {}, i18n.T(lang)("format.decimal"))
    try: svg = mod.FIGURES[name]()
    finally:
        if lang != i18n.SOURCE: figlib.set_language({}, ",")
    return re.sub(r'^<svg\b(?: data-fig="[^"]*")?', f'<svg data-fig="{html.escape(fid)}"', svg, count=1)


def figure_html(fid, lang=i18n.SOURCE, read=None):
    """A referenced figure in a task: the SVG in the page's figure frame (site.css .fig), never cropped on a phone."""
    return f'<div class="fig task-fig">{render(fid, lang, read)}</div>'


# --- the source slice of one figure (what a review of a task that uses it judges) ------------------------------------
def source_slice(text, name):
    """The code of figures.py that draws figure `name`: its FIGURES entry and, transitively, every top-level function,
    class and constant of the file it uses, in file order. None when the file or the name is missing."""
    if text is None: return None
    try: tree = ast.parse(text)
    except SyntaxError: return text                     # a broken file: the whole file, so any change shows
    defs, entry = {}, None
    for node in tree.body:
        names = [node.name] if isinstance(node, (ast.FunctionDef, ast.ClassDef)) else \
                [t.id for t in getattr(node, "targets", []) if isinstance(t, ast.Name)] + \
                ([node.target.id] if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) else [])
        for nm in names:
            if nm == "FIGURES" and isinstance(node.value, ast.Dict):
                for k, v in zip(node.value.keys, node.value.values):
                    if isinstance(k, ast.Constant) and k.value == name: entry = v
            else: defs[nm] = node
    if entry is None: return None
    used, todo, seen = [], [entry], set()
    while todo:
        n = todo.pop()
        for sub in ast.walk(n):
            if isinstance(sub, ast.Name) and sub.id in defs and sub.id not in seen:
                seen.add(sub.id); used.append(defs[sub.id]); todo.append(defs[sub.id])
    lines = text.splitlines()
    parts = [ast.get_source_segment(text, node) or "" for node in sorted(set(used), key=lambda n: n.lineno)]
    return "\n\n".join(parts + [f"FIGURES[{name!r}] = {ast.get_source_segment(text, entry)}"])


def refs_in(text):
    """Figure ids a text refers to with "figure": "<id>" (exercises.json, inquiry.json, tasks.json)."""
    return list(dict.fromkeys(REF.findall(text or "")))


def slice_of(fid, read):
    """The source slice of figure `fid` as `read(relpath)` sees figures.py (the working tree or a commit), or None."""
    rel = code_rel(fid)
    return rel and source_slice(read(rel), split_id(fid)[1])


def check_refs(text):
    """[(figure id, problem)] for the figure references in one text: each must name a figure that figures.py draws (an
    unmanaged, hand-pasted SVG or a decorative illustration cannot carry a task)."""
    errs = []
    for fid in refs_in(text):
        if not exists(fid): errs.append((fid, f"\"figure\": \"{fid}\" names no figure (python scripts/figcat.py find … lists them)"))
        else:
            oid, name = split_id(fid)
            note = getattr(module(str(owner(oid)[0])), "REUSE", {}).get(name, "")
            if note == "decorative" or name in ("hero", "scene"): errs.append((fid, f"{fid} is a decorative illustration: it carries nothing a task can use"))
    return errs


def code_rel(fid):
    """figures.py of a figure id, relative to ROOT (what reviews.py reads from git), or None."""
    oid, _ = split_id(fid)
    o = oid and owner(oid)
    return o and (o[0] / "figures.py").relative_to(ROOT).as_posix()


# --- building the catalog ---------------------------------------------------------------------------------------
LABEL = re.compile(r'<div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex"[^>]*>(?:<span[^>]*>)?\$(.*?)\$')
ARIA = re.compile(r'<svg\b[^>]*\baria-label="([^"]*)"')


def _labels(svg):
    """The distinct LaTeX labels a figure draws, in order, without bare tick numbers (searchable, short)."""
    out = []
    for t in LABEL.findall(svg):
        t = html.unescape(t)
        if re.fullmatch(r"[-\d{},.\s]+", t) or t in out: continue
        out.append(t)
    return out


def _fig_calls(src):
    """[(function name, label)] of every Fig(..., "label") a figures.py makes, read from its code (a function that
    FIGURES does not list may still draw a figure that was pasted into a text by hand)."""
    out = []
    try: tree = ast.parse(src)
    except SyntaxError: return out
    for fn in tree.body:
        if not isinstance(fn, ast.FunctionDef): continue
        for c in ast.walk(fn):
            if isinstance(c, ast.Call) and getattr(c.func, "id", None) == "Fig" and len(c.args) >= 3:
                try: out.append((fn.name, ast.literal_eval(c.args[2])))
                except ValueError: pass
    return out


def _kind(svg, name, made_axes):
    if made_axes: return "graph"
    if 'class="fig-hero"' in svg or name in ("hero", "scene") or "fig-tex" not in svg: return "illustration"
    return "diagram"


def _section(text, pos):
    """The `## ` heading a position of lesson.md or solutions.md sits under (the place a figure is used)."""
    heads = [m for m in re.finditer(r"^##+ (.+)$", text[:pos], re.M)]
    return heads[-1].group(1).strip() if heads else ""


def _uses():
    """{figure id: [where]} and {owner: [(file, n, label)] unmanaged SVGs} from the texts of every language."""
    uses, hand = {}, {}
    for lang_dir in sorted(p for p in (ROOT / "content").iterdir() if p.is_dir() and not p.name.startswith("_")):
        lang = lang_dir.name
        for f in sorted(lang_dir.rglob("*")):
            if not f.is_file() or f.suffix not in (".md", ".json") or "/review/" in f.as_posix() + "/" or f.name == "figures.json": continue
            text = f.read_text(); rel = f.relative_to(ROOT / "content" / lang).as_posix()
            parts = rel.split("/"); oid = parts[1] if parts[1] != "sovella" else f"{parts[0].lower()}-sovella"
            for fid in refs_in(text): uses.setdefault(fid, []).append(f"{lang}:{rel}")
            if lang != i18n.SOURCE: continue
            for i, m in enumerate(re.finditer(r"<svg\b[^>]*>", text.replace('\\"', '"'))):
                tag = m.group(0); name = re.search(r'data-fig="([^"]*)"', tag)
                label = html.unescape((ARIA.search(tag) or [None, ""])[1])
                if name and "/" not in name.group(1):
                    sec = _section(text, m.start()) if f.suffix == ".md" else ""
                    where = f"{lang}:{rel}" + (f" § {sec}" if sec else "")
                    uses.setdefault(f"{oid}/{name.group(1)}", []).append(where)
                else: hand.setdefault(oid, []).append((rel, i + 1, label, name.group(1) if name else None))
    return uses, hand


def _lang_status(oid, fid, langs):
    """{lang: "ok" | "missing <n>" | "no text"} for the languages other than the source: whether the owner's
    figures.json in that language translates every word the figure draws."""
    out = {}
    for lang in langs:
        tr = text_folder(oid, lang) / "figures.json"
        if not tr.parent.is_dir(): out[lang] = "no text"; continue
        figlib.set_language(json.loads(tr.read_text()) if tr.is_file() else {}, i18n.T(lang)("format.decimal"))
        try: module(str(owner(oid)[0])).FIGURES[split_id(fid)[1]]()
        except Exception: pass
        out[lang] = "ok" if not figlib.MISSING else f"missing {len(figlib.MISSING)}"
        figlib.set_language({}, ",")
    return out


def build():
    """The catalog as a dict (deterministic: no times, sorted)."""
    uses, hand = _uses()
    langs = sorted(p.stem for p in (ROOT / "lang").glob("*.json") if p.stem != i18n.SOURCE)
    lessons, figures = {}, []
    for oid, code, texts in owners():
        meta = json.loads((texts / "meta.json").read_text()) if (texts / "meta.json").is_file() else {}
        course = texts.parent.name
        lessons[oid] = {"course": course, "title": meta.get("title") or f"{course} Sovella itsenäisesti",
                        "topics": meta.get("glossary", [])}
        mod = module(str(code)); reuse = getattr(mod, "REUSE", {}); src = (code / "figures.py").read_text()
        labels_by_aria = {}
        for name, fn in mod.FIGURES.items():
            made = []
            orig = figlib.Axes.__init__
            def spy(self, *a, **k): made.append(1); orig(self, *a, **k)
            figlib.Axes.__init__ = spy
            try: svg = fn()
            finally: figlib.Axes.__init__ = orig
            vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
            kind = _kind(svg, name, made)
            fid = f"{oid}/{name}"
            label = html.unescape((ARIA.search(svg) or [None, ""])[1])
            labels_by_aria[label] = fid
            note = reuse.get(name) or ("decorative" if kind == "illustration" else "unchecked")
            entry = {"id": fid, "kind": kind, "reuse": note, "description": label, "labels": _labels(svg)[:14],
                     "size": [int(float(vb.group(1))), int(float(vb.group(2)))] if vb else None,
                     "source": f"{code.relative_to(ROOT).as_posix()}/figures.py#{name}",
                     "slice": hashlib.sha256(source_slice(src, name).encode()).hexdigest()[:12],
                     "used_in": sorted(uses.get(fid, []))}
            if langs: entry["languages"] = _lang_status(oid, fid, langs)
            figures.append(entry)
        for rel, i, label, nm in hand.get(oid, []):
            copy_of = labels_by_aria.get(label)
            drawn = next((fn for fn, lab in _fig_calls(src) if label and lab == label), None) if not copy_of else None
            figures.append({"id": f"{oid}/~{pathlib.PurePosixPath(rel).name.split('.')[0]}-{i}",
                            "kind": "graph" if re.search(r"kuvaaj|mittauspist|pylväs", label, re.I) else "diagram",
                            "reuse": "unmanaged", "description": label, "managed": False,
                            "source": f"content/{i18n.SOURCE}/{rel}" + (f" (data-fig=\"{nm}\")" if nm else ""),
                            **({"copy_of": copy_of} if copy_of else {}),
                            **({"drawn_by": f"{code.relative_to(ROOT).as_posix()}/figures.py:{drawn}() (not in FIGURES)"} if drawn else {})})
    pic_users = courses.deps()
    for d in ("pics", "shared/pics"):
        for f in sorted((ROOT / "assets" / d).rglob("*")):
            if not f.is_file() or f.name.startswith(".") or f.suffix.lower() not in PHOTO + IMAGE: continue
            ref = f.relative_to(ROOT / "assets").as_posix()
            users = sorted(pic_users.get(ref, []))
            figures.append({"id": ref, "kind": "photo" if f.suffix.lower() in PHOTO else "image", "reuse": "unchecked",
                            "description": "", "source": f"assets/{ref}", "used_in": users})
    return {"about": "Generated by scripts/figcat.py build from figures.py, lesson meta and texts; do not edit. "
                     "Search: python scripts/figcat.py find <words>. Reference in a task: \"figure\": \"<id>\".",
            "lessons": lessons, "figures": figures}


def dump(cat):
    """One figure per line: small diffs, and a reader can grep one line without parsing the rest."""
    one = lambda x: json.dumps(x, ensure_ascii=False, separators=(",", ":"))
    les = ",\n".join(f"  {one(k)}:{one(v)}" for k, v in cat["lessons"].items())
    figs = ",\n".join(f"  {one(f)}" for f in cat["figures"])
    return f'{{\n "about": {one(cat["about"])},\n "lessons": {{\n{les}\n }},\n "figures": [\n{figs}\n ]\n}}\n'


def load():
    return json.loads(CATALOG.read_text()) if CATALOG.is_file() else build()


# --- searching --------------------------------------------------------------------------------------------------
def _fold(s): return re.sub(r"[^a-z0-9äöå]+", " ", s.lower())


def _line(f, lessons):
    les = lessons.get(f["id"].split("/")[0], {})
    use = "used " + str(len(f.get("used_in", []))) if f.get("used_in") else "unused"
    desc = f["description"] if len(f["description"]) <= 170 else f["description"][:167].rsplit(" ", 1)[0] + " …"
    return f"{f['id']:<34} {f['kind']:<12} {f["reuse"][:44]:<44} {use:<7} {les.get('title', '')[:38]} | {desc}"


def find(words, course=None, kind=None, reusable=False):
    cat = load(); les = cat["lessons"]; ws = [_fold(w).strip() for w in words if w.strip()]
    out = []
    for f in cat["figures"]:
        L = les.get(f["id"].split("/")[0], {})
        if course and L.get("course", f["id"].split("/")[1].upper() if f["id"].startswith("pics/") else "") != course: continue
        if kind and f["kind"] != kind: continue
        if reusable and (f["reuse"] in ("decorative", "unmanaged") or f["reuse"].startswith("reveals")): continue
        hay = _fold(" ".join([f["id"], f["description"], " ".join(f.get("labels", [])), L.get("title", ""), " ".join(L.get("topics", []))]))
        if all(w in hay for w in ws): out.append(_line(f, les))
    return out


def show(fid):
    cat = load(); f = next((x for x in cat["figures"] if x["id"] == fid), None)
    if f is None: return f"no figure {fid!r}"
    out = json.dumps(f, ensure_ascii=False, indent=1)
    if f.get("managed", True) and not fid.startswith(("pics/", "shared/")):
        rel = code_rel(fid); out += "\n\n# " + rel + "\n" + source_slice((ROOT / rel).read_text(), split_id(fid)[1])
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k: a[a.index(k) + 1] if k in a else None
    if not a: sys.exit(__doc__)
    cmd, rest = a[0], [x for i, x in enumerate(a[1:], 1) if not x.startswith("--") and not (i > 1 and a[i - 1] in ("--course", "--kind", "--lang"))]
    if cmd == "build":
        text = dump(build())
        if "--check" in a:
            ok = CATALOG.is_file() and CATALOG.read_text() == text
            print("figure catalog up to date" if ok else "docs/figures/catalog.json is stale: python scripts/figcat.py build"); sys.exit(0 if ok else 1)
        CATALOG.parent.mkdir(parents=True, exist_ok=True); CATALOG.write_text(text)
        print(f"wrote {CATALOG.relative_to(ROOT)}: {len(json.loads(text)['figures'])} figures")
    elif cmd in ("find", "list"):
        res = find(rest if cmd == "find" else [], course=opt("--course") or (rest[0] if cmd == "list" and rest else None),
                   kind=opt("--kind"), reusable="--reusable" in a)
        print("\n".join(res) if res else "no figure matches"); print(f"({len(res)} figures)", file=sys.stderr)
    elif cmd == "show": print(show(rest[0]))
    elif cmd == "render": print(render(rest[0], opt("--lang") or i18n.SOURCE))
    else: sys.exit(__doc__)
