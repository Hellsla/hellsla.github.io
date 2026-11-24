VERDICT: FAIL
CONTENT-HASH: 374766fe1b22fc4c

## Blocking
- [Major] solutions.md fy3-14-L2-04 (9-13), L3-03 (9-21), L3-04 (9-22) Kaava — the final fraction's numerator is hand-broken with `\begin{array}`: it renders as a stacked "c_v m_v (T_v" over "−T) − c_v m_j T" (L3-04 as four lines "c_v m_v (T_v / −T) / −c_v m_j T / −c_j m_j ΔT_j"), splitting the bracket T_v − T across lines — the formula is hard to read, and it breaks even at 1280 px where it fits — keep each numerator term whole (break only before a + or − outside a bracket, or define the numerator as a symbol, e.g. first row `X = …`, then `s = \dfrac{X}{m_\text{j}}`).
- [Major] solutions.md fy3-14-L3-03 (9-21) Kaava — the `\quad` continuation rows were merged into one line, and the equals signs of the three rows are not in one column (row 1 `Q_luovutettu = Q_vastaanotettu` sits about 150 px to the right of rows 2–3) — an aligned block with unaligned rows reads as broken typography — give every row the form `lhs &= rhs` with the left side on its own row when long, as in L3-04's first rows.

## Polish
(none)

## Checked
- Delta (Kaava re-set as aligned blocks; solutions.md). Opened at 1280 px, solutions open: open-exercises-1280-1 and -8 (L1, short Kaava fine), L2-1280-1/-2/-3 (9-11, 9-12: aligned, fine), L2-1280-4 (9-13: broken numerator, row 1 `=` about 16 px off), L3-1280-4/-5 (9-21: misaligned, broken), L3-1280-6 (9-22: four-line numerator), L3-1280-7/-9/-10 (rest fine).
- Hash same at start and end.

## Scores
illustrations 5 · typography 2 · Finnish 5 · accessibility 4
