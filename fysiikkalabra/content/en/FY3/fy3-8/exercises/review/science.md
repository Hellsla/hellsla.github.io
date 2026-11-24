VERDICT: PASS
CONTENT-HASH: ac3cb81970d997cb

## Blocking

## Polish
- solutions.md:277 (fy3-8-L3-04, Answer) — the sentence "the results are acceptable rounded to two figures" comes after the three-figure $13.2\,\text{mm}$ and does not say which way to round. For an "at least" value the safe side is up ($14\,\text{mm}$), and the check (12.8–13.6) would reject that, while it accepts the unsafe $13$. — Either drop the sentence or say that $13.2\,\text{mm}$ is the computed minimum and that, as a limit, it is never rounded down.
- solutions.md (fy3-8-L3-03, Formula): as before, a last row $= (\gamma_\text{petrol} - 3\alpha_\text{steel})V_0\Delta T$ would simplify the formula all the way.

## Checked
- The diff is one line, L3-04 answer a). The answer is now $13.2\,\text{mm}$ with no practical rounding, so it matches `answer` 13.2 with `tolerance` 0.03 in exercises.json. The Round 2 blocking item is resolved.
- Recomputed: $g_\text{min} = 12\cdot10^{-6}\,\tfrac{1}{\text{K}} \cdot 25.0\,\text{m} \cdot 44\,\text{K} = 13.2\,\text{mm}$. The winter change is $12.0\,\text{mm}$, so $g_\text{max} = 18\,\text{mm}$. answers.py gives 13.2.
- Model answer c) agrees with a): $15\,\text{mm}$ lies in $13.2$–$18\,\text{mm}$, the summer margin is $1.8\,\text{mm}$ and the winter gap is $27\,\text{mm} < 30\,\text{mm}$.
- Nothing else changed since the earlier PASS.
- The hash was the same at the start and the end.
