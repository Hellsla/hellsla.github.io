VERDICT: PASS
CONTENT-HASH: 59d72cf4add3289c

## Blocking

## Polish
- solutions.md:87 — "Muutama kauhallinen jäähdyttää kiviä kymmeniä kelvinejä": under the task's assumption, one ladle alone gives 27 K, so a few ladles would give about 80 K or more. — Say that the real stove keeps heating the stones.
- solutions.md:23 (L1-03) — 45 kg/m² is about 5 cm of ice in one night, which is generous for a first frost night. — About 25 kg/m² (2–3 cm) would be more typical.

## Checked
- The round-1 blocker is fixed. check-2 now has a plateau from 2,0 to 17,0 min, so 900 s gives 0,597 kg. The 120 s warm-up gives 180 kJ, about 72 K on 0,597 kg, which is physically possible. Hint 3, the whole-time mistake (0,677 kg, 17,0 min) and the latent-heat mistake (4,04 kg) are all consistent.
- All 12 exercise answers recomputed in one script. They match answers.py exactly and stay within the 2 % tolerance.
- Worked example: r = Pt/Δm = 2,34 MJ/kg, solved symbolically first. The loss reasoning is correct.
- Lesson numbers: r/s ≈ 6,8; r vs. heating 0→100 °C ≈ 5,4; melting ≈ heating 0→80 °C.
- Heating-curve SVG: segments are proportional to s : cΔT : r. Ice and steam slopes are about 2× the water slope.
- sim.js: the stage energies, stateAt, the sm/P and rm/P plateaus and the phase fractions are correct. simState gives tMelt and tBoil.
- exp-1 and exp-2 isolate P and m. The feedback numbers (83,5 / 565 / 167 / 1130 s, ratio 6,8) match the model.
- pred-1, pred-2 and pred-3 have the correct options. pr-lampo (210 kJ), virhe (66,8 kJ) and siirto (188 W, mistakes 27,8 W and 11 300 W) are correct.
- check-3 model answer: 2260 + 264 J against 264 J, correct.
- Exit ticket and the pressure dependence of the boiling point are correct and within scope.
