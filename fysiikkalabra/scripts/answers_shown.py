"""The answer an exercise shows (teacher 2026-10-30): the exact value, the tolerance and the shown value are kept apart.

- exercises.json `answer` is the exact value the answer check compares with (data-answer), `tolerance` its relative
  tolerance; neither is ever printed on the page.
- The shown answer ("Vastaus" under the exercise) is the model solution's own answer step, rounded as the solution
  rounds and justifies it, in the page language (decimal sign, units). An exercise without a solution shows the exact
  value rounded to three significant figures.

`python scripts/answers_shown.py` (CI) checks every language: each numeric exercise's solution states its answer as a
number in its answer step, and that number agrees with `answer` within the tolerance or the rounding of its last digit,
so the solution and the shown answer never disagree with the value the check accepts."""
import json, math, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import i18n

ROOT = pathlib.Path(__file__).resolve().parents[1]


def numbers(tex):
    """The numbers of a LaTeX answer, each as (value, mantissa, size of half its last digit), one per "=" or "≈" part:
    24{,}0 · 1{,}5 \\cdot 10^{3} · −0{,}50 · 800\\,\\text{J} = 0{,}8\\,\\text{kJ}."""
    out = []
    for part in re.split(r"=|\\approx|\\leq?|\\geq?|<|>", tex):
        t = part.replace("{,}", ".").replace("−", "-").replace("\\,", "").replace("\\ ", "").replace("~", "").replace(" ", "")
        m = re.match(r"([+-]?)(\d+(?:[.,]\d+)?)(?:(?:\\cdot|\\times)10\^\{?([+-]?\d+)\}?)?", t)
        if not m: continue
        digits = m.group(2).replace(",", "."); exp = int(m.group(3)) if m.group(3) else 0
        dec = len(digits.split(".")[1]) if "." in digits else 0
        mant = float(m.group(1) + digits)
        out.append((mant * 10 ** exp, mant, 0.5 * 10 ** (exp - dec), 0.5 * 10 ** -dec))
    return out


def shown(block, label, answer, tolerance=0.02):
    """The $…$ of a solution's answer step that states the checked answer (rounded), or None: the first whose number
    agrees with `answer` within the tolerance or the rounding of its last digit (a value given as a·10^n in the
    exercise's unit agrees by its mantissa)."""
    m = re.search(rf"\*\*{re.escape(label)}:\*\*(.*)", block)
    if not m: return None
    tol = tolerance * abs(answer) if answer else tolerance
    for tex in re.findall(r"\$([^$]+)\$", m.group(1)):
        for v, mant, half, mhalf in numbers(tex):
            if abs(v - answer) <= max(tol, half * 1.0001) or abs(mant - answer) <= max(tol, mhalf * 1.0001): return tex
    return None


def fallback(x):
    """An exact value rounded to three significant figures (no float artefacts), with a plain point."""
    if x == 0: return "0"
    d = max(0, 2 - int(math.floor(math.log10(abs(x)))))
    return f"{round(x, d):.{d}f}"


def blocks(text):
    out = {}
    for block in re.split(r"^## ", text or "", flags=re.M)[1:]:
        head, _, body = block.partition("\n"); out[head.strip()] = body
    return out


def check():
    bad = n = 0
    for lang in i18n.languages():
        label = i18n.lookup(i18n.strings(lang), "lesson.solution_answer_step")
        for ex in sorted((ROOT / "content" / lang).glob("*/*/exercises/exercises.json")):
            sol = ex.parent / "solutions.md"
            sols = blocks(sol.read_text()) if sol.exists() else {}
            for e in (x for lvl in json.loads(ex.read_text()).values() for x in lvl):
                if not isinstance(e.get("answer"), (int, float)) or isinstance(e["answer"], bool): continue
                n += 1; where = f"{ex.parent.relative_to(ROOT)} {e['id']}"
                if e["id"] not in sols: continue                                  # check_solutions.py reports it
                if shown(sols[e["id"]], label, e["answer"], e.get("tolerance", 0.02)) is None:
                    bad += 1; print(f"{where}: no number in the answer step agrees with the checked value {e['answer']}")
    print(f"{n} numeric answers checked" + (f", {bad} problems" if bad else ": every shown answer agrees with the checked value"))
    return bad


if __name__ == "__main__":
    sys.exit(1 if check() else 0)
