VERDICT: PASS
CONTENT-HASH: 893f7af3e4ffe409
SCOPE: delta (work queue 8g: Kaava step of the model solutions; paragraph breaks)

## Blocking

## Polish
- content/en/FY8/fy8-8/exercises/solutions.md (fy8-8-L3-06 Answer): my earlier Polish item still stands. "Three significant figures as in the given constants" gives the wrong reason, because h, c and 1 eV have four figures.

## Checked
- I compared the removed text with the added text outside the Formula lines, ignoring whitespace. They are identical: the rest of the diff is paragraph breaks only. No number, answer or tolerance changed.
- I read the new Formula blocks on disk; the packet's diff flattens their aligned rows.
  - L1-04, L2-01, L3-02 and L3-05 start from E_γ = hf and c = fλ and derive λ = hc/E_γ symbolically. L2-01 and L3-05 first state E_γ = E_u − E_l.
  - L2-03 gets E_g = hc/λ the same way and keeps the ratio E_γλ/(hc).
  - L3-02 states correctly that λ_min comes from E_max.
- L3-06: E_u = E_l + E_γ builds up the levels A, B and C. λ = c/f = hc/E_C is right for the direct C → ground transition: the photon energy equals E_C, as the Formula's own note (E_C = hf) says.
- L2-07, L2-09 and L3-04 have only paragraph breaks; their formulas and reasoning are unchanged.
- I recomputed every touched answer with my own formulas in one script. All agree with answers.py and lie inside their tolerance: L1-04 20.826 pm, L2-01 1.0568 pm, L2-03 2.935e5, L3-02 1.240 pm, L3-04 n_β = 4, L3-05 1.0781 pm, L2-09 2158.6 keV, L3-06 0.49487 pm.
- The hash was 893f7af3e4ffe409 at the start and at the end.
