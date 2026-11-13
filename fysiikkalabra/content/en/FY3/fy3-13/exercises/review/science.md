VERDICT: PASS
CONTENT-HASH: 452c91f8e35f2872
SCOPE: delta added-exercise from daa6fc4f95361ced base 81db4a6fd727

## Blocking
(none)

## Polish
- content/en/FY3/fy3-13/exercises/solutions.md fy3-13-L2-10 Principle — it says "The points are on a straight line", while L2-09 now says "almost on a straight line". The task's own assumption (linear outside the range) covers this; for consistency, write "almost on a straight line" here too.
- exercises.json fy3-13-L1-09 — a tolerance of $4\,\%$ on an exact table value accepts about $-262\ldots-284\,{}^\circ\text{C}$ (carried over from the last report; not blocking).

## Checked
- L1-09: $T = \theta + T_0$ with $T_0 = 273.15\,\text{K}$ gives $\theta_0 = -273.15\,{}^\circ\text{C}$, the same as answers.py. The solution states correctly that no temperature is below this.
- L2-09: from the end points (0; 75) and (100; 102.5), $k = 0.275\,\text{kPa/}{}^\circ\text{C}$ and $\theta_0 = -272.7\,{}^\circ\text{C}$, the same as answers.py. My least-squares fit over all five points gives $k = 0.276$ and $\theta_0 = -272.1\,{}^\circ\text{C}$, so the end-point method is fair.
- L2-09 accepted range: the stated $-260\ldots-286\,{}^\circ\text{C}$ is the same as the $5\,\%$ tolerance ($-259.1\ldots-286.4\,{}^\circ\text{C}$). "Almost on a straight line" fits the data, whose steps are 7, 7, 7 and $6.5\,\text{kPa}$ per $25\,{}^\circ\text{C}$.
- L2-10: $\theta = -73.15\,{}^\circ\text{C}$ gives $p = 54.88\,\text{kPa}$ (the fit gives 54.91), the same as answers.py. The stated range 53–$57\,\text{kPa}$ lies inside the $5\,\%$ tolerance ($52.1\ldots57.6\,\text{kPa}$). The task states that linearity is assumed outside the measured range.
- Both checks against $p \propto T$ ($75 \cdot 200/273.15 = 54.9\,\text{kPa}$, slope $75/273.15 = 0.275$) are real, independent checks.
- The uncertainty statement ("about ten degrees or more" from $1\,\text{kPa}$ readings) is consistent: the slope uncertainty is about $5\,\%$, which is about $\pm 14\,{}^\circ\text{C}$.
- The figure's data and its description give every point, and neither gives the extrapolated value away.
- The hash was the same at the start and at the end.
