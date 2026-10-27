VERDICT: FAIL
CONTENT-HASH: 1b4acbfbd706de7c

## Blocking
- inquiry.json:377 — tarkistus-2 mistake `value: 4.0` says "Vaihdoit kulmakertoimen ja vakiotermin", but swapping k and b gives s = 4,0 t + 3,0 → t = (25 − 3,0)/4,0 = 5,5 h, not 4,0.  — Set the value to 5.5 for this feedback, or keep 4.0 with feedback that the student gave the constant term b (4,0 km) instead of solving for t.
- inquiry.json:362/381 — tarkistus-2 is a *pyöräretki* at 3,0 km/h for 7 h, and its own reasonableness check says "Vauhti 3,0 km/h on kävelyn luokkaa": the check exposes an unrealistic magnitude instead of confirming it. — Make it a walk/hike (patikkaretki), or scale the data to cycling speed (e.g. 15 km/h) and update answer, hints, mistakes and solution.

## Polish
- inquiry.json ennuste-2 wrong option 1 — "Jos suora pakotetaan origon kautta, d ≈ 61 g" holds only with k locked at 0,80 g/ml (as in koe-2); say "kulmakertoimella 0,80 g/ml".
- solutions.md fy1-4-L3-03 — "kaksi merkitsevää numeroa kuten lukemavirheessä": δ = 0,1 has one; the ratio 16 = 8,0/0,5 is exact from the x-values. Justify from Δx.
- solutions.md fy1-4-L3-01 — state that the extrapolation to t < 0 assumes the cart moved at the same speed before the clock started.

## Checked
- All 12 exercise answers recomputed independently; all match answers.py within tolerance (L2-04 1,758 → 1,8 inside 3 %).
- Sim RMS values: D1 k = 0,30/0,50/0,60 → d = 0,76/0,12/0,44 m; D2 k = 0,80, b = 0 → 61 g, best b = 61,3 g → d ≈ 1,2 g; LS 0,787 g/ml, 62 g.
- D3 with b = 80 locked: min d = 5,80 °C (k ≈ −1,90); LS residuals + − − − − + +, so the "ends above, middle below" pattern is true.
- Experiments lock aineisto and b or k; simState gives d. Siirto 20 vrk, tarkistus-2 7,0 h, exit-ticket k = 1,5 m/s, b = 2,0 m; feedback numbers correct.
- Worked example: 8,0 °C/min, 20 °C, 2,5 min; LS fit 7,85 °C/min, 20,5 °C confirms the eye fit; residuals ≤ 0,8 °C.
- SVG figures measured: scatter points equal D1 and line s = 0,5 t (3 above, 3 below); slope figure k = 0,5, b = 1, P1 (2, 2), P2 (8, 5); kettle points, line and 2,5 min all to scale.
- sim.js: RMS and least-squares formulas correct; limits stated; FY1 scope.
