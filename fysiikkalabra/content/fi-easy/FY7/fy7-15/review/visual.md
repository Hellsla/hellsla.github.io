VERDICT: FAIL
CONTENT-HASH: 800d0f7d6f1757aa

## Blocking
- Block 3 (Malus: I = I0 cos² θ = 50 W/m²): the answer's calculation chain is an unbroken inline formula wider than the box, cut off at the right edge and reachable only by scrolling sideways (checked at 360 and 390 px, answer open); the page's chain-to-rows layout (scripts/mathlayout.py) is not applied inside the Pysähdy ja mieti answer. Fix in the shared component (stopthink.py/build.py), not by splitting the chain in the lesson. In this lesson the block sits inside a closed optional box (column 308 px at 390 px, 304 px of text), so the clip is worse.

## Polish
- Block 3 sits inside the closed optional box (Malusin lain tutkiminen), so a student sees it only after opening it; consider moving it out (pedagogy's call).

## Checked
- batch delta review: all 3 new "Pysähdy ja mieti" blocks of fy7-15 (fi-easy) rendered from the built page and photographed with the answer open at 390 px (all) and 360 px and 1280 px (overflow and KaTeX error measurement); label, question, Vastaus summary, spacing, placement beside figures/headings, maths typography ({,}, units, \tfrac, \cdot, colon division) and Finnish read. Listed older captures not reopened (unchanged old content, taken before the blocks existed). No page-level overflow, no red KaTeX source.
