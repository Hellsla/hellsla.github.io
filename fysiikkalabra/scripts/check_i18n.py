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

  a course unit         content/<lang>/units/<id>/ of a local course that lists <lang> in its "translations"
                        (local-courses.json, FY9; teacher 2026-11-04): unit.json, inquiry.json, exit-ticket.json
                        and the task set (practice.py check) are the source unit's data with only the texts
                        translated, unit.md and teacher.md keep its sections, figures and formulas, and its figures
                        are drawn in the language (units.py figures <id> --lang, figures.json in the unit's folder)

A lesson not translated yet is listed, not an error: build.py publishes a language's lessons as they come, each
after its own two reviews (reviews.py; the review files live in the language's folder). An S2 language (S2_LANGS,
Selkeä suomi, NOTES.md §12) needs meta.json key_concepts and may add a formula in a concrete example, never lose one.
Exit 1 on any error."""
import json, re, subprocess, sys, pathlib
from collections import Counter
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses, i18n, inquiry

ROOT = courses.ROOT
TEXT_KEYS = {"text", "reason_prompt", "pending", "detail", "q", "a", "title", "question", "prompt", "feedback", "model", "hint", "hints", "howto", "calc", "label",
             "goals", "prerequisites_note", "glossary", "lead", "summary", "name", "mistakes", "explain", "options", "speaker",
             "claim", "why", "fold", "predictions", "rubric", "note", "words",
             "solution", "contribution", "learn", "prior", "criteria", "pair", "intro", "source_note", "answer", "practice", "caption", "columns"}
WORD_UNIT = re.compile(r"kpl|milj|vrk|kertaa|kierros|heilahdus|toistoa|tuhatta|suuruusluokkaa|ihmistä|annosta|ilma|viivaa|vahvistin|prosenttiyksik")   # a unit that is Finnish words


def is_text(key, value, parent=None):
    """Is this string a text a translation translates? An experiment's column names ({"names": {var: name}}) and a
    unit written in words (kpl, milj. km) are; numbers, ids, symbol units and settings are not."""
    if not isinstance(value, str): return False
    if key == "rows": return not re.fullmatch(r"[−-]?\d+(?:\.\d+)?", value)   # an exercise's data table: numbers stay, words are translated
    if parent in ("names", "values"): return True   # values: {param: {value: words}}, a select's option in words
    if key in ("unit", "units") or parent == "units": return bool(WORD_UNIT.search(value))
    return key in TEXT_KEYS


def value_words(key, parent):
    """The parent key a dict's items are judged under: the words of "values" sit two levels down ({param: {value: words}})."""
    return "values" if parent == "values" else key
JSON_FILES = ("meta.json", "exercises.json", "exit-ticket.json", "inquiry.json")


def lost(a, b, s2=False):
    """Does the translation b lose (or, outside an S2 language, change) a formula of the Finnish text a? An S2 version
    keeps every Finnish formula and may add one in a concrete example ("luvun 170 suuruusluokka on $10^{2}$"; teacher
    2026-11-03, NOTES.md §12); a new number there puts the science reviewer in full review (reviews.py)."""
    fa, fb = Counter(formulas(a)), Counter(formulas(b))
    return bool(fa - fb) if s2 else fa != fb


S2 = False   # set by check_lesson for an S2 language


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
        if lost(a, b, S2): errs.append(f"{path}: formulas differ from Finnish: {formula_diff(a, b)}")
    elif a != b: errs.append(f"{path}: {b!r} differs from Finnish {a!r} (only texts are translated)")


def formulas(text):
    """The LaTeX of a text, \\text{} words set aside: what must stay exactly as it is in every language. A chapter
    reference's title ("(chapter *Power: $P = \\Delta E/\\Delta t$*)") is a name, not a formula of the text: the
    Finnish source may cite the same chapter by a shorter name ("(luku *Teho*)")."""
    text = re.sub(r"\b((?:luku|luvussa|luvusta|luvun|luvuissa|chapter|chapters)\s+)\*[^*]+\*", r"\1", str(text), flags=re.I)
    text = re.sub(r"\((?:luku|chapter)\s[^()*]*\)", "()", text, flags=re.I)   # without the asterisks: "(chapter Heating and cooling …: $Q = cm\\Delta T$)"
    text = re.sub(r"```latex\n(.*?)```", lambda m: "$$" + m.group(1) + "$$", str(text), flags=re.S)
    found = re.findall(r"\$\$(.*?)\$\$", text, re.S) + re.findall(r"(?<!\$)\$([^$\n]+?)\$(?!\$)", re.sub(r"\$\$.*?\$\$", "", text, flags=re.S))
    return sorted(re.sub(r"\s+", "", re.sub(r"\\(text|mathrm)\{[^{}]*\}", r"\\\1{}", f)).replace("{,}", ".") for f in found)   # 4{,}2 = 4.2


def formula_diff(a, b):
    """What a translation lost (-) and added (+) of the Finnish formulas."""
    fa, fb = Counter(formulas(a)), Counter(formulas(b))
    return " ".join([f"-${f}$" for f in (fa - fb).elements()] + [f"+${f}$" for f in (fb - fa).elements()])


def md_shape(text):
    no_svg = re.sub(r"<svg\b.*?</svg>", "", text, flags=re.S)
    return {"figures": re.findall(r'data-fig="([^"]+)"', text), "formulas": formulas(no_svg),
            "blocks": len(re.findall(r"^## ", text, re.M)), "stages": text.count("<!-- vaihe -->"), "sim": text.count("<!-- sim -->")}


S2_LANGS = ("fi-easy",)   # Finnish as a second language: lessons carry "Luvun tärkeät käsitteet" (teacher 2026-11-03, NOTES.md §12)


@__import__("functools").lru_cache(None)
def glossary_terms(): return {g["term"].lower() for g in json.loads((ROOT / "glossary.json").read_text())}


def key_concepts(fi_meta, kc, lang, where, errs):
    """meta.json "key_concepts" of a translation: required in an S2 language, 3–5 {"term", "explain"} with the term
    as glossary.json or the Finnish lesson's glossary names it (a symbol in it set as LaTeX, "$(t,x)$-kuvaaja") (one terminology, never a second glossary), a short
    explanation (at most 25 words) and no term twice; absent from every other language and from the Finnish source."""
    if "key_concepts" in fi_meta: errs.append(f"{where}: the Finnish lesson has key_concepts; they belong to its S2 version only (content/{S2_LANGS[0]}/)")
    if lang not in S2_LANGS:
        if kc is not None: errs.append(f"{where}: key_concepts belong to an S2 language only ({', '.join(S2_LANGS)})")
        return
    lo, hi = inquiry.KEY_CONCEPTS
    if not (isinstance(kc, list) and lo <= len(kc) <= hi):
        errs.append(f"{where}: key_concepts: {lo}–{hi} concepts of the chapter (\"Luvun tärkeät käsitteet\", NOTES.md §12), found {len(kc) if isinstance(kc, list) else 'none'}"); return
    known = glossary_terms() | {t.lower() for t in fi_meta.get("glossary", [])}
    seen = set()
    for i, k in enumerate(kc):
        if not (isinstance(k, dict) and set(k) == {"term", "explain"} and all(isinstance(k[x], str) and k[x].strip() for x in k)):
            errs.append(f"{where}: key_concepts[{i}]: {{\"term\": …, \"explain\": …}}, both non-empty texts"); continue
        if k["term"].replace("$", "").lower() not in known: errs.append(f"{where}: key_concepts[{i}]: \"{k['term']}\" is not a glossary.json term (add it there, or use the glossary's form)")
        if k["term"].replace("$", "").lower() in seen: errs.append(f"{where}: key_concepts[{i}]: \"{k['term']}\" twice")
        seen.add(k["term"].replace("$", "").lower())
        if len(re.sub(r"\$[^$]*\$", "x", k["explain"]).split()) > 25: errs.append(f"{where}: key_concepts[{i}]: the explanation of \"{k['term']}\" is over 25 words; keep it short")


def check_lesson(fi, tr, lang, errs):
    global S2
    rel = tr.relative_to(ROOT); S2 = lang in S2_LANGS
    try: key_concepts(json.loads((fi / "meta.json").read_text()), json.loads((tr / "meta.json").read_text()).get("key_concepts"), lang, f"{rel}/meta.json", errs)
    except (OSError, json.JSONDecodeError) as e: errs.append(f"{rel}/meta.json: {e}")
    for n in courses.TEXT_FILES:
        if n in courses.CODE_FILES: continue
        a, b = courses.lesson_file(fi, n), courses.lesson_file(tr, n)
        if a.exists() != b.exists(): errs.append(f"{b.relative_to(ROOT)}: {'missing' if a.exists() else 'not in the Finnish lesson'}"); continue
        if not a.exists(): continue
        spec = re.compile(r"```voimakuvio(?:\n|\\n).*?```", re.S)                  # drawn force diagrams: the same in every language
        if spec.findall(a.read_text()) != spec.findall(b.read_text()):
            errs.append(f"{b.relative_to(ROOT)}: its ```voimakuvio force-diagram specs differ from the Finnish ones (copy them unchanged)")
        if n.endswith(".json"):
            try: same_data(json.loads(a.read_text()), json.loads(b.read_text()), f"{rel}/{n}", errs)
            except json.JSONDecodeError as e: errs.append(f"{rel}/{n}: {e}")
        else:
            sa, sb = md_shape(a.read_text()), md_shape(b.read_text())
            for k in sa:
                if k == "formulas":
                    if Counter(sa[k]) - Counter(sb[k]) if S2 else sa[k] != sb[k]: errs.append(f"{b.relative_to(ROOT)}: formulas differ from Finnish: {formula_diff(*(re.sub(r'<svg.*?</svg>', '', x.read_text(), flags=re.S) for x in (a, b)))}"[:600])
                    continue
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


UNIT_JSON = ("unit.json", "inquiry.json", "exit-ticket.json")
UNIT_MD = ("unit.md", "teacher.md")
UNIT_SET = ("sovella/tasks.json", "sovella/solutions.md")


def check_unit(uid, lang, errs):
    """A unit's translation (content/<lang>/units/<id>/) against its source (units.lang_of): the checks of a lesson's
    translation, with unit.json for meta.json (its title and description translated, key_concepts in an S2 language)."""
    global S2
    import practice, units
    a, b = units.folder(uid, units.lang_of(uid)), units.folder(uid, lang)
    rel = b.relative_to(ROOT); S2 = lang in S2_LANGS
    for n in UNIT_JSON + UNIT_MD + UNIT_SET:
        if (a / n).exists() != (b / n).exists(): errs.append(f"{rel}/{n}: {'missing' if (a / n).exists() else 'not in the source unit'}")
    try:
        ua, ub = (json.loads((x / "unit.json").read_text()) for x in (a, b))
        key_concepts(ua, ub.pop("key_concepts", None), lang, f"{rel}/unit.json", errs)
        if "description" in ua and "description" in ub:
            if lost(ua["description"], ub["description"], S2): errs.append(f"{rel}/unit.json.description: formulas differ from the source")
            ub["description"] = ua["description"]           # a text, translated
        same_data(ua, ub, f"{rel}/unit.json", errs)
        for n in UNIT_JSON[1:]:
            if (a / n).is_file() and (b / n).is_file(): same_data(json.loads((a / n).read_text()), json.loads((b / n).read_text()), f"{rel}/{n}", errs)
    except (OSError, json.JSONDecodeError) as e: errs.append(f"{rel}: {e}")
    for n in UNIT_MD:
        if not ((a / n).is_file() and (b / n).is_file()): continue
        ta, tb = (a / n).read_text(), (b / n).read_text(); sa, sb = md_shape(ta), md_shape(tb)
        for k in sa:
            if k == "formulas":
                if Counter(sa[k]) - Counter(sb[k]) if S2 else sa[k] != sb[k]: errs.append(f"{rel}/{n}: formulas differ from the source: {formula_diff(*(re.sub(r'<svg.*?</svg>', '', x, flags=re.S) for x in (ta, tb)))}"[:600])
            elif sa[k] != sb[k]: errs.append(f"{rel}/{n}: {k} differ from the source ({sb[k]} vs {sa[k]})"[:400])
        if n == "unit.md":                                  # the sections inquiry.json places, by key
            i18n.set_lang(lang); kb = [inquiry.heading(h)[0] for h in re.findall(r"^## (.+)$", tb, re.M)]
            i18n.set_lang(units.lang_of(uid)); ka = [inquiry.heading(h)[0] for h in re.findall(r"^## (.+)$", ta, re.M)]
            i18n.set_lang(i18n.SOURCE)
            if ka != kb: errs.append(f"{rel}/unit.md: section keys {[k for k in kb if k not in ka]} are not the source's; name the source heading at "
                                     "the end of a translated one: `## The electronic exam {Sähköinen koe}`")
    if (a / UNIT_SET[0]).is_file() and (b / UNIT_SET[0]).is_file():   # its tasks: the same parts, points, answers, criteria; figures in the language
        errs += practice.check(units.task_key(uid), lang)
    try:
        text, new, missing = units.draw(uid, lang)
        if text is not None and new != text: errs.append(f"{rel}/unit.md: figures differ from figures.py (python scripts/units.py figures {uid} --lang {lang})")
        if missing: errs.append(f"{rel}/figures.json has no translation for: " + "; ".join(missing)[:400])
    except Exception as e: errs.append(f"{rel}: figures.py --lang {lang}: {e}")


def unit_translations(lang):
    """(translated, not yet) unit ids of the local courses that list lang in their "translations"."""
    import local_courses, units
    done, todo = [], []
    for code, c in local_courses.load().items():
        if lang not in c.get("translations", []): continue
        for uid in [u["id"] for ch in c.get("chapters", []) for u in ch.get("units", [])]:
            if units.lang_of(uid) is None: continue
            (done if (units.folder(uid, lang) / "unit.json").is_file() else todo).append(uid)
    return done, todo


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
    done, todo = unit_translations(lang)
    for uid in done: check_unit(uid, lang, errs)
    notes += todo
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
