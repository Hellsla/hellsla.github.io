VERDICT: PASS
CONTENT-HASH: 38b2c5ddb83972d4

## Blocking

## Polish
- exercises.json L3-05 vs L1-05 — "a green LED" is $2.00\,\text{V}$ at $9.8\,\text{mA}$ in L3-05 but $2.2\,\text{V}$ at $10\,\text{mA}$ in L1-05. Real LEDs do differ, but a reader may look for one value. — Say "another green LED" in L3-05, or leave it.
- solutions.md L1-06 — "(at most about $1\,\text{V}$)" holds for a silicon diode, not for an LED. — Write "(for a silicon diode about $0.7\,\text{V}$)".
- answers.py:812–813 — the answers of the multiple-choice tasks L1-06 and L1-07 are the Finnish option texts. That is harmless for checking, because those answers are not numeric. — None needed unless the lint compares strings per language.

## Checked
- I recomputed all 19 numeric answers in one script with my own formulas: $U = RI + U_\text{D}$, $P = UI$, $\eta = P/(GA)$, $E = Pt$, the maximum of $UI$ over the tables, and the load line against linear interpolation of the table. Every one matches answers.py and exercises.json.
- The figures match their tasks. In ex-led the curve passes $(2.2\,\text{V};\ 10\,\text{mA})$ exactly. In ex-kenno $I(4.0\,\text{V}) = 198.7\,\text{mA}$, so reading $200\,\text{mA}$ and $0.80\,\text{W}$ is correct. The figure's model gives $P_\text{max} = 0.92\,\text{W}$, as solution L2-09 states. Neither figure gives the answer away.
- L3-05 checks out: threshold $2.00\,\text{V}$ (slope $420\,\text{mA/V}$) and operating point $2.02\,\text{V}$, $13.8\,\text{mA}$ (below $25\,\text{mA}$). In part c the voltage changes by $0.10\,\text{V}$ while the current grows more than fourfold.
- L3-04 checks out: $\sum H = 1027\,\text{kWh/m}^2$, $4683\,\text{kWh}$ produced and $87.7\,\%$ self-sufficiency. The six deficit months need $2517\,\text{kWh}$ ($47\,\%$). "At least this share is bought" is the right conclusion without storage. The data are labelled example data and are realistic for Finland.
- L2-06 data are internally consistent: $U/I$ matches each load resistor to within $2\,\%$. L3-02 is consistent too: the maximum is $49.3\,\text{W}$ at $5.86\,\Omega$, and the reason given for two significant figures is sound.
- L1-06, L1-07 and L2-08 (with its reasons) each have exactly one correct option. Every distractor is really wrong, and its feedback says why. Conventional current runs from + to −, and the anode on the + side means forward direction. The parallel branches are treated as independent circuits.
- L2-01 states the assumption of no reverse current. The reasonableness note on the reverse-voltage rating is a correct safety remark.
- Every answer rounded as its solution rounds it stays within the tolerance (largest deviation $2.0\,\%$ in L1-08, tolerance 0.03). The rounding reasons name the limiting datum, consistent with P7.
- The set stays in scope: components only, no p–n microphysics, and efficiencies, currents and powers are realistic.
- The content hash was the same at the start and at the end.
