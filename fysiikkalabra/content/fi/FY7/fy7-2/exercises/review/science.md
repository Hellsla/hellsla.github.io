VERDICT: PASS
CONTENT-HASH: 17fbd6419d57bd14

## Blocking

## Polish
- solutions.md L3-02: "kierrosaika ei riipu vauhdista" holds while v ≪ c, which is the condition the lesson gives for r = mv : (qB). Fix: add to Järkevyys "kun protonin vauhti on pieni valon nopeuteen verrattuna; suurilla energioilla syklotronin taajuutta on säädettävä".

## Checked
- I recomputed all 12 answers in one script with my own models: L1 1,2015 / 7,581 / 500 / 4,806 / 1,602. L2 6,463 / 3449 / 200 / 2,049. L3 4,006 / 22,86 / 1,409. All are within the tolerance of exercises.json, and `python3 -I answers.py` prints the same values.
- L3-01 uses the right model: same U and q, so r ∝ √m, not ∝ m. The spots are 2(r₁₄ − r₁₂) apart. The checks of "17 % heavier, 8 % larger radius" are right.
- L3-02: T = 2πm/(qB) is derived and the speed cancels. T ≈ 44 ns is right.
- L3-03: r ∝ √(m/q) and r_α : r_p = 1,409 ≈ √2. "Alpha slower but heavier" is right.
- L2-01: the round 1 polish item (the 500 V precision) is fixed.
- L2-03 cites E = U/d from FY6, giving 3,0·10⁴ V/m and 200 km/s.
- L2-04: qvB = mg gives 2,05 mm/s, and 10⁸–10⁹ at 10⁶ m/s is right (4,9·10⁸).
- Magnitudes in the reasonableness checks: a ≈ 7·10¹² ≈ 10¹³ m/s² (L1-01), a proton radius of 14 m (L1-02), v : c of 0,17 % and 1,2 % (L1-03, L2-02).
- Conversions are explicit (mT, µT, cm, kV, km/s, MHz). Every solution runs complete from Annettu to Järkevyys and solves for the unknown symbolically first.
- Scope: everything is inside FY7 with FY6 prerequisites. Notation matches the brief (F_m, r = mv : (qB), v = E : B).
