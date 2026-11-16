VERDICT: PASS
CONTENT-HASH: 0270a6cef047d7a4

## Blocking

## Polish
- [Minor] wide screens, inquiry.json etsi-virhe prompt, kuukoe Järkevyys, exit-ticket.json answer 1 — at 1280 px the page's wide form joins the result onto the continuation row ("$\cdot\ \tfrac{5{,}97 \cdot 10^{24}\,\text{kg}}{(3{,}0 \cdot 10^{5}\,\text{m})^2} \approx 4400\,\text{m/s}^2$"), so the final ≈ is not in the column of the other relations although the whole substitution would fit on one row — shared component (`mathlayout.py` wide form): join a row that starts with `\cdot` to the row above and keep every =/≈ row on its own; no content change needed.
- [Minor] same three formulas — they are display maths now but keep `\tfrac`, so the fractions are script size and their exponents ($10^{24}$, $10^{5}$) about 10 px on a phone; in etsi-virhe the exponent of $3{,}0 \cdot 10^{5}\,\text{m}$ is what the student must spot — `\dfrac` for the substitution fraction in these display blocks (the unit fraction of $\gamma$ may stay small).

## Checked
- Delta round 1 (work queue 5d, reflow): the three lifted chains. Official captures opened: fy5-5-open-exit-1280 (exit answer 1). The kuukoe solution and the 390 px opened states are not in the official set, so I captured the built preview with `?ratkaisut=1` at 390 and 1280 px and measured at 360 px (scratchpad vis456/sheet-fy5-5-L-390-1.png, sheet-fy5-5-L-1280-1.png).
- 390 px: each block is rows starting with =, ≈ or a · before a whole quantity; relations in one column; nothing clipped or scrolled, boxes inside their cards; the sentence's full stop sits inside the formula, and "Mikä ratkaisussa on vialla?" follows as its own line.
- 1280 px: readable, inside the 38rem column; the joined result row is the Polish item above.
- Answer options of etsi-virhe and the surrounding cards unchanged in layout. Formula names are a teacher-approved category; not re-judged.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
