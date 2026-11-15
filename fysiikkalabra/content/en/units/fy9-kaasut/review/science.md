VERDICT: PASS
CONTENT-HASH: 9163aae3c536a20f
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: solutions.md s5 "Yleisiä virheitä": "the amount of substance is calculated with the total pressure ... so the result is about two thirds of the correct one". The number is now right for the molar mass (210 : 311 = 0.68), but "the result" follows "the amount of substance", which becomes 1.5 times too large. Clearer: "so the molar mass is about two thirds of the correct one".

## Checked
- Item 18: 485 - 175 - 233 = 77 kW (16 % of 485 kW, 25 % of 310.5 kW): the corrected row is right. The two-thirds correction checked against s5 a (gauge pressure 210 kPa, total 311 kPa).
- s7 recomputed with my own formulas: a 0.3721; b 2700 MW, 64.8 GWh, 2.333e14 J, shares 63 % + 37 %, 38.4 + 64.8 = 103.2 GWh, 14.0 TWh a year; c c*rho*V/t = 2.388e8 W/K, 11.31 K, 47 kJ per kg, 18.0 K from 4300 MW; d 563 K, 283 K, 280 K : 563 K = 0.50. All agree with tasks.json, the solution and answers.py (practice.py check OK).
- Physics: steady-state energy balance, Q = cm dT applied to a flow with the expression derived in symbols, the stated upper-estimate assumption, the heat-engine argument of d (Q2 is a condition, not a loss; no formula beyond the unit's content) and the low-temperature argument of e are right. Significant figures justified by the source's "n. 1600 MW".
- Rubric points add up (2, 3, 4, 3, 3). Hash the same at the start and the end.
