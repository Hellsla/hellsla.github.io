VERDICT: PASS
CONTENT-HASH: f7828db03e13325f

## Blocking

## Polish
- solutions.md:237 (L2-10 Järkevyys) — the voltage drop $RI \approx 4{,}2\,\text{kV}$ of one conductor is better compared with the phase voltage $110\,\text{kV} : \sqrt{3} \approx 64\,\text{kV}$ than with the line voltage; the conclusion (small) is the same.
- exercises.json (L2-10) — $200\,\text{MW}$ on one $110\,\text{kV}$ line (1050 A) is at the upper edge of what such a line carries; fine for the comparison the teacher's assignment sets, and the solution already says the numbers are a model.

## Checked
- Delta round 1: only fy7-8-L2-10 (FY7-A1) judged; hash identical at start and end.
- Recomputed from the task text: $I = P/(\sqrt{3}\,U)$ = 1049,7 A and 288,7 A; $P_\text{h} = 3RI^2$ = 13,22 MW and 1,000 MW (6,6 % and 0,50 % of 200 MW); ratio $(400:110)^2 = 13{,}2$; $1/0{,}90^2 = 1{,}23$; $400\,\text{kV} : 0{,}4\,\text{kV} = 1000$. answers.py agrees.
- Box answer 13,2231 MW, shown 13 MW (two significant figures from $4{,}0\,\Omega$): 13 is 1,7 % away, inside the 2 % tolerance; currents with three figures from 200 MW and the voltages.
- Symbolic form $P_\text{h} = RP^2/(U^2\cos^2\varphi)$ derived before substitution and checked by the second route $3RI^2$, a real check.
- Model: $P = \sqrt{3}\,UI\cos\varphi$ with $U$ the line voltage and $I$ the phase-conductor current, as in the brief; the task says three-phase, as the brief requires for leaving the two-conductor model. $U^2 : R$ excluded with the right reason.
- Source fetched 16 Nov 2026 (HTTP 200): Fingrid's page lists (2025) 5 400 km of 400 kV, 1 000 km of 220 kV, 7 600 km of 110 kV lines and 320 km of HVDC cables; distribution networks join typically through the 110 kV network and operate at 0.4–110 kV. All the solution's attributed numbers are there. The page gives no reason for the high voltages, and the solution says so instead of attributing one.
- d): four simplifications each with the right direction of effect (R equal at both voltages, $\cos\varphi = 1$, constant power, only conductor resistance); the ratio is unchanged by $\cos\varphi$. "Sisäenergiaksi … siirtyy lämpönä" as the guardrail requires.
- Scope: transmission losses and three-phase power, inside FY7 and the brief.
