VERDICT: PASS
CONTENT-HASH: a2a10722a2880277

## Blocking
None.

## Polish
1. tests/sims/fy3-7.json — Q = P·t is asserted only through the test helpers (`simSetTime`, assertion 31), never during a real animation run. Optional extra assertion: click Lämmitä with m = 0,1 and P = 3000, wait about 300 ms, then check `Math.abs(simState.Q - simState.P*simState.t) < 1e-6` and that both sliders are disabled. I verified this by hand, see Checked. Timing-sensitive in CI, so thin-but-fine as is.
2. tests/sims/fy3-7.json — no assertion that sliders unlock once the run ends at 130 °C. Verified by hand (see Checked); assertions 38-41 cover the locked state and the restart.

## Checked
- `PASS preview/fy3-7  [] []`
- Lint `lint_lesson.py fy3-7`: 0 errors, 0 warnings (not repeated). Hash before and after: a2a10722a2880277 (unchanged).
- Coverage vs sim-spec.md: every simState field (m, P, t, T, phase, Q, tMelt, tBoil, running, content) and both sliders (default, min/max/step, effect on simState) have assertions, as do both buttons, the readout text per phase, the note (60 s = 1 s, steam stays), the controls-before-readout order, the end stop at 130 °C (t capped at 207,67 s), the axis scale (tMax) and the label sweep at two extreme settings. 62 assertions.
- Boundaries: 188 000 J gives 'vesi' with T = 0; 187 999 J gives 'sulaa'; 1 527 500 J gives 'höyry' with T = 100. Each is correct for m = 0,5 kg.
- Formula in sim.js equals the lesson's: Q = c m ΔT per phase, sm and rm on the plateaus, constants 2100, 4190, 2000 J/(kg·K), 334 and 2260 kJ/kg, same as the constants table in lesson.md; plateau durations sm/P and rm/P.
- Independent reference model (my own piecewise T(Q)) against simState over 6 masses × 6 powers × 25 times spanning all five phases = 900 states at 360, 390 and 1280 px: 0 mismatches in T or phase, and Q = P·t every time.
- Layout sweep on the same 900 states per viewport (simLabels boxes): 0 intersections, 0 boxes outside the 600×400 canvas, no horizontal page overflow at 360, 390 and 1280 px.
- Real animation (m = 0,1 kg, P = 3000 W, Lämmitä): sliders disabled while running; after about 1 s t = 60,9 s (60× speed) and Q = P·t exactly; the run stops at 130 °C (t = 103,83 s), sliders unlock; a second click restarts from t = 0; Nollaa gives t = 0, T = −20, not running.
- No console or page errors at any of the three viewports.
