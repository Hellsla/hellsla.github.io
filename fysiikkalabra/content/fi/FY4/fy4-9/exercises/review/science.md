VERDICT: PASS
CONTENT-HASH: d2dfe6f7b0e18bab

## Blocking

## Polish
- exercises/solutions.md:175 (L2-07) — the rounding reason cites "nopeudessa 1,50 m/s pyöristettynä", but that speed has three significant figures and is not used in the calculation (Δv = I/m) — write "kaksi merkitsevää numeroa kuten massassa 0,50 kg".
- exercises/solutions.md:145 (L1-08) — "noin satakertainen" is wrong: 18 000 : 100 = 180 — write "noin 180-kertainen" or "kahden kertaluvun verran suurempi".
- exercises/exercises.json:362 (L3-05) — a 12 ms contact time read from video at 1 ms resolution needs a high-speed camera (an ordinary 30–240 fps video gives 4–33 ms steps) — write "kuvasi suurnopeuskameralla" or give the frame rate.
- exercises/exercises.json:362 (L3-05 c) — the stick-versus-bounce comparison repeats the idea of L3-03 (clay ball vs rubber ball). Acceptable as one part of a multi-step task; c) could instead ask for the fall and rise heights.

## Checked
- I recomputed all 20 answers with my own formulas in one script (trapezoids from the raw tables). The new ones are 1,8; 18 000; 927,45; 5,0 (a: 67 N); 2,88; 50,45 km/h (I = 981 N·s, c: 39,2 kN); 447,3 N (c: 251 N). All agree with exercises.json and answers.py.
- L1-06: exactly one correct option, every distractor is wrong and its feedback says why; p takes the sign of v.
- L3-05: the weight is included in the net force (N − mg)Δt = Δp, signs taken upward, v from free fall (fy4-3 prerequisite). The heights 1,23 m and 0,78 m are realistic for a basketball.
- L2-07 / L3-04: the area is computed correctly as Δt·Σ(interior points) because F = 0 at both ends; peak force > mean force; the rebound speed 1,38 m/s < 1,50 m/s is physically possible.
- Assumptions are stated in each task (weight neglected, friction neglected, only the airbag/belt force acting horizontally); the solutions use the same ones.
- Significant figures and tolerances fit the data; every new answer rounded to 2 s.f. lies inside its tolerance.
- Scope: everything is impulse, momentum change, area under F(t), mean force and 1-D signs; there is no conservation or 2-D content. Notation matches the brief (F_ka, v₀, Δp).
- Plan in docs/exercise-bank/FY4.md covered: MC direction, p = mv, error analysis, kick table, bumper experiment, force sensor area, soft/hard comparison, YO-style bounce. Levels are 8/7/5.
- Hash is the same at the start and at the end.
