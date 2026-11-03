VERDICT: PASS
CONTENT-HASH: bc818ddb9a49965a

## Blocking

## Polish
- exercises.json:99 and :108 (L3-02, L3-03) — unlike the other tasks they do not say "ilmanvastus jätetään huomiotta" — add it (the solutions assume it).
- solutions.md L2-01 Vastaus — "kaksi merkitsevää numeroa kuten ... massassa 30 kg": the limiting datum is 1,2 m/s²; mention only that.

## Checked
- Full review after the malli-ketju label-offset change (figures.py, diff since 9904a31: only lab= of T_1 and the upper T_2; S = 0,10). The exercise texts, solutions and answers.py are unchanged.
- All twelve answers recomputed with my own formulas in one script: 2,0; 4,686; 2,803; 29,43; 4,0; 880,8; 6,54; 8,0; 0,9073; 18 835; 0,4405; 0,8567 — within tolerance and equal to answers.py's output.
- malli-ketju rendered SVG measured: T_1 88 px (880,8 N), G_1 49 px (490,5 N), upper T_2 33 px down from the bottom surface, lower T_2 33 px up from the top surface (330,3 N = m_2(g + a)), G_2 29,5 px (294,3 N) — all at S = 0,10 to the pixel; T_2 equal in both diagrams, directions right, a drawn up as motion, not as a force. The label nudge changed no arrow. Description (T1 longest, T2 equally long) matches the drawing and the L2-01 solution (T_1 = (m_1 + m_2)(g + a), voimakuvio blocks 880,8 / 490,5 / 330,3 / 294,3).
- Each solution writes one equation per body from its diagram, positive direction along the motion, unknown solved symbolically first; signs right in L2-01 (T_2 down on the upper crate) and L1-05/L2-03 (T backwards on the pulled body).
- Voimakuvio blocks: arrow magnitudes match the computed forces; T_1 = T_2 everywhere for one light string; N = G on horizontal surfaces.
- L3-01: axle force 2T on a light pulley in equilibrium, smaller than the sum of weights — correct. L1-04: T = mg, not 2mg — correct.
- Reasonableness checks are real checks (net force = m a, T between the weights, free-fall time 0,43 s in L3-03).
