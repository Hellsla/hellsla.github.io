VERDICT: PASS
CONTENT-HASH: 978c8eb6bbde4904

## Blocking

## Polish
- exercises.json:99 and :108 (L3-02, L3-03) — unlike the other tasks they do not say "ilmanvastus jätetään huomiotta" — add it (the solutions assume it).
- solutions.md L2-01 Vastaus — "kaksi merkitsevää numeroa kuten ... massassa 30 kg": the limiting datum is 1,2 m/s²; mention only that.

## Checked
- All twelve answers recomputed with my own formulas in one script (L3-02 by bisection on T(m_2) = 3,0 N): 2,0; 4,686; 2,803; 29,43; 4,0; 880,8; 6,54; 8,0; 0,9073; 18 835; 0,4405; 0,8567 — all within the stated tolerance of exercises.json and equal to answers.py's output.
- Each solution writes one equation per body from its diagram, positive direction along the motion, unknown solved symbolically first; signs right in L2-01 (T_2 down on the upper crate) and L1-05/L2-03 (T backwards on the pulled body).
- Voimakuvio blocks: arrow magnitudes match the computed forces; T_1 = T_2 everywhere; N = G on horizontal surfaces.
- L3-01: axle force 2T on a light pulley in equilibrium, smaller than the sum of weights — correct reasoning.
- L1-04: T = mg for equal masses at rest, not 2mg — correct, with a good check.
- Reasonableness checks are real checks (net force = m a, T between the weights, free-fall time 0,43 s in L3-03).
- malli-ketju model figure: T_1 longest, T_2 equal on both crates, G from centre, scaled from (m_1 + m_2)(g + a) and m_2(g + a).
