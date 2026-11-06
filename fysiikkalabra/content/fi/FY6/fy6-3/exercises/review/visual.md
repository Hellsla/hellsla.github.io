VERDICT: PASS
CONTENT-HASH: 593f504a543bc1e6
ROUND: 1

## Blocking

## Polish
- [Minor] fy6-3-L1-09 option order — the figures appear as Kuvaaja A, D, B, C (letters stay with their figures, the order is shuffled), which reads oddly on a phone — keep the letters in order by lettering after the shuffle, if the template allows.
- [Minor] fy6-3-L1-09 feedback of Kuvaaja A — the coordinate pair is set as two formulas, "(4,0 mA" and "8,0 V)", with a bare semicolon, and at 390 px it breaks inside the pair — set the pair as one formula ($(4{,}0\,\text{mA};\ 8{,}0\,\text{V})$ as in the solution, which renders whole).
- [Minor] fy6-3-L1-09 figures — each graph is 273 px wide at 390 px, tick numbers about 11 px and gridlines 8 px apart in the vertical direction; readable, but the points the feedback quotes ((4,0 mA; 8,0 V)) have to be found among 24 gridlines — optional: grid every 2 V.

## Checked
- Renders at 390 px of fy6-3-L1-09 with the correct choice and with a wrong one (Kuvaaja A, feedback open), Vastaus and Näytä ratkaisu open; the four option figures seen at full size and measured (viewBox 600 x 360, label 24 px, scale 0.46 at 390 and 0.41 at 360).
- Overflow: page scroll width 390, no element outside the viewport, widest formula chain 247 px (solution) and 230 px (feedback).
- Figure descriptions (aria-label) read from the source: full axis description plus the curve's points, same axes and weight in all four, A curved, B slope 0,5 kΩ (I : U), C correct (9 V at 4,5 mA), D flat at 2 V — the data match the feedback.
- Text only: distractors catch the I : U slope inversion and the "value as height" mistake the lesson names; the correct graph is not identifiable by its description; no reason stage.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
