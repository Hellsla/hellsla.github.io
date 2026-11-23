VERDICT: FAIL
CONTENT-HASH: 57d958bad2f4f0ac
SCOPE: delta (Stop and think boxes only, git diff origin/main)

1. Blocking: All three boxes sit between a paragraph and the figure that illustrates it: after 'does no work' / before the Lorentz figure; after the loss-cone sentence / before the mirror figure; after the torus sentence / before the open-ends-vs-ring figure. Fix: move each box to just after its figure (before the next paragraph).
   All boxes otherwise render cleanly: no overflow at 390 or 1280 px, answer opens inside the box, math renders (no raw $ or \n), consistent look and spacing.
2. Checked: preview/en/fy14-magnetic-confinement.html, every Stop and think box with all details open, clipped context captures at 390 px and 1280 px (page overflow test, no overflow). Built with scripts/screenshot.py (review/shots/ contact sheets generated).
