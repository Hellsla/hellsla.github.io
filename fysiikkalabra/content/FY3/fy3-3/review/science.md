VERDICT: PASS
CONTENT-HASH: 433bf9f742e703d1

## Blocking

## Polish
- lesson.md:51 — "Kun tilavuus pienenee … paine kasvaa, mutta yksittäinen törmäys ei muutu kovemmaksi" holds only at constant temperature (a real compression warms the gas) — add "ja lämpötila pysyy samana".
- inquiry.json:287 — siirto solution, Järkevyys: "Siksi kuumana suljettu purkki voi olla vaikea avata…" describes the reverse case (closed hot, then cooled), not the task's (closed at 20 °C, then heated); "Siksi" does not follow — make it a separate remark ("Vastaavasti…").
- inquiry.json:179 / sim.js — after a volume change the particles stay bunched, so the 1,5 s window reads 10–20 % off for several seconds (measured 0,5→2,0 dm³: 42–60 vs theory 50; 2,0→1,0 settles faster). "Pari sekuntia" is short at "hidas" — say "muutama sekunti", or clear `hist` when V changes.

## Checked
- All 12 exercise answers recomputed independently = answers.py = exercises.json (L1-05 −270,45→−270; L3-03 −126,575→−127; L2-04 3,996→4,0); solutions symbolic first, units right.
- Worked example: k = 0,37 kPa/°C, θ₀ = −270 °C (least-squares fit −271 °C); symbolic solve before substitution; liquefaction caveat stated.
- Extrapolation figure: every point, tick and the p = 0 crossing at −270 °C to scale (0,945 px/°C, 1,375 px/kPa); vertical axis at −300 °C as the text says.
- Kelvin figure to scale (1,20 px/K both intervals); system and micro-model figures correct.
- Inquiry: pred-1 300→600 K ratio 2 (sim 100→200, vRel 1,41), pred-2 50→100 with vRel 1,00, pred-3 particle count/size unchanged; all feedback numbers right.
- virhe 128 kPa, siirto 121,7 → 122 kPa (mistakes 404 and 83,8 right), check-2 −273 °C (mistakes 0 and −123 explained correctly), check-1, check-3 model, exit ticket, misconception 3,5 %.
- sim.js: speed ∝ √T so mean KE ∝ T; pressure = wall momentum per time per length, averaged over both axes (exact for fixed directions); reference uses effective lengths; pTheory ∝ T/V. New "Nopeus" control advances fixed DT steps in simulated time.
- Sim run in Chromium with the current sim.js at speeds 0,5/1/2: measured p tracks theory (300 K 1 dm³ ≈ 100, 600 K ≈ 200, 0,5 dm³ ≈ 200) independent of speed.
- exp-1 locks V and varies T; exp-2 locks T and varies V; initial states and suggested values inside slider ranges; simState gives theta, vRel, pRel, pTheory.
- Scope inside FY3; p ∝ T at constant V stated with its conditions.
