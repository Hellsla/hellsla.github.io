VERDICT: PASS
CONTENT-HASH: ecbc4e40fc947ac8

## Blocking
(none)

## Polish
- exercises/solutions.md fy8-6-L3-02 Formula — say that $\Delta h = \tfrac{h_\text{max} - h_\text{min}}{2}$ is half the range of the steepest and shallowest lines (an estimate, guardrails "Showing uncertainty").

## Checked
- Hash at the start was b12729dd62abae8c (the packet's); in that version L2-06's Formula had $h_0 = 6.626\,\text{J}\,\text{s}$ with the factor $10^{-34}$ missing (the only number lost in the 8g diff). Commit 7eff52543e changed only that line to $6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$; the Finnish file is fixed too. Re-judged at ecbc4e40fc947ac8.
- Apart from that, only Formula lines and paragraph breaks changed; answers.py, answers and tolerances untouched.
- L1-04, L1-07, L2-01, L2-02: eU_k = hf = hc/λ, then λ = hc/(eU_k), U_k = hc/(eλ), h = eU_kλ/c: correct.
- L1-05, L3-01, L3-04: U_k = (h/e)f, slope k = h/e, h = ek: correct.
- L2-03: N = I/e, P = NE = Ihc/(eλ); L3-03: N_f/N_e = Pλe/(hcI): correct.
- L2-04, L2-07: ΔE = hc/λ_1 − hc/λ_2 (energy left in the material): correct.
- L2-05: I = k(U − U_k), U_k = U_1 − I_1/k: correct.
- Hash ecbc4e40fc947ac8 at the end.
