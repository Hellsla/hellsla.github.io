VERDICT: PASS
CONTENT-HASH: 1cebfd341ecec92d

## Blocking

## Polish
- solutions.md:13–14 — the substitution ends "≈ 932 kPa" and the answer is "930 kPa" with no word on why (95 m has two significant figures) — add "(kaksi merkitsevää numeroa)" or end the substitution at 931 950 Pa.
- solutions.md:7 — "kenkien pohjat noin kuudesosa suksien alasta": two shoe soles (≈ 2 × 0,03 m²) are nearer a fifth of 0,30 m² — say "viidesosa–kuudesosa" or "noin viidesosa".

## Checked
- answers.py and an independent recomputation agree for all 12 exercises (2400 Pa, 931,95→930 kPa, 275,08 kPa, 300 kPa, 4414,5 Pa, 4,0 MPa, 35,68 m, 919,98 kg/m³, 3,23 kN, 0,139 m², 9,81 kN, 19,03 kPa); solutions symbolic before substitution, units and rounding consistent.
- Formulas p = F/A and p = p₀ + ρgh with conditions (liquid at rest, uniform density, force normal to surface); derivation via G = mg and m = ρV stays inside FY3 scope (force as scalar, per the slot note).
- Worked example: ρgh = 117,72 kPa, p ≈ 219 kPa, F = ρgh·A ≈ 1,8 kN (≈ 180 kg weight); overpressure only on the window is justified.
- Prose magnitudes: 10 m ≈ one atmosphere (98 kPa), dam at 30 m ≈ 294 kPa ≈ "noin 290 kPa", 290 kN per m².
- Figures: pressure-depth to scale (101 kPa at y 194,5, 199 kPa at y 106,5 against 0,9 px/kPa; 10 m at x 450); brick contact widths 40 vs 120 px = 3A₁; water-column labels G = ρAhg, p = G/A = ρgh correct.
- inquiry pred-1 (150 → 199 kPa, ×1,33), pred-2 (ρgh 98 → 122 kPa, +24 %; total 199 → 223 kPa, +12 %), pred-3 (same pressure): correct options and every feedback's numbers verified.
- exp-1 locks ρ and varies h, exp-2 locks h and varies ρ; simState carries pOver and pTotal; 720 and 1240 kg/m³ reachable with step 5; numeric 9,81 kPa/m and mistake 19,9 correct.
- virhe (3,0 m → 29 kPa), siirto (0,757 m; mistakes 10,3 m and 0,000757 m), check-2 (892 kg/m³; mistakes 2180 and 0,892), check-3 model (29 kPa, ≈ 1,8 N on 0,6 cm²) all correct.
- sim.js implements p = p₀ + ρgh with p₀ = 101 kPa, g = 9,81; equal arrows in all directions; overpressure-only mode drops the intercept; limits (fixed p₀, incompressible liquid at rest, model values) stated in the inquiry text.
- Exit ticket: 49 kPa, 150 kPa, shape independence.
