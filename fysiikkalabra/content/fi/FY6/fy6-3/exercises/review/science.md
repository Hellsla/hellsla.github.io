VERDICT: PASS
CONTENT-HASH: 593f504a543bc1e6
Round: 1 (new task fy6-3-L1-09, graph choice with four figures; the rest of the set was PASS before and is unchanged).

## Blocking

## Polish

## Checked
- Hash 593f504a543bc1e6 at start and end.
- answers.py run against exercises.json: all 18 numeric answers agree within tolerance (one python call).
- L1-09 recomputed: U = 2,0 kΩ · 4,0 mA = 8,0 V. Figure generators match the descriptions: pick-curve U = 0,5 V·(I/mA)² gives (2,0; 2,0), (4,0; 8,0), end (4,5; 10,1); pick-k2 (2,0; 4,0), (4,0; 8,0), (4,5; 9,0); pick-k05 (4,0; 2,0), (4,5; 2,25); pick-flat 2,0 V. Only C is a line through the origin with U : I = 2,0 kΩ everywhere.
- Axes (I horizontal, U vertical, slope = R) as in the lesson; the same axes, colour and weight for every option, so the answer is not given away by form; each option's description is full (axes, grid, points).
- Option A passes through the right point (4,0 mA; 8,0 V) but is curved like a hot lamp's characteristic (concave up, R rising with U as the lesson says), so it catches the lesson's warned mistake about R and U; B catches I : U taken as the slope; D catches R drawn as a height.
- Feedback and solution use U : I with the colon in prose, coordinate pairs with a semicolon, and say why each wrong option is wrong.
- Inline formula widths measured (KaTeX render at 17 px, 1.21 em, own script): widest 241 px. Figures and page not rendered; checked from generator code and text.
