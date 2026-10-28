VERDICT: PASS
CONTENT-HASH: 2c1918a55c16bf98

## Blocking

## Polish
- inquiry.json:simulaatio howto — the howto says "Lopputila kertoo neljästä tapauksesta yhden", but the readout shows only T and the ice left. The case has to be inferred: in case 3 the ice left is more than m_j. — Say "Lopputilasta (T ja jäljellä oleva jää) näet, mikä neljästä tapauksesta toteutuu", or show the case.
- sim-spec.md — still describes a "yhden rivin selitys, mikä kolmesta tilanteesta toteutuu" under the canvas, and an approach timescale of "noin 8 s". The sim has four cases and no case line, with τ = 1,8 s and a run of 8 s. — Update the spec.
- tests/sims/fy3-14.json (case-3 readout) — this test still checks only the substring "jäätä jäljellä". T and 588,0 g are not asserted. — Add `x.includes('$T = 0{,}0\\,{}^\\circ\\text{C}$') && x.includes('$588{,}0\\,\\text{g}$')`.
- inquiry.json:siirto solution and hint 3 — the substitution has no units inside the LaTeX ("J/kg" sits outside it in the hint). — Write the units inside the LaTeX.

## Checked
- The hash was 2c1918a55c16bf98 at both the start and the end. All 12 answers recomputed in one script with my own four-case solver. They equal answers.py and are within tolerance.
- Every inquiry, figure, exit-ticket and example number recomputed: 24,7/75,3 g, 26,6 °C (26,57), 12,6 g (5,9 → 18,5 g), 4,2/31,4 kJ, 6,05 °C, 19 °C without latent heat, −25,6 ≈ −26 °C, 39,9/43,9/438 g, 40/56/35 °C, 12,5 g, 66,8 kJ.
- Figures 2 and 3 are to scale: 6 px/kJ gives 150,8/12,6/200,4 px, the knee is at 26,57 °C = 152,8 px, and T(80 °C) = 40,07 °C. Figure 1 shows 0,375/0,025 kg.
- sim.js diff since the last PASS (129ea07): only label and readout formatting changed (fi/fk → tx/tk TeX, lab() without a halo, with an optional maxW shrink). solve(), stateAt(), the animation, the chart scaling and simState are untouched. The mixed-temperature label (TWd), a polish item from the last round, is in.
- Tests judged: each of the 8 changed assertions is a one-to-one translation of the same quantity and value into TeX via simText. No physics check was lost or loosened, and the tapaus/meltedG checks are unchanged.
- Screenshots at 390 and 1280 px: the KaTeX labels render on the canvas, and the readout reads 0,0 °C / 24,7 g / 25,1 / 0,0 / 33,4 kJ, as computed.
- Formulas, branch conditions (four cases) and FY3 scope are unchanged and correct.
