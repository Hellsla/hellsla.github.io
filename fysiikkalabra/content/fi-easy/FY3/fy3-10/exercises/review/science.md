VERDICT: PASS
CONTENT-HASH: 58713d0f9c157ec6
SCOPE: delta added-exercise from 2d45d7f23d815a16 base 89bcb63b7431
Mode: delta (added exercises fy3-10-L1-09, fy3-10-L2-09)
Round: 1

## Blocking
(none)

## Polish
- exercises.json fy3-10-L2-09: n_B from the figure is one step of what L2-04 already asks (n_A − n_B, same figure). The physics is fine; it overlaps with L2-04 (same in the Finnish).

## Checked
- L1-09: ideal-gas assumption stated; MAFY M(Ar) = 39,95 g/mol; recomputed n = 12,52 mol, p = nRT/V = 3,047 MPa, so 3,05 MPa; 0,0100 m³ conversion right; the magnitude check (about 300 l at 1 atm compressed into 10 l gives about 3 MPa) is a real check.
- L2-09: rigid closed vessel; the B line is p = 0,15 kPa/K · T through (200 K; 30 kPa) and (400 K; 60 kPa) on grid crossings; recomputed n = 60 000 Pa · 0,00200 m³ / (8,31 · 400) = 0,03610 mol. Molar volume check RT/p = 55 l, so about 0,04 mol: consistent.
- Figure pt-suorat: to scale, A slope 0,25 and B slope 0,15 kPa/K; the description lists the points and not n.
- Solutions complete and symbolic first; units and significant figures fit the data; tolerances 4 % and 3 %.
- answers.py matches my recomputation (3,047347; 0,036101).
- Scripted comparison with the Finnish: answer, unit, tolerance, figure, lookup and all numbers in text and solution identical.
- Hash the same at start and end.
