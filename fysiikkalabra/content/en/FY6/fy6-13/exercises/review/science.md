VERDICT: PASS
CONTENT-HASH: 5404e1fb42f97550

## Blocking

## Polish
- solutions.md:220 (L3-05 c): the rounded intermediates do not give the stated result. $4.3^2 = 18.49$, not 18.4, and $18.4 : 2.7 = 6.8$, not 6.9. Fix: write $(60/14)^2 \approx 18.4$ and $5.6/2.1 \approx 2.67$, or keep the fractions unrounded.
- solutions.md:71 (L2-02): "According to the table" points to a table the task does not give. Fix: say "the MAFY table" or "a table of relative permittivities".
- exercises.json:159 / :420 (L1-10, L3-05): the same $\varepsilon_0$ is called "vacuum permittivity" in one task and "electric constant" in the other. Fix: use the lesson's single term.

## Checked
- Round 1's blocking item on L1-08 is withdrawn. The built page (preview/en/fy6-13.html) has data-answer="144" data-tol="0.02" data-step="10". templates/lesson.js part 1 accepts max(2 %, tol, step/2) = ±5 mJ, so the range is 139–149 mJ and the correctly rounded $1.4 \cdot 10^{2}\,\text{mJ}$ is accepted. Under P7(b), $1000\,\mu\text{F}$ has four significant figures and the voltages have two, so two figures is the right rounding.
- I recomputed all 19 numeric answers in one script with my own formulas and compared them with answers.py and exercises.json. All agree (L3-05: 6.888 against 6.9, inside its 3 % tolerance). The fits give $C = 47.2\,\mu\text{F}$ and $k = 100.0\,\text{V/s}$, so $C = 150\,\mu\text{F}$.
- I checked every solution's rounded answer against the page's accept window (data-step from the built page). Each is accepted: 220 pF, 220 cm², 73 s, 63 mJ, 3.7·10² µJ, 1.5 µC, 49 kW, 3.7, 5.1 nF, 6.9.
- Rounding follows P7: 120 pF, 500 V, 200 J and 2200 µF are taken as having three or more significant figures. In L3-03 the minimum area 217 cm² is rounded up to 220 cm², the safe direction. In L2-01 the limit 320 V is exact.
- Disconnected versus connected source is handled correctly. In L1-07 and L3-01, $Q$ stays constant and $\Delta W = 15\,\mu\text{J}$ is the work of pulling the plates apart. In L3-02, $U$ stays constant and $\Delta Q = (\varepsilon_\text{r}-1)C_1U$. Each choice task has exactly one correct option, and every feedback is right.
- L1-09: every true/false judgement is correct. The battery gives $QU = 14.4\,\text{mJ}$, $7.2\,\text{mJ}$ is stored and the rest goes to internal energy of the resistor.
- L2-06: the current is proportional to $\Delta U/\Delta t$. The interval increments 3.5, 2.0, 1.4, 0.8, 0.5 and 0.3 V match the table and the feedback. Charging is treated only qualitatively, as the scope requires.
- L3-05: $W = \tfrac18\varepsilon_0\varepsilon_\text{r}E_\text{max}^2Ad$ is derived correctly. The values (Teflon 1500 V, 3.72 nF, 4.18 mJ; glass 350 V, 9.92 nF, 0.607 mJ) check out.
- Figures: ex-qu passes through (60 µC; 12 V) on the grid lines and ex-qu2 ends at (120 µC; 8 V). Neither figure nor its description gives the answer away.
- Magnitudes are realistic, the set stays in scope (no capacitor connections, no exponential), and the content hash was the same at the start and at the end.
