VERDICT: PASS
CONTENT-HASH: 3b8da62f2de25dff

## Blocking

## Polish
- [Minor] fig-2 (micro-boyle, now animated) — the captures are stills, so the motion and the pause control were not seen — the still is the static layout and reads correctly; spot-check the animation in a browser.

## Checked
- Hash `reviews.py hash fy3-9 --lang en` = 3b8da62f2de25dff at the start, equal to the packet and the captures.
- Opened `review/shots/fy3-9-fig-2-390.png`. Two cylinders, V and p against V/2 and 2p, orange "T constant" arrow, hit mark, red particles; nothing clipped or overlapping, labels in LaTeX, legible at 390 px.
- Diff: only the micro-boyle SVG changed (`class="fig-anim"`, keyframes, `fa-k` groups). The `aria-label` is unchanged and still describes the picture.
- Shared CSS: the animation plays only under `.is-playing`, and `prefers-reduced-motion` and print switch it off and hide the control, so the still stays.
- Did not open other captures; the diff touches nothing else.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
