VERDICT: PASS
CONTENT-HASH: 9513edc0c5bdaae2
Round: 2
Mode: delta

## Blocking

## Polish
- exercises/solutions.md:198 (L3-05) — the first row P_im = (1 − f)S + fS/2 sets the outgoing power at the top equal to the absorbed solar power without saying so; the old text wrote the balance explicitly — open with P_lähtö = P_im and P_lähtö = (1 − f)S + fS/2.

## Checked
- Every changed Kaava starts from P = UAΔT, E = Pt, Q = cmΔT or the energy balance, and solves the asked quantity symbolically; every row algebraically right.
- L1-05 balance P_säteily = P_im = P_tulo − P_heij right (239 W/m²).
- L2-04: P_im = (1 − r)P_tulo, ΔP_im = (r1 − r2)P_tulo = 3.4 W/m² right.
- L3-04 albedo: ΔP = IΔA(a_jää − a_meri) from P_meri − P_jää right; recomputed 1.75·10¹⁴ W, 0.343 W/m².
- L3-05: (1 − f/2)S = 239 W/m² with f/2 = 0.40 gives S = 398.3 W/m²; ground check 239 + 0.40·398.3 consistent.
- L3-01, L3-02: cmΔT = Pt and cmΔT = 10fE_v; conditions (no change of state) stated.
- L3-03: W = (U1 − U2)AΔT t/ε right; L2-07 slope k = UA right.
- Sijoitus and answers unchanged; hash identical at start and end.
