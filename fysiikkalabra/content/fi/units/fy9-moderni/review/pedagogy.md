VERDICT: PASS
CONTENT-HASH: f86c668d8d52ca6b

Delta review (solution practice, 2026-11-12) of the version passed before.

s5 a now models a good graph answer: all 11 points, ln N against t shown as points, a fit line, slope from two far points on the line, T = 153 s, with the two-endpoint 151 s as the check. tasks.json answer 153 s, tol. 4 % agrees. Other symbol changes (H_v share, E0, b = -W/e, m_a, m_U) are correct and short. POLISH 1: the accepted range is 145-160 s in the rubric (units_precision), 145-157 s in solutions 'Hyvaksytaan myos' and 147-159 s from tolerance 4 %; use one range. POLISH 2: s5 a Vastaus 'Taustan vahentaminen muuttaa tulosta' is vague; give the numbers (e.g. 155 s -> 153 s) or drop.

Checked: diff since 761b6673, symbols defined, solved expression equals Sijoitus, answers.py output, tasks.json answer/criteria, cross-language number match.
