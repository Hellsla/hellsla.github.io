VERDICT: DONE

Mode add, round 1: one new level-2 task, fy1-5-L2-08, type 2 "Kuvaajan valinta" (docs/exercise-types.md). Existing tasks, ids and solutions untouched; the chapter now has 8/8/5 = 21.

- exercises.json: L2-08. A walker stands at $6{,}0\,\text{m}$ from the start for $4{,}0\,\text{s}$, then walks back at $1{,}0\,\text{m/s}$; which graph is the (t, s) graph? Four `choices`, each a figure: A rising after 4 s (slope sign), B a (t, v) graph 0 then 1,0 m/s (v–t vs s–t), C correct (flat at 6 m, down to 0 at 10 s), D the distance walked from 0 (paikka vs matka). kind graph, concept; answer "Kuvaaja C".
- solutions.md: Kysytty · Periaate · Mallivastaus · Kuvaajan lukeminen (check_solutions wants the graph step after Mallivastaus in a word task), with $\Delta t = 6{,}0\,\text{s}$ and slope $-1{,}0\,\text{m/s}$ shown.
- answers.py: none (a choice task).
- lessons/FY1/fy1-5/figures.py: new figures pick-back, pick-away, pick-distance, pick-vt (Axes, LaTeX labels, arrows) with REUSE notes; catalog rebuilt with figcat.

Checks: lint 0 errors, check_solutions ok. Not fixable here: lesson.md:297 inline \dfrac warning.
