VERDICT: FAIL
CONTENT-HASH: c5fcfaa69dd7bb45

## Blocking
- [Major] exercises/solutions.md Sijoitus of fy5-6-L1-01, L1-03, L1-05, L1-07, L1-10, L1-11, L2-01, L2-02, L2-04, L3-01 ($\gamma M T^2$) and L3-03, captures fy5-6-open-exercises-1280-1 and my 390 px captures — the row break falls inside a quantity: row 1 ends with the mantissa ("$\cdot\ 5{,}97$", "$\cdot\ 7{,}35$", "$\cdot\ 6{,}42$", "$\cdot\ 1{,}90$", "$\cdot\ 1{,}99$", "$\cdot\ 7{,}346$") and row 2 starts "$\cdot\ 10^{24}\,\text{kg}$", at 390 px and at 1280 px alike, where the whole row would fit the 576 px card — the mass is cut between mantissa and power of ten in eleven solutions, so the mantissa reads as a factor of its own; a chain breaks only before a relation, a sign or a whole quantity — break before the mass, as L1-09's solution already does: `\gamma M &= 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} \\ &\cdot 5{,}97 \cdot 10^{24}\,\text{kg} \\ &= 3{,}984 \cdot 10^{14}\,\text{m}^3/\text{s}^2`; L3-01: `… \\ &\cdot 6{,}42 \cdot 10^{23}\,\text{kg} \cdot (88\,620\,\text{s})^2 \\ &= …` (same numbers and order; each row fits 360 px).

## Polish
- [Minor] the same chains at 1280 px — the wide form also joins the result onto the continuation row ("$\cdot\ 10^{24}\,\text{kg} = 3{,}984 \cdot 10^{14}\,\text{m}^3/\text{s}^2,$"), so its = is outside the column — shared component (`mathlayout.py` wide form): join a `\cdot` row to the row above, keep every = row on its own; then the wide screen shows $\gamma M = \ldots \cdot 5{,}97 \cdot 10^{24}\,\text{kg}$ on one row.

## Checked
- Delta round 1 (work queue 5d, reflow): all sixteen changed formulas. Official capture opened: fy5-6-open-exercises-1280-1 (task 6-1). The official set has no opened solutions at 390 px, so I captured the built preview with every solution open at 390 and 1280 px and measured at 360 px (scratchpad vis456/sheet-fy5-6-X-390-1.png, -390-2.png, sheet-fy5-6-X-1280-2.png).
- Nothing clipped or scrolled at 360, 390 or 1280 px; boxes inside their cards; "joten" on its own line between the boxes, trailing commas with the formulas.
- Järkevyys formulas fine: L1-07 "$7{,}66\,\text{km/s} \cdot \sqrt{\tfrac{318}{62}} \approx 17\,\text{km/s}.$", L1-11 "$1{,}62\,\text{m/s}^2 \cdot 0{,}891 = 1{,}44\,\text{m/s}^2,$", L3-01 "$42\,164\,\text{km} \cdot \sqrt[3]{0{,}107}$ / $\approx 20\,000\,\text{km},$", L3-04 "$1{,}588 \cdot 10^{30}\,\text{kg} : 1{,}99 \cdot 10^{30}\,\text{kg}$ / $\approx 0{,}80$" (≈ on its own row on a phone, one row wide).

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
