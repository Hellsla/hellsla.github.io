VERDICT: PASS
CONTENT-HASH: db3beb9c86a6bb71
SCOPE: delta added-exercise from 2d22792f6d7cc426 base 611fb7d5c174
Mode: delta
Round: 1

## Blocking

## Polish
- solutions.md L1-10 Järkevyys — "Joulut ovat pieniä" should say "Joulet ovat pieniä" ("joulut" means Christmases). This is language only.
- solutions.md L1-10 Vastaus — food labels use the thermochemical kilocalorie (1 cal = 4,184 J), not the international-table 4,1868 J. The difference is 0,07 %, so the answer and tolerance are unaffected (C). If you like, one clause could say that the two definitions differ slightly.
- Earlier items outside this delta (L1-09 "Pellettikattilan lämpöenergia", L1-09 Muunnokset) are still open.

## Checked
- Hash db3beb9c86a6bb71 at the start and the end. I judged only the added L1-10 and L1-11.
- L1-10 recomputed: 180 · 1000 cal · 4,1868 J/cal = 753 624 J = 753,6 kJ, the same as answers.py. The stated 754 kJ is 0,05 % away. With 4,184 J/cal the result is 753,1 kJ and with 4,2 J/cal it is 756 kJ; both are inside the 4 % tolerance.
- L1-10 solution: kcal → cal → J → kJ is done in symbols first (E = N · 4,1868 J) and the conversions are shown. The reasonableness check 180 · 4,2 kJ ≈ 756 kJ is a real check. The lookup is in the text and the hint in `hints`.
- L1-10 scope: this is a unit conversion inside "energian yksikkö" in FY2. 0,75 MJ is a realistic energy content for a chocolate bar.
- L1-11 recomputed: in the figure the tea-water point is at k = 5 (10^5 J), so 1 kJ · 10 · 10 = 100 kJ, the same as answers.py. The tolerance of 2 % fits an exact order-of-magnitude reading.
- L1-11 figure: the description gives the position (two small decades right of 1 kJ), not the value, so it carries the same information as the drawing and does not give the answer away. Every decade from 1 J to 10 TJ is evenly spaced (dx 33,2), so the figure is to scale as it says.
- L1-11 physics: about 100 kJ to boil a cup of tea (about 0,25 kg warmed by about 80 K is about 84 kJ) is the right order of magnitude. The check that a 2 kW kettle takes about a minute is consistent.
- L1-11 shares the figure with L1-05 (AA battery, lightning) and asks a different reading, so it does not repeat that task.
