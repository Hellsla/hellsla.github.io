VERDICT: FAIL
CONTENT-HASH: a71f40db599e2afb

## Blocking
- [Major] open-exercises-L2-1280-1 (L2-01 Annettu), L1-04 and L2-02 Järkevyys — inline values break after the `\cdot` ("9,46 ·" / "10¹⁵ m", "8,8 ·" / "10²⁶ m") and an opening bracket is stranded at a line end ("vedyllä (" / "6,5 · 10⁴)", "valovuotta (" / "4,0 · 10¹⁶ : …") — a mantissa read apart from its power invites misreading in the solution a student checks against — make inline maths nowrap (`.nobr`) and keep the bracket with the maths; one CSS/build fix covers the lesson and exercises.

## Polish
- [Minor] L3-01 Annettu — "$d_\text{M} = 1{,}27 \cdot 10^{7}$ m" fine in form, but the answer chip shows 120 m while the Sijoitus ends at 118 m; the Vastaus line explains it, so only check that the order is clear.
- [Minor] L2-01 answer chip "930" with the unit "tuhatta" in the input is clear, but the solution's last row "930 tuhatta" is plain words after maths; keep as is or set `\text{tuhatta}`.

## Checked
- Opened open-exercises-1280-1, -2 (L1-01, L1-02 with the scale-marks figure), -4 (L1-04/05), open-exercises-L2-1280-1, -3, open-exercises-L3-1280-1, -3. Solutions follow principle, formula, substitution, result and Järkevyys; chains are aligned in rows; units upright with a thin space; scale-marks figure is clear, gives every value and does not give the answer away; input rows and the opened solutions sit inside their cards.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
