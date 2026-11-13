VERDICT: PASS
CONTENT-HASH: 09f7e24961be1824
Round: 5
Mode: full

## Blocking
(none)

## Polish
(none)

## Checked
- All 19 numeric answers recomputed in one independent script (my own formulas from the task texts): every one within its tolerance; for L2-07 my least-squares line through the origin gives U = 0.3505 W/(m2 K), matching 0.35.
- fy3-12-L2-09 (now two steps): read 102 W/m2 from earth-flows, P = 102 W/m2 * 5.1e14 m2 = 5.20e16 W = 52 PW. Multiplying by the whole area is right because 341 and 102 W/m2 are averages over the whole sphere (341 = S/4); two figures from the area, real back-check.
- fy3-12-L3-03: the task now defines the coefficient of performance as heat delivered per kWh of electricity; W = (U1 - U2) A Delta T t / epsilon = 2755 kWh / 2.8 = 984 kWh, answer 980 kWh. The heat-pump argument (it moves heat using electricity, so a smaller heating need means less electricity) is correct and uses "coefficient of performance", not efficiency, as the guardrail asks.
- fy3-12-L1-09: U = lambda/d = 0.14/0.20 = 0.70 W/(m2 K), P = 0.70 * 10 * 30 = 210 W; the formula is given in the task, so no physics beyond the lesson; 4 % tolerance for other table values.
- P = U A Delta T used with constant temperatures (steady state) stated or implied in each task; parallel parts added (L2-01, L2-08); L2-08 order door < roof < windows < wall (60, 216, 288, 459 W) correct.
- Energy balance and albedo: L1-05 239 W/m2, L2-04 3.4 W/m2 (labelled hypothetical), L3-04 0.34 W/m2 with the upper-limit simplification named; L3-05 two-layer model consistent at both top and surface, S = 398.3 W/m2, 16.3 °C; table values agree with sigma T^4 within 1 W/m2.
- Q = c m Delta T used only without a change of state (L2-05, L3-01, L3-02, stated in the solutions); L3-02 ocean mass 2.6e20 kg is realistic for the top 700 m.
- Multiple choice L1-06, L1-07, L1-08: exactly one correct option each; distractor feedback right; L1-08 uses the net-transfer wording and says radiation goes both ways (guardrail).
- Figure earth-flows: arrow shafts to scale (34 and 10 units for 341 and 102), the asked arrow is dashed and marked not to scale; the description gives the same data and not 239.
- Scripted comparison with the Finnish exercises.json: same answers, units, tolerances, figures and task-text numbers for all 23 exercises. Hash identical at start and end.
