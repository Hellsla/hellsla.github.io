VERDICT: PASS
CONTENT-HASH: bce4f733d3154bc0

## Blocking
(none)

## Polish
1. lesson.md:30-35 — SVG p axis not linear: 0→101 kPa spans 90 px, 101→199 kPa spans 108 px, so the 10 m rise looks larger than p₀ (contradicts line 12). — Move the 10 m point to y ≈ 73 (line `y2`, circle `cy`; label "199" at y ≈ 80).
2. lesson.md:49-51 — p is 219 kPa on line 49, then `F = pA` uses 118 kPa. — Write `F = \rho g h \cdot A` (or `\Delta p\,A`).
3. lesson.md:10 — An eardrum is pushed from one side only, and "vaakasuoraan" holds only for a vertical dam face. — "sukeltajan kehoon joka puolelta", "padon pystysuoraan seinään".
4. lesson.md:8 — The derivation assumes a liquid at rest with constant density. — Add "levossa olevassa nesteessä".

## Checked
- Derivation in Ydinajatus: G = ρAhg, p = G/A = ρgh, A cancels, total p₀ + ρgh, 9,81 kPa/m. g in m/s². Force is a scalar normal to the surface, as MAOL allows for FY3. No buoyancy.
- Worked example: ρgh = 117,72 kPa, p = 218,72 kPa (2,17 p₀). Net force on the window = ρgh·A = 1766 N ≈ 1,8 kN ≈ 180 kg·g. Using only the overpressure is right because room air cancels p₀.
- answers.py: every line uses the right formula and conversion (cm²→m², bar→Pa, kPa, MPa). Significant figures and tolerances fit the data.
- Recomputed by hand L3-02 (Pascal barrel): ΔF = ρgh·A = 9810 N. The 0,40 l in the tube weighs 3,9 N, consistent with a 1 cm² tube.
- Recomputed by hand L3-03: the layers add, 3335,4 + 15 696 Pa ≈ 19 kPa. The all-water check of 19,62 kPa is right.
- L2-04 overpressure × lid = 3,2 kN (≈ 329 kg). L3-01 puts the full weight on one foot: 0,139 m² ≈ 25 cm × 56 cm.
- Exit ticket (49,05 kPa, 150 kPa) and every magnitude in the exercises are realistic and correct.
- sim.js:41-44 uses the exact formula p = 101 + ρ·9,81·h/1000 kPa, slope ρg. Ylipaine mode drops only the intercept.

## Python output
```
answers.py: L1 2400.0, 931.95, 275.08, 300.0, 4414.5 | L2 4.0, 35.67788, 919.979613, 3.23 | L3 0.138975, 9.81, 19.0314
example: rho g h 117720.0, p 218720.0, ratio 2.1655; window F 1765.8 N = 180.0 kg * g
L3-02: dp 39240.0, dF 9810.0, tube water 3.924 N, tube area 0.0001 m2
L3-03: oil 3335.4, water 15696.0, sum 19031.4, all-water 19620.0
SVG linear y for 199 kPa: 72.7 (drawn at 52)
```
