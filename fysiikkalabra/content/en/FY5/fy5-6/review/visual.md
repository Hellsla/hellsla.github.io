VERDICT: PASS
CONTENT-HASH: e0c6a4f464dbb877

## Blocking
(none)

## Polish
- [Minor] cannon figure legend "circular" (for "ympyrärata") — "circular orbit" does not fit the 156-unit legend column at 24 px; "circular" reads correctly beside "too slow"/"too fast" and the figure text says "circular-orbit speed" — keep.
- [Minor] sim readout at 390 px wraps ", time t" onto a new line starting with a comma — same wrapping as the Finnish; leave.

## Checked
- Delta (coordinator fix, hash 74bd28343cb1ef34 -> e0c6a4f464dbb877): the only change is inquiry.json reveal.pending (after teoria-paino), Finnish "Palaute avautuu, kun olet lukenut kohdan Painottomuus." -> "Feedback opens when you have read the section Weightlessness."; rebuilt preview/en/fy5-6.html shows it, and it matches the theory heading "Weightlessness" on the page. No other file changed.
- Delta after the sim fix (sim.js line 199 now __('akseli_kulma'), lang/en.json "$\text{angle}\ ({}^\circ)$"): retaken sim-390 and sim-1280 show "angle (°)" under the graph, centred, no clipping; no Finnish left on the English page.
- Captures opened: sim-390, sim-1280, fig-6-390, fig-7-390, fig-11-390 (after the fix), fig-12-390, theory-1280-1, open-tarkista-1280-2.
- Sim labels fit at 390 and 1280 px: Launch/Reset, "Launch speed v = 7.00 km/s", "400 km (like the ISS)", "Mass of the satellite", "Speed", legend and readout; no clipping.
- Figure labels English and LaTeX: Earth, without gravity, only force, towards the / Earth's centre (two lines fit the right column), too slow/circular/too fast, geostationary, orbit of the Earth, orbit of Halley's comet, million km, comet, Sun.
- Fixed here: weightlessness figure heading "At the surface of the Earth" -> "on the Earth's surface" (parallel with "on a space station", shorter) in figures.json, redrawn with figures.py --lang en.
- Mars answer and solution use LaTeX powers of ten; decimal point throughout; check_layout 345 px OK; check_i18n no fy5-6 line.

## Scores
illustrations 4 · typography 4 · Finnish (English) 4 · accessibility 4
