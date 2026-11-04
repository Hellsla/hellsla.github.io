VERDICT: FAIL
CONTENT-HASH: d7a934506223dde6

## Blocking
- [Major] fig-7 (earthing), right panel, $I_\text{fault}$ label (x=526 to 518) — the nudge moved the label's left edge onto the violet current arrow (arrow shaft at x=522, label starts at 518). In the 390 px capture, cropped and enlarged, the arrow shaft runs through the letter I, so the label reads as a slash plus the subscript, not as the symbol. The previous PASS rested on the label being clear of the arrow, which is no longer true — a label that cannot be read as its symbol defeats the figure's point (the fault current flows along the earth wire) — fix: set the foreignObject x to at least 530 (the old 526 was clear; to gain room use a smaller width, not a leftward shift), or put the label left of the arrow; then regenerate the captures.

## Polish
- [Minor] fig-7 left panel — the violet arrow I still crosses the leg and arm (unchanged, optional).

## Checked
- fig-7 at 390 px, opened whole and cropped at 6x (all three languages compared): defect above, same in all three languages.
- fig-11 at 390 px opened; the nudge touches only fig-7, rest of the layout intact.
- fig-11 (RCD) at 390: $I_\Delta$ label and $I_\text{L} - I_\text{N} = I_\Delta$ clear and upright, nothing clipped; fig-9 ("extra-low voltage") and fig-15 ("danger of fibrillation") labels fit without clipping.

## Scores
illustrations 3 · typography 5 · Finnish 5 · accessibility 4
