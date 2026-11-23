VERDICT: FAIL
CONTENT-HASH: 2bec31ef376ba1fb
SCOPE: delta 8g Formula-step rewrite (en), round 1

## Blocking
- content/en/FY1/fy1-8/exercises/solutions.md:105 and :225 (fy1-8-L3-02, L3-05) — A: the new row r = \Delta T/\Delta t = (T_start - T_end)/(t_end - t_start) is false with the course's \Delta T = T_end - T_start (fy1-4 cooling slopes are negative); the rate of fall is the negative of the slope — write r = -\Delta T/\Delta t (or name \Delta T the fall, T_start - T_end) before the second row. The Finnish Kaava step (fi solutions.md:105, :187) has the same row and needs the same fix.

## Polish
- none

## Checked
- Delta (work queue 8g): only the Formula steps of solutions.md changed (aligned blocks from the basic equation); every other changed line in the diff is a paragraph split or spacing, no number, sign or unit changed.
- Each new Formula block checked line by line: every equality and rearrangement is algebraically valid and leads to the formula the unchanged Substitution uses.
- Script comparison with the Finnish Kaava steps (which passed science review): same number of aligned rows, inequalities and numerals in every solution.
- answers.py and exercises.json values not in the diff; answers, units and tolerances unchanged from the passed version.
- Hash recomputed at start and end with --exercises --lang en: unchanged.
- s = vt, half-range, epsilon <= epsilon_max gives t >= Delta t/epsilon_max, repetitions n = (t_tot - t_prep)/(N t_rep) valid.
