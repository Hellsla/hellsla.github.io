VERDICT: PASS
CONTENT-HASH: af00c5738a515fa3

## Blocking
(none)

## Polish
1. [Minor] Figure `barrier`: "strong force" now sits right of the well wall, at $r \approx 4$–$9\ \text{fm}$, under the tunnelling arrow. There it reads as a label for the region where the electric force dominates. Fix: put it inside or below the green well (left of $r = 3\ \text{fm}$, under the axis), or add a short leader to the well.
2. Resolved after the shared `fx/reaction.js` update, rechecked at 360, 390 and 1280: the "MeV/u" line and the $m_\alpha$ line now break and fit, and the step-4 products have a clear gap.

The earlier items are resolved:
- No duplicate scales heading.
- "how hot" instead of "temper-ature".
- "150 million kelvin" throughout.
- The step-2 velocity labels clear the barrier box.
- The new tunnelling step is clear.

## Checked
- Fresh build and captures for this hash (stamp af00c5738a515fa3): contact sheet 1, `stage-selita-390-2` (the barrier figure), `fx-1-390-2`.
- ppchain and barrier label sizes at 390 and 1280 (smallest 14.3 px).
- I stepped the D–T component through all 7 steps at 390: velocity is blue and force red, the legend says the arrows compare speeds within one step only, and the tunnelling step is labelled.
- Worked example at 390.
- Playwright at 390 and 1280: no display overflow in the page, no KaTeX errors, no raw `$`, no horizontal scroll, no console errors.
- Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Shared issues
- none open.
