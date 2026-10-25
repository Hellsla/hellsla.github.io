VERDICT: PASS
CONTENT-HASH: 9c6ecf76a631b766

Hash checked at start and at end (`python scripts/gate.py --hash fy3-3` -> 9c6ecf76a631b766 both times). preview/fy3-3-sim.js is byte-identical to content/FY3/fy3-3/sim.js. No lesson file, sim.js, script or tests/sims/fy3-3.json was edited.

## Committed test, three runs (PW_CHROMIUM=/opt/pw-browsers/chromium-1243/...)
```
== run 1
PASS preview/fy3-3  [] []
== run 2
PASS preview/fy3-3  [] []
== run 3
PASS preview/fy3-3  [] []
```
tests/sims/fy3-3.json has 11 assertions (lines 2-13). The timing-based ones (lines 8, 9, 10) are stable. Margins are large: line 8 and 9 expect ratio > 2 (theory 4, measured about 4). Line 10 needs |p/theory - 1| < 0.3. In 12 extra trials with different preceding states, the ratio was 0.96-1.15 (see finding 3).

## Independent Playwright checks (own script, 1280 px unless noted)
1. No console or page errors in any run, including 320, 360, 390 px viewports and all slider changes: `ERRORS: []`.
2. theta = T - 273,15 checked at T = 100, 200, 300, 450, 600 (simState.theta = -173.15, -73.15, 26.85, 176.85, 326.85): PASS.
3. Particle speed. I hooked the canvas 2D context to record all 80 drawn particle positions every frame and compared the per-frame step with V_REF*sqrt(T/300)/60. Result: the max step equals the expected step exactly at all 5 temperatures. 98-99 % of steps are exactly equal; the rest are wall-clamp frames, which are shorter. simState.speedCheck and vRel match too:
```
T=100 expected step=1.15470 frac equal=0.992 max=1.15470 speedCheck=69.282032 exp v=69.282032 vRel=0.577350
T=200 expected step=1.63299 frac equal=0.989 max=1.63299 speedCheck=97.979590 exp v=97.979590 vRel=0.816497
T=300 expected step=2.00000 frac equal=0.987 max=2.00000 speedCheck=120.000000 exp v=120.000000 vRel=1.000000
T=450 expected step=2.44949 frac equal=0.984 max=2.44949 speedCheck=146.969385 exp v=146.969385 vRel=1.224745
T=600 expected step=2.82843 frac equal=0.982 max=2.82843 speedCheck=169.705627 exp v=169.705627 vRel=1.414214
```
   (All 80 particles are checked through the drawn positions; simState.speedCheck itself only covers particle 0, see finding 4.)
4. Pressure 3 s after a change, measured / theory (pTheory = 100*(T/300)/V):
```
T=300 V=1   meas=103.4 theory=100.0 ratio=1.03
T=100 V=1   meas=33.9  theory=33.3  ratio=1.02
T=150 V=1   meas=50.9  theory=50.0  ratio=1.02
T=200 V=1   meas=68.2  theory=66.7  ratio=1.02
T=450 V=1   meas=159.1 theory=150.0 ratio=1.06
T=600 V=1   meas=205.4 theory=200.0 ratio=1.03
T=300 V=0.5 meas=213.9 theory=200.0 ratio=1.07
T=300 V=2   meas=42.5  theory=50.0  ratio=0.85
T=600 V=0.5 meas=427.0 theory=400.0 ratio=1.07
T=100 V=2   meas=10.6  theory=16.7  ratio=0.64   (see finding 2)
```
   p scales with T and 1/V within 30 % except the one corner case in finding 2.
5. Particles stay in the box. V 2,0 -> 0,5 at 600 K, every particle position in every frame from the first frame after the change: x in [44, 136], y in [84, 276] = exactly the allowed [BOX.x+R, right-R] x [top+R, bottom-R]. PASS.
6. Deterministic start: three fresh loads give identical first-frame positions of all 80 particles (first particle (206.2998, 199.9937)): PASS.
7. Readout DOM text at 300 K / 1,0: `'T = 300 K = 27 °C\nHiukkasten keskinopeus: 1,00 × 300 K:n keskinopeus\nPaine p ≈ 111 (suhteellinen, 100 = 300 K ja 1,0 dm³), teoria 100'`. At 100 K / 0,5: `T = 100 K = −173 °C ... 0,58 × ... teoria 67`. At 600 K / 2,0: `T = 600 K = 327 °C ... 1,41 × ... teoria 100`. Decimal commas, Finnish minus sign: OK.
8. Canvas width/height 600x400 (style 600px x 400px). Slider labels `['Lämpötila T = 300 K', 'Tilavuus V = 1,0 dm³']`. Range attributes `[['100','600','10'],['0.5','2','0.1']]`. N = 80. All match the spec.
9. Viewports (scrollWidth == clientWidth, sliders 40 px high, nothing wider than the viewport):
```
320 {'sw': 320, 'cw': 320, 'canvas': 254, 'sl': [[254, 40, 287], [254, 40, 287]]}
360 {'sw': 360, 'cw': 360, 'canvas': 294, 'sl': [[294, 40, 327], [294, 40, 327]]}
390 {'sw': 390, 'cw': 390, 'canvas': 324, 'sl': [[324, 40, 357], [324, 40, 357]]}
```
   Screenshot at 320 px checked visually: box, thermometer, readout and sliders all visible.

## Findings (none blocking)
1. content/FY3/fy3-3/sim.js:75 (cosmetic, minor). On narrow screens the canvas is scaled down (k = 600/clientWidth) and the thermometer labels `600 K` / `100 K` are drawn at `tx + 14 = 554` with a font enlarged by k. At 320 px they are clipped at the right canvas edge and show as "600" and "100" without "K" (and "300 K" under the bulb is near the edge). The numeric readout is DOM text, so nothing is lost. Optional fix: place the scale labels to the left of the tube or reduce k scaling for these two labels.
2. content/FY3/fy3-3/sim.js:52 (statistical, minor). The pressure window is 90 frames (1,5 s). In the corner of low speed and a wide box (100 K, 2,0 dm³) only a few wall hits fall in the window, so the shown value fluctuates a lot. Measured ratio to theory per second from 100 K / 2,0: 1.95, 1.24, 1.18, 0.85, 1.17, 0.73, 0.86, 1.31, 1.06, 1.06, 1.04, 1.04, 1.09, 1.09. The long-run mean is unbiased (1.036; min 0.71, max 1.40 over 20 s). After enlarging the box the particles also need a few seconds to spread (a real gas-expansion transient), which explains the 0.64 right after 600 K / 0,5 -> 100 K / 2,0. At 300 K / 1,0 the ratio over 30 s was mean 1.036, min 0.881, max 1.191, sd 0.049. This is physically fine and the committed tests avoid the noisy corner. It does mean any later exercise or text that says "pressure is exactly proportional to T/V" should say "about".
3. Systematic offset of about +4 % (+7 % at 0,5 dm³): the particles are reflected at the wall minus the radius R = 4 (sim.js:44-47), so the effective box is 8 px smaller in each direction than the drawn W and 200 px height, while pTheory (sim.js:54) and pRef use the full size. Not a physics error, within the 30 % tolerance, no action needed. Twelve 300 K / 1,0 assertion-style trials after different preceding states: ratio 0.96, 1.11, 1.06, 1.04, 1.06, 1.15, 1.12, 1.04, 0.96, 0.97, 1.05, 1.01; no failure.
4. Coverage of the committed test (advisory, the 11 assertions cover the spec's slider, speed, pressure, readout, canvas and unit points, so no FAIL). Possible additions for the fixer, to be pasted into tests/sims/fy3-3.json (the test file is part of the hash, I did not edit it):
```json
{ "setup": "const r=document.querySelectorAll('#sim-root input[type=range]'); r[0].value=600; r[1].value=2;", "expr": "window.simState.theta - (600 - 273.15)", "expected": 0, "tol": 1e-06, "note": "theta = T - 273,15 also at a non-default T (the first assertion only checks 300 K)" },
{ "setup": "const r=document.querySelectorAll('#sim-root input[type=range]'); r[0].value=450; r[1].value=0.5;", "expr": "window.simState.pTheory - 100 * (450/300) / 0.5", "expected": 0, "tol": 1e-06, "note": "theory pressure = 100 * (T/300) / V" },
{ "expr": "window.simState.N", "expected": 80, "tol": 0, "note": "80 particles" },
{ "setup": "const r=document.querySelectorAll('#sim-root input[type=range]'); r[0].value=100; r[1].value=0.5;", "expr": "(() => { const x=document.querySelector('#sim-root .readout').textContent; return x.includes('T = 100 K = −173 °C') && x.includes('teoria 67') ? 1 : 0 })()", "expected": 1, "tol": 0, "note": "readout follows the sliders: 100 K = -173 °C, theory 67" }
```
   The fixed-seed requirement and the containment of the particles are not exposed in simState, so they cannot be asserted in the test file without a sim.js change (for example an added `simState.checksum` = sum of particle x positions, or `xMax`). I verified both independently (items 5 and 6). Also, `simState.speedCheck` only reads particle 0 (sim.js:60); since every particle shares the same speed by construction (unit direction vector times v, only signs flip), this is adequate.

## Result
No errors, speed and theta exact, pressure scales with T and 1/V, particles confined, start deterministic, readout/canvas/labels as specified, no overflow at 320/360/390 px. Committed test: 3/3 PASS.
