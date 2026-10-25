VERDICT: PASS
CONTENT-HASH: 8fb367b0d6fd83e0

Round 3 (final), tester. Hash checked before and after the review: 8fb367b0d6fd83e0 both times (matches the expected value). preview/fy3-1-sim.js is byte-identical to content/FY3/fy3-1/sim.js (diff empty).

## Official test run

1. `PW_CHROMIUM=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome python scripts/test_sims.py fy3-1`
   Raw output: `PASS preview/fy3-1  [] []` (no console errors, simState present, all 19 assertions in tests/sims/fy3-1.json hold).

## Independent Playwright checks (own script, 1280x900, 65 checks ok, 0 failed, no console/page errors or warnings)

2. G = m g, mass independent of body, for all four bodies (g 1,62 / 3,71 / 9,81 / 24,8) at m = 1, 7, 10, 33, 50, 100 kg (24 states): simState.G equals m*g exactly, simState.m equals the slider value, simState.g and simState.body match the select. sim.js:42, :49.
3. Proportionality over the same 24 states: stretch = 190*G/2480, arrow = 110*G/2480 and bars[i] = m*g_i/2480*220 hold to 1e-9; stretch/G and arrow/G constant over all states (sim.js:43, :47, :48).
4. Changes with both inputs: Maa 10 -> 100 kg gives x10 stretch, x10 arrow, x10 on every bar; at 100 kg Maa -> Kuu stretch and arrow both drop (select changes them). Bars are by design independent of the select (they show the same mass on all four bodies, per sim-spec.md); the select only changes the highlight, so only the mass slider moves bars. This matches the spec.
5. Full scale, 100 kg on Jupiter: `{'m': 100, 'body': 'Jupiter', 'g': 24.8, 'G': 2480, 'stretch': 190, 'arrow': 110, 'bars': [14.37, 32.91, 87.02, 220]}`. Geometry: block bottom y = 346, arrow tip y = 386 (< 400). Pixel scan of the canvas for the red arrow: lowest red pixel y = 383 of 400, so the arrow fits (the previous defect is fixed).
6. DOM readout (Maa, 10 kg): `'Massa m = 10 kg (sama kaikkialla)\ng = 9,81 N/kg (Maa)\nG = m · g = 98,1 N'`. Select options: `Kuu,Mars,Maa,Jupiter`. Canvas width/height attributes 600x400. Slider label parent text `Massa m = 10 kg` (unit kg present). Slider min 1, max 100.
7. Narrow viewports 320, 360, 390 px (loaded, then switched Jupiter 100 kg, Kuu 1 kg, Maa 55 kg): no console or page errors, simState alive, no horizontal overflow (scrollWidth == clientWidth: 320/360/390). Canvas scales to 254/294/324 px; screenshot at 320 px shows the title, bars, value labels and the readout legible and inside the canvas.

## Assertion coverage of sim-spec.md (tests/sims/fy3-1.json)

8. Covered: G = m g at default and three further body/mass pairs (lines 2-7), mass independent of body (line 5), DOM readout (line 8), exactly four select options (line 9), canvas 600x400 (line 10), slider unit and range 1-100 (lines 11, 15), stretch grows with mass (12), stretch/G constant across bodies and masses (13), stretch ordering Kuu < Mars < Maa < Jupiter (14), bars x10 with x10 mass (16), full-scale bound of bar and stretch (17), arrow proportional to G including the Maa/Kuu ratio and the 120 px fit at 100 kg Jupiter (18, 19). Well over the required 3 assertions, and they would catch the earlier defect (a constant term in the arrow).
9. Optional, non-blocking suggestion (not a failure): the bars are only asserted via the x10 mass ratio; a cross-body ratio check (bars[3]/bars[0] = 24.8/1.62 at any mass) would additionally pin the "same mass on all four bodies" part of the spec. Ready-to-paste JSON if the fixer wants it:
   `{ "expr": "(() => { const b=window.simState.bars; return Math.abs(b[3]/b[0]-24.8/1.62) < 0.01*(24.8/1.62) && Math.abs(b[2]/b[1]-9.81/3.71) < 0.01*(9.81/3.71) ? 1 : 0 })()", "expected": 1, "tol": 0, "note": "bar heights are proportional to g of each body for the same mass" }`
   The 2 px bar and 3 px arrow display floors are drawing-only (sim.js:68, :77) and are not exposed in simState, so they are not testable through simState; not required.

No real failures found.
