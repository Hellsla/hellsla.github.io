VERDICT: FAIL
CONTENT-HASH: 190c2fdd98b183b0

## Blocking
- exercises/solutions.md:29 (fy7-3-L1-03, Järkevyys) — A: "voimajohdon alla kompassi kääntyy vain vähän". The line carries alternating current; the task itself says "hetkellisesti" 800 A. A 50 Hz field reverses far too quickly for the needle to follow, and its average is zero, so the compass does not turn at all. — Fix: drop the compass clause and keep the comparison ("noin viidesosa Maan magneettikentästä"), or say that the field of the alternating current changes direction 100 times a second, so the compass does not react.

## Polish
- (none)

## Checked
- Recomputed all 12 answers in one script with my own formulas, all matching answers.py: 80 µT, 3,016 mT, 10 µT, 0,100 mT, 1,005 mT, 3,979 A, 8,571 cm, 2,500 mT, 80 µT, 2,021 A, 15,0 km, 4,0 cm.
- answers.py implements the stated physics: long straight wire, long coil, N = L/(πd), fields added with signs, tan α = B_j/B_h.
- Round-1 items fixed. L1-04 now says "useimmissa kohdissa ja varsinkin kauempana". L3-02 gives the direction of the finite-coil error (about 85 %; my result 0,848), so more wire is needed.
- L2-03: l/d = 5, centre factor 0,981, and "hieman pienempi" is right. L3-02 checks: turn density 2984 per metre, 30 000 × Earth's field.
- L2-04: opposite currents add at the midpoint. L3-03: parallel currents cancel between the wires, and the zero point lies nearer the weaker current.
- L3-01: the field below an N–S wire is horizontal and E–W; the angle is under 45°, so B_j < B_h is consistent. B_h = 14 µT is plausible for Finland.
- Every solution is complete: symbolic first, conversions, significant figures from the limiting datum, a real reasonableness check. Scope: FY7 central contents only.
