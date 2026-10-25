VERDICT: PASS
CONTENT-HASH: ebf5b7a614e84d36

Round 5. Lint 0/0, check_latex OK, test_sims PASS. The domain hash was the same at the start and at the end.

## Blocking
(none)

## Polish
1. lesson.md:22 — "paljon pienempi taivaankappale" is true for the Moon and is not presented as the rule, but "pienempi" alone reads as size, and size does not decide surface g (Uranus). — Optionally "massaltaan ja kooltaan paljon pienempi".

## Checked
- New L3-03: G = 26 kg · 9,81 m/s² = 255,06 N, m = G/3,71 m/s² = 68,75 ≈ 69 kg; answers.py:21, exercises.json:98–101 and solutions.md:89–95 agree; relerr 0,0036 < 0,02; the sanity check (≈ 2,6×) is right.
- lesson.md:22: weight stays a measure of the Moon–astronaut interaction, never a cause of motion.
- lesson.md:38: 1,62/9,81 = 0,165 ≈ 0,17 ≈ 1/6 is correct.
- lesson.md:55: "on 9,81 N" is correct and matches line 29 and the glossary.
- No N/kg in the domain files or tests/sims/fy3-1.json.
- answers.py:8–21: right formula, conversion and ratio on every line.
- Hand recomputation of L3-03, L2-04 and L3-01 (output below).
- sim.js:93–95: the scale text sits beside the full-scale tick (y ≈ 86 vs 90), so round-4 polish 1 is closed. G = m·g exactly, and the stretch and the arrow stay purely proportional.
- Exit ticket: 29 → 4,9 N, 7,5 cm, 15 N.

## Python output
```
fy3-1-L1-01 39.24 39 N relerr=0.0061
fy3-1-L1-02 6.0 6.0 cm relerr=0.0000
fy3-1-L1-03 48.6 49 N relerr=0.0082
fy3-1-L1-04 9.6 9.6 N relerr=0.0000
fy3-1-L1-05 62.0 62 N relerr=0.0000
fy3-1-L2-01 4.9949 5.0 kg relerr=0.0010
fy3-1-L2-02 0.5886 0.59 N relerr=0.0024
fy3-1-L2-03 1187.55 1190 N relerr=0.0021
fy3-1-L2-04 5.886 5.9 N relerr=0.0024
fy3-1-L3-01 6.8073 6.8 N relerr=0.0011
fy3-1-L3-02 133.2222 133 kg relerr=0.0017
fy3-1-L3-03 68.7493 69 kg relerr=0.0036
L3-03 by hand: G=255.06 N; m=68.75 kg; ratio 9.81/3.71=2.644; check 68.75*3.71/9.81=26.00 kg reading
L2-04 by hand: G=1.962 N; F=5.886 N
L3-01 by hand: m=1.8349 kg; G_Mars=6.807 N
lesson: Kuu/Maa=0.1651; 120*9.81=1177.2; 120*3.71=445.2; 70*9.81=686.7
exit: 29.43 4.86 7.50 14.715
```
