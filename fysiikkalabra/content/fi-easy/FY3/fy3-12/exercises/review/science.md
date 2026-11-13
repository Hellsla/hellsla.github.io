VERDICT: PASS
CONTENT-HASH: 54bfccfa69750636
SCOPE: delta added-exercise from 186c6601bf5ac2dc base 141dc47a8c70
Mode: delta (added exercises fy3-12-L1-09, fy3-12-L2-09)
Round: 1

## Blocking
(none)

## Polish
- solutions.md fy3-12-L2-09 Kuvaajan lukeminen — "Ylempi oikea nuoli" for the reflected 102 W/m² arrow: in earth_flows() that arrow runs up and to the left between the Sun and the Earth (x 176–262), and the dashed thermal-radiation arrow is the one right of the Earth. The same wording is in the Finnish. A fix: "Maan yläpuolella vasemmalle osoittava nuoli" (in both languages).

## Checked
- L1-09: P = UAΔT with U = λ/d given in the task (surface resistances left out: a fair simplification, C). MAFY pine λ = 0,14 W/(m·K); recomputed U = 0,70 W/(m²·K), ΔT = 30 K, P = 210 W; two significant figures from λ; tolerance 4 %.
- L2-09: reflected share 102/341 = 29,9 %, in line with the planetary albedo of about 0,30; figure arrows 341 and 102 to scale, the description gives both values; the question mark is not needed and the solution says so.
- Solutions complete, symbolic first, real reasonableness checks.
- answers.py matches my recomputation (210; 29,912).
- Scripted comparison with the Finnish: answer, unit, tolerance, figure, lookup and all numbers identical.
- Hash the same at start and end.
