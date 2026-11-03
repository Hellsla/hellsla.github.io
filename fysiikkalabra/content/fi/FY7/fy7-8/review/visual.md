VERDICT: FAIL
CONTENT-HASH: aa93c04b647589b2

## Blocking
- [Major] grid figure (lesson.md:154–197, fig-7-390 and theory-1280-2) — the vertical line from the dashed "sähköasema" box runs straight through the label "sähköasema" (between "ö" and "a"); a crossed word in a print-quality diagram, and the layout checker does not catch line-over-label — move the label left of the line (e.g. right-aligned, ending before the line) or shift the line.  It is a one-line fix and is the only blocker.

## Polish
- [Minor] grid figure — it shows the whole chain down to the $230\,\text{V}$ home, but sits after "Siirtohäviö ja suurjännite"; the text explaining the steps (110 kV, 20 kV, 230 V) comes only in the next subsection, and the figure leaves out the 110 kV alueverkko step the text names. Move it after "Jännite lasketaan vaiheittain" or add the step. Also the power-station icon (house with a dial) is hard to read as a plant.
- [Minor] lesson.md "Teho säilyy, virta muuttuu" — "se vaihtaa suuren virran suureksi jännitteeksi tai päinvastoin" is ambiguous; "se muuttaa suuren virran ja pienen jännitteen pieneksi virraksi ja suureksi jännitteeksi tai päinvastoin."
- [Minor] sim table header and koe-1 (lab-1280) — "P_h (MW)" has italic subscript h but the lesson writes $P_\text{h}$; "osuus (%)" is plain text. Align to `P_\text{h}`.
- [Minor] exit ticket 1 — "U₂ = U₁N₂ : N₁ = 230 V · 25 : 500" mixes · and : in one line; read left to right it is correct but a fraction in the formula line would be clearer.
- [Minor] Alkutila line in koe-1 — "siirtojännite = 100 kV" with plain "=" (generated).

## Checked
- contact-2; top and sim-390, sim-1280/lab-1280, example-390-1/2, open-ennusta-1280-1, open-tarkista-1280-1, open-exit-1280, theory-1280-1/2/3
- figures: hero (fig-2), transformer (fig-5; geometry, turns 7:4 match the step-down text), grid (fig-7, zoomed), loss-graph (fig-9; 12 %, 3,0 %, 0,75 % check against RP/U²), scene (fig-11)
- Finnish text read in full; maths renders without red source, chains aligned, decimal comma and units correct.

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 5
