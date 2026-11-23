VERDICT: PASS
CONTENT-HASH: cca2bc526200a65c

## Blocking

## Polish
- [Minor] solutions captures — the open-solution captures exist only at 1280 px (664 px column); the new Kaava rows are short (under ~30 characters, one equation per row), so no clipping is expected at 360–390 px, and check_layout covers it. A 390 px open-solution capture would let this be seen.
- [Minor] Kaava aligned blocks — rows of the form `E &= hf` / `c &= f\lambda` align at "=" so symbols sit right-aligned and look slightly staggered; acceptable, consistent with the other solutions.

## Checked
- Delta (solutions.md, Kaava step re-set as aligned LaTeX blocks): fy8-5-open-exercises-L2-1280-3 (5-13: six-row Kaava block)
- Source of every changed Kaava block read: one equation per row, words outside maths, units and decimal comma unchanged, no red KaTeX source seen. The flattened Kaava lines in the packet diff are a diff artefact: the file holds proper aligned blocks.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
