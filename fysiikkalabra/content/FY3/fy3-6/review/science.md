VERDICT: PASS
CONTENT-HASH: 2241eb647ba8f7e1

## Blocking

## Polish
- inquiry.json (tarkistus-3 criterion 1): "noin viisinkertainen hiekkaan tai maahan verrattuna". The factor of 5 holds for dry sand (800 J/(kg·K)), but moist soil has c ≈ 1000–2000 J/(kg·K). Fix: say "kuivaan hiekkaan" (carried over).
- sim.js:1007: the material dropdown no longer shows c beside each name. The label above it still prints $c_\text{k}$ for the selected material, so no information is lost. Optional fix: show c in the options again if students should compare values before choosing.

## Checked
- Test diff (tests/sims/fy3-6.json, 31bb150): the five rewritten assertions check the same physics as before. They still check T = 24,6 °C, C = 1257 and 77,0 J/K, Q = 5,80 kJ given and taken (split count 3), ΔT 4,6 / 75,4 K, the reverse-flow case (17,2 kJ, 19,1 °C), the chart scale 20–100 °C, the slider labels and the equal-temperature message. They now read exact TeX through simText. The old checks `l[0].includes('m')` and a bare "19,1 °C" were replaced by stricter strings. No physics check was lost. I recomputed 17,2 kJ / 19,06 °C myself.
- sim.js diff: formatting only (fi → tx, `$…$` strings). Teq, Q, QW, the heat capacities, the decay law and simState did not change. The Unicode minus inside TeX only affects values that are never negative here.
- The 1280 px and koe-2 screenshots: the KaTeX canvas labels, axis ticks, $T$ line label and readout render with no stray `$`. Values match the model (24,6 °C; 40,0 °C at 0,20 kg).
- All 12 exercise answers recomputed independently. They match answers.py and exercises.json within tolerance.
- solutions.md solves each unknown symbolically before substituting, and every side check is correct (3,4 K, 8,7×, 5,2×, 0,60, 7,5×, 68 / 9 K, 3,5 min).
- The worked example (5656,5 J, 374,6 J/(kg·K), 383 at 24,6 °C, copper 24,6 °C, 1257 / 75 J/K) and the misconception section (35 °C, ≈9×) are correct.
- Figures: the ΔT bars are to scale (105/20 = 5,25 ≈ 4190/800), c-bars are to scale within 0,5 %, and the calorimeter figure matches the worked example.
- ennuste-1 / koe-1: 26,8 / 44,0 °C, 8,5 / 30 kJ, 160 / 838 J/K. ennuste-2 / koe-2: 40,0 / 55,0 / 63,1 °C. Each experiment varies one parameter, and simState gives Teq and CB.
- virhe (6,6 vs 30,0 °C, Kelvin shift invariant), siirto 29,1 kg (mistakes 220 and 21,3), tarkistus-1 4500 vs 838 J/K, tarkistus-2 891 (mistakes 768 and 501) and the exit ticket (419 kJ, ≈9×, 50 / 65 °C) are all verified.
- The howto/model/calc boxes state the sim's limits correctly: lossless, no phase change, τ = 1,5 s is only an illustration, the speed changes the pace only, and the chart scale rule is given.
