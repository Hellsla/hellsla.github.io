VERDICT: PASS
CONTENT-HASH: 7cdf98adf7c64098

## Blocking
(none)

## Polish
- solutions.md L3-03 Järkevyys — 331 MW at 400 kV gives 828 A, not 826 A (826 A comes from the unrounded 330,6 MW). This is the same as in the Finnish version and does not affect the result.

## Checked
- All 12 answers recomputed independently and with answers.py; every one matches exercises.json.
- Task data and answers are identical to the Finnish set: the numbers in every text and solution section match.
- L2-04: the fitted curve through (5,0 A; 20 W) gives R = 0,80 Ω. The point check at 2,5 A (5,0 W) is right, and figures.json keeps the numbers of the alt text.
- L3-01: the transformer keeps P, and the line current comes from 400 kV. The check without a transformer (450 MW > P) is right.
- L3-02 and L3-03: R ≤ 0,010 U²/P = 4,0 Ω; P ∝ U² gives 3,31.
- Significant figures and the reasonableness checks are correct (sauna stoves, more than 10⁶ A at 230 V, 4 % at 110 kV).
