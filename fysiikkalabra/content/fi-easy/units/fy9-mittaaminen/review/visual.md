VERDICT: PASS
CONTENT-HASH: ce981cbb7ceb9e3a
SCOPE: delta: round 3, the fix of round 2 in s7 (Jousen kalibrointi) c criterion `calculation`; s8 grading panel re-checked; 360 px
Round 3: delta against the version round 2 reviewed (fix round 2).

## Blocking
(none) The round-2 Major (literal backslash-n in the s7 c formula, red KaTeX error) is fixed in the fi-easy file: real newlines, three aligned rows render.

## Polish
- [Minor] s7/s8 Sijoitus boxes end in ";" or ","; same as older tasks, optional.

## Checked
- Rebuilt fy9-mittaaminen and rendered preview/fi-easy/fy9-mittaaminen.html in headless Chrome at 360 px with every details element open (s7 and s8 grading panels included): 0 `katex-error` elements, 375 formulas rendered; 0 errors without opening too.
- DOM of the s7 c block read: `x &= \dfrac{4{,}5\,\text{N}}{30{,}0\,\text{N/m}}` etc. present, no raw `\n` text. Hash re-run: ce981cbb7ceb9e3a.
- Round-2 card and figure checks stand; only JSON line breaks changed.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
