VERDICT: PASS
CONTENT-HASH: 888c15245a63228d

## Blocking

## Polish
- exercises.json:57 — L2-02 stores 1.6 while the solution answers 1.60 "three significant figures" — store 1.60/1.605 or keep, tolerance covers it.

## Checked
- Exercise brief in the packet is empty (tool bug); judged against the English lesson's Kaava, example and theory (laser photons hf = E2 − E1, P = (N/t)hf, quantum dots).
- Recomputed all 12 answers in one script with my own formulas: all within 0.8 % of exercises.json and answers.py (e.g. L1-04 1.607e16, L2-01 75.94 %, L2-03 527.7 nm, L2-04 5.04 MW, L3-02 2.03e18 1/s, L3-03 9.22e4).
- L3-01: inversion with the ground state as lower level needs > N/2 ions excited, E ≥ 1.8 J; stated as a lower limit with the no-decay assumption in the task.
- L3-02: one pump photon → at most one 1064 nm photon, two → one 532 nm; energy check 0.76 W < 1.0 W is a real check.
- L2-01 quantum-defect ratio λp/λL and L3-03 qubit energy 2·10⁻⁵ eV are correct physics.
- Solutions solve symbolically first, show conversions, give sig-fig reasons and real reasonableness checks.
- Scope: within FY8 central contents (laser and quantum structures).
