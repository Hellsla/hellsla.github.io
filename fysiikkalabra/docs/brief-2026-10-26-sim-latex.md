# Brief 2026-10-26 (3): every label and value of a simulation in LaTeX

Teacher's rule (NOTES.md §1, CLAUDE.md Lesson form 1): every symbol, value, unit and label the student sees in a
simulation is LaTeX, as in the figures. The shared embed (`templates/sim-embed.js`, read its head comment) already
does the drawing: `p.text(str, x, y)` with a string that contains `$…$` is drawn by KaTeX over the canvas at p.text's
place, size, alignment and fill colour; `p.textWidth(str)` measures such a string as drawn; a p5 element's
`.html(str)` with `$…$` renders its maths (only when the string changes), and the sim's DOM is rendered once after
setup. The model is `content/FY3/fy3-1/sim.js` (`git diff HEAD~1 -- content/FY3/fy3-1/sim.js` shows the conversion).

## Your task for one simulation (work in `fysiikkalabra/`)
1. Every canvas label becomes one `$…$` string: symbols `$G$`, `$T_\text{alku}$`, Greek `$\theta$`, `$\Delta T$`;
   numbers with the decimal comma `{,}` (add `const tx = (x, d) => x.toFixed(d).replace('.', '{,}');` beside the
   sim's `fi`); units `$98{,}1\,\text{N}$`, `$\text{m/s}^2$`, `$^\circ\text{C}$`, `\%` for percent; axis titles
   `$G\ (\text{N})$`; tick numbers `$500$`; words `$\text{Kuu}$`, a word with a symbol `$\text{paino } G$`.
   Keep each label's position, size, colour and alignment; `p.textStyle(p.BOLD)` has no effect on a `$…$` label (use
   `\mathbf{}` only where bold carried meaning).
2. The readout, slider/control labels and legends (`.html()`, `createSpan()`, `createP()`): every symbol, formula and
   value-with-unit inside `$…$` ("Massa $m = 10\,\text{kg}$", "$G = mg = 98{,}1\,\text{N}$"); plain Finnish words
   stay text. A native `<option>` cannot hold maths: an option text names its case in words, no bare symbol.
3. Keep the physics, `window.simState`, the adapter and all keys unchanged. Where the sim builds `simState.labels`
   boxes from `p.textWidth`, keep doing so (it now measures the KaTeX label); fix any overlap the new sizes cause.
4. The sim's `sim-spec.md` and its `tests/sims/<id>.json` must still pass. A test that read the readout's
   `textContent` reads `simText('#sim-root .readout')` instead (sim-embed.js: each formula comes back as its TeX
   between dollars) and checks the new string, e.g. `x.includes('$G = mg = 98{,}1\\,\\text{N}$')` inside the JSON's
   JS (see `git show HEAD -- tests/sims/fy3-1.json`). Never weaken an assertion. `test_sims.py` now also checks that
   every KaTeX label stays inside the canvas and none overlaps another, at 360, 390 and 1280 px over the control sweep.
5. `inquiry.json` texts that quote a canvas label are already maths; leave them.

**Do not touch**: other sims, `templates/`, `scripts/`, `lesson.md`, `figures.py`, `solutions.md`, JSON files,
`review/`, `NOTES.md`, `CLAUDE.md`.

## Check and finish
- `python3 scripts/build.py <id>`, `python3 scripts/check_lesson.py <id>` (all ok), `python3 scripts/test_sims.py` for
  your sim passes.
- Look at the simulation at 390 and 1280 px:
  `python3 /tmp/claude-0/-home-claude-hellsla-github-io/003c1654-fe2f-5eb8-a510-0591d79ffc38/scratchpad/simshot.py <id> /tmp/claude-0/-home-claude-hellsla-github-io/003c1654-fe2f-5eb8-a510-0591d79ffc38/scratchpad/shots/sim-<id>`
  writes `…-390.png` and `…-1280.png` (and prints page errors); open both with Read. Every label in LaTeX, nothing
  overlapping, nothing leaving the canvas, no plain symbol left in the readout. Also move the controls through a few
  states (the sim's own extremes) if a label's width changes with the value.
- Do not commit. Report in at most 80 words: labels converted, readout converted, anything you could not convert.
