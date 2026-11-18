VERDICT: FAIL
CONTENT-HASH: a7fd1f4cabdc517a
SCOPE: delta: new tasks s7 (Calibrating a spring) and s8 (A steel ball dropped, filmed on video), the s8-kuvaaja model graph and the changed intro; older tasks s1-s6 untouched (not re-judged).

## Blocking
1. **A, s8 c, the frame-interval cause is backwards.** This is in the solution ("An error in the time scale ... $0.974 \cdot 0.05\,\text{s} = 0.0487\,\text{s}$") and in the rubric `error_sources` detail ("a frame interval about $2.6\,\%$ shorter than assumed"). We have $g = 2s/t^2$. If the real interval were shorter than the assumed $0.05\,\text{s}$, the assumed times would be too long and the computed $g$ too *small*. To turn a true $9.81$ into the measured $10.35\,\text{m/s}^2$, the real interval must be *longer*: $0.05\,\text{s} \cdot \sqrt{10.35/9.81} \approx 0.0514\,\text{s}$, about $2.7\,\%$ (frame rate about 19.5 instead of 20 per second). The same error is in fi, along with answers.py `c-tscale`.
2. **A, s8 a, "the constant term ... is not significant"** (5th criterion, model answer). Every line that passes through all the $\pm 0.01\,\text{m}$ bars (part b's own test) crosses the $s$ axis between $+0.003$ and $+0.012\,\text{m}$, and no line through the origin fits. The claim therefore contradicts the task's own method (s7 b uses it correctly). Say instead that the constant term is small, about the reading uncertainty, perhaps an offset in the distance zero. Since the line is not forced through the origin, the slope is not affected.

## Polish
- s8 b: "$g = 2 \cdot 5.18 \approx 10.35$". $2 \cdot 5.18$ is $10.36$. Show $5.177$ in the chain.
- In the en solutions file, the headings `### Yleisiä virheitä` and `### Hyväksytään myös` are left in Finnish. Check whether the renderer replaces them, or whether a student sees them.

## Checked
- Translation fidelity against fi, part by part, for s7 a-c and s8 a-c: the task texts, every criterion, the solutions, Common mistakes and Accept also. The numbers, units, points, answers and tolerances are identical, with decimal points used throughout. The physics wording is accurate (spring constant, extension, coils pressed together, elastic limit, extrapolation, acceleration of free fall). The text does not reveal the solution's structure: s8 asks for a graph whose slope gives $g$ but does not name $t^2$.
- The same recomputation script as for fi (the data from the fy5-8 and fy4-2 figure sources; answers.py side by side): s7 $k = 29.98\,\text{N/m}$, bounds $28.83$/$31.27$, $\Delta k = 1.22$, $x = 15.0 \pm 0.61\,\text{cm}$, intercept range $-0.20\ldots+0.27\,\text{cm}$. s8 slope $5.175$, intercept $0.010\,\text{m}$, bounds $5.094$/$5.242$, $g = 10.35 \pm 0.15$, difference $0.54$ ($5.5\,\%$, $3.7\Delta g$). All match the en text except items 1 and 2.
- The alt text of the s8-kuvaaja figure (en solutions) matches the solution: slope $5.18\,\text{m/s}^2$, intercept about $0.01\,\text{m}$, circled points.
- Intro: eight problems, two with a ready graph, one with the ideal gas law: true.
- `practice.py check` OK. The hash is the same at the start and the end.
