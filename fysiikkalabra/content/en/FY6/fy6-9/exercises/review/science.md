VERDICT: PASS
CONTENT-HASH: 30bb671b683987a1
SCOPE: delta added-exercise from 51f6a10c66298771 base 8f23aa7ae3bd

## Blocking
(none)

## Polish
(none)

## Checked
- Delta: only the added exercise fy6-9-L2-08 judged; the rest unchanged per `reviews.py added_exercises`.
- Physics: charge as the area under a piecewise-constant I(t) graph, Q = sum I_i t_i; stored energy W = UQ with the nominal voltage, stated as the task's assumption (consistent with the glossary's battery capacity/energy definition).
- Recomputed independently: Q = 2.0·1.0 + 1.5·2.0 + 0.5·1.0 = 5.5 Ah, W = 61.05 Wh; answers.py prints 61.05; a student's 61 Wh is 0.08 % off, inside tolerance 0.02.
- Figure ex-current2 (figures.py): segments 2.0 A on 0–1.0 h, 1.5 A on 1.0–3.0 h, 0.5 A on 3.0–4.0 h, then zero; grid 0.5 h / 0.5 A; matches the solution's readings and the text description; the charge is not written in the figure.
- Solution complete: given/asked, principle with reason, symbolic formula before numbers, conversion (V·Ah = Wh), substitution with units, rounding reason, reasonableness (mean current 1.4 A between extremes; 61 Wh realistic for a laptop battery).
- Unit Wh and scope (FY6 batteries and charging circuit) correct.
