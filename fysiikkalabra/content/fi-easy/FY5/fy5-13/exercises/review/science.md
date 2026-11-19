VERDICT: PASS
CONTENT-HASH: 866e8cd3c2dcfd03

## Blocking

## Polish
- solutions.md fy5-13-L1-09 — I could not check the MAFY values 971 m/s (He, 0 °C) and 331,5 m/s (air, 0 °C) here. The ±4 % tolerance covers small differences between tables. Worth checking against the MAFY table once.

## Checked
- Recomputed every answer in one script with my own formulas:
  - level 1: L1-01 41,0 Hz; L1-02 515 Hz; L1-03 32,7 Hz; L1-04 0,70 m; L1-05 392 Hz; L1-08 100 Hz; L1-09 639,5 Hz.
  - level 2: L2-01 5,38 Hz; L2-02 339,7 m/s; L2-03 33,3 cm; L2-04 60,0 m/s; L2-05 f/n mean 95,96 Hz, so 122,8 m/s; L2-06 λ = L₃ − L₁ = 0,670 m, so 343 m/s, and e = 0,45 cm; L2-09 31,25 Hz.
  - level 3: L3-01 131 Hz; L3-02 110 Hz; L3-03 f₁ = 170 Hz, L = 0,500 m; L3-04 f²/F = 328,1, 333,5, 326,7 and 332,1, mean 330,1, giving 199,0 Hz; L3-05 A open 330,9 m/s, B closed 330,7 m/s, mean 331 m/s.
  - All agree with answers.py and exercises.json, and every tolerance covers the rounded answer.
- Models: string and open pipe use n·v/2L; the closed pipe uses odd n·v/4L. Successive resonances differ by f₁ on a string and by 2f₁ in a closed pipe. In the resonance tube, the difference of resonance lengths removes the end correction, and the correction's sign (antinode just above the mouth) is right.
- L3-04: the data's f² ∝ F agrees with v ∝ √F. The implied linear density is about 1,8 g/m, which is plausible. The extrapolation to 120 N is named and its reliability judged.
- L3-05: the 1:2:3 and 1:3:5 ratios identify the pipes. 331 m/s fits cold air. The check that swapped types would give 165 and 662 m/s is right.
- Choice tasks (L1-06, L1-07, L2-07, L2-08): exactly one correct option in each; every distractor's feedback is right. L2-08: v/(4·L/2) = v/2L, so the frequency is unchanged.
- Figure fy5-13/kuvio-tehtava: 1,20 m on the ruler, four equal loops, five nodes. It agrees with L2-04 and L2-09.
- Every solution solves symbolically before substituting, and the significant-figure reasons are right. L2-01 is given 2 figures because of the 7,0 m/s difference. L1-08 is 1,0·10² Hz.
- L1-09 physics note (vocal-tract resonances rise, vocal-fold frequency barely changes) is correct.
- Hash identical at start and end.
