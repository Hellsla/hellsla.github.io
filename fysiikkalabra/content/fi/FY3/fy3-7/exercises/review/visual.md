VERDICT: PASS
CONTENT-HASH: 6adc73b630c26584
ROUND: 3

Round 3 checks the last commit (`git show HEAD -- content/fi/FY3`), which touches only fy3-7 L2-05 (tolerance and Vastaus line); the rest is covered by the round-2 PASS.

## Blocking
(none)

## Polish
- [Minor] The round-2 polish on L2-05 (tolerance accepting 312 kJ/kg) is resolved: 0,05 gives 317,3..350,7 and the Vastaus says ±5 %.
- [Minor] Stearin Mallivastaus c): "4190 · 35,0 J = 146 650 J" and "2 406 650 J" lack units on the factors (carried over, verify).
- [Minor] Data tables: header and number alignment (site-wide; carried over).
- [Minor] Answer-field wording "Vastauslaatikkoon" vs "Vastauskenttään" in fy3-4 (site-wide; carried over).

## Checked
- Diff HEAD read: one number in exercises.json (0.05) and "\pm 5\,\%" in solutions.md, valid LaTeX with the thin space as elsewhere; no layout impact. No plain-text quantity in the changed text.
- No new capture; one-character change.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
