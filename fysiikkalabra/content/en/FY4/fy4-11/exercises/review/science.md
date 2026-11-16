VERDICT: PASS
CONTENT-HASH: 5285b4b68c882994

## Blocking

## Polish
- solutions.md (L2-09) — the formula uses $s_\text{j}$ and $t_\text{j}$, while every other English solution uses $s_\text{b}$ and $t_\text{b}$ — use the b subscripts.
- solutions.md (L2-10, Formula) — the collision-speed expression stands after the part d sentence about $\mu$ — move it to the part c derivation.
- solutions.md (L2-10, Principle and "Limits of the model") — "the only horizontal force is friction" holds when air resistance is neglected; say so (level C, the calculator's constant deceleration implies it).

## Checked
- Diff since the passed version (bab8736584): only solutions.md of L2-10, Answer split into paragraphs before "In addition: a)", "b)", "d)", "e)"; whitespace-normalised text identical to the passed version; exercises.json and answers.py unchanged.
- All 22 numeric answers recomputed in one script with my own formulas (own fits for L2-05, L2-06, L3-04): all inside tolerance and equal to answers.py.
- L2-10 against the coordinator's source record (1 s; 9 and 1.5 m/s²; rounding to a metre): model reproduces 11/7/18, 17/15/32, 22/27/50, 28/43/71 m and ice 165/187 m.
- L2-10 c: 80 km/h stops at 49.66 m (0.3 m margin, not relied on: safe side); 100 km/h: $v^2 = 771.6 - 400.0$, $v = 69.4\,\text{km/h}$; rounded 28 m gives 69.8 km/h, inside 0.03.
- L2-10 d: ice 164.6 m and 186.8 m, six-fold as $9 : 1.5$; $\mu = 0.92$ and $0.15$; e: ABS cannot raise $\mu$, $1.25^2 = 1.56$, calculator 27 → 43 m. No energy "turned into heat".
- Multiple choice L1-06, L1-07, L2-08: one correct option each (L2-08 factor $2 : 4 = 0.50$); distractor feedback correct.
- L3-05 0.79 m, 10 kN, 18 kN; L3-06 10.5 → 11 kN inside 0.05; L3-04 $t_\text{r} = 1.21\,\text{s}$, $a = 5.10\,\text{m/s}^2$, 66 km/h.
- Figures ex-tv-jarrutus and ex-tv-tyyny give the values the solutions read.
- Hash identical at start and end.
