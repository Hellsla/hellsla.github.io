VERDICT: PASS
CONTENT-HASH: 6d4426affade3fc5

## Blocking
None.

## Polish
- fy7-k3 c asks for I, F and P; `answer` lists only F and P. Add I = 0,50 A.
- fy7-k5 b: k = 3 is called the most reliable order, but the plain mean (3,331 µm) is the best estimate; a weighted mean gives 3,326 µm. Järkevyys says the results "sopivat yhteen", then shows that k = 2 and k = 3 differ by 0,026 µm, more than their 0,018 µm reading uncertainties. Make the solution and the conclusion criterion say the same.
- fy7-k7 a: graph_fit requires a line through the origin. A free fit (slope 2,81·10⁻³ m·K, intercept −19 nm) is also valid. Add it to Hyväksytään myös.
- fy7-k2 c Järkevyys: the relative uncertainty of r is 1,5–2,6 %, not 2–3 %.
- fy7-k6 d: 4000 full-power hours are the worst case for losses at a given energy. With variable production the losses are smaller and the payback longer than 9 a; state that direction.

## Checked
- Recomputed every number with my own script from the task data; all agree with the solutions and answers.py:
  - k1: d 0,08 V; i 73,7°; h 0,122 m and 3,0 m
  - k2: e/m 1,74·10¹¹ C/kg (read 1,72·10¹¹); extreme lines 1,68 and 1,85·10¹¹, so ±0,084·10¹¹ C/kg
  - k3: 0,30 V, 0,50 A, 0,060 N, 0,15 W = I²R
  - k4: 40 Hz, 12,37 V, 0,0516 T, 2788 turns, 3,72 A
  - k5: 3,327/3,347/3,321 µm, ±27/12/6 nm, k_max = 6
  - k6: 600 A, 1,728 MW (14,4 %), 109 A, 57,1 kW, N₁ = 500, 334 200 €/a, 8,98 a; with transformer losses 9,67 a
  - k7: b 2,758·10⁻³ m·K, 4,8 %, 2,6 % random, 9,47 µm, 5269 K
- Osa 1: each item has exactly one correct option, and the distractors and their feedback are right.
- k3 b: the current direction (Lenz and v × B) is correct.
- k7 c: the systematic error and its direction (tungsten's emissivity) are correct.
- Rubrics: each criterion asks only what its part asks; all part sums are right.
- Scope: everything is inside FY7. Polarisation stays qualitative; no self-induction, no photon.
- Data: invented data are marked `source: example`; the constants are correct.
- Figures: the data in figures.py match the tasks, and the read points lie on the drawn lines.
