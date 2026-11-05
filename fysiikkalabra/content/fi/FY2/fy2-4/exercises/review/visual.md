VERDICT: FAIL
CONTENT-HASH: 7cbf518ecd23380a
Round: 1

## Blocking
- [Major] fy2-4-L2-08 text, Rivi 1-4 at 390 px (own render of preview/fy2-4.html; the 1280 capture is fine) — each row is one inline chain with two to four "=" and does not wrap: "$2500\,\text{W}$", "$600\,000\,\text{J} = 600\,\text{kJ}$", "$240\,\text{kJ}$" and "$= 167\,\%$" are cut off at the card edge, with no scroll. The student must read these lines to find the error, and the result 1,67 and 167 % in Rivi 4 is the clue. At 360 px it is worse. — Fix: break each row into two shorter inline formulas, e.g. "Rivi 4: $\eta = E_\text{o} : E_\text{a}$" then "$= 600\,\text{kJ} : 360\,\text{kJ} = 1{,}67 = 167\,\%$", or set Rivi 1-4 as one display `aligned` block with an `=` column; each piece about 25 characters.

## Polish
- [Minor] L2-08 choices — the shuffled order is Rivi 4, 3, 2, 1, Ei virhettä (reversed rows, seen in both the capture and the render); the rows read more naturally in 1-4 order, a fixed order for row choices if the shuffler allows it.
- [Minor] L2-08 Rivi 1 — the two conversions break at "ja" over two lines; fine once the rows are shortened.

## Checked
- Captures opened: fy2-4-open-exercises-L2-1280-8 and -9 (L2-08 as 4-16: text, opened feedback, choices; neighbouring 4-15); content/fi/FY2/fy2-4/review/shots/, newer than the content. The captures are 1280 px only, so the clipping was found in my own 390 px render (viewport screenshot, details opened).
- Diff only: solutions.md L2-08 (Mallivastaus uses \dfrac and stacked lines; not rendered by me).

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 3
