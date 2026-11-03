VERDICT: PASS
CONTENT-HASH: a3316f786ce951c7

## Blocking

## Polish
- exercises/solutions.md:29 (L1-03, Järkevyys) — "narun on vedettävä kiveä hieman painoa suuremmalla voimalla" treats the rope's pull as the 6.7 N net force. In a horizontal circle the rope also holds the weight, so its tension is √(6.7² + 4.9²) ≈ 8.3 N. Say that the rope's horizontal component is 6.7 N, or compare the net force (not the rope's pull) with the weight.

## Checked
- I recomputed all 12 answers in one script with my own formulas: 5.0; 1.7534; 6.6667; 7.9057; 900; 4.3333; 4.7374; 6.012; 2.0636; 27.6193; 1.4067; 201.3566. All match exercises.json and answers.py.
- Reasonableness numbers: L2-01 μ0 ≥ 0.340, L3-01 dry 78 km/h (√8 ≈ 2.8), L3-02 period 0.711 s, L3-03 453 m at 120 km/h (2.25 times), and L2-03 v²/r = 4.8 m/s², which is less than g.
- Force solutions (L2-01, L2-03, L3-01, L3-02, L3-03): the forces suit each situation, x points to the centre, there is no centrifugal or separate centripetal arrow, the voimakuvio lengths are consistent (N = G on level ground, N < G on the bump), and each solution solves symbolically before substituting.
- Conversions: 72 and 80 km/h to m/s, m/s to km/h with 3.6, and kN.
- Significant figures follow the limiting data (L1-02 to 3 figures, the rest to 2).
- Stated conditions: a level road and no air or rolling resistance in the friction tasks, a smooth table in L3-02, and "oletetaan vaakasuora ympyrä" for the hammer.
- Scope: rotation frequency f = 1/T and no ω.
