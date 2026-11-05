VERDICT: PASS
CONTENT-HASH: 8b572d40e2c95165
Round: 2

## Blocking

## Polish
- [Minor] L1-08 and L2-07 — both end on "T = 2πm/(qB) does not depend on v" (carried over); a different misconception in L2-07 would widen the bank. The speed in L1-08 is now 5,0·10^6 m/s, so L1-08 no longer shares its numbers with the lesson example.
- [Minor] L3-04 Sijoitus — still the only display `aligned` chain with `\quad` in the new set; the page shows it well, the inline chain form would match the other solutions.

## Checked
- Round 1 had no Blocking items. Round 1 Polish: the straight quotes of L2-07 are now ”…” (resolved).
- Captures L2-1280-6 (L2-05 ion tracks: the right-hand-rule step, H+, H−, H2+ and the energy remark), L2-1280-8 and L3-1280-8 (L3-05 cyclotron at B = 1,00 T): chains and fractions aligned, no red KaTeX, no clipping.
- Recomputed L1-08 (T = 1,79 ns, r = 1,42 mm), L3-05 (v = 1,92·10^7 m/s, E_k = 3,07·10^-13 J, 32 crossings, 16 turns, t = 1,05 µs, v/c = 0,064, correction 0,3 %), the mass-spectrometer slope 0,118 cm²/V → 22,8 u: the answers and the solutions agree, and answers.py follows.
- L1-06 option wording changed only in the distractors; the correct option unchanged. check_layout 360/768/1280 clean.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4

## Follow-up (8b572d40e2c95165: four solutions.md edits on top of the hash above)
- After `python scripts/build.py fy7-2 --exercises`, Playwright on the preview page with every exercise level and solution open, at 360 and 390 px: every inline `.katex` of L1-02 Annettu and Kaava (and L2-03, L3-02) has `getClientRects().length == 1`. The grouped ${|q| = e = …\,\text{C}}$ is 213 px in a 274 px (360) / 304 px (390) column; $|q|vB = \dfrac{mv^2}{r}$ 118 px, $r = \dfrac{mv}{|q|B}$ 80 px. No horizontal overflow.
- Absolute-value bars, upright units and the decimal comma render cleanly; the chapter titles stay italic.
- No blocking issue.
