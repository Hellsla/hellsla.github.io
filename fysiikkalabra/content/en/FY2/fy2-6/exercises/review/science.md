VERDICT: PASS
CONTENT-HASH: 220846710e02220d
Mode: full (translation review of the new task fy2-6-L1-09)
Round: 1

## Blocking
(none)

## Polish
(none)

## Checked
fy2-6-L1-09 (en) compared with the reviewed Finnish in exercises.json and solutions.md: same given data (3.0 MW, 33 %, 5000 kWh, 8760 h), same four choices, same correct flag (about 2000), same tolerance and feedback physics.
Recomputed: P_avg = 0.33 * 3.0 MW = 0.99 MW = 990 kW; E = 990 kW * 8760 h = 8.67e6 kWh; / 5000 = 1734, so 2000. Distractors: 8.7e3 MWh / 5000 = 1.7 (about 2, unit slip); 3.3 % gives 173 (about 200); rated power gives 3000 kW * 8760 / 5000 = 5256 (about 5300, shown as 5000). All feedback numbers right.
Numbers and LaTeX identical to Finnish apart from the decimal separator (point). No Finnish left in en. check_i18n.py: nothing for fy2-6; build.py fy2-6 succeeds.
Hash unchanged at the end (no file edited by this review).
