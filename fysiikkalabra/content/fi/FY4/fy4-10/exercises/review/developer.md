VERDICT: DONE

Round 1, exercises: one new data task, `fy4-10-L2-10` (teacher's brief FY4-A4), in fi, en and fi-easy. No existing exercise, id or answer changed.

- `lessons/FY4/fy4-10/answers.py`: a commented block for L2-10 (dict `s10`, not printed): every number of the model solution from the PhET Collision Lab default values (momentum and kinetic energy before, and after at 100 %, 50 % and 0 %; the momentum changes; the shares lost). The answer is a string, so nothing was added to `a`. The values agree with the coordinator's.
- `content/{fi,en,fi-easy}/FY4/fy4-10/exercises/exercises.json`: L2-10 appended as the last item of `level2`, kind data, model, reasoning; the situation with the source link, then parts a) to d); a string answer.
- `content/{fi,en,fi-easy}/FY4/fy4-10/exercises/solutions.md`: the block `## fy4-10-L2-10` appended (Kysytty, Periaate, Mallivastaus): the method, then a dated example solution with the default values, parts a) to d), the rounding of the display and the model's limits. Calculations are display rows with the same structure in all three languages.

Deviation: the task text writes the date as "16. marraskuuta 2026", because the lint rejects "16.11.2026" in a task text (decimal point rule).

Checks: lint, check_solutions, check_lesson and the layout at 360 px pass; 352 px reports only formulas of text not touched here.
