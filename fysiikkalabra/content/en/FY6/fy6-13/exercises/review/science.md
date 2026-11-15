VERDICT: FAIL
CONTENT-HASH: 5404e1fb42f97550

## Blocking
- exercises.json:115 (fy6-13-L1-08) — A, assessment: the solution's own rounded answer $1.4 \cdot 10^{2}\,\text{mJ}$ (solutions.md:140, two significant figures, which is right because $6.0\,\text{V}$ and $18\,\text{V}$ have two) is $2.8\,\%$ from the stored answer 144. Tolerance 0.02 marks it only "close", so a student who rounds correctly is not accepted (CLAUDE.md: a student rounding to the data's figures stays inside the tolerance). — Set the tolerance to 0.03 (or more). Leave the answer as 144.

## Polish
- solutions.md:220 (L3-05 c) — the rounded intermediates do not give the result stated: $4.3^2 = 18.49$, not 18.4, and $18.4 : 2.7 = 6.8$, not 6.9. — Write $(60/14)^2 \approx 18.4$ and $5.6/2.1 \approx 2.67$, or use the fractions without rounding them.
- solutions.md:71 (L2-02) — "According to the table" refers to a table the task does not give. — Say "the MAFY table" or "a table of relative permittivities".
- exercises.json L1-10 / L3-05 — the same $\varepsilon_0$ is called "vacuum permittivity" in one task and "electric constant" in the other. — Use the lesson's one term.

## Checked
- I recomputed all 19 numeric answers in one script with my own formulas ($C = Q/U$, $C = \varepsilon_0\varepsilon_\text{r}A/d$, $U_\text{max} = E_\text{max}d$, $W = \tfrac12 CU^2$, least-squares slopes through the origin). Every one matches answers.py and exercises.json. Fits: $C = 47.2\,\mu\text{F}$ and $k = 100.0\,\text{V/s}$.
- Figures: the $(Q, U)$ line of ex-qu passes through $(60\,\mu\text{C};\ 12\,\text{V})$ on the grid lines, and ex-qu2 ends at $(120\,\mu\text{C};\ 8\,\text{V})$. Neither figure nor its description gives the answer away.
- Disconnected vs connected source: in L1-07 and L3-01, $Q$ stays constant; in L3-02, $U$ stays constant and $\Delta Q = (\varepsilon_\text{r}-1)C_1U$. The physics, the options and every feedback are correct, with exactly one correct option.
- L1-09: every true/false judgement and its feedback are right. The battery gives $QU$, half is stored, and the other half goes to internal energy of the resistor.
- L2-06: the largest current is where $\Delta U/\Delta t$ is largest ($I \propto \mathrm{d}U/\mathrm{d}t$). Charging is treated only qualitatively, with no exponential, as the scope requires.
- L3-03 and L3-05: the half-of-dielectric-strength safety margin is applied correctly ($d = 0.50\,\text{mm}$, $A = 217\,\text{cm}^2$). The rounding to $220\,\text{cm}^2$ errs on the safe side. Ratio 6.89, and $W \propto \varepsilon_\text{r}E_\text{max}^2$ is derived correctly.
- L3-04: $C = I/k = 150\,\mu\text{F}$, $243\,\text{J}$, $48.6\,\text{kW}$ and $18\,\text{s}$. The extrapolation is justified by the constant current, and the safety statement about stored charge is correct.
- Rounding follows P7: 120, 500, 200 and 2200 are taken as having three or more significant figures, and every reason names the datum that really limits the result. Every other rounded answer is within 2 %.
- Magnitudes are realistic (defibrillator, supercapacitor, Teflon and glass values) and the set stays in scope (no capacitor connections).
- The content hash was the same at the start and at the end.
