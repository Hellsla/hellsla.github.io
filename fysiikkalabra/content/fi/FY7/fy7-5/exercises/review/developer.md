VERDICT: DONE

Added fy7-5-L2-08 (figure task, Level 2) in fi, en and fi-easy; chapter now has 2 figure tasks (L2-02, L2-08).
- lessons/FY7/fy7-5/figures.py: new figure variant `flux-task-2` (Φ(t) 5,0 → −3,0 → 0 mWb, flux changes sign, no voltage drawn) plus REUSE note (safe). Existing figures untouched. figcat build not run (coordinator).
- lessons/FY7/fy7-5/answers.py: one new line, L2-08 = 4,0 V.
- content/{fi,en,fi-easy}/FY7/fy7-5/exercises/exercises.json: new task (N = 200, |e_ka| over 0–0,40 s, answer 4,0 V, tolerance 0,02).
- solutions.md in each language: full solution with Kuvaajan lukeminen.
- content/{en,fi-easy}/FY7/fy7-5/figures.json: description translations.
Checks: check_lesson.py all ok; lint 0 errors (one old warning on L3-05 length); check_solutions ok; figures --check ok. check_i18n.py not run (long); left to the coordinator.
