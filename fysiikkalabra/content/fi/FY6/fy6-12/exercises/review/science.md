VERDICT: PASS
CONTENT-HASH: 4703625fe3ccea47
Round: 2, science, mode full. Scope: the round-1 fixes to fy6-12-L2-08 (commit 57a66480d). The rest of the set is unchanged since round 1. Checked from text only, no renders.

## Blocking

## Polish

## Checked
- The fixes change only form: the stem is split into two paragraphs, the correct option's feedback reads "Laskettaessa tulee U = V_B − V_A = 90 V", and the solution's chains are split into one per row. No number, model or truth value changed.
- Physics re-verified: rows 1, 2 and 4 are right, and row 3 is the only wrong row. I recomputed 90 eV = 1,442e-17 J ≈ 1,4e-17 J and 120 eV = 1,92e-17 J.
- The rounding sentence now reads "kahden merkitsevän numeron tarkkuudella", and its reason still holds.
- All numeric answers of the set were recomputed from answers.py in one python call: no mismatch.
- The distractors still carry the lesson's warned mistakes: potential vs. potential difference and potential energy, and the direction for a negative charge.
- No option can be picked out by its form.
- Inline chains (text estimate): every row is now under about 200 px.
