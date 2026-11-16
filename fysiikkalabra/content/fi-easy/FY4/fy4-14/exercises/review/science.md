VERDICT: PASS
CONTENT-HASH: 4de8ceed5601dd99
Mode: full

## Blocking

## Polish
- solutions.md:789 (L2-04 Vastaus) — "luvut 450 N, 180 N ja 1200 kg luetaan kolminumeroisiksi": by the teacher's rule 1200 kg has four figures; the answer's three figures follow from 450 N and 180 N — name those two as the limiting data.
- solutions.md:977 (L2-08 Järkevyys) — "Luvun kuvaajan malli" is the model $F_\text{v} = kv^2$, $k = 0{,}26\,\text{kg/m}$, which the exercise brief does not show; the sentence is right (53,2 m/s) but the student cannot recompute it — fine as a comparison, no change needed.

## Checked
- Hash the same at the start and the end (4de8ceed5601dd99).
- All 18 numeric answers recomputed with my own formulas in one script; all inside tolerance and equal to answers.py (L1-03 3,52 m/s² up; L1-08 911,4 N up; L2-03 14,196 m/s²; L2-05 0,1062 N; L3-03 0,4965 N; L3-04 2239,4 N = 2,78 mg; L3-05 171,55 m/s).
- L2-08: a = (46,4 − 40,4) m/s : 4,0 s = 1,50 m/s²; F_v = 75,0 kg · 8,31 m/s² = 623,25 N = 84,7 % of 735,75 N; slopes 9,3 and 0,45 m/s² as stated; the points level off near 48 m/s (they follow v_T tanh(gt/v_T) with v_T = 48 m/s to 0,1 m/s).
- L2-08 added sentence: the chapter model gives √(mg/k) = √(735,75 N : 0,26 kg/m) = 53,2 m/s ≈ 53 m/s for 75,0 kg; 48 m/s needs k = mg/v² = 0,32 kg/m, a larger drag area, so "leveämpi asento / väljä puku" is the right direction of the explanation.
- Force diagrams (checklist): each lists only weight and air resistance (plus N, driving friction and rolling resistance on the road tasks); F_v opposite to the velocity in every case (up when falling, down when rising); arrow lengths agree with the motion (equal at terminal speed, F_v longer when the canopy opens); velocity and acceleration marked beside, never as forces; equations follow from the diagrams with the stated positive direction.
- L1-06, L1-07, L2-07: exactly one correct option; distractor feedback physically right. L1-09: 1 T, 2 F, 3 T, 4 F, 5 F correct (G = 2,65 N).
- L2-06 b: force ratio 4,0 with speed ratio 2,07 supports F_v growing about as v²; stated as an observation, not a law to compute with.
- L3-05: 0,0140 g drop, 8,0 m/s: F_v = 1,37·10⁻⁴ N; 172 m/s = 620 km/h without air; fall time about 190 s.
- Figure ex-tangentti: tangent through (0; 2,0) and (2,0; 15,0) has slope 6,5 m/s² and touches the tanh curve at P by construction.
- Scope: air resistance only given or deduced from motion, as the brief says.
