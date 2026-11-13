VERDICT: PASS
CONTENT-HASH: 1384d394cc10e7a3
SCOPE: delta added-exercise from 4bbd51e0c6f48c2d base 81db4a6fd727

## Blocking
- none

## Polish
1. content/fi-easy/FY3/fy3-13/exercises/solutions.md (fy3-13-L2-10, Periaate): it still says "Pisteet ovat suoralla", while L2-09 says "lähes suoralla" about the same figure. Use "lähes suoralla" here too.

## Checked
- L2-09 now finds the zero point from the slope. The solution says, correctly, that the figure's axis ends at −150 °C, so θ₀ cannot be read off the graph and is computed as θ₀ = θ₁ − p₁/k. The earlier eye-fit range has been removed.
- L2-09 recomputed: k = 27,5/100 = 0,275 kPa/°C, so θ₀ = −75/0,275 = −272,7 °C. answers.py gives −272,727.
- The uncertainty statement is consistent: ±1 kPa at 100 °C gives k between 0,265 and 0,285, so θ₀ runs from −283 to −263 °C (about ±10 °C). The 5 % tolerance (±13,6 °C) covers this, and the "third digit not reliable" remark is right.
- The independent check is valid: 75 kPa / 273,15 K = 0,275 kPa/K.
- L2-10 unchanged: p = 75 + 0,275 · (−73,15) = 54,88 kPa, which agrees with p ∝ T.
- L1-09 unchanged: θ₀ = −T₀ = −273,15 °C.
- The script compared fi-easy with the Finnish: answers, units, tolerances, figure ids and all numbers are identical.
- Hash the same at start and end.
