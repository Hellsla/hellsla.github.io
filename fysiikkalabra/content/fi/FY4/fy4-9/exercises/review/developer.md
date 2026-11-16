VERDICT: DONE

Round 1, exercises: one new data task, `fy4-9-L2-09` (teacher's brief FY4-A3), in fi, en and fi-easy. No existing exercise, id or answer changed.

- `lessons/FY4/fy4-9/answers.py`: a commented block for L2-09 (written task, no entry in `a`): method 1 $m = F\Delta t/\Delta v$ = 80 kg, the same with Newton II, method 2 $p_1$ = 4,0 kg·m/s and $m_2$ = 80 kg, the error example (Δv 0,130 m/s → 77 kg, about 4 %), each asserted.
- `content/{fi,en,fi-easy}/FY4/fy4-9/exercises/exercises.json`: L2-09 appended last in `level2`, kind experiment, reasoning, concept; situation with the NASA link, parts a)–d); `answer` a string, `unit` "", tolerance 0.02.
- `content/{fi,en,fi-easy}/FY4/fy4-9/exercises/solutions.md`: Kysytty, Periaate (names the facts taken from the source), Mallivastaus a)–d) with example values labelled as such, a second method by Newton III and impulse, error sources, reasonableness.

Deviations: the date is written "16. marraskuuta 2026" (the lint reads "16.11.2026" as a decimal point); springs are not attributed to SLAMMD (not in the verified facts); method 2 is computed in two rows ($p_1$, then $m_2$) so no formula is clipped at 360 or 352 px.

Checks: lint, check_solutions, check_lesson (all ok), check_layout 360 and 352 ok; check_i18n has no fy4-9 finding.
