VERDICT: PASS
CONTENT-HASH: 4a4554bfe169b358
Delta review (figure label moved, 2026-11-12) of the version passed at 59b9a9f4251795d9.

## Blocking
None.

## Polish
None.

## Checked
- Diff: one line in `lessons/units/fy9-moderni/figures.py`, figure `pallo`: the label "pallon pinta" / "sphere surface" is now end-anchored 14 px left of the far arc's upper end, at (P(r2, -30)x - 14, P(r2, -30)y + 8). Before, it was start-anchored 10 px to the right of that point and ran past the 530 px figure in English. (An intermediate version at x = 590 was replaced during this review; this report judges the current one.) The unit.md change is only the regenerated SVG of this figure.
- New label box x 180-350, y 8.5-37.5. The far sphere surface (r_2 = 340, arc -30..30 degrees) ends at (364, 15), so the label ends just left of it and still points to it. Both arcs are sphere surfaces, so the label is right whichever arc a reader takes it for. The near arc (upper end (217, 100)), the r_1 arrow and label (around (141-224, 123-134)), the ray cone (+-10 degrees, top ray ends at y about 122) and the r_2 arrow (+22 degrees, downwards) are all well below it, so nothing overlaps.
- The physics is the same: two sphere surfaces at r_1 and r_2 = 2 r_1, the same cone meets a patch twice as tall (four times the area), dose rates H_1 and H_2 at the two distances, no numbers and no result formula. The alt text, the other figures, the lesson text, exercises, answers and simulation have not changed.
- `python3 scripts/units.py hash fy9-moderni --lang en` is the same at the start and the end of this review.
