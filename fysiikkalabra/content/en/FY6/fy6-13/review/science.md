VERDICT: PASS
CONTENT-HASH: d3bbbfc30db75858

## Blocking
- none

## Polish
- lang/en.json:2014 (sims.fy6-13.lukemat_lap) — "values calculated with the ideal model before breakdown" does not quite describe what is shown: during connected breakdown the readout shows $Q = CU_0$ and $W = \tfrac12 CU_0^2$ at the set voltage, which is above the breakdown voltage. For example, at d = 1.0 mm in air with $U_0 = 3.1\,\text{kV}$ it shows 549 nC and 851 µJ, while the largest values before breakdown (3.0 kV) are 531 nC and 797 µJ — say "ideal-model values at this voltage, as if no breakdown happened". Not blocking: the mallirajaus note says the model no longer holds.

## Checked
- sim.js:81: `lukemat_lap` is chosen only when `S.lap && !S.burnt` (connected source, E > E_max). When disconnected, breakdown still discharges to Q = 0 and shows `purkautui-teksti`. The model and `simState` are unchanged (Q, W, lapilyonti keys are the same).
- The breakdown readout still shows C, U, E and E_max. The breakdown text and the mallirajaus note are still added, so the model's limit is stated at the point of use.
- Recomputed (experiment 5): C = ε0A/d = 177 pF; breakdown starts at U0 > 3.0 kV (E > 3 MV/m, strict inequality in code); Q and W as above.
- fi and fi-easy strings say the same as en.
- No other content changed since the last PASS (git diff); content hash the same at start and end.
