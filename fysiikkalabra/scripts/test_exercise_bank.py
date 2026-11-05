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

# the YO-skill forms (teacher 2026-11-05): figure options, two-stage, true-or-false, order
ok(lint_lesson.exercise_choice_errors({**good, "choices": [dict(c, figure="fy1-5/x") for c in good["choices"]]}) == [], "an option may be a figure")
ok(lint_lesson.exercise_choice_errors({**good, "reasons": good["choices"]}) == [], "a valid two-stage task passes")
ok(lint_lesson.exercise_choice_errors({**good, "reasons": good["choices"][:2]}), "a two-stage task needs 3–5 reasons")
tf = {"id": "x-L1-07", "answer": "1 tosi, 2 epätosi, 3 tosi", "unit": "", "statements": [{"text": "a", "true": True, "feedback": "f"}, {"text": "b", "true": False, "feedback": "f"}, {"text": "c", "true": True, "feedback": "f"}]}
ok(lint_lesson.exercise_choice_errors(tf) == [], "valid statements pass")
ok(lint_lesson.exercise_choice_errors({**tf, "statements": [dict(c, true=True) for c in tf["statements"]]}), "statements need one true and one false")
ok(lint_lesson.exercise_choice_errors({**tf, "statements": [dict(tf["statements"][0], true="kyllä")] + tf["statements"][1:]}), "true is a boolean")
ok(lint_lesson.exercise_choice_errors({**tf, "choices": good["choices"]}), "one answer form per task")
od = {"id": "x-L1-08", "answer": "C, A, B", "unit": "", "prompt": "Järjestä pienimmästä suurimpaan.", "order": [{"text": "C"}, {"text": "A"}, {"text": "B"}]}
ok(lint_lesson.exercise_choice_errors(od) == [], "a valid order task passes")
ok(lint_lesson.exercise_choice_errors({**od, "prompt": ""}), "an order task names its quantity in the prompt")
ok(lint_lesson.exercise_choice_errors({**od, "answer": ""}), "an order task gives the order in words")

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
