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

  python scripts/kaavat.py write [--check]   write the names of docs/fy9/kaavanimet.tsv into the FY9 unit texts
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FENCE = re.compile(r"```kaavat\n(.*?)```", re.S)
SEP = " :: "
NAMES = ROOT / "docs" / "fy9" / "kaavanimet.tsv"


def rows(body):
    """[(name, tex)] of a fence's body; a line without ` :: ` is a formula without a name."""
    out = []
    for line in body.strip().split("\n"):
        if not line.strip(): continue
        name, tex = line.split(SEP, 1) if SEP in line else ("", line)
        out.append((name.strip(), tex.strip()))
    return out


def as_display(text, names=True):
    """Each ```kaavat fence as display maths, one `$$...$$` per formula on its own line (its name before it when
    `names`), the line count kept: what the checks that read LaTeX and words see."""
    def one(m):
        return "\n" + "\n".join((f"{n} " if names and n else "") + f"$${t}$$" for n, t in rows(m.group(1))) + "\n"   # as many lines as the fence
    return FENCE.sub(one, text)


def as_html(text):
    """Each ```kaavat fence as the formula table's HTML (build.py, before markdown): a `<dl class="kaavat">` whose rows
    are a `<dt>` name and a `<dd>` with the formula as `$$...$$`, typeset by KaTeX in the browser like every formula."""
    def one(m):
        out = []
        for n, t in rows(m.group(1)):
            name = f"<dt>{html.escape(n, quote=False)}</dt>" if n else ""
            out.append(f'<div class="kaava-rivi{"" if n else " nimeton"}">{name}<dd>$${t}$$</dd></div>')
        return '\n<dl class="kaavat">' + "".join(out) + "</dl>\n"
    return FENCE.sub(one, text)


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
                if p: parts.append(p)
        return parts
    def block(texes):
        return "\n<<KAAVAT>>\n" + "\n".join(p for t in texes for p in lines(t)) + "\n<</KAAVAT>>\n"
    text = re.sub(r"```latex\n(.*?)```", lambda m: block([m.group(1)]), text, flags=re.S)
    text = FENCE.sub(lambda m: block([t for _, t in rows(m.group(1))]), text)
    return re.sub(r"\n{2,}", "\n\n", text)


def review_view(text, ok):
    """What a text's reviews judge apart from formula names in `ok` ({(name, formula)}, approved()): its canonical text,
    with every name that is not in `ok` kept beside its formula, so a change carries only when the formulas, the text
    around them and the grouping of the formulas into blocks are as before and every name added is an approved one."""
    def fence(m):
        bad = [f"{n} :: {t}" for n, t in rows(m.group(1)) if n and (n, " ".join(t.split())) not in ok]
        return m.group(0) + ("".join(f"\n<<NIMI {b}>>" for b in bad))
    return canonical(FENCE.sub(fence, text))


def names_of(text):
    """[(name, tex)] of every named formula of a text."""
    return [(n, t) for m in FENCE.finditer(text) for n, t in rows(m.group(1)) if n]


# ------------------------------------------------------------------ FY9: names of docs/fy9/kaavanimet.tsv into the texts
LANGS = {"fi": "nimi", "fi-easy": "nimi", "en": "name_en"}


def table():
    """The rows of docs/fy9/kaavanimet.tsv as dicts."""
    lines = [l for l in NAMES.read_text(encoding="utf-8").split("\n") if l and not l.startswith("#")]
    head = lines[0].split("\t")
    return [dict(zip(head, l.split("\t"))) for l in lines[1:]]


def approved(unit, lang):
    """{(name, canonical formula)} the teacher approved for a unit in a language: what reviews.py lets carry."""
    col = LANGS.get(lang)
    if not col or not NAMES.is_file(): return set()
    out = set()
    for r in table():
        if r["yksikkö"] != unit or not r.get(col): continue
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
    """Rewrite every FY9 display block that has names in the table as a ```kaavat fence. The table's rows are in text
    order per unit; the formulas must match the text's, or nothing is written."""
    import units
    rows_by = {}
    for r in table(): rows_by.setdefault(r["yksikkö"], []).append(r)
    changed, errs = [], []
    for lang, col in LANGS.items():
        for uid, rs in rows_by.items():
            f = units.folder(uid, lang) / "unit.md"
            if not f.is_file(): continue
            text = f.read_text(encoding="utf-8")
            out, pos, k = [], 0, 0
            for m, parts in _blocks(text):
                mine = rs[k:k + len(parts)]; k += len(parts)
                want = [r["kaava"] if lang != "en" else r["kaava_en"] for r in mine]
                if [" ".join(w.split()) for w in want] != parts:
                    errs.append(f"{lang}/{uid}: formulas at {m.start()} differ from the table: {parts} != {want}"); break
                names = [r[col] for r in mine]
                if not any(names): continue                     # a calculation or an unnamed block stays as it is
                fence = "```kaavat\n" + "".join(f"{n}{SEP}{t}\n" if n else f"{t}\n" for n, t in zip(names, want)) + "```"
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


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    if sys.argv[1:2] == ["write"]:
        sys.exit(0 if write("--check" in sys.argv) else 1)
    print(__doc__); sys.exit(1)
