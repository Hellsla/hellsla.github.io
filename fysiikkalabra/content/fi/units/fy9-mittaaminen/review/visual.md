VERDICT: PASS
CONTENT-HASH: 81de44efc34be42b
SCOPE: delta: round 3, the fix of round 2 in s7 (Jousen kalibrointi) c criterion `calculation`; s8 grading panel re-checked; 360 px
Round 3: delta against the version round 2 reviewed (fix round 2).

## Blocking
(none) The round-2 Major (literal backslash-n in the s7 c formula, red KaTeX error) is fixed: the JSON now has real newlines, and the formula is rendered as three aligned rows.

## Polish
- [Minor] s7/s8 Sijoitus boxes still end in ";" or "," between chain boxes; same as older tasks, optional.

## Checked
- Rebuilt fy9-mittaaminen (fi) and rendered preview/fy9-mittaaminen.html in headless Chrome at 360 px width with every details element open (self-assessment/mallivastaus panels of s7 and s8 included): 0 `katex-error` elements, 373 rendered formulas; also without opening: 0 errors.
- DOM source of the s7 c block read: `x &= \dfrac{4{,}5\,\text{N}}{30{,}0\,\text{N/m}}` etc. present as KaTeX annotation, no raw `\n` text. Hash re-run: 81de44efc34be42b.
- The round-2 render of the cards and figures (no clipping or overflow) stands; only the JSON line breaks changed.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
