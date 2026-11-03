VERDICT: PASS
CONTENT-HASH: fc1949394b1858c6

## Blocking

## Polish
- exercises/solutions.md:43 (L1-05 Periaate) — "Oikosulkuvirtaa ei mitattu" now sits next to points that are "mallista lasketut", so "mitattu" implies the other points were measured. Write "Oikosulkupiste ei ole kuvaajan pisteiden joukossa, vaan …".
- exercises/solutions.md:49 (L1-05 Järkevyys) — "pysyy samana myös mittausalueen ulkopuolella": with model points, "pisteiden alueen ulkopuolella".
- Carried from round 1: L3-03 rounding reason (the 2,0 Ω and 6,0 Ω data limit R_s I₁) and L1-05 reading uncertainty (about 0,1 A, not the 0,5 A grid step).

## Checked
- Change judged: L1-05 task text and solution no longer call the figure's points measured; "(mallista lasketut pisteet)" matches the figure catalog ("four model (I, U) points") and figures.py (points on U = 4,5 − 1,5 I exactly). This removes the invented-measurement problem (guardrail: say whether data are measured, simulated or calculated).
- Extrapolation to U = 0 still says why it is justified (R_s constant beyond the points).
- All 12 answers recomputed in one script with my own formulas (L3-01 by node analysis, L1-05 from the slope of two points, L3-03 by solving two equations): 1,38 V; 32,5 A; 6,2 V; 0,15 Ω; 3,0 A; 1,0 Ω; 5,5 V; 3,0 W; 1,0 A; 0,75 A; 0,316 A; 1,60 V — all match answers.py and exercises.json.
- No number, symbol or answer changed; physics, notation (E, R_s, I_k) and assumptions as in my earlier PASS.
