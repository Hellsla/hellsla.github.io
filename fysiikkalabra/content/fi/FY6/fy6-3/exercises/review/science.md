VERDICT: FAIL
CONTENT-HASH: 0b63d6873f704fa6

## Blocking
- exercises/solutions.md:90 (fy6-3-L2-04 Järkevyys) — A: "Poikkipinta-ala on noin 0,13 mm², vähän alle simulaation ohuimman langan" is wrong: the sim's thinnest wire is 0,10 mm², so 0,13 mm² is a little *more*; the same sentence then says "hieman paksumpaa lankaa", contradicting itself — write "vähän yli simulaation ohuimman langan (0,10 mm²)".

## Polish
- lessons/FY6/fy6-3/answers.py:26–27 — comments give the slope as 5,45 Ω/m; the computed least-squares slope is 5,473 Ω/m (solutions.md correctly says 5,47) — correct the comments.
- exercises/solutions.md (L3-03 Järkevyys) — "langan ohuin kohta kuumenee eniten" could add the reason (largest resistance per length there), so it is a mechanism, not a label.

## Checked
- Recomputed all 12 answers from the task text with own formulas: 26,4→26 Ω; 3,3 V; 10 A; 0,17 Ω; 2,5 kΩ; 0,375→0,38 A; 6,69→6,7 Ω; 1,7 mm²; 7,96→8,0 Ω; 3,2 Ω; 1,09→1,1 µΩ·m; 3,0 A — all agree with exercises.json and answers.py.
- L2-02: lamp-curve figure drawn from the same lamp model as the sim; at 1,0 V the curve is at 0,149 A, readable as 0,15 A on the 0,05 A grid.
- L3-01: constant volume, l doubles and A halves → 4R; reasoning stated.
- L3-02: R : l per point (5,49 / 5,43 / 5,56 / 5,43 Ω/m) and fit through the origin correct; origin justified by R ∝ l; guardrail fit sentence used.
- L3-03: cold-filament inrush 12× running current, consistent with lesson model (1,0 Ω cold, 12 Ω at 3,0 V).
- Unit conversions mm² ↔ m² and mA, unknowns solved symbolically first, significant figures justified by the limiting data.
- Ohm's-law conditions (constant temperature) stated in L2-01; L1-01/L1-03 use R = U : I at the operating point, which is correct.
