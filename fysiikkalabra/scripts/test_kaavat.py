"""Named formulas (```kaavat, scripts/kaavat.py; teacher 2026-11-12): the fence's parsing and HTML, what the checks
read, and the review view that lets reviews carry over approved formula names (FY9 units, FY1–FY8 lessons) and nothing else.

  python scripts/test_kaavat.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kaavat

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
ok('class="kaava-rivi nimeton"><dd>$$y = 2$$</dd>' in h, "HTML: an unnamed formula has no <dt> (not in the MAFY tables)")
ok(kaavat.parse("tiheys :: \\rho = m/V\n:: m = \\rho V\ny = 2\n") == [("tiheys", "\\rho = m/V", False), ("", "m = \\rho V", True), ("", "y = 2", False)],
   "a line ':: tex' is another form of the named formula above, a plain line a formula without a name")
ok(kaavat.parse("+ H = \\dot{H} t\n") == [("", "H = \\dot{H} t", "lisa")] and kaavat.names_of("```kaavat\n+ H = \\dot{H} t\n```") == [],
   "a line '+ tex' is extra information, not a named formula")
ok('<div class="kaava-rivi lisatieto"><dt>Lisätieto</dt><dd>$$H = \\dot{H} t$$</dd></div>' in kaavat.as_html("```kaavat\n+ H = \\dot{H} t\n```", "Lisätieto"),
   "HTML: extra information shows the word Lisätieto in the name column")
ok('class="kaava-rivi nimeton jatko"><dd>$$m = \\rho V$$</dd>' in kaavat.as_html("```kaavat\ntiheys :: \\rho = m/V\n:: m = \\rho V\n```"), "HTML: another form of a named formula is a continued row")
ok(not any(n == kaavat.SAME for n, _ in kaavat.approved("fy1-7", "fi")), "the list's '=' (another form of the formula above) is no name")
ok(NEW.count("\n") == kaavat.as_display(NEW).count("\n"), "as_display keeps the line count (the checks' line numbers)")
ok("$$Q = sm$$" in kaavat.as_display(NEW, names=False) and "sulamislämpö" not in kaavat.as_display(NEW, names=False), "as_display without names: only the formulas (the translation check)")
ok(kaavat.canonical(OLD) == kaavat.canonical(NEW), "canonical: an aligned block and a \\qquad row equal the same formulas named")
ok(kaavat.review_view(OLD, OK) == kaavat.review_view(NEW, OK), "review view: approved names carry")
ok(kaavat.review_view(OLD, OK - {("paikka", "x = x_0 + v_0\\,t")}) != kaavat.review_view(NEW, OK - {("paikka", "x = x_0 + v_0\\,t")}), "review view: a name not approved does not carry")
ok(kaavat.review_view(OLD, OK) != kaavat.review_view(NEW.replace("v_0\\,t\n", "v_0 t\n", 1), OK), "review view: a changed formula does not carry")
ok(kaavat.review_view(OLD, OK) != kaavat.review_view(NEW.replace("Teksti välissä", "Toinen teksti"), OK), "review view: changed prose does not carry")
ok(kaavat.review_view(NEW, kaavat.ANY) == kaavat.review_view(OLD, set()), "review view: names of the passed version taken out carry (only MAFY's names, teacher 2026-11-12)")
ok(kaavat.review_view(NEW, kaavat.ANY) != kaavat.review_view(NEW, OK - {("paikka", "x = x_0 + v_0\\,t")}), "review view: a passed name kept that is no longer approved does not carry")
merged = NEW.replace("```\n\nTeksti välissä.\n\n```kaavat\n", "")
ok(kaavat.review_view(OLD, OK) != kaavat.review_view(merged, OK), "review view: formulas regrouped into other blocks do not carry")
ok(kaavat.write(check=True), "every docs/*/kaavanimet.tsv and its texts agree (kaavat.py write --check)")
ok(("tiheys", "\\rho = \\frac{m}{V}") in kaavat.approved("fy1-7", "fi") and ("density", "\\rho = \\frac{m}{V}") in kaavat.approved("fy1-7", "en"),
   "a lesson's names come from its module's list (docs/fy1/kaavanimet.tsv), in each language")
stray = [(f.relative_to(kaavat.ROOT).as_posix(), n) for l in kaavat.LANGS for f in sorted((kaavat.ROOT / "content" / l).glob("FY*/*/lesson.md"))
         for n, t in kaavat.names_of(f.read_text(encoding="utf-8")) if (n, " ".join(t.split())) not in kaavat.approved(f.parent.name, l)]
ok(not stray, "every formula name in a lesson is in its module's approved list" + (f": {stray[:3]}" if stray else ""))
ok(kaavat.write_symbols(check=True), "the FY9 texts and figures have MAFY's symbols of docs/fy9/mafy-tunnukset.tsv (kaavat.py symbols --check)")
ok(kaavat.apply_symbols("fy9-energia", "fi", "inquiry.json", '"$\\\\eta = E_\\\\text{a}$"') == '"$\\\\eta = W_\\\\text{a}$"' and kaavat.apply_symbols("fy9-energia", "fi", "unit.md", "$E_\\text{a}$") == "$W_\\text{a}$",
   "a replacement is made as written in a text and as JSON writes it in a .json file")
ok(kaavat.apply_symbols("fy9-tasavirta", None, "figures.py", "$l$ johtimen pituus") == "$l$ johtimen pituus", "figures.py takes only the replacements of every language")
ok(all(old not in new for k in {r["_key"] for r in kaavat.table()} for l in [None, *kaavat.LANGS] for old, new in kaavat.symbol_rows(k, l)),
   "no MAFY replacement keeps its old text inside the new one (kaavat.py symbols can run twice)")
J = "```johda\nJohda virta $I$.\nToinen rivi.\n---\nKirchhoffin 2. laki:\n\n$$E - RI = 0$$\n\nRatkaistaan $I$.\n```"
q, paras = kaavat.johda_parts(J[9:-3])
ok(q == "Johda virta $I$. Toinen rivi." and paras == ["Kirchhoffin 2. laki:", "$$E - RI = 0$$", "Ratkaistaan $I$."], "```johda: the question before ---, the derivation in paragraphs")
h = kaavat.johda_html("A\n\n" + J + "\n\nB", "Johda itse", "Näytä johto")
ok('<div class="johda"><p class="johda-q"><strong>Johda itse.</strong> Johda virta $I$. Toinen rivi.</p>' in h and '<details class="solution johda-sol"><summary>Näytä johto</summary>' in h
   and '<p>Kirchhoffin 2. laki:</p>$$E - RI = 0$$<p>Ratkaistaan $I$.</p>' in h, "```johda HTML: the question in view, the derivation behind a closed button")
derived = [(f.relative_to(kaavat.ROOT).as_posix(), t) for l in kaavat.LANGS for f in sorted((kaavat.ROOT / "content" / l / "units").glob("fy9-*/unit.md"))
           for t in ("U = E - R_\\text{s} I", "I = \\frac{E}{R + R_\\text{s}}") if t in kaavat.JOHDA.sub("", f.read_text(encoding="utf-8"))]
ok(not derived, "FY9: a result derived in a Johda itse task is not given as a formula elsewhere in the text" + (f": {derived[:3]}" if derived else ""))
import reviews
A = "Vanha teksti.\n\n```latex\nQ = s m \\qquad \\text{ja} \\qquad Q = r m\n```\n"
B = "Uusi teksti.\n\n```kaavat\nsulamislämpö :: Q = s m\nhöyrystymislämpö :: Q = r m\n```\n"
ok(reviews._unnamed(A, B, {("sulamislämpö", "Q = s m"), ("höyrystymislämpö", "Q = r m")}) == "Uusi teksti.\n\n```latex\nQ = s m \\qquad \\text{ja} \\qquad Q = r m\n```\n",
   "reviews: approved names put back as the passed block, so the other change (the prose) is classified as usual")
ok(reviews._unnamed(A, B, {("sulamislämpö", "Q = s m")}) is None, "reviews: a name not approved is not put back")
bare = [(f.relative_to(kaavat.ROOT).as_posix(), kaavat.rows(m.group(1))[0][1])
        for l in kaavat.LANGS for f in sorted((kaavat.ROOT / "content" / l).glob("**/*.md"))
        for m in kaavat.FENCE.finditer(f.read_text(encoding="utf-8")) if not any(n for n, _ in kaavat.rows(m.group(1)))]
ok(not bare, "a block with no name is display maths (```latex), never a formula table without names" + (f": {bare[:3]}" if bare else ""))

print(f"\n{len(fails)} failure(s)")
sys.exit(1 if fails else 0)
