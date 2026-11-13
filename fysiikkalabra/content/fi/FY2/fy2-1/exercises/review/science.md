VERDICT: PASS
CONTENT-HASH: 1b1e4f5288cc758f
SCOPE: delta added-exercise from a5e3a606c3d94d47 base 2d61e6aff472
Mode: delta
Round: 1

## Blocking

## Polish
- exercises.json fy2-1-L1-10 hints / solutions.md L1-10 Annettu — the hint names the table *Polttoaineiden LHV-lämpöarvoja* and the solution "polttoaineiden lämpöarvot"; name it the same way in both (C, no physics error).
- solutions.md L1-10 Järkevyys — "puuhun, jonka lämpöarvo on noin 16 MJ/kg" (still open from earlier rounds): air-dry firewood is about 15 MJ/kg; write "ilmakuivaan polttopuuhun (noin 15 MJ/kg)".
- Earlier items outside this delta (L1-09 "likimain eristetyn", L3-04 c), L1-07 option 3) are still open.

## Checked
- Hash 1b1e4f5288cc758f at the start and the end. I judged only the added L1-10 and L2-08.
- L1-10: the hint now sits in `hints` (moved out of the text); the text still asks for the MAFY lookup and marks the situation as invented ("Kuvitellaan").
- L1-10 recomputed: E = Hm = 43,4 MJ/kg · 2,0 kg = 86,8 MJ, same as answers.py; the stated 87 MJ is 0,2 % away. H = 43,4 MJ/kg is a sound LHV for petrol.
- L1-10 tolerance 4 %: table values 42–44 MJ/kg give 84–88 MJ, at most 3,2 % from 86,8, so all are accepted. Two significant figures follow from m = 2,0 kg; 87 MJ ≈ 24 kWh is right.
- L1-10 physics: chemical → kinetic + thermal energy is right, and no isolated-system claim is made. E = Hm is in FY2 scope.
- L2-08 recomputed: (700 + 0) − (300 + 300) = 100 J, p = 14,29 %, same as answers.py; 14 % is inside the 3 % tolerance.
- L2-08 figure: FRICTION data (A 700/0, B 300/300, C 0/500) match the solution's readings and the description. The bars sit on 100 J gridlines and B lies at height 3/7 of the rim, which agrees with E_p,B = 300 J of 700 J.
- L2-08 consistency: thermal energy grows from 100 J at B to 200 J at C, which is right for a path with friction. The figure shows no thermal energy or total, so it does not give the answer away.
- L2-08 solution: E_lämpö = E_A − E_B is solved symbolically before substitution, rounding comes from the 100 J reading precision, and the check 600 + 100 = 700 J is a real check.
