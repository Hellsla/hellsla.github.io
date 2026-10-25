"""Mechanical checks for a lesson folder, encoding the rules in CLAUDE.md and NOTES.md.

  python scripts/lint_lesson.py <id>            lint one lesson (folder found under content/)
  python scripts/lint_lesson.py content/FY3/fy3-3
  python scripts/lint_lesson.py --all           every lesson except content/_gold

Prints one line per finding, `ERROR file:line message` or `WARN file:line message`, and exits 1 when
there is at least one ERROR. Run it before any reviewer starts: everything it catches used to cost a review
round. When a new rule lands in NOTES.md, add the check here. The gate runs this too (`lint` check).

It also runs the lesson's `answers.py` when present (`python -I answers.py` prints a JSON object
{exercise id: numeric answer}) and compares every value with exercises.json within its tolerance.
"""
import json, pathlib, re, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); from reviews import status as review_status
ROOT = pathlib.Path(__file__).resolve().parents[1]
UNITS = r"(?:N/kg|m/s²|m/s|km/h|kPa/°C|kPa|MPa|Pa|°C|K|N|kg|g|km|cm|mm|m|s|min|h|kJ|J|kW|W|dm³|l|Hz|%)"
NUM = r"[−-]?\d+(?:,\d+)?"
LABELS = ["Annettu", "Kysytty", "Kaava", "Sijoitus", "Vastaus", "Järkevyys"]


class Lint:
    def __init__(self, folder):
        self.folder = folder; self.out = []; self.errors = 0; self.form_errors = 0

    def err(self, f, line, msg): self.errors += 1; self.out.append(f"ERROR {f}:{line} {msg}")
    def form(self, f, line, msg):
        """A human lesson-form rule (CLAUDE.md). An error for one lesson (the developer, the reviewers); in --all,
        legacy lessons written before the rule report it without failing CI until they are reworked."""
        self.form_errors += 1; self.err(f, line, msg)
    def warn(self, f, line, msg): self.out.append(f"WARN  {f}:{line} {msg}")


def find_lesson(arg):
    p = pathlib.Path(arg)
    if p.is_dir(): return p.resolve()               # absolute, so answers.py is run from the right folder
    for f in sorted((ROOT / "content").glob(f"*/{arg}")):
        if f.parent.name != "_gold" and (f / "meta.json").exists(): return f
    sys.exit(f"no lesson folder for {arg!r}")


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
    text = re.sub(r"```latex\n(.*?)```", lambda m: "$$" + m.group(1) + "$$", text, flags=re.S)
    for m in re.finditer(r"\$\$(.*?)\$\$|\$([^$\n]+?)\$", text, re.S):
        line = text.count("\n", 0, m.start()) + 1
        yield line, (m.group(1) if m.group(1) is not None else m.group(2)), m.group(1) is not None


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
        if re.search(r"(?<!\\)\*", frag):
            L.warn(name, line, "use \\cdot for multiplication, not * (NOTES 1.5)")
        if not display and "\\dfrac" in frag:
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
    body, line = section(text, "Esimerkki")
    if body:
        stages = body.count("<!-- vaihe -->")
        if not 3 <= stages <= 6:
            L.form("lesson.md", line, f"worked example has {stages} stages; write 3–6 stages separated by `<!-- vaihe -->` lines (human rule 4)")
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
    check_math(L, "lesson.md", text)
    check_lesson_form(L, text)
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
    f = folder / "exercises.json"
    if not f.exists(): L.err("exercises.json", 1, "missing"); return {}
    try: ex = json.loads(f.read_text())
    except json.JSONDecodeError as e: L.err("exercises.json", e.lineno, f"invalid JSON: {e.msg}"); return {}
    raw = f.read_text()
    lid = folder.name
    want = {"level1": 5, "level2": 4, "level3": 3}
    answers = {}
    for lvl, n in want.items():
        items = ex.get(lvl, [])
        if len(items) != n: L.err("exercises.json", 1, f"{lvl} has {len(items)} tasks, expected {n} (CLAUDE.md exercise levels)")
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


def check_solutions(L, folder, answers):
    f = folder / "solutions.md"
    if not f.exists(): L.err("solutions.md", 1, "missing"); return
    text = f.read_text()
    check_text_rules(L, "solutions.md", text)
    if "$" in text: L.warn("solutions.md", 1, "solutions are plain text with Unicode, not LaTeX (NOTES 1)")
    blocks = re.split(r"^## ", text, flags=re.M)[1:]
    seen = {}
    for b in blocks:
        head, _, body = b.partition("\n")
        eid = head.strip()
        start = text.find(f"## {eid}")
        line = text.count("\n", 0, start) + 1
        seen[eid] = body
        for lab in LABELS:
            if f"**{lab}" not in body: L.warn("solutions.md", line, f"{eid}: no '**{lab}:**' step")
        k = re.search(r"\*\*Kaava:?\*\*:?([^\n]*)", body)
        if k and "=" not in k.group(1):
            L.form("solutions.md", line, f"{eid}: the Kaava step must end with the formula solved for the unknown in symbols (human rule 2)")
        elif k and re.search(r"=[^=]*\d[,.]?\d*\s?(?:" + UNITS[3:-1] + r")\b", k.group(1).split(",")[-1]) and "Sijoitus" in body:
            L.warn("solutions.md", line, f"{eid}: numbers with units in the Kaava step; keep Kaava symbolic and put the numbers in Sijoitus (human rule 2)")
        words = len(body.split())
        if words > 130: L.warn("solutions.md", line, f"{eid}: {words} words, solutions stay under 120 words")
        m = re.search(r"\*\*Vastaus:?\*\*:?\s*([−-]?\d[\d\s]*(?:,\d+)?)", body)
        if m and eid in answers:
            ans, tol = answers[eid]
            try: got = fi_float(m.group(1).replace(" ", ""))
            except ValueError: continue
            if abs(got - ans) > max(tol, 0.005) * max(1, abs(ans)):
                L.err("solutions.md", line, f"{eid}: Vastaus {m.group(1).strip()} does not match exercises.json answer {ans:g}")
    for eid in answers:
        if eid not in seen: L.err("solutions.md", 1, f"no solution for {eid}")


def check_exit_ticket(L, folder):
    f = folder / "exit-ticket.json"
    if not f.exists(): L.err("exit-ticket.json", 1, "missing"); return
    try: q = json.loads(f.read_text())
    except json.JSONDecodeError as e: L.err("exit-ticket.json", e.lineno, f"invalid JSON: {e.msg}"); return
    if len(q) != 3: L.err("exit-ticket.json", 1, f"{len(q)} questions, expected 3")
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
    if meta.get("course") != folder.parent.name: L.err("meta.json", 1, "course does not match the folder")
    if meta.get("solutions", "first") not in ("first", "all", "none"): L.err("meta.json", 1, "solutions must be first, all or none")
    glossary = {e["term"] for e in json.loads((ROOT / "glossary.json").read_text())}
    for term in meta.get("glossary", []):
        if term not in glossary: L.err("meta.json", 1, f"glossary term {term!r} missing from glossary.json (add it, do not invent synonyms)")
    cur = json.loads((ROOT / "curriculum.json").read_text())
    ids = {l["id"] for k, v in cur.items() if not k.startswith("_") for l in v.get("lessons", [])}
    if lid not in ids: L.warn("meta.json", 1, f"{lid} is not a slot in curriculum.json")
    for p in meta.get("prerequisites", []):
        if p not in ids: L.err("meta.json", 1, f"prerequisite {p!r} is not in curriculum.json")
    return meta


def check_sim(L, folder, meta):
    sim = folder / "sim.js"
    if meta.get("sim") and not sim.exists(): L.err("sim.js", 1, "meta.sim is true but sim.js is missing")
    if not sim.exists(): return
    js = sim.read_text()
    if "window.simState" not in js: L.err("sim.js", 1, "sim must expose window.simState every frame (tester asserts on it)")
    if not re.search(r"createCanvas\(\s*600\s*,\s*400", js): L.warn("sim.js", 1, "canvas is not 600×400 (the embed scales that size)")
    if ".class('readout')" not in js and 'class("readout")' not in js and "readout" not in js:
        L.warn("sim.js", 1, "no DOM readout (.readout); numbers in the canvas are hard to read on a phone (NOTES 2)")
    if re.search(r"\bfetch\(|XMLHttpRequest|https?://", js): L.err("sim.js", 1, "no network requests from a simulation")
    if not (folder / "sim-spec.md").exists(): L.err("sim-spec.md", 1, "a lesson with sim.js needs sim-spec.md")
    t = ROOT / "tests" / "sims" / f"{folder.name}.json"
    if not t.exists(): L.err("tests/sims", 1, f"no tests/sims/{folder.name}.json; the graphics agent writes it with sim.js")
    else:
        try: n = len(json.loads(t.read_text()))
        except json.JSONDecodeError as e: L.err(f"tests/sims/{folder.name}.json", e.lineno, "invalid JSON"); return
        if n < 3: L.err(f"tests/sims/{folder.name}.json", 1, f"only {n} assertions, at least 3 covering the spec")
    check_text_rules(L, "sim-spec.md", (folder / "sim-spec.md").read_text()) if (folder / "sim-spec.md").exists() else None


def check_answers_py(L, folder, answers):
    f = folder / "answers.py"
    if not f.exists():
        L.warn("answers.py", 1, "no answers.py; the exercise author saves the Python that computed the answers so the gate can re-run it")
        return
    r = subprocess.run([sys.executable, "-I", str(f)], capture_output=True, text=True, cwd=folder, timeout=60)
    if r.returncode != 0: L.err("answers.py", 1, "failed: " + (r.stderr.strip().splitlines() or ["?"])[-1]); return
    try: got = json.loads(r.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError): L.err("answers.py", 1, "must print a JSON object {exercise id: number} as its last line"); return
    for eid, (ans, tol) in answers.items():
        if eid not in got: L.err("answers.py", 1, f"no value for {eid}"); continue
        v = got[eid]
        if not isinstance(v, (int, float)): L.err("answers.py", 1, f"{eid}: value {v!r} is not a number"); continue
        if abs(v - ans) > tol * max(1e-9, abs(ans)):
            L.err("answers.py", 1, f"{eid}: computes {v:g} but exercises.json says {ans:g} (tolerance {tol:g})")


def lint(folder):
    L = Lint(folder)
    meta = check_meta(L, folder)
    check_lesson_md(L, folder)
    answers = check_exercises(L, folder)
    check_solutions(L, folder, answers)
    check_exit_ticket(L, folder)
    check_sim(L, folder, meta)
    check_answers_py(L, folder, answers)
    return L


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    folders = ([f.parent for f in sorted((ROOT / "content").glob("*/*/meta.json")) if f.parent.parent.name != "_gold"]
               if args[0] == "--all" else [find_lesson(args[0])])
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
