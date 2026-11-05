VERDICT: PASS
CONTENT-HASH: 3e63fa3729828f29
Mode: full
Round: 2

## Blocking
(none)

## Polish
- content/fi/FY2/fy2-2/exercises/exercises.json (L1-09 text) — "Pellettikattilan lämpöenergia on 1 MJ" gives a boiler a stored "lämpöenergia" value, which has no clear meaning (heat is energy in transfer). Write e.g. "Pellettikattila luovuttaa veteen lämpönä 1 MJ energiaa." Also 1 MJ is only about a minute of a home boiler's output, which is fine for a conversion task.
- solutions.md L1-09 Muunnokset — "1 000 000 : 1000 kJ" mixes a pure number with the unit; "1 000 000 J = (1 000 000 : 1000) kJ" is clearer.

## Checked
- Hash 3e63fa3729828f29 at start and end of this round; the diff from 18b454cd1 to HEAD touches only L1-09 (exercises.json, solutions.md).
- Round-1 blocking item fixed: the task now uses only J, kJ, MJ, GJ, which the brief's lesson teaches. No W, kWh or power is left.
- Recomputed each option: 1000 J = 0,001 MJ; 1 000 000 kJ = 1000 MJ = 1 GJ; 1000 kJ = 1 MJ; 1000 GJ = 10^6 MJ.
- Exactly one option is correct (1000 kJ), and it matches answer and the correct flag. Each distractor's feedback names its actual value correctly (1 kJ, 1 GJ, 10^6 MJ).
- The solution states the prefix rule before substituting, the Vastaus line names every option's value, and the check 1000 kJ · 1000 = 10^6 J holds.
- No number answer, so no answers.py line is needed; the other tasks are unchanged from the PASS set.
