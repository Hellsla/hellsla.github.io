VERDICT: PASS
CONTENT-HASH: 1fb07c9450b90b82

## Blocking

## Polish
- inquiry.json:57,66,166 — "Mittauksesi näyttävät…" (pred-1 wrong-option feedbacks) and "Lue se mittauksistasi" (exp-1) still call the sim's computed values measurements; the round-2 fix changed only the other feedbacks — write "mallin arvot" here too.
- lesson.md:94 — "hydrostaattinen paine eli ylipaine Δp = p − p₀" equates the two only when p₀ is the surrounding air pressure — add "kun pinnalla on ympäröivä ilmanpaine" (carried from round 1).

## Checked
- Round 2: changes since cb4b8f4 are inquiry.json:62,84,88,93,97 ("Mittaukset" → "Mallin arvot"); numbers unchanged and recomputed: 150,05 / 199,1 kPa, Dead Sea ρgh = 121,6 kPa (+24 %), total 199,1 → 222,6 kPa (+11,8 % ≈ 12 %).
- p = F/A with F perpendicular, p = p₀ + ρgh derived from the column's weight with A cancelling; isotropy argued; inside FY3 scope.
- Magnitudes: 9,81 kPa/m, ≈ 1 atm per 10 m, dam 294 kPa, mercury column 0,757 m.
- Worked example symbolic first: ρgh = 117,72 kPa, p ≈ 219 kPa, F ≈ 1,8 kN from overpressure only.
- answers.py unchanged since round 1: all 12 matched, rounding within tolerance.
- solutions.md unchanged: unknowns isolated first, layered ΔF = ρ₁gh₁ + ρ₂gh₂.
- Figures unchanged: pressure–depth graph to scale; brick widths 1 : 3; column figure schematic.
- Simulation unchanged: p = 101 kPa + ρgh, equal arrows in all directions, overpressure mode drops the intercept; limits stated.
- exp-1 varies h at fixed ρ, exp-2 varies ρ at fixed h; simState carries pOver, pTotal; numeric 9,81 kPa with mistakes 9810 and 19,9.
- virhe 29 kPa; check-2 892 kg/m³; eardrum F ≈ 1,8 N; exit ticket 49 and 150 kPa.
