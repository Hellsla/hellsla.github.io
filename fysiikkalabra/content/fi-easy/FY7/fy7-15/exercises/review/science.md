VERDICT: PASS
CONTENT-HASH: 0e56d53720367ec8

## Blocking

## Polish
- solutions.md:255 (L2-08) — "Hyvä vastaus on 43–46°" is wider than the tolerance 0.03 allows (42,9–45,5°): 46° is not accepted — write 43–45° or widen the tolerance to 0.04.
- solutions.md:234 (L1-10) — "Hyvä vastaus on 260–280 W/m²" against tolerance 0.04 (257,7–279,1 W/m²): 280 falls just outside — write 260–279 or set the tolerance to 0.045.
- exercises.json:318 / solutions.md:258 (L2-09) — reflected light is partly polarised only at oblique incidence (not when the camera looks straight at the glass); the task implies it ("himmenee selvästi") and the brief's lesson states the claim the same way, so this is a fair simplification (C). Optionally add "vinosti" to the situation.
- exercises.json:359 (L3-04) — still carries "Aineisto on esimerkkiaineisto." after it was removed from L2-05 and L2-06; remove it for consistency if the teacher's rule (no provenance line on example data) is meant for the whole set.

## Checked
- Hash identical at start and end (0e56d53720367ec8), same as the packet.
- All 22 numeric answers recomputed in one script with my own formulas (Malus, halving, Brewster, Snell for L2-04, own least-squares fits for L2-05 and L2-08, numeric maximum for L3-04): all agree with exercises.json and answers.py output.
- L2-09 (new, core, qualitative): physics correct. Reflection from glass is partly polarised parallel to the surface; filter axis perpendicular to it absorbs most; unpolarised light from the goods passes about half at every orientation; a quarter turn restores the reflection; "ei katoa kokonaan, koska vain osittain polarisoitunutta" correct. No Malus or Brewster calculation needed, so it fits the qualitative core path; answers.py has a comment only (no number), as it should.
- L2-05 and L2-06 after the removed sentence: data, answers and tolerances unchanged; fit gives slope 313,9 lx and intercept 6,9 lx; without background subtraction 322 lx falls outside the 1,5 % tolerance, as the solution says. L2-06 points scatter around cos² θ realistically.
- L1-09 ordering: D 100 < E 125 < A 150 < B 200 < C 240 W/m².
- L1-06: exactly one correct option; each distractor is wrong and its feedback gives the right reason.
- L3-02: 36,9° is below the critical angle 48,8°; L2-07: 36,3° is the refraction angle and the inside-to-air Brewster angle.
- L3-05: Sun's elevation 36,9°, θ = 65,0°, 7,14 W/m²; thresholds 56,8° and 33,2° correct; unpolarised comparison (50 % against 30 %) correct.
- L3-04: model 0, 30, 90, 120, 90, 30, 0 W/m² against the table; 1/8 = 12,5 % exact.
- L1-11: crown glass n = 1,520 matches the verified MAFY value list; Brewster n₁/n₂ assignment matches the lesson's definition in every solution; notation (α_B, n₂ : n₁, I₀, E in lx) as in the brief.
