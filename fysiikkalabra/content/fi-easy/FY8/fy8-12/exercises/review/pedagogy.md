VERDICT: FAIL
CONTENT-HASH: 6dde98f836adf9f7

## Blocking

- exercises.json fy8-12-L3-07 (and its solutions.md section) — the permitted ratio 1/20 gives I0:I = 20 and the factor ln 20/ln 2 = 4,3219, exactly the worked example's (5,0 % = 1/20, same ln 20 substitution). Only d1/2 comes from the graph, so the calculation repeats the example ("none repeats the worked example") — change the limit to a ratio the example does not use, e.g. 1/50 (d = 12 mm * ln 50/ln 2 = 67,7 mm, answer 68 with two figures rounded up), and update answers.py, the solution's sanity check (5 and 6 half-value thicknesses: 1/32 and 1/64) and the "Riittääkö 48 mm" conclusion (R(48 mm) = 50 pulses/min is then still above the limit 16).

## Polish

- L2-09 and L3-07 use the same figure and the same read-d1/2 step; with the fix above the L3 task still adds extrapolation beyond the graph and a safety decision, so the difference in level is real. Optional: name a second material/graph for L3 for variety.
- L2-09 solution: answer 140 and 141,4 both accepted; consistent with 2 % tolerance, fine.

## Checked

- L2-09 is level 2: graph reading plus one law substitution with a non-integer exponent (2,5); not the worked example's unknown.
- L2-09 solution has all seven parts, reads the graph with a check point (24 mm, 200), and the sanity check brackets 140 between 200 and 100.
- L3-07 asks to compare the graph's end (48 mm, 50 pulses/min) with the limit, a reasoning step not in other tasks; rounding up for an "at most" limit follows the house rule.
- Situation first, question last; figure description gives the data (800 at 0, to 48 mm) without d1/2 or answer.
- Answers 141,4 and 52 are right (800*2^-2,5; 12*4,3219 = 51,86), tolerance 2 % fits.
- Kind mix (graph, data, reasoning, model) adds to the set's variety; wording and Finnish/English/easy-language versions consistent.
- Method: delta, added exercises only; hash unchanged at start and end.
