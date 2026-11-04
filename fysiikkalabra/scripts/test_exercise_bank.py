"""The exercise bank's schema (teacher 2026-11-04, README "Exercise schema"): multiple choice, data tables, kinds,
counts as minimums, and data tables in translations. python scripts/test_exercise_bank.py; exit 1 on a failure."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check_i18n, courses, exercise_bank, lint_lesson

fails = []
def ok(cond, msg):
    if not cond: fails.append(msg)

good = {"id": "x-L1-06", "answer": "B", "unit": "", "choices": [{"text": "A", "feedback": "no"}, {"text": "B", "correct": True, "feedback": "yes"}, {"text": "C", "feedback": "no"}]}
ok(lint_lesson.exercise_choice_errors(good) == [], "a valid multiple choice passes")
ok(lint_lesson.exercise_choice_errors({**good, "answer": "A"}), "answer must be the correct option's text")
ok(lint_lesson.exercise_choice_errors({**good, "choices": good["choices"][:2]}), "at least three options")
ok(lint_lesson.exercise_choice_errors({**good, "choices": [dict(c, correct=True) for c in good["choices"]]}), "exactly one correct option")
ok(lint_lesson.exercise_choice_errors({**good, "choices": [{"text": "A", "correct": True}] + good["choices"][:2]}), "every option has feedback")

table = {"caption": "t", "columns": ["$t\\,(\\text{s})$", "$x\\,(\\text{m})$"], "rows": [["0.0", "0.10"], ["1.0", "0.61"]]}
ok(lint_lesson.data_errors(table) == [], "a valid data table passes")
ok(lint_lesson.data_errors({**table, "rows": [["0,0", "0.10"], ["1.0", "0.61"]]}), "a decimal comma in a cell fails")
ok(lint_lesson.data_errors({**table, "rows": [[0.0, 0.10], ["1.0", "0.61"]]}), "a number cell is a string")
ok(lint_lesson.data_errors({**table, "rows": [["0.0"], ["1.0", "0.61"]]}), "a row has one cell per column")

errs = []; check_i18n.same_data(table, {**table, "caption": "Position", "rows": [["0.0", "0.10"], ["1.0", "0.61"]]}, "x", errs)
ok(errs == [], f"a translated caption passes: {errs}")
errs = []; check_i18n.same_data(table, {**table, "rows": [["0.0", "0.10"], ["1.0", "0.62"]]}, "x", errs)
ok(errs, "a changed number in a translation fails")
words = {"columns": ["Lähde", "$P\\,(\\text{MW})$"], "rows": [["Tuuli", "12.0"], ["Vesi", "8.5"]]}
errs = []; check_i18n.same_data(words, {"columns": ["Source", "$P\\,(\\text{MW})$"], "rows": [["Wind", "12.0"], ["Water", "8.5"]]}, "x", errs)
ok(errs == [], f"words in cells are translated: {errs}")

ok(set(courses.EXERCISE_KINDS) <= set(exercise_bank.COLS), "the report counts every kind")
c = courses.course("FY1")
ok(c["exercise_total"] >= sum(c["exercise_levels"].values()), "exercise_total is at least the levels' sum")

print("\n".join(f"FAIL {m}" for m in fails) or "OK test_exercise_bank")
sys.exit(1 if fails else 0)
