VERDICT: PASS
CONTENT-HASH: 598982a9db689aad
SCOPE: delta added-exercise from a5e3a606c3d94d47 base 141dc47a8c70
Mode: delta
Round: 3

## Blocking

## Polish
- solutions.md:75 (L1-10 Järkevyys) — "puuhun, jonka lämpöarvo on noin $16\,\text{MJ/kg}$" still differs from the 15 MJ/kg for air-dry firewood in *Polttoaineet ja lämpöarvo* (still open from round 2) — write "ilmakuivaan polttopuuhun (noin $15\,\text{MJ/kg}$)".
- solutions.md:72 / answers.py L1-10 — H = 43,4 MJ/kg (MAFY LHV) and the fy2-5 heating-value figure (bensiini 43) say the same thing at different precision (C, no contradiction). If you like, note in fy2-5 that 43 is a rounded value.
- Earlier items (L1-09 "likimain eristetyn", L3-04 c), L1-07 option 3) are still open. They are outside this delta.

## Checked
- Hash 598982a9db689aad at the start and the end. I judged only the added L1-10 and L2-08.
- L1-10 change: H = 43,4 MJ/kg is the same in the solution (Annettu, Sijoitus, Vastaus) and in answers.py. It is a plausible lower heating value for petrol (LHV, typically 42–44 MJ/kg). The task says to look it up in MAFY and marks the situation as invented ("Kuvitellaan").
- L1-10 recomputed: E = Hm = 43,4 MJ/kg · 2,0 kg = 86,8 MJ, the same as exercises.json and answers.py (86.8). The stated 87 MJ is 0,2 % away from it.
- L1-10 tolerance 4 %: table values of 42 / 43 / 44 MJ/kg give 84 / 86 / 88 MJ, which are 3,2 / 0,9 / 1,4 % from 86,8. All are accepted, as the solution says.
- L1-10: two significant figures follow from m = 2,0 kg. The check 87 MJ ≈ 24 kWh (24,1) is right, and the estimate 40 · 2 = 80 MJ is a real check. Chemical energy → kinetic + thermal is right, and there is no isolated-system claim.
- L2-08 has not changed since round 2. Recomputed: (700+0) − (300+300) = 100 J, p = 14,29 %, the same as answers.py. The answer 14 % is 2,1 % away, inside the 3 % tolerance. The figure data (FRICTION list) match the solution's readings.
