VERDICT: PASS
CONTENT-HASH: a31ce9eef8a09de8

## Blocking

## Polish
- solutions.md:120 — L3-03: "$220\,\text{cm}^2$ eli $2{,}2 \cdot 10^{2}\,\text{cm}^2$, kaksi merkitsevää numeroa": under P7 (b) the first form reads as three figures. Give $2{,}2 \cdot 10^{2}\,\text{cm}^2$ alone. The area is a minimum, because d = 0,50 mm is the thinnest safe layer, so rounding 217 up to 220 is the safe direction (P7 c). One clause saying so would help.
- solutions.md:39 — L1-04: "$2{,}2 \cdot 10^{2}\,\text{pF} = 220\,\text{pF}$": the same issue, so drop "= 220 pF".
- solutions.md:80 — L2-03: "$1{,}0 \cdot 10^{2}\,\mu\text{F}$ eli $100\,\mu\text{F}$": the same issue, so drop "eli 100 µF".

## Checked
- Hash a31ce9eef8a09de8 at the start and at the end.
- I recomputed all 19 numeric answers in one script with my own formulas, including both least-squares fits (L2-05: C = 47,2 µF, so 3,40 mJ; L3-04: k = 100,0 V/s, C = 150 µF, 48,6 kW, charge time 18 s). Every one agrees with answers.py and exercises.json.
- The round-1 blocking item is fixed. L3-01 (:100) now reads $15{,}0\,\mu\text{J}$, three figures as in 120 pF and 500 V.
- The round-1 polish items are done too. L1-05 reads $3{,}6 \cdot 10^{2}\,\mu\text{J}$, L2-08 $3{,}7 \cdot 10^{2}\,\mu\text{J}$ and L2-01 $3{,}2 \cdot 10^{2}\,\text{V}$ alone. L2-07 names 24 V as the limiting datum, since 220 µF has three figures.
- P7 (b) elsewhere: 470 µF, 2200 µF, 1000 µF, 250 cm² and 220 pF are never named as limiting. 10 F, 60 MV/m and 2,0 kV count as two figures.
- P7 (c): the L2-01 maximum, U_max = 16 MV/m · 0,020 mm = 320 V, is exact, so it needs no rounding.
- Every tolerance lets an answer rounded to the data's figures pass (L3-03: 220 against 217,2 is 1,3 %; L2-05: 3,3–3,5 mJ is inside 4 %).
- Physics: C = Q/U; the plate-capacitor conditions (thin gap, dielectric filling the gap); U_max = E_max·d; W = ½QU = ½CU². Source connected or disconnected is handled right in L1-07, L3-01 and L3-02. The halving of the energy in L1-09 and L2-07 is stated as the result of the resistive-charging model.
- L2-06: the voltage rises per second are 3,5 / 2,0 / 1,4 / 0,8 / 0,5 / 0,3 V. Exactly one option is correct, and each distractor's numbers are right. L1-06, L1-07 and L1-09 each have one consistent key.
- L3-05: ratio 6,89; the scaling ε_r·E_max² is right.
- Scope: no capacitor connections and no exponential function. Everything stays inside "kondensaattori ja kondensaattorin energia" and "läpilyöntilujuus".
