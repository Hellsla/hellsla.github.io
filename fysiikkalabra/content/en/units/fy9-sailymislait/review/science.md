VERDICT: PASS
CONTENT-HASH: a5ce41b2c877ab0d

Science review, round 3, of the en translation of fy9-sailymislait, 2026-11-04.

Round 2 found no Blocking science issue. Since round 2, scripts/figlib.py translate() also translates \textbf{} contents, and the en figures were redrawn. The only change in this unit's content is the three concept-map branch headings (energy, momentum, applications). No number, answer, tolerance, formula or correct flag changed. All figure numbers still use a decimal point (1.6 m/s, 0.80 m/s, 41 kJ, 20 kJ, 51 200 kg·m/s, k ≈ 0.080 s²/m, t_r ≈ 0.86 s). check_i18n.py: en 0 errors. units.py check: 77 units ok. practice.py check: en/units/fy9-sailymislait OK, 6 tasks, 95 points.

## Blocking
None.

## Polish
1. Not changed: stopping distance is written $s_\text{p}$ (unit.md, sovella/solutions.md, s3 graph labels), while English fy4-11 uses $s_\text{stop}$. A figures.json key "p" would also rename $E_\text{p}$, so this needs a change in figures.py. Left as it is so text and graphs agree.
2. Not changed: the ratio colon ($|\Delta p| : \Delta t$, $\mu = a : g$) is a project-wide typography question.
