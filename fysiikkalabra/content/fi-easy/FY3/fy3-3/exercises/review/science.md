VERDICT: PASS
CONTENT-HASH: 84cdf45ac45c57f4
SCOPE: delta added-exercise from 7701b8401cab51a9 base 81db4a6fd727

## Blocking
(none)

## Polish
- content/fi-easy/FY3/fy3-3/exercises/solutions.md (fy3-3-L2-08, Järkevyys): the check uses the point (75 °C; 96 kPa), which "Annettu" does not list. Name it under "Kuvaajan lukeminen" as well, or bracket 100 kPa with the line values instead. Same in the Finnish.

## Checked
- L2-08 now asks for the temperature at 100 kPa (it was an extrapolation before). It uses constant volume and an amount of gas the task says stays the same ("suljetussa jäykässä"), and the task states linearity ("Oleta"), so the condition is covered.
- L2-08 recomputed: end-point slope k = (102,5 − 75)/100 = 0,275 kPa/°C, so θ = 25/0,275 = 90,9 °C. Interpolating between the neighbouring points (75; 96) and (100; 102,5) gives 90,4 °C, and a least-squares line through all five points gives 90,5 °C. All of these are inside the 8 % tolerance (83,6–98,2 °C) and the stated range 84–98 °C.
- The tolerance reason is consistent: a 1 kPa reading error moves θ by about 3,6 °C (about 4 %), and 8 % covers about 2 kPa on a 25 kPa grid.
- The figure description lists every point, so a reader who cannot see the figure has the same data. Neither the figure nor its description gives θ.
- L1-10 unchanged: T = −196 + 273,15 = 77,15 K, so 77 K.
- The script compared fi-easy with the Finnish: answer 90,9, unit °C, tolerance 0,08 and figure id are identical, and so are all numbers in the text and the solution.
- Hash the same at start and end.
