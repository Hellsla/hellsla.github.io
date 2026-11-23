VERDICT: PASS
CONTENT-HASH: 19eec2ea84a99282

## Blocking
(none)

## Polish
- [Minor] L2-06 Formula step: the deviation `\dfrac{h-h_0}{h_0}` inline makes the line very tall; \tfrac inline per NOTES §1.

## Checked
- delta, en (8g: the Kaava step of the model solutions as aligned blocks, one equation per row). The packet's 390 px captures did not exist for the exercise solutions, so I rebuilt preview/en/fy8-6.html and took my own 390 px captures (all details open) of the Formula blocks: the three to four tallest per set, opened and read.
- Measured at 360 and 390 px with every solution open: no clipped or overflowing KaTeX in any solution step, no page-level horizontal overflow, no red KaTeX source.
- The packet hash was b12729dd62abae8c; the content changed afterwards (commit 7eff52543e: the single $h_0$ unit fix in L2-06, which I opened: correct). A second uncommitted edit followed (L2-04 Formula step with \approx and + b, plus the L2-10 formula line), which I also opened (aligned block with three rows, readable). Reviewed against the current hash 19eec2ea84a99282.
- Equals signs align in one column, left sides right-aligned, fractions in display size, subscripts legible, prose and blocks interleave correctly; the changed rows sit in their cards.
- Hash re-run at the end: unchanged.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
