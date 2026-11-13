VERDICT: PASS
CONTENT-HASH: 4f14228b78fa5222
SCOPE: delta added-exercise from fe05eb0dfc9bafde base 611fb7d5c174

## Blocking
(none)

## Polish
- solutions.md fy2-7-L2-09 Vastaus — "kolme merkitsevää numeroa kuten 250 MWh": the shares read off the figure (4 %, 9 %) are whole-percent labels. The precision argument therefore rests on more than 250 MWh. The Finnish says the same. — Fix: "kuvan osuudet ovat tasaprosentteja, joten 12,5 MWh" or give 13 MWh. The tolerance already accepts both.

## Checked
- Hash taken at the start and at the end with `--lang fi-easy`; it did not change.
- fy2-7-L1-09: 0,040 × 500 kWh = 20 kWh, and 20 kWh × 3,6 MJ/kWh = 72 MJ. My recomputation, answers.py and exercises.json agree. The loss is taken as a share of the energy sent, as the task states. 1 kWh = 3,6 MJ is exact.
- fy2-7-L2-09: `fy2-7/sankey` prints 4 % lost for the grid and 9 % for district heating, with equal input widths. 0,09 × 250 MWh − 0,04 × 250 MWh = 12,5 MWh. The 3 % tolerance fits. District heating losing more than the power grid matches the lesson's qualitative picture.
- Compared with the reviewed Finnish: answer, unit, tolerance, figure, lookup, level and every number in the task text and the solution are identical.
