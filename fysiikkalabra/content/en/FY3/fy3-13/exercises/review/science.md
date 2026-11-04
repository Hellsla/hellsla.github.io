VERDICT: PASS
CONTENT-HASH: fcc0d449c338b7d3
Mode: full
Round: 1

## Blocking
(none)

## Fixed
- (none; no text edits were needed)

## Polish
- solutions.md L2-05 Substitution: "$250\,{}^\circ\text{C} : 5$" uses a colon for division (as in the Finnish source); a division sign would read more naturally in English, but formula parity with fi is kept. Same in L2-06 and L2-07 ("2.0 : 15", "104.0 kPa : 0.33").

## Checked
- Scripted comparison of exercises.json against fi: all 219 leaf strings and values checked; ids, answers, units, tolerances, correct flags, choice order, kind lists and table cells identical; every number in texts and feedback equals fi (decimal point in en JSON and LaTeX).
- solutions.md: the 20 sections match fi in every number (scripted); no formula changed.
- New tasks L1-06..08, L2-05..07, L3-04..05: answers recomputed from the data (77.4 K, -274, -302, -370, 10.7, -17.5 degC) and equal the Finnish answers.
- Terms follow the guardrails: absolute zero is the lowest energy, not "particles stop"; extrapolation is an estimate under a model assumption.
- Language: natural English, no Finnish left (grep for ä/ö clean); theta_av subscript is right.
- check_i18n.py en: 0 errors.
