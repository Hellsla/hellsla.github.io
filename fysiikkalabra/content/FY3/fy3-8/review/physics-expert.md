VERDICT: PASS
CONTENT-HASH: 27f5201d4017be25

## Blocking
(none)

## Polish
1. lesson.md:12 — The gas sentence says the particles are "lähes vapaita" but not why the volume grows at constant pressure. — Optionally add "nopeammat hiukkaset törmäävät seiniin voimakkaammin" as a lead-in to fy3-9.
2. solutions.md:31 — "hieman suurempi" is right (densities give about 0,90 l against 0,84 l), but the reason is that 12…32 °C is centred at 22 °C, above the table's 20 °C. — Optional: "välin keskilämpötilassa γ on taulukon arvoa suurempi".

## Checked
- Lint has 0 errors and 0 warnings. The hash is the same at the start and the end of the review.
- lesson.md:6: the asymmetric repulsion and attraction is described correctly, so the mean spacing grows and the particles do not.
- lesson.md:12: the liquid and gas sentences are correct, gases are limited to constant pressure, and the 4 °C lake stratification is right.
- lesson.md:19: α is the relative elongation per kelvin, ΔL ∝ L₀ follows from the number of particle spacings, and the table's 12 means 12 · 10⁻⁶ 1/K. All correct.
- lesson.md:21, 25: γ ≈ 3α comes from (1+αΔT)³ ≈ 1+3αΔT and holds for solids. Air's γ = 3,4 · 10⁻³ 1/K matches an ideal gas at 20 °C.
- The tables match handbook values. The worked example (0,0864 m, 0,07 %) is correct.
- answers.py: every line uses the right formula, sign and unit conversion. L1-03 gives ΔL directly in mm, and L1-05 uses 9,0e-6.
- Hand-recomputed three answers. L1-03 is 0,85 mm. In L2-03 each rail end moves ΔL/2 and two neighbours close the gap, so it closes at 36 °C. L3-03 is 475 − 18 = 457 cm³, and the γ ratio of 26 makes "yli 25 kertaa" true.
- solutions.md reasoning (shrink fit, bimetal bending toward steel, sealed can) and exit-ticket answers 1–3 are correct.
- sim.js:59–64 implements ΔL = αL₀ΔT exactly, with the vibration amplitude growing as √T.

## Python output
```
answers.py: {"L1-01": 2.88, "L1-02": -51.75, "L1-03": 0.85, "L1-04": 0.84, "L1-05": 0.3375, "L2-01": 52.083333, "L2-02": 3.024, "L2-03": 36.0, "L2-04": 23.0, "L3-01": 120.0, "L3-02": 20.0, "L3-03": 457.0}
L1-03 0.85 (0.17 %); L2-03 dL 7.2 mm, each end 3.6; L3-03 475-18=457, ratio 26.4
L1-04 real from densities 0.898 l; air +30 K linear 0.1020 vs exact 0.1023
```
