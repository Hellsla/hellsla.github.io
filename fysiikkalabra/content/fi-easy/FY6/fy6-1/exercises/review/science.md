VERDICT: PASS
CONTENT-HASH: 9c35811b1982a8c7
SCOPE: delta added-exercise from 25bea0e8e337cf85 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- none

## Checked
- fy6-1-L2-08: own recomputation Q = 0,50 A · 40 s + ½ · 0,50 A · 60 s = 35 C, E = UQ = 4,0 V · 35 C = 140 J; matches answers.py and exercises.json (unit J, tolerance 0,02 fits two significant figures).
- Model: E = UQ with the terminal voltage stated constant in the task; charge as the area under the (t, I) graph, consistent with the lesson's I = Q/t and U = E/Q.
- Figure fy6-1/lataus-kuvaaja (figures.py): 0,50 A on 0–40 s, linear fall to 0 at 100 s; gives every value needed, alt text carries the same values, the charge is not shown.
- Solution complete: given/asked, principle, symbolic Q and E before substitution, no conversions needed, rounding reason, a real upper-bound check (200 J).
- Content hash checked at start and end.
