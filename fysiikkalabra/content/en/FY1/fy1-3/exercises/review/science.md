VERDICT: PASS
CONTENT-HASH: 6ed6cdfba3595d98

## Blocking

## Polish
- content/en/FY1/fy1-3/exercises/solutions.md (fy1-3-L2-09, Model answer c) — "and next four experiments at Gran Sasso" still reads oddly — "and later four experiments at Gran Sasso".

## Checked
- Hash (--exercises --lang en) 6ed6cdfba3595d98 at start and end.
- Delta is paragraph splitting in solutions.md (L1-01, L1-03, L1-05, L2-01, L2-05, L3-02, L1-06, L1-07, L2-04, L2-06, L3-04, L3-05, L3-06, L2-09): no word, number, sign or unit changed; every Principle/Answer keeps its full reasoning.
- fy1-3-L1-09 substitution recast as an aligned chain: mean 5.050/5 = 1.010 g/cm³, deviation (1.010 − 0.998206)/0.998206 = 1.18 %, matches answers.py and exercises.json (tolerance 0.04).
- fy1-3-L2-09 recomputed: t = 2.435 ms, Δt/t = 0.00246 %, cΔt = 18.0 m, t/Δt ≈ 40 600; unchanged.
- Guardrail wording (reading half a division plus total uncertainty, outlier kept unless a recorded gross error, overlapping intervals do not prove equality, estimates not certain limits) intact after the splits.
