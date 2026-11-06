VERDICT: PASS
CONTENT-HASH: 5701e43715c62ef4

## Blocking

## Polish
- fy5-8/exercises/exercises.json L2-08 choices — Carried over from round 1: no distractor carries a mistake the lesson's method section warns about, such as reading the slope from two neighbouring raw points or using total length instead of extension (bank plan). This is optional. The current distractors are physically sound.

## Checked
- The round-1 Blocking item is fixed (commit 4ff432a8f). All four options now have the form "X, koska Y" and are of similar length. Three of them mention the uncertainty: options 1 and 2 wrongly, option 3 correctly. The right option can no longer be picked by form.
- Option 2 (exercises.json:267) is now the warned unit mismatch: a ratio difference in N/m compared with the force uncertainty 0,05 N. Its feedback names the mismatch and gives the right comparison (±1,3 N/m).
- Option 1 compares the growth of the force with 0,05 N, which is a true statement used for a wrong conclusion. Its feedback says why this tells nothing about k.
- The answer string equals the text of the correct option. The correct option's feedback gives no extra reason.
- I recomputed every row again: the ratios are 24,5 / 25,5 / 24,5 / 25,0 / 25,1 N/m with uncertainties ±2,5 / 1,25 / 0,83 / 0,63 / 0,50 N/m, and 25 N/m lies inside every interval.
- The solution now writes Δ(F_v/x), and its closing paragraph matches the new options. The guardrails hold: a physical reason for the line through the origin, the slope read from the fitted line, and "within the uncertainty" not taken as proof the values are equal.
- The aligned chain in the solution is two lines. From the text it fits 300 px. I did not render it.
- answers.py ran again: all numeric answers agree with exercises.json within tolerance. The data table is unchanged.
- The hash was the same at the start and at the end of round 2.
