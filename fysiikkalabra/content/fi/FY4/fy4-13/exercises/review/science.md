VERDICT: PASS
CONTENT-HASH: 158b41a2a2e12f2f

## Blocking

## Polish
- solutions.md:60 (L2-01) and figures.py malli_ketju — Both ends of the lower rope are named T₂. In the lesson, T₁ and T₂ name the two ends of one string over a pulley, so the convention changes here. It is not wrong. Either add one clause ("alempi köysi vetää kumpaakin laatikkoa voimalla, jonka suuruus on $T_2$") or use distinct symbols.
- exercises.json:90 (L3-01) — "voima köydestä kohdistuu pyörän akseliin": the rope acts on the wheel, and the force reaches the axle only through the light wheel. The solution handles this correctly. The wording could read "Kuinka suuri voima akseliin kohdistuu pyörästä".

## Checked
- Round-1 blocker fixed: L1-03, L3-02 and L3-03 now state a light, inextensible string and a light, frictionless pulley. L2-02, L2-04 and L3-01 add "venymätön", and L1-05 and L2-03 mention air resistance.
- Recomputed all 12 answers in one script with my own formulas (scratchpad rc.py), solving L3-02 numerically by bisection: 2,0; 4,686; 2,803; 29,43; 4,0; 880,8; 6,54; 8,0; 0,9073; 18 835 (2T on the axle, T = 9418 N); 0,4405; 0,857. answers.py agrees, and every rounded answer stays inside its tolerance (L1-04 is at 1,5 % of 2 %).
- L3-01 has a new question (the axle force). The pulley's equilibrium F = 2T is right for a light wheel, and the check 2T < G₁ + G₂ is a real check.
- L3-02: T rises monotonically with m₂, so the limit T = T_max gives the maximum. Rounding down to 0,44 kg stays safe.
- Every solution names the bodies and draws the diagram, gives each body its positive direction, then the equations. The unknown is solved in symbols first, and the rounding names the limiting datum. No third-law pair sits on one diagram, and no velocity or acceleration is drawn as a force.
- Hash 158b41a2a2e12f2f at start and end.
