VERDICT: FAIL
CONTENT-HASH: ac3574cbe218ea95

## Blocking
- [Major] Task 16-17 (L2-09), figure `fy7-16/charger-points` — in the English page the figure's `aria-label` is in Finnish ("Periaatekuva langattomasta laturista sivulta leikattuna, kentän muoto laskettu…"; it is in `preview/en/fy7-16.html`). The other figures in the English page (e.g. `graph-curve`) are in English. The task depends on counting the field lines through the receiver coil, so an English-speaking screen-reader user gets no usable description of an essential figure. Fix: give the English version of this figure's description (the same content: two panels, pad and coil, phone at 3 mm and 6 mm, lines drawn at equal flux steps, the darker lines through the receiver coil are the ones to count) and rebuild. Do not give the counts away.

## Polish
- [Minor] figure `charger-points` (capture L2-11) — the label "$\text{phone}: z = 3\,\text{mm}$" has a loose colon, and "receiver coil" sits right by the dashed divider with a long leader line. The line count of 6 against 4 is hard to count at that size. Consider slightly thicker darker lines.
- [Minor] data tables (L2-05 and others, capture L2-5) — the caption wraps to four lines in a column about 45 % of the card width. Let the caption run full width.
- [Minor] solution L2-09 (L2-12) — the formula box for $e_0'/e_0$ breaks to three rows with the second `=` under the first; it would be clearer on one line, $\dfrac{e_0'}{e_0} = \dfrac{\Phi_0'}{\Phi_0} = \dfrac{n'}{n}$.

## Checked
- Captures at 1280 px with every solution open: L1 part 1; L2 parts 5, 9, 11, 12, 13; L3 part 6. The stage-exercises-390 capture was not opened, so no opened card was seen at phone width.
- Figures: `charger-points` (L2-11) and `graph-curve` (L2-12 and L2-13). The graph has axes with quantity and unit, readable ticks, and a plain curve with no marked points. The task says the graph ends at 40 km, and the solution names the 70 km value as calculated, not read.
- Source: all exercises and solutions read in full. Units and quantities are LaTeX, `\cdot` is used, the decimal point is correct for English, and the order is principle, formula, substitution, answer, check.
- The rendered `aria-label`s were read in `preview/en/fy7-16.html`.
- Not opened: the other L1-L3 parts and the exit ticket.

## Scores
illustrations 3 · typography 4 · Finnish (English prose) 5 · accessibility 3
