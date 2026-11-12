"""Named formulas (```kaavat, scripts/kaavat.py; teacher 2026-11-12): the fence's parsing and HTML, what the checks
read, and the review view that lets reviews carry over approved formula names (FY9 units, FY1–FY8 lessons) and nothing else.

  python scripts/test_kaavat.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kaavat, units

fails = []
def ok(cond, what):
    if not cond: fails.append(what)
    print(("ok   " if cond else "FAIL ") + what)

OLD = """Teksti ennen.

```latex
\\begin{aligned}
v &= v_0 + a\\,t \\\\
x &= x_0 + v_0\\,t
\\end{aligned}
```

Teksti välissä.

```latex
Q = sm \\qquad Q = rm
```
"""
NEW = """Teksti ennen.

```kaavat
nopeus :: v = v_0 + a\\,t
paikka :: x = x_0 + v_0\\,t
```

Teksti välissä.

```kaavat
sulamislämpö :: Q = sm
höyrystymislämpö :: Q = rm
```
"""
OK = {("nopeus", "v = v_0 + a\\,t"), ("paikka", "x = x_0 + v_0\\,t"), ("sulamislämpö", "Q = sm"), ("höyrystymislämpö", "Q = rm")}

ok(kaavat.rows("a :: x = 1\ny = 2\n") == [("a", "x = 1"), ("", "y = 2")], "a fence's rows: name and formula, a line without ' :: ' is unnamed")
h = kaavat.as_html("```kaavat\n$\\beta^-$-hajoaminen <b> :: x = 1\ny = 2\n```")
ok('<dl class="kaavat">' in h and "<dt>$\\beta^-$-hajoaminen &lt;b&gt;</dt><dd>$$x = 1$$</dd>" in h, "HTML: the name escaped in a <dt>, the formula as $$...$$ in its <dd>")
ok('class="kaava-rivi nimeton"><dd>$$y = 2$$</dd>' in h, "HTML: an unnamed formula has no <dt> and spans the row")
ok(NEW.count("\n") == kaavat.as_display(NEW).count("\n"), "as_display keeps the line count (the checks' line numbers)")
ok("$$Q = sm$$" in kaavat.as_display(NEW, names=False) and "sulamislämpö" not in kaavat.as_display(NEW, names=False), "as_display without names: only the formulas (the translation check)")
ok(kaavat.canonical(OLD) == kaavat.canonical(NEW), "canonical: an aligned block and a \\qquad row equal the same formulas named")
ok(kaavat.review_view(OLD, OK) == kaavat.review_view(NEW, OK), "review view: approved names carry")
ok(kaavat.review_view(OLD, OK - {("paikka", "x = x_0 + v_0\\,t")}) != kaavat.review_view(NEW, OK - {("paikka", "x = x_0 + v_0\\,t")}), "review view: a name not approved does not carry")
ok(kaavat.review_view(OLD, OK) != kaavat.review_view(NEW.replace("v_0\\,t\n", "v_0 t\n", 1), OK), "review view: a changed formula does not carry")
ok(kaavat.review_view(OLD, OK) != kaavat.review_view(NEW.replace("Teksti välissä", "Toinen teksti"), OK), "review view: changed prose does not carry")
merged = NEW.replace("```\n\nTeksti välissä.\n\n```kaavat\n", "")
ok(kaavat.review_view(OLD, OK) != kaavat.review_view(merged, OK), "review view: formulas regrouped into other blocks do not carry")
ok(kaavat.write(check=True), "every docs/*/kaavanimet.tsv and its texts agree (kaavat.py write --check)")
ok(("tiheys", "\\rho = \\frac{m}{V}") in kaavat.approved("fy1-7", "fi") and ("density", "\\rho = \\frac{m}{V}") in kaavat.approved("fy1-7", "en"),
   "a lesson's names come from its module's list (docs/fy1/kaavanimet.tsv), in each language")
stray = [(f.relative_to(kaavat.ROOT).as_posix(), n) for l in kaavat.LANGS for f in sorted((kaavat.ROOT / "content" / l).glob("FY*/*/lesson.md"))
         for n, t in kaavat.names_of(f.read_text(encoding="utf-8")) if (n, " ".join(t.split())) not in kaavat.approved(f.parent.name, l)]
ok(not stray, "every formula name in a lesson is in its module's approved list" + (f": {stray[:3]}" if stray else ""))
missing = [(l, u) for l in kaavat.LANGS for u in units.ids(l) if u.startswith("fy9-") and "```latex" in (units.folder(u, l) / "unit.md").read_text()
           and any(r["yksikkö"] == u and r[kaavat.LANGS[l]] for r in kaavat.table())]
ok(not missing or all(u == "fy9-koe" for _, u in missing), "every FY9 display formula with a name in the table is named in every language (the koe unit's calculation stays a ```latex block)")

print(f"\n{len(fails)} failure(s)")
sys.exit(1 if fails else 0)
