# Notes: how a lesson is written

Lessons learned, for the developer and the reviewers. When a mistake costs a review round, add a line under the
right heading (what, why, how to check) and a check to `scripts/lint_lesson.py` when it can be checked mechanically.

## 1. Maths in LaTeX

- `lesson.md` is rendered by `scripts/build.py`, then KaTeX 0.16.11 (vendored) in the browser. `$$...$$` or a
  ```` ```latex ```` fence is display maths, `$...$` inline; the build hides maths from markdown first, so `_`, `*`
  and `\` are safe inside it. Maths also renders in `exercises.json` (`text`) and `exit-ticket.json` (`q`, `a`),
  with doubled backslashes in JSON. `solutions.md` is plain text with Unicode (`W₁`, `m/s²`, `·`), no LaTeX; the
  simulation canvas and inline SVG labels are plain text too.
- Every formula appears once in display form with its symbols named; inline maths only for short references.
  Inline maths stays on one line.
- Units: `40\,\text{N}`, `9{,}81\,\text{m/s}^2`. Decimal comma inside maths is `{,}`. Multiplication `\cdot`,
  degrees `^\circ`, roots `\sqrt{2gh}`, `\frac` in display and `\tfrac` inline, Finnish words in `\text{}`.
- Works: `aligned`, `cases`, `\cancel`, `\boxed`, `\color`, Greek letters. Does not work: siunitx, `\( \)`,
  `\[ \]`, `\newcommand` over a built-in. A bad fragment does not fail the build; the page shows red source.
- A `·` inside `\text{}` is a parse error: write `\tfrac{\text{J}}{\text{mol}\cdot\text{K}}`. The litre is
  `\textsf{l}` (`\text{l}` reads as the digit 1). Both are lint errors.
- Every display formula fits a 360 px phone: about 25 characters per row, one `=` step per row. In `aligned`
  the columns add up, so a long left side goes alone on its own row and the `= …` parts follow in one
  left-aligned column (`\begin{aligned} &a \\ &= b \\ &\approx c \end{aligned}`). `check_lesson.py` measures it.
- Markdown tables scroll sideways on a phone by design; keep header cells short.

## 2. Numbers, Finnish, scope

- The MAOL guide in `docs/lops2019/` decides what belongs to a module. FY2 introduces energy forms without
  expressions; `E_k`, `E_p`, the work-energy theorem, vectors and `cos α` are FY4. FY3 has force as a measure of
  interaction, `W = Fs`, graphical integration in (s,F) and Joule's experiment.
- g is always written in m/s² (g = 9,81 m/s², Moon 1,62, Mars 3,71, Jupiter 24,8), never N/kg.
- Round only at the end, show unrounded intermediates (`v = 80/3,6 m/s`). Final answers carry the data's
  significant figures, and a student rounding to them stays inside the relative `tolerance` (0,02 as a rule; `77 K`
  has two figures, so −196 °C needs 0,03 or a whole-number task). A coefficient with a power of ten counts its
  mantissa: `9,0 · 10⁻⁶ 1/K`, not `9 · 10⁻⁶`.
- Compute every answer in `answers.py` (one commented line per step, prints `{id: value}`); the lint re-runs
  it. A task whose answer is a datum plus a small change (L = L₀ + ΔL) cannot be marked by relative tolerance:
  ask for the change.
- Finnish: inflect the unit (`80 N:n voimalla`) or write nominative sentences; "paino" is a force, so "kappaletta
  pidetään paikallaan", not "painoa". Terms come from `glossary.json`.

## 3. Lesson form (human decisions 2026-10-25)

- **Figures.** At least one inline SVG in `## Ydinajatus` and one in `## Kaava`, right after the paragraph it
  explains: the micro model, a setup sketch, a graph of the formula, an energy-flow diagram, a before/after.
  House style `viewBox="0 0 600 300"`, `currentColor` strokes and fills, text 24 px or more (about 13 px on a
  360 px phone), an `aria-label` saying what the figure shows, no overlapping labels.
- **Formulas and symbols in figures are LaTeX** (human decision 2026-10-25): a label that carries a formula, a
  symbol with a subscript or a unit goes in `<foreignObject x y width height><div xmlns="http://www.w3.org/1999/xhtml"
  class="fig-tex">$p V = n R T$</div></foreignObject>`; KaTeX renders it on the page and it scales with the
  figure. Plain words stay in `<text>`. Give the box room (height ≥ 1,6 × font size, width for the widest
  rendering); `check_layout.py` treats the box like a text label (no overlap, inside the figure), and
  `check_latex.py` parses the formula. A figure drawn to scale is to
  scale; a schematic one says so. No paragraph over about 120 words.
- **Symbolic first.** Worked example and every solution: name the unknown, write the formula, solve it with
  symbols, substitute values with units, compute and round, check. In `solutions.md` the **Kaava:** line ends with
  the formula solved for the asked quantity and only **Sijoitus:** has numbers. In `lesson.md` the first row of a
  calculation is symbolic (`V_2 &= \frac{p_1 V_1}{p_2}`); the lint flags a first row with numbers.
- **Staged example.** Under `## Esimerkki`: the problem, then 3–6 stages each after a line `<!-- vaihe -->`
  (blank lines around it), typically **Tunnetut ja kysytty.** · **Kaava ratkaistuna.** · **Sijoitus.** ·
  **Tulos.** · **Järkevyys.** One bold lead-in and at most one display block per stage. The page shows stage 1 and
  reveals the rest; without JavaScript and in print all stages show.
- **Visually rich simulations.** Keep the controls the spec asks for. Draw the situation, not boxes: gradients, a
  container that looks like one, particles that move, a heater that glows, levels, arrows whose length is the
  quantity. Colour carries meaning (cold-to-hot scale, the same colour for the same quantity in picture and chart,
  a legend). Charts have gridlines, labelled axes with units, the current point highlighted, the theory curve faint
  behind the measured points. Decoration that hides numbers is not welcome.

## 4. Simulations and pages

- p5.js instance mode, a 600×400 canvas inside `#sim-root`, `window.simState` updated every frame.
  `templates/sim-embed.js` resizes and scales the canvas, pauses it off-screen, lowers the frame rate under
  `prefers-reduced-motion` and sets the page font; sims never handle resizing themselves.
- Every animated simulation has a **speed control** (a `select` "Nopeus": hidas · normaali · nopea, default so that a
  student can follow the motion with the eye; the physics advances by simulated time `dt·speed`, and every
  measurement is taken per simulated time, so slowing down changes nothing but the pace). **The canvas carries only
  labels and values**; the explanation of the model, its assumptions and how to read the picture goes under the
  canvas behind a `<details><summary>Lisätietoja</summary>…</details>`, with at most one short legend line visible.
  (Human decision 2026-10-25, after fy3-10.)
- Create `div.controls` before `div.readout`, main button first, so canvas and button fit one phone screen (an
  off-screen canvas is paused, so a button below the fold starts an animation nobody sees). Clamp the animation
  step (`Math.min(p.deltaTime, 100)`) so a resume cannot skip ahead. The readout is DOM text, tap targets 40 px.
- Canvas text grows with `ts()` (k ≈ 2 at 360 px). Every canvas text goes through a `lab(s, x, y, align)` helper
  that draws it and pushes `{s, x0, y0, x1, y1}` (canvas coordinates) to `simState.labels`; `test_sims.py` then
  sweeps every control at 360, 390 and 1280 px by itself and fails on any overlap or clipping (fy3-9 is the
  pattern). Draw every second tick label when k > 1,5 and keep a few pixels of clearance: CI's fonts are wider.
- `tests/sims/<id>.json`: an assertion on `simState` for every control and displayed quantity (set inputs through
  the DOM, read outputs, compare within 1 %), plus the label sweep. Never loosen an assertion to make it pass.
- The page places the simulation after `## Kaava` (before `## Esimerkki`); a line `<!-- sim -->` in `lesson.md`
  overrides the position. Exercises get a browser-side answer check; nothing is stored or sent. No third-party
  requests, fonts are self-hosted. Reviewer screenshots stay out of git (`**/review/*.png`).

## 5. Inquiry sequence (teacher's brief 2026-10-25)

- `inquiry.json` (format and activity types: `docs/inquiry.md`; the brief: `docs/inquiry-spec.md`). The pilot
  `content/FY3/fy3-2/inquiry.json` shows the shape; do not copy it mechanically — choose activities by what the
  lesson's goals need. A lesson without a simulation investigates a table, a figure or competing explanations.
- Order of the student's work: a phenomenon in the lesson's voice and the question it raises; a retrieval item on
  the prerequisite lesson; predictions the investigation can refute (each wrong option's feedback repairs the
  misconception it reveals, each right option's names the evidence); the simulation, then guided experiments that
  set the initial conditions, lock the controlled parameters and record the varied one with the measured
  quantities (`min` 2 before the prediction is revealed); the theory sections; a reflection that shows the
  student's own predictions and asks whether to revise; the worked example, an error-spotting item, a transfer
  task with three progressive hints and common-mistake feedback, the exercises; three checks (concept,
  representation or calculation, explanation with model answer and self-assessment criteria); the exit ticket.
- Never disclose the answer to the opening question before the student has committed; gate feedback, not
  access. Call the simulation's numbers model values; call what Joule measured measurements. Say at the point of
  use which simplifications the model makes (no friction, constant force).
- The sim declares its adapter (`defineSimAdapter`: the parameters experiments may set or lock, `reset`, `step`);
  the physics stays in `sim.js`, `window.simState` is unchanged, the existing assertions keep passing.
- `inquiry.json` is in the content hash: a migrated lesson needs both reviews again.

## 6. Learning from mistakes
When a reviewer finds an error that is objectively testable or has happened before: fix it, name the general
pattern, and then either add a check (`lint_lesson.py`, `test_sims.py`, `check_layout.py`) with a test that catches
the original case and passes on every other lesson, or, when it cannot be checked mechanically, add one line to
the right heading above. Never both, never a paragraph. The checks run before any reviewer, so the reviewers are
paid only for what scripts cannot see. Deterministic coverage today: numbers (`answers.py` re-run against
`exercises.json`, `Vastaus` lines, significant figures and tolerances, coefficient mantissas), LaTeX (KaTeX parse,
`{,}`, `\textsf{l}`, `·` in `\text`), lesson form (figures, stages, symbolic first rows, paragraph length),
pages (formula, table, figure and page width at 360 px, SVG labels overlapping or leaving a figure),
simulations (console errors, per-sim assertions, finite `simState` and label boxes at 360/390/1280 px over every
control combination), publication (content hash, rebuild equality, atomic build).

## 7. Exam material (inspiration only)
Exam files, if ever collected, live only in the git-ignored `docs/exams/` and are studied for patterns (task
types, contexts, how points split between reasoning and calculation), never quoted or reworded. Every exercise is
original.
