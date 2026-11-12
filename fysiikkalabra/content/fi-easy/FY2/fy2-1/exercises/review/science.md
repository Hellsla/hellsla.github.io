VERDICT: PASS
CONTENT-HASH: 1398dc519f5045f4
SCOPE: delta added-exercise from 2c9fdf155f72e6a3 base 141dc47a8c70

## Blocking

## Polish
- solutions.md:75 (fy2-1-L1-10): the check gives wood "noin 16 MJ/kg", but the course's fy2-5 figure uses 15 MJ/kg for air-dry firewood. Fix: write "ilmakuivan polttopuun, noin 15 MJ/kg" so the course says the same thing everywhere.
- exercises.json:156 (fy2-1-L1-10): "Se muuttuu liike-energiaksi ja lämpöenergiaksi" leaves out the step in between, where combustion first makes thermal energy and the engine turns part of it into kinetic energy. This simplification suits level 1 (C), so it is not an error. Fix (optional): "suurin osa muuttuu lämpöenergiaksi, osa liike-energiaksi".

## Checked
- L1-10, scope: the task states E = Hm, which is in FY2 scope (the scope notes list E = Hm). The c·m·ΔT physics and the wrong claim that the system is isolated are both gone, so the two blocking items from round 1 are fixed.
- L1-10, numbers: H = 43 MJ/kg × 2,0 kg = 86 MJ. answers.py gives 86.0, the same as exercises.json. The unit is MJ, and 2 significant figures follow from m = 2,0 kg.
- L1-10, lookup: 43 MJ/kg agrees with the course's own fy2-5 heating-value data (bensiini 43). The ±4 % tolerance accepts 82,6 to 89,4 MJ, which covers table values of about 41 to 45 MJ/kg. A higher heating value of about 46 to 47 MJ/kg would be outside it, but MAFY gives the lower value, so this is acceptable.
- L1-10, checks: 86 MJ / 3,6 = 23,9 ≈ 24 kWh is correct. The order-of-magnitude estimate is sound.
- L1-10, solution: it is complete (Annettu, Kysytty, Periaate, Kaava, Sijoitus, Vastaus with sig-fig reason, Järkevyys) and symbolic before numbers. The Periaate (chemical energy converts, the amount is conserved) is correct.
- L2-08, numbers: I recomputed 100·(700 − 600)/700 = 14,29 %. answers.py gives 14.285714, and exercises.json gives 14.3 with tolerance 3 %, so 14 is accepted (lower limit 13,87).
- L2-08, round-1 polish: the weak "puolivälissä" check is removed. Only the sum check 600 J + 100 J = 700 J remains. The answer is now "noin 14 %" and gives the 100 J reading accuracy as the reason.
- L2-08, figure and physics: figures.py FRICTION (A 700/0, B 300/300) matches the readings and the alt text. The figure has no thermal or total bar, so it does not give the answer away. The isolated system (skater, half-pipe and surroundings) is stated.
- Hash 1398dc519f5045f4 at the start and at the end.
