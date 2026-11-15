VERDICT: PASS
CONTENT-HASH: 6a32e9655e538bee

## Blocking

## Polish
- solutions.md:150 (fy6-1-L2-06 b) — the model answer says "No current flows through the lamp", but the Principle line above it says "almost all of the current flows through the wire" (C-level simplification, slightly inconsistent) — write "practically no current flows through the lamp".
- solutions.md:9 (fy6-1-L1-01 Reasonableness) — the comparison $21\,\text{W} : 12\,\text{V}$ uses $P = UI$, which this chapter does not teach yet (power comes later in FY6) — compare with a current instead, or say only that the order of magnitude is that of a car bulb.
- exercises/review/packet-science.md — the exercise brief is empty (the English lesson's sections were not picked up), so notation could be compared only with the glossary and the solutions themselves — check the packet tool for the en lesson headings.
- lessons/FY6/fy6-1/figures.py kaavio_malli — the labels `\text{kytkin}`, `\text{lamppu}` are Finnish; check that the English model figure shows "switch" and "lamp" (visual reviewer's call).

## Checked
- All 16 numeric answers recomputed in one script with my own formulas (I = Q/t, U = E/Q, N = It/e, trapezoid sum, graph areas, Wh sums, v = I/(ne)): all agree with exercises.json and answers.py.
- L3-05 b: $t = 5.21 \cdot 10^{4}\,\text{s} = 14.5\,\text{h}$; L3-04: $Q = 3.35\,\text{Ah}$, $U_\text{avg} = 3.73\,\text{V}$, estimate $7.2\,\%$ too large: correct.
- L2-07 averages $0.310\,\text{A}$ / $0.306\,\text{A}$; resolution (not uncertainty) used correctly per guardrails.
- Rounding: every 2-s.f. student answer (23 C, 1.1·10² C, 40 kJ, 1.0·10¹⁸, 9.4·10¹⁹) stays within the 2 % tolerance; L3-04's 3 s.f. justified by the decimal-place rule for sums.
- Choice tasks L1-06, L1-07: exactly one correct option, every distractor really wrong and its feedback right; L1-09 truth values 1F 2T 3T 4F 5F verified ($18\,\text{C}$, $54\,\text{J}$), condition (no wire/battery resistance) stated.
- Conventional current + to −, electrons opposite; current not used up; signal vs drift explained without "speed of light" error.
- Figures virta-kuvaaja and lataus-kuvaaja: plotted values match the solutions' readings (11 C, 35 C); alt texts give the same data.
- Model figure kaavio-malli: cells in series (− of upper to + of lower), + at top, current arrow rightwards from + along the top edge: consistent with the model answer.
- Scope: DC current and voltage only; Ah/mAh defined in the task; short circuit safety noted.
- Magnitudes realistic (phone battery 12.5 Wh, drift 0.019 mm/s, 40 kJ ≈ 40 kg lifted 100 m).
