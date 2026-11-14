VERDICT: FAIL
CONTENT-HASH: e803f57504935926 (from the packet and shots/stamp.txt; `reviews.py hash FY7/koe` does not resolve an example exam, so it could not be re-run at the end)

## Blocking
- [Major] k2 c) Mallivastaus, VASTAUS (page-390-16, fig-4..: boxed answer) — at 390 px the framed answer `e/m_e = (1,74 ± 0,08)·10^{11} C/kg` renders as an empty narrow box; the answer is readable only at 1280 px (page-1280-11) — the essential result is invisible on a phone — let the boxed answer wrap or scroll inside the frame, or set the frame to `max-width:100%` with the formula inline-breaking.
- [Major] k2 b) and c) SIJOITUS (page-390-15, -16) — display substitution chains (`(e/m_e)_min = 2/((0,80·10^{-3} T)^2 · 1,859·10^{-5} m^2/V)` and the one in k2 b) are cut off at the right edge of the white panel at 390 px; the units and exponents cannot be read — long chains should break at `=`/operators, not clip — split the fraction (denominator on its own row) or enable wrapping in the formula panel.

## Polish
- [Minor] Opening "Kokeen rakenne" — the bold sentence breaks "120 / p:n" and "70 / p." across lines; use a non-breaking thin space between number and `p`.
- [Minor] k2 rubric (page-1280-12) — "±0,08–0,13 · 10^{-3} m²" and "1,65–1,83 · 10^{11} C/kg" are ambiguous ranges (exponent applies to the end value only, and the first wraps after the dash); write `(0,08\ldots0{,}13)\cdot10^{-3}\,\text{m}^2` and `(1{,}65\text{–}1{,}83)\cdot10^{11}\,\text{C/kg}`.
- [Minor] k4 graph e(V) (fig-6) — x ticks 5…55 are set far below the axis under the −20 gridline and are crowded at 390 px; put them at the axis (or on the bottom edge with the origin 0) so they read as the t-axis.
- [Minor] k2 graph r²(U) (fig-3) — error bars are about 3 px and the middle points nearly disappear at 390 px; enlarge them or the markers.
- [Minor] "Esimerkkiaineisto." label under tasks 5–7 and the quoted "luo energiaa" use straight quotes; use Finnish ” ” quotes.

## Checked
- All 16 contact sheets (184 captures) opened, including k4–k7 and the scoring section.
- 1280 px: page-1, 11, 12, 13, 16, 17, 23, 24, 30, 36, 42, 43, 44 (opening, k2 solution, k3, k4 rubric, k5, k6, k7 rubric, Kokeen pisteet).
- 390 px: page-390-15, -16; figs 1, 3, 6, 12 (the four graphs) at doubled size; the other figure captures are KaTeX snippets (sqrt, fractions) seen on the contact sheets only.
- The scoring section (Kokeen pisteet, 0 / 70 p with the three part totals) is clear and consistent at both widths.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 3
