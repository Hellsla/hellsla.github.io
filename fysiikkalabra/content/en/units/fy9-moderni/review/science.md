VERDICT: PASS
CONTENT-HASH: 2b347105827eead3
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at 4a4554bfe169b358.

## Blocking
(none)

## Polish
1. s5 a Answer quotes "without subtracting the background the fit would give $157\,\text{s}$" (recomputed: 157.08 s, correct), but answers.py has no key for it (`s5-a-raw` = 154.9 s is the raw two-point value). Adding a key such as `s5-a-raw-fit` would make the number traceable.

## Checked
Every hunk of the en merge diff (word diff). Refit of all 11 background-subtracted points (own numpy fit): slope $-4.528\cdot10^{-3}$ 1/s, intercept 5.993, value 4.635 at 300 s, $T_{1/2} = 153.07$ s; two-endpoint 150.8 s (−1.5 %); raw fit 157.1 s; answers.py run (s5-a 153.1, s5-a-two 150.83, nothing references the removed `s5-a-fit` key); tasks.json value 153 with 4 % tolerance = the stated 147–159 s range, the two-point method accepted. Photoelectric $W = -eb$, $f_0 = -b/k$ with $k = h/e$: 5.43·10¹⁴ Hz; $E_0(1/4 - 1/9)$ form; the Cs and U mass symbols. Every changed formula is symbolic before substitution and uses no symbol in a sense that differs from the unit's ```kaavat``` names or notation from #522; the $ and brace balance of each added line is checked; `units.py check` passes; the hash was taken at the start and the end and matches.
