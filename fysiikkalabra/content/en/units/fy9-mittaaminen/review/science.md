VERDICT: PASS
CONTENT-HASH: 2996fa9824b493d6
SCOPE: delta: round 3, the fixes of round 2 in fy9-mittaaminen-s7 and -s8 (s8 a rubric criterion 5, s7 c formula rows); older tasks s1-s6 untouched (not re-judged).
Round 3: delta against the version round 2 reviewed (fix round 2).

## Blocking
None.

## Polish
- s8 a, criterion 5: the added range ("every line through the $\pm 0.01\,\text{m}$ ranges of the points crosses the $s$ axis between $+0.003\ldots{+}0.012\,\text{m}$, and no line through the origin fits") is correct, but the model answer (solutions.md row 812) does not show it. The grader should not require it. Add it to the model answer or mark it as extra. Wording: "between $+0.003$ and $+0.012\,\text{m}$" reads better than "between $+0.003\ldots{+}0.012$".
- s7 c, rubric detail 3: $\tfrac{1.2}{30.0} \approx 4.1\,\%$ is arithmetically $4.0\,\%$. The solution (row 727) uses $1.22$, so write $\tfrac{1.22}{30.0}$. The result $\pm 0.6\,\text{cm}$ does not change.
- Carried from earlier rounds: the `### Yleisiä virheitä` and `### Hyväksytään myös` headings are Finnish in the en solutions. The interval $10.19\ldots10.48$ versus $10.35 \pm 0.15$ in s8 c: both are defensible.

## Checked
- Round-2 item 1 is fixed in the en tasks.json. s8 a criterion 5 no longer says "so it is not significant". It now says the term is small, the size of the reading uncertainty, that zero is excluded, and that it does not affect the slope because the line is not forced through the origin. Recomputed (scratchpad s8r2.py): intercepts of the admissible lines are $+0.0033\ldots+0.012\,\text{m}$, so the rounding to $0.003$ is right. The criterion agrees with the model answer, and the numbers are the same as in fi.
- s7 c, rubric detail 2: the chain is now an `aligned` block with real newlines ($4.5\,\text{N}/30.0\,\text{N/m} = 0.150\,\text{m} = 15.0\,\text{cm}$), with aligned rows and the same chain as the solution. Recomputed: $\Delta k = (31.27-28.83)/2 = 1.22\,\text{N/m}$, $\Delta x = 0.61\,\text{cm}$, $x_\text{min}/x_\text{max} = 14.4/15.6\,\text{cm}$.
- s7 b detail (when the line may be forced through the origin): correct physics and a faithful translation.
- Decimal points throughout. The unit fields are language-neutral.
- `practice.py check`: OK for en (8 tasks, 116 points). The hash is $2996fa9824b493d6$ at the start and at the end.
