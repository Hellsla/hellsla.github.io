VERDICT: PASS
CONTENT-HASH: d7c7d0d3dad93aab

## Blocking

## Polish
- assets/sims/fy1/fy1-3/sim.js:124–131 (plot) — at satunnaisvirhe 0 and n = 40 the squeezed column (≈3,2 px per dot, d = 8,6 px) no longer lets the eye count the dots; the readout carries n, so nothing is wrong — optionally print the count of identical readings beside a column taller than the plot.

## Checked
- Round-4 diff: sim.js stacking only (collision levels first, then step = min(d + 1,5, (yLow − yHigh)/maxLv)); rest passed in round 3.
- Preview driven in Playwright at 1280 and 390 px for sat 0, 0,05, 0,15, 0,30; sys −0,30, 0, +0,30; n = 2, 10, 40: dotTop (simState) always ≥ 202,75 (k = 1) / 214 (phone), below the $\bar t$ label bottom (194,8 / 206,0).
- Screenshots sat 0, sys +0,30, n = 40 (1280) and exp-3 state sat 0,05, n = 40 (390): all 40 dots on the canvas, none over the ramp, the $ or $\bar t$ labels.
- Dot x positions still the exact readings; mean and $ markers unchanged; simState keys (mean, puoli, vir) unchanged.
- Hash identical at start and end.
