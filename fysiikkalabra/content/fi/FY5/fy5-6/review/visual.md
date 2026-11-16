VERDICT: FAIL
CONTENT-HASH: 20dc116bb33511df

## Blocking
- [Major] inquiry.json koe-1 solution, virhe prompt (Esimerkit, "Missä on virhe?") and siirto solution, the $\gamma M$ chain — the row break falls inside a quantity: row 1 ends "$\cdot\ 5{,}97$", row 2 starts "$\cdot\ 10^{24}\,\text{kg}$" (in virhe "$\cdot\ 10^{24}\,\text{m}^3/\text{s}^2$"), at 390 px and at 1280 px alike, where the row would fit whole — the Earth's mass $5{,}97 \cdot 10^{24}\,\text{kg}$ is cut between mantissa and power of ten, so $5{,}97$ reads as a separate factor; in an error-hunting task an odd-looking line is itself a distraction — break before the whole quantity: `\gamma M &= 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} \\ &\cdot 5{,}97 \cdot 10^{24}\,\text{kg} \\ &= 3{,}984 \cdot 10^{14}\,\text{m}^3/\text{s}^2`; in virhe `\gamma M &= 6{,}674 \cdot 10^{-11} \\ &\cdot 5{,}97 \cdot 10^{24}\,\text{m}^3/\text{s}^2 \\ &= …` (same numbers and order; each row fits 360 px).

## Polish
- [Minor] tarkistus-2 solution, $\gamma T^2$ at 1280 px — the wide form joins the result onto the continuation row ("$\cdot\ (27\,540\,\text{s})^2 = 5{,}0619 \cdot 10^{-2}\,\tfrac{\text{m}^3}{\text{kg}},$"), so its = is outside the column — shared component (`mathlayout.py` wide form): join a `\cdot` row to the row above, keep every = row on its own.

## Checked
- Delta round 1 (work queue 5d, reflow): the five changed places. The 390 px opened states are not in the official set, so I captured the built preview with `?ratkaisut=1` at 390 and 1280 px and measured at 360 px (scratchpad vis456/sheet-fy5-6-L-390-1.png, sheet-fy5-6-L-1280-1.png): virhe prompt, siirto Sijoitus, tarkistus-2 Sijoitus, data Järkevyys.
- koe-1's solution would not open in my capture; its built markup is the same formula with the same row breaks as siirto's, which I saw rendered.
- data Järkevyys: "$26\,560\,\text{km} : 6790\,\text{km}$ $\approx 3{,}9$" wraps before ≈ on a phone, one row at 1280 px; fine.
- tarkistus-2 at 390 px: rows start with · before a whole quantity and with =; fine. Nothing clipped or scrolled anywhere; boxes inside their cards; trailing commas stay with the formulas, "joten" follows on its own line.
- Figures are a teacher-approved category; not re-judged.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
