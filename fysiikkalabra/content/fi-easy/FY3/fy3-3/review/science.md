VERDICT: PASS
CONTENT-HASH: eec751c0f8637a81

## Blocking
- none

## Polish
- inquiry.json check-2 hints[1] — "$k = …$, Paine" has a stray capital after the comma, and the hints write `\text{°C}` where the rest of the lesson writes `{}^\circ\text{C}` — make the notation consistent.

## Checked
- Full review (fi-easy, round 1). System, surroundings, closed system and state variables match the glossary. Temperature and kinetic energy are tied to a dilute gas, with the limits for liquids and solids in Mallin rajat. Absolute zero is the lowest energy and motion does not fully stop (guardrail). Temperature is kept apart from internal energy (ice and water at 0 °C).
- Conditions stated: p ∝ T only at constant V and n for a dilute gas far from condensing (theory, summary, example, siirto); the extrapolation assumes the same dependence and real gases condense before 0 K; the Kelvin relation is written as an equation of numerical values.
- Causality: at constant T the hits come more often, not harder, and at constant V they come both more often and harder. This is consistent across the lesson and the inquiry.
- Recomputed in one script: the worked example (k = 0,37 kPa/°C, θ₀ = −270,27 °C, which reports as −270 °C; the ideal check gives 136,6 kPa), pred-1 ratio 1,9995 and √2, virhe 128 kPa, siirto 121,67 kPa (mistakes 404 and 83,8), check-c2 1,035, check-2 −273 °C, misconception 3,5 %. All agree.
- Figures: extrapolation is to scale (0,945 px/°C, 1,38 px/kPa; the data points, −270 at x = 120 and the axis at −300 °C are right); kelvin-scale is to scale (100 K = 120 px on both scales).
- Sim: a 2D ideal gas where every particle has the same speed ∝ √T. The pressure comes from the counted wall momentum per wall length, so p ∝ T/V emerges and is not just computed. The window resets on a change; the limits (2D, no collisions between particles, one speed) are stated in Mallin oletukset.
- exp-1 locks V = 1,0 and varies T; exp-2 locks T = 300 K and varies V; simState gives theta, vRel, pRel and pTheory; the suggested values are on the slider grid.
- Every choice item has exactly one correct option, and the distractors' feedback is right; the explain model answers agree with the theory.
- Hash checked at the start and at the end.
