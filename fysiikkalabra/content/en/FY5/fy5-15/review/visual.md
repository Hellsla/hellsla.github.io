VERDICT: PASS
CONTENT-HASH: 43f3a8c3664dc353

## Blocking
- none

## Polish
- [Minor] fig-3-390 — "hearing threshold" sits close to the left edge at 390 px but is not clipped; the longer "threshold of hearing" would not fit. Keep.
- [Minor] figures.json (fixed) — description of the opening illustration: "on an afternoon" and "reached by the arcs as pale ones" rewritten as natural English; figures.py --lang en rerun.

## Checked
- Captures opened: contact-1, fig-3-390, sim-390, example-390-2, lab-1280-1, contact-5 (from the capture set before the alt-text fix; the text-only fix changes no pixels of a figure; captures retaken for the final hash).
- Figures 1–5: all labels LaTeX, decimal points (90.0, 84.0, 1.0, 2.0), no Finnish words left; descriptions translated.
- Sim at 390 and 1280 px: "Power per loudspeaker P = 50 mW", "Loudspeakers / 1 speaker", "Distance r", "Speed" fit, nothing clipped; readouts render.
- Worked example: aligned rows, fractions and units render; check_layout --lang en --width 345 OK; check_i18n en 0 errors.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
