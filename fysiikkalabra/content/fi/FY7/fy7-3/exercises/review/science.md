VERDICT: PASS
CONTENT-HASH: 624f7552329ed5be

## Blocking
- (none)

## Polish
- (none)

## Checked
- Recomputed all 12 answers in one script with my own formulas, all matching answers.py: 80 µT, 3,016 mT, 10 µT, 0,100 mT, 1,005 mT, 3,979 A, 8,571 cm, 2,500 mT, 80 µT, 2,021 A, 15,0 km and 4,0 cm. L3-03 was found by root search, not by the closed form.
- Round-2 item fixed: L1-03 no longer claims that the compass turns under an AC line.
- answers.py implements the physics stated in the tasks: long straight wire, long coil, N = L/(πd), fields added with signs, tan α = B_j/B_h.
- L2-03: l/d = 5 and the centre factor is 0,981, so "hieman pienempi" is right. L3-02: turn density 2984 per metre, centre factor 0,848 (≈ 85 %), 30 000 × Earth's field, so more wire is needed.
- L2-04: opposite currents add at the midpoint. L3-03: parallel currents cancel between the wires, and the zero point lies nearer the weaker current.
- L3-01: the field below an N–S wire is horizontal and E–W. The angle is under 45°, so B_j < B_h is consistent.
- Every solution is complete: symbolic first, conversions right, significant figures from the limiting datum, and a real reasonableness check. Notation matches the lesson. Scope is FY7 only.
