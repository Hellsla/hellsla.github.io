VERDICT: FAIL
CONTENT-HASH: f775c61f5a128688

## Blocking
- [Major] Koe 1 and Koe 2 "Alkutila" lines (inquiry.json koe-1/koe-2 units; built by scripts/inquiry.py), 390 and 1280 px — the start state prints "vauhti v = 110⁶ m/s": value 1 and the plain-text unit "10⁶ m/s" run together and read as 110⁶ — a student reads a wrong speed (about 100 times too large) where the sim shows 1,0 · 10⁶ m/s; the unit is also plain text (standing rule: quantity as one formula) — render the value and unit as one formula, "$1{,}0 \cdot 10^{6}\,\text{m/s}$" (units.v as "\cdot 10^{6}\,\text{m/s}" with a thin space, or a build-time conversion); same for the "10⁻¹⁴ N" units in the Koe 2 table headers and the answer-field units where they appear. Also B shows "0,2 T" and "0,15 T" against 0,20 T in the text: keep the sig figs.

## Polish
- [Minor] fig r-graph (fig-10-390) — the proton line runs through the label "protoni" (rule: a line never runs over a label) — move the label above the line or to its end.
- [Minor] lesson.md display of r (qvB = mv²/r, r = mv/(qB)) — the two fractions nearly touch between the rows; cramped — more row spacing (\\[6pt]).
- [Minor] fig spectrometer (fig-12-390) — "raskaampi" label straddles the chamber edge and covers a field dot; lighter path unlabelled — put the label outside the chamber and add "kevyempi".
- [Minor] sim canvas (sim-390/1280) — the F_m label at the slit overlaps a B dot and the arrow tip, unreadable at 390 px — offset the label.
- [Minor] fig track-sign (fig-20) — the dashed track runs through a × symbol; leave clear space.

## Checked
- contact-1, contact-2; fig-6 (force-dir), fig-8 (circle-path), fig-10 (r-graph), fig-12 (spectrometer), fig-20 (track-sign) at 390 px; hero (top/intro-1280). Force directions verified against the right-hand rule as drawn: all consistent.
- sim-390, sim-1280, exp-koe-2-390 (1 and 2), lab-1280-1, example-390-2, stage-sovella-390-1.
- theory-1280-1, -2, -3; open-tarkista-1280-1.
- Source text of lesson, inquiry, exit ticket read for language and notation.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
