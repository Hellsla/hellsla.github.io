VERDICT: PASS
CONTENT-HASH: 69d3219159d1724e

## Blocking

## Polish
- exercises.json:294 (fy6-9-L3-01) — `"unit": "kertaa"` is the Finnish word in the English set — use `"times"` or `""` as fy6-1-L3-02 does.
- solutions.md:120 (fy6-9-L3-03 Reasonableness) — "the loss is a few percent": $3.24\,\text{kJ} : 43\,\text{kJ} \approx 7.5\,\%$ — say "about $8\,\%$" or "under a tenth".
- solutions.md (fy6-9-L3-04 c) — the internal resistance from the two discharges' mean voltages assumes the same mean source voltage, though the discharges end at different depths ($2.6\,\text{Ah}$ vs $2.4\,\text{Ah}$); the task states the assumption, so this is C, but the answer could call $0.10\,\Omega$ an estimate.
- exercises/review/packet-science.md — the exercise brief is empty, so notation ($W$ for energy, $E$ for source voltage, $R_\text{s}$, $U_\text{ch}$) was checked against the glossary and internal consistency only; it is consistent throughout the set.

## Checked
- All 19 numeric answers recomputed in one script with my own formulas ($Q = It$, $W = UQ$, loop law $I = (U_\text{ch} - E)/(R + R_\text{s})$, trapezoid energy sum, least-squares slope, $R_\text{s} I^2 t$, staged charging): all agree with exercises.json and answers.py.
- L2-07: least-squares slope $2.5\,\text{A/V}$ gives $R_\text{tot} = 0.40\,\Omega$, intercept $E = 12.39\,\text{V}$; the solution's line readings $(13.0\,\text{V};\ 1.5\,\text{A})$, $(14.6\,\text{V};\ 5.5\,\text{A})$ lie on the fitted line, slope read from the line not raw neighbours (guardrails).
- L3-05: stage currents $4.75$, $4.25$, $3.75\,\text{A}$, total $7.12\,\text{h}$, bounds $6.0\,\text{h}$ and $8.6\,\text{h}$ correct.
- L3-04: $\eta = 77\,\%$ (large current), $87\,\%$ (small), $R_\text{s} = 0.10\,\Omega$, $E = 3.75\,\text{V}$ at both currents.
- L1-07: charging current inside the battery from + to −, correct; every distractor wrong and its feedback right.
- L1-06, L1-09: exactly one correct option; unit analysis ($\text{V}\cdot\text{Ah} = \text{Wh}$; $UQt$ double-counts time) right; "a battery does not store charge" consistent with the glossary.
- L2-06: the loss $(U_\text{ch} - E)It = 1.5\,\text{Wh}$ cross-checked with $R I^2 t$; constant voltages stated in the task.
- P7: L1-02 four s.f. from $3000\,\text{mAh}$ (trailing zeros significant); every student rounding stays within tolerance.
- Figures ex-current, ex-current2: steps match the solutions' readings ($4.0\,\text{Ah}$, $5.5\,\text{Ah}$); alt texts carry the same values, no answer shown.
- Scope: battery capacity (Ah, Wh), charging circuit with the loop law, efficiency; all in FY6 contents; magnitudes realistic (e-bike $0.47\,\text{kWh}$, laptop $61\,\text{Wh}$).
