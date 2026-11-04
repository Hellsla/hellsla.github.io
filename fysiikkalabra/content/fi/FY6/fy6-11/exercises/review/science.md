VERDICT: PASS
CONTENT-HASH: b47fd13b952cba5f
Round 2: full review of the exercise set after the round-1 fixes (commit e6301a0ac).

## Blocking

## Polish
- docs/exercise-bank/FY6.md fy6-11 Taso 2 — the plan's graph task (droplet deflection, figure) became the error-analysis task L2-06, and no new task has a graph. Update the plan line.

## Checked
- Hash b47fd13b952cba5f at start and end. Diff since 048b5f229 read in full.
- Round-1 Blocking (L3-04, A) fixed: Periaate now says all charges are integer multiples of one step and the smallest is taken as one step if the ratios to it are integers; b) states that the ratios 2,0; 3,0; 4,0; 3,0 are integers, so drop 3 has n = 1, supported by c. The inference is now valid.
- L3-04 recomputed: q = 3,20 / 4,84 / 1,59 / 6,38 / 4,83 ·10⁻¹⁹ C, n = 2, 3, 1, 4, 3, e = 1,60·10⁻¹⁹ C; "alle 1 %, mittaustarkkuuden rajoissa" and "raskaammat ja vähemmän varautuneet" (d) right.
- L2-07 new datum 58,0 µN at x = 8 cm: E = 2,90·10⁴ V/m, deviations 0,7 / 1,2 / 2,0 / 3,7 / 45,2 %; points 0–6 cm under 3 %; mean 2,98·10⁴ V/m (answer 29 812,5), 0,6 % from U : d. Realistic for wide plates; solution and answers.py updated consistently.
- L2-05: answer line now first in Vastaus; 4,0·10² V unchanged.
- L1-06, L1-07 after reordering: exactly one correct option (index 3 and 0), `answer` equals it, feedback right.
- answers.py re-run: all 18 numeric answers agree with exercises.json.
- Scope (uniform field, E = U : d, F = qE), levels and notation unchanged; no duplicates.
