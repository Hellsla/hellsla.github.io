VERDICT: FAIL
CONTENT-HASH: 7ea980554d63e713
SCOPE: full (the three new pysahdy boxes judged first, then unit.md, inquiry.json, teacher.md and the Sovella set s1-s8 with answers.py). Language: fi.

## Blocking
- teacher.md, Arviointi and Tuntisuunnitelma (65-75 min), A (internal consistency, points): the text says the task set is s3 at 20 points plus "muut viisi" at 15 points each, "yhteensä 95 pistettä", and in the plan "muut viisi tehtävää". The set now has eight tasks: s7 is worth 12 points and s8 13, so the total is 15+15+20+15+15+15+12+13 = 120. The intro in tasks.json already says eight tasks. Fix: say seven Osa II type tasks (five at 15 points, s7 at 12, s8 at 13), 120 points in total, and "muut seitsemän tehtävää".

## Polish
- Source speed symbol: the unit's formulas use $v_\text{L}$ (MAFY), but the feedback for lt-6 and the juna hints and solution use $v_\text{s}$, and s2 c uses $v_\text{l}$. The physics is right; using $v_\text{L}$ everywhere would match the formula section.
- jousitus, Periaate: "$T = 2\pi\sqrt{m/k}$" is written where $m$ has just been defined as the driver's mass (90 kg). The Kaava line correctly uses $m_\text{kori} + m$. The Periaate could also write the sum.
- pysahdy 3: "nimittäjä on pienempi kuin $v$" is correct. "Nimittäjä $v - v_\text{L}$ on pienempi kuin osoittaja $v$" would be clearer.

## Checked
- pysahdy 1: the source sets the frequency, which stays the same across the boundary; $v$ grows, so $\lambda = v/f$ grows. This agrees with the Ydinajatus answer: $350/3000 = 0{,}117 \approx 0{,}12$ m and $1500/3000 = 0{,}50$ m. pysahdy 2: $\Delta s = \lambda/2$ is the $n = 0$ case of $(n+\tfrac12)\lambda$, so the sound weakens, as in lt-4 and tarkistus-1. pysahdy 3 matches the stated Doppler formula and its condition ($v_\text{L} < v$, only one of them moves).
- Hero image: underwater wavefront spacing is about 4 times the air spacing (1500/350 = 4,3), so the aria text is right. Ominais image: the string has nodes at both ends, the open pipe has displacement antinodes at the ends and a node in the middle, and the closed pipe has a node at the closed end. The S/K labels sit at the right places.
- One script recomputed every number and printed it next to the given value. All agree:
  - Inquiry: pipes B and A 342,6 and 342,8 m/s, mistakes 170,4 and 85,2; jousitus k = 110 363 N/m, f = 1,472 Hz, all three mistakes; poiju 1,722 m/s; juna 27,46 m/s, f0 = 517 Hz; konsertti 178,3 m; seismic distance 119,3 km; echo sounder 17,8 m; Moon pendulum 0,164 m.
  - Sovella: s1 142,6 m/s, 3,118 m, 577,2 mm and 70,8 mm, 108,5 Hz; s2 11,33 mm, 2,04 m, 30,54 and 31,08 kHz; s3 fit k = 4,040 s²/m, b = 0,0546 s², intercept -1,35 cm, read g = 9,778 m/s², l = 0,977 m; s4 100, 80 dB, 15 min; s5 354,2 ± 52 m/s, 334 m/s at 5 °C; s6 18,79 m/s, x = 21,59 m, 39,59 m, 26,17 m/s², 4,867 s; s7 and s8 as before.
- Predictions: each has exactly one correct option, and every distractor's feedback is physically right. The explain model answer (spring force does not depend on mass; the pendulum's restoring force grows with $mg$) is correct.
- Scope is FY5 (plus FY4 energy in s6, and FY1 graph and measurement skills). Rubric parts sum to the part points. Significant-figure reasons are sound.
- Content hash 7ea980554d63e713 at start and end.
