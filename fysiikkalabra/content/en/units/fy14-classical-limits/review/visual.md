VERDICT: PASS
CONTENT-HASH: 246a2edfabca8c0a

## Blocking
(none) All earlier findings are resolved:
- French corner: *un corps noir* is now *ẽ KOR NWAR*. The respellings are in italics, and the box explains the convention once.
- The 4000 K label sits above its own peak without a white box. The spectrum shows "X-rays" and "micro-/waves".
- The worked example keeps its equalities whole at 390: Given, Unit conversions and Answer ("$\approx 1.07\ \mu\text{m}$, that is, $1070\ \text{nm}$").

## Polish
1. [Minor] `figures.py`: the new labels "micro-", "waves" and "4000 K" use `size=22`, which renders at 13.1 px at 390, below the 14 px rule. Every other label renders at 14.3 px. Fix: use the default size 24. "micro-" fits in the 111-unit band. Put "4000 K" right of the red peak, at about `(820, 0.17)`, where it touches no curve; at 22 it now just touches the red curve's rise.
2. [Minor] Timeline legend at 390: the four themes still wrap one per line, except the last two (shared component; see below).

## Checked
- Fresh build and captures for this hash (stamp current): top and intro at 390 and 1280, every stage at 390 and 1280, and `fx-2-390-1` (timeline: strip at its real width, cards with an open/close toggle).
- My 2× captures at 390 of the hero, spectrum, curves and catastrophe figures, and the worked example with all seven steps open at 390 and 1280.
- In Playwright at 390 and 1280: no `.katex-error`, no clipped display maths, no page overflow, no console errors.
- The timeline data now writes `$E = mc^2$`. The hash is unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Shared issues
- `assets/units/fy14/fx/timeline.js`: the legend `ul` wraps unevenly at 390. Fix: `display:flex; flex-wrap:wrap; gap:.25rem 1rem` on `.fx-legend`.
