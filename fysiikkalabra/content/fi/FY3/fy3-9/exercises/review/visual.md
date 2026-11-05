VERDICT: PASS
CONTENT-HASH: fb4c9e7694ba0259

## Blocking

## Polish
- [Minor] fy3-9-L2-08 figures at 390 px — SVG text scales to about 11 px (figure about 270 px wide inside the option card) — tick numbers and axis titles are readable but at the lower limit; widen the figures in choice cards if the layout allows.
- [Minor] fy3-9-L2-08 option order — the page shuffles the options, so the letters appear C, A, D, B — alphabetical or fixed order would read more naturally and match the solution's "A ja B".
- [Minor] fy3-9-L2-08 graphs A and B — same blue for all four lines; they are told apart by shape and grid only, which works (300 vs 200 kPa at 20 ml reads off the grid), no change required.
- Carried over: L2-05 and L3-04 Järkevyys formula/colon items from the previous report.

## Checked
- Rendered fy3-9 preview at 390 px (Playwright), L2-08 closed, with all four options' feedback open and the solution (Periaate, Mallivastaus, Kuvaajan lukeminen) open. Opened the images.
- All four figures pick-flat, pick-line, pick-rising, pick-boyle: same axes (V (ml) 0–45, p (kPa) 0–450), LaTeX axis titles and ticks, arrowheads, grid every 5 ml / 50 kPa, labels on 10/100 steps, no clipping. A (straight line, 400 to 100 kPa) and B (convex curve) clearly differ; line ranges 10–40 ml match the task. No overflow (scrollWidth 390).
- Solution fractions p_2, p_3 break into aligned rows, fit 390 px. Feedback texts in LaTeX with units. The new task is split into situation and question.
- Correct option not identifiable by form: feedbacks of similar length; distractors catch the warned mistakes (straight line, constant p, p proportional to V).
- From text only: the changed paragraph splits in other tasks (diff).

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 4
