VERDICT: PASS
CONTENT-HASH: 097ebcd0ca9722b8

## Blocking

## Polish
- solutions.md fy3-16-L2-09 — "The assumption of no losses makes the true value slightly smaller" reads backwards — fix: "With losses, the true $c$ is slightly smaller than calculated."
- solutions.md fy3-16-L2-06 — "in a month like February" names a month, but the table has no months — fix: "in the month with $T_\text{out} = -8\,{}^\circ\text{C}$".

## Checked
- Round 2 fix: L2-01 (1.7 kg) and L3-03 (1.6 kg) now have tolerance 0.04. The accepted ranges are 1.632–1.768 and 1.536–1.664. The rounded-down 1.6 (−5.9 %) and 1.5 (−6.3 %) are rejected, which matches "Round your answer up so that the ice is sure to last" and the solutions' "would not last". answers.py rounds up with `math.ceil`.
- I recomputed all 19 numeric answers with my own formulas in one script. They agree with answers.py, the same file as fi-easy's, and with exercises.json within tolerance. Every answer, tolerance, unit and correct flag is the same as in the fi-easy version, which I reviewed in the same session.
- L2-06: least-squares slope $-99.8\,\text{kWh/K}$, so $UA = 139\,\text{W/K}$. The x-intercept is $20.1\,{}^\circ\text{C}$. The slope is read from points on the line, not from raw points.
- L3-02: the check that all the ice melts comes first, and $T = 8.06\,{}^\circ\text{C}$. The case where ice is left is stated.
- L2-07 (ratio 11.5) and L2-08 (ratio 2, one correct option, the distractors' feedback is right).
- L1-06 and L1-07: one correct option each. The net-transfer and melting wordings follow the guardrails.
- L2-05: the period efficiencies 82/75/70 % and the explanation of the losses are right.
- L3-04 ($5443\,\text{kWh}$, $480.6\,\text{€}$, break-even $0.44\,\text{€/kg}$) and L3-05 ($592\,\text{kW}$, freezing $85\,\%$, a lower limit).
- L2-10: the graph's 220 kJ and the exact 220.6 kJ both lie inside the tolerance.
- The exercise brief in this packet is empty again, so I compared the notation against the set and the fi-easy brief: it is consistent. Scope is FY3.
