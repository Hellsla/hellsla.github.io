VERDICT: FAIL
CONTENT-HASH: 28956a3df07f9f05

Note on the hash: the hash at the start of the review was da9ba5eb24ac7a54 (as expected). Finding 1 required me to add 4 assertions to tests/sims/fy3-1.json, and that file is part of the content hash, so the hash is now 28956a3df07f9f05. Other reviewers' reports carry the old hash and must be rerun after the fix (the fix changes the hash again anyway).

1. FAIL (real defect): the spring stretch does not react to the mass slider. content/FY3/fy3-1/sim.js:37 `const stretch = SPRING.maxLen * (G / (m * G_MAX));` divides out m, so stretch = maxLen * g / G_MAX depends only on the body. sim-spec.md says "jousi venyy painon mukaan" (the spring stretches according to the weight), and sim.js:3 says "The spring stretches in proportion to G". Measured via simState.stretch (identical for m = 1, 10, 50, 100):
   Kuu 12.411, Mars 28.423, Maa 75.157, Jupiter 190 (all four values constant over the slider range). On Maa the lowest dark pixel of the spring+block column only moves 199 -> 199 -> 202 -> 213 px for m = 1, 25, 50, 100, and the movement is only the block growing (sim.js:53), not the spring. A student dragging 1 -> 100 kg sees the same stretch while G goes 9,81 -> 981 N, which contradicts the readout. Fix: make stretch proportional to G, for example `SPRING.maxLen * G / (100 * G_MAX)` (full scale 100 kg on Jupiter), and then check that the 1 kg case on Kuu is still visible (1,62 / 2480 of full scale is about 0,1 px, so a spring scale that works over the whole range needs a floor, or a different mapping such as sqrt, or a note that the scale is nonlinear; a linear scale with a minimum visible length is the honest choice). The bar chart at sim.js:64 has the same normalisation: bar heights are m-independent (only the N labels change); that is acceptable for a comparison across bodies, but the heights also would not show the slider.
   Added assertions (tests/sims/fy3-1.json lines 12-14): "stretch grows with mass slider" (currently 0 -> FAIL), "stretch/G constant across bodies and masses" (currently 0 -> FAIL), "stretch grows Kuu < Mars < Maa < Jupiter" (passes).

2. PASS: page loads with no console errors or page errors. test_sims.py errors list is [] and my own script also printed errors [].

3. PASS: the formula is exact. sim.js:36 `const G = m * g;` with the table at sim.js:8 [Kuu 1.62, Mars 3.71, Maa 9.81, Jupiter 24.8]. My sweep over all 4 bodies x m in {1,10,50,100} gave G - m*g = 0.0 in all 16 cases (e.g. Jupiter 100 kg: G = 2480, Kuu 1 kg: G = 1.62). simState.m was always the slider value regardless of body (mass independent of body).

4. PASS: the highlight of the selected body in the bar chart works. Pixel sample at the base of each bar (alpha 255 for the selected, 90 for the others):
   Kuu   [[150,150,150],[229,194,183],[179,204,218],[233,215,194]]  (bar 0 full colour)
   Mars  [[215,215,215],[190,90,60],[179,204,218],[233,215,194]]    (bar 1 full colour)
   Maa   [[215,215,215],[229,194,183],[47,120,160],[233,215,194]]   (bar 2 full colour)
   Jupiter [[215,215,215],[229,194,183],[179,204,218],[200,150,90]] (bar 3 full colour)
   The block colour (sim.js:54) also follows the body.

5. PASS (select half only): the spring reacts to the select. Lowest dark pixel y at m = 10: Kuu 152, Mars 164, Maa 199, Jupiter 285; simState.stretch 12.4 / 28.4 / 75.2 / 190. See finding 1 for the slider half.

6. PASS: coverage of the existing 11 assertions against the spec. G = m g default (98,1 N), g default 9,81, Kuu 5 kg -> 8,1, Mars 25 kg -> 92,75, Jupiter 100 kg -> 2480, Maa 10 kg -> 98,1, mass from slider (5) independent of body, DOM readout text contains "G = m · g = 98,1 N" and "g = 9,81 N/kg", select options exactly Kuu,Mars,Maa,Jupiter, canvas 600x400, slider label contains "kg". All four g values are exercised. I added a slider range check (min 1, max 100, spec says 1-100 kg) at tests/sims/fy3-1.json line 15; it passes.

7. INFO (minor, no action required): tests/sims/fy3-1.json assertion tol is relative for |expected| > 1, so the 2480 N check allows 0,00248 N slack; still tight enough. Readout text content concatenated without separators in textContent ("(sama kaikkialla)g = 9,81 N/kg (Maa)G = ...") is only a textContent artefact of the <br> tags; visually it is three lines. Preview preview/fy3-1-sim.js is identical to content/FY3/fy3-1/sim.js (diff clean).

Raw test output, before my additions:
PASS preview/fy3-1  [] []

Raw test output, after my additions (output shortened; two assertions fail, both on spring stretch vs mass):
FAIL preview/fy3-1  [] ["(async () => { ... s.value='Maa'; r.value=10; ... r.value=100; ... return b>a*1.5 ? 1 : 0 })() = 0 (expected 1)", "(async () => { ... stretch/G ... })() = 0 (expected 1)"]

Command: PW_CHROMIUM=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome python scripts/test_sims.py fy3-1
My own Playwright script (scratchpad t.py) printed: canvas [600, 400, 1]; errors []; readout "Massa m = 100 kg (sama kaikkialla)g = 9,81 N/kg (Maa)G = m · g = 981,0 N"; slider label "Massa m = 100 kg".
