VERDICT: FAIL
CONTENT-HASH: c64883a8ea9fcc46

## Blocking
- [Major] exercises/solutions.md `akselit 180` (fy5-4-L3-01 and the other voimakuvio blocks with `akselit 180`, lines 62, 120, 139, 158; capture open-exercises-L3-1280-1) — the axis glyph draws x to the left but y pointing DOWN (y = x+90° in fbdspec.py), while the same solution says "x kohti keskipistettä ja y ylös", and the lesson's worked-example figure draws y up — a figure that contradicts its own text and the example teaches the wrong sign convention — make the renderer/spec draw y up for `akselit 180` (x left, y up), or reword every such text; do not leave figure and text in conflict.
- [Major] inquiry.json names.m (exp-1 line 151, exp-2 line 230) — "massa m" is plain text; the generated Alkutila line shows "massa m = 1500 kg" in sans plain text next to maths "r = 50 m" (capture lab-1280) — a plain symbol and plain quantity where the student looks (NOTES §1, blocking) — write "massa $m$".
- [Major] simulation card at 1280 px (sim-1280, lab-1280) — the last line of the legend ("Punaiset nuolet ovat voimia, sininen nuoli nopeus ja oranssi kiihtyvyys.") is cut in half at the card's bottom edge; at 390 px it is whole — the colour legend is clipped — let the card grow to its content (no fixed height).

## Polish
- [Minor] sim canvas force diagram (sim-390, sim-1280) — acceleration labelled $\overline{a}$ without the subscript n, the lesson figures and solutions use $\overline{a}_\text{n}$ — use $\overline{a}_\text{n}$.
- [Minor] sim-1280 controls — the Ratanopeus slider sits beside the buttons and Säde on the next row, a ragged control grid — align the sliders in their own row.
- [Minor] fig-10 / nyppyla, hump panel (fig-10-390) — the $\overline{a}_\text{n}$ arrow hangs below the ground line beside the body and the $\overline{N}$ label touches the car rectangle; same N-label contact in fig-12 and fig-13 — nudge labels 6–8 px outwards.
- [Minor] exercise figures fig-12..16 — the centripetal-force arrow is labelled $\overline{F}_\text{kp}$ with a non-glossary abbreviation; fine as the deliberate error, but name it in the description as "keskeisvoima" (for science: check the Etsi virhe figure's description gives nothing away).

## Checked
- Contact sheets 1 and 3; fig-1 (hero), fig-7 (muutos), fig-8 (kaarre), fig-9 (kuvaaja), fig-10 (nyppyla), fig-12 to fig-14 (task figures), fig-row-1280, example-390-1/2.
- top-390, intro-1280, theory-1280-2, sim-390, sim-1280, lab-1280, open-ennusta-1280.
- open-exercises-1280-1, L2-1280-3, L3-1280-1, L3-1280-4.
- Not opened separately: fig-15/16 (seen on contact sheet only), exit-ticket and stage captures.
- Figures 1, 7, 8, 9, 10 and the example read well at 390 px: vectors, colours (v blue, a orange, F red) and the graph (units, ticks, dashed r=100 m) are consistent; G/N lengths in hump and dip are right.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
