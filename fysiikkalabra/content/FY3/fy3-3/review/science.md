VERDICT: FAIL
CONTENT-HASH: cabf3911941dad86

## Blocking
- exercises.json:64 (also solutions.md:58–62, answers.py:13–14) — L2-03 data (110 kPa at 10 °C, 130 kPa at 80 °C in a rigid closed container) are not physically possible: the line through them reaches p = 0 at 10 − 110/0,2857 = −375 °C, which is below absolute zero, and an ideal gas would be at 110 · 353,15/283,15 = 137 kPa. This contradicts the lesson's central claim that extrapolation gives −273 °C. The solution's Järkevyys line ("absoluuttiseen nollapisteeseen on vielä matkaa") hides the problem. — Change 130 kPa to 137 kPa. Then k = 0,3857 kPa/°C and p(−50 °C) = 86,9 kPa, so answer 87. Update answers.py and the solution to match.

## Polish
- inquiry.json:285 — siirto Järkevyys: "Siksi kuumana suljettu purkki voi olla vaikea avata vasta jäähdyttyään" describes the reverse process (sealed hot, then cooled), so "Siksi" doesn't follow from this jar, which was sealed cold and heated. — Present it as the reverse case: "Käänteisesti…".
- exercises.json L3-01 — 300 kPa for a bike tyre reads like a gauge overpressure, but p ∝ T holds only for absolute pressure. — Add "(absoluuttinen paine)" or use about 400 kPa.
- inquiry.json:96 — pred-2 last option: in the sim only the piston walls get hit more often. On the top and bottom walls the hit rate stays the same and only the wall length shrinks. The feedback merges the two. — Optional rewording.
- sim.js — has no hidas/normaali/nopea speed control (lesson form 3). — Add one (pedagogy may own this).

## Checked
- All 12 exercise answers recomputed independently; they match answers.py and exercises.json, and every one is inside its tolerance.
- Worked-example table matches p ∝ T (107,3 … 136,6 kPa). k = 0,37 gives θ₀ = −270 °C. SVG plot coordinates are to scale (axis at −300 °C, zero at x = 107).
- The kelvin/celsius SVG is to scale (1,285 vs 1,29 px/unit).
- sim.js: 2D impulse per wall length gives N v²/(2 Wc Hc), so pRel equals pTheory = 100 (T/300)/V exactly, and v ∝ √T.
- pred-1, pred-2, pred-3: the correct options and the numbers in the feedback (300→600 K, 50→100, √2 ≈ 1,41) agree with the sim.
- exp-1 and exp-2 vary one variable and lock the other. Their initial values are within the slider ranges, and simState provides theta, vRel, pRel and pTheory.
- virhe: 128 kPa. siirto: 122 kPa; the mistake values 404 and 83,8 are correct. check-2: −273 °C; mistake feedback is correct.
- check-1, check-3 model answer, exit ticket and glossary physics are correct (N₂ boils at −196 °C, 10→20 °C is a 3,5 % rise).
