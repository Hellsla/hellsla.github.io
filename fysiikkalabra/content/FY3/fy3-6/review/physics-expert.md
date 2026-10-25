VERDICT: PASS
CONTENT-HASH: fbd6190138f1aa85

## Blocking

None.

## Polish

None. Both round-2 items are applied correctly (lesson.md:100 and solutions.md L3-02).

## Checked

- Hash before and after the review: fbd6190138f1aa85 (unchanged). lint: 0 errors, 0 warnings. check_latex: all 13 fragments OK.
- Diff against c2ad583: the formula splits (Q = cmΔT / ΔT, the T-solving derivation, the example's two displays, the 35 °C working) change layout only. No number, sign or step differs from round 2.
- lesson.md:15-47: Q = cmΔT with its sign convention, C = cm, the balance c1m1(T1−T) = c2m2(T−T2) and the derivation to T = (c1m1T1 + c2m2T2)/(c1m1 + c2m2) are all correct. The weighted-mean sentence (l.48) is correct.
- lesson.md:87-99: c_metalli = 5656,5 / (0,200 · 75,5) = 374,6 ≈ 3,7·10² J/(kg·K). A reading of 24,6 °C gives 383 J/(kg·K). Lossless copper gives 24,618 °C, so "24,6 °C" and the sim default agree. 0,300 · 4190 = 1257 J/K and 0,200 · 374,6 ≈ 75 J/K are correct.
- lesson.md:100: the 0,1 K gap is now put down to reading resolution or to heat going into the vessel and air. This is physically sound. It is a real-world aside that does not contradict the stated idealisation, because it says "todellisuudessa".
- lesson.md:105-115: the 35 °C working now has the hot water on the left (80 − T = 3T − 60, so 140 = 4T, so T = 35 °C). The row references in l.115 are correct. The weighted mean (3,0 · 20 + 1,0 · 80)/4,0 = 35 °C is correct.
- solutions.md L3-02: 3,6 K is correctly called an upper limit (evaporation and night-time radiation are left out). The L2-02 ΔT = 80 K line is correct.
- answers.py: every line uses the right formula, sign and conversion (L1-04 is negative, L1-05 ΔT is 18 K, L2-03 adds ΔT to T_alku, L3-01 uses the 260 K drop for the stones, in L3-02 the area cancels). I recomputed L2-04 = 27,11 °C, L3-02 = 3,58 K and L3-03 = 3,27 m³ by hand.
- The solutions.md sanity checks and exit-ticket.json (419 kJ, about 9 times, 50 °C and 65 °C) are physically correct. sim.js uses exactly the lesson's Teq, with C = cm and Q_body = Q_water, and no approximation. It is unchanged, as are the other files.

```
{"fy3-6-L1-01": 0.633528, "fy3-6-L1-02": 210.6, "fy3-6-L1-03": 720.0, "fy3-6-L1-04": -35.196, "fy3-6-L1-05": 18.9, "fy3-6-L2-01": 77.6, "fy3-6-L2-02": 209.5, "fy3-6-L2-03": 53.749403, "fy3-6-L2-04": 27.113624, "fy3-6-L3-01": 12.086538, "fy3-6-L3-02": 3.579952, "fy3-6-L3-03": 3.273438}
```
