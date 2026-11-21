VERDICT: FAIL
CONTENT-HASH: c44af12a9e3f76c8

## Blocking
- Block 1 (langaton laturi) is garbled Finnish: "Puhelin nostetaan langattoman laturin päältä $3\,\text{mm}$:n korkeudelle $20\,\text{mm}$:n korkeudelle." says "to a height of 3 mm to a height of 20 mm"; the start height must be "korkeudelta" ("…päältä 3 mm:n korkeudelta 20 mm:n korkeudelle"). Fix the sentence in the lesson.
- Block 3 (A = aL = 9,0 dB): the answer's calculation chain is an unbroken inline formula wider than the box, cut off at the right edge and reachable only by scrolling sideways (checked at 360 and 390 px, answer open); the page's chain-to-rows layout (scripts/mathlayout.py) is not applied inside the Pysähdy ja mieti answer. Fix in the shared component (stopthink.py/build.py), not by splitting the chain in the lesson.

## Polish
(none)

## Checked
- batch delta review: all 3 new "Pysähdy ja mieti" blocks of fy7-16 (fi-easy) rendered from the built page and photographed with the answer open at 390 px (all) and 360 px and 1280 px (overflow and KaTeX error measurement); label, question, Vastaus summary, spacing, placement beside figures/headings, maths typography ({,}, units, \tfrac, \cdot, colon division) and Finnish read. Listed older captures not reopened (unchanged old content, taken before the blocks existed). No page-level overflow, no red KaTeX source.
