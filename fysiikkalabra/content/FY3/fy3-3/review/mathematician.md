VERDICT: PASS
CONTENT-HASH: 3b1b29439e94b105

Round 2. Hash checked at start and end: 3b1b29439e94b105 (unchanged). check_latex.py: all LaTeX ok (5 fragments). All solutions recomputed in Python; every exercises.json answer equals the solutions.md final answer; units match.

Tolerance check (relative 0,02), routes tested: exact 273,15; 273; intermediate rounded to data sf; rounded final answer; rounded slope.
- L1-01..05, L2-01, L2-04, L3-01..03: all routes (273 vs 273,15, rounded intermediates) are inside tolerance. Worst case L1-05 (-270,45 / -270,3 vs -270): 0,17 %. L3-03 with 273: -126,5 vs -127: 0,4 %.
- L2-02: 101,55 (answer 102) 0,44 %; slope 0,33 exact; 90+0,3·35 = 100,5 also inside.
- L2-03 (the previous failure): exact -270,9; answer -270 deviates 0,3 %. Slope rounded correctly to 0,28 gives -265,7 (1,6 %, inside, band -264,6...-275,4). Graph reading -265...-275 inside. Only a 1-sf slope 0,3 (-246,7) or a truncated slope 0,27 (-276,3) falls outside, and neither is a correct rounding of 0,275. PASS.

Findings (none blocking):
1. exercises.json L2-03 — answer -270 sits close to the edge for a student who rounds the slope to 0,28 (1,6 % margin of 2 %) — acceptable; no change required. Optionally the answer could be -271 (exact -270,9) to centre the band, but then lesson example -270 and solution would differ.
2. solutions.md:134-135 — sijoitus 20 − 290,9 = −270,9 and final −270 (2 sf data) are consistent; correct.
3. lesson.md:24-62 — table, slope (137−100)/100 = 0,37 kPa/°C, p = p₀ + kθ, θ = −p₀/k = −270,27 ≈ −270 °C, all correct (least-squares fit of the table gives −271, consistent). Misconception ratio 293/283 = 1,0353 ≈ 1,035, +3,5 %: correct.
4. lesson.md:30-48 SVG — scale x 1,25 px/°C (0 at 445, 100 at 570, −270 at 107,5); y 1,5 px/kPa (0 at 250, 100 at 100, 137 at 44,5); the five other points (470,90),(495,78),(520,67),(545,56) match 107,115,122,129; dashed line (107,250)→(445,100) has the right slope 0,444; solid line 445,100→570,44; y-axis at x=70 = −300 °C as the caption states; "p = 0" label moved to (80,212) clears axis and dashed line. Correct.
5. exit-ticket.json — 283 K → 293 K, about 3,5 %; 0 K = −273 °C (3 sf): correct.
