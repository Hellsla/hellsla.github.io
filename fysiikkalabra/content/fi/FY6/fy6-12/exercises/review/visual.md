VERDICT: FAIL
CONTENT-HASH: 2e352fcfcb383439

Delta: new L2-08 (12-16, find-the-error choice) and three L3 texts split into paragraphs.

## Blocking
- [Major] 12-16 model answer (solution), line `U = V_B - V_A = 120 V - 30 V = 90 V` — the single inline formula is 326 px wide at 390 px and the card clips it: it ends "= 90" with "V" cut off (the same line is 369 px right edge vs 347 px card edge) — the key corrected value is unreadable and the 300 px rule is broken — break it over two lines (`U = V_B - V_A` / `U = 120 V - 30 V = 90 V`) or use an aligned block.

## Polish
- [Minor] 12-16 the options appear in the order Rivi 1, Rivi 4, Rivi 3, Rivi 2 although the task says "rivi riviltä"; keep row order (last option stays last).
- [Minor] 12-16 the correct option is the longest row label (39 vs 24-33 characters); shorten it or lengthen others, e.g. "Rivi 3: liike-energia".
- [Minor] 12-16 solution `E_k = 1,442 ... ≈ 1,4 ...` is exactly 304 px, with no margin at 390 px; split it.

## Checked
- Renders (own script, 390 px and 360 px, correct option committed, all feedback and answer and solution open): 12-16 card, overflow measured (page width = viewport; clipping inside the card found for the U line, at 360 px also the E_k line).
- Rendered: option feedback (the correct one starts "Oikein, tämä rivi on väärin" and gives no further stage), distractors catch row 1 direction, row 2 sign of E_p, row 4 unit factor, no-error option.
- Text only: Finnish compound words and glossary (potentiaaliero, potentiaali) consistent; the L3-01 and L3-03 paragraph splits (no figure or formula change, read in the diff).

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 3
