VERDICT: PASS
CONTENT-HASH: b4ffca66ec96bd6c

## Blocking

## Polish
- [Minor] Mittaa, sentence before the table — "pit" and "lyh" are plain words in the running text, so "ja lyh sen lyhentämistä" reads as a garble — write "Alaindeksi $\text{pit}$ tarkoittaa ilmapatsaan pidentämistä ja $\text{lyh}$ sen lyhentämistä."
- [Minor] investigation.md (Epävarmuus ja luotettavuus, 390 px) — the line break falls after `lukuarvo ±` so the sign is separated from `epävarmuus`; use `lukuarvo $\pm$~epävarmuus` or a no-break space.
- [Minor] fig-9 (model graph) and fig-12 (frequency graph) — axis titles $L$, $\lambda$, $1/f$ have no unit, and the y axis has no ticks — the graphs are schematic, but the NOTES §3 rule asks for quantity and unit on each axis — write $L\ (\text{m})$, $\lambda\ (\text{m})$, $\dfrac{1}{f}\ (\dfrac{1}{\text{Hz}})$ and say "kaaviokuva, ei mittakaavassa" in the aria-label.
- [Minor] fig-9 — the line starts at about n = 0.7 on the axis and never shows the negative intercept $-(\lambda/4+e)$ that the next sentence asks about — a dashed extension to n = 0 (extrapolation) would support the hint — extend dashed to the y axis.
- [Minor] fig-3 (standing wave) — the left antinode is drawn exactly at the tube mouth, while the theory text says the antinode is slightly outside — add a short dashed overshoot or a note, as fig-7 does with $e$.
- [Minor] investigation.md, Tunnettu arvo — `\ \text{m/s}` and `\ \text{K}` use a normal space in the formula; the house form is the thin space `\,`.
- [Minor] Epävarmuus section — "lukuarvo ± epävarmuus" is plain text, while the formula in the line below is LaTeX — write "$\pm$" in maths. "Kaksi tapaa käsitellä tulokset" reads better as "…tuloksia".

## Checked
- Delta 2026-11-18: headers $L_\text{pit}$, $L_\text{lyh}$ and the added sentence. Opened page-390-8 (table fits, no break) and -9, -11 (surroundings fine).

## Earlier checked (delta 2026-11-16)
- Changes: heading ”Kaksi tapaa käsitellä tuloksia”, `\pm` as maths, thin spaces in the speed formula. Opened page-1280-6 and -7: heading, ± and `(\ldots \pm \ldots)\,\text{m/s}` render correctly.
- Figures untouched by this branch (not judged now); no overflow or clipping seen in the opened captures.
- Phone (390 px): page-390-8, page-390-10 (heading, ±, (… ± …) m/s, formula): fine, no overflow.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
