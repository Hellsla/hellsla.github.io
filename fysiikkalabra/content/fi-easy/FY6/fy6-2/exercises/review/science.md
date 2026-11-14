VERDICT: PASS
CONTENT-HASH: 60fd7dae122dc102
SCOPE: delta added-exercise from 99b43d4ac55dcc70 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- exercises.json fy6-2-L2-10 — a lamp's voltage is set by the circuit, not by the lamp, so "sopiiko lukema nimellisarvoon" is a judgement about the operating point rather than the measurement; the solution says so ("lamppua käytetään eri jännitteellä"), so no wrong picture remains — optionally phrase the question as "selittääkö mittarin virheraja eron".
- exercises.json fy6-2-L2-09 — tolerance 0,12 admits the rounded 0,03 V only by a margin (+11,7 %) — fine as is; keep it if the tolerance is ever tightened.

## Checked
- fy6-2-L2-09 recomputed: ΔU = 0,005 · 1,37 V + 2 · 0,01 V = 0,02685 V ≈ 0,03 V; matches answers.py and exercises.json; unit V.
- fy6-2-L2-10 recomputed: (1,45 V − 1,37 V) : 0,02685 V = 2,98; a student using the rounded 0,03 V gets 2,67 (−10,5 %), inside tolerance 0,12; dimensionless unit right.
- Formula Δx = p·x + n·r and its conditions as in the brief; resolution of the 20 V range 0,01 V matches the brief's table and the display's two decimals.
- Figure fy6-2/multimeter-task (figures.py): display 1,37 V, pointer at −35° = 20 V range; alt text gives the same; no error limit or answer shown.
- Conclusion of L2-10 (difference about 3 × the error limit, so the meter's limit does not explain it) correct; interval 1,34–1,40 V right.
- Both solutions complete (given, principle, symbolic formula, conversion, substitution, rounding reason, check).
- Content hash checked at start and end.
