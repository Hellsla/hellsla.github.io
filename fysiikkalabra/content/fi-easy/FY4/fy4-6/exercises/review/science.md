VERDICT: PASS
CONTENT-HASH: 3dd1d151602926c5

## Blocking

## Polish
- exercises.json fy4-6-L1-08, the distractor "$N > G$…" feedback — "Kohtisuoraan pintaa vastaan vaikuttavat vain paino ja tukivoima" is loose, because the weight is not perpendicular to the slope. Fix: "…vaikuttavat vain painon komponentti $G_y$ ja tukivoima".
- fy4-6-L1-09 — I could not check the MAFY steel–ice value $\mu = 0{,}014$ offline. The 4 % tolerance covers small differences between tables. Confirm it against mafytaulukot.fi once.

## Checked
- Recomputed all 20 numeric answers in one script with my own formulas, side by side with answers.py and exercises.json: every value agrees (L1-01 259, L1-02 35, L1-03 0,31, L1-04 7,4, L1-05 59, L1-09 6,18, L2-01 0,13, L2-02 0,81, L2-03 0,21, L2-04 8,1, L2-05 0,42, L2-06 0,29, L2-07 0,47, L2-09 2,1, L3-01 0,36, L3-02 0,80, L3-03 0,33, L3-04 73, L3-05 8,7).
- L1-07 as it stands now (edited after the packet was made): 220,7 N is rounded up to 230 N as an "at least" value (P7). Tolerance 5 % accepts the unrounded 221 N.
- L3-01: $\mu_0 \ge 0{,}357$ is rounded up to 0,36, the safe side.
- L2-08: the order is B 30 N, C 44 N, A 59 N, D 123 N. D really is at rest, since $\mu_0 N = 149\,\text{N} > 123\,\text{N}$.
- The fits through the origin (L2-03, L2-05) are least-squares slopes, and the mittaus points in figures.py match answers.py.
- L3-04: locked-wheel kinetic friction, and on the downhill $a = g(\mu\cos\alpha - \sin\alpha)$. L3-05: the student's error is $N = mg$, with $a$ 1,47 against the correct 1,93 m/s².
- L3-02: the remark on staying put after stopping ($\mu_0 \ge \tan 20^\circ$) is correct.
- Choice tasks L1-06 and L1-08 each have exactly one correct option.
- The solutions are complete: symbolic first, then conversions, substitution and rounding reasons, and real reasonableness checks.
