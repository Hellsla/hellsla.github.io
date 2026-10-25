VERDICT: PASS
CONTENT-HASH: 941320a85db9b4cb

1. solutions.md: all 12 solutions recomputed in Python (python3 -I); every substitution, intermediate value and unit is correct (kg · m/s² = N throughout; L3-03 reading = N / (m/s²) = kg).
2. exercises.json: every `answer` equals the solutions.md final answer (39, 6.0, 49, 1.5, 62, 5.0, 0.59, 1190, 5.9, 6.8, 133, 0.99). Exact values: 39.24, 6.0, 48.6, 1.5, 62.0, 4.995, 0.5886, 1187.55, 5.886, 6.807, 133.22, 0.9908.
3. Tolerance 0.02: the largest deviation of the unrounded value from the stored answer is 0.8 % (L1-03). Plausible student roundings stay inside: L2-03 1185/1187/1187.55 vs 1190 (<=0.4 %); L3-01 6.79-6.84 vs 6.8; L3-02 133.3 vs 133; L3-03 0.989 vs 0.99. L2-03 and L3-02/L3-03 state both g values, so no ambiguity.
4. Sanity-check sentences in solutions.md are numerically right (294 N on Earth; 1.62/9.81 = 0.165 about 1/6; 2.5 times Earth for Jupiter; 83 % decrease; mass ratio about 6).
5. exit-ticket.json: 29 N (29.43) and 4.9 N (4.86); 7.5 cm; 690 N (686.7, 2 sf) all correct.
6. lesson.md: worked example 1177.2 N rounds to 1180 N = 1.18 kN, Mars 445.2 N rounds to 445 N; spring proportionality examples (5.0 N, 2.0 cm; 10 N, 4.0 cm; 2.5 N, 1.0 cm) correct; table g values consistent with NOTES.md; 1 N = 1 kg·m/s² stated correctly; 70 kg gives about 690 N.
7. check_latex.py: all LaTeX ok (7 fragments).
8. Hash unchanged at the end of the review (941320a85db9b4cb).
