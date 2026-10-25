VERDICT: PASS
CONTENT-HASH: ac207ba43c7421e7

## Blocking
(none)

## Polish
1. lesson.md:14 — "yläreunassa nolla" holds only if water reaches the crest. — "vedenpinnan tasolla nolla".
2. lesson.md:27 — ρgh equals the overpressure only when p₀ is air pressure, yet p₀ is "yleensä" air pressure. — Add "kun pinnalla on ilmanpaine".

## Checked
- Round 3: only sim.js changed (git diff 23c90fd). Lint clean; hash unchanged from start to end of review.
- sim.js:22-56 is untouched: P0 = 101 kPa, G = 9,81, slope = ρ·G/1000, pOver = slope·h, pTotal = P0 + pOver, ratio = pTotal/P0, base = 0 in over-only mode else P0. The readout text and simState are identical to round 2, so they still match lesson.md (p = p₀ + ρgh, g = 9,81 m/s²).
- The blue line is still drawn from (0, base) to (20 m, base + slope·20). The dot is at (h, base + pOver). X() and Y() are unchanged in form; CH.y0 335 (was 345) only shifts the chart up 10 px, so the scale stays linear and Y(P0) lands correctly. The over-only line passes through the origin.
- The new code (say, meas, segHit, candidate boxes, simDebug) only places and draws text. The reading label prints fi(base + pOver, 0) kPa, the same value as before. The "h" bracket label now appears only for h ≥ 2 m, which is cosmetic.
- Recomputed readout values (Python below): water 12 m gives 117,7 kPa, p = 218,7 kPa, 2,17 × p₀, matching the lesson example. Water 10 m gives 98,1 kPa ≈ p₀; ρ = 1300 at 20 m gives 255,1 kPa. All values are realistic.
- Round 2 findings still hold: the derivation, dam paragraph, example, answers.py (every line), solutions.md and exit ticket are correct. The lesson files are unchanged since round 2.
- I could not run test_sims.py here (Playwright browsers are not installed); the physics review does not depend on it.

## Python output
```
rho h  pOver  p     ratio
720 10 70.6 171.6 1.7
1000 0 0.0 101.0 1.0
1000 10 98.1 199.1 1.97
1000 12 117.7 218.7 2.17
1000 20 196.2 297.2 2.94
1025 20 201.1 302.1 2.99
1240 20 243.3 344.3 3.41
1300 20 255.1 356.1 3.53
```
