VERDICT: PASS
CONTENT-HASH: 5d25f761f164396f
none

## Blocking
(none)

## Polish
- [Minor] solutions.md 7-17 Kaava — row 2 `x = A/2 ⇒ sin(…) = 1/2` has two relations and is aligned at the arrow, so the `=` column breaks; optionally split into `x &= \dfrac{A}{2}` and `\sin\left(\dfrac{2\pi t}{T}\right) &= \dfrac{1}{2}`.
- [Minor] solutions.md 7-17 Järkevyys block — small `\tfrac` inside `\sin(...)` is tiny next to the text size; legible, untouched by this diff.

## Checked
- Delta: about a dozen Kaava lines became aligned multi-row blocks (L1-01, 7-4, L2, L3). Opened open-exercises-1280-1 (7-1, untouched single-line Kaava for comparison), L3-1280-1, -2 (7-17 and 7-18 Kaava), -3, -4 (7-19 `k T_1 = m T_2`, `\quad` remark), -5 (7-20, four rows), -7 (7-22, five rows with d_max/d_min).
- Rows align at `=`, KaTeX clean, subscripts legible, no clipping or overflow at 1280 px; Sijoitus, answers and Järkevyys unchanged. Layout checks (360–1280 px) already green in the packet.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
