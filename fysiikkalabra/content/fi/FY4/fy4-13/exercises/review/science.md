VERDICT: PASS
CONTENT-HASH: 44904908c0e5a59c

## Blocking

## Polish
- solutions.md:60 (L2-01) and figures.py malli_ketju — Both ends of the lower rope are named T₂. In the lesson, T₁ and T₂ name the two ends of one string over a pulley, so the convention changes here. It is not wrong. Either add one clause ("alempi köysi vetää kumpaakin laatikkoa voimalla, jonka suuruus on $T_2$") or use distinct symbols.
- exercises.json:90 (L3-01) — "voima köydestä kohdistuu pyörän akseliin": the rope acts on the wheel, and the force reaches the axle only through the light wheel. The solution handles this correctly. The wording could read "Kuinka suuri voima akseliin kohdistuu pyörästä".

## Checked
- The change since the PASS (solutions.md:96, L2-04): the substitution factors the unit out, $(9{,}81 + 2{,}0)\,\text{m/s}^2$ over $(9{,}81 - 2{,}0)\,\text{m/s}^2$. The numbers and units are unchanged and still right: 0,60 kg · 11,81 m/s² = 7,086 N, and 7,086 N / 7,81 m/s² = 0,9073 kg. The terms of each sum share a unit, so factoring it out is valid.
- Recomputed all 12 answers in one script with my own formulas, solving L2-04 and L3-02 numerically by bisection: 2,0; 4,686; 2,803; 29,43; 4,0; 880,8; 6,54; 8,0; 0,9073; 18 835 (2T, T = 9418 N); 0,4405; 0,857. answers.py agrees, and every rounded answer is inside its tolerance (L1-04 is the closest, at 1,5 % of 2 %).
- L2-04 check: (m₂ − m₁)g/(m₁ + m₂) = 2,000 m/s². T = 7,09 N lies between the weights 5,9 N and 8,9 N.
- L3-01: F = 2T on a light wheel is right, and 2T < G₁ + G₂ is a real check. L3-02: T rises monotonically with m₂, so the limit gives the maximum. L3-03: v = 2,10 m/s, and free fall takes 0,43 s.
- Force diagrams: each body gets its own diagram and positive direction before the equations. No third-law pair sits on one diagram, and acceleration is drawn off the body in malli-ketju. T₂ acts at the lower crate's top face and at the upper crate's bottom face.
- Notation, assumptions (light, inextensible string; light, frictionless pulley) and the formulas match the brief.
- Hash 44904908c0e5a59c at start and end.
