VERDICT: FAIL
CONTENT-HASH: 0da2cfcc91630694
SCOPE: delta: round 2, the fixes of round 1 in fy9-mittaaminen-s7 and -s8 (s8 solutions, rubric, answers.py, the s8-kuvaaja model graph); older tasks s1-s6 untouched (not re-judged).
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
1. **A, s8 a, round-1 item 2 is fixed only in the solution.** The en model answer now says: "It is small, and because the line is not forced through the origin, it does not affect the slope." This is correct. The 5th rubric criterion of a (tasks.json, tag `graph`) still reads "The constant term of the line is about $0.01\,\text{m}$, the size of the reading uncertainty, so it is not significant." I recomputed every line through all the $\pm 0.01\,\text{m}$ bars. Each crosses the $s$ axis between $+0.0033$ and $+0.012\,\text{m}$, so zero is excluded. The criterion awards a point for a wrong conclusion, and it contradicts the model answer. Reword it, for example: "The constant term (about $0.01\,\text{m}$) is small, the size of the reading uncertainty, and does not affect the slope because the line is not forced through the origin." The same item is open in fi and fi-easy.

## Polish
- The headings `### Yleisiä virheitä` and `### Hyväksytään myös` in the en solutions are still in Finnish. This is carried from round 1; it is fine if the renderer maps them to the English labels.
- s8 c: the interval $10.19\ldots10.48\,\text{m/s}^2$ (the limiting lines) differs slightly from $10.35 \pm 0.15$ ($10.20\ldots10.50$). Both are defensible.

## Checked
- Round-1 item 1 is fixed in the en solution c ("if the real frame interval is longer than the assumed $0.05\,\text{s}$, the times are underestimated and the calculated $g$ is too large"; $1.027 \cdot 0.05\,\text{s} = 0.0514\,\text{s}$, about $2.7\,\%$, lower frame rate), in the rubric `error_sources` detail and in answers.py `c-tscale` ($\sqrt{g/9.81}$). "Shorter than assumed" and $0.0487$ no longer appear.
- The polish is fixed: the substitution uses $2 \cdot 5.177\,\text{m/s}^2 = 10.35$, and so does the rubric detail.
- My script (scratchpad s8r2.py): least-squares slope $5.175$, intercept $0.0100\,\text{m}$, largest residual $0.008\,\text{m}$. Read slope $5.177$, limiting slopes $5.094$/$5.242$, $\Delta g = 0.147$, difference $0.54$ ($5.5\,\%$, $3.7\Delta g$), interval $0.0514\,\text{s}$. All match the en text, with the same numbers as fi and decimal points throughout.
- Precision: $(10.35 \pm 0.15)\,\text{m/s}^2$ and the check value $0.83\,\text{m}$ fit the data. The task text does not name $t^2$ (no structure revealed). Calculation chains are in aligned rows. The unit fields `N/m`, `cm` and `m/s^2` are language-neutral.
- The figure alt text matches the solution (slope $5.18$, intercept about $0.01\,\text{m}$, circled points). The physics wording of the fix is accurate.
- `practice.py check` OK for en (8 tasks, 116 points). The hash is the same at the start and the end.
