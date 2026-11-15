VERDICT: PASS
CONTENT-HASH: e7b751ab72402bfa

## Blocking

## Polish
- exercises.json:351 (L2-01) and :536 (L3-03) — the tolerance is 0,06. It still accepts 1,6 kg for L2-01 (5,9 % off 1,7) and 1,5 kg for L3-03, and the solutions call both values insufficient. The task text now says "Pyöristä vastaus ylöspäin", so the intent is clear, but the checker cannot enforce it. This is acceptable, because the computed minima 1,617 and 1,511 must stay inside the tolerance. — Optional: the Vastaus could add one sentence saying that the rounded-down value is accepted only as a calculation.
- L1-02 and L1-09 — both are a single Q = rm step for water at 100 °C. L1-09's MAFY lookup gives it a purpose of its own, so nothing needs to change.

## Checked
- Hash at start and end: e7b751ab72402bfa.
- I recomputed all 21 numeric answers in one script with my own formulas: Q = cmΔT, sm, rm; P = UAΔT; P = c(m/t)ΔT; and the energy balances. All of them are within tolerance and agree with answers.py.
- The round-1 blocking item is fixed. L2-01: m = UAΔT·t/s = 25 W · 21 600 s / 334 000 J/kg = 1,617 kg, rounded up to 1,7 kg. answers.py (ceil), the key, the solution's Vastaus and the task text now agree, and it matches L3-03 (1,511 → 1,6 kg).
- L3-03: the wall brings 486 000 J and the drinks 50 280 J, against 355 000 J per kg of freezer ice. The assumptions are stated in the task.
- L2-06: the least-squares slope is −99,8 kWh/K, so UA = 139 W/K. The line crosses the axis at 20,1 °C, which is the indoor temperature; the model answer for part c) is right.
- L2-05: η = 8,16 MJ / 10,8 MJ = 75,6 %. The part b) mechanism is right: the losses grow with the temperature difference.
- L2-09 and L2-10: the figures' data give 900 J/(kg·K) and 220 kJ → 2,44 h. The independent check gives 220,2 kJ, which is consistent.
- L3-02: all the ice melts, since 251 kJ > 167 kJ, so T = 8,06 °C. Reporting two significant figures is justified, because the subtraction loses one.
- L3-04: ΣΔT = 126 K and E = 5443 kWh; the saving is 480,6 €. The break-even wood price is 0,44 €/kg, as the model answer says. L3-05: the power is 592 kW, and freezing takes 85 % of the energy.
- Multiple choice: L1-06, L1-07 and L2-08 (t₂/t₁ = 2) each have exactly one correct option, and every distractor's feedback is right. The wording follows the guardrails: net transfer, and melting changes the interactions between particles.
