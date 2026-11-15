VERDICT: PASS
CONTENT-HASH: 601522414dcda47b

## Blocking

## Polish
- exercises.json:223, 227–228; solutions.md:170 (L2-07): two wrong options still say "mittausvirhettä" and "virhe jakautuu", and their feedback and the model answer echo "virhe ei jakaudu". Wrong options may stay wrong on purpose, so this is allowed. For full consistency, the feedback could say "epävarmuus ei jakaudu mihinkään".
- solutions.md:78 (L2-03): "ero johtuu mittausepävarmuudesta" should say *mittausvirheestä*, or "mahtuu mittausepävarmuuden rajoihin".
- exercises.json:300 (L2-10, figure spectrum-q): at 250 lines/mm the second-order spectrum would start at about $20\,\text{cm}$, inside the drawn screen. The figure shows only the first order. A note in the task would avoid confusion. This figure is teacher-approved.
- solutions.md:212 (L3-05): "$x = \dfrac{2x}{2}$" reads like an identity. Say it in words: the maximum's distance from the hole is half of $2x$.
- solutions.md:154 (L2-05): the reason for three significant figures should say "kuten useimmat $x_k$ ja $L$", because $x_1 = 6{,}3\,\text{cm}$ has only two.

## Checked
- Round 2 diff (HEAD~1): in fy7-13-L2-07 the task text, answer, correct option, the feedback of the "varjostin lähemmäs" option and the solution now say "lukeman epävarmuus" and "suhteellinen epävarmuus". This matches the lesson's "epävarmuus $\Delta x$". The round 1 blocking item is resolved.
- No number, answer, option order or correct flag changed in the diff. Exactly one option is still correct, and the physics of every option's feedback is unchanged and right.
- From round 1 (unchanged content): I recomputed all 21 numeric answers with my own formulas, and each one agrees with exercises.json and answers.py within 0.2 %.
- L2-05: $\lambda = 634\,\text{nm}$ from the slope through the origin, a plausible value for a red laser. L3-04: the table follows the ideal pattern with a $5{,}0\,\text{mm}$ period, and $6{,}3 \cdot 10^2\,\text{nm}$ lies inside the tolerance. L3-05: mean $d = 0{,}7374\,\mu\text{m}$, the second-order sine is $1{,}44$, the deviation is $-0{,}36\,\%$, and the separator is clear.
- setup-q and spectrum-q are to scale, and their descriptions match the drawings without giving the answer away.
- The content hash was `601522414dcda47b` at the start and at the end of this round.
