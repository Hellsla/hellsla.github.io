VERDICT: PASS
CONTENT-HASH: afa2083a19a7066f

## Blocking

## Polish
- sim.js:940 — at 150 K (the low value exp-1 suggests) the 1,5 s window holds few collisions, so measured p swings roughly ±20 % around theory 50; at 300–600 K it stays within about ±5 %. Optionally lengthen WINDOW (e.g. 180 frames) or scale it with 1/v.
- inquiry.json check-2 solution — $k = \tfrac{1}{3}\,\text{1/°C}$ drops the relative pressure unit; "1/3 suhteellista yksikköä per °C" would be cleaner.

## Checked
- Changed Ydinajatus sentence (forward pointer to fy3-9 on p, V, T): physically neutral. The direct proportionality p ∝ T at constant V and n stays stated in the paragraph and Tiivistelmä, within FY3 scope.
- answers.py against my own recomputation: all 12 answers agree and lie within tolerance (e.g. L2-03 86,86 → 87 kPa, L2-04 3,996 → 4,0, L3-03 −126,6 → −127 °C).
- Worked example: endpoint slope 0,37 kPa/°C, θ = −p₀/k ≈ −270 °C (least-squares fit −271 °C). Solved symbolically before substitution. Graph coordinates match the data, and the liquefaction caveat is present.
- The Kelvin/Celsius figure is to scale. T = θ + 273,15 and ⟨E_k⟩ ∝ T are correct, with their conditions stated.
- pred-1 (300 → 600 K, p ×2, speed ×1,41), pred-2 (2 → 1 dm³, p 50 → 100, vRel 1,00) and pred-3 feedback are consistent with the model.
- exp-1 and exp-2 isolate the varied parameter (V or T locked). simState gives theta, vRel, pRel and pTheory. sim.js is unchanged since the last PASS; its pressure is N v²/(2A) with the same effective box as the reference, so p ∝ T/V.
- siirto: 121,7 → 122 kPa. Mistakes 404 and 83,8 match the errors they name. The virhe item gives 128,2 → 128 kPa.
- check-2: zero at −273 °C. Mistakes 0 and −123 are explained correctly.
- Misconception: 293/283 ≈ 1,035. The L3 Järkevyys counter-examples (36 °C, 10 °C) are correct.
- Solutions: the unknown is solved symbolically before substitution, and units and magnitudes are realistic (liquid N₂ −196 °C, CMB −270 °C).
