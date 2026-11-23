VERDICT: PASS
CONTENT-HASH: 958750c0c34be8fa
SCOPE: full (unit.md, inquiry.json, teacher.md, Sovella tasks/solutions/rubrics, answers.py); new ```pysahdy boxes judged first against the Finnish unit. Language: en.

## Blocking
- (none)

## Polish
- pysahdy 3 (perfectly inelastic): "Kinetic energy is transformed into internal energy" reads as if all of it. The Finnish partitive "Liike-energiaa" means part of it, and the paragraph above says "the largest share". "Part of the kinetic energy is transformed…" would match. Category C; the paragraph above it and lt-5 say "part".
- Earlier Polish stays open: s8 b "47 km/h" comes from the rounded 13 m/s (the unrounded value is 45 km/h); s7 d's closing remark about air resistance goes beyond the task's own assumption.

## Checked
- The three pysahdy boxes match the Finnish in physics. 1: the condition for momentum (sum of the external forces zero, or their impulse negligible); mechanical energy turns into internal energy, and the total is conserved. 2: W < 0 because friction opposes the motion, and the lost mechanical energy becomes internal energy. 3: momentum is conserved, kinetic energy is not. "Perfectly inelastic … move on together" matches the Finnish "kimmottomasti … jatkaa yhdessä". All three agree with Key idea, the Formula section, lt-3, lt-5, tarkistus-1 and Common mistakes.
- One script recomputed every number from the task data with my own formulas. Everything matches answers.py and the solutions:
  - s1: 26.58 m/s, −19.73 kJ, 48.1 N, 769 N, ratio 0.956
  - s2: μ 0.01015, 0.57 m/s, 3.652/3.110 J, 1.632 m
  - s3: least-squares fit t_r 0.864 s, a 6.26 m/s²; the read line gives 0.86 s and 6.25 m/s²; μ 0.637; distance 85.6 m
  - s4: 3.375, 9.54 MW, 12.7 MW, 88 kJ/m³
  - s5: −11.9/−6.3/−3.7/−2.9 %, 54 % of the kinetic energy lost
  - s6: 3.431 m/s, 2.611 m/s, 4926 J (24 %), 916 kN, 7.14 K
  - s7: 2.04 m, −15 J, 2.5 N, 5.0 and 6.32 m/s, α 19.9°, μ 0.135; d stays 5.0 m/s
  - s8: 5.4 N s, 12.56 m/s, 33.9 J, 8.04 m, −6.49 J, 1.0 N
- Inquiry recomputed: air track (momentum within 1.7 %; kinetic energy lost 1.7/25/41.7 %), cyclist 13.48 m/s, hydro 3.302 MW, seat belt 6.48 kN, body check 1.182 m/s, slide 53.6 %. Every mistake value (58.34, 1.39, 65.0, 20.99, 26.45, 181.8, 3.752, 4.264, 0.3366, 23.33, 0.7778, 64.81, 5.312, 0.75, 2.185, 46.44, 7.11) matches its feedback.
- Each prediction and choice has one correct option, and its distractor feedback is right. The wet-road example (22 + 31 → 22 + 62 m) is right.
- Wagon example: 51 200 kg·m/s, 41 → 20 kJ. The tormays figure is to scale (arrows 160:80, bars 160/160 and 160:80).
- Derivations: stopping distance, P = ηρQgh, P = ½ηρAv³ (rated-power limit stated).
- The tuuli picture matches its labels (A at the rotor, a v∆t cylinder upstream). The hero shows two identical wagons, the left one moving.
- Rubrics: every part's criteria add up to its points. Totals are 6×15 + 20 + 14 = 124, which matches teacher.md ("other seven", "six of 15 and one of 14"). Teacher.md's extra question (≈19 m + 252 m ≈ 270 m) is right.
- Scope: FY4 mechanics, plus FY3 cΔT in s6 as the stated combination of modules.
- The hash was the same at the start and the end.
