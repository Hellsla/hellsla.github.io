VERDICT: PASS
CONTENT-HASH: 3da39fd69be8f71f
SCOPE: delta kaava-steps (8g)

## Blocking
(none)

## Polish
(none)

## Checked
- Diff parsed hunk by hunk: only Formula lines and paragraph breaks changed; no number dropped from a Formula line; answers.py, answers and tolerances untouched.
- Every Formula block starts from ΔE = hf (photon energy = level difference) and c = fλ, then solves λ = hc/ΔE symbolically (L1-02, L1-05, L2-01, L2-03, L3-01).
- L2-02: smallest energy gap gives the longest wavelength, λ_max = hc/ΔE_min: correct.
- L3-01: ionisation from level 2, hc/λ_min = 0 − E_2: correct.
- L3-03 (fluorescence cascade): E_UV = E_1 + E_2, λ_2 = hc/(hc/λ_UV − E_1): correct energy conservation.
- L3-04: levels above ground E_1 < E_2 < E_3, E_1 = E_3 − (E_3 − E_1), λ_6 = hc/E_1; checked against the pairing argument in the Principle (E_1 = 1.10 eV, longest line).
- L3-05: lost fraction p = 1 − E_fl/E_abs = 1 − λ_abs/λ_fl: correct.
- L3-06: E_viol − E_green = E_l,green − E_l,viol: correct.
- Hash 3da39fd69be8f71f at start and end.
