VERDICT: PASS
CONTENT-HASH: 58ca1c36704e1ad3
Mode: full
Round: 1

## Blocking

## Polish
- [Minor] L2-05 table column "Curves" is short and fits; no change needed beyond keeping it short on 360 px.

## Checked
- Opened open-exercises-1280-6 (L1-06 choices, correct feedback block, solution), open-exercises-L2-1280-5 (L2-05 task text, table caption and header), open-exercises-L3-1280-4 (L3-03 solution, L3-04 start) at the English build.
- Formulas render with decimal point, units upright with thin space, no clipping, no Finnish text on the page.
- Table captions and headers in English; formula spacing like the Finnish page.
- The unit "times" (L3-03) replaces "kertaa" in the answer unit display.
- check_i18n.py en: 0 errors.

## Scores
illustrations 5 · typography 5 · English 5 · accessibility 4

## Follow-up (58ca1c36704e1ad3: four solutions.md edits on top of the hash above)
- After `python scripts/build.py fy7-2 --exercises`, Playwright on the preview page with every exercise level and solution open, at 360 and 390 px: every inline `.katex` of L1-02 Annettu and Kaava (and L2-03, L3-02) has `getClientRects().length == 1`. The grouped ${|q| = e = …\,\text{C}}$ is 213 px in a 274 px (360) / 304 px (390) column; $|q|vB = \dfrac{mv^2}{r}$ 118 px, $r = \dfrac{mv}{|q|B}$ 80 px. No horizontal overflow.
- Absolute-value bars, upright units and the decimal point render cleanly; the chapter titles stay italic.
- No blocking issue.
