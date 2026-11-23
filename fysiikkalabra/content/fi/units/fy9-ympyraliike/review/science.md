VERDICT: PASS
CONTENT-HASH: 45fe09079d5cb888
SCOPE: full: the three new pysahdy boxes first, then unit.md, inquiry.json, teacher.md, the Sovella set s1-s9 (tasks, solutions, rubrics, answers.py, figures.py).

## Blocking
- (none)

## Polish
- teacher.md "Arviointi" is out of date for the nine-task set: it says six long tasks and 95 points (five Osa II tasks of 15 points plus s3 at 20), but the set has 9 tasks and 142 points (s9 is 17). It also says "Kaikki aineistot ovat keksittyjä", but s7 uses real NASA data. "muut viisi tehtävää" (65-75 min) has the same problem. This is teacher-facing text, so it gives students no wrong physics, but its statement about where the data come from is wrong (category 6).
- s8 writes the static friction coefficient as $\mu_\text{s}$, while unit.md and the inquiry use $\mu_0$ (lepokitkakerroin). The notation should be the same everywhere.
- Carried over from earlier: in s9 b the intermediate value is written both as 331 N and as 330 N.

## Checked
- Pysahdy 1: the net force points to the centre because $\Sigma\overline{F} = m\overline{a}$ and the acceleration points there. Correct, and the cause is right.
- Pysahdy 2: the velocity is along the tangent and $a_\text{n}$ points to the centre. Correct and matches the Kaava paragraph above it.
- Pysahdy 3: doubling $r$ gives a quarter of $F_\text{g}$ ($\propto 1/r^2$). Correct and matches lt-5.
- One script recomputed every number from the task data with my own formulas and printed my values beside answers.py. All of them agree:
  - lesson geo: $r$ = 42 158 km, $h$ = 35 787 km, $v$ = 3,07 km/s, $r/R$ = 6,6
  - lt-6: 88,5 %; GPS 12,0 h; poljin 72,4 Nm (sin distractor 50,7 Nm); lumilapio 142,8 / 88,8 / 113,4 N; puhelin 27,6 km/h (diameter 39,1 km/h); tiedesatelliitti 98,4 min (h used as r: 3,01 min); kottikärryt 235,4 N (2299 N)
  - s1: 444,6 N, 45,3 kg, 5,392 kN, 11,09 cm, 32,4 kg
  - s2: 7,438 km/s, 101,4 min, 31,5 kN, 78,3 %, 25,41°, 2826 km; slant range to Finland about 39 600 km
  - s3: least-squares $k$ = 1,950 N·s², $b$ = 0,034 N; the circled points lie on that line; $m$ = 0,1976 kg; $T_\text{min}$ = 0,494 s; the line reaches 8,0 N at $1/T^2$ = 4,09 1/s²
  - s4: 8,69 m/s², 21,0 s
  - s5: 114,3 g, ±1,3 g, report error 26 %
  - s6: 22,76 m/s, 3696 N (6,28 mg), 11,21 m/s, 164,8 N
  - s7: 7,707 km/s, 8,773 m/s² (89 %), 83,9 kW, shadow 39 % (36 min), 138 kW in sunlight
  - s8: 75 m, 3,6 kN, 19,18 m/s (69,0 km/h), 61 %, 7358 N
  - s9: 382,6 N; H 331,3 N, V 14,7 N, 331,7 N at 2,54°; 29,08 kg; 270,5 N (−29 %)
- Inquiry: each choice item has exactly one correct option, and every distractor's feedback gives the right physics. The `numeric` mistakes are the errors their feedback names, and the `explain` model answer is correct.
- Force diagrams:
  - The geo image (webp) shows $\overline{v}$ along the tangent and $\overline{F}$ toward the centre. Rotation is counterclockwise for both, and the 6 h quarter turn is consistent.
  - In tilanteet, $N_2 = 2N_1$ and $N_1 + N_2 = G$. At the hump $N < G$ with $\overline{a}$ down, and the satellite has gravity only. kaarre is right.
  - No centrifugal force appears anywhere.
- Scope is FY5 plus the FY4 energy principle (s6) and FY6 power (s7 d). Significant-figure reasons hold.
- Rubrics: every criterion asks only what its part gives, and the points add up. s4 c correctly says the key lands slightly behind (antispinward).
- Hash 45fe09079d5cb888 at start and end.
