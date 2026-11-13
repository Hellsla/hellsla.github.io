VERDICT: PASS
CONTENT-HASH: 68c008a6b44a806f
SCOPE: delta added-exercise from 73af95b33d80d8a2 base 81db4a6fd727
## Blocking

## Polish
- content/fi-easy/FY4/fy4-6/exercises/exercises.json:350 — the new opening drops the word "esimerkkiaineisto", while the figure's description and the set's other data tasks still mark the data as example data — add "(esimerkkiaineisto)" after the first sentence (same in fi), so made-up points are not read as a real measurement.

## Checked
- Only change: L2-09 opening split into short sentences; same content as fi (block pulled on a table, friction measured at several normal forces), no number, symbol or condition changed.
- Conditions still stated: same table, horizontal sliding, only weight, normal force and friction; fit line asked for because the block's N has no point.
- Recomputed: origin fit slope Σ(NF)/ΣN² = 295/1375 = 0,2145; N = 0,80 kg · 9,81 m/s² = 7,85 N, F_μ = 1,68 N, a = F_μ/m = 2,10 m/s² against the motion; answer 2.1, tolerance 5 % unchanged and equal to fi.
- All 23 tasks: answer, unit, tolerance, figure, data and correct options equal the Finnish set; answers.py agrees.
- Hash unchanged at start and end.
