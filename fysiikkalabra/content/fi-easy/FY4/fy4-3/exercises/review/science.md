VERDICT: FAIL
CONTENT-HASH: 6d157e2383c3163e

## Blocking
- solutions.md:265–279 (L3-04, both `voimakuvio` blocks; renderer scripts/fbdspec.py `draw`) — A. In the cart diagram $\overline{T}$ (450 N) and in the horse diagram $\overline{F}_\text{t}$ (480 N) have their heads at x = 642 in a 600-wide viewBox. Both forward arrows end without a head, so the direction of the forces that drive the paradox is not shown. — Fix the crop in `draw` so that every head and label is inside the viewBox, then re-render.

## Polish
- solutions.md:265–279 (L3-04) — only horizontal forces are drawn. Add one sentence: paino ja tien tukivoima kumoavat toisensa eikä niitä piirretä.
- solutions.md:227 (L1-08) — the moved Periaate text is correct; "eli lasta vastaan" is unclear (carried).

## Checked
- L3-04: the working-tree edit renames the rolling resistance F_v → F_r in Annettu, Kaava and the spec, so the alt text no longer calls it "ilmanvastus". Each body now has its own diagram. Both sums are zero and match the Kaava step.
- The numbers and answers are the same as in the fi set and were recomputed (450 N, 480 N, 38 N, …).
- The hash changed during the review because of an uncommitted developer edit. This report judges 6d157e2383c3163e.
