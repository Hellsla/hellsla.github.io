VERDICT: FAIL
CONTENT-HASH: 570b93738d02c5c4

## Blocking
- [Major] solutions.md:304 (teacher's "Hyväksytään myös", k5, page-390-35 / contact-3 #36) — the inline chain `24 000 kg · 0,90 m/s : 0,80 s = 27 kN` runs past the right edge of its card at 390 px and the unit is cut to "27 kI" — a clipped formula (the unit is essential) breaks the "no clipped formula" rule — put the calculation in a form the page can break (shorter chain, e.g. `\Delta p = \ldots = 21\,600\,\text{N}\cdot\text{s}`, then `F = \ldots = 27\,\text{kN}` as two chains) or let the shared component wrap it; run `check_layout.py FY4-koe --width 360`.

## Polish
- [Minor] top-1280 / top-390 — "120 p:n" and "70 p." break across lines ("120 / p:n", "70 / p.") — use a non-breaking space between number and p.
- [Minor] fy4-k1-graphs — panels A–D have no scales; fine for a shape question, axes are labelled.
- [Minor] fy4-k6-graph — the "+" and "−" area marks are thin and easy to miss — a heavier stroke.
- [Minor] fy4-k1-fbd panel B — the F label sits close to the v arrow — move it slightly.

## Checked
- contact-1, contact-3, contact-4; top-390, top-1280; page-390-35 at full size.
- Figures fig-1 (k1-graphs), fig-3 (k1-fbd), fig-6 (k1-impulse), fig-11 (k2-graph), fig-13 (k3-fbd), fig-15 (k6-graph), fig-17 (k7-pulse) at 390 px: quantities and units on axes, data points vs fitted lines, force red / velocity blue / acceleration orange, vectors with overlines. fig-2 and the other small captures are icons only.
- Term change liikekitka → liukukitka / lähtökitka read in tasks and solutions: consistent (k3, k4, k1-f, k1-e); lepokitka kept for the body at rest; no "liikekitka" left in the visible text.
- Not opened individually: the remaining 390 px page parts and the 1280 page parts (seen only through the contact sheets).

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
