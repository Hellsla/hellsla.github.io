VERDICT: PASS
CONTENT-HASH: b9d35043f608c48a

## Blocking

## Polish
- sim.js:68,108 — in case 1 the "vesi" label shows only the original water until the last ice melts, then drops to T_f in one frame: 31,9 → 23,9 °C at 60 °C, and 7,4 → 6,2 °C in the worked example. The water colour keeps following TW for another 5 s. A stirred liquid is at m_v·T_W/(m_v + m_sulanut) the whole time (the melt water is at 0 °C), and that reaches T_f smoothly. — Use that weighted value for the label, and for the colour, whenever liquid is present.
- tests/sims/fy3-14.json (case-3 readout assertion) — after the rewrite this test checks only the substring "jäätä jäljellä". The displayed values T = 0,0 °C and 588,0 g are not asserted. — Add `x.includes('T = 0,0 °C') && x.includes('jäätä jäljellä 588,0 g')`.
- sim-spec.md — still describes "yhden rivin selitys, mikä kolmesta tilanteesta toteutuu" under the canvas. That line has been removed, and the model has four cases. — Update the spec.
- inquiry.json:siirto solution — the substitution `\dfrac{4190 \cdot 0{,}25 \cdot 14}{334\,000 + 4190 \cdot 8{,}0}\,\text{kg}` has no units on its values. Hint 3 leaves "J/kg" outside the LaTeX. — Write the units inside the LaTeX.

## Checked
- Hash b9d35043f608c48a, the same at start and end. All 12 answers recomputed in one script. They equal answers.py and are within tolerance.
- Every inquiry, figure, exit-ticket and example number recomputed: 24,7/75,3 g, 26,6 °C, 12,6 g, 6,05 °C, −26 °C, 39,9/43,9/438 g, 40/56 °C, 12,5 g.
- Round-2 fixes are in. The exit-ticket calculations are LaTeX with units. Example stage 2 has a substitution row with units. The koe-1 prompt says to bracket and then calculate (26,5 °C → 0,3 g of ice, 27 °C → 0,32 °C).
- Sim re-run in Chromium for cases 1 (60 °C and 30 °C), 2, 3 and 4 and the example. End states equal my solver: 23,8; 2,6; 0/24,7 g; 0/588,0 g; −3,5 °C/600 g; 6,0 °C. q/Q_end = 1. The end label equals T_f because mixing conserves energy.
- In case 4 the cubes vanish once the water has frozen. The labels read "vesi: jäätyi" and "jää −3,5 °C".
- "tests-weakened" judged: coverage held. The cases 1, 2 and 4 rewrites keep every displayed number (T, ice left, kJ). The removed prose (case sentence, 75,3 g, 88,0 g) is no longer displayed, and simState now asserts it (tapaus, meltedG). The thermometer values moved to the canvas, and the exact label strings are asserted. Case 3 is slightly thinner (see Polish).
- The howto now matches what the sim shows: thermometer "jäätyi"/"ei jäljellä", the mixed temperature, and the four cases.
- Figures 1–3 are unchanged: numbers to scale and every label in LaTeX. No lesson id appears in the page's visible text.
- Formulas, branch conditions and FY3 scope are unchanged and correct.
