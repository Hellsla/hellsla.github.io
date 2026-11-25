VERDICT: PASS
CONTENT-HASH: cddfd08f0802bd10

## Blocking
None.

## Polish
1. [Minor] s3 c, hint 3 (en): ok; none required. Optional: "As the time, use" -> "Use the mean of the three readings as the time" (s3 a, hint 2).
2. [Minor] all parts, 390 px (en): an open hint box is indented and narrower than the task text (about 270 px of 324 px), so formulas such as $\sigma = \dfrac{M}{N\,a\,b}$ wrap onto their own line. Nothing is clipped or scrolled. Shared issue (templates/site.css `ol.parts>li>.hints`): reduce the left margin of the open box on phones. This is optional.

## Checked
- Built previews at 390 and 1280 px: Tehtävät cards with hints closed (row of three, one row at 1280, three stacked lines at 390) and open (s1 a-d, s2 a-d, 29 hint groups counted, no horizontal page overflow, scrollWidth equal to viewport).
- Formulas in the hint boxes (fractions, \Delta, \tau_k, units with thin spaces) render inside the boxes. Decimal comma or point is correct for the language. Reading order is correct.
