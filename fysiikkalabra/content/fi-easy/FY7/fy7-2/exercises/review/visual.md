VERDICT: PASS
CONTENT-HASH: e317aca52d260b6d

## Blocking
(none)

## Polish
- [Minor] solutions.md L2-01 Sijoitus — the connecting word between the v chain and the r display is not shown (the layout renders the display as its own block); the two blocks read as consecutive steps, so nothing is lost.

## Checked
- Delta: L2-01 solution Sijoitus, r as an aligned display (fraction row, \quad \cdot v row, = 0,06463 m = 6,463 cm row); rendered at 360 and 390 px from the built page with every solution open, and open-exercises-L2-1280-1 at laptop width.
- Result: three rows with equals signs in one column, units upright with a thin space, nothing clipped, no horizontal overflow; the v chain above it is unchanged.
- Only the line breaking of the formula changed; text, numbers and units unchanged (diff read). Deterministic layout checks 360/768/1280 clean per packet.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4

## Follow-up (e317aca52d260b6d: four edits on top of the hash above)
- Built `python scripts/build.py fy7-2 --exercises` and measured in Playwright (preview page, every exercise level and solution opened) at 360 and 390 px: every inline `.katex` of L1-02 Annettu and Kaava (and L2-03, L3-02 Periaate/Kaava) has `getClientRects().length == 1`. The grouped ${|q| = e = …\,\text{C}}$ is 213 px wide in a 274 px (360) / 304 px (390) column; $|q|vB = \dfrac{mv^2}{r}$ 118 px, $r = \dfrac{mv}{|q|B}$ 80 px. No horizontal overflow.
- Opened the 360 px capture of the L1-02 solution: absolute-value bars, upright units, decimal comma and fraction all render cleanly; the chapter titles are italic as before.
- No blocking issue.
