VERDICT: PASS
CONTENT-HASH: 3b1b29439e94b105

Round 2 tester review of fy3-3 (gas particle sim). No blocking failures.

1. Gate/test runner: `python scripts/gate.py --hash fy3-3` = 3b1b29439e94b105 (expected). `test_sims.py fy3-3` run 3 times, raw output each time: `PASS preview/fy3-3  [] []` (no console errors, no failed assertions).
2. Assertion coverage (tests/sims/fy3-3.json, 16 assertions, spec covered): theta = T - 273,15 at 300 K and 600 K (lines 2, 13); defaults T=300, V=1,0; speed sqrt(2) at 600 K and sqrt(1/3) at 100 K; pTheory formula; pressure 600 K > 2x 150 K; 0,5 dm3 > 2x 2,0 dm3; pRel within 30 % of theory at 300 K/1,0 dm3; readout text; canvas 600x400; slider units K and dm3; N = 80. No missing assertions.
3. Console/page errors at 1280, 390, 360, 320 px: none (raw: `1280 errors [] ... 320 errors []`). No horizontal scroll (scrollWidth = innerWidth at all widths). Canvas stays 600x400 internally (CSS-scaled 574/324/294/254 px wide).
4. theta = T - 273,15 and speeds: at nine (T,V) combos theta error 0.0 and speedCheck/(120*sqrt(T/300)) = 1.0 exactly (sim.js:66, speed at sim.js:25).
5. Pressure vs simState.pTheory after 3 s settling. Mean of 40 samples over 8 s (relative deviation measured/theory): 300 K/1,0: mean 0.000, sd 0.047, max 0.122; 600 K/0,5: -0.012, sd 0.03, max 0.073; 100 K/0,5: -0.008, max 0.103; 450 K/1,5: -0.011, max 0.146; 600 K/2,0: -0.016, max 0.187; 300 K/2,0: -0.017, sd 0.10, max 0.19; 100 K/2,0: +0.020, sd 0.171, max 0.388. No systematic offset (effective-box fix at sim.js:57-59 works; means within 2 % of theory). 
6. Non-blocking observation: instantaneous pRel (1,5 s window, sim.js:16,54-60) fluctuates more at low collision rate, i.e. large V and low T. At 100 K/2,0 dm3 45 % of samples deviate more than 15 % from theory (max 39 %); at 300 K/2,0 15 %. Statistical noise, no bias; sim.js:38 note tells students it varies. Optional: larger WINDOW (e.g. 150 frames) would calm it. Not a failure.
7. Particles stay inside the box after V reduced 2,0 -> 0,5 (sim.js:50 clamps to the piston): pixel scan of the canvas found 0 of 2749 particle pixels outside the effective box.
8. Deterministic start: fixed p.randomSeed(7) (sim.js:29); three fresh loads give identical first-frame state [pRel 0, speedCheck 120].
9. Thermometer labels (sim.js:81-82): not clipped at 1280 or 320 px; ink bbox inside canvas (x 459-573 of 600, y up to 398 of 400 at 320 px; bottom "T K" label is tight, 2 px margin, but fully visible in screenshot). Labels left-aligned of tube, scale 600 K / 100 K visible at T=100 and 600.
10. Readout (DOM, sim.js:63-65): "T = 300 K = 27 °C"; at 100 K/0,5: "T = 100 K = −173 °C ... teoria 67"; mean-speed line "0,71 × 300 K:n keskinopeus" at 150 K. Slider labels: "Lämpötila T = 300 K", "Tilavuus V = 1,0 dm³".
11. Hash re-run at end: 3b1b29439e94b105 (unchanged).
