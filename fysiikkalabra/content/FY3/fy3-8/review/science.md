VERDICT: PASS
CONTENT-HASH: a1d5a91060a6b797

## Blocking

## Polish
- lesson.md:58: "siihen palataan oppitunnilla fy3-9" names the lesson by its id. The owner wants the chapter named instead, e.g. "Kaasujen tilanmuutokset" luvussa. The same applies to inquiry.json:5–6, where "(fy3-3)" in `prior` should be the chapter name.
- sim.js:1033–1036: the thin lines on the chart for the other materials have no key on the canvas. Only `howto` names the steepest and the gentlest. Add short end labels (Al, Cu, lasi, …) so a printed or screenshotted chart can be read on its own.
- inquiry.json pred-1, third option feedback: "teräksen α on käytännössä vakio". This is true to within about 10 % between −40 °C and 120 °C. Saying "lähes vakio" would be more exact.

## Checked
- Last round's blocking item is fixed. The simulation's `model` text now says that the micro model draws the vibration symmetrically and sets the spacing from the formula, so it shows *that* the spacing grows but not *why*. The pred-3 feedback for Bea's option repeats this, so the simulation no longer appears to confirm Cem's account.
- Last round's three polish items are also fixed: the range of validity is now "noin sata kelviniä", Aino's feedback now says "malli olettaa", and siirto now says "etanolin tilavuus".
- All 12 exercise answers were recomputed independently. They match answers.py and exercises.json within tolerance (rounded cases: L1-02 −51,75 → −52, L2-01 52,08 → 52, L3-03 457 → 460).
- Worked example: 0,0864 m and 0,07 %. The unknown is already isolated, the units are checked, and the reasoning about the expansion joint is right.
- The inquiry numbers all recompute correctly:
  - pred-1 and pred-2: 6,00 and 12,0 mm, relative change 0,0600 %.
  - Interpret table: 0,36, 2,1, 11 and 34 cm³.
  - virhe: 27,9 mm against 1,84 mm (×15), 0,7 %.
  - siirto: 44 mm. The mistakes 0,044 and 110 are right, the glass ratio is ≈41, and the result with glass is 42,9 mm.
  - check-2: 23, from both columns. The mistakes 46 and 15,3 are right.
  - check-3: air/steel ≈94. Exit ticket: 21 mm.
- Physics is correct throughout:
  - γ ≈ 3α, sign convention when cooling, L = L₀ + ΔL.
  - A hole grows with the plate. The shrink fit (100 K) works.
  - The bimetal strip bends toward the steel.
  - Rail gap: ΔL/2 at each end, closed from both neighbours.
  - Water anomaly and lake freezing.
  - The anharmonic-interaction argument stays within FY3 scope.
- The coefficient tables are realistic at 20 °C (air 3,4·10⁻³ ≈ 1/293 K).
- exp-1 locks material and L₀ and varies T. exp-2 locks material and T and varies L₀. `simState` exposes dT, dL and rel, and the initial values reproduce the numbers in the prediction feedback.
- Simulation code:
  - Implements ΔL = αL₀ΔT from 20 °C.
  - The ×100 exaggeration is labelled, and "alle 0,3 %" holds (maximum 0,23 %).
  - Amplitude ∝ √T. Particles keep their size.
  - The chart scales to aluminium. Speed changes only the picture.
- Figures 1 and 2: particles drawn the same size, d > d₀, the ΔL arrow ends exactly at the end of the warm rod, the exaggeration is stated, and labels are in LaTeX.
