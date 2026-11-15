VERDICT: FAIL
CONTENT-HASH: 9218a0cc5bf3ce91

## Blocking
- content/fi/FY4/fy4-7/exercises/solutions.md:367 (fy4-7-L2-10, Lisähuomio) — **B** (claim true only under an unstated condition). "kun hitaampi auto on jo pysähtynyt, nopeammalla on vielä $13{,}3\,\text{m}$ jarrutusmatkaa jäljellä … noin $52\,\text{km/h}$" is true only for the *place* where the slower car stops (both drivers reacting at the same point), not for the *moment* the sentence names. Recomputed with the task's model: the slower car stops at $t = 3{,}78\,\text{s}$; at that moment the faster car moves at $12\,\text{km/h}$ and has $0{,}69\,\text{m}$ left. — Fix: state the condition as a place, e.g. "Siinä kohdassa, johon hitaampi auto pysähtyy, nopeammalla autolla on vielä $13{,}3\,\text{m}$ jarrutusmatkaa jäljellä, kun kuljettajat alkavat reagoida samassa kohdassa. Sen nopeus tässä kohdassa on …".

## Polish
- solutions.md:348 (a) — "Suurin osa ajaa siis lähellä rajoitusta, vähän sen yli": the group 0–10 km/h over is $48{,}2\,\%$, the largest group but under half, and the table does not say how far under the limit the $38{,}0\,\%$ drive — "suurin ryhmä ($48{,}2\,\%$) ajaa enintään $10\,\text{km/h}$ yli rajoituksen".
- solutions.md:370 (d) — "mittausasemat eivät ole niissä" (junctions, built-up areas) is stated as a fact of the source; the coordinator's record of the report says only that the stations are on main roads — soften ("mittausasemat ovat pääteillä") or check it in the report.

## Checked
- All 21 numeric answers recomputed with my own formulas: agree with exercises.json and answers.py inside each tolerance.
- L2-10 table, 268 stations, summer 2025, definitions of the shares: the same as the coordinator's record of the Fintraffic report; source dated (16.11.2026); every number the task needs is in the task, so no moving value.
- L2-10 b: $370\,370\,\text{J}$, $489\,815\,\text{J}$, ratio $1{,}3225$ (+32 %, speed +15 %).
- L2-10 c: $53{,}09\,\text{m}$, $66{,}37\,\text{m}$, $\Delta s = 13{,}29\,\text{m}$; answer 13.3, tolerance 0.05 accepts the shown $13\,\text{m}$; two significant figures justified.
- L2-10 c is derived from $v_0 + a t_\text{j} = 0$ and $s = v_0 t + \tfrac12 a t^2$ (symbolic first); kinematics is a prerequisite; scope FY4.
- L2-10 d: no causal claim about accidents from the table; model limits stated; braking energy "sisäenergiaksi".
- L1-07 proofreading fix: $80 \cdot 10 \cdot 12 = 9600\,\text{J} = 9{,}6\,\text{kJ}$, compared correctly with $9{,}4\,\text{kJ}$.
- Hash the same at the start and the end.
