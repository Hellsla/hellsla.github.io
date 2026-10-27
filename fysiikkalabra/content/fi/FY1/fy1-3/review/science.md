VERDICT: FAIL
CONTENT-HASH: e27a99b915476d03

## Blocking
- assets/sims/fy1/fy1-3/sim.js:124–131 (plot, new collision stacking) — when readings coincide the stack outgrows the plot: `step` is still sized from the per-bin count (3,3 px at n = 40), but the collision test raises a dot until it is a full diameter (8,6 px) from every earlier one, so identical readings stack ~9,9 px apart. At satunnaisvirhe 0 (a slider value, the natural "no random error" check) n ≥ 30 the column runs up through the T/mean labels, over the ramp and off the canvas (captured at n = 40: about six dots invisible, the scene covered) — the plot shows fewer dots than n and hides the true-value and mean markers. At exp-3's own initial state (n = 40, sat 0,05 s, sys 0) the top dots already overlap the $T$ label by 7–17 px (k = 1 and phone scale). — Place the dots first as integer levels by collision, then set `step = min(d + 1.5, (yB − 3 − yTop)/maxLevel)` from the real maximum level (or treat a dot as clear when its vertical gap ≥ step), so the stack always fits between baseline and yTop.

## Polish

## Checked
- Diff since PASS: sim.js plot stacking, solutions.md L2-01 and L2-02, inquiry.json sim `model`.
- Reproduced the new placement in Python for all sat (0…0,30), sys (−0,30…0,30), n (1…40), k = 1 and 1,76: overflow only for sat ≤ 0,05; screenshots at sat 0 and 0,05 confirm.
- Dot x positions remain exact readings; reading model, simState keys (mean, puoli, vir) unchanged.
- L2-01: $\varepsilon = 0{,}09/1{,}865 = 4{,}83\,\%$ → 4,8 %; new justification (about 5 %, exact half-range) is sound.
- L2-02: $\Delta L_\text{sys} = 10{,}67\,\text{mm}$ → 10,7 mm, symbol now distinct from the half-range.
- Sim `model` "monen lukeman": true (n = 2 gives 0,135 s < 0,15 s).
- Hash identical at start and end.
