VERDICT: PASS
CONTENT-HASH: bcba5280a01c2a67

## Blocking

## Polish
- solutions.md (L3-06 Reasonableness) — "A lighter 20 g magnet would fall more slowly" with the same k holds only for a magnet of the same strength and size (same remark as on fi) — add "equally strong".
- solutions.md (L2-03 Reasonableness) — "A heavier magnet would fall faster" has the same unstated condition (same k) — add "with the same k" or "equally strong".
- solutions.md (L2-09 Answer) — "100 mW, two significant figures" is ambiguous as written — write $1.0 \cdot 10^2\,\text{mW}$ or $0.10\,\text{W}$.

## Checked
- Hash identical at start and end. The packet's lesson brief was empty; notation judged against the fi brief (e = N ΔΦ/Δt, Q = mgh − ½mv², P = Fv), and the exercises use it.
- All 16 numeric answers recomputed independently in one script (F = mg, ΔE_k, P = mgv, e = NΔΦ/Δt, I = e/R, v_t = mg/k, P = Fv with 250 km/h = 69.44 m/s, means, ΔT = nQ₁/(cm), F = (Bl)²v/R, a = g − kv/m, P = kd²). Each matches answers.py and lies inside its tolerance.
- L3-04 data agrees with the stated model: with τ = m/k = 0.075 s, v(t) = v_t(1 − e^(−t/τ)) gives 0.36, 0.54, 0.64, 0.69, 0.73 m/s. The claim that the central difference is greater than the tangent slope (2.8 vs 2.65 m/s²) is correct (v‴ > 0).
- L3-05: P ∝ d² at fixed volume and field in the thin-sheet limit is right; ratios within about 3 % of the mean, and 2.86² = 8.2. The "same resistance" step in the reasoning is a fair simplification at this level.
- L2-05: thick 7.32 s → 0.137 m/s, F/v 1.44 versus 0.78 N·s/m (thin, 4.0 s); conclusion and energy reasoning are right.
- L1-02, L1-06, L2-06, L2-08: pole and direction from Lenz are correct each time. L1-06 now reads "tries to keep the flux unchanged" in the answer, options, feedback and solution. Exactly one correct option (and one correct reason in L2-08), and every distractor's feedback is right.
- L3-03 energy balance F·v = RI² = 1.8 W is right. L3-01 states that no heat is transferred to the surroundings.
- Figure brake-task: line F = 1.6 N·s/m · v. Readings 0.40 N at 0.25 m/s and 0.32 N at 0.20 m/s are on the line, and the weight 0.44 N falls inside the drawn range. The figure gives away neither answer.
- Energy wording follows the guardrails ("converted into internal energy", never "into heat"). No self-induction, no diamagnetism, inside the FY7 scope.
- Solutions are complete: symbolic first, conversions shown, rounding justified.
