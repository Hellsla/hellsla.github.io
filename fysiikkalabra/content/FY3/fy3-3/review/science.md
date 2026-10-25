VERDICT: PASS
CONTENT-HASH: a8b10444aa1808d4

## Blocking

## Polish
- sim.js:945 — at 150 K (the low value exp-1 suggests) the 1,5 s window holds few collisions, so measured p swung 41–62 around theory 50 in a headless run (±20 %); at 300–600 K it stays within about ±5 % — optionally lengthen WINDOW (e.g. 180 frames) or scale it with 1/v so the low-temperature reading is steadier.
- inquiry.json check-2 solution — $k = \tfrac{1}{3}\,\text{1/°C}$ mixes the relative pressure unit away; writing "1/3 per °C (suhteellista yksikköä)" would be cleaner.

## Checked
- answers.py vs own recomputation: all 12 answers agree and lie within tolerance (L2-03 now 86,86 → 87 kPa from the corrected data).
- Worked example: endpoint slope 0,37 kPa/°C, θ = −p₀/k ≈ −270 °C (least-squares fit −271 °C); symbolic before substitution; graph coordinates match the data (1,25 px/°C, 1,5 px/kPa, axis at −300 °C).
- Kelvin/Celsius figure is to scale (373,15 K at x ≈ 540).
- Formula T = θ + 273,15, p ∝ T at constant V and n, ⟨E_k⟩ ∝ T: conditions stated, within FY3 scope; liquefaction caveat on extrapolation present.
- pred-1 (300→600 K, ×2; speed ×1,41), pred-2 (V 2→1 dm³, p 50→100, vRel 1,00), pred-3 feedback consistent with the model.
- exp-1/exp-2 isolate the varied parameter (V or T locked); simState provides theta, vRel, pRel, pTheory; Playwright: p ≈ 202/200 at 600 K, 47/50 at 2 dm³, 192/200 at 0,5 dm³.
- sim.js pressure: mean over both axes gives N v²/(2A) exactly, reference uses the same effective box; p ∝ T/V.
- siirto 121,7 → 122 kPa; mistakes 404 and 83,8 match the named errors; virhe 128 kPa.
- check-2: −123/27/177 °C → 150/300/450 K, zero at −273 °C; mistakes 0 and −123 explained correctly.
- Misconception 293/283 ≈ 1,035; L3 Järkevyys counter-examples (36 °C, 10 °C) correct.
