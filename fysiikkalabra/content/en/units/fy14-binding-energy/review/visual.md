VERDICT: PASS
CONTENT-HASH: 9c862ad14f6e60cb

## Blocking
(none) The explorer label finding is resolved by the updated `fx/binding.js`, now that point labels are paper cards drawn above the points:
- $^{4}\text{He}$ sits beside its own point at $A = 4$ and is no longer in the C, N and O cluster.
- $^{56}\text{Fe}$ marks the peak.
- $^{2}\text{H}$, $^{92}\text{Kr}$, $^{141}\text{Ba}$ and $^{235}\text{U}$ are fully readable.
- "fusion" sits below its arrow.

This holds at 360, 390 and 1280. The reaction steps (D–T and U-235) have no display overflow at any of the three widths.

## Polish
1. [Minor] Explorer at 390: the $^{4}\text{He}$ card covers part of the Li-6 and Li-7 points just below it. Optional: a little transparency (`opacity: .9`) on the cards.

## Checked
- Rebuilt for this hash; the components changed outside the hash.
- Captured the explorer myself at 360, 390 and 1280, in the start state and with U-235 fission and D–T fusion. The 360 and 390 graphs zoomed ×2.
- From the earlier pass for this hash: the worked example with all steps at 390, and the ladder and qbars figures.
- Playwright: no display overflow, no console errors, no KaTeX errors, no raw `$`.
- Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Re-check 2026-11-01: photographs
- Screenshots at 360, 768 and 1280 px (details opened, image loaded); check_layout.py OK at 360 and 1280 px; figure gaps 20 px above and 24 px below, no overflow, credit on its own line and legible.
- Meitner portrait fine at all widths; the scan's light border is visible on the left edge but unobtrusive.
