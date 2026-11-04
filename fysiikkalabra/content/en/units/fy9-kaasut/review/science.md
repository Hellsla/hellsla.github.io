VERDICT: PASS
CONTENT-HASH: 97b2ac678f09a7f6

Science review (round 3) of the en translation of fy9-kaasut. Source: content/fi/units/fy9-kaasut/.

## Blocking
None.

## Polish
None open.

## Round-2 findings
1. Concept-map headings in Finnish: fixed. figlib.translate() now also handles \textbf{}, and the en concept map draws **liquid**, **gas** and **heat engine** from figures.json.
2. $P_\text{l}$ (s2 c): fixed in this round. Renamed to $P_\text{h}$ in solutions.md (Formula and Substitution lines). The Formula line now defines both symbols in words: "$P_2 = P_0 - P_\text{s}$ (heat power given away), $P_\text{h} = 0.75\,P_2$ (recovered heat power)". No new formula was added, and the numbers are unchanged (232.9 kW, η_tot = 0.840, about 84 %).

## Checked
- check_i18n: en 0 errors, fi-easy 0 errors. units.py check and practice.py check: fy9-kaasut OK (6 tasks, 95 points) in fi, en and fi-easy.
- The redrawn figures keep every number and formula of the source: tyre bars 331 / 286 kPa, Δp = 230 / 185, p0; heat engine Q1 = 1000 J, W = 350 J, Q2 = 650 J; syringe graph k ≈ 0.135 ml/°C, (0; 37.7), (80; 48.5); θ0 ≈ −279 °C, extreme lines −265 and −294 °C; T = θ + 273.15 K.
- Decimal points everywhere. No regression in answers, tolerances or formulas.
