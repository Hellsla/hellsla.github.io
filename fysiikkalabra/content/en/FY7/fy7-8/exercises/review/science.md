VERDICT: PASS
CONTENT-HASH: 28f469e13603292f

## Blocking

## Polish
- solutions.md:273 (L2-10 Reasonableness) — the voltage drop $RI \approx 4.2\,\text{kV}$ of one conductor is better compared with the phase voltage $110\,\text{kV} : \sqrt{3} \approx 64\,\text{kV}$ than with the line voltage; the conclusion (small) is the same (same remark as on the Finnish set).
- exercises.json (L2-10) — $200\,\text{MW}$ on one $110\,\text{kV}$ line (1050 A) is at the upper edge of what such a line carries; acceptable for the comparison, and the solution says the numbers are a model.

## Checked
- Delta round 1: only fy7-8-L2-10 (FY7-A1) judged; hash identical at start and end.
- Recomputed from the task text: $I = P/(\sqrt{3}\,U)$ = 1049.7 A and 288.7 A; $P_\text{h} = 3RI^2$ = 13.22 MW and 1.000 MW (6.6 % and 0.50 % of 200 MW); ratio $(400:110)^2 = 13.2$; $1/0.90^2 = 1.23$; $RI = 4.2\,\text{kV}$; $400\,\text{kV} : 0.4\,\text{kV} = 1000$. answers.py agrees.
- English against Finnish by script: answer 13.2231, unit MW, tolerance 0.02, kind and every number of the task text and the solution are the same.
- Box answer 13.2231 MW, shown 13 MW (two figures from $4.0\,\Omega$): 13 is 1.7 % away, inside the 2 % tolerance.
- Symbolic form $P_\text{h} = RP^2/(U^2\cos^2\varphi)$ derived before substitution and checked by the second route $3RI^2$.
- Model: $P = \sqrt{3}\,UI\cos\varphi$ with $U$ the line voltage and $I$ the phase-conductor current; the task says three-phase and gives both equations. $U^2 : R$ excluded with the right reason.
- Source fetched 16 Nov 2026 (HTTP 200): Fingrid's page lists (2025) 5 400 km of 400 kV, 1 000 km of 220 kV and 7 600 km of 110 kV power lines and 320 km of HVDC cables; distribution networks join typically through the 110 kV network and operate at 0.4–110 kV. Every number the English solution attributes to the source is there. The page gives no reason for the high voltages, and the solution says so.
- d): four simplifications, each with the right direction of effect; the ratio is unchanged by $\cos\varphi$. "Becomes internal energy … transferred to the surroundings as heat", as the guardrail requires.
- Scope: transmission losses and three-phase power, inside FY7.
