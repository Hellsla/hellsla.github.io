VERDICT: PASS
CONTENT-HASH: 96c26f38f6eaa964

Delta review of the FY9 audit fixes (2026-11-10). Previous PASS hash: 5d7daab35c8d643b. The hash was the same at the start and the end of this review.

## Blocking
None.

## Polish
None.

## Checked
- Tutki graph (energy chain of a condensing plant): the x axis line now ends at x2=384 and the arrowhead path is M396,296 L383,302 L383,290, so the tip lies inside the 400-wide viewBox; the largest x coordinate in the SVG is 390 (gridlines).
- The SVG in inquiry.json is byte-identical to figures.py tehot() output (imported and compared), so the generator and the page agree.
- Built preview at 360 px: the arrowhead is visible, bars still read P0 = 400, P1 = 350, P2 = 150, P3 = 140 MW on the 50 MW grid, matching the aria-label; the to-scale claim and the efficiencies are unaffected.
- Only coordinates of the axis changed; no physics text changed.
- Language version checked: fi; the change is the same as in fi, in translation.
