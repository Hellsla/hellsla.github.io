VERDICT: FAIL
CONTENT-HASH: 7e6d204e0c7b09d6

## Blocking
- exercises.json:359–361 (fy3-8-L3-04) — **7, assessment.** The solution's answer a) is now "$13.2\,\text{mm}$, in practice at least $14\,\text{mm}$". That is the right safe-side rounding of an "at least" value to the two figures of $\alpha$. But the check has `answer` 13.2 and `tolerance` 0.03, so it accepts only $12.8$–$13.6\,\text{mm}$. A student who rounds to two figures as the solution and the house rule say, and enters $14$, is marked wrong ($+6\,\%$), while a student who rounds the wrong way and enters $13$ is marked right. — Fix: let the check accept $14$, for example `tolerance` 0.065 around 13.2. Alternatively, have the task ask for the computed value only (part a "to three figures") and keep $14\,\text{mm}$ as the practical remark.

## Polish
- solutions.md (fy3-8-L3-04, Answer): "the results are acceptable rounded to two figures" sits next to the three-figure $13.2\,\text{mm}$. Saying that $13.2$ is the computed value and $14\,\text{mm}$ the two-figure safe-side value would make it consistent.
- solutions.md (fy3-8-L3-03, Formula): as before, a last row $= (\gamma_\text{petrol} - 3\alpha_\text{steel})V_0\Delta T$ would simplify it to the end.

## Checked
- The diff is one line, L3-04 answer a). The direction of the rounding is now physically right: the gap must not close, so the minimum is rounded up.
- Recomputed: $g_\text{min} = 12\cdot10^{-6}\,\tfrac{1}{\text{K}} \cdot 25.0\,\text{m} \cdot 44\,\text{K} = 13.2\,\text{mm}$ and $g_\text{max} = 30 - 12.0 = 18\,\text{mm}$. answers.py gives 13.2.
- Model answer c) is consistent: $15\,\text{mm}$ lies in both $13.2$–$18$ and $14$–$18\,\text{mm}$, and the summer margin is $1.8\,\text{mm}$, the winter gap $27\,\text{mm}$.
- Nothing else changed since the PASS of the previous round.
- The hash was the same at the start and the end.
