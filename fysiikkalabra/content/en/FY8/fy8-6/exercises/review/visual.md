VERDICT: PASS
CONTENT-HASH: 02af06d85c6fff13
SCOPE: delta numbers,reflow from 6fa3173777f1fcd9 base 4b05399

## Blocking
(none)

## Polish
- [Minor] solutions 6-5 / L2-04 Formula inline: unit-like fractions such as $\tfrac{\text{V}}{\text{Hz}}$ in running text make lines taller (untouched text).
- [Minor] No true 390 px captures of the open solutions exist; phone wrapping rests on check_layout.py (run at 360 px for en, fi, fi-easy: OK).

## Checked
- Delta (solutions.md: the Kaava step, \approx to = for the line and h = ek). Opened fy8-6-open-exercises-L3-1280-6 (L3-04 Formula: aligned blocks, k = dfrac with ≈ row, h = ek in text), 1280-4 and 1280-5 (6-4 aligned Formula/Substitution blocks), L2-1280-1 (6-9).
- Fractions at display size, equals signs in one column, subscripts legible, blocks inside their cards, no red KaTeX.
- check_layout.py fy8-6 --width 360: OK in all three languages with solutions open.
- Hash re-run at end: unchanged.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
