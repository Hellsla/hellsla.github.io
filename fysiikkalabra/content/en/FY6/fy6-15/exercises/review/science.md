VERDICT: PASS
CONTENT-HASH: 69299f6aec49b867
SCOPE: delta added-exercise from f60d53b70291bcbe base 8f23aa7ae3bd

## Blocking
(none)

## Polish
- content/en/FY6/fy6-15/exercises/solutions.md (fy6-15-L2-08, Answer) — "two significant figures like the rated current 16 A" names a value that does not enter the calculation; the limiting data are the graph reading 4000 W (on a 1000 W gridline) and U = 230 V (same note as on the Finnish set).

## Checked
- Delta: only the added exercise fy6-15-L2-08 judged; the rest unchanged per `reviews.py added_exercises`.
- Task and figure description say "example data", not measured data (the Finnish round-1 finding is carried into the English).
- Figure ex-kuorma (figures.py): steps 1000 / 3000 / 4000 / 2000 / 3500 W at 0–4 / 4–10 / 10–16 / 16–24 / 24–30 min, as the description and the solution's reading; maximum 4000 W on a gridline; no current or fuse limit drawn.
- Physics: loads of the group in parallel at 230 V, so I = P : U (resistive loads, power factor about 1: fair simplification, C).
- Recomputed: I = 4000 W : 230 V = 17.39 A = answers.py; the rounded 17 A is 2.2 % off, inside the 3 % tolerance.
- Fuse statement correct: P_max = 230 V · 16 A = 3680 W; only the 4000 W step exceeds it; "the fuse does not necessarily trip at once" is right for a ~9 % overload of a few minutes (a fuse trips on a slight overload only after a long time), so no overstated safety claim.
- Solution complete: principle and reason, graph reading, formula before numbers, units, rounding, real check against 3680 W.
- Scope: FY6 electrical safety (fuse).
