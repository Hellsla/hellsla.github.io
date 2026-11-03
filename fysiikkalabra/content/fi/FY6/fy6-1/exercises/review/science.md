VERDICT: PASS
CONTENT-HASH: 83920706a91f4df7

## Blocking

## Polish
- exercises/solutions.md:9 (L1-01 Järkevyys): the comparison "21 W : 12 V = 1,75 A" uses power and P = UI, which this lesson does not teach yet. Either keep only the value ("auton jarruvalon lampussa noin 1,8 A") or drop the comparison.

## Checked
- Recomputed every answer in one script with my own formulas, and all agree with exercises.json and answers.py: L1 1,5 A, 20 C, 9,0 V, 1800 J, 30 s; L2 108 C, 9,99·10¹⁷, 39,96 kJ, 11 C; L3 8,0 h, ratio 1,2.
- Both round 1 polish items are fixed: the brake-light value is right (1,75 A), and L1-02 now names 0,50 A as the motor current.
- L2-04 virta_kuvaaja: 0,40 A for 0–20 s, 0,10 A for 20–50 s, 0 afterwards. This matches the description and the solution's readings, and the area gives 8,0 + 3,0 = 11 C. The graph does not show the charge.
- L2-03: 3000 mAh = 10 800 C and E = 39 960 J ≈ 40 kJ. The check mgh = 40 kg·9,81 m/s²·100 m ≈ 39 kJ is right.
- L3-01: Ah is a unit of charge, 7200 C : 0,25 A = 8,0 h. L3-02: 16 200 J : 13 500 J = 1,2. The capacities are realistic.
- L3-03 kaavio_malli: two cells in series with + up and the upper cell's − on the lower cell's +; a closed switch, the lamp and the ammeter are in one loop, and the I arrow points + → around the loop. This agrees with the answer text and the model solution.
- Every solution solves symbolically first, converts before substituting, and justifies significant figures by the limiting datum. The reasonableness checks are real checks.
- The notation (I, Q, t, U, E, N, e) matches the brief's lesson, and nothing is beyond FY6 scope.
