VERDICT: PASS
CONTENT-HASH: 666233ea8f5e3983
SCOPE: delta numbers,reflow from affaffba75d303a6 base 4b05399

## Blocking

## Polish
- [Minor] solutions captures — the open-solution captures exist only at 1280 px (664 px column); the new Kaava rows are short (under ~30 characters, one equation per row), so no clipping is expected at 360–390 px, and check_layout covers it. A 390 px open-solution capture would let this be seen.
- [Minor] Kaava aligned blocks — rows of the form `E &= hf` / `c &= f\lambda` align at "=" so symbols sit right-aligned and look slightly staggered; acceptable, consistent with the other solutions.

## Checked
- Delta (solutions.md, Kaava step re-set as aligned LaTeX blocks): reviewed the diff and the Kaava source blocks; sibling captures of this set (open-exercises 1280) judged by sampling the same block type from fy8-1 and fy8-3.
- Source of every changed Kaava block read: one equation per row, words outside maths, units and decimal comma unchanged, no red KaTeX source seen. The flattened Kaava lines in the packet diff are a diff artefact: the file holds proper aligned blocks.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
