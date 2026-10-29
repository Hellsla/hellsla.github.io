"""The site's languages: every text a visitor sees comes from content/<lang>/ (long texts, one folder per page) or
lang/<lang>.json (short interface texts). Finnish (fi) is the source language; another language is added by creating
content/<lang>/ and lang/<lang>.json, nothing else (README "Languages").

lang/<lang>.json groups its keys by where they are shown: "format" (html lang, locale), "site" (header, menus,
footer, front and course pages), "lesson" (the lesson page built by build.py), "inquiry" (the inquiry stages built by
inquiry.py), "js" (messages of lesson.js, inquiry.js and sim-embed.js in the browser) and "sims" (one block per
simulation: its buttons, slider labels, readouts and canvas labels). A value may hold placeholders {{name}}, filled
in by t() here and by __() in the browser; formulas, numbers and units stay in the value exactly as they are shown.

A simulation calls __('key') or __(`key`, {name: expr}) where it used to have the literal. resolve_js() puts the
strings back: the quote of the key is the quote of the original literal, so the resolved sim.js is byte for byte the
file as it was before its texts moved here. The review hash (reviews.py) and the checks that read a simulation's
labels (lint_lesson.py, review_packet.py) read the resolved file, so moving a text changes no hash, while changing a
simulation's wording in lang/fi.json changes its lesson's hash like any other content change.

  python scripts/i18n.py resolve <sim.js> [lang]   print the simulation with its texts in place
  python scripts/i18n.py check                     every language has every key of fi, with the same placeholders
"""
import json, os, pathlib, re, sys

ROOT = pathlib.Path(os.environ.get("FYSIIKKALABRA_ROOT") or pathlib.Path(__file__).resolve().parents[1])
SOURCE = "fi"
PLACEHOLDER = re.compile(r"\{\{(\w+)\}\}")
_cache = {}


def languages():
    """The languages the site has: fi first, then every other lang/<code>.json in alphabetical order."""
    codes = sorted(p.stem for p in (ROOT / "lang").glob("*.json"))
    return [SOURCE] + [c for c in codes if c != SOURCE]


def strings(lang=SOURCE):
    if lang not in _cache: _cache[lang] = json.loads((ROOT / "lang" / f"{lang}.json").read_text())
    return _cache[lang]


def lookup(table, key):
    v = table
    for part in key.split("."):
        if not isinstance(v, dict) or part not in v: raise KeyError(f"lang: no key {key!r}")
        v = v[part]
    return v


def fill(text, vals):
    return PLACEHOLDER.sub(lambda m: str(vals[m.group(1)]) if m.group(1) in vals else m.group(0), text)


class T:
    """t("lesson.check") -> "Tarkista"; t("lesson.tasks", n=5) fills {{n}}. Missing keys fall back to Finnish."""
    def __init__(self, lang=SOURCE): self.lang = lang
    def __call__(self, key, **vals):
        try: v = lookup(strings(self.lang), key)
        except KeyError:
            if self.lang == SOURCE: raise
            v = lookup(strings(SOURCE), key)
        return fill(v, vals) if isinstance(v, str) else v
    def count(self, key, n, **vals):
        """A text with a number: the value is {"one": "{{n}} oppitunti", "other": "{{n}} oppituntia"}, so 1 never reads
        "1 oppituntia" or "1 lessons". t.count("site.lessons_n", 8) -> "8 oppituntia"."""
        v = self(key)
        if isinstance(v, dict): v = v["one" if n == 1 else "other"]
        return fill(v, dict(vals, n=n))
    def has(self, key):
        try: lookup(strings(SOURCE), key); return True
        except KeyError: return False


t = T()


def set_lang(lang):
    """The language that t() (and so build.py and inquiry.py) renders in from now on."""
    t.lang = lang


# ---------------------------------------------------------------- simulations
def _skip_string(s, i):
    """Index after the string literal (' or ") that starts at s[i]."""
    q = s[i]; i += 1
    while i < len(s) and s[i] != q:
        i += 2 if s[i] == "\\" else 1
    return i + 1


def _skip_template(s, i):
    """Index after the template literal that starts at s[i], ${...} parts included."""
    i += 1
    while i < len(s) and s[i] != "`":
        if s[i] == "\\": i += 2
        elif s.startswith("${", i): i = _skip_code(s, i + 2, "}") + 1
        else: i += 1
    return i + 1


def _skip_code(s, i, close):
    """Index of the bracket `close` that ends the code starting at s[i] (strings, templates and brackets skipped)."""
    depth = 0
    while i < len(s):
        c = s[i]
        if c in "'\"": i = _skip_string(s, i); continue
        if c == "`": i = _skip_template(s, i); continue
        if c in "([{": depth += 1
        elif c in ")]}":
            if depth == 0 and c == close: return i
            depth -= 1
        i += 1
    raise ValueError("unbalanced brackets")


def _split_args(s):
    """'a: x, b: f(y, z)' -> [('a', 'x'), ('b', 'f(y, z)')], expressions verbatim."""
    out, i, start, depth = [], 0, 0, 0
    while i <= len(s):
        if i == len(s) or (s[i] == "," and depth == 0):
            part = s[start:i].strip()
            if part:
                m = re.match(r"(\w+)\s*:\s*", part)
                if not m: raise ValueError(f"__(): an argument must be name: expression, not {part!r}")
                out.append((m.group(1), part[m.end():]))
            start = i + 1; i += 1; continue
        c = s[i]
        if c in "'\"": i = _skip_string(s, i); continue
        if c == "`": i = _skip_template(s, i); continue
        if c in "([{": depth += 1
        elif c in ")]}": depth -= 1
        i += 1
    return out


def js_literal(text, quote):
    """The JS source of a string literal with this value (the escapes the simulations use)."""
    text = text.replace("\\", "\\\\").replace("\n", "\\n")
    if quote == "`": return "`" + text.replace("`", "\\`").replace("${", "\\${") + "`"
    return quote + text.replace(quote, "\\" + quote) + quote


CALL = re.compile(r"(?<![\w$.])__\((['\"`])([\w.-]+)\1\s*(,|\))")
VALUE = re.compile(r"(?<![\w$.])__v\(")


def _strip_values(src):
    """__v(expr) -> expr: a displayed identifier (a material, a body, a process) shown in the page's language from the
    simulation's "values" block; in Finnish the value is shown as it is, so the call stands for the bare expression."""
    out, pos = [], 0
    for m in VALUE.finditer(src):
        if m.start() < pos: continue
        end = _skip_code(src, m.end(), ")")
        out.append(src[pos:m.start()]); out.append(_strip_values(src[m.end():end])); pos = end + 1
    out.append(src[pos:])
    return "".join(out)


def resolve_js(src, table):
    """The simulation source with every __('key') / __(`key`, {name: expr}) call replaced by the literal it stands
    for, from `table` (the simulation's block of lang/<lang>.json), and every __v(expr) by expr. A key the table
    lacks is left as the call."""
    src = _strip_values(src)
    out, pos = [], 0
    for m in CALL.finditer(src):
        if m.start() < pos: continue                 # inside an argument already resolved
        quote, key = m.group(1), m.group(2)
        args, end = [], m.end()
        if m.group(3) == ",":
            ob = src.index("{", m.end())
            cb = _skip_code(src, ob + 1, "}")
            args = _split_args(src[ob + 1:cb])
            end = _skip_code(src, cb + 1, ")") + 1
        if key not in table: continue
        value = table[key]
        if args:
            vals = {name: "${" + resolve_js(expr, table) + "}" for name, expr in args}
            parts = PLACEHOLDER.split(value)          # text, name, text, name, ...
            lit = "`" + "".join(js_literal(p, "`")[1:-1] if k % 2 == 0 else vals[p] for k, p in enumerate(parts)) + "`"
        else: lit = js_literal(value, quote)
        out.append(src[pos:m.start()]); out.append(lit); pos = end
    out.append(src[pos:])
    return "".join(out)


def sim_key(path):
    """The block of lang/<lang>.json "sims" that a simulation file uses: the lesson id for an FY3 sim.js in its lesson
    folder, the simulation folder's name otherwise (assets/sims/fy4/fy4-1/sim.js -> fy4-1)."""
    p = pathlib.PurePosixPath(str(path))
    return p.parent.name


def sim_strings(key, lang=SOURCE, table=None):
    sims = (table if table is not None else strings(lang)).get("sims", {})
    return sims.get(key, {})


def resolved_sim(path, lang=SOURCE):
    """A simulation file's text with its strings in place (what the reviews and the label checks read)."""
    path = pathlib.Path(path)
    return resolve_js(path.read_text(), sim_strings(sim_key(path), lang))


def browser_strings(sim_key_=None, lang=SOURCE):
    """The strings a page's scripts need, as one JSON object: the js block and the page's simulation block."""
    tab = strings(lang)
    out = {"js": tab.get("js", {})}
    if sim_key_: out["sim"] = sim_strings(sim_key_, lang)
    return out


# ---------------------------------------------------------------- check
def _flat(d, prefix=""):
    for k, v in d.items():
        if isinstance(v, dict): yield from _flat(v, f"{prefix}{k}.")
        else: yield f"{prefix}{k}", v


def check():
    """Problems as strings: a key fi has and another language lacks (or the other way), a different set of
    placeholders. Empty list when every language is complete."""
    errs = []
    fi = dict(_flat(strings(SOURCE)))
    for lang in languages()[1:]:
        other = dict(_flat(strings(lang)))
        for k in fi:
            if k not in other: errs.append(f"lang/{lang}.json: missing {k}")
            elif isinstance(fi[k], str) and set(PLACEHOLDER.findall(fi[k])) != set(PLACEHOLDER.findall(str(other[k]))):
                errs.append(f"lang/{lang}.json: {k} has placeholders {sorted(set(PLACEHOLDER.findall(str(other[k]))))}, fi has {sorted(set(PLACEHOLDER.findall(fi[k])))}")
        errs += [f"lang/{lang}.json: {k} is not in lang/fi.json" for k in other if k not in fi]
    return errs


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "resolve":
        print(resolved_sim(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else SOURCE), end="")
    elif len(sys.argv) == 2 and sys.argv[1] == "check":
        e = check(); print("\n".join(e) if e else f"lang: {', '.join(languages())} complete"); sys.exit(1 if e else 0)
    else: sys.exit(__doc__)
