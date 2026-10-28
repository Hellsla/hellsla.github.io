"""Mechanical checks for a lesson folder, encoding the rules in CLAUDE.md and NOTES.md.

  python scripts/lint_lesson.py <id>            lint one lesson (folder found under content/fi/)
  python scripts/lint_lesson.py content/fi/FY3/fy3-3
  python scripts/lint_lesson.py --all           every lesson of content/fi/ (content/_gold is the reference, not a lesson)

Prints one line per finding, `ERROR file:line message` or `WARN file:line message`, and exits 1 when
there is at least one ERROR. Run it before any reviewer starts: everything it catches used to cost a review
round. When a new rule lands in NOTES.md, add the check here. The gate runs this too (`lint` check).

It also runs the lesson's `answers.py` when present (`python -I answers.py` prints a JSON object
{exercise id: numeric answer}) and compares every value with exercises/exercises.json within its tolerance, and
checks that `lesson-answers.py` (the numbers of the lesson text and inquiry.json, when there are any) runs.
"""
import json, pathlib, re, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from reviews import status as review_status
import courses, i18n
import check_solutions as solution_rules
import physics_phrases
from courses import ROOT
UNITS = r"(?:N/kg|m/s²|m/s|km/h|kPa/°C|kPa|MPa|Pa|°C|K|N|kg|g|km|cm|mm|m|s|min|h|kJ|J|kW|W|dm³|l|Hz|%)"
NUM = r"[−-]?\d+(?:,\d+)?"


# The figure palette (NOTES.md §3): one meaning per colour in every lesson's figures.
PALETTE = {"#1f2933", "#6b7480", "#c9c2b2", "#e3dccb", "#ffffff", "#eef5f9", "#2f74b5", "#a9d1f0", "#d9b26a", "#e9c98a", "#f1dfb5",
           "#a97a35", "#8a5f22", "#e8590c", "#ffc078", "#c92a2a", "#f2a69c", "#1971c2", "#d0e6fb", "#8a96a3", "#c4ccd4", "#6c757d",
           "#b8622d", "#a5d8ff", "#4f8fbf", "#2b8a3e", "#b2f2bb", "#f6f1e6"}


class Lint:
    def __init__(self, folder):
        self.folder = folder; self.out = []; self.errors = 0; self.form_errors = 0
        try: self.state = review_status(folder)["state"]
        except Exception: self.state = "draft"
        try: self.ex_state = review_status(folder, "exercises")["state"]   # the exercise set is reviewed apart (README "Exercises")
        except Exception: self.ex_state = self.state

    def err(self, f, line, msg): self.errors += 1; self.out.append(f"ERROR {f}:{line} {msg}")
    def form(self, f, line, msg):
        """A human lesson-form rule (CLAUDE.md). An error for one lesson (the developer, the reviewers); in --all,
        legacy lessons written before the rule report it without failing CI until they are reworked."""
        self.form_errors += 1; self.err(f, line, msg)
    def warn(self, f, line, msg): self.out.append(f"WARN  {f}:{line} {msg}")
    def page(self, f, line, msg):
        """A lesson-page rule of 2026-10-26 (CLAUDE.md "Lesson page"). An error for a lesson being written or edited
        (its reviews are not current); a lesson reviewed before the rule reports it as a warning until it is next edited."""
        state = self.ex_state if f.startswith("exercises/") or f == "solutions.md" else self.state
        if state == "draft": self.err(f, line, msg)
        else: self.warn(f, line, msg + " (page rule 2026-10-26: fix when the lesson is next edited)")


def find_lesson(arg):
    p = pathlib.Path(arg)
    if p.is_dir(): return p.resolve()               # absolute, so answers.py is run from the right folder
    return courses.find_lesson(arg)


def sig_figs(s):
    """Significant figures of a Finnish number string: "4,0" -> 2, "77" -> 2, "300" -> 3, "0,20" -> 2."""
    s = s.lstrip("−-")
    digits = s.replace(",", "").lstrip("0")
    return len(digits) if digits else 1


def round_sf(x, n):
    if x == 0: return 0.0
    return float(f"{x:.{n}g}")


def fi_float(s): return float(s.replace("−", "-").replace(",", "."))


def strip_math_and_svg(text):
    """Blank out LaTeX and inline SVG so text rules do not fire inside them (keeps line numbers)."""
    def blank(m): return re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"```latex\n.*?```", blank, text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$", blank, text, flags=re.S)
    text = re.sub(r"\$[^$\n]+?\$", blank, text)
    text = re.sub(r"<svg.*?</svg>", blank, text, flags=re.S)
    return text


def math_fragments(text):
    """(line, LaTeX, display) for every formula. A label inside a figure (foreignObject) counts as display: it sits
    alone in its box, so a full-size \\dfrac there does not break a line of text."""
    text = re.sub(r"```latex\n(.*?)```", lambda m: "$$" + m.group(1) + "$$", text, flags=re.S)
    figs = [(m.start(), m.end()) for m in re.finditer(r"<foreignObject.*?</foreignObject>", text, re.S)]
    for m in re.finditer(r"\$\$(.*?)\$\$|\$([^$\n]+?)\$", text, re.S):
        line = text.count("\n", 0, m.start()) + 1
        yield line, (m.group(1) if m.group(1) is not None else m.group(2)), m.group(1) is not None or any(a <= m.start() < b for a, b in figs)


PLAIN_QTY = re.compile(r"(?<![\w,])\d+(?:[ ,]\d+)*\s?(?:%|(?:[kMGT]?(?:W|J|Wh)|snt|€|kg|g|t|km|m|min|h|s|l|°C|K|ppm)\b)")


def check_plain_quantities(L, name, text):
    """A number with its unit is maths everywhere a student reads (teacher 2026-10-28, "kaikki LaTeXilla"; NOTES 1):
    $80\\,\\text{W}$, $4{,}0\\,\\%$. Only aria-labels (inside SVG) stay plain."""
    plain = strip_math_and_svg(text)
    plain = re.sub(r'aria-label="[^"]*"', "", plain)
    for i, line in enumerate(plain.splitlines(), 1):
        m = PLAIN_QTY.search(line)
        if m: L.page(name, i, f"number with its unit in plain text: \"{m.group(0)}\"; write it as maths (NOTES 1, teacher 2026-10-28)")


def check_text_rules(L, name, text):
    """Rules that apply to every Finnish prose file (lesson.md, solutions.md, sim-spec.md)."""
    plain = strip_math_and_svg(text)
    for i, line in enumerate(plain.splitlines(), 1):
        if re.search(r"\d\.\d", line) and not re.search(r"\b(v\d|\d\.\d\.\d)", line):
            L.err(name, i, "decimal point in Finnish text; use a decimal comma (NOTES 1.4)")
        if re.search(rf"\d{UNITS}(?![a-zA-Z³²/])", line) and re.search(r"\d(N|kg|kPa|Pa|J|W|K)\b", line):
            L.err(name, i, "number glued to its unit; write a space: 40 N (CLAUDE.md conventions)")
        if re.search(r"\b(\d+ (?:N|kg|m|s|J|W|K|°C|Pa|kPa|cm)) (voimalla|matka|matkan|nousu|nousun|lasku|painolla|massalla|paineessa|lämpötilassa)\b", line):
            L.warn(name, i, "inflect the unit (80 N:n voimalla) or use a nominative sentence (NOTES 2, Finnish)")
        if re.search(r"astet?ta?\b[^.\n]{0,40}absoluuttis", line) or re.search(r"\d+ astetta\b[^.\n]{0,20}\bK\b", line):
            L.warn(name, i, "kelvins are not 'asteita'; write 'kelviniä' (fy3-3 lesson rule)")
        if "pitää painoa paikallaan" in line or "painoa paikallaan" in line:
            L.warn(name, i, "'paino' is a force; say 'kappaletta' (NOTES 2, Finnish)")
        if re.search(r"\\\(|\\\[", line):
            L.err(name, i, "\\( \\) and \\[ \\] are not rendered; use $ and $$ (NOTES 1)")


def check_math(L, name, text):
    for line, frag, display in math_fragments(text):
        if re.search(r"(?<![{,])\d,\d", frag):
            L.err(name, line, "decimal comma inside math must be {,} (NOTES 1.4): " + frag[:60])
        if "\\text{l}" in frag:
            L.err(name, line, "\\text{l} looks like the digit 1 in KaTeX; write the litre as \\textsf{l} (NOTES 1)")
        if re.search(r"\\text\{[^}]*·", frag):
            L.err(name, line, "· inside \\text{} breaks KaTeX; write \\text{mol}\\cdot\\text{K} (NOTES 1): " + frag[:60])
        if re.search(r"\\(si|SI|unit)\b|\\newcommand", frag):
            L.err(name, line, "siunitx and \\newcommand do not work in KaTeX (NOTES 1.10)")
        if re.search(r"\\times\b|×|\\div\b|÷", frag):
            L.page(name, line, "multiplication is \\cdot and a written division a colon : (teacher 2026-10-28, NOTES 1): " + frag[:60])
        if re.search(r"(?<!\\)\*", frag):
            L.warn(name, line, "use \\cdot for multiplication, not * (NOTES 1.5)")
        if not display and "\\dfrac" in frag and name != "solutions.md":   # a solution line is a calculation of its own, a full-size fraction reads best there
            L.warn(name, line, "inline \\dfrac breaks the line; use \\tfrac or display math (NOTES 1)")
        if re.search(r"\d\s(?:N|kg|m|s|J|W|K|Pa)\b", frag) and "\\text" not in frag and "\\mathrm" not in frag:
            L.warn(name, line, "units in math go in \\text{} after \\, (NOTES 1.3): " + frag[:60])
    # an odd number of single dollars on a line means an inline formula is unbalanced or spans lines
    for i, line in enumerate(text.splitlines(), 1):
        if line.count("$") % 2 == 1 and "$$" not in line:
            L.err(name, i, "unbalanced $ on this line (inline math must stay on one line, NOTES 1.2)")


def section(text, name):
    """Body of `## name` up to the next `## ` heading, and its first line number."""
    m = re.search(rf"^## {name}[^\n]*\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
    return (m.group(1), text.count("\n", 0, m.start()) + 1) if m else ("", 1)


def first_row_has_numbers(frag):
    """True when the first row of a display calculation already has substituted values, i.e. numbers with units
    (rule: symbols first). Constants such as \\frac{1}{2} or 273,15 in a symbolic formula, and sub- and superscripts
    (T_1, m^3, P_\\text{seinä}), do not count."""
    body = re.sub(r"\\begin\{aligned\}|\\end\{aligned\}", "", frag).strip()
    first = re.split(r"\\\\", body)[0]
    if "=" not in first: return False
    first = re.sub(r"[_^]\\(?:text|mathrm|textsf)\{[^}]*\}|[_^]\{[^}]*\}|[_^]\w", "", first)
    has_digit = re.search(r"\d", first)
    has_unit = re.search(r"\\(?:text|textsf|mathrm)\{|\\%|\{\}\^\\circ", first)
    return bool(has_digit and has_unit)


def check_figures(L, text):
    """Figures as textbook illustrations (CLAUDE.md "Lesson page" 9, NOTES.md §3): text at least 24 px in the 600-unit
    figure, colours from the figure palette, not a monochrome currentColor sketch."""
    for m in re.finditer(r"<svg\b.*?</svg>", text, flags=re.S):
        svg, line = m.group(0), text.count("\n", 0, m.start()) + 1
        sizes = [float(x) for x in re.findall(r"font-size[:=]\s*\"?(\d+(?:\.\d+)?)", svg)]
        if sizes and min(sizes) < 24: L.page("lesson.md", line, f"figure text at {min(sizes):g} px; use 24 px or more so it reads at 13 px on a 360 px phone (NOTES 3)")
        for t in re.finditer(r"<text\b[^>]*>(.*?)</text>", svg, flags=re.S):
            L.page("lesson.md", line + svg.count("\n", 0, t.start()), f"figure label in <text>: every label in a figure is LaTeX in a fig-tex foreignObject, words as \\text{{}} (teacher's rule 2026-10-26, NOTES 3): {re.sub(r'<[^>]+>', '', t.group(1)).strip()[:40]}")
        colours = {c.lower() for c in re.findall(r"#[0-9a-fA-F]{6}\b", svg)}
        if not colours: L.page("lesson.md", line, "monochrome figure (currentColor only): draw it as a textbook illustration with the figure palette, materials you can recognise and colour that carries meaning (NOTES 3)")
        elif colours - PALETTE: L.warn("lesson.md", line, f"colours outside the figure palette: {', '.join(sorted(colours - PALETTE))} (NOTES 3)")


def check_lesson_form(L, text):
    """Human decisions on lesson form (CLAUDE.md, NOTES.md section 4)."""
    for name in ("Ydinajatus", "Kaava"):
        body, line = section(text, name)
        if body and "<svg" not in body:
            L.form("lesson.md", line, f"no figure in ## {name}: every lesson has an inline SVG in Ydinajatus and in Kaava (CLAUDE.md, human rule 1)")
    for m in re.finditer(r"(?:^|\n\n)([^\n<`#|>-][^\n]+)", text):
        words = len(m.group(1).split())
        if words > 130:
            L.warn("lesson.md", text.count("\n", 0, m.start(1)) + 1, f"paragraph of {words} words; keep paragraphs under about 120 words and add a figure or a list (human rule 1)")
    for m in re.finditer(r"^## (Ydinajatus|Yleinen virhekäsitys)[^\n]*\n(.*?)(?=^## |\Z)", text, flags=re.S | re.M):
        prose = re.sub(r"<svg\b.*?</svg>|\$\$.*?\$\$|```.*?```", "", m.group(2), flags=re.S)
        words, paras = len(prose.split()), len([p for p in re.split(r"\n\s*\n", prose) if p.strip() and not p.lstrip().startswith(("<", "|", "#"))])
        if words > 320 and "\n### " not in m.group(2):
            L.warn("lesson.md", text.count("\n", 0, m.start()) + 1, f"## {m.group(1)}: {words} words in {paras} paragraphs without a ### subheading; give each main idea a short subheading that names it (NOTES 8, teacher 2026-10-27)")
    body, line = section(text, "Esimerkki")
    if body:
        stages = body.count("<!-- vaihe -->")
        if not 3 <= stages <= 7:
            L.form("lesson.md", line, f"worked example has {stages} stages; write the 7 stages of check_solutions.py separated by `<!-- vaihe -->` lines (human rule 4)")
        start = text.find(body)
        for m in re.finditer(r"```latex\n(.*?)```|\$\$(.*?)\$\$", body, flags=re.S):
            frag = m.group(1) or m.group(2)
            if first_row_has_numbers(frag):
                L.form("lesson.md", text.count("\n", 0, start + m.start()) + 1,
                      "worked example substitutes before solving: the first row of a calculation must be the formula solved for the unknown in symbols, numbers with units come on the next row (human rule 2): " + frag.strip()[:60])



def check_lesson_md(L, folder):
    f = folder / "lesson.md"
    if not f.exists(): L.err("lesson.md", 1, "missing"); return
    text = f.read_text()
    if not re.search(r"^> \*\*Miksi\*\*", text, re.M):
        L.warn("lesson.md", 3, "no motivating question (`> **Miksi** ...`) like the gold lesson")
    for h in ("Ydinajatus", "Kaava", "Esimerkki", "Yleinen virhekäsitys", "Tiivistelmä"):
        if not re.search(rf"^## {h}", text, re.M): L.warn("lesson.md", 1, f"no '## {h}' section (gold structure)")
    if "$$" not in text and "```latex" not in text:
        L.warn("lesson.md", 1, "no display formula; every formula appears once in display LaTeX (CLAUDE.md)")
    check_text_rules(L, "lesson.md", text)
    check_plain_quantities(L, "lesson.md", text)
    for jf in ("inquiry.json", "exit-ticket.json", "exercises/exercises.json"):
        f = courses.lesson_file(folder, jf) if "/" not in jf else folder / jf
        if f.exists(): check_plain_quantities(L, jf, f.read_text())
    check_math(L, "lesson.md", text)
    check_lesson_form(L, text)
    check_figures(L, text)
    m = re.search(r"^## Kaava\s*$", text, re.M)
    if m: L.page("lesson.md", text.count("\n", 0, m.start()) + 1, "name the formula section after its law, `## Kaava: Lämpömäärä` (the page shows the name; inquiry.json keeps \"Kaava\")")
    for m in re.finditer(r"lähtölip|herätä kiinnostus", text, re.I):
        L.err("lesson.md", text.count("\n", 0, m.start()) + 1, f"\"{m.group(0)}\": the page says Exit ticket and Pohdinta (2026-10-26)")
    for m in re.finditer(r"\|[^\n]*\|", text):
        cells = [c.strip() for c in m.group(0).strip("|").split("|")]
        if any(len(c) > 22 for c in cells) and m.group(0).count("|") > 2 and "---" not in m.group(0):
            L.warn("lesson.md", text.count("\n", 0, m.start()) + 1, "long table cell; wide tables scroll on a phone, keep header cells short (NOTES 1)")
            break


def numbers_with_units(text):
    """Finnish numbers that carry a unit in a task text, e.g. '4,0 kg', '77 K', '−173 °C'."""
    plain = [m.group(1) for m in re.finditer(rf"({NUM})\s?{UNITS}(?![a-zA-Zäö])", text)]
    # coefficients written as "9,0 · 10⁻⁶ 1/K": the mantissa carries the significant figures
    coeff = [m.group(1) for m in re.finditer(rf"({NUM})\s?·\s?10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+\s?(?:1/K|{UNITS})", text)]
    return plain + coeff


def check_exercises(L, folder):
    f = courses.lesson_file(folder, "exercises.json")
    if not f.exists(): L.err("exercises.json", 1, "missing"); return {}
    try: ex = json.loads(f.read_text())
    except json.JSONDecodeError as e: L.err("exercises.json", e.lineno, f"invalid JSON: {e.msg}"); return {}
    raw = f.read_text()
    lid = folder.name
    want = courses.course(courses.course_of(lid))["exercise_levels"]   # 5/4/3 unless the course config says otherwise
    answers = {}
    for lvl, n in want.items():
        items = ex.get(lvl, [])
        if len(items) != n: L.err("exercises.json", 1, f"{lvl} has {len(items)} tasks, expected {n} (CLAUDE.md exercise levels, curriculum.json exercise_levels)")
        for e in items:
            eid = e.get("id", "?")
            line = raw.count("\n", 0, raw.find(f'"{eid}"')) + 1 if eid in raw else 1
            for k in ("id", "level", "text", "answer", "unit", "tolerance"):
                if k not in e: L.err("exercises.json", line, f"{eid}: missing {k}")
            if not str(eid).startswith(f"{lid}-L{lvl[-1]}-"): L.err("exercises.json", line, f"id {eid} does not match {lid}-L{lvl[-1]}-NN")
            if e.get("level") != int(lvl[-1]): L.err("exercises.json", line, f"{eid}: level field is {e.get('level')}, in {lvl}")
            tol = e.get("tolerance")
            if not isinstance(tol, (int, float)) or tol <= 0: L.err("exercises.json", line, f"{eid}: tolerance must be a positive number")
            text = e.get("text", "")
            if re.search(r"\d\.\d", re.sub(r"\$[^$]*\$", "", text)): L.err("exercises.json", line, f"{eid}: decimal point in task text; use a comma")
            ans = e.get("answer")
            if isinstance(ans, str) and re.fullmatch(r"[−-]?\d+,\d+", ans.strip()):
                L.err("exercises.json", line, f"{eid}: numeric answer written as a string with a comma; JSON uses a number with a decimal point")
            if isinstance(ans, (int, float)) and isinstance(tol, (int, float)) and tol > 0:
                answers[eid] = (ans, tol)
                data = [d for d in numbers_with_units(text) if fi_float(d) != 0]   # 0 °C is a reference point, not a datum
                if data:
                    sf = min(sig_figs(d) for d in data)
                    if sf <= 1:
                        L.warn("exercises.json", line, f"{eid}: a datum has 1 significant figure ({[d for d in data if sig_figs(d) <= 1]}); write 4,0 instead of 4 so the answer can have 2 sf")
                    else:
                        r = round_sf(ans, sf)
                        if ans != 0 and abs(r - ans) > tol * abs(ans):
                            need = abs(r - ans) / abs(ans)
                            L.err("exercises.json", line,
                                  f"{eid}: data has {sf} significant figures, a student rounding to {sf} sf answers {r:g}, which is {need:.1%} from {ans:g} (tolerance {tol:g}); raise tolerance to at least {need + 0.005:.2f} or ask for a whole number (NOTES 2, numbers)")
                        if sig_figs(str(ans).replace(".", ",").rstrip("0").rstrip(",") or "0") > sf + 1 and not float(ans).is_integer():
                            L.warn("exercises.json", line, f"{eid}: answer {ans:g} has more significant figures than the data ({sf} sf)")
    return answers


def latex_plain(s):
    """A LaTeX answer as the plain number it shows: $-3{,}50\\,\\text{kJ}$ -> −3,50 kJ."""
    s = s.replace("$", "").replace("{,}", ",").replace("\\,", " ").replace("\\ ", " ").replace("\\approx", "")
    return re.sub(r"(?<=\*\*)(:?\s*)-", r"\1−", s)


def check_solutions(L, folder, answers):
    f = courses.lesson_file(folder, "solutions.md")
    if not f.exists(): L.err("solutions.md", 1, "missing"); return
    text = f.read_text()
    check_text_rules(L, "solutions.md", text)
    check_plain_quantities(L, "solutions.md", text)
    check_math(L, "solutions.md", text)
    blocks = re.split(r"^## ", text, flags=re.M)[1:]
    seen = {}
    for b in blocks:
        head, _, body = b.partition("\n")
        eid = head.strip()
        start = text.find(f"## {eid}")
        line = text.count("\n", 0, start) + 1
        seen[eid] = body
        for lab in ("Kaava", "Sijoitus"):
            k = re.search(rf"\*\*{lab}:?\*\*:?(.*?)(?=\n\*\*|\Z)", body, re.S)   # the step runs to the next label: a display $$ block on the next line counts
            if k and "$" not in k.group(1):
                L.page("solutions.md", line, f"{eid}: the {lab} step is plain text; write the calculation in LaTeX, $p = \\dfrac{{F}}{{A}}$ (teacher's rule 2026-10-26, NOTES 1)")
        body = tex_plain(body)
        k = re.search(r"\*\*Kaava:?\*\*:?([^\n]*)", body)
        if k and "=" not in k.group(1):
            L.form("solutions.md", line, f"{eid}: the Kaava step must end with the formula solved for the unknown in symbols (human rule 2)")
        elif k and re.search(r"=[^=]*\d[,.]?\d*\s?(?:" + UNITS[3:-1] + r")\b", k.group(1).split(",")[-1]) and "Sijoitus" in body:
            L.warn("solutions.md", line, f"{eid}: numbers with units in the Kaava step; keep Kaava symbolic and put the numbers in Sijoitus (human rule 2)")
        words = len(body.split())
        if words > 260: L.warn("solutions.md", line, f"{eid}: {words} words; a complete solution is about 100–220 words, put long reasoning in Periaate and Järkevyys, not in Sijoitus")
        m = re.search(r"\*\*Vastaus:?\*\*:?\s*([−-]?\d[\d\s]*(?:,\d+)?)", latex_plain(body))
        if m and eid in answers:
            ans, tol = answers[eid]
            try: got = fi_float(m.group(1).replace(" ", ""))
            except ValueError: continue
            if abs(got - ans) > max(tol, 0.005) * max(1, abs(ans)):
                L.err("solutions.md", line, f"{eid}: Vastaus {m.group(1).strip()} does not match exercises.json answer {ans:g}")


def tex_plain(text):
    """A solution in LaTeX read as the plain text the older checks expect: '$930\\,\\text{kPa}$' -> '930 kPa'."""
    def one(m):
        t = m.group(1) if m.group(1) is not None else m.group(2)
        t = re.sub(r"\\(?:text|mathrm|textsf)\{([^{}]*)\}", r"\1", t)
        t = t.replace("{,}", ",").replace("\\,", " ").replace("\\;", " ").replace("\\ ", " ").replace("\\cdot", "·").replace("\\approx", "≈")
        t = re.sub(r"\\[a-zA-Z]+", " ", t)
        return re.sub(r"[{}]", "", t)
    return re.sub(r"\$\$(.*?)\$\$|\$([^$\n]+?)\$", one, text, flags=re.S)


CHAPTER_REF = re.compile(r"\b[Ff][Yy]\d-\d+\b(?![-\w])|\b[Oo]ppitunni(?:lla|n|sta|ssa|lta)\s+[Ff][Yy]\d|\b[Ee]dellise(?:llä|n|ssä|ltä)\s+oppitun\w*|\bedellinen oppitunti\b")


def check_chapter_refs(L, name, text):
    """A student sees chapter names, never lesson ids (teacher's rule 2026-10-26): 'luvussa Paine ja hydrostaattinen
    paine', not 'oppitunnilla fy3-4' or '(fy3-4)' or 'edellisellä oppitunnilla'. Exercise ids ("id": "fy3-4-L1-01")
    and solution headings are not shown as text and are skipped, and so is a figure id ("figure": "fy3-4/pressure-depth")."""
    for i, ln in enumerate(text.splitlines(), 1):
        if re.match(r"\s*(\"id\"|\"figure\"|## fy)", ln): continue
        for m in CHAPTER_REF.finditer(ln):
            L.page(name, i, f"\"{m.group(0)}\": name the chapter, not the lesson id or 'the previous lesson' (teacher's rule 2026-10-26)")


def check_exit_ticket(L, folder):
    f = folder / "exit-ticket.json"
    if not f.exists(): L.err("exit-ticket.json", 1, "missing"); return
    try: q = json.loads(f.read_text())
    except json.JSONDecodeError as e: L.err("exit-ticket.json", e.lineno, f"invalid JSON: {e.msg}"); return
    if not 1 <= len(q) <= 3: L.err("exit-ticket.json", 1, f"{len(q)} questions, expected 1–3 that the checks and exercises do not already ask (NOTES §11)")
    for i, item in enumerate(q, 1):
        if not item.get("q") or not item.get("a"): L.err("exit-ticket.json", 1, f"question {i} needs q and a")
        if re.search(r"\d\.\d", re.sub(r"\$[^$]*\$", "", item.get("q", "") + item.get("a", ""))): L.err("exit-ticket.json", 1, f"question {i}: decimal point; use a comma")


def check_meta(L, folder):
    f = folder / "meta.json"
    meta = json.loads(f.read_text())
    lid = folder.name
    for k in ("id", "course", "title", "goals", "prerequisites", "glossary", "sim"):
        if k not in meta: L.err("meta.json", 1, f"missing {k}")
    if meta.get("id") != lid: L.err("meta.json", 1, f"id {meta.get('id')!r} does not match folder {lid!r}")
    code = courses.course_of(lid)
    if meta.get("course") != folder.parent.name or folder.parent.name != code:
        L.err("meta.json", 1, f"course {meta.get('course')!r}, folder content/{courses.lang_of(folder)}/{folder.parent.name}/ and id prefix ({code}) must agree")
    glossary = {e["term"] for e in json.loads((ROOT / "glossary.json").read_text())}
    for term in meta.get("glossary", []):
        if term not in glossary: L.err("meta.json", 1, f"glossary term {term!r} missing from glossary.json (add it, do not invent synonyms)")
    cur = courses.curriculum()
    ids = {l["id"] for k, v in cur.items() if not k.startswith("_") for l in v.get("lessons", [])}
    if lid not in ids: L.warn("meta.json", 1, f"{lid} is not a slot in curriculum.json")
    for p in meta.get("prerequisites", []):
        if p not in ids: L.err("meta.json", 1, f"prerequisite {p!r} is not in curriculum.json")
    return meta


def check_sim(L, folder, meta):
    c = courses.course(courses.course_of(folder.name)); d = courses.sim_dir(folder, meta)
    if d is None: return
    kind, where, _ = d
    if kind == "lesson" and not c.get("lesson_folder_sims"):
        L.err("sim.js", 1, f"a {c['code']} simulation lives in its own folder, {(c['paths']['sims'] / folder.name).relative_to(ROOT)}/ (sim.js, sim.css, images), not in the lesson folder")
    sim = where / "sim.js"
    if not sim.exists(): L.err("sim.js", 1, f"meta.sim is {meta.get('sim')!r} but {sim.relative_to(ROOT)} is missing"); return
    js = i18n.resolved_sim(sim)                         # its labels and readouts from lang/fi.json in place
    if "window.simState" not in js: L.err("sim.js", 1, "sim must expose window.simState every frame (tester asserts on it)")
    if not re.search(r"createCanvas\(\s*600\s*,\s*400", js): L.warn("sim.js", 1, "canvas is not 600×400 (the embed scales that size)")
    if ".class('readout')" not in js and 'class("readout")' not in js and "readout" not in js:
        L.warn("sim.js", 1, "no DOM readout (.readout); numbers in the canvas are hard to read on a phone (NOTES 2)")
    if re.search(r"\bfetch\(|XMLHttpRequest|https?://", js): L.err("sim.js", 1, "no network requests from a simulation")
    if not courses.lesson_file(folder, "sim-spec.md").exists(): L.err("sim-spec.md", 1, "a lesson with sim.js needs sim-spec.md")
    t = ROOT / "tests" / "sims" / f"{folder.name}.json"
    if not t.exists(): L.err("tests/sims", 1, f"no tests/sims/{folder.name}.json; the developer writes it with the simulation")
    else:
        try: n = len(json.loads(t.read_text()))
        except json.JSONDecodeError as e: L.err(f"tests/sims/{folder.name}.json", e.lineno, "invalid JSON"); return
        if n < 3: L.err(f"tests/sims/{folder.name}.json", 1, f"only {n} assertions, at least 3 covering the spec")
    check_text_rules(L, "sim-spec.md", courses.lesson_file(folder, "sim-spec.md").read_text()) if courses.lesson_file(folder, "sim-spec.md").exists() else None
    sim_rule = L.page if sim_edited(folder) else L.warn   # an old sim's notes are folded by sim-embed.js until the sim itself is edited
    for m in re.finditer(r"\bp\.text\(\s*(['\"`])((?:(?!\1)[^\\]|\\.)*)\1", js):   # a literal canvas label: LaTeX (teacher 2026-10-26)
        if "$" not in m.group(2) and m.group(2).strip():
            sim_rule("sim.js", js.count("\n", 0, m.start()) + 1, f"canvas label '{m.group(2)[:30]}' is plain text; draw it as LaTeX, p.text('$\\text{{…}}$', x, y) (NOTES 1, sim-embed.js)")
    for m in re.finditer(r"\.html\(\s*(['\"`])((?:(?!\1)[^\\]|\\.)*)\1", js):   # a readout with a formula outside maths
        plain = re.sub(r"\$[^$]*\$", "", re.sub(r"\$\{[^}]*\}", "1", m.group(2)))   # template values first, then the maths
        if re.search(r"(?<![<!-])=(?![^<]*>)|\b\d+(?:,\d+)?\s?(?:N|J|W|K|kg|g|m|s|Pa|kPa|ml|°C|%)(?![\w])", plain):
            sim_rule("sim.js", js.count("\n", 0, m.start()) + 1, f"readout '{m.group(2)[:40]}' has a formula or a value with a unit outside $…$ (NOTES 1)")
    if "'Lisätietoja'" in js or '"Lisätietoja"' in js:
        sim_rule("sim.js", 1, "a Lisätietoja box in the sim: explanations go in the lesson's inquiry.json sim activity as howto, model and calc (Käyttöohje, Mallin oletukset, Laskennan selitys)")
    for m in re.finditer(r"createP\(((?:[^()]|\([^()]*\))*)\)", js):
        words = len(" ".join(re.findall(r"(['\"`])((?:(?!\1).)*)\1", m.group(1)) and [x[1] for x in re.findall(r"(['\"`])((?:(?!\1).)*)\1", m.group(1))]).split())
        if words > 15: sim_rule("sim.js", js.count("\n", 0, m.start()) + 1, f"a {words}-word paragraph in the sim: the sim shows the picture, the controls and the values; one legend line of at most 15 words, the rest in inquiry.json howto/model/calc")


def sim_edited(folder):
    """True when the lesson's simulation is new or its code changed since the science reviewer's last PASS."""
    try:
        from reviews import scope
        sc = scope(folder)["science"]
    except Exception: return True
    return sc["base"] is None and sc["why"] != "0 changed wording line(s): the version it passed" or "simulation" in sc["categories"]


def check_answers_py(L, folder, answers):
    f = courses.lesson_file(folder, "answers.py")
    if not f.exists():
        L.warn("answers.py", 1, "no answers.py; the exercise author saves the Python that computed the answers so the gate can re-run it")
        return
    r = subprocess.run([sys.executable, "-I", str(f)], capture_output=True, text=True, cwd=f.parent, timeout=60)
    if r.returncode != 0: L.err("answers.py", 1, "failed: " + (r.stderr.strip().splitlines() or ["?"])[-1]); return
    try: got = json.loads(r.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError): L.err("answers.py", 1, "must print a JSON object {exercise id: number} as its last line"); return
    for eid, (ans, tol) in answers.items():
        if eid not in got: L.err("answers.py", 1, f"no value for {eid}"); continue
        v = got[eid]
        if not isinstance(v, (int, float)): L.err("answers.py", 1, f"{eid}: value {v!r} is not a number"); continue
        if abs(v - ans) > tol * max(1e-9, abs(ans)):
            L.err("answers.py", 1, f"{eid}: computes {v:g} but exercises.json says {ans:g} (tolerance {tol:g})")
    f = courses.lesson_file(folder, "lesson-answers.py")   # the lesson's and the inquiry's own numbers, when it has any
    if f.exists():
        r = subprocess.run([sys.executable, "-I", str(f)], capture_output=True, text=True, cwd=f.parent, timeout=60)
        try: ok = r.returncode == 0 and isinstance(json.loads(r.stdout.strip().splitlines()[-1]), dict)
        except (json.JSONDecodeError, IndexError): ok = False
        if not ok: L.err("lesson-answers.py", 1, "must run and print a JSON object {id: number} as its last line: " + ((r.stderr.strip().splitlines() or ["?"])[-1]))
        elif set(json.loads(r.stdout.strip().splitlines()[-1])) & set(answers):
            L.err("lesson-answers.py", 1, "an exercise id: the exercises' answers belong in answers.py, the exercise set's own file (README \"Exercises\")")


def check_pictures(L, folder):
    """Pictures the text refers to exist under assets/ and belong to the lesson's course or to the shared folder."""
    slug = courses.course(courses.course_of(folder.name))["slug"]
    for ref in courses.pic_refs(folder):
        if not courses.pic_source(ref).is_file(): L.err("lesson", 1, f"picture {ref} not found: put it in assets/{ref}")
        elif not (ref.startswith(f"pics/{slug}/") or ref.startswith("shared/pics/")):
            L.err("lesson", 1, f"picture {ref} belongs to another course; use assets/pics/{slug}/ or, when it is genuinely shared, assets/shared/pics/")


def lint(folder):
    L = Lint(folder)
    meta = check_meta(L, folder)
    check_pictures(L, folder)
    check_lesson_md(L, folder)
    answers = check_exercises(L, folder)
    check_solutions(L, folder, answers)
    for name, line, msg in solution_rules.problems(folder): L.err(name, line, msg + " (complete solutions, teacher 2026-10-27, scripts/check_solutions.py)")
    check_exit_ticket(L, folder)
    check_sim(L, folder, meta)
    check_answers_py(L, folder, answers)
    check_inquiry(L, folder)
    for f in ("lesson.md", "solutions.md", "inquiry.json", "exercises.json", "exit-ticket.json"):
        if courses.lesson_file(folder, f).exists(): check_chapter_refs(L, f, courses.lesson_file(folder, f).read_text())
    check_figure_refs(L, folder)
    for f, line, rid, msg, s in physics_phrases.problems(folder):   # review warnings, docs/physics-guardrails.md
        L.warn(f, line, f"physics [{rid}]: {msg} (docs/physics-guardrails.md): «{s[:90]}»")
    return L


def check_figure_refs(L, folder):
    """"figure": "<id>" in a task names a figure that some figures.py draws (scripts/figcat.py, NOTES §11)."""
    import figcat
    for f in ("inquiry.json", "exercises.json", "exit-ticket.json"):
        p = courses.lesson_file(folder, f)
        if not p.exists(): continue
        text = p.read_text()
        for fid, msg in figcat.check_refs(text):
            L.err(f, text.count("\n", 0, max(text.find(f'"{fid}"'), 0)) + 1, msg)


def check_inquiry(L, folder):
    """inquiry.json (docs/inquiry.md): every error names the field; build.py refuses the lesson on any."""
    if not (folder / "inquiry.json").exists(): return
    import inquiry
    try: data = inquiry.load(folder)
    except ValueError as e: L.err("inquiry.json", 1, f"not valid JSON: {e}"); return
    for msg in inquiry.validate(folder, data, (folder / "lesson.md").read_text() if (folder / "lesson.md").exists() else ""):
        L.err("inquiry.json", 1, msg.split("inquiry.json: ", 1)[-1])
    for a in data.get("activities", []) if isinstance(data, dict) else []:
        if isinstance(a, dict) and a.get("type") == "sim" and len((a.get("text") or "").split()) > inquiry.LEAD_WORDS:
            L.page("inquiry.json", 1, f"the sim activity's text is {len(a['text'].split())} words; keep a lead of at most {inquiry.LEAD_WORDS} words and move the rest to howto, model and calc (Käyttöohje, Mallin oletukset, Laskennan selitys)")
    blob = json.dumps(data, ensure_ascii=False)
    for m in re.finditer(r"lähtölip|herätä kiinnostus", blob, re.I):
        L.err("inquiry.json", 1, f"\"{m.group(0)}\": the page says Exit ticket and Pohdinta (2026-10-26)")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    folders = courses.lessons() if args[0] == "--all" else [find_lesson(args[0])]
    bad = 0
    for folder in folders:
        L = lint(folder)
        rel = folder.relative_to(ROOT) if folder.is_relative_to(ROOT) else folder
        state = review_status(folder)["state"]
        note = " (draft: errors do not fail --all, the developer fixes them before review)" if args[0] == "--all" and state == "draft" and L.errors else ""
        print(f"== {rel}: {L.errors} error(s), {len(L.out) - L.errors} warning(s){note}")
        for line in L.out: print("  " + line)
        if args[0] == "--all" and state == "legacy" and L.form_errors:
            print(f"  ({L.form_errors} lesson-form finding(s) in a legacy lesson: they do not fail --all until it is reworked)")
            bad += L.errors - L.form_errors
        elif not (args[0] == "--all" and state == "draft"): bad += L.errors
    sys.exit(1 if bad else 0)
