VERDICT: FAIL
CONTENT-HASH: 976d1bb4784c43af

## Blocking
- solutions.md:265–279 (L3-04, both `voimakuvio` blocks; renderer scripts/fbdspec.py `draw`) — A. $\overline{T}$ on the cart (450 N) and $\overline{F}_\text{road}$ on the horse (480 N) have their heads at x = 642 in a 600-wide viewBox, so both forward arrows end without a head at the figure's edge. The two forces that drive the paradox show no direction. — Fix the crop in `draw` so that every head and label is inside the viewBox, then re-render.

## Polish
- solutions.md:265–279 (L3-04) — only horizontal forces are drawn, and the cart's diagram has no surface. Add "the weight and the normal force of the road cancel each other and are not drawn", as in L1-04.
- solutions.md:227 (L1-08) — the moved Principle text is correct. "that is, against the child" is unclear; "(the rope pulls the child backwards)" is clearer.

## Checked
- The labels now match the text: with figures.json `F_k→F_dc`, `F_h→F_dh`, `F_t→F_road` and spec `F_r`, the diagrams show T, F_r, F_dc and F_road, T, F_dh, as in the Formula step. (The committed version showed the 410 N rolling resistance as F_d, a drag; the working-tree edit fixes this.)
- L3-04: cart 450 − 410 − 40 = 0 and horse 480 − 450 − 30 = 0. Friction on the hooves points forward, T appears on separate bodies, and a = 0.
- The answers agree with the Finnish set (same data, recomputed): 450 N / 480 N, 38 N, and the rest.
- The hash changed during the review because of an uncommitted developer edit. This report judges 976d1bb4784c43af.
