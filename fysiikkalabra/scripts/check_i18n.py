"""Is every language complete, and does every translation keep the lesson's numbers, formulas and structure?
Usage: python scripts/check_i18n.py [<lang>]

Finnish (fi) is the source. For every other language, lang/<lang>.json and content/<lang>/ (README "Languages"):

  lang/<lang>.json      every key of lang/fi.json, with the same {{placeholders}} (i18n.check)
  courses.json          content/<lang>/courses.json names every module of curriculum.json and every lesson slot
  a lesson's folder     content/<lang>/<COURSE>/<id>/ has the text files its Finnish folder has; meta.json,
                        exercises.json, exit-ticket.json and inquiry.json are the Finnish data with only the
                        texts translated: the same keys, list lengths, ids, answers, units, tolerances, correct
                        options and experiment settings; lesson.md and solutions.md have the same sections
                        (## keys), the same figures (data-fig) and the same formulas once the words in \\text{}
                        are set aside; figures.json translates every text figures.py draws (figures.py --lang)

A lesson not translated yet is listed, not an error: build.py publishes a language's lessons as they come, each
after its own two reviews (reviews.py; the review files live in the language's folder). Exit 1 on any error."""
import json, re, subprocess, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n, inquiry

ROOT = courses.ROOT
TEXT_KEYS = {"text", "q", "a", "title", "question", "prompt", "feedback", "model", "hint", "hints", "howto", "calc", "label",
             "goals", "prerequisites_note", "glossary", "lead", "summary", "name", "mistakes", "explain", "options", "speaker",
             "claim", "why", "predictions", "rubric", "note", "words",
             "solution", "contribution", "learn", "prior", "criteria", "pair", "intro", "source_note", "answer"}
WORD_UNIT = re.compile(r"kpl|milj|vrk|kertaa|toistoa|tuhatta|suuruusluokkaa|ihmistä|annosta|ilma")   # a unit that is Finnish words


def is_text(key, value, parent=None):
    """Is this string a text a translation translates? An experiment's column names ({"names": {var: name}}) and a
    unit written in words (kpl, milj. km) are; numbers, ids, symbol units and settings are not."""
    if not isinstance(value, str): return False
    if parent in ("names", "values"): return True   # values: {param: {value: words}}, a select's option in words
    if key in ("unit", "units") or parent == "units": return bool(WORD_UNIT.search(value))
    return key in TEXT_KEYS


def value_words(key, parent):
    """The parent key a dict's items are judged under: the words of "values" sit two levels down ({param: {value: words}})."""
    return "values" if parent == "values" else key
JSON_FILES = ("meta.json", "exercises.json", "exit-ticket.json", "inquiry.json")


def same_data(a, b, path, errs, key=None, parent=None):
    """b is a translation of a: everything but the texts is identical."""
    if isinstance(a, dict):
        if not isinstance(b, dict) or set(a) != set(b):
            errs.append(f"{path}: keys {sorted(set(a) ^ set(b if isinstance(b, dict) else {}))} differ from Finnish"); return
        for k in a: same_data(a[k], b[k], f"{path}.{k}", errs, k, value_words(key, parent))
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b): errs.append(f"{path}: {len(a)} items in Finnish, {len(b) if isinstance(b, list) else 'not a list'} here"); return
        for i, (x, y) in enumerate(zip(a, b)): same_data(x, y, f"{path}[{i}]", errs, key, parent)
    elif is_text(key, a, parent):
        if formulas(a) != formulas(b): errs.append(f"{path}: formulas differ from Finnish: {formula_diff(a, b)}")
    elif a != b: errs.append(f"{path}: {b!r} differs from Finnish {a!r} (only texts are translated)")


def formulas(text):
    """The LaTeX of a text, \\text{} words set aside: what must stay exactly as it is in every language."""
    text = re.sub(r"```latex\n(.*?)```", lambda m: "$$" + m.group(1) + "$$", str(text), flags=re.S)
    found = re.findall(r"\$\$(.*?)\$\$", text, re.S) + re.findall(r"(?<!\$)\$([^$\n]+?)\$(?!\$)", re.sub(r"\$\$.*?\$\$", "", text, flags=re.S))
    return sorted(re.sub(r"\s+", "", re.sub(r"\\(text|mathrm)\{[^{}]*\}", r"\\\1{}", f)).replace("{,}", ".") for f in found)   # 4{,}2 = 4.2


def formula_diff(a, b):
    """What a translation lost (-) and added (+) of the Finnish formulas."""
    from collections import Counter
    fa, fb = Counter(formulas(a)), Counter(formulas(b))
    return " ".join([f"-${f}$" for f in (fa - fb).elements()] + [f"+${f}$" for f in (fb - fa).elements()])


def md_shape(text):
    no_svg = re.sub(r"<svg\b.*?</svg>", "", text, flags=re.S)
    return {"figures": re.findall(r'data-fig="([^"]+)"', text), "formulas": formulas(no_svg),
            "blocks": len(re.findall(r"^## ", text, re.M)), "stages": text.count("<!-- vaihe -->"), "sim": text.count("<!-- sim -->")}


def check_lesson(fi, tr, lang, errs):
    rel = tr.relative_to(ROOT)
    for n in courses.TEXT_FILES:
        if n in courses.CODE_FILES: continue
        a, b = courses.lesson_file(fi, n), courses.lesson_file(tr, n)
        if a.exists() != b.exists(): errs.append(f"{b.relative_to(ROOT)}: {'missing' if a.exists() else 'not in the Finnish lesson'}"); continue
        if not a.exists(): continue
        if n.endswith(".json"):
            try: same_data(json.loads(a.read_text()), json.loads(b.read_text()), f"{rel}/{n}", errs)
            except json.JSONDecodeError as e: errs.append(f"{rel}/{n}: {e}")
        else:
            sa, sb = md_shape(a.read_text()), md_shape(b.read_text())
            for k in sa:
                if k == "formulas" and sa[k] != sb[k]: errs.append(f"{b.relative_to(ROOT)}: formulas differ from Finnish: {formula_diff(*(re.sub(r'<svg.*?</svg>', '', x.read_text(), flags=re.S) for x in (a, b)))}"[:600]); continue
                if sa[k] != sb[k]: errs.append(f"{rel}/{n}: {k} differ from Finnish ({sb[k]} vs {sa[k]})"[:400])
            if n == "lesson.md":
                i18n.set_lang(lang); kb = [inquiry.heading(h)[0] for h in re.findall(r"^## (.+)$", b.read_text(), re.M)]
                i18n.set_lang(i18n.SOURCE); ka = [inquiry.heading(h)[0] for h in re.findall(r"^## (.+)$", a.read_text(), re.M)]
                if ka != kb: errs.append(f"{b.relative_to(ROOT)}: section keys {[k for k in kb if k not in ka]} are not Finnish ones; "
                                         "name a lesson's own section's Finnish heading at its end: `## The structure of matter {Aineen rakenne}`")
            if n == "solutions.md" and re.findall(r"^## (\S+)", a.read_text(), re.M) != re.findall(r"^## (\S+)", b.read_text(), re.M):
                errs.append(f"{rel}/exercises/solutions.md: the ## exercise ids differ from Finnish")
    if courses.lesson_file(fi, "figures.py").exists():
        r = subprocess.run([sys.executable, str(ROOT / "scripts/figures.py"), fi.name, "--lang", lang, "--check"], capture_output=True, text=True)
        if r.returncode: errs.append(f"{rel}: figures.py --lang {lang}: " + (r.stdout + r.stderr).strip().splitlines()[-1])


def check_language(lang):
    errs, notes = [e for e in i18n.check() if e.startswith(f"lang/{lang}.json")], []
    cur = courses.curriculum(); f = ROOT / "content" / lang / "courses.json"
    tr = json.loads(f.read_text()) if f.is_file() else {}
    for code in courses.codes():
        mod = tr.get(code, {})
        if "title" not in mod: errs.append(f"content/{lang}/courses.json: no title for {code}")
        if len(mod.get("tavoitteet", [])) != len(cur[code].get("tavoitteet", [])): errs.append(f"content/{lang}/courses.json: {code} tavoitteet: {len(mod.get('tavoitteet', []))} of {len(cur[code].get('tavoitteet', []))}")
        missing = [l["id"] for l in cur[code].get("lessons", []) if l["id"] not in mod.get("lessons", {})]
        if missing: errs.append(f"content/{lang}/courses.json: {code} has no title for {', '.join(missing)}")
    for fi in courses.lessons():
        t = courses.translation(fi, lang)
        if not (t / "meta.json").exists(): notes.append(fi.name); continue
        check_lesson(fi, t, lang, errs)
    extra = [t.name for t in courses.lessons(lang=lang) if not (courses.translation(t, i18n.SOURCE) / "meta.json").exists()]
    errs += [f"content/{lang}/: {x} has no Finnish lesson" for x in extra]
    return errs, notes


if __name__ == "__main__":
    langs = sys.argv[1:] or i18n.languages()[1:]
    if not langs: print(f"lang: {i18n.SOURCE} only (the source language); nothing to compare"); sys.exit(0)
    bad = 0
    for lang in langs:
        errs, notes = check_language(lang)
        for e in errs: print("ERROR", e)
        if notes: print(f"note  {lang}: not translated yet: {', '.join(notes)}")
        print(f"{lang}: {len(errs)} error(s)"); bad += bool(errs)
    sys.exit(1 if bad else 0)
