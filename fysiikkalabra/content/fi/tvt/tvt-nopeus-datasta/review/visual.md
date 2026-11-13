VERDICT: PASS
CONTENT-HASH: 432de54e086d7ae9

## Blocking
(none)

## Polish
- [Minor] guide.md steps 4–8 — the rendered ordered list restarts at 1 under each ### subheading (step "Ymmärrä pinta-ala suikaleina" shows as 1., "Laske ensin nopeus" as 1.), although the source numbers 1–8 — continuous numbering would let the teacher and students refer to "vaihe 7" — fix in the shared list renderer (start attribute), not in this guide.
- [Minor] guide.md step 6–7 — "tee laskettu sarake s, yksikkö m" and "sarake v": the column names are plain letters in running text, while the units are KaTeX; they read as quantities, not column names — write the names in code style like `s` and `v` (as `t`, `x` already are in the intro) or as "sarake `v`".
- [Minor] fig-1 (strips) — the leader line from "Δs ≈ v · Δt" crosses the blue curve before reaching the highlighted strip; end the line at the strip's top edge. Label "s = pinta-ala" has a white plate that is fine but slightly heavy; optional.
- [Minor] guide.md — code-style expressions (integral("v","t")) are monospace and not LaTeX; this is correct for software syntax, no change needed, noted only so the convention stays deliberate.

## Checked
- review/shots/tvt-nopeus-datasta-fig-1-390.png: the only figure, legible at 390 px, axes with arrowheads, titles with units, strips and Δt bracket clear, no overlap or clipping, schematic with no numbers (stated in aria-label).
- page-390-3.png (steps 4–7 and figure in place at phone width), page-1280-2.png (same at laptop: figure under its paragraph, reading column intact).
- Not opened individually: other page parts and contact sheets (deterministic layout/a11y checks are clean per the packet); fig-2 capture is a 28×28 empty stub, not a figure.
- Mathematical typography checked in the opened parts: the fractions \tfrac, Δ, \approx, \cdot, decimal commas, units upright with thin space, case ending "1,0 cm:n" all render correctly; division as a colon (0,010 m : 0,020 s).

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 4
