VERDICT: FAIL
CONTENT-HASH: c8723da10d15d450

## Blocking
- [Major] assets/sims/fy1/fy1-5/sim.js (sim-390, sim-1280) and inquiry.json `howto` — the replay-pace select is now labelled "Speed", the same word as the physics slider "Speed v = 2,0 m/s". On the same control row a student cannot tell which one changes the trolley's speed. The howto sentence "*Speed* changes only the pace of the replay" is then ambiguous too. At 1280 px the select also shows only "normal", with no visible label beside it. — The two controls mean different things (the quantity v against the playback pace), and the lesson is about v. — Give the select a distinct word, for example "Playback" or "Pace" (it must not read "Speed"), and use the same word in the `howto`. Keep the interface text short.

## Polish
- [Minor] sim-390 — the "Moment t" slider and the select sit on one row, so the slider is short (about half width). Acceptable, but the select could go on the row of the Start and Reset buttons.
- [Minor] sim.js — the legend note (flag, arrow, dots) was removed from the page. `howto` still explains the flag, arrow and marks, so nothing essential is lost.

## Checked
- fy1-5-sim-390.png and fy1-5-sim-1280.png: controls, readout and labels. The canvas labels render as LaTeX, with no clipping or overflow. The removed note leaves no gap.
- fy1-5-top-390.png and fy1-5-intro-1280.png: the new hero picture (Voyager 2 and the planets). It is a clear flat illustration, the subject sits in the middle third, and it has no text or clutter.
- fy1-5-fig-2-390.png: the motion diagram (fy1-5-motion.webp, the changed picture). Five trolleys, equal Δs brackets, blue velocity arrow, LaTeX labels, legible at 390 px.
- The text of inquiry.json: only the control name changed. The LaTeX is intact.

## Scores
illustrations 5 · typography 5 · Finnish (English prose) 4 · accessibility 4
