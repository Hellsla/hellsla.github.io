VERDICT: PASS
CONTENT-HASH: c6de36add8c9d166

## Blocking

## Polish
- solutions.md:150 (L2-05): "kolme merkitsevää numeroa kuten jaksonajoissa ja pituuksissa" is not true of the data. The lengths 0,20–0,80 m and the time 0,90 s have two significant figures. Fix: justify three figures by the fit through five points, or give 9,8 m/s². Both are inside the 4 % tolerance.
- answers.py:32 (L2-06): the comment says "-> 20,1 N/m", but the solution answers 20 N/m with two figures. Make the comment match.
- solutions.md:171 (L2-07): "erotus 0,14 s" is the period difference 2,15 s − 2,006 s = 0,144 s, but part b) lists 0,14 s as the 20° difference of t₁₀. Fix: name the difference, or justify the figures from t₁₀: 1,44 s ± 0,2 s gives 7,2 ± 1 %.

## Checked
- The hash was the same at the start and at the end.
- One script recomputed all 22 numeric answers from the task text. Each matches answers.py within the tolerance.
- My own least-squares fits give these values. L2-05 through the origin: g = 9,78 m/s² (the solution reads 9,77). L2-06 through the origin: k = 20,07 N/m (20,14). L3-04 with an intercept: k = 25,12 N/m and m₀ = 20,8 g (25,14 and 21 g). The data follow T ∝ √m and T ∝ √l, and L2-07's t₁₀ values match the lesson's T:T₀ table (20,10 / 20,22 / 20,68 / 21,53 s).
- L3-03: the lag is t(1 − √(l/(l+Δl))) = 21,7 s, the clock model is right, and the warning about rounding the intermediate result is correct (26 s).
- L3-05: T/4 = 0,549 s, h = 1,82 cm, v = 0,598 m/s, and the harmonic model gives 0,599 m/s (+0,13 %). The explanation is right: mgα > mg sin α means more work.
- Significant figures (P7b): 50, 80, 120 and 200 N/m count their trailing zeros. Each stated limiting datum is the real one (0,80 kg, 0,20 kg, 0,050 m, 0,50 kg, 3,0 cm, 0,50 mm).
- Multiple choice: exactly one option is correct in L1-06, L1-07, L1-08 and L2-08. The reason choice in L2-08 (the pendulum's restoring force is part of the weight; the spring's −kx is not) is correct, and every distractor's feedback is right.
- Figure kuvaaja-k: 3 cos(2πt/0,40) gives A = 3,0 cm and T = 0,40 s, as L1-10 and L2-09 read it.
