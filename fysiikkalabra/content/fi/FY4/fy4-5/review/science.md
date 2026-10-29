VERDICT: PASS
CONTENT-HASH: 323719bbcc0ccf96

## Blocking

## Polish
- sim.js:139 — in push mode at about 40°, the F_x label still touches F's arrowhead at the sled's corner. — Offset it in push mode.
- review/shots and site/sims/fy4/fy4-5/sim.js are still the old point-model versions. — Regenerate and rebuild before publishing.

## Checked
- Delta e71366d4 (fifth rule: G at the geometric centre, N from the contact surface perpendicular to it, G and N never on one line):
  - esimerkki: N moved to x = 290, from the bottom face (y = 207), with G from the centre (270; 185). That is 20 px apart. N is still 71,8 N to scale (82,5 px at 1,151 px/N).
  - heliumpallo: F_noste and G now start at the centre (515; 490) of the 480–550 rectangle. N still pushes down, ends on the top face at x = 495 and is 20 px from G. F_noste = G + N (100 = 40 + 60 px) is unchanged.
- The rule holds in the other figures, which this commit did not change: tilanne 20 px, suunnat lattia 15 px, hissi a–d 12 px, virhe 20 px, malli-tyonto 30 px, malli-pulkka 24 px and malli-hissi 12 px apart. On the slope, N is perpendicular and not parallel to G. The sim draws N 14 px left of G at the bottom face.
- The rendered PNGs (contact sheet) show N and G clearly side by side in every diagram. The arrow lengths and directions are unchanged.
- From my earlier reviews this round: the four drawing rules, the lift options (exactly one error each), every recomputed number, and no point-model text.
