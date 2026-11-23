VERDICT: PASS
CONTENT-HASH: ff46a59fd2b8b611
SCOPE: delta added-exercise from e73b4e5e83dd72e3 base 5b3ca4f81c77

## Blocking

## Polish
- exercises/exercises.json (fy8-7-L2-08 and L3-06 text): my earlier Polish item still stands. "As a function of wavelength" reads as if one laser's wavelength were varied.

## Checked
- I compared the removed text with the added text outside the Formula lines, ignoring whitespace. They are identical word for word: the only other change is new paragraph breaks. No number, answer, tolerance or substitution changed.
- I read every new Formula block on disk. The packet's diff flattens the `aligned` rows, but on disk each is a clean aligned derivation. Each starts from E = hf (or P = (N/t)·hf, E = N·hf), uses f = c/λ and reaches the same derived form as before. L1-03, L1-04, L2-03 and L3-01 solve for the unknown symbolically. L2-01, L2-02, L3-03, L3-05 and L3-06 cancel hc (or h) symbolically before substitution.
- L3-04: η_q = (P_L λ_L)/(P_p λ_p) follows from N/t = Pλ/(hc). P_unav = (N_L/t)(hf_p − hf_L) is the right unavoidable part (the quantum defect).
- L3-05: the chain ΔP_L/ΔP_p = (ΔN_L/ΔN_p)(λ_p/λ_L) is inverted correctly, giving ΔN_L/ΔN_p = slope · λ_L/λ_p.
- L3-03: E_light = hf_light and E_q = hf_q, so the ratio is c/(λ f_q). This is right.
- I recomputed every numeric answer with my own formulas in one script (h = 6.626e-34, c = 2.998e8). All of them agree with answers.py and lie inside their JSON tolerance: for example L1-04 1.6069e16, L2-03 527.66 nm, L3-02 2.0338e18 1/s, L3-04 82.223 %, L3-05 0.5241, L2-08 1.490 mW, L3-06 3.022.
- The notation (E = hf, f = c/λ, N/t) stays within the FY8 photon-energy scope.
- The hash was ff46a59fd2b8b611 at the start and at the end.
