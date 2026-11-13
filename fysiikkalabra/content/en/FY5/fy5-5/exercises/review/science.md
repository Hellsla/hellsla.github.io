VERDICT: PASS
CONTENT-HASH: fc3b190ea3328bed
SCOPE: delta added-exercise from 2dfa5cdb22af192d base 81db4a6fd727

## Blocking
(none)

## Polish
- solutions.md fy5-5-L1-09 — the reasonableness check uses 9.81 m/s² for the Earth while the figure shows 9.80 m/s²; harmless (ratio 0.38 either way) — optionally use the figure's value.

## Checked
- fy5-5-L1-09: F = mg = 85 kg · 3.71 m/s² = 315 N → 3.2·10² N (two significant figures from 85 kg); answer 320 within 2 % of 315.
- fy5-5-L2-09 (reworked, probe at h = R): r = R + h = 2R measured from the centre, g = g0 (R/r)² = 24.8/4 = 6.20 m/s², F = 850 kg · 6.20 m/s² = 5.27 kN. Recomputed independently via M = g0R²/γ and F = γMm/r²: same 5.27 kN; answers.py agrees.
- The remark that 24.8 m/s² belongs to the equatorial radius is right; inverse-square law and its distance-from-centre condition stated.
- Figure fy5-5/planeetat: English labels Moon, Mars, Earth, Jupiter and the values 3.71 and 24.8 m/s² match what the solutions quote.
- Compared with the Finnish set by script: every number, answer, unit, tolerance and figure id identical.
- Hash unchanged at start and end.
