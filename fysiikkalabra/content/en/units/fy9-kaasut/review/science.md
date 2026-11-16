VERDICT: PASS
CONTENT-HASH: 3faa649403b7a6f4
Round 2: delta against the version round 1 reviewed (fix round 1).
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- (none)

## Checked
- s2 c reasonableness: the added sentence is right. Recomputed: 485.1 kW - 174.6 kW - 232.9 kW = 77.6 kW (= 16 % of the fuel power = 25 % of 310.5 kW); the row with rounded powers gives 77 kW. answers.py key `fy9-kaasut-s2-waste` computes the same quantity from unrounded values.
- s5 "Yleisiä virheitä": "the molar mass comes out at about two thirds of the correct one" is now unambiguous and right (210 : 311 = 0.68; the amount of substance itself becomes 1.5 times too large).
- s7 c task text: "derive in symbols ... heat transferred to the water per unit time (the heat power) and the volume flowing per second" matches the rubric and the solution (P_2 t = c rho V dT); the task stays solvable with the given data. Recomputed dT = 2.7e9 W : 2.388e8 W/K = 11.3 K.
- s7 e: "about 21 C" now agrees with 10 C + 11 K and with the reasonableness check of part c (the old 20 C did not).
- practice.py check OK (7 tasks, 110 points). Hash the same at the start and the end.
