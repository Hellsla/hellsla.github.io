VERDICT: PASS
CONTENT-HASH: 85ea8eb31e4d0bd7

## Blocking
(none)

## Polish
- [Minor] fy4-s1-graph (solutions.md:7–81) — label "voide B: 0,245 m/s²" sits on gridlines and close to the B marker at t = 5 s; the unit fractions are tiny at 390 px — move the label lower right clear of the markers; use a one-line `\text{m/s}^2` unit in the label.
- [Minor] fy4-s1-fbd (solutions.md:89–127) — the overline of $\overline{G}_x$ touches the block's lower-right edge — shift the label 8–10 px outward.
- [Minor] fy4-s1-drag (solutions.md:170–228) — the fitted curve past the last point (9,0 m/s) is solid, while the extrapolation to v = 0 is dashed — dash the short tail too, or end the line at the last point.
- [Minor] fy4-s3-collision — $v_\text{A} = 0$ is black, not velocity blue, while the other velocity labels are blue — optional; fine as the value is zero.
- [Minor] tasks.json fy4-s3 — the last bullet of the police report ends in a period, the others do not — make it consistent.

## Checked
- Delta after c2c6eff02 (s2 d conclusion criterion trimmed): re-read the changed teacher criterion and re-ran the DOM check on the refreshed page (no KaTeX error, no overflow); layout and figures unchanged, nothing new.
- First full review: rendered page at 390 px and 1280 px, every box open: no KaTeX error, no plain number-and-unit in prose, no ×/÷, no horizontal overflow (own DOM check); contact sheets 1 and 2; top-390; page-1280-3; fig-1, 3, 5, 7, 19 at 390 px.
- All four figures (s1-graph, s1-fbd, s1-drag, s3-collision) re-rendered at 2x and inspected: axes, units, markers vs fitted lines, colours (force red, velocity blue, acceleration orange, momentum violet), vectors, schematic note in the aria-label.
- Task texts (s1–s3), source notes, tables, model answers read for Finnish: natural, one voice, case endings after units correct.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
