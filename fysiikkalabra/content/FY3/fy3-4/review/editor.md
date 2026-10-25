VERDICT: PASS
CONTENT-HASH: 48c322a6f3742eff

The lesson now tells one complete story. The dam hook (lesson.md:3) is answered in lesson.md:14: air pressure acts on both sides, so only the overpressure loads the wall, from zero at the top to about 290 kPa (294 300 Pa) at 30 m, which is 290 kN per m². The goals are met: p = F/A from the pin and the skis; ρgh derived from the weight of the column (V = Ah, m = ρV, G = mg); p = p₀ + ρgh as a line with slope ρg and constant p₀ in the text, a to-scale SVG and the sim; and force taken as a magnitude because it is perpendicular to the surface (line 10). The example, the misconceptions, the 5/4/3 exercises, the exit ticket and the sim all fit this story. The theory is long, 861 words against 633 (fy3-1) and 691 (fy3-3), with five Ydinajatus paragraphs where the gold template has three. The new dam paragraph earns its place, so the length is acceptable.

## Blocking
(none)

## Polish
- exercises.json:62–67 — the skill goal (a line with a constant term) is shown but no task makes the student read the slope ρg or the constant p₀ from data, and the exit ticket does not either. — Rebuild one task (L2-03 or an L3) from two gauge readings at two depths, asking for one quantity (for example ρ from the difference), or add an exit-ticket item: "Mitä kuvaajan (h, p) kulmakerroin ja vakiotermi kertovat?"
- lesson.md:12 — the paragraph says twice that air pressure acts on the water surface ("Veden pinnalla vaikuttaa jo…" and "Ilmanpaine vaikuttaa myös veden pintaan…"). — Drop the second clause and keep "ja välittyy veden kautta syvyyteen".
- lesson.md:6–14 — Ydinajatus has five paragraphs, and lines 10 and 12 partly overlap Kaava (line 27) and Tiivistelmä. — If length matters, merge line 12 into line 14 so the air-pressure point is made once, where the dam needs it.

## Checked
- The lint reports 0 errors and 0 warnings.
- The dam answer is right: 1000 · 9,81 · 30 = 294 kPa ≈ 290 kPa (2 sf), and the wall is loaded only by the overpressure.
- The SVG p axis is now linear: 101 kPa at y = 150 and 199 kPa at y = 52, about 1 px/kPa from y = 250.
- Overpressure is named once as Δp = p − p₀ (line 27) and is used the same way in the example, the misconceptions and glossary.json.
- answers.py matches all 12 answers at the data's significant figures.
- No exercise repeats the example (diver plus window). L2-04 uses a pressure-cooker lid, not a depth.
- The scope stays within FY3: no vectors, no Newton's laws, no buoyancy.
- sim-spec.md matches sim.js: simState has h, rho, pOver, pTotal and ratio, and the overpressure-only toggle shows the line through the origin.
- p₀ = 101 kPa and g = 9,81 m/s² are the same everywhere.
