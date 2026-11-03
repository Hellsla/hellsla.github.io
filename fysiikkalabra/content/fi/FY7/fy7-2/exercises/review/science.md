VERDICT: PASS
CONTENT-HASH: 589ff3dddc428f9b

## Blocking

## Polish
- solutions.md L2-01: "kaksi merkitsevää numeroa kuten kentässä 0,050 T". The 500 V is ambiguous in precision, so 0,050 T as the limiting datum is a fair choice, but say that 500 V is read as having at least two significant figures.

## Checked
- I recomputed all 12 answers in one script with my own models: L1 1,2015 / 7,581 / 500 / 4,806 / 1,602. L2 6,463 / 3449 / 200 / 2,049. L3 4,006 / 22,86 / 1,409. All are within tolerance of exercises.json, and answers.py prints the same values.
- L3-01 uses the right model (same U, so r ∝ √m, not ∝ m); I checked it through a full v = √(2qU/m) computation.
- L3-02: T = 2πm/(qB), with the speed cancelling. This is shown, not assumed.
- L3-03: r ∝ √(m/q) and r_α/r_p = 1,41, with the reasoning correct.
- L2-03: E = U/d from FY6 is cited, giving 3,0·10⁴ V/m and 200 km/s.
- L2-04: qvB = mg gives 2,0 mm/s. The 10⁸–10⁹ comparison in Järkevyys is right (5·10⁸ at 10⁶ m/s).
- Unit conversions are explicit (mT, µT, cm, kV, km/s). Every solution is complete: Annettu → Järkevyys.
- Magnitudes in the reasonableness checks are correct: the L1-01 radius is about 1,3 cm, L1-02 for a proton is about 14 m, v/c is stated where it matters.
- Scope: everything is inside FY7 with FY6 prerequisites. The cyclotron is used only as an application of r = mv/(qB).
