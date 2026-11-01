VERDICT: PASS
CONTENT-HASH: 1471d73e16f9321b

## Blocking
(none) This is a re-review after commit c6532e4f and the timeline commits up to b3bbc371. All earlier Polish items are resolved or reduced:
- D–T is now `$\text{D–T}$` and no longer breaks.
- Percentages are in LaTeX.
- The site paragraph is in time order.
- The table cell reads "2034 (research)".
- 1987 and 1988 now agree.

## Polish
1. [Minor] `schedule` figure (my 2× capture at 390). The `+4 years` arrow now ends just at the left edge of the 2039 "D–T" label and still almost touches the "D". Fix: shorten it by another 8–10 units, or set the label 10 units to the right.
2. [Minor] Timeline legend (`fx-1-390-1`). The task shows only eight Politics and Machines events, but the legend still lists "Scientific discovery" and "People". This is a shared component: list only the themes present.

## Checked
- Fresh build and captures for this hash, taken after the last timeline commit: top and intro at 390 and 1280, every stage at 390 and 1280, contact sheets.
- The eight-event timeline (closed cards, one toggle each).
- The `schedule` figure at 2× (labels 15.5 px at 390 and 18 px at 1280).
- Playwright: no `.katex-error`, no raw `$` and no overflow at 390 or 1280.
- The new text in Why, Challenges, the site paragraph and the find-error options.

## Shared issues
(none new)

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Re-check 2026-11-01: photographs
- Screenshots at 360, 768 and 1280 px (details opened, image loaded); check_layout.py OK at 360 and 1280 px; figure gaps 20 px above and 24 px below, no overflow, credit on its own line and legible.
- Aerial site photo in the inquiry card stays inside the card and above the choice question; the central solenoid photo sits 35 px above the next heading.
