VERDICT: FAIL
CONTENT-HASH: 75f5c6500e5d4581

## Blocking
- [Major] exercises/solutions.md fy5-5-L2-03 (task 5-12) Sijoitus, captures fy5-5-open-exercises-L2-1280-4 and my 390 px capture — the row break falls inside a quantity: row 1 ends "$\cdot\ 5{,}97$" and row 2 starts "$\cdot\ 10^{24}\,\text{kg} \cdot 1200\,\text{kg}$", at 390 px and at 1280 px alike (where the row would fit whole) — the mantissa reads as a factor of its own and the Earth's mass $5{,}97 \cdot 10^{24}\,\text{kg}$ is no longer one value; a chain may break only before a relation, a sign or a whole quantity — break before the mass: `\gamma M m &= 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} \\ &\cdot 5{,}97 \cdot 10^{24}\,\text{kg} \cdot 1200\,\text{kg} \\ &= 4{,}7812 \cdot 10^{17}\,\text{N}\cdot\text{m}^2` (same numbers and order; both rows fit 360 px).

## Polish
- [Minor] wide screens, L1-01, L1-02, L1-03, L1-04, L3-03 Sijoitus — at 1280 px the wide form joins the first result onto the continuation row ("$\cdot\ \tfrac{70\,\text{kg} \cdot 55\,\text{kg}}{(0{,}80\,\text{m})^2} = 4{,}015 \cdot 10^{-7}\,\text{N}$"), so that = is outside the column of the others although the whole substitution fits one row of the 576 px card — shared component (`mathlayout.py` wide form): join a `\cdot` row to the row above, keep every =/≈ row on its own.

## Checked
- Delta round 1 (work queue 5d, reflow): all eleven changed formulas (L1-01–L1-04, L2-02, L2-03 twice, L2-09, L3-03, L3-05 Järkevyys). Official capture opened: fy5-5-open-exercises-L2-1280-4. The official set has no opened solutions at 390 px, so I captured the built preview with every solution open at 390 and 1280 px and measured at 360 px (scratchpad vis456/sheet-fy5-5-X-390-1.png, sheet-fy5-5-X-1280-1.png).
- 390 px: nothing clipped or scrolled; rows start with =, ≈ or · before a whole quantity, except L2-03 above. Fractions `\dfrac`, legible.
- Short Järkevyys formulas on their own row ("$1200\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \approx 11{,}8\,\text{kN}.$", "$850\,\text{kg}\cdot 24{,}8\,\text{m/s}^2 = 21{,}1\,\text{kN}$ … ja", "$16 \cdot 0{,}0337\,\text{m/s}^2 \approx 0{,}54\,\text{m/s}^2.$"): the sentence still reads through, punctuation stays with the formula.
- Captions without the example-data marker (teacher-approved): short, nothing stranded.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
