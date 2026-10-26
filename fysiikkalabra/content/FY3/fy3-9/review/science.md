VERDICT: PASS
CONTENT-HASH: 91491325ded5c903

## Blocking

## Polish
- sim.js:241 — the `tx` helper carries a stray second comment "three significant figures" (it formats with fixed decimals) — delete the stray comment.

## Checked
- All 12 exercise answers recomputed independently (one script) and compared with answers.py: all inside tolerance (67,3; 13,7; 287; 2,6; 87,3; 2,0 m³; 89,7→90 °C; 2,0 J; 890 m³; 5,9 cm³; 202 kPa; 29,9 cm). L2-03 syringe pV values 1980–2030 kPa·ml, origin fit 2009 kPa·ml.
- Solutions: symbolic before substitution; absolute vs gauge pressure handled right (L3-02, celsius/gauge traps 216 kPa and 25 °C correct); hydrostatic p₀ + ρgh from the prerequisite; the 300 bar non-ideality remark (Z ≈ 1,1 → about 1,8 m³) is realistic; freezer-lid force ≈ 7 kN correct.
- Worked example 101·0,80/78 = 1,036 l ≈ 1,0 l, +30 %; misconception example 1,04 l, 3,5 % correct.
- Figures: micro-Boyle gas heights 2 : 1 with twice the hits; boyle-graphs points really to scale for pV = 2000 kPa·ml in both (V, p) and (1/V, p); absolute-zero graphs to scale (V and p ratios 1,474 = 373/253) with extension through 0 K.
- Predictions: pV = 5,00 J, 60,2 ml and V/T = 0,171 ml/K at 80 °C, 25/50/100 ml → 200/100/50 kPa; every distractor's feedback numerically right.
- Exp-2 question: 0,171/50 = 3,41·10⁻³ 1/K = 1/293 K, linking to the lesson *Lämpölaajeneminen*; the 1/273 distractor explained correctly.
- Syringe table: pV = 5040 on four rows, 5430 (+7,7 %) at 30 ml; the implied warming is below the adiabatic limit for 40→30 ml (≈ 12 %), so the "fast compression" story is physically consistent; leak correctly rejected (would lower pV).
- Etsi virhe 252,5 ≈ 250 kPa; siirto 1,07 l, mistakes 2,10 and 0,00107; check-2 120 kPa, mistakes 108 and 0,12; kertaus 30 N and distractors; exit ticket 160 kPa and 308/280 = 1,1.
- sim.js: p, V, T from pV/T = const in all three modes; units of `constant` (J, m³/K, Pa/K) match the experiment labels; speed ∝ √T; hit rate per wall length ∝ √T/V and flash size ∝ speed give p ∝ T/V; axis ranges cover slider ranges; the model and calc boxes say pressure is computed, not counted.
- Experiments isolate their variable (exp-1 mode and θ locked, V varied; exp-2 isobaric, θ varied). Hash identical at start and end.
