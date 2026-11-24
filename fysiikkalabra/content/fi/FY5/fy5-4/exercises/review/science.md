VERDICT: PASS
CONTENT-HASH: afd4fbbebd320dc8
SCOPE: delta answers,numbers from eeef02e000ff63e5 base 48ff417

## Blocking

## Polish
- content/fi/FY5/fy5-4/exercises/solutions.md:164 (L3-03, reasonableness check) — "about 450 m" for 120 km/h is the exact 2,25 · 201,4 m = 453 m. It is also a smallest allowed radius, and by the same rule it would round up to 460 m (or 2,25 · 210 m ≈ 470 m). It is not wrong as an estimate. — Optionally write "about 460 m".

## Checked
- The hash was the same at the start and the end. I judged only the diff (L3-01, L3-03: answer, tolerance, the Answer line, answers.py). My previous Polish item (limits rounded to the unsafe side) is fixed.
- I recomputed in one script with my own formulas: L3-01 v = sqrt(mu0 g r) = 7,672 m/s = 27,62 km/h; L3-03 r = v²/(0,25 g) = 201,36 m. answers.py now gives 27 (floor) and 210 (ceil to two figures). These match exercises.json in this language.
- Direction of rounding: L3-01 asks for the greatest speed ("at most"), so it rounds down to 27 km/h; L3-03 asks how large the radius must be at least ("at least"), so it rounds up to 210 m = 2,1·10² m. Both follow CLAUDE.md P7 (limit values to the safe side). Two figures are right (60 m, 0,10; 80 km/h, 0,25).
- Tolerances, checked with the page's rule max(2 %, tol, half a unit): L3-01 (tol 0,03) accepts 27 and the exact 27,6, and 28 is only "near"; L3-03 (tol 0,045) accepts 210, 201 and 201,4, and 200 is only "near". So the exact value is accepted and the unsafe rounding is not.
- The new Answer lines state the exact value, the significant figures and the reason for the rounding direction correctly. The Sijoitus rows above them are unchanged (27,62 km/h; 201,4 m).
- The L3-01 check (sqrt 8 · 27,62 ≈ 78 km/h on dry asphalt) is still consistent.
