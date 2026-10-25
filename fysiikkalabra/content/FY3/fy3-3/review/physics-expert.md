VERDICT: PASS
CONTENT-HASH: 536cade809f2b051

Round 3 (final), physics-expert, lesson fy3-3. Hash re-run at the end: 536cade809f2b051 (unchanged).

## Findings
1. lesson.md, micro model (lines 8): correct. Smaller volume gives more frequent wall hits with the same per-collision push, so pressure increases; heating at fixed volume gives more frequent and harder collisions. No overclaim.
2. lesson.md, pressure definition (line 6): p = force per area, Pa, 1 kPa = 1000 Pa. Correct; deeper treatment deferred.
3. lesson.md, proportionality (line 10, summary line 73): p proportional to T (V, n constant) and mean kinetic energy proportional to T stated as facts, with the detailed study deferred to later gas courses. In scope for FY3 and not derived. E_k formula not used. OK.
4. lesson.md, kelvin: T = theta + 273,15, equal unit size, differences equal in K and degC, 0 K = -273,15 degC, "ei astetta" wording correct. OK.
5. lesson.md, worked example: the six data points lie on the line p = 100 + 0,37 theta within 0,6 kPa; k = 0,37 kPa/degC; theta0 = -100/0,37 = -270,27, shown as about -270 degC, near -273. The SVG coordinates are consistent with the data (x 1,25 px/degC, y 1,5 px/kPa, line end at -270 degC, y axis at about -300 degC, as the caption says). The caveat that real gases liquefy so the line is only a model is correct.
6. lesson.md, misconception: 293/283 = 1,0353, about 3,5 %. Correct. 0 degC is not the lowest temperature. Correct.
7. exercises.json: all answers recomputed in Python (python3 -I) from the problem text alone, with 273,15 and with 273. All lie within relative tolerance 0,02, also with students' sensible rounding (see output). L2-03 extrapolation to -50 degC gives 92,857 kPa, answer 93, OK. Significant figures match the data.
8. solutions.md: reasoning and arithmetic correct for all 12; the sanity-check texts are valid (L2-03 says the value is below 110 kPa and well above zero; L2-04 notes that a degC ratio is meaningless).
9. exit-ticket.json: correct. 283 to 293 K is about 3,5 %; -273 degC; absolute zero reasoning is fine at this level.
10. sim.js: 2D model with v = V_REF sqrt(T/300), so E_k is proportional to T. Wall momentum per time per wall length gives p proportional to N v^2/(2A), so p is proportional to T/V; reference normalisation (effective box) is consistent. Texts are correct: faster particles hit more often and harder, a smaller box means more frequent hits. Readout shows T in K and degC (T - 273,15) correctly. The note that the measured value fluctuates around the theory value is accurate.
11. Nit, no action required: "liike-energia pienimmillään 0 K:ssa" ignores zero-point energy, which is appropriate for upper-secondary level.

No physics, number, unit or scope errors found.

## Python output (python3 -I)
K0 273.15: L1-01 294.15, L1-02 76.85, L1-03 -195.75, L1-04 25, L1-05 -270.45, L2-01 59.85, L2-02 101.55, L2-03 92.857, L2-04 3.9955, L3-01 320.82, L3-02 127.05, L3-03 -126.575
K0 273: L1-01 294, L1-02 77, L1-03 -195.6, L1-04 25, L1-05 -270.3, L2-01 60, L2-02 101.55, L2-03 92.857, L2-04 4.0, L3-01 320.83, L3-02 127.0, L3-03 -126.5
Rounded variants: L2-02 k=0,33 gives 101,55; L2-03 k=0,29 gives 92,6; L3-01 with 288/308 K gives 320,83
Example: -100/0,37 = -270,27 degC; 293/283 = 1,0353
Hash: 536cade809f2b051
