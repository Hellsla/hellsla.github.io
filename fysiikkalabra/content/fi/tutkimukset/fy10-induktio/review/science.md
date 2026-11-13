VERDICT: PASS
CONTENT-HASH: 14aa4c1c63c79a34

## Blocking
None.

## Polish
- (visual, not physics) Lines leaving the bottom bound (y 278) stop about 12 px above the bottom fade (290); in the 390 px capture no abrupt end is visible, but a line clipped there would end in white.

## Checked (delta 2026-11-13)
- Figure *flux* redrawn (figures.py, investigation.md SVG), capture fy10-induktio-fig-3-390.png viewed. The lines are still traced from the two-pole model (source at the red pole, sink at the blue); only the points inside the magnet are now dropped, so each line starts on the red half's surface and ends on the blue half's surface instead of at one pole point: physically better (field lines outside a bar magnet leave its N half and enter its S half). Direction arrows point away from the red pole on every line, so the lines leave red and return to blue. The lines through the coil ($x_0$, inside the turns) are the darker ones; the lighter ones curve past the coil back towards the blue half, and the frame fades them out rather than ending them. The alt text (four darker lines through the turns, lighter ones back to the blue end) matches. Label *käämi, N kierrosta* moved up to clear the lines: placement only. No text or physics changed.
