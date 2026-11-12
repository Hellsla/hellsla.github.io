VERDICT: FAIL
CONTENT-HASH: 075d17656120eb22

## Blocking
- exercises.json:158 (fy2-1-L1-10), solutions.md:67-75 — A, scope: the task rests on $E = c\,m\,\Delta T$ and specific heat capacity. The FY2 scope notes exclude $Q = cm\Delta T$ (it is FY3 content), and the brief's lesson does not teach it. Stating the formula in the task does not fix this. — Fix: replace it with an in-scope MAFY lookup (e.g. heating value $H$ with $E = Hm$, or 1 kWh = 3,6 MJ), or drop the exercise.
- solutions.md:70 (fy2-1-L1-10) — A, model: "Kaikki sähköenergia siirtyy veteen …, joten systeemi on eristetty" is wrong. Kettle and water are not isolated, because electrical energy comes in from the grid. — Fix (if any version is kept): say that energy is conserved and, with no losses, the electrical energy taken in equals the increase in the water's thermal energy. Also state that the water does not boil (guardrail: $Q = cm\Delta T$ holds only while the state does not change).

## Polish
- solutions.md:156 (fy2-1-L2-08) — "B on rinteen puolivälissä, joten noin puolet" is a weak check. B is at 3/7 of the rim height, and friction losses need not scale that way. — Keep only the sum check $600 + 100 = 700\,\text{J}$, or call the half a rough expectation.
- solutions.md:155 (fy2-1-L2-08) — a 100 J difference of values read to 100 J has about one significant figure, so "noin 14 %" would be more honest. Acceptable at this level.

## Checked
- L2-08: recomputed 100·(700 − 600)/700 = 14,29 % → answers.py 14.3; 14 is within the 3 % tolerance.
- L2-08: figures.py FRICTION (700/0, 300/300, 0/500) matches the solution's readings and the alt text; B's height u² = 3/7 matches E_p,B; there is no thermal or total bar, so the answer is not given away.
- L2-08: the physics holds (isolated skater + half-pipe + surroundings; thermal = E_A − E_B); at C 200 J = 29 %, consistent with L1-03.
- L1-10: 4,19·0,50·40 = 83,8 kJ (4,18 → 83,6 kJ, also within tolerance); ΔT °C = K; 2 kW → 42 s. Only the scope and the system claim fail.
- Hash 075d17656120eb22 at the start and at the end.
