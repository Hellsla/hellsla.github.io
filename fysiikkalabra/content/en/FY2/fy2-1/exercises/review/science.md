VERDICT: FAIL
CONTENT-HASH: 7db9426afc47ccfe

## Blocking
- content/en/FY2/fy2-1/exercises/exercises.json:156 (fy2-1-L1-10), solutions.md:67 — **A (scope)**: the task gives the student $E = c\,m\,\Delta T$ to use and asks for a table value of $c$. The FY2 scope notes say "FY2 has no ... Q = c m Delta T"; that formula and specific heat capacity belong to FY3, which builds on FY2. The physics and the number are right ($4.19 \cdot 0.50 \cdot 40 = 83.8\,\text{kJ}$), but the task is outside the course. — Fix: replace it with a FY2-level MAFY lookup task, e.g. a heating value with $E = Hm$ (taught later in FY2, so better placed in that chapter) or one inside this chapter's content (energy forms and conservation with given energies). Alternatively move this task to the FY3 chapter on heat.

## Polish
- solutions.md:67 (L1-10) — "the system is isolated": electrical energy comes into the kettle from the mains, so kettle and water are not an isolated system unless the wiring and grid are included. "No energy escapes to the surroundings, so all the electrical energy becomes thermal energy of the water" says it more exactly.
- solutions.md:147 (L2-08), Reasonableness — "B is halfway down the slope": B is at $3/7$ of the height ($E_\text{p}$ drops from 700 to 300 J of 700 J), and friction losses depend on the path length, not the height. Better: "B lies about halfway between A and C, and half of the loss by C comes before B", or check only $600 + 100 = 700\,\text{J}$ and $0 < p < 100\,\%$.

## Checked
- Hash 7db9426afc47ccfe at the start and at the end (`--exercises --lang en`).
- L2-08: the figure's data FRICTION has B = (300 J, 300 J) and A = (700 J, 0 J), the same as the solution and the alt description. B's place on the track (u² = 300/700) matches its $E_\text{p}$, so the drawing is to scale. The figure does not show the thermal energy or a total, so it does not give the answer away.
- Recomputed L2-08 myself: $E_\text{thermal} = 700 - 600 = 100\,\text{J}$, $p = 14.29\,\%$, the same as answers.py. The rounded answer 14 % is 2 % off, inside tolerance 0.03. Two significant figures fits values read on 100 J gridlines.
- L2-08 physics: friction turns mechanical energy into thermal energy and conservation is applied to skater, half-pipe and surroundings, as the guardrail requires (no energy is created). It does not contradict L1-03 (200 J by C, 29 %).
- Recomputed L1-10: $83.8\,\text{kJ}$, the same as answers.py. With $c = 4.18$ the result is 83.6 kJ, inside tolerance. The 2 kW kettle check gives 42 s, which is right. The temperature stays between 20 and 60 °C with no change of state, so $cm\Delta T$ applies. Unit kJ, rounding to 2 sig. figs from 0.50 kg is justified.
- Both solutions are complete in all seven stages and solve symbolically before substituting.
