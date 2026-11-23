VERDICT: FAIL
CONTENT-HASH: bb4c59d60a1ec530

## Blocking
- exercises/solutions.md:213 (fy6-7-L3-04 Formula) — A: the new row "S = aE_heater" is a false equation: S is the saving, while aE_heater is the cost of the heater's energy at one price, and a is undefined here (high or low price?). The next row S = E_heater(a_high − a_low) is right, but it does not follow from that row. — Replace the row with the costs at the two prices, e.g. "K_high = a_high E_heater \\ K_low = a_low E_heater \\ S = K_high − K_low \\ S = E_heater(a_high − a_low)". (The Finnish file has the same row, line 195.)

## Polish
- none

## Checked
- Other new Formula blocks derive from E = Pt (and P = UI, U = RI, K = aE, K = K_base + aE): every row correct, last row the one substituted into (L1 steps sum, E = UIt, K = aPt, ΔE = (P1 − P2)t, equal-energy t2 = P1t1/P2, E = (K − K_base)/a, resistor heating water, appliance-day sum and ×365).
- Recomputed: saving 6.0 kWh · 15.5 c/kWh = 93.0 c; average price 267.44 c : 19.0 kWh = 14.08 c/kWh; numbers in the diff unchanged.
- Paragraph splits (kWh choice, unit-error task, meter graph, refrigerator payback, oven, ENERGY STAR task) change no physics or reasoning order.
- Content hash checked at start and end.
