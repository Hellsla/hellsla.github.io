VERDICT: PASS
CONTENT-HASH: 885be814ebf99534

## Blocking

## Polish
- exercises.json fy3-16-L3-01 — "water at 20 °C" is plain text, against the rule that every number with its unit is LaTeX (a house-rule item for the visual or pedagogy reviewer, not physics) — fix: `$20\,{}^\circ\text{C}$`.
- exercises.json fy3-16-L2-01 — the tolerance of 0.06 around 1.7 accepts 1.6, which the solution says "would not last the full six hours" — optional: tolerance 0.04.
- solutions.md fy3-16-L2-09 — "The assumption of no losses makes the true value slightly smaller" reads backwards — fix: "With losses, the true $c$ is slightly smaller than calculated."
- solutions.md fy3-16-L2-06 — "in a month like February" names a month, but the table has no months — fix: "in the month with $T_\text{out} = -8\,{}^\circ\text{C}$".

## Checked
- I recomputed all 19 numeric answers with my own formulas in one script. They agree with answers.py, which is the same file as fi-easy's, and with exercises.json within tolerance. The rounded-up minimums of L2-01 and L3-03 follow the task text.
- Every number, option and correct flag matches the fi-easy version, which I reviewed in the same session.
- L2-06: my least-squares slope is $-99.8\,\text{kWh/K}$, so $UA = 139\,\text{W/K}$, and the x-intercept is $20.1\,{}^\circ\text{C}$. The slope is read from points on the fitted line, not from raw points, as the guardrail asks.
- L3-02: the check that all the ice melts comes before the balance, and the case where ice is left is stated. $T = 8.06\,{}^\circ\text{C}$.
- L2-07 error analysis ($299\,\text{K}$ against $26\,\text{K}$, ratio $11.5$) and L2-08 (ratio 2, one correct option, each distractor's feedback right).
- L1-06 and L1-07: one correct option each, and the net-transfer and melting wordings are right.
- L2-05: the period efficiencies (82, 75 and 70 %) and the explanation that losses grow with the temperature difference.
- L3-04 ($5443\,\text{kWh}$, $480.6\,\text{€}$, break-even price $0.44\,\text{€/kg}$) and L3-05 ($592\,\text{kW}$, freezing $85\,\%$, the result as a lower limit).
- Figures heating-line and melting-curve give the needed grid values and state no answer.
- The exercise brief in the packet was empty, so notation was compared against the set itself and the fi-easy brief's model: consistent. Scope is FY3.
