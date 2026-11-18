VERDICT: PASS
CONTENT-HASH: 876c08f6ee47b4ec
SCOPE: delta: round 2, the fixes of round 1 in fy9-moderni-s8 and -s9 (changed passages, 360 px layout); older tasks untouched

Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- [Minor] s8 rubric c, calculation row: the display is still followed by ", joka on yli $1{,}0\,\text{mSv}$"; move the clause into its own sentence (fi-easy already does).
- [Minor] s8 and s9 figures (fy8-13/vaimennus, fy8-16/hubble-t): small tick numbers and pale grid at phone width; shared catalogue figures, for a later figure-fix.
- [Minor] s8 rubric a: $\ln(80 : 5{,}0)$-type unitless rows in the model solution; harmless.

## Checked
- Rebuilt captures for hash 876c08f6ee47b4ec (screenshot.py, current stamp). Opened fi stage-exercises-390-64 (s8 task parts, links, start of model solution), -66 (s8 b: aligned substitution rows, answer box, järkevyys) and -75 (s9 a and b: fractions, answer box, units).
- Read the changed s8 and s9 text in fi tasks.json: situation first, question last, no revealed solution structure; results rounded to the data's precision (6,6 µSv/h, 24 cm, 72, 117 -> 120 Mpc, 1,4 · 10^10 a); calculation chains as aligned rows; unit fields language-neutral (1/cm, µSv/h, km/s/Mpc, a).
- check_layout.py fy9-moderni --width 360: OK; the only known clipped formulas on the page are older ones (fy9-moderni rows with 1,342 · 10^20 and 6,626 · 10^-34), none in s8 or s9.
- No separate 360 px captures exist (captures are 390 px); 360 taken from check_layout.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
