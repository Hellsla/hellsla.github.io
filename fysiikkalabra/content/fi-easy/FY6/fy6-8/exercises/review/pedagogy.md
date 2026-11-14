VERDICT: PASS
CONTENT-HASH: 8a4aaa9b86ce5839
SCOPE: delta added-exercise from 7090f26f691f0c78 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- exercises.json fy6-8-L2-09 text — "Mallista lasketut pisteet ovat viisi" is clumsy. Fix: "Kuvaajassa on viisi mallista laskettua pistettä, ja jokainen vastaa eri kuormitusta käynnistysmoottorille."
- exercises.json fy6-8-L2-09 tolerance 0,04 for the answer 0,02 Ω accepts everything from 0 to 0,06 Ω, so a rough guess passes. Fix: a tolerance of about 0,004 (the wrong U : I of one point, 0,22 Ω, is rejected either way).
- Same method as L1-05 (internal resistance from an (I, U) graph); level 2 holds through the two-point slope derivation and the car-battery scale.

## Checked
- L2-09: level 2 fits; arithmetic 4 V : 200 A = 0,020 Ω correct; the third-point check (9 V at 150 A) and E = 12 V are correct.
- Solution is stepwise: U = E - R_s I, two equations subtracted, symbols before numbers, units, sensibility.
- It names the real misconception (U : I of one point is the load, not R_s).
- Figure ex-graph-car gives all five points; its description matches and states neither slope, intercept nor R_s.
- Situation first, question as its own sentence; the rest of the Finnish is correct; kinds in the set stay varied.
