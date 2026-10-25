# Notes: things to take into consideration

Living checklist for the human and every agent. Read it before drafting or reviewing a lesson.
When a mistake costs a review round, add a line under the right heading (what, why, how to check).

## 1. Math in LaTeX

### How it is rendered
- `lesson.md` goes through `scripts/build.py`, then KaTeX 0.16.11 (vendored in `templates/vendor/katex`, no CDN) renders it in the browser.
- Delimiters: `$$...$$` for display, `$...$` for inline. A ```` ```latex ```` fence becomes display math.
- The build hides all math from the markdown converter first, so `_`, `*` and `\` inside formulas are safe.
- Math also renders in `exercises.json` (`text`) and `exit-ticket.json` (`q`, `a`), because auto-render runs over the whole page. In JSON every backslash is doubled: `"$\\frac{1}{2}$"`.
- `solutions.md` is rendered under the exercise as a collapsible "Ratkaisu" (which ones depends on `meta.solutions`: `first`, `all` or `none`). It goes through markdown but is written in plain text with Unicode (`W₁`, `m/s²`, `·`), no LaTeX, so a `$` in it would be picked up by auto-render.
- The simulation canvas and the inline SVG figures cannot use LaTeX either. Use plain text and Unicode there (`W = F · s`, `m/s²`).

### Writing rules
1. Every formula appears once in display form with its symbols named (house rule). Use inline math only for short references and numbers.
2. Inline math stays on one line. A `$...$` that spans a line break is not recognised.
3. Units go in `\text{N}` or `\mathrm{N}` after a thin space: `40\,\text{N}`, `9{,}81\,\text{m/s}^2`. A normal space `\ ` also works, but use `\,` in new text.
4. Decimal comma inside math is `{,}`: `0{,}20`, `9{,}81`. A bare `9,81` renders with a gap after the comma. In JSON values (`answer`) use a decimal point.
5. Multiplication is `\cdot`, never `*` or `x`. Degrees are `^\circ`. Square roots are `\sqrt{2gh}`.
6. Use `\frac` in display formulas and `\tfrac` inline, so inline formulas stay compact.
7. Finnish words inside math go in `\text{}`: `F_\text{kitka}`, `\text{työ}`. Ä and ö work.
8. Vectors are `\mathbf{F}`, magnitudes plain `F`. Vectors belong to FY4; FY3 treats force as a scalar.
9. Verified to work: `aligned`, `cases`, `\cancel`, `\boxed`, `\color`, `\Delta`, `\rho`, `\approx`, `\Rightarrow`.
10. Verified **not** to work: siunitx (`\si`, `\SI`, `\unit`) and redefining a built-in with `\newcommand` (for example `\N`).

### Pitfalls
- A bad fragment does **not** fail the page build. The page shows the raw source in red. Always run the checker.
- `\( ... \)` and `\[ ... \]` are not recognised. Use `$` and `$$`.
- A literal dollar sign starts math. Write "euroa" or "€" instead.
- Math in an SVG `<text>` or in canvas text is plain text. Keep the labels short.
- An inline `\dfrac` makes a tall fraction that breaks the line. Put calculations with fractions on their own line in display math.
- A `·` inside `\text{}` is a KaTeX parse error. Write compound units as `\tfrac{\text{J}}{\text{mol}\cdot\text{K}}` or `\text{J/(mol}\cdot\text{K)}`. The lint reports it.
- The litre in math: `\text{l}` renders like the digit 1 in KaTeX's serif font, so `0{,}80\,\text{l}` reads as "0,801". Write `\textsf{l}`. The lint reports `\text{l}`. (Found in fy3-9.)
- Every display formula must fit a 360 px phone without scrolling: about 25 visible characters per line. Split long calculations into rows, one `=` step per row. In `aligned` the two columns' widths add up, so `a &= b \\ &= c` is no narrower when `a` is long: put a long left side alone on its own row and the `= …` parts on the following rows in one left-aligned column (`\begin{aligned} &a \\ &= b \\ &\approx c \end{aligned}`). Run `python scripts/check_layout.py <id>` after the build; it lists every formula, figure or page that is too wide. (Cost a round in fy3-6 and fy3-8.)
- A wide markdown table overflows a phone. The site CSS makes tables scroll sideways inside themselves; keep header cells short.

### Check before every commit that touches math
```bash
python scripts/lint_lesson.py fy3-2                 # every mechanical rule in this file; exits 1 on an ERROR
python scripts/check_latex.py content/FY3/fy3-2     # .md files and every string in the .json files
```
Both exit 1 on a problem. CI and the gate run them too. After changing any formula, change `answers.py` first and copy its output into `exercises.json` and `solutions.md`.

## 2. Other things learned in this project

### Scope and curriculum
- The MAOL guide in `docs/lops2019/` decides what belongs to a module. FY2 introduces energy forms **without** expressions; `E_k`, `E_p`, the work-energy theorem, vectors and `cos α` are FY4. FY3 has force as a measure of interaction, `W = Fs`, graphical integration in (s,F) and Joule's experiment. Grep the guide before adding a formula.
- Slot ids follow the module: `fy3-2` is the second FY3 lesson. The gold reference is `fy4-4`.

### Numbers
- **g is always written in m/s²** (human decision, 2026-10-25): g = 9,81 m/s², Kuu 1,62 m/s², Mars 3,71 m/s², Jupiter 24,8 m/s². Never use N/kg for g, in text, tables, exercises, solutions, simulations or tests. The weight formula G = mg gives newtons when m is in kg and g in m/s² (1 N = 1 kg·m/s², explained in FY4); weight is never described as the cause of a motion in FY3.
- Round only at the end; show unrounded intermediates in solutions (`v = 80/3,6 m/s`, not `22,2`).
- Final answers have as many significant figures as the data (2 sf data gives 2 sf). Check that a student who rounds correctly stays inside the relative `tolerance` (0,02).
- Compute every answer in `answers.py` (one commented line per step, prints `{id: value}` as JSON); the lint and the gate re-run it against `exercises.json`.
- The lint checks that a student rounding to the data's significant figures stays inside the tolerance. `77 K` has two figures, so an answer of −196 °C needs a tolerance of 0,03 or the task must ask for a whole number.
- Coefficients written with a power of ten count too: `9 · 10⁻⁶ 1/K` has one significant figure, so write `9,0 · 10⁻⁶ 1/K`. The lint reads the mantissa. (Cost a round in fy3-8.)
- A task whose answer is a datum plus a small change (the new length L = L₀ + ΔL) cannot be marked by relative tolerance: the unchanged L₀ is almost as close as the right answer. Ask for the change (ΔL in mm) and show L in the solution.

### Finnish
- Avoid "25 m matka" and "80 N voimalla". Either inflect the unit (`80 N:n voimalla`, `40 N:ssä`) or write nominative sentences ("Voima on 80 N ja matka 25 m").
- "Paino" is a force (`G = mg`). Do not "pitää painoa paikallaan"; say "kappaletta".
- Terms come from `glossary.json`; add a missing term there instead of inventing one.

### Pages and publishing
- Only `status: reviewed` lessons are built into `site/`, which is committed and served by Pages from `main`. Previews and `--all` go to the git-ignored `preview/`.
- The numeric readout in a simulation is DOM text, not canvas text, so it stays readable on a phone. Tap targets are at least 40 px, and there is no horizontal overflow at 390 px.
- In a simulation, create `div.controls` before `div.readout`, with the main button first, so the canvas and its button fit in one 640 px phone screen; the embed pauses an off-screen canvas, so a button below the fold starts an animation nobody sees. Clamp the animation step (`Math.min(p.deltaTime, 100)`) so a resume cannot skip ahead. (Cost a round in fy3-6 and fy3-7.)
- Canvas text grows with `ts()` (k ≈ 2 at 360 px), so labels that fit at 1280 px collide on a phone. Before finishing a sim, sweep every slider over its full range at 360, 390 and 1280 px and check that no two label boxes intersect or leave the canvas; draw every second tick label when k > 1,5. (Cost two rounds in fy3-4.)
- `templates/sim-embed.js` wraps every sim: it resizes the 600×400 canvas to the container and scales the drawing, pauses the sketch when it is off-screen, lowers the frame rate under `prefers-reduced-motion`, and sets the page font inside the canvas. Sims draw in 600×400 coordinates and never handle resizing themselves. `test_sims.py` scrolls the sim into view before it reads `simState`.
- The page places the simulation after the `## Kaava` section (before `## Esimerkki`). A line `<!-- sim -->` in `lesson.md` overrides the position.
- Exercises have an answer field: the page compares the typed number with `answer` within `tolerance` (decimal comma accepted). Everything happens in the browser; nothing is stored or sent.
- Fonts are self-hosted (`vendor/fonts`). Add no third-party requests, tracking, logins or forms.
- Reviewer screenshots stay out of git (`**/review/*.png`).

### Process
- Publishing goes through the gate (`scripts/gate.py`): all reviewers PASS on the current content hash, then the publisher agent commits. Do not hand-edit `status`, `reviewed_by`, `reviewed_on` or `reviewed_hash`.
- Reviewers never edit anything that is part of the hash (that includes `tests/sims/<id>.json`); the graphics agent writes the tests with the sim, the tester reports gaps and the fixer adds them.
- Any edit to a lesson changes its full hash, but each reviewer's verdict is tied to the hash of its own files (`gate.py --hash <id> --for <reviewer>`), so after a fix only the reviewers whose files changed run again. `gate.py <id>` names them.
- Reviewers never edit lesson files. Only `## Blocking` findings fail a lesson; spelling and style go in the proofreader's diff and are applied by the fixer.
- One commit per review round (`fysiikkalabra: <id> review round <n>`); the branch name is given by the session.

## 3. Matriculation exam material (inspiration only)

- Source named by the human: https://yle.fi/abitreenit/fysiikka (physics exams collected there). Status: **not collected yet**, because the cloud environment's network policy blocked yle.fi (and the exam-file host it links to).
- Store downloaded exam files only in `docs/exams/`, which is git-ignored. They are third-party material, so they never go into commits, `site/` or lesson folders.
- Use them to study, never to copy: which skills each task type tests, typical contexts, how multi-part tasks are built, how many points go to reasoning versus calculation, which formulas the tasks expect students to know.
- Record findings as short pattern notes in this file (for example "typical level-3 task: graph reading plus one calculation"), never as quoted or lightly reworded tasks.
- Every exercise stays original: new context, new numbers, own wording. CLAUDE.md still forbids copying exam questions.
- When a pattern changes how a lesson should be written, add the change to the relevant section above and mention it in the commit.

### Exam-style patterns used so far (from general knowledge, not yet checked against the files)
- A task starts with a context and runs through several parts, from a direct calculation to reasoning.
- Graph reading and graph-based calculation are common. Applied in fy3-2 (area under the (s,F) graph) and fy3-1 (spring stretch against force).
- Tasks ask the student to reason with a changed situation ("what does the scale show on Mars?"), not only to plug numbers in. Applied in the level 3 tasks.
- Units, conversions (g to kg, minutes to seconds) and sensible rounding are part of the grading, so every exercise keeps them.
- Check these against the real files when `docs/exams/` is filled, and replace this list with verified findings.

## 4. Lesson form (human decisions, 2026-10-25)
These four rules come from the human and apply to every lesson, including published ones. They are summarised in CLAUDE.md.

### Figures in the text
- At least one inline SVG in `## Ydinajatus` and one in `## Kaava`, each right after the paragraph it explains. Good subjects: the micro model (particles), a setup sketch (piston, calorimeter, dam), a graph of the formula, an energy-flow diagram, a before/after comparison.
- SVG house style: `viewBox="0 0 600 300"`, `currentColor` strokes and fills (opacity for tints), text 24 px or more (it renders at about 13 px on a 360 px phone), an `aria-label` that says what the figure shows. No label may overlap a line or another label; the web-designer checks at 360 px.
- A figure drawn to scale must be to scale (reviewers measure it); a schematic one says so in the aria-label or a caption.
- No paragraph over about 120 words; split it, or move a list of cases into a short bullet list.

### Symbolic first, then numbers
- Worked example and every solution: (1) name the unknown, (2) write the formula, (3) solve it for the unknown with symbols only, (4) substitute values with units, (5) compute and round, (6) check.
- In `solutions.md` the **Kaava:** line ends with the formula solved for the asked quantity (`α = ΔL / (L₀ ΔT)`), and only **Sijoitus:** has numbers, each with its unit.
- In lesson.md displays, the first row of a calculation is symbolic (`V_2 &= \frac{p_1 V_1}{p_2}`), the next row has the numbers with units, the last the result. The lint flags a display under `## Esimerkki` whose first row already has numbers.

### Worked example in stages
- Under `## Esimerkki`: the problem statement, then 3–6 stages, each starting after a line `<!-- vaihe -->` (blank lines around it). Typical stages: **Tunnetut ja kysytty.** · **Kaava ratkaistuna.** · **Sijoitus.** · **Tulos.** · **Järkevyys.** A stage is one bold lead-in sentence plus at most one display block.
- `build.py` (`staged_example`) wraps the stages; `lesson.js` shows stage 1 and reveals the rest with "Näytä seuraava vaihe" / "Näytä kaikki". Without JavaScript and in print all stages show.
- Each display must still fit 360 px (see section 2), so split long rows.

### Visually rich simulations
- Keep the controls the sim has; do not add sliders to look busy.
- Draw the physical situation, not boxes: shaded or gradient fills, a container that looks like one, particles with motion, flames or a heater that glows, liquid levels, arrows whose width or length is the quantity.
- Colour carries meaning: a cold-to-hot colour scale for temperature, consistent colours for the same quantity in the picture and the chart, a small legend.
- Small animations that explain (particles speeding up, a needle moving, a level rising) are welcome; decoration that hides numbers is not.
- Charts: gridlines, labelled axes with units, the current point highlighted, the theoretical curve faint behind measured points.
- Label sweep at 360, 390 and 1280 px still applies.


### What the lint checks
- `lint_lesson.py <id>`: an ERROR when Ydinajatus or Kaava has no `<svg`, when the worked example has fewer than 3 or more than 6 `<!-- vaihe -->` stages, when a display under `## Esimerkki` has numbers in its first row (start every calculation with the symbolic row), and when a solution's **Kaava:** step has no equation. A WARN for paragraphs over 130 words and for numbers with units in a **Kaava:** step.
- `lint_lesson.py --all` (CI): lessons published before these rules report the lesson-form findings without failing, until they are reworked and republished. The gate runs the single-lesson lint, so no lesson can be published or republished without meeting them.
