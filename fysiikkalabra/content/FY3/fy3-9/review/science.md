VERDICT: PASS
CONTENT-HASH: c5c376b42c58397a

## Blocking

## Polish
- sim.js:53 — the sim is animated but has no speed control (hidas · normaali · nopea), which lesson-form rule 3 requires (fy3-10 and fy3-11 have one). Not a physics error — add the three-way speed control that scales `dt`.
- sim.js:55 — the explanatory note sits as plain text under the canvas instead of behind a "Lisätietoja" button. Physics is right — move it behind the button if the page template does not already do so.
- solutions.md:47 — "tulo pV on noin 10 % suurempi kuin laki ennustaa" is correct (Z ≈ 1,1 for air at 300 bar), but "laki ennustaa" is vague for students — consider "suurempi kuin ideaalikaasulla, jossa on sama määrä ilmaa".

## Checked
- All 12 answers recomputed independently (L2-03 by least squares through the origin, 2009 kPa·ml); each matches answers.py and exercises.json within tolerance, and the rounded data stays inside it.
- Inquiry numbers: kertaus (30 N; distractors 300 N, 0,030 N, 3,3·10⁸ N), pred-1 (200 kPa, pV = 5,00 J), pred-2 (106,8 kPa, 341 Pa/K, 0,34 kPa/°C), pred-3 (200/100/50 kPa), ruisku (pV 5040 vs 5430, 168 kPa, +7,7 %), virhe (252 → 250 vs 40 kPa), siirto (1,07 l; mistakes 2,10 and 0,00107; 71 %), check-2 (120; mistakes 108, 0,12).
- exp-1/exp-2: setups isolate V or θ (mode plus T or V locked); slider ranges include every requested value; simState `p`, `T` and `constant` come in Pa, K, J and Pa/K as the column labels say.
- sim.js: isothermal p = p₀V₀/V, isobaric V = V₀T/T₀, isochoric p = p₀T/T₀; speed ∝ √T; hit rate × hit size ∝ T/V; chart axes start at zero; gauge and chart ranges cover all states.
- SVG figures: p–V points satisfy x·y = 8360 (constant); 1/V points lie on the drawn line through the origin; kelvin figure scale 1,2 px/K, with points at 253–373 K proportional to T; micro model shows a 2 : 1 height ratio and 4 vs 8 hits.
- Worked example (1,036 → 1,0 l, about 30 %), misconception example (1,04 l, 3,5 %) and exit ticket (160 kPa, ratio 1,1) are correct.
- Solutions solve symbolically first; gauge versus absolute pressure is handled correctly in L3-02 (and the 216 kPa wrong-method figure) and in L3-03.
- Formulas and their conditions (fixed amount of gas, constant T/p/V, kelvins, absolute pressure) are stated and fall within FY3 scope.
