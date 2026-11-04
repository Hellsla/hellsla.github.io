VERDICT: PASS
CONTENT-HASH: 8631b611eae6c176

Full review of the exercise-bank additions (L1-06..08, L2-05..07, L3-04..05); existing tasks unchanged.

## Blocking
(none)
## Polish
- exercises.json:131/227/277, solutions.md:151–153, 179–193 — the new tasks L2-05, L3-04 and L3-05 write position as $x$, $x_0$ while the lesson's formula and the other 15 tasks use $s$, $s_0$ — use $s$ (and $s_0$) in text, data columns and solutions, or say once that $x$ is the same paikka.
- exercises.json:284/289 vs :290 and solutions.md:192 — the correct option says the speed "olisi ääretön", its feedback and the Periaate say $\Delta x : \Delta t$ "ei ole mikään luku" — pick one wording, e.g. "nopeuden pitäisi olla ääretön, joten osamäärä ei ole mikään luku" in all three places.
- exercises.json:227 (L3-04) — the number asked (60 m : 40 s) can be got without the piecewise model or the break point; consider also asking for $v_1$ and $v_2$ (3,0 and 1,0 m/s) so the YO-style modelling step is graded.
- exercises.json:277 (L3-05) — as multiple choice the level-3 "laadullinen perustelu" of the plan shrinks to a recognition task; consider an open written justification.
- solutions.md:156 (L2-05) — "17,5–18,5 m on hyvä vastaus" but the tolerance 0,04 accepts 17,3–18,7 m; make the two ranges agree.
## Checked
- answers.py run with python3 -I: all 18 numbers match exercises.json; recomputed independently in one call.
- L1-07 0,80·12 = 9,6 m; L1-08 2400 m : 960 s = 2,5 m/s; L2-06 v = 1,5 m/s, s = 17 m (33 m would need 4,2 m/s).
- L2-05 least squares: slope 1,403 m/s, intercept 1,21 m, x(12 s) = 18,04 m; the solution's line (0; 1,2)–(5,0; 8,2) lies on the fit (8,22 m at 5 s); extrapolation 0–5 s → 12 s named as a model assumption (guardrail "Fits").
- L2-07 0,2 s : t ≤ 2,0 % → t ≥ 10 s, s = 8,0 m; 1,0 m → 16 %; hand-timing 0,2 s matches the guardrail example.
- L3-04 data consistent: 3,0 m/s on 0–10 s, every later point on 1,0 m/s; v_ka = 1,5 m/s; mean of speeds 2,0 m/s correctly rejected (time-weighting).
- L3-05 physics right: a (t, x) graph is a function, vertical line = Δt = 0; stop = horizontal line; distractor feedback each says why it is wrong.
- Scope: everything stays at s = s₀ + vt; no duplicate of L1-01..L3-03; set plan (+3/+3/+2) followed.
