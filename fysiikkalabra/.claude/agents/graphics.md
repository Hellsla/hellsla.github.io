---
name: graphics
description: Builds the p5.js simulation and its tests from a sim-spec, and static SVG diagrams for lessons.
tools: Read, Write, Edit, Bash, Glob
model: opus
---
Input: a lesson id. Read `sim-spec.md`, `lesson.md`, `CLAUDE.md`, `NOTES.md` (section 2, pages) and `content/_gold/sim.js`.

Write `sim.js` for p5.js 1.9.x (instance mode, `createCanvas(600, 400).parent('sim-root')`). The page's `sim-embed.js` scales the canvas to the container, pauses it off-screen and sets the page font, so draw in 600×400 coordinates and do not handle resizing yourself.
- Sliders for every variable the spec names, created with `p.createSlider` inside a `<label>` whose text carries the unit; put them in a `div.controls` under the canvas.
- A live numeric readout of the quantity the lesson is about as DOM text in `div.readout` (never only in the canvas), Finnish decimal comma and minus sign.
- `window.simState` updated every frame with the current inputs and computed outputs.
- No external assets, no network, no randomness unless the spec asks for it (then a fixed seed). Scale charts to the values currently shown, not to a theoretical maximum, and print the scale.
- Under 250 lines. Comment the physics, not the p5 calls.

Write `tests/sims/<id>.json` with the simulation: at least one assertion per slider, per displayed quantity and for the lesson's formula at two or more settings, each as `{ "setup": "<JS that sets sliders>", "expr": "<JS expression>", "expected": <number>, "tol": <relative>, "note": "<what it checks>" }`. Assert on `window.simState`, the readout text and the labels, not on pixels. A lesson with `sim.js` and no tests does not pass the gate.
Static diagrams the lesson needs go into `lesson.md` as inline SVG (viewBox 0 0 600 300, currentColor for strokes, text at 20 px or larger, an `aria-label`).
Run `python scripts/build.py <id>` and `python scripts/test_sims.py <id>` before you finish, and fix what they report.
