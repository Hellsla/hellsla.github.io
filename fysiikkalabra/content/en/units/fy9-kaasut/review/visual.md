VERDICT: PASS
CONTENT-HASH: 97b2ac678f09a7f6

Visual and editorial review (round 3) of the en translation of fy9-kaasut. I built preview/en/fy9-kaasut.html with `python3 scripts/build.py fy9-kaasut` and checked it in Playwright at 390 and 1280 px with every details element open. I captured and looked at all 10 figures at both widths.

## Blocking
None.

## Polish
None open.

## Round-2 findings
1. Concept map `kartta` with Finnish branch headings: fixed. It now shows **liquid**, **gas** and **heat engine**. "heat engine" fits its box at 390 px, and the rows ("work done by gas", "ideal gas law", and so on) do not overlap the formulas.
2. $P_\text{l}$ (s2 c): fixed. It is now $P_\text{h}$, defined in words in the Formula line.

## Checked
- Figures: the hero illustration, the p–T graph (A, B), the concept map, the tyre bar chart, heat-engine energy flows (hot source T1, engine, colder environment T2), the p–V graph, the syringe V–θ graph, the extrapolation graph ("extreme lines: −265 and −294 °C"), and both force diagrams ("pad"). All labels are English, they use decimal points, and they are readable at 390 px.
- scrollWidth equals the viewport at 390 and 1280 px. There are 0 KaTeX errors.
- check_i18n: en 0 errors. units.py check and practice.py check: fy9-kaasut OK.
