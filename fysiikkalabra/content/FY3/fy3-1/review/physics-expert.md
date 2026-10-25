VERDICT: PASS
CONTENT-HASH: 941320a85db9b4cb

Findings (no FAIL-level issues):

1. lesson.md l.21 and l.57: g is written as 9,81 m/s² everywhere; bridging sentence ("sama luku kuin FY1:n putoamiskiihtyvyys, mutta tässä se mittaa vuorovaikutuksen voimakkuutta jokaista kilogrammaa kohti"), 1 kg weighs 9,81 N, and 1 N = 1 kg·m/s² are correct. Summary no longer equates g with a weight. Weight is explicitly not the cause of motion (FY3 scope respected).
2. lesson.md table (Kuu 1,62; Mars 3,71; Maa 9,81; Jupiter 24,8 m/s²) correct, Jupiter caveat (cloud tops) correct.
3. Worked example: 120·9,81 = 1177,2 N ≈ 1180 N (1,18 kN); 120·3,71 = 445,2 N ≈ 445 N. Correct. Apple ~1 N (0,981 N), 70 kg -> 686,7 N ≈ 690 N, bathroom scale / 9,81 m/s² and Moon ≈ 1/6 (0,165) correct.
4. solutions.md: wording "massan paino" correct, all numbers and sanity checks consistent (e.g. 30 kg Earth 294 N, 83 % decrease).
5. exercises.json: all 12 answers recomputed from problem text, all within tolerance 0,02 (output below). Level-3 tasks physically sound (L3-02 equal force, L3-03 scale shows G/9,81 m/s² -> 0,99 kg).
6. exit-ticket.json: 29,43 -> 29 N, 4,86 -> 4,9 N (≈1/6), 7,5 cm, 686,7 ≈ 690 N all correct.
7. sim.js: BODIES g in m/s²; G = m·g in N; full scale 100 kg·24,8 = 2480 N; texts correct; no N/kg.

Python output (python3 -I):
fy3-1-L1-01 39.24 39 N rel 0.0061 OK
fy3-1-L1-02 6.0 6.0 cm rel 0.0 OK
fy3-1-L1-03 48.6 49 N rel 0.0082 OK
fy3-1-L1-04 1.5 1.5 cm rel 0.0 OK
fy3-1-L1-05 62.0 62 N rel 0.0 OK
fy3-1-L2-01 4.9949 5.0 kg rel 0.001 OK
fy3-1-L2-02 0.5886 0.59 N rel 0.0024 OK
fy3-1-L2-03 1187.55 1190 N rel 0.0021 OK
fy3-1-L2-04 5.886 5.9 N rel 0.0024 OK
fy3-1-L3-01 6.8073 6.8 N rel 0.0011 OK
fy3-1-L3-02 133.2222 133 kg rel 0.0017 OK
fy3-1-L3-03 0.9908 0.99 kg rel 0.0008 OK

Hash re-run at end: 941320a85db9b4cb (unchanged).
