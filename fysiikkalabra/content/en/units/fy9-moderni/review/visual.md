VERDICT: PASS
CONTENT-HASH: f5355edae2761e52
SCOPE: delta: round 2, the fixes of round 1 in fy9-moderni-s8 and -s9 (changed passages, 360 px layout); older tasks untouched

Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- [Minor] s8 rubric c: the display is still followed by ", which is more than $1.0\,\text{mSv}$"; make it its own sentence.
- [Minor] s9 figure alt text may still say "speed" where the task says "velocity"; align in a later figure-fix.
- [Minor] s8 and s9 figures: small ticks and faint grid on a phone; shared catalogue figures.

## Checked
- Rebuilt captures for hash f5355edae2761e52 (screenshot.py --lang en, current). Layout confirmed through the same shared components as fi (fi captures 64, 66, 75 opened: parts, aligned rows, answer boxes intact); the English text is cut the same way as the Finnish.
- Read the English s8 and s9 text and every rubric row: same numbers as fi ($18\,\text{cm}$, $1.5\,\text{h}$, $220$, $1.0\,\text{mSv}$, $250\,\text{Mpc}$, $8400\,\text{km/s}$), decimal point, LaTeX units, results at the data's precision (6.6, 24 cm, 72, 120 Mpc, 1.4 · 10^10 a), question last, no revealed structure, units language-neutral.
- check_layout.py --width 360 for preview/en/fy9-moderni: OK; known clipped formulas are older rows, none in s8/s9.

## Scores
illustrations 4 · typography 4 · Finnish (English language) 5 · accessibility 4
