VERDICT: PASS
CONTENT-HASH: 7dc28f251828e30e
Round: 3
Mode: delta

## Blocking
(none)

## Fixed
- No text changes needed.

## Polish
- none

## Checked
- Scripted comparison against the reviewed Finnish: all ids present; answers, units (kertaa), tolerances, kind, choices and correct flags, data rows and column headers identical.
- New tasks L1-06, L1-08, L2-05..07, L3-04, L3-05: every number in texts, tables and solutions equals the Finnish (1,5 K, 1,7 kertaa, 40 s, 0,6 K, 145 C, 797 ja 696 kPa, 13,6 %, 16 %, 37,1 ja 37,0 C); decimal comma in LaTeX as {,}.
- Physics in the choice feedback and solutions is the same as in the Finnish (closed system = no matter crosses the boundary; total pressure, not gauge pressure, is proportional to kelvin temperature).
- Solutions keep the Finnish structure and formulas step for step.
- check_i18n.py fi-easy: 0 errors.

## Checked in round 2
- Delta (HEAD): split aligned rows in solutions.md re-derived against the previous rows. Each "... \\ &= result" is the old row cut at its last "="; all numbers, units, symbols and values identical (mechanical check: old and new rows equal once \\, & and = are removed), and the results still follow from the inputs. No physics or answer changed.

## Checked in round 3
- Delta (HEAD~3..HEAD, solutions.md display maths only): Sanity pass of the change: the last row was moved out of the aligned block into its own display formula, theta_forehead,corr = 37,6 - 0,6 = 37,0 degC; arithmetic correct and identical to the earlier text, and it matches the Vastaus paragraph below. The aligned block above still closes properly. Rest of the set not re-derived; previous PASS stands, no number or wording changed.
