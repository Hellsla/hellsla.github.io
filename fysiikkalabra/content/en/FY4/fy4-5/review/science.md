VERDICT: PASS
CONTENT-HASH: eb566cbcc01e931e

## Blocking

## Polish
- Layout check (`check_layout.py fy4-5 --lang en`, 360 and 1280 px) reports a figure-label overlap "N / F_y" that is identical in the Finnish preview (generated figure, not translation text). The English caption of the generated component figure, "horizontal and vertical forces to different scales", is wider than its figure in en ("leaves the figure", 360 and 1280 px); it comes from the figure generator's English string, not from the content files, and is outside this review's files.

## Checked
- Delta `git diff a6af45ae` of fi, en and fi-easy for fy4-5; every changed passage compared with the Finnish: hook (two children take turns; pull vs push), model text (ice and friction neglected; rope force is tension usually T, here F because the simulation switches between pull and push), solution of the 50 N vertical-component task (G-N = 50 N, rounding to whole newtons, decimals not significant figures, G 196,2 / N 146,2 spec), exp-2 question "when the angle α > 0°", spec blocks beside the Voimakuvio steps of the inquiry solutions; lesson epigraph (sled presses on the ground/surface beneath it, not snow). Numbers, symbols, \overline vectors and decimal marks agree with the Finnish.
- All `voimakuvio` blocks in inquiry.json and lesson.md identical to the Finnish (check_i18n enforces); `check_i18n.py` 0 errors; `build.py fy4-5` builds; `figures.py fy4-5 --lang en --check` up to date.
