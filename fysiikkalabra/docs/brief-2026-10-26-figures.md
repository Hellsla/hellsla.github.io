# Brief 2026-10-26: figures, solutions and symbols to the teacher's rules

The teacher's standing rules (CLAUDE.md "Lesson form" 1, 2, 6; NOTES.md §1, §2, §3 as of today):

1. Every label in a figure is LaTeX (a `fig-tex` foreignObject), words as `\text{}`; no `<text>` element.
2. Solutions (`solutions.md`) are written in LaTeX.
3. The page works at every width (360, 768, 1280 px): the shared templates do the layout; your figures must read at 360 px.
4. Graphs are drawn carefully and clearly (NOTES.md §3 Graphs).
5. A theory point that has a picture (pressure p = F/A as a force on an area, …) gets a simple figure.
6. Chapter names, never lesson ids (already done in every lesson; keep it so).
7. Figures good enough for a printed textbook (NOTES.md §3 Print quality).

## Your task for one lesson `<id>` (work in `fysiikkalabra/`)

Read NOTES.md §1 and §3 first, then `scripts/figlib.py` and the model `content/FY3/fy3-1/figures.py` (three redrawn
figures: an illustration, a measured-points graph, a family of lines). Then:

**A. Figures.** Every inline SVG in `lesson.md` is redrawn from a `figures.py` in the lesson folder with figlib:
1. `python3 scripts/figures.py <id> --tag name1,name2,...` once: names the existing figures in order (short
   kebab-case names).
2. Write `content/<course>/<id>/figures.py` with one function per figure and `FIGURES = {name: function}`; run
   `python3 scripts/figures.py <id>` to write them into lesson.md. Edit figures.py, never the generated SVG.
3. Keep what each figure shows (its physics, its numbers, what is to scale) and its aria-label's facts; redraw it to
   the rules: all labels through `f.tex(...)` (words `\text{…}`, numbers `2{,}5`, units `\text{kPa}`, symbols
   with subscripts `T_\text{alku}`), graphs through `Axes` (ticks on gridlines, LaTeX numbers, filled arrowheads,
   axis titles beyond the arrow tips: leave ~80 units right of the x arrow and ~30 above the y arrow), honest
   scales, computed points, a curve's label at its end in its colour, `bg=True` for a label that must sit on
   gridlines. Illustrations: recognisable materials from the palette (figlib constants), gradients and patterns in
   `f.defs_add` with ids prefixed by the lesson (`fy34-water`), outlines 2–3, 12 units of margin, nothing clipped.
   A figure the lesson already draws well keeps its drawing; it still moves into figures.py with LaTeX labels.
   Gradients: `<linearGradient id="fy34-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient>`.
4. Add a simple new figure where a theory point has a picture and the lesson has none (the task line below names
   what the teacher expects at least). Place it with a line `<svg data-fig="name"></svg>` right after the
   paragraph it explains (blank lines around), then run figures.py.
5. Look at every figure: `python3 scripts/build.py <id>`, then
   `python3 /tmp/claude-0/-home-claude-hellsla-github-io/003c1654-fe2f-5eb8-a510-0591d79ffc38/scratchpad/figshot.py <outprefix> <id> 1280`
   and the same with `360` (it writes `<outprefix>-0.png`, `-1.png`, … one per figure; use an out prefix in
   `/tmp/claude-0/-home-claude-hellsla-github-io/003c1654-fe2f-5eb8-a510-0591d79ffc38/scratchpad/shots/<id>-...`).
   Open each PNG with Read and fix what a careful book designer would: collisions, labels on lines, cramped
   spacing, a label too far from its thing, a line past its axis, uneven spacing. Repeat until clean.
   `python3 scripts/check_layout.py <id>` and `--width 1280` must print no svg-text line.

**B. Solutions in LaTeX.** Rewrite `solutions.md` keeping every step's content and every number: each label line
keeps its `**Label:**`, the symbols, formulas and values with units go in inline `$...$`:
```
## fy3-4-L1-01
**Annettu:** $F = 720\,\text{N}$, $A = 0{,}30\,\text{m}^2$
**Kysytty:** paine $p$
**Kaava:** $p = \dfrac{F}{A}$
**Sijoitus:** $p = \dfrac{720\,\text{N}}{0{,}30\,\text{m}^2} = 2400\,\text{N/m}^2 = 2400\,\text{Pa}$
**Vastaus:** $2400\,\text{Pa}$
**Järkevyys:** Kenkien pohjat ovat noin kuudesosa suksien alasta, joten …
```
Decimal comma `{,}`, multiplication `\cdot`, `\approx` where rounded, `^\circ\text{C}`, the litre `\textsf{l}`,
`\Delta`, `\rho`, powers `10^{-6}`. Prose words stay outside maths. Keep each Sijoitus inline (it wraps at `=`).

**C. Symbols in theory prose.** In `lesson.md` (outside figures) a symbol named in prose is inline maths:
"missä $G$ on paino (N), $m$ massa (kg)", "ΔU" → `$\Delta U$`, "p₀" → `$p_0$`. Numbers with units in plain prose
stay as they are (9,81 m/s²). Do not change wording otherwise.

**Do not touch**: `sim.js`, `assets/sims/`, `tests/sims/`, `inquiry.json`, `exercises.json`, `answers.py`,
`exit-ticket.json`, `review/` (another thread is changing the simulations and some inquiry texts right now),
`scripts/`, `templates/`, `NOTES.md`, `CLAUDE.md`. If a check fails because of those files, say so in the report.

**Finish** with `python3 scripts/lint_lesson.py <id>` (no error about figures, solutions or chapter names) and
`python3 scripts/check_latex.py content/<course>/<id>` (all ok), and `check_layout.py` at 360 and 1280 with no
svg-text or formula line. Do not commit. Report in at most 150 words: figures redrawn (names), figures added
(names, what they show), anything you could not fix.
