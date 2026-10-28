VERDICT: FAIL
CONTENT-HASH: f53689a1dbdda5ef

## Blocking
- lesson.md:38 and lesson.md:233 — (B) the weighing masses 0,83 / 5,78 / 6,02 / 9,10 g are stated as fact ("kaasujen massat ovat…") and R is then derived "Punnitustuloksesta", but they are invented example values with added scatter (inquiry.json "punnitus": source simulated, "keksityt esimerkkiarvot"; the johtopäätös model answer says so too). Real masses are 5,81 g (N₂) and 9,17 g (CO₂), so as measurements the numbers are wrong, and theory and inquiry disagree about what the data are. Fix: mark them in the theory, e.g. "…kaasujen massat ovat esimerkkipunnituksessa (keksityt arvot, joissa punnituksen hajontaa) hyvin erilaiset…" and "Esimerkkipunnituksesta saadaan luku…".

## Polish
- inquiry.json:481 — check-2 solution writes "pV = NkT" with a Boltzmann constant k the chapter never introduces; "p ∝ NT/V (tilanyhtälöstä, kun n ∝ N)" says the same with the chapter's symbols.
- lesson.md:230 — "kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan": correct for the point-particle model as written, but the guardrail wording is "etenemisliikkeen keskimääräiseen liike-energiaan"; using it avoids a clash for the diatomic/CO₂ gases discussed in the same chapter.
- inquiry.json:389 — "2{,}0\,\text{l}" here vs \textsf{l} elsewhere (typography only).

## Checked
- Worked example recomputed: n = 101 000 Pa · 0,0050 m³ / (8,31 · 293,15 K) = 0,2073 → 0,21 mol, m = 0,83 g; molar volume check 24,1 l; staged, symbolic first, figures justified.
- R from the example data: mean m/M = 0,2071 mol → 8,32 ≈ 8,3 J/(mol·K); helium row 8,302 (mistakes 121,7 / 8302 / 0,008302 correct).
- Hot-air balloon 91 200 mol → 2645 kg → 2,64·10³ kg (mistakes 9870, 2,64 correct); 1,2 kg/m³ · 2800 m³ · 293/373 ≈ 2640 kg, ~700 kg lift realistic.
- virhe 0,083 mol (student's 1,2 mol from T = 20 K); check-2 3,0 (mistakes 2,25, 1,69); exp-2 N = 50 (mistakes 200→4,00, 71, 25→0,50); exit ticket 0,601 mol.
- Simulation table: pV/(NT) for the five rows 1,05 / 1,00 / 0,98 / 0,98 / 0,99 match p_pred = (N/100)(T/300)/V.
- sim.js: elastic wall hits, impulse 2m|v⊥| per perimeter length per time (2D pressure), v ∝ √T on temperature change, volume change leaves speeds unchanged (as Mallin oletukset says), no particle collisions (stated); exp-1/exp-2 lock T and V and vary N, simState has pMeasured and hitRate.
- Figures: mole-mass bars to scale (3,5 px/g); He : air speed arrows 2,7 : 1 = √(29/4).
- Every choice item has exactly one correct option; distractor feedback right (Boyle, "toistensa tiellä", "puristuvat pienemmiksi", "nopeammin pienemmässä tilassa").
- Model limits stated (high pressure, low temperature); Celsius/kPa/litre pitfalls correct; combined gas law with constant n.
- Hash identical at start and end.
