VERDICT: PASS
CONTENT-HASH: 657ad8e418c9b0a6

## Blocking

## Polish
- solutions.md:165 (fy6-7-L2-06 Reading the table) — "The differences are positive, so the meter works correctly" is not a valid inference (a cumulative meter's differences are always positive; positivity proves nothing about accuracy) — drop the sentence or say only that every day's energy is of the same size, $7\,\text{kWh}$–$9\,\text{kWh}$.
- lessons/FY6/fy6-7/figures.py dryer — the cooling phase $0.2\,\text{kW}$ lies halfway between the $0.4\,\text{kW}$ grid lines the solution says the values are read from; the reading is still unambiguous, but a $0.2\,\text{kW}$ minor grid (as in washer) would match the solution's wording.
- lessons/FY6/fy6-7/figures.py washer, dryer — phase labels (`lämmitys`, `pesu`, `linkous`, `kuumennus`, `kuivaus`, `jäähdytys`) are Finnish; check the English figure shows English labels (visual reviewer's call).
- exercises/review/packet-science.md — the exercise brief is empty, so notation was compared with the glossary and the solutions only.

## Checked
- All 21 numeric answers recomputed in one script with my own formulas ($E = Pt$, $P = UI$, $I = U/R$, $K = aE + K_\text{base}$, period-by-period cost, payback $T = H/(a\Delta E)$): all agree with exercises.json and answers.py.
- L2-07: least-squares line through the origin gives $1.639\,\text{kWh}$ at $48\,\text{h}$ and $299\,\text{kWh}$ a year; the stored $299.3$ (read $1.64$) is well inside the $5\,\%$ tolerance; the origin constraint has its physical reason (reading $0.00$ at $t = 0$).
- L2-06 daily differences $7.7 \ldots 7.4\,\text{kWh}$, sum $56.3\,\text{kWh}$, $335\,\text{W}$, $9.0\,\text{€}$; L3-04 costs sum $267.44\,\text{c}$, $19.0\,\text{kWh}$, $14.08\,\text{c/kWh}$, saving $93\,\text{c}$; L3-05 gain $77.1\,\text{€}$ ($16\,\%$).
- P7: L1-03 answer $5.22\,\text{A}$ to three s.f. because $230\,\text{V}$ has three; L2-05 two s.f. limited by $90\,\text{W}$, $60\,\text{W}$ and the times, consistent with trailing zeros significant.
- L1-06: one correct option (energy); each distractor's feedback right. L1-09: every distractor value reproduces its stated unit error ($0.0010$, $3.6$, $60$, $3600\,\text{kWh}$).
- L1-03 principle: mains $230\,\text{V}$ is an effective value, valid for a resistive heater (C-level, correct).
- L3-05 c: an old fridge's waste heat offsetting electric heating is a correct, real model limitation.
- Figures washer, dryer: plotted steps match the solutions' readings ($0.80\,\text{kWh}$, $2.5\,\text{kWh}$); alt texts carry the same values; no energy written on them.
- Scope: electric power and household energy in kWh, bill and saving, matching the slot and FY6 contents; magnitudes realistic.
- Every solution has given, principle, symbolic formula, conversions, substitution, justified rounding and a real check.
