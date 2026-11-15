VERDICT: PASS
CONTENT-HASH: 9a9dc31c4b0b84b7

## Blocking

## Polish
- exercises.json L3-05 and L3-03 — these are limit answers with the same shared-check limitation as L2-05. In L3-05 the check accepts $7.7\,\text{A}$, which is above the maximum $7.61\,\text{A}$. In L3-03 it accepts $7.1\,\text{A}$, which is below the minimum $7.16\,\text{A}$. Neither can be fixed per task, because the check always accepts at least ±2 %. — Include L3-03 and L3-05 in the one-sided limit check proposed to the coordinator (P7c). Not blocking.
- solutions.md L2-05 — the step heading says "Reading the graph", but the task gives a table. — "Reading the table".
- solutions.md L3-02 — the reason for keeping $156\,\%$ is that "$10\,\text{A}$ and $16\,\text{A}$ are exact settings". The reason is defensible, but under P7(b) $10\,\text{A}$ has two significant figures, which would give $1.6 \cdot 10^{2}\,\%$. — Either keep it and say in the task that the settings are exact, or round. The check accepts both.
- solutions.md L2-04 — "about $3.5\,\text{W}$ per metre" is per metre of cable, counting both conductors. — Say so.

## Checked
- I recomputed all 20 numeric answers in one script with my own formulas: $W = (s_2 - s_1)W_\text{full}$, $P = UI$, $P = 3UI$, $t = W_\text{battery}/(\eta P)$, $P = RI^2$, $R = \rho \cdot 2l/A$, trapezoids, and the cost sums (the distances add up to $14\,640\,\text{km}$). Every one matches answers.py and exercises.json.
- L2-03 follows P7c: the limit $11.96\,\text{A}$ is rounded down to $11\,\text{A}$. The stored answer $11.478$ with tolerance 0.043 accepts $10.98\text{–}11.97\,\text{A}$, so both $11\,\text{A}$ and $11.96\,\text{A}$ pass and $12\,\text{A}$ fails, as intended.
- L2-05 follows P7c: the exact limit $17.25 - 6.8 = 10.45\,\text{kW}$ is rounded down to $10.4\,\text{kW}$. Part c is correct: only 19–20 h exceeds $6.25\,\text{kW}$. That the check also accepts $10.5\,\text{kW}$ is the known site-wide 2 % floor in templates/lesson.js, already raised with the coordinator.
- L3-03 rounds its minimum up ($7.16 \to 7.2\,\text{A}$), which is the safe direction. L3-05 rounds its maximum down ($7.61 \to 7.6\,\text{A}$). The cable dissipates $23.6\,\text{W}$ and $104\,\text{W}$, and the 33.4 A overload argument is correct.
- 230 V is treated as three significant figures (P7a), and each rounding reason names the datum that really limits the result. Every rounded answer stays within its tolerance, including L1-02 (2.2 % at tolerance 0.03) and L2-01 (1.8 %).
- L2-08: all four options are recomputed (15.3, 13.0, 11.1 and 5.1 h). Each distractor matches exactly the error its feedback names, and only one option is correct. L1-06 (kW vs kWh) has exactly one correct option, and every feedback is right.
- L2-06: both errors are identified correctly (the charge-level fraction and the efficiency). The correct time is $5.29\,\text{h}$.
- Figures: lataus-ex has grid lines at $11$ and $5.5\,\text{kW}$ and steps at 2.0 and 3.0 h, and talo-ex has steps of $2, 5, 7, 3\,\text{kW}$. Each gives exactly what its task needs, and the descriptions match the drawings.
- Models and assumptions are stated in the task texts: loads equally divided between the phases, constant power, the current returning along the neutral, and a socket in good condition. The safety statements are correct, and the set stays in scope.
- The content hash was the same at the start and at the end.
