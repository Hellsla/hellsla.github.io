VERDICT: PASS
CONTENT-HASH: 6484663d453f39fa
SCOPE: full: en unit.md (incl. the three new pysahdy boxes, the raster hero and ominais), inquiry.json, exit-ticket.json, teacher.md, sovella/tasks.json, solutions.md, answers.py; fidelity to fi. Language: en.

## Blocking
(none)

## Polish
- The Doppler symbol differs inside the unit: the Formula section and pysahdy box 3 use $v_\text{L}$, but the lt-6 feedback and the *Train* hints and solution use $v_\text{s}$. The Finnish version has the same split. The physics is the same, but one symbol would read better.
- s7 c (carried over): the model answer says P is "not completely silent because the farther loudspeaker is heard slightly more weakly", but the task text says that loudness difference is ignored. Adding "in practice" would fix the clash.

## Checked
- pysahdy boxes, judged first: the physics of all three is the same as in fi (word-for-word meaning and the same formulas). 1) The source sets the frequency and $v$ grows in water, so $\lambda = v/f$ grows. This agrees with the Key idea paragraph (0.12 m to 0.50 m) and with lt-3. 2) With in-phase sources, $\Delta s = \lambda/2$ is the $n = 0$ destructive condition. This agrees with lt-4, tarkistus-1 and s7 c. 3) An approaching source has a denominator $v - v_\text{L} < v$, so $f > f_0$. The condition ($v_\text{L} < v$, only the source moves) is stated in the paragraph just above the box. All three are type C at most; no A or B findings.
- Raster images: in ominais.webp the string has nodes at both ends; the open tube has displacement antinodes at the ends and a node in the middle; the closed tube has a node at the closed end and an antinode at the open end. These match the overlaid N/A labels and the $L = \lambda/2$, $\lambda/2$, $\lambda/4$ labels. In hero.webp the arcs are about 4.3 times farther apart in water than in air, which matches 1500/350.
- One script recomputed every number from the task data with my own formulas, and every value agreed: the whistle (0.117 / 0.50 m); tube B 342.6 m/s and tube A 342.8 m/s, with the mistakes 170.4 and 85.2; the suspension k = 110 363 N/m and f = 1.472 Hz, with its mistakes; the buoy 1.722 m/s; the train 27.46 m/s, f0 517 Hz; the concert 178.3 m; the quake 119.3 km, with its mistakes; the echo 18 m; the rope 1.2 m; the Moon pendulum 0.164 m. Sovella: s1 142.6 m/s, 3.118 m, 577.2 mm, 70.8 mm, 108.5 Hz. s2 11.33 mm, 2.04 m (3.5 %), 30.54 and 31.08 kHz. s3 T² values; the least-squares fit gives k = 4.040 s²/m and b = 0.055 s²; the read values give g = 9.778 m/s², intercept -0.014 m and l = 0.9768 m; a fit forced through the origin gives 9.58 m/s². s4 100 dB, 80 dB, 15 min, ×31.6. s5 354.2 ± 51.6 m/s, 309–415 m/s, 334 m/s. s6 18.79 m/s, x = 21.59 m, 39.59 m, 26.17 m/s², 4.867 s, energy check 27.96 kJ. s7 6.0 / 6.5 / 0.50 m, λ = 1.001 m, 686.8 Hz. s8 0.600 m, 30 m/s, 37.5 Hz, f1 = 12.5 Hz, f2 = 25 Hz, 20 Hz giving 1.6 loops.
- Points: every part's criteria add up to the part's points. The set totals 20 + 5·15 + 12 + 13 = 120, as teacher.md now says ("other seven").
- Fidelity: a number-by-number comparison of fi and en shows the same numbers in tasks.json, inquiry.json, exit-ticket.json, unit.md and teacher.md. In solutions.md the only differences are SVG coordinates. The inquiry diff only splits paragraphs.
- Scope is FY5 plus FY4 energy in s6 and FY1 measurement in s3/s5; nothing comes from later courses. Correct options are unique and the distractor feedback is right.
- Hash 6484663d453f39fa (units.py hash --lang en) at the start and at the end.
