VERDICT: PASS
CONTENT-HASH: 03c6dfd77e8da8ce

## Blocking

## Polish
- lesson.md:8 — "ne osuvat seinämiin kaksi kertaa niin usein" is strictly true per unit wall area — write "osuvat jokaiseen seinämän kohtaan kaksi kertaa niin usein" or similar.
- lesson.md:134–136 — `T = \theta + 273{,}15\,\text{K}` adds a pure number to a kelvin quantity, patched by "lukuarvona"; `T/\text{K} = \theta/{}^\circ\text{C} + 273{,}15` would be dimensionally clean.

## Checked
- Formulas p₁V₁ = p₂V₂, V₁/T₁ = V₂/T₂, p₁/T₁ = p₂/T₂: correct, with conditions stated (fixed amount, kelvins, total not gauge pressure); within the FY3 content "kaasujen tilanmuutokset" and the Boyle lab in docs/lops2019; no Newton's laws, no pV = nRT.
- Pa·m³ = N·m = J and 1 kPa·1 l = 1 J correct; kPa/litre use on both sides valid.
- Worked example: V₂ = p₁V₁/p₂ solved symbolically, then substituted with units; 1,036 l ≈ 1,0 l (2 s.f.), +30 %; 78 kPa cabin pressure realistic; taut-bag pressure correctly stated as above cabin pressure.
- Misconception numbers: 1,00 l · 293/283 = 1,04 l (+3,5 %); exit ticket 160 kPa and ×308/280 = 1,1 correct.
- All 12 answers.py lines model their problem text (formula, kelvin conversion, gauge ↔ absolute, bar → kPa, l → m³, kPa·ml → J). Recomputed by hand: L2-03 least-squares slope through origin 2009 kPa·ml = 2,0 J (pV 1980–2030 kPa·ml); L3-02 351 → 303,1 kPa absolute, gauge 202 kPa (216 kPa if the reading is used, as stated); L2-04 2800 · 373,15/283,15 − 2800 = 890 m³.
- Solutions: each solves the unknown symbolically first; side claims correct (≈7 kN on a 0,5 m² lid, 2020 l / 50 l/min ≈ 40 min, Z ≈ 1,1 at 300 bar → ≈1,8 m³, ~¼ of heated air expelled, 3/4 of pump stroke spent compressing).
- Magnitudes realistic (water rocket, tyre, SCBA, balloon, dive, sauna).
- Figure 1: gas heights 2 : 1, equal speed arrows, 4 → 8 hit marks.
- Figures 2–3: all (V, p) points have xy = 8360 (hyperbola); (1/V, p) points on the drawn origin line (slope 0,917); T-figure 1,2 px/K, points 253–373 K with V ∝ T, dashed extension reaches 0 K.
- sim.js uses the exact laws p = p₀V₀/V, V = V₀T/T₀, p = p₀T/T₀; speed ∝ √T; constants converted correctly to SI (kPa·ml·10⁻³ = J, ml/K·10⁻⁶, kPa/K·10³); chart ranges contain all states; dashed extension only for the proportional plots.
