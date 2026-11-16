VERDICT: PASS
CONTENT-HASH: f368ccd18e65ea2e

## Blocking
None.

## Polish
- [Minor] figures.json — it holds translation entries for two "Kuvaaja mittakaavassa …" variants (a_n up to 12, F up to 25 m/s). No figure in the current lesson uses them. They are harmless, but remove them if they are orphans.

## Checked (delta 2026-11-15, work queue 8m)
- Delta review of the diff: the sim readout and its text changed from "suurin lepokitka" to "lähtökitka", the Koe 1 intro and its minimum measurement count (4 → 6), the table header "lähtökitka (N)", and the feedback, hints and model texts.
- Opened fy5-4-sim-390.png and fy5-4-sim-1280.png (fy5-4-lab-1280.png at 1280 px): the readout "tarvittava kitka …, lähtökitka …" reads cleanly in KaTeX and wraps without clipping at 390 px.
- Opened fy5-4-exp-exp-1-390-1.png and -2.png, and lab-1280: the new intro text reads cleanly in KaTeX. The table header "lähtö-kitka (N)" breaks at the syllable, and the table is not clipped at 390 or 1280 px.
- Opened fy5-4-fig-15-390.png (the graph): the live aria-label matches the drawing (values 2, 8, 18; both radii; points at 10 and 20).
- Not opened: the other figures, whose diff was a description string only, and the exercise captures.

(Report text of the visual-editorial-reviewer run, saved by the orchestrator because the agent's report did not reach the file.)

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
