VERDICT: PASS
CONTENT-HASH: 5988de04ca4b7b84

## Blocking

## Polish
- exercises/solutions.md:29 (L1-03) — "2 eV … on oranssin valon fotonin energia": 2,0 eV ≈ 620 nm lies on the orange–red boundary; "oranssinpunaisen" is safer.

## Checked
- All 12 answers recomputed independently: L1 3,734e-19 J, 1,623e-24 J, 1,998 eV, 4,882 eV, 0,69 eV; L2 579,4 nm, 1,636e16 1/s, 1,906 eV, 2,283 eV; L3 6,665e5 m/s, 422,8 vrk, 5,548e14 Hz: all match exercises.json within the tolerance.
- answers.py uses the right physics (hc/λ, hf − W, λ0 = hc/W, ½mv², P = N·hc/λ, W = IAt).
- L3-01: the ½mv² condition (v ≈ 0,2 % of c) is checked in the solution ✓.
- L3-02: the wave-model assumptions are stated in the task, and the result is set against the observation ✓.
- L3-03: slope 4,13·10^-15 eV/Hz ≈ h, intercept by the line; 2 sf justified ✓.
- Every solution: symbolic first, conversions shown by substitution, rounding tied to the limiting datum, a real reasonableness check ✓.
- Work functions (Na 2,28, Mg 3,68, Zn 4,31, Cs 2,14 eV) are typical table values that match the lesson ✓.
- Scope within FY8 ✓.
