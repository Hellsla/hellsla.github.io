VERDICT: PASS
CONTENT-HASH: 3ceda54783b971b7

## Blocking

## Polish
- lessons/FY3/fy3-3/lesson-answers.py:5-9 — computes only the recap item (20 °C, 8); `g` is unused, and the numbers for virhe (128 kPa), siirto (122 kPa, mistakes 404 and 83.8), check-2 (−273 °C), check-c2 (1.035) and the worked example (0.37 kPa/°C, −270 °C, 136.6 kPa) are missing — add them and remove `g`.
- inquiry.json pr-pumppu feedback — writes $\Delta T$ for a Celsius difference given in °C; $\Delta\theta$ would match the lesson's symbols (θ Celsius, T kelvin).
- lesson.md:503 — "two significant figures": −270 °C is fine, but writing it as $-2{,}7\cdot10^2$ or saying "about" once would make the precision explicit (style).

## Checked
- I recomputed every number in one script (scratchpad r.py), using my own formulas: worked-example table vs $p\propto T$ (100·T/273.15 → 107, 115, 122, 129, 137), slope 0.37, θ₀ = −270 °C, check 136.6 kPa; virhe 128 kPa; siirto 121.7 → 122 kPa, mistakes 404 and 83.8; check-2 −273 °C; check-c2 +3.5 %; pred-1 ratio 2, speed ×1.41; pred-2 50→100. All match.
- Simulation: a 2D estimator of momentum per time per wall length, averaged over both axes, with effective box (W−2R)(H−2R) and the reference at the same lengths. My re-implementation gives 49.9/99.2/198.7 (V = 1, T = 150/300/600 K) and 49.8/198.2 (T = 300 K, V = 2/0.5) against theory 50/100/200/50/200. So p ∝ T/V comes out of the counted hits and is not hard-coded. vRel = √(T/300).
- simState gives theta, vRel, pRel and pTheory. The slider ranges and steps reach every suggested value (150, 300, 600 K; 1.0 and 2.0 dm³). exp-1 locks V and exp-2 locks T, so each isolates its parameter.
- The model's limits are stated: 2D, no particle–particle collisions, one speed set by T, measured value fluctuates. The conclusion's model answer separates model assumptions from simulation results.
- Conditions: $p\propto T$ is stated for constant V and n and a dilute gas far from liquefying (theory, summary). The limits section covers translational KE, interaction energy in liquids and solids (temperature ≠ internal energy), and motion not stopping at 0 K (guardrails).
- Causality: at constant V a temperature rise gives more frequent and harder hits; at constant T a smaller volume gives more frequent hits only. These match the theory, pred-1, pred-2, pred-3, the exit ticket and the explain model answers.
- Each choice item has exactly one correct option, and every distractor's feedback names the right reason (12× Celsius ratio, 1.4× speed, "particles expand", caloric substance, 0 °C = rest, +10 %).
- Figures: Kelvin scale is to scale (100 K = 120 px on both scales). Extrapolation axis and points within 0.5 px, p = 0 at −270 °C, axis at −300 °C as stated. Micro-model figure: same N and box, hot arrows and animation speed ≈ 2× cold. The system figure's boundary, surroundings and V span are correct.
- Scope: system, state variables, temperature, pressure as F/A and the Kelvin scale are FY3 contents. Kinetic energy is used only qualitatively in the micro model (C). The extrapolation of absolute zero matches the FY3 experimental work (Kokeellisuus).
- Photo captions (thermometer shows its own temperature, LN₂ mist is condensed water) and the check-1 value N₂ −196 °C are correct.
