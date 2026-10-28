"""Hand a translator only the texts of a lesson, and put the translated texts back (README "Languages").
Usage: python scripts/translate_kit.py extract <unit> <lang> <workdir>
       python scripts/translate_kit.py apply <unit> <lang> <workdir>
       python scripts/translate_kit.py changed <unit> <lang> <workdir>

<unit> is a lesson id (fy3-5) or a course's module-end tasks (FY3-sovella). extract writes <workdir>/<lang>/<unit>/:

  strings.json   {"<file>|<path>": "Finnish text"}: every text field of the lesson's JSON files (check_i18n.TEXT_KEYS;
                 practice.TEXT_KEYS for tasks.json). Translate the values; the keys and everything else stay as they are.
  lesson.md, solutions.md
                 the Finnish texts with each figure of figures.py cut to its empty placeholder
                 `<svg data-fig="name"></svg>` (apply draws it again in the language). Translate the text around them.
  figures.json   {"Finnish text figures.py draws": ""}: fill in the translations.

apply copies the Finnish JSON files with the translated strings in place, writes the Markdown and figures.json into
content/<lang>/, draws the figures in the language (figures.py --lang, practice.figures) and prints the unit's
check_i18n / practice.py check errors. A translation already in content/<lang>/ is used as the starting point
of extract, so re-extracting after a Finnish change keeps the work done; `changed` lists the strings whose Finnish
text differs from what the translation was made from (the Finnish of the last extract, kept as source.json), so only
new or changed text is translated again."""
import copy, json, pathlib, re, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n, figlib, importlib.util
from check_i18n import TEXT_KEYS

ROOT = courses.ROOT
PRACTICE_KEYS = {"intro", "title", "text", "detail", "source_note"}


def unit_files(unit, lang):
    """(name, Finnish path, translation path, text keys) of a unit's text files, and its figures.py."""
    if unit.endswith("-sovella"):
        code = unit.split("-")[0]
        fi, tr = ROOT / "content/fi" / code / "sovella", ROOT / "content" / lang / code / "sovella"
        return [("tasks.json", fi / "tasks.json", tr / "tasks.json", PRACTICE_KEYS),
                ("solutions.md", fi / "solutions.md", tr / "solutions.md", None)], ROOT / "lessons" / code / "sovella/figures.py", tr
    fi = courses.find_lesson(unit); tr = ROOT / "content" / lang / fi.parent.name / fi.name
    out = []
    for n in ("meta.json",) + courses.TEXT_FILES:
        if n in courses.CODE_FILES: continue
        a = courses.lesson_file(fi, n)
        if a.exists(): out.append((n, a, courses.lesson_file(tr, n), TEXT_KEYS if n.endswith(".json") else None))
    return out, courses.lesson_file(fi, "figures.py"), tr


def walk(o, keys, path=(), key=None):
    if isinstance(o, dict):
        for k, v in o.items(): yield from walk(v, keys, path + (k,), k)
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from walk(v, keys, path + (i,), key)
    elif isinstance(o, str) and key in keys and o.strip() and not re.fullmatch(r"[a-z0-9_-]+", o): yield path, o   # not ids


def put(o, path, v):
    for p in path[:-1]: o = o[p]
    o[path[-1]] = v


def pathkey(name, path): return name + "|" + ".".join(map(str, path))


def figure_names(figpy):
    if not figpy.is_file(): return {}
    spec = importlib.util.spec_from_file_location("figs_" + figpy.parent.name.replace("-", "_"), figpy)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod.FIGURES


def stub(text, names):
    for nm in names:
        text = re.sub(r'<svg\b[^>]*\bdata-fig="' + re.escape(nm) + r'"[^>]*>.*?</svg>', f'<svg data-fig="{nm}"></svg>', text, flags=re.S)
    return text


def figure_texts(figs, lang):
    """Every Finnish text the figures draw (figlib collects what has no translation)."""
    figlib.set_language({"\0": "\0"}, i18n.T(lang)("format.decimal"))
    for fn in figs.values(): fn()
    found = list(figlib.MISSING); figlib.set_language({}, ","); return found


def extract(unit, lang, work):
    files, figpy, tr = unit_files(unit, lang)
    out = pathlib.Path(work) / lang / unit; out.mkdir(parents=True, exist_ok=True)
    figs = figure_names(figpy)
    strings, source = {}, {}
    for name, a, b, keys in files:
        if keys is not None:
            fi = json.loads(a.read_text()); old = json.loads(b.read_text()) if b.exists() else None
            for path, s in walk(fi, keys):
                k = pathkey(name, path); source[k] = s
                prev = old
                if prev is not None:
                    try:
                        for p in path: prev = prev[p]
                    except (KeyError, IndexError, TypeError): prev = None
                strings[k] = prev if isinstance(prev, str) else s
        else:
            (out / name).write_text(stub((b if b.exists() else a).read_text(), figs))
    (out / "strings.json").write_text(json.dumps(strings, ensure_ascii=False, indent=1) + "\n")
    (out / "source.json").write_text(json.dumps(source, ensure_ascii=False, indent=1) + "\n")
    have = json.loads((tr / "figures.json").read_text()) if (tr / "figures.json").is_file() else {}
    ft = figure_texts(figs, lang)
    if ft: (out / "figures.json").write_text(json.dumps({t: have.get(t, "") for t in ft}, ensure_ascii=False, indent=1) + "\n")
    print(f"{out}: {len(strings)} strings, {len(ft)} figure texts, " + ", ".join(n for n, *_ , k in files if k is None))


def apply(unit, lang, work):
    files, figpy, tr = unit_files(unit, lang)
    src = pathlib.Path(work) / lang / unit
    strings = json.loads((src / "strings.json").read_text())
    for name, a, b, keys in files:
        b.parent.mkdir(parents=True, exist_ok=True)
        if keys is not None:
            data = json.loads(a.read_text()); new = copy.deepcopy(data)
            for path, s in walk(data, keys):
                k = pathkey(name, path)
                if k in strings: put(new, path, strings[k])
            b.write_text(json.dumps(new, ensure_ascii=False, indent=2) + "\n")
        else:
            b.write_text((src / name).read_text())
    if (src / "figures.json").is_file():
        figs = {k: v for k, v in json.loads((src / "figures.json").read_text()).items() if v}
        (tr / "figures.json").write_text(json.dumps(figs, ensure_ascii=False, indent=1) + "\n")
    if unit.endswith("-sovella"):
        code = unit.split("-")[0]
        import practice
        practice.figures(code, lang)
        errs = practice.check(code, lang)
    else:
        if figpy.is_file(): subprocess.run([sys.executable, str(ROOT / "scripts/figures.py"), unit, "--lang", lang])
        import check_i18n
        errs = []; check_i18n.check_lesson(courses.find_lesson(unit), tr, lang, errs)
        import inquiry
        if (tr / "inquiry.json").is_file():                # the build's own checks of the page, in the language
            i18n.set_lang(lang)
            errs += [f"inquiry.json: {e}" for e in inquiry.validate(tr, json.loads((tr / "inquiry.json").read_text()), (tr / "lesson.md").read_text())]
            i18n.set_lang(i18n.SOURCE)
    same = [k for k, v in strings.items() if v == json.loads((src / "source.json").read_text()).get(k) and
            (len(re.findall(r"[a-zäö]{3,}", v)) >= 3 if lang == "en" else len(v) > 160)]
    if same: print(f"note: {len(same)} string(s) still as in Finnish: " + ", ".join(same[:20]))
    print("\n".join(errs) if errs else f"{unit} ({lang}): checks pass")
    return not errs


def changed(unit, lang, work):
    src = pathlib.Path(work) / lang / unit
    before = json.loads((src / "source.json").read_text())
    files, *_ = unit_files(unit, lang)
    for name, a, b, keys in files:
        if keys is None: continue
        for path, s in walk(json.loads(a.read_text()), keys):
            if before.get(pathkey(name, path)) != s: print(pathkey(name, path))


if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[1] not in ("extract", "apply", "changed"): sys.exit(__doc__)
    r = {"extract": extract, "apply": apply, "changed": changed}[sys.argv[1]](*sys.argv[2:])
    sys.exit(0 if r is not False else 1)
