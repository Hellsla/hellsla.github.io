VERDICT: PASS
CONTENT-HASH: daa0330ac3b9a714
SCOPE: delta added-exercise from e5c2c0ca37639b87 base 8f23aa7ae3bd

## Blocking

## Polish
- solutions.md (fy6-9-L2-08) — "kaksi merkitsevää numeroa kuten virran lukemissa": the reading 0,5 A has one significant figure written, but it is read off grid lines, so it is known to about 0,05 A. Say that the readings are known to the grid's precision instead of counting written digits.

## Checked
- Hash daa0330ac3b9a714 at start and end; only fy6-9-L2-08 was judged (delta added-exercise).
- Figure fy6-9/ex-current2 (figures.py): the steps are 2,0 A for 0–1,0 h, 1,5 A for 1,0–3,0 h and 0,5 A for 3,0–4,0 h, then zero. They match the solution's readings and the alt text, and the alt text does not give the charge.
- I recomputed it myself: Q = Σ I·Δt = 2,0 + 3,0 + 0,5 = 5,5 Ah, so W = 11,1 V · 5,5 Ah = 61,05 Wh. This equals answers.py and the json answer; unit Wh, tolerance 0,02.
- The model W = UQ with the nominal voltage is the lesson's formula. The task states the assumption explicitly, so the energy lost in charging (η < 100 %) does not make the answer wrong (finding C).
- Physics: the charge is the area under the I(t) graph and the current is constant on each piece. 61 Wh is realistic for a laptop battery.
- The solution has all seven parts, the symbolic Q and W before the numbers, the conversion 1 V·Ah = 1 Wh, and a real check (the mean current 1,4 A lies between the extremes).
- In scope: akut ja latauspiiri (capacity, energy).
