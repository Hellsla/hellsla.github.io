VERDICT: PASS
CONTENT-HASH: 70401639c33a7a24
SCOPE: delta added-exercise from a1a0baded87547f2 base 8f23aa7ae3bd

## Blocking
(none)

## Polish
(none)

## Checked
- Delta: only L1-10 and L2-08 judged; the rest unchanged per `reviews.py added_exercises`.
- L1-10: parallel-plate capacitor C = ε0 εr A : d with polyethylene εr = 2.3 (MAFY); recomputed 5.091 nF = answers.py; conversions cm² → m² and mm → m right; 5.1 nF inside 5 %; table editions with εr 2.25–2.4 give 4.98–5.31 nF, all inside the tolerance. Air comparison (2.2 nF) recomputes.
- L1-10 principle: capacitance depends only on construction; the dielectric multiplies C by εr — consistent with the glossary definition.
- L2-08: figure ex-qu2 (figures.py) is a line from the origin to (120 µC; 8 V) on 20 µC / 1 V gridlines, the end point on gridlines; nothing gives C or W away.
- L2-08 recomputed: C = Q : U = 15 µF; W = ½CU² = ½ · 15 µF · (7.0 V)² = 367.5 µJ = answers.py; 370 µJ is 0.7 % off, inside 2 %.
- L2-08 reasoning: constant Q/U so any point of the line gives C (correct); check via ½QU with Q = 105 µC gives the same, and W < QU as it should.
- Both solutions complete: given/asked, principle with reason, symbolic formulas before numbers, conversions, rounding reasons, reasonableness checks.
- Scope: capacitor and its energy, no connections or exponentials (scope notes respected).
