VERDICT: PASS
CONTENT-HASH: 81de44efc34be42b
SCOPE: delta: round 3, the fixes of round 2 in fy9-mittaaminen-s7 and -s8 (s8 a rubric criterion 5, s7 c formula rows); older tasks s1-s6 untouched (not re-judged).
Round 3: delta against the version round 2 reviewed (fix round 2).

## Blocking
None.

## Polish
- s8 a, criterion 5 now gives the range of the axis crossing ($+0{,}003\ldots{+}0{,}012\,\text{m}$) and says no line through the origin fits. This is correct, but the model answer (solutions.md row 812) does not show it. A grader should give the point for "small, about the size of the reading uncertainty, does not affect the slope" without the range. Either add the sentence to the model answer or mark the range as extra information.
- s7 c, rubric detail 3: $\tfrac{1{,}2}{30{,}0} \approx 4{,}1\,\%$ is arithmetically $4{,}0\,\%$. The solution uses $\tfrac{1{,}22}{30{,}0} = 4{,}07\,\%$. Write $1{,}22$ in the rubric too. The result $\pm 0{,}6\,\text{cm}$ does not change.
- Carried from round 2: s8 c, the interval $10{,}19\ldots10{,}48$ versus $10{,}35 \pm 0{,}15$. Both are defensible.

## Checked
- Round-2 item 1 is fixed. In tasks.json, s8 a criterion 5 no longer says "ei ole merkitsevä". It now says the constant term is small, that every line through all the $\pm 0{,}01\,\text{m}$ bars crosses the $s$ axis at $+0{,}003\ldots{+}0{,}012\,\text{m}$ (I recomputed $+0{,}0033\ldots{+}0{,}012$ in scratchpad s8r2.py, so the rounding is right), and that it does not affect the slope because the line is not forced through the origin. The criterion agrees with the model answer.
- s7 c: the substitution chain in rubric detail 2 is now a real `aligned` block with newlines and aligned rows ($4{,}5/30{,}0 = 0{,}150\,\text{m} = 15{,}0\,\text{cm}$). It is the same chain as in the solution. Recomputed: $\Delta k = (31{,}27 - 28{,}83)/2 = 1{,}22$, $\Delta x = 0{,}61\,\text{cm}$, $x_\text{min}$/$x_\text{max}$ $14{,}4$/$15{,}6\,\text{cm}$.
- s7 b, detail: "forcing through the origin is justified here, but not when the constant term stands out" is correct physics.
- s8 recomputation is unchanged from round 2: slope $5{,}175$/$5{,}177$, bounds $5{,}094$/$5{,}242$, $g = 10{,}35 \pm 0{,}15$, $0{,}0514\,\text{s}$.
- `practice.py check`: OK (8 tasks, 116 points). The hash is $81de44efc34be42b$ at the start and at the end.
