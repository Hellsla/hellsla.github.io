VERDICT: PASS
CONTENT-HASH: 4563049723f00d29

## Blocking

## Polish
- sim.js:133 — the "light, freely moving piston" is drawn fixed at the rim during boiling and the steam phase, which looks like the rigid vessel the model text excludes; let it rise a little as the liquid fraction falls (still not to scale).
- inquiry.json:132 (`simulaatio.model`) — at constant pressure part of the heater energy is the steam's work on the piston (pΔV ≈ 170 kJ/kg, ~7,5 % of r); r and c_p already include it, so numbers are right, but "kaikki kuumentimen energia siirtyy aineeseen" deserves a clause such as "r ja höyryn c ovat vakiopaineen arvoja, joten ne sisältävät myös männän työntämiseen kuluvan energian".

## Checked
- Diff since cb4b8f4: only the worked example's wording (128 g marked as an invented figure, "tämän lukeman mukaan"); the physics and r = Pt/Δm = 1000·300/0,128 = 2,34 MJ/kg are unchanged and correct.
- Everything else (answers.py, exercises, inquiry, sim.js, figures) unchanged since the round-1 full review, whose recomputations still hold: 12 exercises, inquiry numbers (210 kJ, 83,5/565 s, ratio 6,8, 66,8 kJ, 188 W, 0,597 kg), sim plateaus sm/P and rm/P, heating-curve slopes.
- Hash identical at start and end.
