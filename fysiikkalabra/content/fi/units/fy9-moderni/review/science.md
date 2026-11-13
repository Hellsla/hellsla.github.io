VERDICT: PASS
CONTENT-HASH: dc13071f6130e116
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at b657e7155ea191a7.

## Blocking
(none)

## Polish
(none)

## Checked
- s5 a, refitted from the data in answers.py (net counts): slope $-4.528\cdot10^{-3}$ 1/s, giving $T_{1/2} = 153.1$ s. The fitted line is 5.993 at 0 s and 4.635 at 300 s, as quoted. Without the background the fit gives 157.1 s, as stated. The two-point estimate is 150.8 s, −1.5 %. The answer value 153 s with tolerance 0.04 matches the 147–159 s range in the rubric and in Hyväksytään myös. Part b's "noin 153 s" is consistent.
- s1 c: 0.0681 mSv, 1.15 %. s2 a: $\lambda = hc/(E_0(1/4-1/9)) = 656.5$ nm. s3 d: $W = -eb = 2.24$ eV and $f_0 = -b/k = 5.43\cdot10^{14}$ Hz with $k = h/e$. s6 b: 1653 kg, 1.51 kg.
Every number in the changed lines was recomputed with an independent script (scratchpad fy9merge/sci_fi.py); `units.py hash` gave the same value at the start and the end. LaTeX in all added lines has balanced `$` and braces.
