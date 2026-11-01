VERDICT: PASS
CONTENT-HASH: 63a171be08f0db43

## Blocking
(none) The earlier polish and shared items are resolved:
- **Marks.** Marks closer than one mark width now share a stacked column. With all eras there are 0 overlapping marks at 390 (50 before) and 5 at 1280.
- **Maths.** `timeline.json` uses LaTeX ($E = mc^2$ title and text, keV, MeV), and titles go through `md`. Four KaTeX nodes render on the Einstein cards, with no errors.
- **Frame.** The strip has a single frame: the SVG has no border or padding, so the scale is exactly 1.000 at 390 and the year labels are 15 px.
- **Resize.** A resize redraws only the strip. Tested by rotating 390 → 844: the open biography and cards stay open.
- **Countries.** The seven countries since 2015 are named.

## Polish
1. [Minor] Task 3 (`fx-ft-map`) tells students to "use *Show on the map*". The component now shows that link only when `fy14-global-fusion-explorer.html` is published, so on the preview the cards have no map link and the instruction points at nothing. This is acceptable only if both units are published together, as the developer report says. Otherwise give the fallback in the prompt ("If the map is not available yet, …").
2. [Minor] Small task timelines (for example `fx-ft-map`, three events, two themes) show all four theme entries in the legend. Fix (shared `timeline.js`): list only the themes of the events shown.

## Checked
- Rebuilt after commit 525827b2 (the shared component changed during this review: no filters on the task timelines, map links only when published). Captures regenerated.
- All five timelines (`fx-ft-timeline`, `-claims`, `-map`, `-geo`, `-steps`) measured at 390 and 1280. Year labels 15–17 px with no overlaps. No horizontal scroll, and `check_layout` reports OK at 360.
- Cards are closed by default. Clicking a mark opens and focuses its card.
- No console errors or failed requests (the earlier 404 for the map page is gone). Hero at both widths (no text). Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

## Shared issues
- Badge style (`.badge` with a long note, for example "Made-up example data", "Values calculated by a model", "Statistical data"): a wrapped note in a pill-shaped badge becomes an oval at 390. Use a smaller radius when it wraps, or put the note outside the badge.
- `timeline.js` legend: list only the themes present among the events shown.
