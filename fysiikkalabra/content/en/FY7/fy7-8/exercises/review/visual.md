VERDICT: FAIL
CONTENT-HASH: 28f469e13603292f

## Blocking
- [Major] content/en/FY7/fy7-8/exercises/solutions.md:191 (fy7-8-L3-04, part c “Saving”, 390 and 1280 px) — the rows `&\cdot 50\,\tfrac{€}{\text{MWh}} = 30\,300\,\text{MWh}` and `&\cdot 50\,\tfrac{€}{\text{MWh}} = 1.515 \cdot 10^{6}\,€` carry the relation in mid-row. On a phone `·50 €/MWh` stands left of the equals column twice, so the rows read `·50 €/MWh = 30 300 MWh` and `·50 €/MWh = 1.515 · 10⁶ €`; at 1280 px the first row ends `… · 50 €/MWh = 30 300 MWh` — the product `30 300 MWh · 50 €/MWh` is cut in two and the visible equality is false, ambiguous notation in a worked calculation — break at the relations: `&= (43\,440\,\text{MWh} - 13\,140\,\text{MWh}) \\ &\cdot 50\,\tfrac{€}{\text{MWh}} \\ &= 30\,300\,\text{MWh} \cdot 50\,\tfrac{€}{\text{MWh}} \\ &= 1.515 \cdot 10^{6}\,€`.

## Polish
- [Minor] solutions.md:266 — after the boxed value the rest reads as a fragment: “Is the power loss at the line voltage …”. Write: `**Answer:** $13\,\text{MW}$. This is the power loss at …`.
- [Minor] solutions.md:273 — `P_\text{h} \sim 1 : U^2`: the site mostly writes proportionality with `\propto`.
- [Minor] solutions.md:244 — on a phone the inline `\dfrac` formulas in the Formula step make uneven line spacing; readable.

## Checked
- Delta (reflow). The packet's inventory has no phone-width capture of the opened exercise solutions, so own captures were made from preview/en/fy7-8.html (built after the content) with every exercise solution open at 390 and 1280 px: every solution step holding a display formula, opened at full size (sheets S8-390-1.png, S8-1280-1.png in the session scratchpad). Also S8-1280-2.png not opened: it holds one block seen at 390 px.
- Measured at both widths: no formula wider than its card, no page overflow, no KaTeX error, no raw LaTeX; no row starts inside a number, a power of ten or a unit.
- Reflow: L2-04, L2-06, L3-01, L3-02, L3-04, L3-05 at both widths.
- New exercise fy7-8-L2-10 in full at 390 px (N8-390-1/2.png) and 1280 px (N8-1280-1.png): source line (Fingrid link, language note, reading date), parts a)–d), answer box, every solution step. Typography and English are sound; $P_\text{h}$ follows the chapter's notation.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 5
