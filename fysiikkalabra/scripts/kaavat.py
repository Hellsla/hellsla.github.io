"""Named formulas (teacher 2026-11-12, "FY09 kaavat nimetään kuten MAFY-taulukossa"): a ```kaavat fence in a text is a
list of formulas, one per line, each with its name before ` :: `, shown like a formula table (the name in bold
beside the formula, above it on a phone):

    ```kaavat
    nopeus tasaisesti kiihtyvässä suoraviivaisessa liikkeessä :: v = v_0 + a\\,t
    paikka tasaisesti kiihtyvässä suoraviivaisessa liikkeessä :: x = x_0 + v_0\\,t + \\tfrac{1}{2}\\,a\\,t^2
    ```

The name is plain text (inline `$...$` allowed); the formula is display LaTeX as in a ```latex fence. The FY9 names
follow the formula tables of mafytaulukot.fi, or are proposals in their style; docs/fy9/kaavanimet.tsv lists every
FY9 formula with its name in each language and is the teacher's approval of the names (reviews.py "formula names").
The modules FY1–FY8 follow one at a time (teacher 2026-11-12, "nimeä ainoastaan kaavat jotka ovat mafyssa"): only a
formula that is in the MAFY tables gets a name, MAFY's own; docs/<fy1>/kaavanimet.tsv lists every display formula of
the module's lessons (first column `tunti`) as the FY9 table lists the units' (first column `yksikkö`).

  python scripts/kaavat.py write [--check]   write the names of every docs/*/kaavanimet.tsv into the texts
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FENCE = re.compile(r"```kaavat\n(.*?)```", re.S)
SEP = " :: "
NAMES = ROOT / "docs" / "fy9" / "kaavanimet.tsv"


def tables():
    """Every approved list: docs/fy9/kaavanimet.tsv (units) and docs/<module>/kaavanimet.tsv (lessons)."""
    return sorted((ROOT / "docs").glob("*/kaavanimet.tsv"))


CONT = ":: "        # a line `:: m = \\rho V`: another form of the named formula above it, shown under its name
EXTRA = "+ "        # a line `+ H = \\dot{H} t`: extra information, not in MAFY's tables; an exam gives it when a task needs it


def parse(body):
    """[(name, tex, continued)] of a fence's body: a line without ` :: ` is a formula without a name (not in the MAFY
    tables), a line starting with `:: ` another form of the formula above (`continued` True), shown under its name, a
    line starting with `+ ` extra information (`continued` "lisa", teacher 2026-11-12: "lisätieto", a formula an exam
    gives when a task needs it), shown with the word Lisätieto in the name column."""
    out = []
    for line in body.strip().split("\n"):
        if not line.strip(): continue
        if line.startswith(CONT): out.append(("", line[len(CONT):].strip(), True)); continue
        if line.startswith(EXTRA): out.append(("", line[len(EXTRA):].strip(), "lisa")); continue
        name, tex = line.split(SEP, 1) if SEP in line else ("", line)
        out.append((name.strip(), tex.strip(), False))
    return out


def rows(body):
    """[(name, tex)] of a fence's body; a formula without a name, or another form of the one above, has the name ""."""
    return [(n, t) for n, t, _ in parse(body)]


JOHDA = re.compile(r"```johda\n(.*?)```", re.S)


def johda_parts(body):
    """(question, [paragraphs of the derivation]) of a ```johda fence: the question, then a line `---`, then the
    derivation in paragraphs (blank lines between them; a paragraph may be display maths `$$...$$`)."""
    q, _, sol = body.partition("\n---\n")
    paras = [" ".join(p.split("\n")).strip() for p in re.split(r"\n\s*\n", sol.strip()) if p.strip()]
    return " ".join(q.split()), paras


def johda_html(text, label, show):
    """Each ```johda fence (teacher 2026-11-12: "Johda itse", a result the exam asks to derive is not given as a
    formula of its own in FY9) as a task in the reading column: the question in view, the derivation behind a closed
    button like a task's solution (the student tries first). Its maths stays $...$ for build.py's stash."""
    def one(m):
        q, paras = johda_parts(m.group(1))
        body = "".join(p if p.startswith("$$") else f"<p>{p}</p>" for p in paras)
        return (f'\n\n<div class="johda"><p class="johda-q"><strong>{html.escape(label)}.</strong> {q}</p>'
                f'<details class="solution johda-sol"><summary>{html.escape(show)}</summary><div class="steps">{body}</div></details></div>\n\n')
    return JOHDA.sub(one, text)


def as_display(text, names=True):
    """Each ```kaavat fence as display maths, one `$$...$$` per formula on its own line (its name before it when
    `names`), the line count kept: what the checks that read LaTeX and words see."""
    def one(m):
        return "\n" + "\n".join((f"{n} " if names and n else "") + f"$${t}$$" for n, t in rows(m.group(1))) + "\n"   # as many lines as the fence
    return FENCE.sub(one, text)


def as_html(text, extra="Lisätieto"):
    """Each ```kaavat fence as the formula table's HTML (build.py, before markdown): a `<dl class="kaavat">` whose rows
    are a `<dt>` name and a `<dd>` with the formula as `$$...$$`, typeset by KaTeX in the browser like every formula."""
    def one(m):
        out = []
        for n, t, cont in parse(m.group(1)):
            if cont == "lisa":
                out.append(f'<div class="kaava-rivi lisatieto"><dt>{html.escape(extra, quote=False)}</dt><dd>$${t}$$</dd></div>'); continue
            name = f"<dt>{html.escape(n, quote=False)}</dt>" if n else ""
            out.append(f'<div class="kaava-rivi{"" if n else " nimeton jatko" if cont else " nimeton"}">{name}<dd>$${t}$$</dd></div>')
        return '\n<dl class="kaavat">' + "".join(out) + "</dl>\n"
    return FENCE.sub(one, text)


JOINERS = {r"\text{ja}", r"\text{and}", r"\text{tai}", r"\text{or}"}


def canonical(text):
    """The text with every display formula (```latex or ```kaavat) reduced to its formulas, one per line, without names
    or alignment marks: two versions that differ only in formula names, alignment (`&`, aligned) and a `\\qquad` between
    two formulas of a row have the same canonical text; each block keeps its formulas in their order (reviews.py
    "formula names")."""
    def lines(tex):
        tex = re.sub(r"\\(?:begin|end)\{aligned\}", "", tex)
        parts = []
        for line in re.split(r"\\\\", tex):
            for p in re.split(r",?\s*\\q?quad\s*", line.replace("&", "")):
                p = " ".join(p.split()).rstrip(",").strip()
                if p and p not in JOINERS: parts.append(p)   # a joining word between two formulas of a row (Q = sm ja Q = rm) is no formula
        return parts
    def block(texes):
        return "\n<<KAAVAT>>\n" + "\n".join(p for t in texes for p in lines(t)) + "\n<</KAAVAT>>\n"
    text = re.sub(r"```latex\n(.*?)```", lambda m: block([m.group(1)]), text, flags=re.S)
    text = FENCE.sub(lambda m: block([t for _, t in rows(m.group(1))]), text)
    return re.sub(r"\n{2,}", "\n\n", text)


ANY = object()      # review_view(passed, ANY): the version a reviewer passed, whose names may all go (teacher 2026-11-12: only MAFY's)


def review_view(text, ok):
    """What a text's reviews judge apart from formula names in `ok` ({(name, formula)}, approved()): its canonical text,
    with every name that is not in `ok` kept beside its formula, so a change carries only when the formulas, the text
    around them and the grouping of the formulas into blocks are as before and every name added is an approved one."""
    def fence(m):
        bad = [f"{n} :: {t}" for n, t in rows(m.group(1)) if n and ok is not ANY and (n, " ".join(t.split())) not in ok]
        return m.group(0) + ("".join(f"\n<<NIMI {b}>>" for b in bad))
    return canonical(FENCE.sub(fence, text))


def names_of(text):
    """[(name, tex)] of every named formula of a text."""
    return [(n, t) for m in FENCE.finditer(text) for n, t in rows(m.group(1)) if n]


# ------------------------------------------------------------------ names of the docs/*/kaavanimet.tsv into the texts
LANGS = {"fi": "nimi", "fi-easy": "nimi", "en": "name_en"}
KEYS = ("yksikkö", "tunti")
SAME = "="                           # in a list's name column: another form of the named formula above (`:: ` in the text)
PLUS = "+"                           # in a list's name column: extra information, not MAFY's (`+ ` in the text)          # the first column: a unit of FY9 or a lesson of FY1–FY8


def table(path=None):
    """The rows of one list (docs/fy9/kaavanimet.tsv by default), or of every list (path "all"), as dicts; "_key" is
    the unit or lesson id, "_kind" its column (yksikkö, tunti)."""
    out = []
    for p in (tables() if path == "all" else [path or NAMES]):
        lines = [l for l in p.read_text(encoding="utf-8").split("\n") if l and not l.startswith("#")]
        head = lines[0].split("\t")
        for l in lines[1:]:
            r = dict(zip(head, l.split("\t"))); r["_kind"] = head[0]; r["_key"] = r[head[0]]; out.append(r)
    return out


def text_file(kind, key, lang):
    """The text a row's formulas are in: a unit's unit.md, a lesson's lesson.md (None when the language has none)."""
    if kind == "yksikkö":
        import units
        f = units.folder(key, lang) / "unit.md"
    else:
        f = next(iter(sorted((ROOT / "content" / lang).glob(f"*/{key}/lesson.md"))), None)
    return f if f and f.is_file() else None


def approved(key, lang):
    """{(name, canonical formula)} the teacher approved for a unit or a lesson in a language: what reviews.py lets carry."""
    col = LANGS.get(lang)
    if not col: return set()
    out = set()
    for r in table("all"):
        if r["_key"] != key or not r.get(col) or r[col] in (SAME, PLUS): continue
        tex = r["kaava"] if lang != "en" else r.get("kaava_en", "")
        out.add((r[col], " ".join(tex.split())))
    return out


def _blocks(text):
    """[(match, [formula lines])] of the display blocks of a text in order (```latex or ```kaavat)."""
    out = []
    for m in re.finditer(r"```(latex|kaavat)\n(.*?)```", text, flags=re.S):
        body = m.group(2)
        texes = [body] if m.group(1) == "latex" else [t for _, t in rows(body)]
        out.append((m, [p for t in texes for p in canonical("```latex\n" + t + "```").split("\n")
                        if p and not p.startswith("<<")]))
    return out


def write(check=False):
    """Rewrite every display block that has names in a list as a ```kaavat fence. A list's rows are in text order per
    unit or lesson; the formulas must match the text's, or nothing is written."""
    rows_by = {}
    for r in table("all"): rows_by.setdefault((r["_kind"], r["_key"]), []).append(r)
    changed, errs = [], []
    for lang, col in LANGS.items():
        for (kind, uid), rs in rows_by.items():
            f = text_file(kind, uid, lang)
            if f is None: continue
            text = f.read_text(encoding="utf-8")
            out, pos, k = [], 0, 0
            for m, parts in _blocks(text):
                mine = rs[k:k + len(parts)]; k += len(parts)
                want = [r["kaava"] if lang != "en" else r["kaava_en"] for r in mine]
                if [" ".join(w.split()) for w in want] != parts:
                    errs.append(f"{lang}/{uid}: formulas at {m.start()} differ from the table: {parts} != {want}"); break
                names = [r[col] for r in mine]
                if not any(n and n != SAME for n in names):     # nothing named: display maths like any other
                    if m.group(1) == "latex": continue          # a calculation or an unnamed block stays as it is
                    fence = "```latex\n" + (want[0] if len(want) == 1 else
                                             "\\begin{aligned}\n" + " \\\\\n".join("&" + w for w in want) + "\n\\end{aligned}") + "\n```"
                else:
                    fence = "```kaavat\n" + "".join(f"{CONT}{t}\n" if n == SAME else f"{EXTRA}{t}\n" if n == PLUS else f"{n}{SEP}{t}\n" if n else f"{t}\n" for n, t in zip(names, want)) + "```"
                if fence == m.group(0): continue
                out.append(text[pos:m.start()] + fence); pos = m.end()
            else:
                if k != len(rs): errs.append(f"{lang}/{uid}: the table has {len(rs)} formulas, the text {k}"); continue
                new = "".join(out) + text[pos:]
                if new != text:
                    changed.append(f"{lang}/{uid}")
                    if not check: f.write_text(new, encoding="utf-8")
    for e in errs: print(e)
    print(f"{len(changed)} text(s) {'would change' if check else 'written'}" + (": " + ", ".join(changed) if changed and check else ""))
    return not errs and not (check and changed)


# ------------------------------------------------------------------ FY9: formulas and symbols as in MAFY (docs/fy9/mafy-tunnukset.tsv)
SYMBOLS = ROOT / "docs" / "fy9" / "mafy-tunnukset.tsv"
ALL_LANGS = set(LANGS)
NL = "⏎"            # a line break in the table's old and new text (a formula's own line in a block)


def symbol_rows(key, lang=None):
    """[(old, new)] of the teacher's exact replacements for a unit in a language (lang None: the rows of every
    language, which also apply to its language-neutral figures.py)."""
    if not SYMBOLS.is_file(): return []
    lines = [l for l in SYMBOLS.read_text(encoding="utf-8").split("\n") if l and not l.startswith("#")]
    head = lines[0].split("\t"); out = []
    for l in lines[1:]:
        r = dict(zip(head, l.split("\t")))
        langs = set(r["kielet"].split(","))
        if r["yksikkö"] == key and (langs >= ALL_LANGS if lang is None else lang in langs): out.append((r["vanha"].replace(NL, "\n"), r["uusi"].replace(NL, "\n")))
    return out


def apply_symbols(key, lang, name, text, canonical=False):
    """`text` (a unit's file `name`; figures.py when lang is None) with the replacements made, in the table's order;
    in a .json file each string is replaced as JSON writes it; `canonical`: as canonical() writes formulas (reviews)."""
    import json
    if not text: return text
    for old, new in symbol_rows(key, lang):
        if canonical: old, new = old.replace("&", "").replace(NL, "\n").strip(), new.replace("&", "").strip()   # canonical(): no alignment marks, a formula per line
        if name.endswith(".json"): old, new = json.dumps(old, ensure_ascii=False)[1:-1], json.dumps(new, ensure_ascii=False)[1:-1]
        text = text.replace(old, new)
    return text


def write_symbols(check=False):
    """Make the replacements of docs/fy9/mafy-tunnukset.tsv in the units' texts and figures.py."""
    import units
    keys = sorted({k for k in {l.split("\t")[0] for l in SYMBOLS.read_text(encoding="utf-8").split("\n")[1:] if l and not l.startswith(("#", "yksikkö"))}})
    changed = []
    for key in keys:
        files = [(units.folder(key, lang) / n, lang, n) for lang in LANGS for n in units.TEXTS] + [(units.code_folder(key) / "figures.py", None, "figures.py")]
        for f, lang, n in files:
            if not f.is_file(): continue
            t = f.read_text(encoding="utf-8"); new = apply_symbols(key, lang, n, t)
            if new != t:
                changed.append(f.relative_to(ROOT).as_posix())
                if not check: f.write_text(new, encoding="utf-8")
    print(f"{len(changed)} file(s) {'would change' if check else 'written'}" + (": " + ", ".join(changed) if changed and check else ""))
    return not (check and changed)


if __name__ == "__main__":
    if sys.argv[1:2] == ["symbols"]:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        sys.exit(0 if write_symbols("--check" in sys.argv) else 1)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    if sys.argv[1:2] == ["write"]:
        sys.exit(0 if write("--check" in sys.argv) else 1)
    print(__doc__); sys.exit(1)
