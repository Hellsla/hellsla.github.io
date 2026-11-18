VERDICT: PASS
CONTENT-HASH: c6b17c0a5ccb80ab

## Blocking

## Polish

## Checked
- Delta round 1 (work queue 8g, Formula step rewritten as basic law, derived formula, symbolic simplification): hash identical at start and end.
- 21 Formula steps re-derived ($U_1/U_2 = N_1/N_2$, $P_1 = P_2$, $P_\text{h} = RP^2/U^2$, $R = 0.010\,U^2/P$, $P_2/P_1 = U_2^2/U_1^2$, three-phase $P_\text{h} = 3RI^2 = RP^2/(U^2\cos^2\varphi)$): algebra correct; L3-08's derivation moved from Principle into Formula, as in Finnish.
- English against Finnish by script: every Formula step's LaTeX is identical to the Finnish `**Kaava:**` once the subscripts are translated (only `text{}` labels differ, e.g. käämi/coil, ka/AVG, raja/limit); no Finnish subscript is left in the English set.
- Every number in every solution section is the same multiset as in the Finnish one (decimal comma normalised); exercises.json ids, numeric answers, tolerances and figures unchanged and equal to Finnish.
- The other changed lines are paragraph splits only: removed and added text identical after whitespace normalisation.
- Substitutions, answers and rounding unchanged from the version passed, so the earlier recomputation stands.
