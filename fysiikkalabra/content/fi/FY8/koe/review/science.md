VERDICT: FAIL
CONTENT-HASH: 54f883462cec865c

## Blocking
1. **A, figure number (figures.py `leds()`, fy8-k2-graph description).** The description says the dashed line crosses the frequency axis "noin taajuudella 2,6 kymmenen potenssiin 14 hertsiä". It actually crosses at −B/S = 0,110 V / (0,425 V per 10^14 Hz) ≈ 0,26·10^14 Hz. The drawing itself is correct, but a screen-reader user gets a value ten times too large, and it conflicts with solution d (intercept −0,1 V). Fix: "0,26 kymmenen potenssiin 14 hertsiä" or "lähellä origoa".

## Polish
- k2 b: the slope is rounded to 4,2·10^-15 V s, but 1,602 · 4,2 = 6,73, not 6,8. Write 4,22·10^-15.
- fy8-k3-graph description: "puolittunut alkuarvostaan 401" makes 401 sound like the start value. Suggest "arvoon 401".

## Checked
My own script, independent of answers.py, recomputed:
- **Osa 1:** each item has exactly one correct option, and each distractor fails for the reason its Perustelu gives.
  - b: f0 = 5,61·10^14 Hz, W = 3,71·10^-19 J = 2,32 eV. The figure's line starts at 0,24 V.
  - d: 5,4 (the distractors 3,0 and 0,6 are right).
  - e: 2,74 V (4,0 and 1,3).
  - g: 20 h (linear 7,75).
  - h: 5·10^7 (keV and GeV distractors).
  - i: 20 mSv and 1 mSv.
  - j: weak interaction, d → u.
- **k2:**
  - Frequencies are right.
  - Least squares gives h = 6,81·10^-34, reading from the line 6,76.
  - The extreme lines stay inside all five bars (checked by residuals). h_max = 7,37, h_min = 6,18, Δh = 0,60·10^-34.
  - Model deviations 0,02–0,07 V and intercept −0,11 V. The direction of the bandgap effect is right.
- **k3:** fit T½ = 3,18 min, λ = 0,217 /min, N(15) = 31 (4 %), 3,5 %, last point 11 %.
- **k4:** binding energies 28,30 / 7,07, 1,11 and 2,83 MeV. Q = 17,59 MeV, also from binding energies. 3,37·10^14 J/kg, 1,1·10^7 times coal.
- **k5:** 656,5 nm, 121,6 nm, 2,80 eV (4,49·10^-19 J), limit 365 nm. The orbital model stays qualitative.
- **k6:**
  - μ = 0,1137 /mm (reading 0,114), d½ = 6,1 mm.
  - Dose: factor 35,6, so d = 31,4 mm.
  - Uncertainty 3,9 % (3,4 % or 3,7 % accepted).
  - μ without background subtraction = 0,110.
  - The narrow-beam and extrapolation caveats are stated.
- **k7:** 0,321, 1540 MBq, 511 keV, 2,43 pm, 5,32 mSv (90 %). C-11: 0,0022 left, 2,7 TBq.
- Rubrics, point sums, tolerances and scope are fine. Hash unchanged from start to end.
