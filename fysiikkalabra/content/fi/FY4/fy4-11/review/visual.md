VERDICT: PASS
CONTENT-HASH: de63a4dbeb2629d3

## Blocking

## Polish
- [Minor] inquiry.json exp-3 (Koe 3: keli) — after *Aseta alkutila* the sim card reads "Käytössä:" with no experiment name (Koe 1 and 2 show theirs; reproduced in a browser at 390 px) — the label probably looks for a title that an optional experiment keeps in its summary; fill it with "Koe 3: keli" (template/inquiry.js, not this text).
- [Minor] figure tormays (fig-4) — the white box behind "vyössä: Δt = 0,10 s" cuts a visible gap in the blue line just above it, and the ticks mix precision ($0{,}1$ among $0{,}02$ … $0{,}12$; same in tF) — move the label a few px left/down clear of the line; write the tick $0{,}10$ in both graphs.
- [Minor] figure tF (fig-6) — the force bars are blue and orange-brown, the FY4 colours of velocity and acceleration; the labels say what they are, so nothing is misread, but a force graph in force-red shades (two tints) would keep the colour code — optional.
- [Minor] lesson.md Esimerkki, Sijoitus — first row writes the unit as $\tfrac{\text{m}}{\text{s}}$, every other row and the text $\text{m/s}$; write `22{,}22\,\text{m/s} \cdot 2{,}0\,\text{s}`.
- [Minor] lines breaking at the wrong place at 390 px: "$(t,v)$ / -kuvaajan" in the Esimerkki Periaate step (line starts with the hyphen), and the sim readout's "…, $s_\text{p} = \dots\,\text{m}$ / $, t_\text{p}$" (line starts with a comma) — keep the hyphen/comma glued to the maths (no-break), as elsewhere on the page.

## Checked
- Contact sheets 1–6; full size: top-390, intro (contact), fig-1…fig-6-390, theory-1280-1…4, sim-390, sim-1280, lab-1280-1/2, stage-tutki-390-1, exp-exp-3-390-1/2, example-390, open-tarkista-1280-2.
- stage-tutki-390-1 showed a garbled canvas (labels on top of each other); re-captured the Tutki sim at 390 px myself and it renders correctly — capture artefact, not a finding.
- example-390 shows only Vaihe 1/7 (the "Näytä kaikki" click did not take in screenshot.py); made my own capture with every step revealed: aligned chain, phantom columns and Järkevyys render cleanly.
- sim-1280 / lab-1280 bottom cut-off is the sticky `.lab-side` scroll panel (site.css), by design.
- Hero: moose, sign and car read at 390 px; jarrutus: $\overline{v}$ blue, $\overline{a}$ orange, forces red, $\overline{N}$ and $\overline{G}$ equal; pysahtyminen to scale, labels clear.
- Prose for plain number+unit quantities: none found (the OTI counts 278/198/114 are bare counts).

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
