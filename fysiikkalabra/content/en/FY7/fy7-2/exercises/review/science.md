VERDICT: PASS
CONTENT-HASH: b165aaff977bb9ac

## Blocking

## Polish
- solutions.md:110 L3-02: the period is independent of speed only while v ≪ c, the condition the brief gives for r = mv : (qB). Add it to the reasonableness check, e.g. "at high energies a cyclotron's frequency must be adjusted" (carried over; not blocking at this level, C/B-borderline).
- exercises.json:100 L3-03: the unit "kertaa" is Finnish on the English page; use "times" (language only).

## Checked
- Full review triggered by commit c85fdffb: solutions.md:57–58 (L2-01) now shows r = m : (qB) · v as an aligned display, split over rows. It is algebraically the same as r = mv : (qB), the symbolic form stays in the Formula line, and the value is unchanged: 0.06463 m = 6.463 cm → 6.5 cm.
- Recomputed all 12 answers in one script with my own models (L3-01 from r = √(2mU : q) : B, L3-03 from v = √(2qU : m) and r = mv : (qB)): 1.2015 / 7.581 / 500 / 4.806 / 1.602; 6.463 / 3449 / 200 / 2.049; 4.006 / 22.86 / 1.409. Each is within the tolerance of exercises.json and equals `python3 -I lessons/FY7/fy7-2/answers.py`.
- answers.py computes the right physics on every line: qvB sin α, r = mv : (qB), v = E : B, E = U : d, qU = ½mv², qvB = mg, f = qB : (2πm), r ∝ √(m : q).
- Rounding follows the limiting datum. L3-01's 4.0 cm is justified by the difference's 0.1 cm precision, and L2-01's 500 V is read as at least two figures.
- The reasonableness magnitudes are right: v : c of 0.1 %, 0.17 % and 1.2 %; a proton radius of 14 m; 4.9·10⁸ at 10⁶ m/s; T ≈ 44 ns; 17 % heavier but an 8 % larger radius.
- Every solution is complete and solves symbolically first. The notation matches the brief, and the scope is FY7 plus the FY6 prerequisites.
- Hash at start and end: b165aaff977bb9ac (unchanged).
