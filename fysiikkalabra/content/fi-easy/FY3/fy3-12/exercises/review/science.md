VERDICT: PASS
CONTENT-HASH: 33c167b962f1698e

## Blocking
- none

## Polish
1. content/fi-easy/FY3/fy3-12/exercises/solutions.md (fy3-12-L1-05, Kuvaajan lukeminen): "Alempi oikea nuoli" for the dashed arrow has no upper partner any more. "Maan oikealla puolella oleva katkoviivanuoli" would match the figure.
2. content/fi-easy/FY3/fy3-12/exercises/exercises.json (fy3-12-L1-08): "kokonaisuutena" for the net transfer is a fair Selkeä suomi rendering (C), and the feedback says that both sides radiate. The guardrail word "nettomääräisesti" (as in the Finnish), with a short gloss, would keep the two texts aligned.

## Checked
- My own script recomputed all 21 numeric answers from the task texts: L1-01 432 W, L1-02 1,2, L1-03 30 K, L1-04 49 kWh, L1-05 239 W/m², L1-09 210 W, L2-01 −20 °C, L2-02 149 €, L2-03 211,7 kWh, L2-04 3,4, L2-05 6,98 W, L2-06 57,6 W, L2-07 0,35, L2-09 52,0 PW, L3-01 20,05 K, L3-02 0,139 K, L3-03 984 kWh, L3-04 0,343, L3-05 16,3 °C. All agree with answers.py, and each rounded answer is inside its tolerance.
- L2-09 (now two steps): 341 and 102 W/m² are averages over the whole sphere, so multiplying by 5,1·10¹⁴ m² is the right model. 102 · 5,1·10¹⁴ W = 52 PW, as observed.
- L3-03: the lämpökerroin is defined in the task (heat delivered per kWh of electricity), and W = Q/ε = 2755/2,8 kWh. It is a coefficient of performance, not an efficiency, as the guardrail asks.
- L2-07: a least-squares line through the origin gives 0,1753 W/K, so U = 0,351 W/(m²·K). The origin has a physical reason (ΔT = 0 gives P = 0). The text says "yleensä" and reads the slope from the line, not from the points.
- L3-05: both balances give S = 239/(1 − f/2) = 398,3 W/m². The table matches σT⁴ (390 at 288 K, 478 at 303 K, 240 at 255 K), and interpolation gives 289,4 K.
- L3-04: 90 · 3,6·10¹² · 0,54 / 5,1·10¹⁴ = 0,343 W/m². The model's limits, including that the estimate is an upper bound, are stated.
- The conditions are stated where they are used: P = UAΔT at constant temperatures, Q = cmΔT with no change of state, and the boundary of the energy balance.
- L1-06, L1-07, L1-08: exactly one correct option each, and every distractor's feedback gives the right physics.
- The figure earth-flows gives 341 and 102 W/m², and its description says the same. The asked flux is a "?".
- The fi-easy set matches the Finnish in every answer, unit, tolerance, figure and number. Hash the same at start and end.
