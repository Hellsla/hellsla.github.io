VERDICT: FAIL
CONTENT-HASH: f4d4beecdc2e560f

## Blocking
- [Major] inquiry.json solutions: a comma or full stop left at the start of the text after a display block ("$$, saadaan…") — a sentence punctuation mark detached from its sentence reads as an error and looks broken on a phone (lone "." or "," rows) — keep the sentence's punctuation out of the break: end the sentence before the block ("…massa on:" then the block) and start the next sentence with a capital after it, or put the closing "\," . or "," inside the aligned block's last row; never leave a paragraph starting with "." or ",".

## Polish
- [Minor] Display blocks that stay in running text use \tfrac, so the fractions in the aligned rows are small and hard to read at 390 px — use \dfrac in these lifted blocks.

## Checked
batch delta review: opened the 390 px theory/example captures where the lifted formulas appear (fy8-1 selita-3/4, fy8-2 example-1, fy8-5 example-2, fy8-10 selita-1/2/4); the aligned rows themselves fit without clipping, equals signs aligned; the stranded punctuation was confirmed in the rendered captures and in the sources of this lesson.
