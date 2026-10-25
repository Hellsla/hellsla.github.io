VERDICT: PASS
CONTENT-HASH: 4396a7deb8e88cef

## Blocking
(none)

## Polish
1. lesson.md:14 — "Ylipaine on yläreunassa nolla" is true only if the water reaches the crest. A dam's crest normally sits above the water. — Write "vedenpinnan tasolla nolla".
2. lesson.md:27 — "hydrostaattinen paine eli ylipaine Δp = p − p₀" equates ρgh with overpressure (pressure above air pressure). That holds only when p₀ is air pressure, but the same sentence allows another surface pressure. — Add "kun pinnalla on ilmanpaine".

## Checked
- lint_lesson.py fy3-4: 0 errors, 0 warnings. Hash 4396a7deb8e88cef was the same at the start and at the end.
- Round-1 changes: the derivation V = Ah, m = ρV, G = mg = ρAhg, p = G/A = ρgh is correct and assumes a liquid at rest. The argument for sideways pressure is sound. The lowest hole spurts "voimakkaimmin" because the outflow speed grows with depth. Δp = p − p₀ is consistent with lines 14 and 56.
- The dam paragraph is correct. Air pressure cancels on both sides of the wall, Δp(30 m) = 294 300 Pa ≈ 290 kPa, and that gives ≈ 290 kN on each m². The overpressure grows linearly with depth.
- Worked example: ρgh = 117 720 Pa, p = 218,72 kPa (2,17·p₀), F = ρgh·A = 1765,8 N ≈ 1,8 kN ≈ 180 kg·g, rounded only at the end. Using only the overpressure is right because the room air cancels p₀. The explanation for why the diver is not crushed is correct. There is no buoyancy, and force is treated as a scalar normal to the surface, both within FY3.
- 10 m of water gives 98,1 kPa ≈ p₀ (lines 12 and 62). The slope is 9,81 kPa/m, and the SVG is linear at about 1 px/kPa (101 kPa at y = 150, 199 kPa at y = 52).
- answers.py: each line uses the right formula and the right conversions (cm²→m², bar→Pa, kPa, MPa, G = mg). Significant figures and tolerances fit the data.
- Hand-recomputed L3-02: ΔF = 39 240 Pa · 0,25 m² = 9810 N. The tube holds 3,9 N of water, so its cross-section is 1 cm².
- Hand-recomputed L3-01: A = 833,85 N / 6000 Pa = 0,139 m² ≈ 25 cm × 56 cm. Putting the whole weight on one foot is correct.
- Hand-recomputed L2-04: F = 85 000 Pa · 0,0380 m² = 3230 N ≈ 329 kg·g. All the magnitudes are realistic: water tower 35,7 m, rapeseed oil 920 kg/m³, heel 4,0 MPa. The solutions' reasoning is correct, and the exit ticket gives 49 kPa and 150 kPa.
- sim.js:41-44 uses the exact formula p = 101 + ρ·9,81·h/1000 kPa with slope ρg. Ylipaine mode removes only the intercept. The liquid densities in sim-spec.md and sim.js are realistic.

## Python output
```
answers.py: {"fy3-4-L1-01": 2400.0, "fy3-4-L1-02": 931.95, "fy3-4-L1-03": 275.08, "fy3-4-L1-04": 300.0, "fy3-4-L1-05": 4414.5, "fy3-4-L2-01": 4.0, "fy3-4-L2-02": 35.67788, "fy3-4-L2-03": 919.979613, "fy3-4-L2-04": 3.23, "fy3-4-L3-01": 0.138975, "fy3-4-L3-02": 9.81, "fy3-4-L3-03": 19.0314}
dam 30 m: 294300.0 Pa; per m2 294.3 kN
example: rho g h 117720.0 p 218720.0 ratio 2.1655 F 1765.8 N = 180.0 kg*g
10 m: 98100.0 vs p0 101000
L3-02: dp 39240.0 dF 9810.0 tube water 3.924 N, tube area 0.0001
L2-04 F 3230.0 N = 329 kg*g ; L3-01 A 0.138975 ; exit 49050.0 150050.0
```
