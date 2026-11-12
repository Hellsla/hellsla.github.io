VERDICT: PASS
CONTENT-HASH: a1fbb6ffcc68c242
SCOPE: delta added-exercise from be130260722cc92a base 611fb7d5c174
Mode: delta
Round: 1

## Blocking

## Polish
- solutions.md fy2-4-L1-09 Vastaus — "eri taulukoiden arvot poikkeavat hieman … ±4 %" does not hold for light fuel oil. Motiva and Tilastokeskus give about 42,7 MJ/kg, and that gives η = 74,9 %, which is 5 % off and outside the tolerance. The task does point to MAFY (40,6, docs/mafy-arvot.tsv VERIFIED), so this is C, but say that the answer expects the MAFY value, or widen the tolerance to 0,06.
- fy2-4-L2-09 — η = 25 % is low for an electric motor (typically 70–90 %). It fits a small hobby motor (C). The figure is shared with L3-03, so keep it, but you could add "pieni leikkimoottori" to the text.

## Checked
- Hash a1fbb6ffcc68c242 at the start and the end. I judged only the added L1-09 and L2-09.
- L1-09 recomputed: E_o = Hm = 40,6 MJ/kg · 2,5 kg = 101,5 MJ and η = 80 : 101,5 = 0,788 = 78,8 %, the same as answers.py. The stated 79 % is 0,3 % away. H = 40,6 MJ/kg is the MAFY LHV value (docs/mafy-arvot.tsv, VERIFIED).
- L1-09 physics: the task gives E_o = Hm, and η = E_a/E_o is the lesson's formula. Losses with the flue gases are the right mechanism, and η < 100 % is checked. 79 % is realistic for an oil boiler, and two significant figures fit the data.
- L2-09 recomputed: in the figure the input arrow is H = 160 units = 8 squares (sq = 20) and the useful arrow is ηH = 40 = 2 squares; the loss arrow is 120 = 6 squares, and its edges lie on grid lines (ytop 80, yloss 200). So η = 2/8 = 25 %, the same as answers.py.
- L2-09 figure: the drawing and its description agree. No output value or efficiency is printed, so the answer is not given away. The arrows are to scale as the text says.
- L2-09 solution: η = E_a/E_o equals the ratio of thicknesses (the lesson's Sankey statement). The check 60 J + 180 J (2 + 6 = 8 squares) shows that energy is conserved and agrees with L3-03 (180 J).
