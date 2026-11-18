VERDICT: FAIL
CONTENT-HASH: 0ca9f52c9bb8edae
SCOPE: delta: round 2, the fixes of round 1 in fy9-mittaaminen-s7 and -s8 (s8 solutions, rubric, answers.py, the s8-kuvaaja model graph); older tasks s1-s6 untouched (not re-judged).
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
1. **A, s8 a, round-1 item 2 is fixed only in the solution.** The model answer now says what is true: the constant term is small, about the size of the reading uncertainty, and does not affect the slope. But the 5th rubric criterion of a (tasks.json, the criterion tagged `graph`) still gives a point for "Suoran vakiotermi on noin $0{,}01\,\text{m}$, ja se on lukemisen epävarmuuden suuruinen, joten se ei ole merkitsevä." My script checked every line that passes through all the $\pm 0{,}01\,\text{m}$ bars. Each one crosses the $s$ axis between $+0{,}0033$ and $+0{,}012\,\text{m}$. So the data do not show that the constant term is insignificant. The rubric now also contradicts the model answer. Reword the criterion to match the model answer, for example: "Vakiotermi (noin $0{,}01\,\text{m}$) on pieni, lukemisen epävarmuuden suuruinen, eikä vaikuta kulmakertoimeen, koska suoraa ei ole pakotettu origon kautta."

## Polish
- s8 c: the interval $10{,}19\ldots10{,}48\,\text{m/s}^2$ comes from the limiting lines ($2 \cdot 5{,}094$, $2 \cdot 5{,}242$), while the stated result $10{,}35 \pm 0{,}15$ gives $10{,}20\ldots10{,}50$. Either is correct. One sentence saying which one is used would prevent confusion.

## Checked
- Round-1 item 1 is fixed in the solution c, in the rubric `error_sources` detail and in answers.py `c-tscale` ($\sqrt{g/9{,}81}$): a real frame interval of $0{,}0514\,\text{s}$, about $2{,}7\,\%$ longer than assumed, so the frame rate is lower than nominal. The direction is right: $g = 2s/t^2$, and times that are underestimated make $g$ too large.
- The round-1 polish items are fixed: the chain uses $2 \cdot 5{,}177 = 10{,}35$, and "pituuskaava" no longer appears.
- My script (scratchpad s8r2.py) recomputed from the data: least-squares slope $5{,}175$, intercept $0{,}0100\,\text{m}$ and largest residual $0{,}008\,\text{m}$ (matches "enintään noin $0{,}008$"). The read slope is $5{,}177$, the limiting slopes $5{,}094$/$5{,}242$, $\Delta g = 0{,}147$, the difference $0{,}54$ ($5{,}5\,\%$, $3{,}7\Delta g$) and the interval $0{,}0514\,\text{s}$ ($2{,}7\,\%$). All agree with the text and answers.py.
- Precision: $10{,}35 \pm 0{,}15$ (two digits because the first digit of the uncertainty is 1) and $0{,}83\,\text{m}$ in the check are consistent with the data. The task text names no $t^2$ and does not reveal the structure. Calculation chains are in aligned rows. The unit fields are `N/m`, `cm`, `m/s^2`: language-neutral.
- The alt text of s8-kuvaaja (slope $5{,}18$, intercept about $0{,}01\,\text{m}$, circled points) matches the solution.
- `practice.py check` OK (8 tasks, 116 points). The hash is the same at the start and the end.
