VERDICT: PASS
CONTENT-HASH: 706bdc1c984c1ed5

## Blocking

## Polish
- solutions.md:13–14 — the substitution ends "≈ 932 kPa" and the answer is "930 kPa" with no word on why (95 m has two significant figures) — add "(kaksi merkitsevää numeroa)" or end the substitution at 931 950 Pa.
- solutions.md:7 — "kenkien pohjat noin kuudesosa suksien alasta": two shoe soles (≈ 2 × 0,03 m²) are nearer a fifth of 0,30 m² — say "viidesosa–kuudesosa" or "noin viidesosa".

## Checked
- Round-2 conversion (git diff since the figure pass): exit-ticket a1/q2/a2, inquiry pred-3 feedbacks ("Selitä-vaihe" → "Teoriatiivistelmä"), sim howto and check-2 prompt "(h, p)" → "$(h, p)$": every number, unit, formula and meaning unchanged (ρ = 1000 kg/m³, 9,81 m/s², 5,0 m, ≈ 49 kPa, 101 + 49 ≈ 150 kPa, p = F/A). The renamed reference points to the theory activity, which holds the ρAhg/A derivation, so it still says the true thing.
- answers.py and an independent recomputation agree for all 12 exercises (2400 Pa, 931,95→930 kPa, 275,08 kPa, 300 kPa, 4414,5 Pa, 4,0 MPa, 35,68 m, 919,98 kg/m³, 3,23 kN, 0,139 m², 9,81 kN, 19,03 kPa); solutions symbolic first, LaTeX values match.
- Formulas p = F/A and p = p₀ + ρgh with conditions (liquid at rest, uniform density, force normal to the surface); derivation via G = mg, m = ρV inside FY3 scope.
- Worked example: ρgh = 117,72 kPa, p ≈ 219 kPa, F ≈ 1,77 kN ≈ 1,8 kN (≈ 180 kg weight).
- Prose: 10 m ≈ 98 kPa ≈ one atmosphere; dam 30 m → 294 kPa ≈ "noin 290 kPa".
- Figures: pressure-depth to scale (0,895 px/kPa: 101 kPa at y 194,5, 199 kPa at y 106,5; 10 m at x 450); bricks 40 vs 120 px = 3A₁; water column G = ρAhg, p = G/A = ρgh; LaTeX labels render correctly.
- inquiry pred-1 (150 → 199 kPa), pred-2 (ρgh 98 → 122 kPa, +24 %; total 199 → 223 kPa, +12 %), pred-3: correct options and feedback numbers right.
- exp-1 locks ρ, varies h; exp-2 locks h, varies ρ; simState has pOver, pTotal; numeric 9,81 kPa/m, mistakes 9810 and 19,9 right.
- virhe 29 kPa; siirto 0,757 m (mistakes 10,3 m, 0,000757 m); check-2 892 kg/m³ (mistakes 2180, 0,892); check-3 model 29 kPa, ≈ 1,8 N.
- sim.js implements p = p₀ + ρgh (p₀ = 101 kPa, g = 9,81), equal arrows in all directions; model limits stated in the inquiry.
