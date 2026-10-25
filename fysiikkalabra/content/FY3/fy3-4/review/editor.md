VERDICT: PASS
CONTENT-HASH: 48c322a6f3742eff

The dam hook (lesson.md:3) is now answered in lesson.md:14. Air pressure acts on both sides, so only the overpressure loads the wall: zero at the top and about 290 kPa at 30 m, or 290 kN per m². The goals are met: p = F/A; ρgh derived from the weight of the column; p = p₀ + ρgh as a line with slope ρg and constant p₀ in the text, the SVG and the sim; and force taken as a magnitude because it is perpendicular to the surface (line 10). The example, the misconceptions, the 5/4/3 exercises, the exit ticket and the sim tell one story. The theory is long, 861 words against 633 (fy3-1) and 691 (fy3-3), but the new paragraph earns its place.

## Blocking
(none)

## Polish
- exercises.json:62–67 — no task or exit-ticket item makes the student read the slope ρg or the constant p₀ from data, although that is the skill goal. — Build L2-03 from two gauge readings at two depths (ask for ρ), or add an exit-ticket question on what the slope and constant term mean.
- lesson.md:12 — the paragraph says twice that air pressure acts on the water surface. — Drop "Ilmanpaine vaikuttaa myös veden pintaan" and keep "välittyy veden kautta syvyyteen".
- lesson.md:6–14 — Ydinajatus has five paragraphs, where the gold template has three. — Merge line 12 into line 14 so the air-pressure point is made once.

## Checked
- The lint reports 0 errors and 0 warnings.
- The dam numbers are right: 1000 · 9,81 · 30 Pa = 294 kPa ≈ 290 kPa.
- The SVG axis is linear: 101 kPa at y = 150, 199 kPa at y = 52.
- Δp = p − p₀ is named once (line 27) and used consistently, including in glossary.json.
- answers.py matches all 12 answers.
- No exercise repeats the example.
- The scope stays within FY3: no vectors, no Newton's laws, no buoyancy.
- sim-spec.md matches simState (h, rho, pOver, pTotal, ratio).
- p₀ = 101 kPa and g = 9,81 m/s² are the same everywhere.
