VERDICT: PASS
CONTENT-HASH: 166934baf35a42f6

## Blocking
- none

## Polish
- lesson.md Key idea — "The temperature of a gas tells you the average kinetic energy of the particles" is stated before its limits; the *Limits of the model* subsection restricts it correctly (dilute gas, translational motion), so C. "translational" could be added at first use if the text is edited anyway.
- sim.js readout — decimal comma ({,}) on the English page; language/visual, not physics.

## Checked
- Full review (changed line with a number/formula, proofreading round 1): hash equal at start and end.
- Definitions: system, surroundings, closed system, state variables (T, p, V, n), pressure as force per area, Kelvin scale, absolute zero ("kinetic energy smallest, motion does not stop entirely") — all match the guardrails.
- Model conditions: p ∝ T only for constant V and n and a dilute gas far from liquefying — stated in theory, summary, check-3 model and siirto principle; liquid/solid temperature vs internal energy (ice/water at 0 °C) correct.
- Causality: compression → more frequent, not harder, collisions; heating → more frequent and harder; pred-1 feedback 1.41·1.41 ≈ 2 correct.
- Recomputed in one script: pred-1 600 K/300 K = 2, v ratio 1.414; pred-2 50 → 100; worked example k = 0.37 kPa/°C, θ₀ = −270 °C, check 136.6 kPa; table matches p ∝ T within rounding; virhe 128 kPa; siirto 121.7 → 122 kPa and mistakes 404, 83.8; check-c2 1.035; check-2 −273 °C (table = model at 150/300/450 K, reachable with the 10 K slider step).
- Worked example: line equation solved symbolically for θ₀ before substitution; slope from two points justified; extrapolation flagged as model beyond the measured range and real gases liquefy first.
- Figures: kelvin-scale "to scale" verified (0 K at x = 70, 273.15 K at 398, 373.15 K at 518: 1.20 px/K throughout); extrapolation graph points and dashed line land on −270 °C and the data within a pixel.
- Simulation: 2D, no particle-particle collisions, one speed ∝ √T — all stated in the model box; measured pressure from wall impulses per length agrees with p ∝ T/V (reference uses the effective box); speed control changes pace only; settling handled.
- Experiments: exp-1 locks V, varies T, measures theta, vRel, pRel, pTheory; exp-2 locks T, varies V — simState carries every key.
- Assessment: one correct option per choice item; liquid-nitrogen caption (condensed water droplets) and nitrogen −196 °C correct.
