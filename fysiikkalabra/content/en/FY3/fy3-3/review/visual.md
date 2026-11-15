VERDICT: PASS
CONTENT-HASH: 65a5de3ff8a2313d

## Blocking
- none

## Polish
- [Minor] Example 3 "Apply to a new situation", Reasonableness — the new display block starts with a bare numeric expression ($0.205 \cdot 101\,\text{kPa}$) and so does not say what it computes; the lead-in sentence ("so the pressure rises by about") carries it — when the text is next edited, start the row with the quantity, e.g. `\Delta p \approx 0.205 \cdot 101\,\text{kPa} \approx 21\,\text{kPa}` (the Finnish likewise).
- [Minor] same block at 360/390 px — the second row's "≈" sits a few pixels right of the first row's left edge (relation spacing after `&`); cosmetic, both rows read clearly.
- [Minor] screenshot.py — no listed capture opens the optional Example 2/3 boxes of Esimerkit, so their solutions cannot be judged from the packet's captures; an `open-sovella` capture would close the gap (shared tool, not this lesson).

## Checked
- Delta: one chain in the Reasonableness of the optional Example 3 solution (inquiry.json), now a display block; numbers, signs, units unchanged.
- Packet captures opened: fy3-3-stage-sovella-390-2, fy3-3-stage-sovella-390-3 (worked example steps 3–7 and the closed optional boxes: layout intact, no overflow). The changed solution is closed in every packet capture.
- Therefore captured the opened solution myself from the current preview page (preview/en/fy3-3.html, `?ratkaisut=1`, all boxes open) at 360, 390 and 1280 px and opened all three: KaTeX renders (no red source, no raw `$$`), the block sits in its white formula panel inside the solution card; on a phone two rows ("0.205 · 101 kPa" / "≈ 21 kPa,"), at 1280 px one row; nothing clipped; page scroll width equals the viewport at all three widths; the comma is set inside the formula and the sentence continues "and 101 + 21 ≈ 122 kPa" on the next line without a stray leading comma. Decimal point, upright units with thin space, `\cdot` all correct.
- The neighbouring text of the solution (fraction 60/293, 80/20 = 4, 404 kPa, 101 kPa) is unchanged and reads well.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
