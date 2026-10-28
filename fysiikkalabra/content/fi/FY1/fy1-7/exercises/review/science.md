VERDICT: PASS
CONTENT-HASH: 4336e3fb3c6c8370

## Blocking

## Polish
- content/fi/FY1/fy1-7/exercises/exercises.json:48 — L2-01 now mixes a LaTeX product of the dimensions with a plain-text density "19 300 kg/m³" in the same sentence — write both the same way (e.g. density also in LaTeX).

## Checked
- All 12 answers recomputed (ρ = m/V, m = ρV, V = m/ρ, displacement V2 − V1, container mass subtracted, equal-mass ratio, mixture mean density, wire L = m/(ρπr²)) and equal to answers.py; tolerances fit the rounded answers (L2-01 1,93 → 1,9: 1,6 %; L2-02 1,975 → 2,0: 1,3 %).
- Densities match the lesson's table; magnitudes realistic (lead, steel ≈ 7860, ice 920, ethanol 788).
- Significant figures justified by the limiting datum, incl. the 4,2 ml difference in L2-03.
- Teacher's rules 2026-10-28: L2-01's former "×" is now "\cdot" with the meaning (product of three dimensions) unchanged; no × elsewhere; divisions as operations use ':' (L1-05, L2-03, L3-01 ratio V_Al : V_Cu and 8960 : 2700); colon replacements in a196d94 keep operands and meaning.
- Notation ρ, m, V, a, L as in the lesson; every solution complete and symbolic first; inside FY1 scope.
