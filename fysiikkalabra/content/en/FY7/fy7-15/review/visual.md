VERDICT: FAIL
CONTENT-HASH: 9ace94216814e81f

## Blocking
- [Major] A new "Stop and think" answer holds a formula chain that does not fit 360 px: the Malus's-law chain $I = I_0 \cos^2\theta = \ldots = 50\,\text{W/m}^2$ (third block), about 344 px too wide. `check_layout.py fy7-15 --width 360` fails (en, fi and fi-easy: "clipped or scrolling", at `details.stop-think-a > span.katex.kx-wide`). The answer is a plain `<p>` in `<details class="stop-think-a">`, so `mathlayout.py` does not break the chain into aligned rows as it does in the rest of the page. Fix in the shared component (stopthink.py / mathlayout.py or site.css), not per lesson.

## Polish
- Question and answer blocks render cleanly at 390 px (label, question, "Answer" summary), no red KaTeX source.

## Checked
- batch delta review: opened the Theory capture with the new block, read all three blocks in the diff, rebuilt preview checked (3 blocks, no katex-error), ran check_layout at 360 px; hash unchanged at start and end.
