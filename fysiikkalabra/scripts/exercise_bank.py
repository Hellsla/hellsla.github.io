"""The exercise bank of a module (teacher 2026-11-04, "laajenna tehtäväpankit"): how many exercises each chapter has
per level and what they practise, against the bank's target.

  python scripts/exercise_bank.py FY1 [FY2 ...]     one line per chapter, then the module's sums
  python scripts/exercise_bank.py FY1 --md          the same as a Markdown table (docs/exercise-bank/)

Target per chapter (CLAUDE.md "Exercise levels"): at least 20 exercises, about 8 + 7 + 5 over the three levels, of
which 2–3 aineistotehtävää (kind "data": measurements in a table or a graph to read, fit or judge) mostly at level 2,
and some conceptual multiple choice, justified qualitative answers, experimental design, error analysis and graph
reading beside the calculations. A kind is what the exercise's own "kind" list says; a task without one counts as a
calculation (numeric answer) or a written answer. The lint enforces the counts a course sets in curriculum.json
(exercise_levels, exercise_total); this report shows the mix, which no lint can judge.
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import courses

TARGET = 20
COLS = ("calc", "written", "choice") + courses.EXERCISE_KINDS


def chapter(folder):
    f = courses.lesson_file(folder, "exercises.json")
    ex = json.loads(f.read_text()) if f.exists() else {}
    n = [len(ex.get(f"level{i}", [])) for i in (1, 2, 3)]
    mix = dict.fromkeys(COLS, 0)
    for items in ex.values():
        for e in items:
            mix["choice" if e.get("choices") else "calc" if isinstance(e.get("answer"), (int, float)) else "written"] += 1
            for k in e.get("kind", []): mix[k] += 1
    return n, mix


def main(argv):
    md = "--md" in argv
    codes = [a for a in argv if not a.startswith("--")] or courses.codes()
    head = ["luku", "L1", "L2", "L3", "yht."] + list(COLS)
    if md: print("| " + " | ".join(head) + " |\n|" + "---|" * len(head))
    else: print(" ".join(f"{h:>7}" for h in head))
    for code in codes:
        tot = [0, 0, 0]; short = 0
        for l in courses.curriculum()[code].get("lessons", []):
            folder = courses.course(code)["paths"]["content"] / l["id"]
            if not (folder / "meta.json").exists(): continue
            n, mix = chapter(folder)
            tot = [a + b for a, b in zip(tot, n)]; short += sum(n) < TARGET
            row = [l["id"], *n, sum(n), *mix.values()]
            print(("| " + " | ".join(map(str, row)) + " |") if md else " ".join(f"{x:>7}" for x in row))
        print(f"{code}: {sum(tot)} exercises ({'/'.join(map(str, tot))}); {short} chapter(s) under {TARGET}")


if __name__ == "__main__": main(sys.argv[1:])
