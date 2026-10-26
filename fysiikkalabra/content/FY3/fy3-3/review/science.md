VERDICT: PASS
CONTENT-HASH: 0aaf01ed9efec6be

## Blocking

## Polish
- inquiry.json:510, 548 (exp-1, exp-2 intro) — the pressure window is 1,5 s of simulated time, so at "hidas" it takes 3 s of real time to refresh, and after a volume change the bunched particles keep the reading 10–20 % off for several seconds; "pari sekuntia" is short — say "muutama sekunti", or clear `hist` when V changes.
- sim.js:1014 — `lastT` is no longer used since the fixed-step speed control; remove it.

## Checked
- Round-2 conversion: every changed string compared with the previous version (pred-1 feedback 600 K / 300 K = 2; virhe option 313 K / 293 K ≈ 1,07 → 128 kPa; siirto mistake 80/20 = 4 and 353 K / 293 K ≈ 1,20; check-2 table −123/27/177 °C → 50/100/150; exp-1/exp-2 $v$): no number, formula or meaning changed.
- lesson.md: "ja lämpötila pysyy samana" makes the compression sentence correct (at constant T a single hit is no harder); nothing else in lesson.md changed.
- siirto Järkevyys now matches the task: closed at 20 °C, heated to 80 °C → 122 kPa > 101 kPa outside, lid pushed outward. Correct.
- All 12 exercise answers recomputed independently = answers.py = exercises.json (L1-05 −270,45 → −270; L2-04 3,996 → 4,0; L3-03 −126,575 → −127); solutions symbolic first, units right.
- Worked example: k = 0,37 kPa/°C, θ₀ = −270 °C, symbolic solve before substitution, liquefaction caveat stated.
- Extrapolation figure to scale (0,945 px/°C, 1,375 px/kPa; all six points and the p = 0 crossing at −270 °C); kelvin figure to scale; system and micro-model figures right.
- Inquiry: pred-1 ratio 2 with vRel 1,41; pred-2 50 → 100 with vRel 1,00; pred-3 count and size unchanged; virhe 128,2 kPa; siirto 121,7 → 122 kPa, mistakes 404 and 83,8 right; check-2 −273 °C, mistakes 0 and −123 explained right; check-1, check-3 model, exit ticket, misconception 293/283 ≈ 1,035.
- sim.js: v ∝ √T so mean KE ∝ T; pressure from wall momentum per time per effective length, reference on the same lengths; pTheory = 100·(T/300)/V. Speed control advances fixed DT = 1/60 s steps of simulated time, window 90 steps, so speed changes only pace.
- exp-1 locks V, varies T; exp-2 locks T, varies V; initial states and suggested values inside slider ranges; simState gives theta, vRel, pRel, pTheory.
- Scope inside FY3; p ∝ T at constant V and n stated with its conditions.
