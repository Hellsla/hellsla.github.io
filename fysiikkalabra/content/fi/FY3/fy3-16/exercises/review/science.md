VERDICT: PASS
CONTENT-HASH: c3c6dce924fa959f

## Blocking

## Polish
- exercises.json:134 (L2-01) and :319 (L3-03) — with tolerance 0,04 the accepted ranges are 1,632–1,768 kg and 1,536–1,664 kg. The rounded-down values 1,6 kg and 1,5 kg are now rejected, as intended. So are the unrounded minima 1,617 kg and 1,511 kg (4,9 % and 5,6 % off). This fits the explicit "Pyöristä vastaus ylöspäin", and 1,617 still shows as "Lähellä". — Optional: one sentence in each Vastaus saying that an unrounded minimum is not accepted, because the task asks for the value rounded up.
- L1-02 and L1-09 — both are a single Q = rm step for water at 100 °C. L1-09's MAFY lookup gives it its own purpose, so nothing needs to change.

## Checked
- Hash at start and end: c3c6dce924fa959f.
- Round-3 change: L2-01 and L3-03 now have tolerance 0,04 (above). The answers 1,7 kg (ceil of 1,617) and 1,6 kg (ceil of 1,511) agree with answers.py, the task text and the solutions' Vastaus.
- I recomputed all 21 numeric answers in one script with my own formulas: Q = cmΔT, sm, rm; P = UAΔT; P = c(m/t)ΔT; energy balances; a least-squares fit for L2-06. All are within tolerance and agree with answers.py.
- L3-03: the wall brings 486 000 J and the drinks 50 280 J, against 355 000 J per kg of freezer ice. The assumptions are stated in the task.
- L2-06: the slope is −99,8 kWh/K, so UA = 139 W/K. The x-intercept is 20,1 °C, the indoor temperature, so the part c) model answer is right.
- L2-05: η = 75,6 %. The part b) mechanism (losses grow with the temperature difference) is right.
- L2-09: 900 J/(kg·K). L2-10: 220 kJ read from the figure, against 220,2 kJ computed, giving 2,44 h. Both figures and their descriptions give the needed points without the answer.
- L3-02: all the ice melts (251 kJ > 167 kJ), so T = 8,06 °C. Two significant figures are justified by the subtraction.
- L3-04: saving 480,6 €; break-even wood price 0,44 €/kg. L3-05: 592 kW, with freezing about 85 % of the energy.
- L1-06, L1-07 and L2-08 (t₂/t₁ = 2) each have exactly one correct option, and every distractor's feedback is right. The wording follows the guardrails (net transfer; melting changes the interactions between particles).
