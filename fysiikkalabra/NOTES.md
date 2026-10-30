# Notes: how a lesson is written

Lessons learned, for the developer and the reviewers, shared by every course. When a mistake costs a review round, add a
line under the right heading (what, why, how to check, ending with the date and the lesson: `(2026-11-02, fy4-3)`) or a
check to `scripts/lint_lesson.py` when it can be checked mechanically. What concerns one course only goes in that
course's `scope_notes` in `curriculum.json`, not here. Lines without a date predate 2026-10-26.

## 1. Maths in LaTeX

- `lesson.md` is rendered by `scripts/build.py`, then KaTeX 0.16.11 (vendored) in the browser. `$$...$$` or a
  ```` ```latex ```` fence is display maths, `$...$` inline; the build hides maths from markdown first, so `_`, `*`
  and `\` are safe inside it. Maths also renders in `exercises.json` (`text`) and `exit-ticket.json` (`q`, `a`),
  with doubled backslashes in JSON. `solutions.md` is LaTeX too (teacher's rule 2026-10-26): every symbol, formula and
  value with its unit in inline `$...$` (`**Kaava:** $p = \dfrac{F}{A}$`, `**Sijoitus:** $p = \dfrac{720\,\text{N}}{0{,}30\,\text{m}^2} = 2400\,\text{Pa}$`),
  one `=` step after another on the Sijoitus line, words outside the maths; the lint reads the Vastaus value through
  the LaTeX. Keep writing a calculation as one inline chain: the page shows a long chain (two or more `=`/`\approx`,
  or a long side) as rows with the equals signs in one column, each row wrapping after an operator on a phone
  (`scripts/mathlayout.py`, §8), so never hand-split a chain or rewrite it as display maths for the layout's sake. Inline SVG labels are LaTeX as well (§3). A symbol or formula named in the student's text is inline maths
  everywhere: `lesson.md`, `inquiry.json`, `exercises.json`, `exit-ticket.json` ("$T$:hen", "$(V, p)$-kuvaaja"); a
  number with its unit in prose is maths too ($98\,\text{N}$, $4{,}0\,\%$; teacher 2026-10-28, as FY1 and FY2 do), only
  an `aria-label` stays plain text. The experiments' Alkutila line and table headers turn
  a symbol in `names`/`measure` labels into maths at build time (scripts/inquiry.py `tex_name`). The simulation too
  (teacher 2026-10-26, "latexilla kaikki"): every label drawn on the canvas is a `p.text('$…$', x, y)` string, words
  as `\text{}`, numbers with `{,}`, units `\,\text{kPa}` (`templates/sim-embed.js` draws a `$…$` string with KaTeX
  over the canvas at p.text's place, size, alignment and fill, and `p.textWidth` measures it as drawn); the readout,
  slider labels and legends write their symbols, values and units as `$…$` in `.html()` / `createSpan()`. Only a
  native `<option>` stays plain text (it cannot hold maths), so an option names a case in words, not a symbol.
  A plain-text symbol anywhere the student looks is a blocking finding.
- Every formula appears once in display form with its symbols named; inline maths only for short references.
  Inline maths stays on one line.
- Units: `40\,\text{N}`, `9{,}81\,\text{m/s}^2`. Decimal comma inside maths is `{,}`. Multiplication `\cdot`,
  degrees `^\circ`, roots `\sqrt{2gh}`, `\frac` in display and `\tfrac` inline, Finnish words in `\text{}`.
- Notation (teacher 2026-10-28, after FY1): multiplication is always `\cdot`, never `\times` or ×, also in powers of
  ten (`3{,}6 \cdot 10^{6}\,\text{J}`); a division written as an operation in a sentence or a chain is a colon
  (`7200\,\text{J} : 60\,\text{s}`), a formula keeps its fraction (`P = \dfrac{E}{t}`); never ÷. A measurement
  error is `\Delta x` (`\Delta t`, `\Delta m`). The lint flags `\times`, ×, `\div` and ÷ in maths.
- Works: `aligned`, `cases`, `\cancel`, `\boxed`, `\color`, Greek letters. Does not work: siunitx, `\( \)`,
  `\[ \]`, `\newcommand` over a built-in. A bad fragment does not fail the build; the page shows red source.
- A `·` inside `\text{}` is a parse error: write `\tfrac{\text{J}}{\text{mol}\cdot\text{K}}`. The litre is
  `\textsf{l}` (`\text{l}` reads as the digit 1). Both are lint errors.
- Every display formula fits a 360 px phone: about 25 characters per row, one `=` step per row. In `aligned`
  the columns add up, so a long left side goes alone on its own row and the `= …` parts follow in one
  left-aligned column (`\begin{aligned} &a \\ &= b \\ &\approx c \end{aligned}`). `check_lesson.py` measures it.
- Markdown tables scroll sideways on a phone by design; keep header cells short.

## 2. Numbers, Finnish, scope

- The MAOL guide in `docs/lops2019/` decides what belongs to a course; each course's own limits are its
  `scope_notes` in `curriculum.json`, which your packet carries (moved there 2026-10-26).
- g is always written in m/s² (g = 9,81 m/s², Moon 1,62, Mars 3,71, Jupiter 24,8), never N/kg.
- Round only at the end, show unrounded intermediates (`v = 80/3,6 m/s`). Final answers carry the data's
  significant figures, and a student rounding to them stays inside the relative `tolerance` (0,02 as a rule; `77 K`
  has two figures, so −196 °C needs 0,03 or a whole-number task). A coefficient with a power of ten counts its
  mantissa: `9,0 · 10⁻⁶ 1/K`, not `9 · 10⁻⁶`.
- Compute every exercise answer in `answers.py` and every number of the lesson text and the inquiry in
  `lesson-answers.py` (one commented line per step, each prints `{id: value}`; 2026-10-28: the exercises are a part of
  their own, README "Exercises"); the lint re-runs both. A task whose answer is a datum plus a small change (L = L₀ + ΔL) cannot be marked by relative tolerance:
  ask for the change.
- Data provenance (2026-10-28, FY2): an `interpret` table of official statistics is `source: statistics` with the
  source and year in `source_note`; invented realistic numbers are `source: example` (Keksitty esimerkkiaineisto), never
  `simulated` or `measured`.
- Understanding before formulas (teacher 2026-10-28, FY1): a unit conversion substitutes the unit
  (`4{,}2\,\text{km} = 4{,}2 \cdot 1000\,\text{m}`, `1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s}`), never a general
  conversion formula; no helper quantities or ratio formulas the student does not need (the essential idea must not
  drown in notation); a comparison is said in words with one division, not a coefficient formula. (2026-10-28, fy1-1, fy1-2)
- A difference of readings has the figures of the difference, not of the readings: 38 °C − 31 °C = 7 K has one
  significant figure, so a task whose answer carries two gives its temperatures as 38,0 °C and 31,0 °C; a rounding
  justification in a solution names the datum that really limits the result. (2026-10-27, fy3-6)
- A student sees chapter names, never lesson ids (teacher's rule 2026-10-26): "luvussa *Paine ja hydrostaattinen
  paine*", "(luku *Työ ja energia*)", not "oppitunnilla fy3-4", "(fy3-4)" or "edellisellä oppitunnilla". The
  chapter name is the lesson's `title` in meta.json (without a trailing formula). `lint_lesson.py` flags ids and
  "edellinen oppitunti" in every file the page shows.
- Finnish: inflect the unit (`80 N:n voimalla`) or write nominative sentences; "paino" is a force, so "kappaletta
  pidetään paikallaan", not "painoa". Terms come from `glossary.json`.

## 3. Lesson form (human decisions 2026-10-25)

- **Figures.** At least one inline SVG in `## Ydinajatus` and one in `## Kaava: <law>`, right after the paragraph,
  table or list it explains (the page sets it beside that block on a wide screen): the micro model, a setup sketch,
  a graph of the formula, an energy-flow diagram, a before/after. `viewBox` 600 wide (300–380 high), text 24 px or more
  (about 13 px on a 360 px phone), an `aria-label` saying what the figure shows and what is to scale, no overlapping
  labels. (2026-10-26, replaces the monochrome `currentColor` style)
- **Textbook illustrations** (2026-10-26, model: fy3-6). Draw the thing, not a diagram of boxes: a glass basin with
  water that has a surface, sand with grains, a thermometer with a scale. Colours from the figure palette only, one
  meaning each: ink `#1f2933` (outlines 2–3 px, text), muted `#6b7480` (ticks, axes' numbers), rules `#c9c2b2`/`#e3dccb`,
  glass `#eef5f9`, water `#a9d1f0`→`#2f74b5`, sand `#f1dfb5`→`#d9b26a` with grains `#a97a35`, energy or heat flow
  `#ffc078`→`#e8590c` (filled arrows), temperature and its rise `#c92a2a` (before the rise `#f2a69c`), cold `#1971c2`
  /`#d0e6fb`, metals `#c4ccd4` (aluminium), `#6c757d` (iron), `#b8622d` (copper), ice `#a5d8ff`, `#2b8a3e`/`#b2f2bb` for
  a correct or stable state, momentum `#7048e8` (FY4: apart from velocity `#1971c2`, force red and acceleration
  `#e8590c`); `lint_lesson.py` holds the list. Colour never carries information alone: a bracket and a
  label say what the red segment says. Equal quantities get equal shapes (two equal Q arrows); a ratio is drawn to
  scale (ΔT 20 px and 105 px for c 4190 and 800). Gradients and patterns go in the figure's own `<defs>` with ids
  prefixed by the lesson (`fy36-water`), because two figures share one page. A filled path makes an arrow (a gradient
  on a vertical line's stroke does not render). Leave room: labels outside the shapes, a dashed rule between panels.
- **Opening illustration** (2026-10-26, teacher chose flat vector style; samples fy3-6, fy3-7). Every chapter opens
  (teacher 2026-10-29; `lint_lesson.py` errors without one) with a wide illustration of its Miksi scene right under the question: `Fig(..., width=1200, hero=True)` in
  figures.py (`data-fig="hero"`), 1200 × 600, figure palette plus the paper `#f6f1e6`, flat shapes, no text, the
  subject in the middle third so it reads at 360 px; site.css `.fig-hero` gives it the column width.
  A second everyday scene of the same phenomenon may sit beside the summary list: `H.scene(...)` (600 × 360,
  `data-fig="scene"`) right after the list under `## Tiivistelmä`, same style. Both kinds without labels are the
  review category "illustration" (science none, pedagogy delta; teacher 2026-10-26).
- **Every label in a figure is LaTeX** (human decision 2026-10-25, extended by the teacher 2026-10-26 to all labels):
  symbols, formulas, units, axis titles, tick numbers and words all go in `<foreignObject x y width height><div
  xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$p V = n R T$</div></foreignObject>`, words as `$\text{vesi}$`,
  so one typeface (KaTeX) runs through text, formulas and figures; KaTeX renders it on the page and it scales with
  the figure. No `<text>` element (the lint flags one). Give the box room (height ≥ 1,6 × font size, width for the
  widest rendering; `style="text-align:center|right"` for centred or right-aligned labels); `check_layout.py` treats
  the box like a text label (no overlap, inside the figure), and `check_latex.py` parses the formula. A figure drawn
  to scale is to scale; a schematic one says so. No paragraph over about 120 words.
- **Graphs** (teacher's rule 2026-10-26, after fy3-1's force–extension graph): axes 2,5 px ink with filled arrowheads,
  the axis title at the arrow end as `$F\ (\text{N})$`, ticks 6 px on every gridline with the numbers in LaTeX
  (`$2{,}5$`) centred under (x) or right-aligned beside (y) the tick, gridlines `#e3dccb` on every tick, the origin
  `$0$` once, data lines 3 px, measured points as filled circles r 6 with a white 2 px ring, guide lines dashed `#6b7480`
  1,5 px only where the text reads a value off. The plot area leaves 10 px between any line and any label, a line
  never runs over a label or past the last gridline, and a curve's label sits at its end in the curve's colour.
  Scales are honest: equal steps for equal values, and the drawn points are the computed ones.
- **Print quality** (teacher's rule 2026-10-26): a figure must be good enough for a printed textbook: coordinates on
  whole or half pixels, consistent stroke widths (outlines 2–3, details 1,5), no element touching the figure's edge
  (12 px margin), arrows as filled paths, nothing clipped, no stray decoration. A theory point that has a picture
  (pressure as force on an area, a lever arm, a phase diagram) gets a simple one beside its paragraph.
- **Symbolic first.** Worked example and every solution: name the unknown, state the principle, write the formula,
  solve it with symbols, convert units, substitute values with units, compute and round, check (Complete solutions below). In `solutions.md` the **Kaava:** line ends with
  the formula solved for the asked quantity and only **Sijoitus:** has numbers. In `lesson.md` the first row of a
  calculation is symbolic (`V_2 &= \frac{p_1 V_1}{p_2}`); the lint flags a first row with numbers.
- **Staged example.** Under `## Esimerkki`: the problem, then seven stages each after a line `<!-- vaihe -->`
  (blank lines around it), exactly **Tunnetut ja kysytty.** · **Periaate.** · **Kaava ratkaistuna.** ·
  **Yksikkömuunnokset.** · **Sijoitus.** · **Tulos.** · **Järkevyys.** (teacher 2026-10-27; `check_solutions.py`).
  One bold lead-in and at most one display block per stage. The page shows stage 1 and reveals the rest; without
  JavaScript and in print all stages show.
- **Complete solutions** (teacher 2026-10-27; CLAUDE.md "Lesson form" 7). Every exercise in `exercises.json` has its
  `## <id>` block in `solutions.md`, and every `numeric` task in `inquiry.json` (the transfer task, the checks, an
  experiment's question) has a `solution`, with these bold steps in this order, each on its own line (in JSON a
  paragraph of its own), each with real content:
  `**Annettu:**` the data with units, the table values used named as such ("taulukosta $c = …$");
  `**Kysytty:**` the quantity, its symbol and the unit asked for;
  `**Periaate:**` the law or principle and *why it applies here* (energy is conserved because no heat is lost; the
  temperature stays constant, so Boyle's law; the ice does not melt, so no latent heat), one to three sentences;
  `**Kaava:**` the starting equation, then the asked quantity solved in symbols (ends with `<unknown> = …`, no numbers);
  `**Muunnokset:**` every conversion made (`2{,}4\,\text{kW} = 2400\,\text{W}`, °C to K where an absolute temperature
  is needed, g to kg, MJ to J), or a sentence saying why none is needed (the unit cancels, a difference is the same in
  °C and K);
  `**Sijoitus:**` the values with units into the solved formula, intermediate results unrounded, one `=` step after
  another;
  `**Vastaus:**` the value first, then its unit and in a few words why that many significant figures
  (`$0{,}63\,\text{MJ}$, kaksi merkitsevää numeroa kuten massassa $1{,}8\,\text{kg}$`);
  `**Järkevyys:**` a real check: an estimate with round numbers, the sign, a comparison with experience, the energy
  balance recomputed, a limiting case, units. "Tulos on järkevä" alone is not a check.
  A task whose text refers to a graph adds `**Kuvaajan lukeminen:**` after Periaate: which points or which area are
  read, at which values, and how the answer follows. A task answered in words (`answer` a string) has `**Kysytty:**`,
  `**Periaate:**` and `**Mallivastaus:**` with the reasoning. A complete solution is about 100–220 words. The model
  is `content/fi/FY3/fy3-6/exercises/solutions.md` and its inquiry tasks `siirto` and `tarkistus-2`. (2026-10-27, all lessons)
- **Every language version is as complete** (teacher 2026-10-27). A translated or S2 (Finnish as a second language)
  version of a lesson keeps every solution step and justification; S2 writes shorter sentences, opens each concept
  the first time it appears ("ominaislämpökapasiteetti eli se, kuinka paljon energiaa yhden kilogramman lämmittäminen
  yhdellä kelvinillä vaatii") and may add steps, never remove them.
- **Visually rich simulations.** Keep the controls the spec asks for. Draw the situation, not boxes: gradients, a
  container that looks like one, particles that move, a heater that glows, levels, arrows whose length is the
  quantity. Colour carries meaning (cold-to-hot scale, the same colour for the same quantity in picture and chart,
  a legend). Charts have gridlines, labelled axes with units, the current point highlighted, the theory curve faint
  behind the measured points. Decoration that hides numbers is not welcome.

## 4. Simulations and pages

- One simulation per folder, `assets/sims/<course>/<name>/` (sim.js, its own sim.css and images, loaded from
  `document.getElementById('sim-root').dataset.base`); `meta.json` `"sim": true` is the lesson's own folder, a name
  reuses one the course has. Reuse before creating; changing a folder another lesson uses re-opens that lesson's
  reviews, so it needs the teacher's word. FY3's sims stay as `sim.js` in their lesson folders. (2026-10-26)
- p5.js instance mode, a 600×400 canvas inside `#sim-root`, `window.simState` updated every frame.
- **Readable on a phone** (2026-10-29, fy4-3, fy4-4: reviewers failed three-panel sims shrunk to 0,6 at 390 px). The page
  scales the canvas to `#sim-root`'s width, so a 600-px picture is drawn at about 0,6 on a phone. A sim with several
  panels (picture, graph, force diagram) stacks them on a narrow screen: when `#sim-root.clientWidth < 500`,
  `resizeCanvas(600, <taller>)` and draw each panel at the full 600 width, one under another, with label fonts and
  strokes multiplied by `600 / clientWidth` so that labels read at about 14 CSS px. `test_sims.py` checks the label
  boxes against the canvas's actual size; a test asserting 600×400 is written for the wide layout only.
  `templates/sim-embed.js` resizes and scales the canvas, pauses it off-screen, lowers the frame rate under
  `prefers-reduced-motion` and sets the page font; sims never handle resizing themselves.
- Every animated simulation has a **speed control** (a `select` "Nopeus": hidas · normaali · nopea, default so that a
  student can follow the motion with the eye; the physics advances by simulated time `dt·speed`, and every
  measurement is taken per simulated time, so slowing down changes nothing but the pace). **The canvas carries only
  labels and values**; the explanation of the model, its assumptions and how to read the picture goes under the
  canvas, behind closed boxes, with at most one legend line of at most 15 words visible in the sim (human decision
  2026-10-25, after fy3-10). Since 2026-10-26 the boxes are the lesson's, not the sim's: the sim activity in
  inquiry.json has a lead of at most 30 words (`text`) and `howto`, `model`, `calc` (markdown, LaTeX allowed), shown
  as Käyttöohje, Mallin oletukset and Laskennan selitys under the readout; sim.js writes no explanation paragraph and
  no Lisätietoja box. The readout lists quantities and values (`T = 24,6 °C`, `Q = 5,80 kJ`); the formulas behind them
  go in Laskennan selitys. Old sims' longer `p.note` paragraphs are folded by `sim-embed.js` until the simulation itself is edited (the lint
  asks for the new form then).
- Create `div.controls` before `div.readout`, main button first, so canvas and button fit one phone screen (an
  off-screen canvas is paused, so a button below the fold starts an animation nobody sees). Clamp the animation
  step (`Math.min(p.deltaTime, 100)`) so a resume cannot skip ahead. The readout is DOM text, tap targets 40 px.
- Canvas text grows with `ts()` (k ≈ 2 at 360 px). Every canvas text goes through a `lab(s, x, y, align)` helper
  that draws it and pushes `{s, x0, y0, x1, y1}` (canvas coordinates) to `simState.labels`; `test_sims.py` then
  sweeps every control at 360, 390 and 1280 px by itself and fails on any overlap or clipping (fy3-9 is the
  pattern). Draw every second tick label when k > 1,5 and keep a few pixels of clearance: CI's fonts are wider.
- `tests/sims/<id>.json`: an assertion on `simState` for every control and displayed quantity (set inputs through
  the DOM, read outputs, compare within 1 %), plus the label sweep. Never loosen an assertion to make it pass.
- With inquiry.json the simulation sits where its `sim` activity is; on a wide screen the stage that holds it is a
  two-column lab: the experiments on the left, the sim on the right, moving level with the experiment the student
  starts (`inquiry.js`; on a phone the sim moves into the experiment). Without inquiry.json the page places it after
  `## Kaava` (before `## Esimerkki`); a line `<!-- sim -->` in `lesson.md` overrides the position. Exercises get a browser-side answer check; nothing is stored or sent. No third-party
  requests, fonts are self-hosted. Reviewer screenshots stay out of git (`review/shots/`).

## 5. Inquiry sequence (teacher's brief 2026-10-25)

- `inquiry.json` (format and activity types: `docs/inquiry.md`; the brief: `docs/inquiry-spec.md`). The pilot
  `content/fi/FY3/fy3-2/inquiry.json` shows the shape; do not copy it mechanically — choose activities by what the
  lesson's goals need. A lesson without a simulation investigates a table, a figure or competing explanations.
- No fixed template (2026-10-26, after the FY3 review found twelve lessons with one sequence): vary what the student
  does by the topic: read a value off a graph, fit a line, extrapolate, handle noisy data, decide what to hold
  constant, build or compare models. An experiment whose simulation only computes the formula being predicted
  confirms the program's arithmetic, not the physics; prefer one whose result emerges (pressure from counted hits).
- Options are shown shuffled (`inquiry.choice_order`): never refer to an option by letter or place, and do not let
  one speaker ("Aino:", "Bea:") be right most of the time; `check_choices.py` warns on both. (2026-10-26)
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
- The page (2026-10-26, CLAUDE.md "Lesson page"): stages Pohdinta → Ennusta → Tutki → Teoriatiivistelmä → Sovella →
  Tarkista osaamisesi, then Tehtävät last, whatever stage the `exercises` activity names; Ennusta inside a box that
  starts closed (so a prediction's wording must make sense when the student reopens it after the investigation);
  "Exit ticket" in headings and links. Every task stands in one reading column, never two side by side (§8). Look at
  the preview at 360, 768 and 1280 px; `check_layout.py --width <w>` and `test_inquiry.py <id>` test the layout.
- Core path (2026-10-26, FY3): retrieval, reflect, Etsi virhe, siirto, a third check and secondary experiments are
  `optional` unless the lesson's goal needs them; 1–2 predictions, the key investigation, a conclusion `explain` with
  `after` its experiments, and 1–2 checks stay. Lengths are not equalised. Example data carries `source`
  (docs/inquiry.md); a sim's numbers are model values in the conclusion's model answer too.

## 6. Learning from mistakes
When a reviewer finds an error that is objectively testable or has happened before: fix it, name the general
pattern, and then either add a check (`lint_lesson.py`, `test_sims.py`, `check_layout.py`, `test_inquiry.py`) with
a test that catches the original case and passes on every other lesson, or, when it cannot be checked mechanically,
add one dated line with the lesson id to the right heading above. Never both, never a paragraph. The checks run before any reviewer, so the reviewers are
paid only for what scripts cannot see. Deterministic coverage today: numbers (`answers.py` re-run against
`exercises.json`, `Vastaus` lines, significant figures and tolerances, coefficient mantissas), LaTeX (KaTeX parse,
`{,}`, `\textsf{l}`, `·` in `\text`), lesson form (figures, stages, symbolic first rows, paragraph length),
complete solutions (`check_solutions.py`: every exercise and numeric task solved with all steps, the seven example stages, `solutions: all`),
pages (`check_layout.py`, §8: overflow of formulas, tables, figures, columns and the page, SVG labels overlapping or
leaving a figure, overlapping blocks, reading order, empty columns beside an opened card or a figure, line length,
text and control size, headings under the sticky navigation; at eight widths, closed, with hints and with
everything open),
simulations (console errors, per-sim assertions, finite `simState` and label boxes at 360/390/1280 px over every
control combination), inquiry (gating, locked parameters, reveal after the experiment, every rendered option with
its own flag and feedback, navigation, 360 px, per lesson), the page form of 2026-10-26 (stage and section names, the
closed Ennusta box keeping its answers, the exercises last, the sim's controls in view and its text behind named
boxes, the wide layout and line length at 1280 and 1920 px; in the lint the law-named formula section, figure text
size and palette, the sim's lead and paragraphs), answer positions per course, publication (content hash,
change categories and carried reviews, rebuild equality, atomic build).

## 7. Exam material (inspiration only)
Exam files, if ever collected, live only in the git-ignored `docs/exams/` and are studied for patterns (task
types, contexts, how points split between reasoning and calculation), never quoted or reworded. Every exercise is
original.

## 8. Readability and layout (teacher's brief 2026-10-27, "luettavuus ja taitto")
The shared components carry the layout, so a writer never solves it per lesson and never adds CSS for one lesson.
What the writer still owns:
- **No text walls.** One main idea per paragraph, about 120 words at most (lint warns over 130). A theory section with
  several ideas gets short, content-naming `###` subheadings ("Miksi aine laajenee?", "Lämpölaajeneminen arjessa"),
  not one before every pair of sentences (model: `content/fi/FY3/fy3-8` Ydinajatus). Bold only a key definition or
  conclusion, a few words, never a sentence run. No new coloured boxes: headings, spacing and type do the work.
- **Never thin the physics to shorten text.** Keep the causal chain and the reasons (why the mean spacing of the
  particles grows when they vibrate harder, not just "they move more"); restructure, do not cut.
- **The opening** (`inquiry.json`): `learn` holds 2–3 goals from the student's side, each one line that completes the
  heading "Tällä tunnilla opit" (teacher 2026-10-29): "laskemaan …", "tunnistamaan …", "vertailemaan … ja selittämään …"
  (third infinitive illative -maan/-mään, lowercase, parallel forms; never "Osaat …"/"Opit …" under the heading).
  Selkeä suomi: the same form, shorter; a short second sentence may explain. English: "In this lesson, you will learn
  to" + "calculate …", "explain …" (bare verb, natural English, not a mirror of the Finnish). Module goals, Pohjatiedot,
  rubrics and summaries keep their own grammar. `scripts/objectives.py` checks it; the explanation belongs to the theory. `prior` is a list, one fact per item,
  ending with the chapter it comes from as `(luku *<chapter title>*)` (the page turns it into a quiet link; never an
  id). The Miksi question is one question, or two short sentences when it has two ideas. `contribution` stays as the
  reviewers' one-sentence statement of what the lesson adds; the page does not show it.
- **A figure goes right after the paragraph, table or list it explains** and nowhere else. The build sets the two
  side by side on a wide screen only when they are about as tall (`build.py fig_side`), otherwise the figure stands
  under its text; after the unit the text runs on in the reading column. So keep the paragraph a figure explains
  about the size the figure needs (roughly 40–110 words for a 600×330 figure), and put a figure that explains a
  whole subsection after that subsection's last paragraph, not after a 200-word block.
- **Calculations** stay in the source as one inline chain per step (§1, §3); the page splits long chains into
  aligned rows. A multi-line calculation written as display maths uses `aligned` with the `&` before each `=`
  (`Q &= cm\Delta T \\ &= …`); one written with every row starting `&` (`&Q = …`) is aligned at its first `=` by
  the build when that does not make it wider. The answer (Vastaus) is shown set apart, its precision reasons after
  it; Järkevyys is its own block, so it may say two things (an order-of-magnitude estimate and the energy balance).
- **Task texts**: a long task (about 28 words or more) reads as the situation and then the question; the page breaks
  it before the first sentence that asks something, so write the situation first and the question last, each a
  sentence of its own. Options are whole clickable rows; a choice's feedback, a hint and a solution open inside
  the task's own card and push the next task down, never sideways.
- **What the checks prove** (`check_layout.py`, every lesson, in CI at 360, 390, 640 (1280 at 200 % zoom), 768, 1024,
  1280, 1440 and 1920 px, each in three states: closed, first hints and solutions open, everything open): no
  overflow of the page, a formula, a figure or a column; no overlapping blocks; task cards in reading order; no
  two-column row with a large empty area beside the shorter column; text no wider than 44rem; reading text not
  under 17 px and controls not under 40 px on any width; every stage heading clear of the sticky navigation after
  its link. `screenshot.py <id>` adds rendered captures of the opening, the theory and the opened Ennusta, Tarkista,
  exit ticket and exercises at 1280 px for a human look. What no script judges: whether a figure is the right
  figure, whether a subheading names its content, whether a paragraph holds one idea, whether the goals match the
  lesson; the reviewers and the teacher see those.

## 9. Exam readiness, Sovella itsenäisesti and self-assessment (teacher's brief 2026-10-28)
The Finnish physics matriculation exam (2021–2026 papers and their *Hyvän vastauksen piirteet*) rewards six transferable
competencies (`competencies.json`): conceptual understanding, mathematical problem-solving, graphical and numerical
analysis, experimental reasoning, scientific communication and independent transfer. Graphs and data recur in every
paper (question 2 in all eleven papers 2021–spring 2026), so data and graph work belongs in every course, not only FY1.
Exam questions are studied for patterns only (§7); every task is original, with its own context and data.
- **Keep the inquiry.** Pohdinta builds curiosity, Ennusta conceptual reasoning, Tutki exploration, Teoriatiivistelmä
  explains, Sovella applies, Tarkista gives short feedback. Exam-style work does not go into every stage.
- **Chapter vs. module end.** Chapter activities optimise understanding, progression, feedback and scaffolding.
  Sovella itsenäisesti optimises independence, transfer, authentic contexts, several connected steps, written
  justification and point-based assessment. It is designed for that purpose, never the hardest exercises relabelled.
- **A Sovella itsenäisesti task**: the situation and its source material (a table, a dataset, a report, a figure)
  first; parts a), b) … with points, rising in demand, mixing explanation and calculation; one part that asks the
  student to evaluate (a result, an assumption, a conclusion, a method) where it fits. No heading or prompt names the
  law or formula ("Aurinkokeräin", not "Lämpömäärä ja hyötysuhde"); a needed constant may be given as data. Data that is
  not measured says so (`source`, `source_note`). A course's tasks vary: not all the same calculation chain.
- **Its solution** follows CLAUDE.md "Lesson form" 7 per part (`### a)`: calc parts the full steps, word parts Kysytty ·
  Periaate · Mallivastaus, graph parts Kysytty · Kuvaaja (the model graph from figures.py) · Mallivastaus), then
  `### Yleisiä virheitä` (real mistakes) and, where another method is right, `### Hyväksytään myös`.
- **Its rubric**: specific criteria worth 1–4 points each; a part's points are their sum. Use a shared key
  (graph_axes, graph_points, graph_fit, graph_read, equation, calculation, units_precision, reasonableness,
  uncertainty, error_sources, assumptions, conclusion) with a `detail` for this task's specifics; write a task-specific
  criterion with its own `tag` when no key fits. Never award points for irrelevant things. The page says the points
  are self-assessed and that the rubric is Fysiikkalabra's own, modelled on the exam's principles, not YTL's.
- **Links**: `links` maps each competency the task's criteria use to the chapter where it is practised; a student who
  gives themselves at most half of a criterion's points sees that chapter (by name). Deterministic, no model.
- **Difficulty grows with the course** (FY1 → FY8): conceptual and mathematical complexity, independence, the number of
  connected steps, the variety of sources and the expected written justification. An FY1 task is demanding for FY1
  goals, not for the whole exam; never import later-course physics to imitate a full exam question.
- **No chapter-level "Osaan / Tarvitsen" checklist** (teacher 2026-10-28, replacing the "Arvioi osaamistasi" of the
  same morning): confidence alone is not evidence. A written answer is self-assessed against its model answer's
  observable criteria (§11); a multiple-choice check needs no self-assessment; the point-based rubric stays in
  Sovella itsenäisesti.
- **Coverage, not quotas.** `python scripts/coverage.py <COURSE>` derives from each activity's form who produces what
  and how independently; a completed graph to read is not graph construction, a sim-drawn graph is not either, and a
  prompt that supplies the formula is not model choice. Close a real gap by improving or replacing a weak activity.
- **Token economy.** Write once, reuse: shared criteria texts and labels in `lang/<lang>.json`, one rubric component,
  packets without lesson texts, deterministic checks before reviews, one review pair per course's tasks, and in
  translations only new or changed text. A translation (`content/en/`, `content/fi-easy/` for Selkeä suomi) keeps the
  same tasks, points, criteria and links (`practice.py check`); Selkeä suomi clarifies the language and keeps the
  physics terms and the cognitive demand.


## 10. Physics accuracy and consistency (teacher's brief 2026-10-28, after the FY1–FY3 audit)
- `docs/physics-guardrails.md` is the short physics reference every writer and science reviewer follows: A/B/C
  findings, measurement terms, outliers, fits, a law's conditions where it is used, particles and phase changes,
  heat and efficiency, task assumptions and rubrics. One explanation is worded the same in every place it appears.
- `scripts/physics_phrases.py` warns (lint) about known wrong claims taught as fact and `test_physics_phrases.py`
  (CI) keeps the corrected ones from coming back; `scripts/concepts.py <concept>` gathers a concept's passages from
  every chapter for a cross-chapter review (README "Physics consistency"). A new recurring error: add a line to the
  guardrails, and a rule with right and wrong example sentences when it can be matched with high precision.

## 11. Figures in tasks and assessment (teacher's brief 2026-10-28, "kuvat löydettäviksi ja tehtäviin")
- **Find before you draw.** `docs/figures/catalog.json` lists every figure of every course (built by `python
  scripts/figcat.py build`, CI checks it is current): id, kind (graph, diagram, illustration, photo), the
  description (its `aria-label`), its LaTeX labels, the owner chapter's title and glossary terms, where it is used and
  what it would give away (`reuse`). Search it with `python scripts/figcat.py find <words> [--course FY3] [--kind
  graph] [--reusable]`; `figcat.py show <id>` prints one entry and the code that draws it. Never read lesson.md, a
  published page or an SVG body to look for a figure. (2026-10-28, pilot fy1-4, fy3-9)
- **Refer, do not copy.** A task shows a figure by its id: `"figure": "fy3-9/boyle-points"` on an exercise in
  exercises.json, an inquiry task (hook, text, choice, numeric, explain, interpret, or an interpret task's question)
  or a Sovella task or part. The build draws it from the one figures.py that owns it, in the page's language (that
  chapter's `figures.json`), with its LaTeX labels; the lint, `inquiry.py` and `practice.py check` fail on an unknown id
  or a decorative illustration. Never paste a figure's SVG into a task text.
- **Question-safe variants.** A theory figure may show the answer (`reuse: "reveals: …"`). Make a variant in the
  owner's figures.py from the same data, registered in FIGURES under its own name (`"scatter-points"`), without the
  result (no fitted line, no curve, no read-off guide), and give it a description that lists the data a sighted
  student reads off, not the answer. Add its note to `REUSE` ("safe: …"). A variant that only tasks use needs no
  `<svg data-fig>` block in lesson.md.
- **A figure task needs the figure.** The values the student uses come from the figure (a point on a gridline, a
  length, an arrangement), and the text does not repeat them. Choose grid crossings for values that must be read
  exactly; a by-eye fit gets a tolerance that accepts every reasonable line and the solution says the range. The
  solution has `**Kuvaajan lukeminen:**` (which points, which values). Decoration is never a figure task.
- **Reviews follow the figure.** The exercise set's hash covers the code that draws each figure it refers to (its
  FIGURES entry and the functions and data it uses), not the rest of that figures.py: a change to that figure stales
  the exercises (category `figure`), a change to another figure does not, and the lesson's own hash is untouched by
  an exercise's figure. Packets carry the figure's description and, for the science reviewer, its code; never an SVG.
- **Conceptual checks.** Tarkista osaamisesi has about 2–3 multiple-choice checks of the chapter's key concepts when
  the concepts call for them, each with misconception-based distractors and feedback of its own; prefer converting a
  good exit-ticket question or replacing a redundant task over adding one. `python scripts/assessment.py <COURSE>`
  (docs/assessment/, CI checks it is current) lists per chapter the checks, the figure tasks, the exit ticket and
  possible repeats; it is evidence for the developer and the reviewers, not a quota.
- **Exit ticket** keeps one to three quick questions that the checks and exercises do not already ask; a question
  that only repeats a check is removed, not replaced.
- **Guided self-assessment of written answers** (`explain`): own answer → model answer → observable criteria
  ("Vastaus kertoo, että …", never "Osaan …") → "Mitä vastauksestani puuttuu?" lists the unticked criteria → where to
  practise (the task's `practice`, markdown with a link, or the theory and the exercises). Criteria assess what the
  question asks. No runtime grading, nothing stored but in the student's own browser.
