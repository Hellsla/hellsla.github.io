VERDICT: PASS
CONTENT-HASH: 724262a8cdeb5d9e
## Blocking

## Polish
- content/fi-easy/FY4/fy4-9/exercises/solutions.md:175 — L2-07 justifies two figures "kuten … pyöristetyssä nopeudessa 1,50 m/s", but 1,50 has three figures and Δv = I/m does not use it (same in fi:175) — say the mass 0,50 kg limits it to two.
- content/fi-easy/FY4/fy4-9/exercises/solutions.md (L3-03) — $v_\text{k}$ for the rubber ball's rebound speed clashes with $v_\text{k}$ = keskinopeus in this module (and the mean speed in L2-05) — use e.g. $v_\text{kumi}$ (in fi too).

## Checked
- One script recomputed all 18 numeric answers from the task data: L1 5,1; 6,0; 4,86; 6,0; 150; 1,8; 18 000; L2 6,0 kN; 6,44 kN; 1,5; 25,6; 927; 5,0 (a: 67 N); 2,88 (rebound 1,38); 450; L3 3,0; 57,6; 60; 50,45 (I = 981 N·s, rigid 39,2 kN); 447,3 (clay 251,1). All equal exercises.json, answers.py and the Finnish set.
- L2-08 (sig-fig fix): triangle 900 N, 12 ms from figures.py; I = 5,4 N·s, F_ka = 450 N; two figures now justified as read from the graph, same as fi.
- L3-01 figure ex-potku: trapezoid 60 N, sides 1,00 s and 0,60 s, 48 N·s → +2,0 m/s; area not shaded.
- Impulse principle with the net force everywhere: weight neglected where stated (L1-03, L2-02, L2-05, L1-09), weight included in L3-05 ((N − mg)Δt = Δp), friction/air resistance neglected where stated; signs and positive directions consistent with the brief.
- L1-06 and L1-09: exactly one correct option; each distractor's feedback names the real error (0,4 N ≈ 2 × weight 0,20 N; 4,0 J / 1 ms is power; grams give 400 kN).
- L1-08 error task: 64 800 is kg·km/h, factor 3,6 explained; 1,8·10⁴ kg·m/s.
- Reasonableness checks are real checks (weights vs contact forces, F_max > F_ka, drop 1,23 m and rise 0,78 m).
- Units and tolerances fit the data (L2-07 4 %, L3-04 3 % for trapezoid reading).
- Hash unchanged at start and end.
