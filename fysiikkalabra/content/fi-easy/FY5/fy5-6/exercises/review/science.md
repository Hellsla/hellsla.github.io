VERDICT: PASS
CONTENT-HASH: 7d2542dd563a3195

## Blocking

## Polish

## Checked
- Hash same at start and end (c85d130d8268574e; after the paragraph split 7d2542dd563a3195). Delta, round 1 (fi-easy): queue 18 rounding reasons (L2-01 9,57·10³ km, 1,13 m/s, Jupiter mass, satellite B, 3,87/15,5 kN, exoplanet star, L1-11), L1-11 marked "Syventävä tehtävä", new data task L2-09 (Kepler III, NASA Fact Sheet).
- Script comparison with content/fi/FY5/fy5-6: same ids, answer, unit, tolerance, level, kind; every number in each task text and solution identical in fi and fi-easy (no step or justification dropped).
- L2-09 data equal to sources.md (Mercury–Jupiter a and T); Moon column excluded correctly; the task marked Syventävä per the teacher's decision of 16.11, and the law is derived from the chapter's circular-orbit model.
- Recomputed: T_Mars = 365,2 · (228,0/149,6)^1,5 = 687,12 d -> 687,1 (tol 2 %); with 227,9: 686,67 d; T²/a³ = 0,0399, 0,0399, 0,0398, 0,0398, 0,0398, spread 0,35 % (< 0,4 %); Jupiter −0,2 %, Uranus −0,33 %, Saturn −1,26 %, Neptune −2,46 % vs Earth, as stated; a³ ratio 2432 (> 2000).
- Slope check: k = 0,0398 -> 2,97·10⁻¹⁹ s²/m³, M = 4π²/(γk) = 1,99·10³⁰ kg. Points (100; 4,0), (400; 15,9) lie on the line.
- Simplified wording right: semi-major axis = half the longest diameter of the ellipse; Kepler III holds for ellipses with a, so eccentricity is correctly not the cause of the difference.
- Exoplanet: mean of c and e alone gives 1,591·10³⁰ kg -> 1,59, as the new rounding reason says; Jupiter ratios differ in the 4th digit (3,2056–3,2110).
- L1-11: MAFY values have four figures; three-figure answer 1,45 m/s² justified. answers.py lines for L2-09 compute the right physics. No SCOPE line in the packet's instructions, so none written.
- Follow-up delta (git diff HEAD~1): L3-04 Vastaus split from one paragraph into five; the text is word for word identical once whitespace is normalised, with no number or formula changed.
