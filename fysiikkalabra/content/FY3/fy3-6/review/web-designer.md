VERDICT: PASS
CONTENT-HASH: 9d2d7a30f569bc1d

## Blocking
None. All five round-2 items are resolved.

## Polish
None.

## Checked
- Hash 9d2d7a30f569bc1d at start and end; lint 0 errors, 0 warnings; build ok; `check_layout.py fy3-6` OK at 360 and at 390 px; 0 console errors at 1280, 390, 360.
- All 8 display formulas: scrollWidth equals clientWidth (606 / 356 / 326 px) at 1280, 390, 360. Widest row is 274 px (the `c_metalli` balance, lesson.md:81) against the 326 px box at 360, so 52 px spare. Page overflow 0 at all widths.
- Screenshots of each split block at 360 and 1280 px (lesson.md:15, 33-36, 81, 85, 92-97): rows read cleanly. Each `=` continuation is indented one step under its left side, and the two-equation blocks (33-36, 92-97) are separated by a clear gap. The 3-row result (85) steps =, ≈ under the first `=`. No row is clipped and no unit fraction collides with a neighbour. The blocks are centred as a unit, which is fine.
- The 35 °C working (92-97): first equation split over two rows, then three short left-aligned rows; reads as one derivation.
- Sim layout unchanged from round 2: canvas, then controls (Upota first, 92x40 px), then readout. Canvas-to-button gap 34 / 35 / 8 px and button bottom 474 / 290 / 244 px from the canvas top at 1280 / 390 / 360, so canvas and button still fit one screen.
- Controls: every button, slider and the select is 40 px tall, no tap target under 40 px, no wrapping labels; the sim readout is DOM text.
- Upota run to t = 10 s at 1280, 390 and 360: TW = TB = Teq = 24,62 °C each time, no errors.
- Text column 67 characters at 1280; 40 and 36 at 390 and 360 (expected for a phone, text size 17 px).
- Screenshots in the scratchpad, not in the repo.
