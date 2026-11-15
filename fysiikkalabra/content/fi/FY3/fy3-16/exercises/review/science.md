VERDICT: FAIL
CONTENT-HASH: e165c1601691d33b

## Blocking
- exercises/solutions.md:58, exercises.json:128, answers.py:18 (L2-01) — A (internal consistency and assessment). L2-01 asks the same thing as L3-03: how large the ice pack must be so that the ice lasts 6,0 h. That is a minimum. L3-03 now rounds its minimum up (1,511 → 1,6 kg) and says that the lower value "ei riittäisi". L2-01 still rounds 1,617 kg down to 1,6 kg, which by that rule does not last 6,0 h. A student who applies the set's own rule answers 1,7 kg. That is 6 % off the key, so the page marks it wrong. — Treat L2-01 the same way: give 1,7 kg in answers.py (ceil) and in the key, with the same "pyöristetään ylöspäin, 1,6 kg ei riittäisi" sentence in the Vastaus. Alternatively, reword the task so it no longer asks for a minimum.

## Polish
- exercises.json:314 (L3-03) — The tolerance of 0,06 is needed so that the computed 1,51 kg is accepted, but it also accepts 1,5 kg, which the solution calls insufficient. No tolerance can separate the two, so state the reason in the Vastaus as well: 1,5 kg counts as correct to two figures, but 1,6 kg is the safe choice.

## Checked
- I recomputed all 21 numeric answers in one script with my own formulas: Q = cmΔT, sm, rm; P = UAΔT; P = c(m/t)ΔT; and the energy balances. Each one agrees with answers.py; the keys are rounded correctly.
- L3-03: the wall brings 486 000 J and the drinks 50 280 J, against 355 000 J per kg of freezer ice, so m = 1,511 kg. answers.py's ceil gives 1,6, and the solution's reasoning and check are consistent.
- L2-05, edited mechanism line: the resistors convert electrical energy into internal energy, which is transferred as heat to the stones. This is correct. η = 8,16/10,8 = 75,6 % → 76 %.
- L1-08, edited wording ("jouleina"): t = 251 s → 250 s; the physics is unchanged.
- L2-06: the least-squares slope is −99,8 kWh/K, so UA = 139 W/K, and the line crosses the axis at about 20 °C (the indoor temperature). This is correct.
- L2-09 and L2-10: the figures' data give 900 J/(kg·K) and 220,6 kJ (2,44 h).
- L3-02: the water can give 251 kJ, more than the 167 kJ needed to melt all the ice, so all of it melts and T = 8,06 °C. L3-05: m = 54 000 kg, the three stages need 2,72, 18,04 and 0,57 GJ, and the power is 592 kW → 590 kW.
- L3-04: ΣΔT = 126 K and E = 5443 kWh; electricity costs 816 € and wood 336 €, so the saving is 481 € → 480 €.
- Multiple choice: L1-06, L1-07 and L2-08 (t₂/t₁ = 2) each have exactly one correct option, and every distractor's feedback is right.
- The hash was the same at the start and the end.
