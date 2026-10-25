VERDICT: PASS
CONTENT-HASH: fc5375c46d696bd5

Round 2 tester review of fy3-1 (sim.js, sim-spec.md, tests/sims/fy3-1.json). Hash checked at start and at end: fc5375c46d696bd5 both times (matches expected). preview/fy3-1-sim.js is byte-identical to content/FY3/fy3-1/sim.js (cmp).

1. Official sim test (`PW_CHROMIUM=... python scripts/test_sims.py fy3-1`), run at start and again at the end:
   `PASS preview/fy3-1  [] []` (no console errors, simState present, all 18 assertions hold).

2. Independent Playwright run (own script, headless Chromium 1243, 1280x900), no console errors or page errors (`errs == []`).

3. G = m g (sim.js:41, simState at sim.js:47). 4 bodies x masses 1, 7, 10, 33, 50, 100 = 24 combinations. G == m*g to 1e-9, simState.g equals 1,62 / 3,71 / 9,81 / 24,8, simState.body equals the select value. 0 failures.

4. Mass independent of body: simState.m equals the slider value in all 24 combinations. 0 failures.

5. Stretch (sim.js:42): simState.stretch == 190*G/2480 for all 24 combinations (0 failures). It is strictly increasing with mass for each body (1..100 kg) and strictly increasing Kuu < Mars < Maa < Jupiter for each mass. So it changes with BOTH the mass slider and the select. The earlier defect (stretch ignoring the mass slider) is fixed.

6. Bars (sim.js:46, exposed as simState.bars): bars[i] == m*g_i/2480*220 for all four bodies in all 24 combinations. Proportional to G, change with the slider. The chosen body does not change the heights (by design: the chart compares the same mass on all four bodies; the select only changes the highlight, sim.js:75). Full scale (100 kg Jupiter): bar 220 px, stretch 190 px.

7. Drawing at the extremes (screenshots checked): 100 kg Jupiter, spring and block (bottom about y=346 incl. arrow) stay inside the 600x400 canvas, bar 2480 N reaches the top region below the title, labels legible. 1 kg Kuu: spring at rest length (rest line matches), 2 px minimum bars visible, labels "1,6 N / 3,7 N / 9,8 N / 24,8 N" present.

8. DOM readout (sim.js:44-45), e.g. at 100 kg Jupiter: `Massa m = 100 kg (sama kaikkialla)g = 24,80 N/kg (Jupiter)G = m · g = 2480,0 N`. Verified for all four bodies at 37 kg: m, g with decimal comma, and G = m · g formatted correctly.

9. Select options: `['Kuu', 'Mars', 'Maa', 'Jupiter']`. Canvas 600x400. Slider label text `Massa m = 100 kg` (unit kg present). Slider min 1, max 100 (test line 16).

10. Assertion coverage versus sim-spec.md (tests/sims/fy3-1.json): 18 assertions on window.simState (>= 3 required).
    - G = m g and values on all four bodies (lines 2-8), mass independent of body (line 6), readout text (line 9), select options (line 10), canvas size (line 11), slider unit (line 12), slider range (line 16).
    - Stretch grows with mass (line 13), stretch/G constant across bodies and masses (line 14), stretch ordered across bodies (line 15).
    - Bars proportional to G (line 17), full scale fits the chart (line 18).
    All spec points are covered. No missing assertions, so nothing to paste.

Non-blocking observations (no action required):
- tests/sims/fy3-1.json:6 checks "mass independent of body" only for the Kuu 5 kg state; the default-state and Kuu checks together with my 24-combination run confirm it. An optional extra assertion would be m equal to the slider on every body, but the spec is already covered.
- At 1 kg the bars are only the 2 px minimum height (documented in sim-spec.md), so the very smallest weights are visible only through their value labels.
