VERDICT: PASS
CONTENT-HASH: 45f15bceac913270
SCOPE: delta added-exercise from 2c9fdf155f72e6a3 base 141dc47a8c70

## Blocking

## Polish
- solutions.md:75 (fy2-1-L1-10): the solution still gives wood as "noin 16 MJ/kg", while fy2-5 uses 15 MJ/kg for air-dry firewood. Fix: "ilmakuivan polttopuun, noin 15 MJ/kg".
- exercises.json:156 (fy2-1-L1-10): "Se muuttuu liike-energiaksi ja lämpöenergiaksi" skips the step where combustion first makes thermal energy and the engine turns only part of it into kinetic energy. This is a fair level-1 simplification (C). Fix (optional): "suurin osa muuttuu lämpöenergiaksi, osa liike-energiaksi".

## Checked
- L1-10, change in this round: H = 43,4 MJ/kg is now the same in the task, the solution (Annettu, Sijoitus, Vastaus) and answers.py ("MAFY LHV"). The lower heating value is the right one for an engine.
- L1-10, numbers: I recomputed 43,4 MJ/kg · 2,0 kg = 86,8 MJ. It matches answers.py and exercises.json (86.8 MJ). The answer "≈ 87 MJ" has 2 significant figures, set by m = 2,0 kg.
- L1-10, tolerance: ±4 % accepts 83,3 to 90,3 MJ, which covers table values of H from about 41,7 to 45,1 MJ/kg. A student who uses 43 MJ/kg (as in fy2-5) gets 86 MJ, which is 0,9 % off and is accepted. Rounding 43,4 to 43 in fy2-5 is consistent with this value.
- L1-10, checks: 86,8 MJ / 3,6 = 24,1 ≈ 24 kWh is correct, and the estimate 40 · 2 = 80 MJ is a real order-of-magnitude check.
- L1-10, scope and physics: E = Hm is in FY2 scope. The task does not claim the system is isolated. The Periaate (chemical energy changes form and the amount is conserved) is right. The solution is complete and symbolic first.
- L2-08, unchanged since round 2: I recomputed 100 · (700 − 600)/700 = 14,29 %. answers.py and the json value 14.3 agree, and ±3 % accepts 13,9 to 14,7, so 14 is accepted. FRICTION (A 700/0, B 300/300) matches the readings and the alt text. The figure shows no thermal-energy or total bar, so it does not give the answer away.
- Hash 45f15bceac913270 at the start and at the end.
