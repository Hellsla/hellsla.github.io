VERDICT: PASS
CONTENT-HASH: b1ec7b6c20b84876
SCOPE: delta added-exercise from 2652c350745c0908 base 89bcb63b7431
Mode: delta (added exercises fy3-9-L1-09, fy3-9-L2-09)
Round: 1

## Blocking
(none)

## Polish
- None.

## Checked
- L1-09: Boyle's law fits (closed bag, temperature held constant as the task states; the solution notes the real cooling). MAFY 3000 m p = 70,1 kPa (standard atmosphere 70,1 kPa); recomputed V₂ = 101 · 2,0 / 70,1 = 2,882 l, so 2,9 l; tolerance 4 % fits two significant figures.
- L2-09: rigid closed vessel, so isochoric p/T constant. The figure points lie on p = 0,40 kPa/K · T (200/80, 250/100, 300/120, 350/140), on grid crossings, to scale; the description gives the same points and not the answer. Recomputed p₂ = 120 · 373,15/300 = 149,3 kPa, so 149 kPa; T in kelvins; tolerance 2 %.
- Both solutions complete (given, principle with its reason, symbolic first, conversions, substitution, rounding, a real check). The notation is the brief's.
- answers.py lines match my own recomputation (2,881598; 149,26).
- Scripted comparison with the Finnish set: answer, unit, tolerance, figure, lookup and every number in the text and solution are identical.
- Hash the same at start and end.
