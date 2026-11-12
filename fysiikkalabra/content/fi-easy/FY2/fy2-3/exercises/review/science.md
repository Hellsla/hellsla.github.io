VERDICT: PASS
CONTENT-HASH: e71fed8737775da9
SCOPE: delta added-exercise from 0dd670b21be99b54 base 611fb7d5c174

## Blocking
(none)

## Polish
- solutions.md fy2-3-L1-09 Järkevyys — "vähän suurempi kuin vedenkeittimen teho": 3,7 kW is close to twice a typical 2 kW kettle. The Finnish says the same. — Fix: "lähes kaksi vedenkeitintä" (nearly two kettles), in both languages.

## Checked
- Hash taken at the start and at the end with `--lang fi-easy`; it did not change.
- fy2-3-L1-09: 5,0 hp × 735,5 W/hp (metric horsepower, which the task names) = 3677,5 W. Then 3677,5 W × 1800 s = 6,62 MJ. My recomputation, answers.py and exercises.json agree. The solution rearranges ΔE = PΔt symbolically first. It uses P constant ("täydellä teholla tasaisesti"), which the task states. 6,62 MJ = 1,84 kWh is correct. The ±4 % tolerance fits.
- fy2-3-L1-10: on `fy2-3/graph-ab`, A runs from the origin to (80 s; 120 kJ), giving 1500 W. B runs from the origin to (80 s; 40 kJ), giving 500 W. The ratio is 3,0. All the points the solution reads lie on the drawn lines and on gridline crossings. The slope is the power because the conversion is steady, as the task says.
- Compared with the reviewed Finnish: answer, unit, tolerance, figure, lookup, level and every number in the task text and the solution are identical.
