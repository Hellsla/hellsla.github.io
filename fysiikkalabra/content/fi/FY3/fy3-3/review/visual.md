VERDICT: PASS
CONTENT-HASH: eced6a5c7d9e54b5

## Blocking

## Polish
- [Minor] fig-3 (micro-model) — while it plays, the velocity arrows are hidden (opacity 0 between 3 % and 97 %), so the "short vs long arrows" in the alt text is only visible in the still (reduced motion, print, loop start). The speed difference is still clear from the motion. Optional: mention in the alt text that the arrows show when the animation is paused.
- [Minor] fig-3 — the static state with the arrows visible was not captured (the shot is mid-animation); the still follows the unchanged SVG geometry.

## Checked
- Delta: fig-3 (micro-model) made animated (class fig-anim, fa-k groups). Opened fy3-3-fig-3-390.png and fy3-3-fig-row-1280.png (neighbouring figure and layout beside the paragraph intact).
- Checked in templates/site.css that the animation is paused by default via .is-playing, switched off under prefers-reduced-motion and print, and that the .fa-ctl control exists. Colours: the cold gas particles are blue and the hot ones red, the same as before. Labels are LaTeX and unclipped; p_1 and p_2 > p_1 are readable at 390 px.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
