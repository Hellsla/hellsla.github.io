VERDICT: PASS
CONTENT-HASH: a17ecdadf7d4e05c
SCOPE: delta added-exercise from f2c0a93ba89108b4 base 141dc47a8c70

## Blocking

## Polish
- solutions.md (fy2-1-L1-10), Reasonableness: the MAFY row the student reads is dry wood, $16.2\,\text{MJ/kg}$. "about $16\,\text{MJ/kg}$ for dry wood" would name that row.
- exercises.json (fy2-1-L1-10): "changes into kinetic and thermal energy". In a car engine most of the energy becomes thermal energy and only part becomes kinetic energy. "mostly thermal energy, part kinetic energy" would be more exact. This is level C.

## Checked
- Hash a17ecdadf7d4e05c (`--exercises --lang en`) at the start and at the end.
- The round-2 blocking item is fixed. Given, Substitution and Answer in the solution, answers.py and exercises.json `answer` 86.8 now all use the MAFY petrol value $H = 43.4\,\text{MJ/kg}$ (*Polttoaineiden LHV-lämpöarvoja*, bensiini).
- Recomputed fy2-1-L1-10: $E = Hm = 43.4 \cdot 2.0 = 86.8\,\text{MJ}$. answers.py prints 86.8. The rounded 87 MJ is 0.2 % off. Table values of 42–44 MJ/kg give −3.2 % to +1.4 %, inside the 0.04 tolerance. 87 MJ ≈ 24 kWh is correct.
- fy2-1-L1-10: two significant figures follow from $m = 2.0\,\text{kg}$. The unit is MJ, and $E = Hm$ is within FY2 scope. The heating value is defined as the energy released per kilogram burned, and nothing suggests that energy is created.
- Recomputed fy2-1-L2-08 from the figure data (A 700/0 J, B 300/300 J): 100 J thermal, $p = 14.29\,\%$. This matches answers.py. The rounded 14 % is 2.0 % off, inside 0.03.
- fy2-1-L2-08 model: the isolated system is the skater, the half-pipe and the surroundings, and friction turns mechanical energy into thermal energy. This is consistent with L1-03 on the same figure (200 J by C, so the thermal energy grows along the path).
- Both added solutions have all seven stages, write the formula symbolically before substituting, and give a reason for the rounding.
