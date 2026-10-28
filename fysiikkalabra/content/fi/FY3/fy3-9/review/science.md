VERDICT: PASS
CONTENT-HASH: 532dc0152871b210

## Blocking

## Polish
- content/FY3/fy3-9/sim.js:174 — `p.textSize(ts(9))` before the needle is left over from the removed dial numbers and draws nothing. Delete it.
- content/FY3/fy3-9/sim.js:238–240 — `fi()` is still unused, and the stray duplicate comment "three significant figures" still trails `tx`. Delete both (carried over from round 1).
- content/FY3/fy3-9/review/shots/fy3-9-sim-1280.png, fy3-9-sim-390.png — these captures still show dial numbers and "kPa" on the gauge face, but the current sim.js draws neither (checked with a fresh Playwright render of the preview). Regenerate the shots so the pedagogy reviewer judges the current gauge.
- content/FY3/fy3-9/inquiry.json (simulaatio, model) — the gauge and readout show the gas's absolute (total) pressure, 100 kPa at the start. Lesson.md tells students to use total pressure, not the gauge's overpressure. One clause in `model` ("mittari näyttää kokonaispaineen") would keep the two from seeming to contradict each other.

## Checked
- I recomputed all 12 exercise answers independently. Each agrees with answers.py and exercises.json within tolerance: 67,3; 13,7; 287; 2,6; 87,3; 2,0; 90; 2,0 (least-squares fit, 2009 kPa·ml); 890; 5,9; 202; 29,9.
- Worked example (1,036 l, +29,5 %), siirto (1,07 l; mistake 2,10 l; 71 %), check-2 (120 kPa; mistakes 108 and 0,12), exit ticket (160 kPa; 308/280 = 1,1), misconception (1,035 → 1,04 l): all correct, and every one is solved symbolically first.
- inquiry: pred-1 (200 kPa, pV = 5,00 J), pred-2 (60,2 ml, 0,1706 ml/K), pred-3 (the curve) and the γ question (1/293 K = 3,41·10⁻³ 1/K) are correct. In ruisku, pV = 5040 except at 30 ml (5430, +7,7 %), and heating is the correct reason. The kertaus answer is 30 N.
- New gauge (fresh render, 1280 and 390 px): the needle angle is 135° + 270°·p/300 kPa, so 100 kPa sits at 225°. The reading `100,0 kPa` above the gauge equals simState.p. The needle never clips: the maximum is 250 kPa when isothermal and 144 kPa when isochoric, both under 300.
- The phone label scaling (k = 1,85 at 390 px) only thins the tick labels. Every label that remains still has the right value at the right position: thermometer −50/50/150 °C, chart axes 0–300 kPa and 40/80 ml.
- The sim physics is unchanged: pV/T = const in all three modes, the SI conversions of `constant` are correct, and the axis maxima cover the slider ranges. Fresh simState: isochoric p/T = 341,1 Pa/K = 100 kPa/293,15 K.
- Experiments: exp-1 locks mode and Tc and varies Vml. exp-2 locks mode and varies Tc. The adapter supplies p, constant, T, Vgas and VperT in the units the tables state.
- Figures are to scale (I checked their coordinates): boyle-graphs (pV = 2000 kPa·ml), absolute-zero (253–373 K points, slope 0,449 to the origin in both panels), micro-boyle (heights 2 : 1, hit marks 4 → 8).
- Scope: Boyle's law and the isobaric and isochoric changes fall under "kaasujen tilanmuutokset" and the Boyle experiment. L3-01 uses ρgh from fy3-4.
