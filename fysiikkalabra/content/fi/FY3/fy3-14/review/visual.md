VERDICT: PASS
CONTENT-HASH: d6e581ceff728ce3

## Blocking

## Polish
- [Minor] fig-2 (before-after, 1280 px) — the bottom caption row "jää 0,10 kg …" sits close to the frame edge, and the final thermometer's scale label "0" touches the glass; fine at 390 px — leave extra margin at the bottom in the raster.
- [Minor] fig-2 and fig-3 — the raster text is a picture, so labels are no longer LaTeX (a teacher-approved figure; the aria-label carries the content) — for science: fig-2 has ice at 0 °C but fig-3 ice at −10 °C with the same masses; the text should say they are different cases.
- [Minor] fig-2/fig-3 — `<image>` height (355, 397.5) differs from the viewBox (344, 392), so the bottom edge is trimmed slightly — match the heights.

## Checked
- Delta: three rasters replaced the inline SVGs (hero, before-after, energy-balance), approved by the teacher; lesson.md otherwise unchanged.
- Opened fig-1-390 (hero), fig-2-390, fig-3-390, intro-1280 (hero beside the goals box, opening layout fine) and theory-1280-1 (figures beside and under their paragraphs, layout intact).
- Alt text and aria-labels are kept and describe the figures; labels in the rasters are legible at 390 px; velocity, force and heat colours are consistent with the palette.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
