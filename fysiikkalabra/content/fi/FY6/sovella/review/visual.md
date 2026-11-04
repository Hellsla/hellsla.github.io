VERDICT: FAIL
CONTENT-HASH: 6f3465d0e19501e5

## Blocking
- [Major] fy6-s3 Mallivastaus b) Kaava and Sijoitus, and Järkevyys (shots page-390-26, page-1280-19) — the square roots render broken. In $v = \sqrt{\dfrac{2qU}{m}}$ the radical's overline runs through the numerator $2qU$ (1280 px). At 390 px the Sijoitus row "= \sqrt{180\,\text{m}^2/\text{s}^2}" shows a slash with a line struck through the number, and the Järkevyys \sqrt{2\cdot450\ldots\cdot0{,}20\,\text{m}} has a tiny surd sign. The notation reads as a strike-through and a student could misread the radicand. — fix: find why the KaTeX surd/vinculum is drawn at the wrong height here (same markup inside .sol blocks and the mathlayout row split; compare with a sqrt in another lesson), and re-check every \sqrt in the task solutions at 390 and 1280 px. Not a content change.

## Polish
- [Minor] fig fy6-s3-field (fig 7) — the droplet $q$ floats mid-gap although the text says it starts at rest at the nozzle plate; schematic, but the description or the position could say "lähtee levyltä".
- [Minor] fig fy6-s3-field — label "+60 kV" sits tight against the plate's left end; give it the 10 px clearance.
- [Minor] fig fy6-s1-circuit — the I arrows are purple (momentum colour in the palette); current has no fixed colour, but keep the colour meaning distinct from momentum.
- [Minor] fy6-s4 has no figure (a set-up or U(t) sketch of the flash discharge would help); optional.

## Checked
contact-1 and contact-3; top-1280; page-390-4, -26; page-1280-19; fig-1, fig-3, fig-5, fig-7 at 390. Figures: sets and graph are legible, axes with units, points as markers distinct from the line, E marked at I = 0 with an open ring, the line extended to the axis; polarity and current direction consistent in both circuit figures; the field figure has the field arrows pointing from + plate to earthed plate. No horizontal overflow, no red KaTeX source seen in the captures opened; hints, solutions and feedback open inside their cards. Not opened one by one: stage captures s1 to s4 (seen only in contact sheets), the other 1280 parts.

## Scores
illustrations 4 · typography 2 · Finnish 4 · accessibility 4
