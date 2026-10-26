VERDICT: PASS
CONTENT-HASH: 150708be69f8d013

## Blocking

## Polish
- inquiry.json:57,62,66,84,88,93 (also 166, 252) — the prediction feedback calls the simulation's numbers "mittaukset/mittauksesi", but the sim computes p = p₀ + ρgh from the formula (its model box and the conclusion say so); the brief asks that these be called model values — write "mallin arvot näyttävät…" / "mallin arvot tukevat tätä", and "lue se mallin arvoista" in the exp-1 question.
- lesson.md:196 — "hydrostaattinen paine eli ylipaine Δp = p − p₀" equates the two only when the surface pressure p₀ is the surrounding air pressure (as in every task here); a half-sentence "kun pinnalla on ympäröivä ilmanpaine" would keep the definition exact.

## Checked
- p = F/A with F perpendicular to the surface, p = p₀ + ρgh with symbols and units named; derivation from the column's weight ρAhg with A cancelling; isotropy and the perpendicular force argued; inside FY3 scope.
- Magnitudes: 9,81 kPa/m, ≈1 atm per 10 m, dam at 30 m ≈ 294 kPa ≈ 290 kN/m², Dead Sea 1240 kg/m³, rapeseed oil 920 kg/m³, mercury column 0,757 m.
- Worked example symbolic first: ρgh = 117,72 kPa, p ≈ 219 kPa, F = ρghA ≈ 1,8 kN using only the overpressure because the room is at air pressure.
- answers.py recomputed in one script: all 12 match my formulas; rounding to the data's figures stays within tolerance.
- solutions.md: unknowns isolated first (h = Δp/ρg, ρ = Δp/gh, A = G/p_max, F = ΔpA, layered ΔF = ρ₁gh₁ + ρ₂gh₂).
- Figures: pressure–depth graph to scale; brick contact widths 40 : 120 px = 1 : 3 as stated; water-column figure labelled schematic.
- Simulation: p = 101 kPa + ρgh with ρg in kPa/m, four equal arrows (pressure in every direction), overpressure-only mode drops the intercept; limits (fixed p₀, incompressible liquid at rest) stated.
- exp-1 locks ρ and varies h, exp-2 locks h and varies ρ; simState carries pOver and pTotal; exp-1 numeric 9,81 kPa with mistakes 9810 and 19,9.
- Predictions: 150 → 199 kPa (×1,33, overpressure ×2); Dead Sea 98 → 122 kPa (+24 %), total 199 → 223 kPa (+12 %); equal bottom pressure in tube and pool.
- virhe 29 kPa at 3,0 m; check-2 892 kg/m³ (mistakes 2180, 0,892); check-3 eardrum Δp ≈ 29 kPa, F ≈ 1,8 N at 0,6 cm²; exit ticket 49 and 150 kPa.
