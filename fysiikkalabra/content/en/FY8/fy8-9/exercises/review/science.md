VERDICT: PASS
CONTENT-HASH: 3d201d15eeee0bda
SCOPE: delta added-exercise from c0842f06ba77912b base 5b3ca4f81c77

## Blocking

## Polish

## Checked
- I compared the removed text with the added text outside the Formula lines, ignoring whitespace. They are identical: the rest of the diff is paragraph breaks only. No number, answer or tolerance changed.
- L1-03 and L2-01: N = N₀e^(−λt) with N = N₀/2 at t = T½ gives λT½ = ln 2. This is a correct derivation and within the scope note (both forms of the decay law are taught).
- L2-02: A = λN and λ = ln 2/T½ give N = A·T½/ln 2. L2-04: m = N·m_nucleus carries the decay law over to mass. Both are correct.
- L1-08, L2-05, L3-01 and L3-02: the logarithm step ln(A₀/A) = (t/T½) ln 2 is correct, and the unknown is isolated before substitution. In L2-05 and L3-02 the background is subtracted from the net counts and rates, as stated.
- L2-06: R(2T½) = R₀/4 is right.
- L3-03: equal initial activities (stated in the task), so A₀ cancels symbolically. This is right.
- L3-04: the ratio A₂(t₂)/A₂(t₁) removes A₂(0), and T₂ follows. The substitution uses total activity at 96 h and 168 h as A₂. This is justified, because the 6.0 h nuclide has decayed away by then (as before).
- L3-05: λ_eff = λ_phys + λ_bio, which the task gives, divided by ln 2 gives 1/T_bio = 1/T_eff − 1/T_phys. This is correct.
- L2-09: the net-count form (y − B) is kept through the logarithm. This is correct.
- I recomputed the touched answers in one script with my own formulas: L1-03 0.023028 1/a, L2-02 7.294e14, L2-04 0.69526 mg, L2-05 149.21 s, L3-02 5.0458 min, L3-03 6.9725 %, L3-04 2.6829 d, L3-05 4.9599 d. All agree with answers.py and lie inside their tolerance. The hash was 3d201d15eeee0bda at the start and at the end.
