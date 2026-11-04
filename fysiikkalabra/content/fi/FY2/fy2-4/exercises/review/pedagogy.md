VERDICT: FAIL
CONTENT-HASH: bb79df8de9f7fc6e

## Blocking
- exercises.json:289 (fy2-4-L3-05) and solutions.md:183 — level 3 is not met: the whole task reduces to one error diagnosis (the student divided losses instead of useful energy) and one subtraction plus one division on the last row; the other rows are decoration. It is the same table, error and method as L2-06 (E_o and E_a for a motor) one level lower. Fix: add a second stage that needs modelling of the whole table, e.g. "Lamppu palaa 3,0 h vuorokaudessa; laske vuodessa lämmöksi muuttuva sähköenergia kWh:na ja sen hinta 0,20 €/kWh" using P = E/t from the slope (9,0 W), or move the task to level 2 and write a new level 3 task from a different context.

## Polish
- exercises.json L2-06 — "data, experiment" but the answer needs only the last row (95/120); ask for the efficiency of each row or for the slope of E_a against E_o so the table is actually used. Solution then needs no "muut rivit tarkistuksena".
- solutions.md L3-05 Vastaus — "Oppilaan 70 % olisi ledille liian hyvä" is confusing (70 % is the loss share); say "70 % on häviöiden osuus, ei hyötysuhde".
- exercises.json L2-05, L2-06, L3-05 — invented measurements not marked as example data.
- solutions.md L2-06 Vastaus — key is 79,17 while the solution rounds to 79 %; harmless within tolerance, but state "noin 79 %".
- L3-04 is an excellent YO-style task; the question text runs long, so consider setting the last sentence on tuotanto as its own line.

## Checked
- Data tasks at level 2: L2-05 (table) and L2-06 (table) = 2; plus MC L2-07; matches the plan.
- L3-04 (unit conversion, two efficiencies, useful vs taken energy, scope limit) is a genuine modelling task; recomputed 192 MJ = 53,3 kWh, ratio 3,1, useful 15,3 and 13,3 kWh.
- L2-05 (5, 10, 20, 30 %; ratio 3,0), L2-07 (75 % vs 80 %), L3-05 (30,09 %) recomputed correct.
- New L1 tasks: L1-06 MC with misconception distractors and repairing feedback; L1-07 (9,0 kJ) and L1-08 (200 kW) correct.
- Solutions are complete and followable.
- Only 1280 px exercise captures exist; 360 px layout covered by deterministic checks.
