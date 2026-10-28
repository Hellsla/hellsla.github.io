VERDICT: PASS
CONTENT-HASH: bfbcfbf827b20b90

## Blocking

## Polish
- content/fi/FY3/fy3-8/lesson.md:255 — the worked example's problem gives "12 · 10⁻⁶ 1/K" as plain text and "+$30\,{}^\circ\text{C}$" with the plus sign outside the math, while every other value with a unit is inline LaTeX — write `$12 \cdot 10^{-6}\,\tfrac{1}{\text{K}}$` and `$+30\,{}^\circ\text{C}$`.
- content/fi/FY3/fy3-8/lesson.md:165 — "Kaasun hiukkaset ... lähes vapaita, joten vakiopaineessa kaasun tilavuus kasvaa paljon enemmän" names the absence of restraint but not the push: faster particles hit the walls harder, so at constant pressure the gas expands until the pressure is the same again. Fair at this level (the chapter on gas changes returns to it); one clause would complete the cause.

## Checked
- One Python run recomputed every number: example ΔL = 86,4 mm → 86 mm, αΔT = 0,072 %; pred-1/pred-2 6,00 mm, 12,0 mm, 0,0600 %; virhe 28 mm vs 1,84 mm (×15, 0,7 %); siirto 44 mm (mistakes 0,044 and 110 mm; glass 40× smaller; 42,9 mm with glass); check-2 α = 23·10⁻⁶ 1/K from both columns (mistakes 46 and 15,3); check-3 air γ / steel 3α ≈ 94 ("noin sata"); exit ticket 21 mm; interpret table 0,36 / 2,1 / 11 / 34 cm³.
- Tables: α and γ values realistic; air γ = 3,4·10⁻³ 1/K = 1/293 K at 20 °C and constant pressure.
- Guardrail conditions stated: linear formulas for solids over about 100 K, liquids' γ only near the 20 °C of the table, γ ≈ 3α for small changes, gases at constant pressure.
- Mechanism: asymmetric interaction (repulsion steep, attraction weakens gradually) explains the growth of the mean spacing; particles do not grow; Cem's symmetric-vibration distractor is correctly refuted; the sim box says it sets the spacing from the formula and draws symmetric vibration.
- Water anomaly 0–4 °C, density maximum at 4 °C, lakes freeze from the top: correct in theory, virhekäsitys and check-1 (exactly one correct option).
- Experiments: exp-1 locks material and L₀ and varies T; exp-2 locks material and T and varies L₀; simState gives dT, dL (m) and rel.
- Simulation implements ΔL = αL₀ΔT from 20 °C with the lesson's α values, exaggeration 100× stated, "alle 0,3 %" true (max 0,23 %).
- Exactly one correct option in every choice item; each distractor's feedback right.
- Hash identical at start and end.
