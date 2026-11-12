VERDICT: PASS
CONTENT-HASH: 6a4b518eb95a91d8
SCOPE: delta added-exercise from 2d22792f6d7cc426 base 611fb7d5c174
Mode: delta
Round: 2

## Blocking

## Polish
- exercises.json fy2-3-L1-09: the symbol "hp" usually stands for mechanical horsepower (745,7 W). The text now says "metristä hevosvoimaa", which settles the value; "hv" would be the symbol for the metric unit. Both values are inside the 4 % tolerance (6,71 against 6,62 MJ), so this is C.

## Checked
- Hash 6a4b518eb95a91d8 at the start and the end. I judged only the added L1-09 and L1-10.
- L1-09 recomputed in my own script: P = 5,0 · 735,5 W = 3677,5 W, Δt = 1800 s, ΔE = PΔt = 6,62 MJ, the same as answers.py and exercises.json (MJ, 0,04).
- L1-09 text now asks for the motor's mechanical output power and mechanical energy, as I suggested in round 1. The task and the solution now agree, and the "tasaisesti" condition is stated.
- L1-09 solution: ΔE = PΔt is solved before substitution, the hp → W, min → s and J → MJ conversions are shown, and the result has two significant figures. The checks (≈ 6,7 MJ, ≈ 1,8 kWh) are right.
- L1-10 now asks for the power ratio. From the figure, A gives 60 000 J : 40 s = 1500 W and B gives 40 000 J : 80 s = 500 W, so P_A/P_B = 3,0. This matches answers.py and exercises.json (unit "", 0,02).
- L1-10 figure: A runs to (80; 120) and B to (80; 40) on 10 s and 20 kJ gridlines, and the description agrees. No power is printed, so the answer is not given away.
- L1-10 solution: it uses the slope as the power (the lesson's statement). The check 120 kJ : 40 kJ at the same 80 s is independent of the main calculation and gives the same ratio.
- L1-10 differs from L1-04: L1-04 asks only P_A, and the ratio needs both lines.
