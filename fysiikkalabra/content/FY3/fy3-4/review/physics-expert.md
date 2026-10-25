VERDICT: PASS
CONTENT-HASH: 4396a7deb8e88cef

## Blocking
(none)

## Polish
1. lesson.md:14 — "yläreunassa nolla" holds only if water reaches the crest. — "vedenpinnan tasolla nolla".
2. lesson.md:27 — ρgh equals the overpressure only when p₀ is air pressure, yet p₀ is "yleensä" air pressure. — Add "kun pinnalla on ilmanpaine".

## Checked
- Lint clean; hash unchanged start to end.
- Round-1 changes: the derivation V = Ah, m = ρV, G = mg = ρAhg, p = G/A = ρgh is correct and assumes a liquid at rest. The sideways-pressure argument and "voimakkaimmin" are sound. Δp = p − p₀ is consistent with lines 14 and 56.
- The dam paragraph is correct. Air pressure cancels on both sides of the wall, Δp(30 m) = 294 300 Pa ≈ 290 kPa, and that gives ≈ 290 kN on each m². The overpressure grows linearly with depth.
- Worked example: ρgh = 117 720 Pa, p = 218,72 kPa (2,17·p₀), F = ρgh·A = 1765,8 N ≈ 1,8 kN ≈ 180 kg·g, rounded only at the end. The diver explanation is correct. No buoyancy; force is a scalar normal to the surface (FY3 scope).
- 10 m of water gives 98,1 kPa ≈ p₀ (lines 12, 62). The SVG is linear, about 1 px/kPa.
- answers.py: right formula and conversion on each line (cm²→m², bar→Pa, kPa, MPa, G = mg); significant figures and tolerances fit.
- Hand-recomputed L3-02: ΔF = 39 240 Pa · 0,25 m² = 9810 N.
- Hand-recomputed L3-01: A = 833,85 N / 6000 Pa = 0,139 m² ≈ 25 cm × 56 cm. Putting the whole weight on one foot is correct.
- Hand-recomputed L2-04: F = 85 000 Pa · 0,0380 m² = 3230 N. All magnitudes are realistic. The solutions' reasoning and the exit ticket (49 kPa, 150 kPa) are correct.
- sim.js:41-44 uses the exact formula p = 101 + ρ·9,81·h/1000 kPa. Ylipaine mode removes only the intercept. Densities are realistic.

## Python output
```
answers.py: L1 2400.0, 931.95, 275.08, 300.0, 4414.5 | L2 4.0, 35.67788, 919.979613, 3.23 | L3 0.138975, 9.81, 19.0314
dam 30 m: 294300.0 Pa; per m2 294.3 kN
example: rho g h 117720.0 p 218720.0 ratio 2.1655 F 1765.8 N = 180.0 kg*g
L3-02: dp 39240.0 dF 9810.0 tube water 3.924 N, tube area 0.0001
L2-04 F 3230.0 N = 329 kg*g ; L3-01 A 0.138975 ; exit 49050.0 150050.0
```
