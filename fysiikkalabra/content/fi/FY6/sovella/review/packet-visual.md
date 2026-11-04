# Packet: FY6-sovella (Sovella itsenäisesti, fi)
Role: **visual** (`.claude/agents/visual-editorial-reviewer.md`). Mode: **full**. Content hash now: `b106a60fd17e0ee3`.
House rules: `CLAUDE.md` (in your context). This is not a lesson: no inquiry stages, no exercises; judge the page as the Sovella itsenäisesti it is (an investigation: the student's working instructions by working mode, the figures and set-up sketches, the data tables and graphs, the teacher's notes; a guide: the screenshots of the software are the school's own and are judged for legibility and fit, not redrawn).

## Your standard (docs/EDITORIAL_QUALITY_STANDARD.md: severity and dimensions 7–10)
**Severity** (every reviewer, every dimension):
- **Critical — blocks publication**: a physically misleading statement or figure; essential information unreadable,
  clipped or missing; broken or ambiguous mathematical notation; an editorial ambiguity that changes the scientific
  meaning; an accessibility failure that prevents use of essential content.
- **Major — normally blocks**: a confusing or inconsistent diagram; clearly poor mathematical readability; a weak or
  misleading graph; a serious language or presentation problem; a structure that substantially hinders
  comprehension; (science and pedagogy keep their own Blocking criteria in their agent files).
- **Minor — polish**: small stylistic inconsistencies, decorative details, wording, subtle spacing that does not
  affect use. A subjective aesthetic preference alone is never a finding above Minor.

## 7. Illustration and diagram quality (visual)
Every figure must contribute to understanding, not decorate. Three kinds, each with its own standard:
- **Phenomenon illustrations** (the opening illustration `data-fig="hero"`, scenes): restrained, simple natural
  outlines, few fills, the figure palette on paper or white, limited environment, the phenomenon in the middle third
  so it reads at 390 px; no needless arrows, labels or decoration; not cartoonish, crowded or over-polished.
  (The house style is the flat vector style the teacher chose on 2026-10-26, NOTES.md §3 "Opening illustration";
  a slightly hand-drawn look is welcome where it suits the scene, but no restyling of existing illustrations is
  asked for.)
- **Scientific diagrams** (force, motion, circuit, ray, energy-flow, experimental set-ups): correct geometry and
  meaningful relative positions; consistent notation (`\overline{F}`, NOTES.md §1); forces and their components
  clearly apart (dashed components, `docs/force-diagrams.md`); arrow lengths that mean something and labels that read;
  no accidental relation shown that is not there; schematic or to scale said in the description. **Scientific
  correctness takes priority over style.**
- **Graphs and data visualisations** (NOTES.md §3 Graphs): quantity and unit on each axis, readable ticks, data
  points as markers distinct from a fitted model line, error bars where the uncertainty matters, simulated or
  illustrative data labelled as such, no invented points, no unexplained exaggeration, interpolation and
  extrapolation distinguished (dashed beyond the data).
Conventions that are fixed project-wide (never changed without the teacher): velocity, acceleration and force in
different colours in every figure and simulation (FY4: force red `#c92a2a`, velocity blue `#1971c2`, acceleration
orange `#e8590c`, momentum `#7048e8`); every label LaTeX; the figure palette; print quality (NOTES.md §3).
- **5** Every figure teaches the point beside it, is consistent with the others, legible at 390 px, print quality,
  with a description that gives a non-seeing reader the same information.
- **4** Good; small inconsistencies of stroke, spacing or label placement.
- **3** A figure that is hard to read on a phone, or decoration that distracts, or a description that says less than
  the figure.
- **2** A confusing or inconsistent diagram, a graph without units or with data and model indistinguishable.
- **1** A figure that shows a physically misleading situation, or essential labels clipped.

## 8. Mathematical typography (visual)
As rendered by KaTeX on the page: equations aligned at `=`; spacing around operators; fractions (`\dfrac` in display,
`\tfrac` inline); exponents, sub- and superscripts legible; `\overline{F}` vectors; Greek letters; decimal comma
`{,}` in Finnish (a simulation's canvas and readout may keep the decimal comma in every language, teacher 2026-10-31); SI units upright with a thin space (`9{,}81\,\text{m/s}^2`); `\cdot` for multiplication, a colon for
a written division, `\Delta x` for a measurement error; significant figures consistent between substitution,
answer and its justification; equations placed where the text refers to them; long chains broken at meaningful
boundaries by `mathlayout.py` (never shrunk); figure labels and simulation readouts in the same typeface. The
preferred order is **physical principle → symbolic equation → substitution → result → interpretation**. The
visual reviewer judges the presentation; mathematical correctness belongs to the science reviewer.
- **5** Every formula reads like a well-set printed book on a phone and a laptop.
- **4** Correct and readable; small spacing or alignment slips.
- **3** Inconsistent notation between sections, or a chain hard to follow at 390 px.
- **2** Significantly poor readability (cramped fractions, misaligned rows, a symbol in plain text).
- **1** Broken or ambiguous notation (red KaTeX source, a symbol that reads as another).

## 9. Finnish editorial quality (visual)
Read as an experienced Finnish science textbook editor: natural, fluent Finnish; the glossary's terms, used the
same way across the chapter; one instructional voice (the student addressed consistently); one idea per paragraph,
in a logical order; no needless repetition, ambiguity or over-long sentences; no mechanical AI phrasing ("On tärkeää
huomata, että …", stacked "Tämä tarkoittaa, että …", every paragraph ending in a summary); headings consistent in
form; exercise instructions that say exactly what to do; observations, conclusions and assumptions kept apart;
correct case after a number and unit ("$80\,\text{N}$:n voimalla", the quantity in LaTeX: NOTES §1). A complete explanation is better than a shorter
incomplete one: never shorten for brevity, never rewrite a correct sentence because another phrasing is possible.
English and Selkeä suomi versions are judged in their own language by the same standard. Selkeä suomi is also judged
for S2 students (NOTES.md §12): a difficult word or physics term explained where it first appears, abstract ideas made
concrete with a correct example, instructions that say what to do in order, *Luvun tärkeät käsitteet* that name the
chapter's central concepts in plain sentences; never fragmented, childish or padded, and the physics unchanged.
- **5** Reads like carefully authored educational prose throughout.
- **4** Fluent; a few awkward sentences.
- **3** Understandable but mechanical or repetitive in places; a term used inconsistently.
- **2** Serious language problems (errors, ambiguity, a register that changes) in several places.
- **1** An ambiguity that changes the scientific meaning, or text that is hard to follow throughout.

## 10. Accessibility and responsive usability (visual; pedagogy for the phone use of tasks)
At 390 px (phone) and 1280 px (laptop), and other widths where needed (`check_layout.py` already measures 360–1920
px in every open state): readable text, clear visual hierarchy, comfortable reading width, appropriate density,
consistent spacing, tables and figures usable on a phone, interactive tasks, opened hints and worked solutions
inside their cards, simulation labels and controls, contrast, alt text and figure descriptions, keyboard focus and
navigation where relevant, nothing clipped, no horizontal overflow, nothing misleading. The front page's compact
FY01–FY08 overview and the immediately visible school-specific courses stay; no large decorative cards or excess
whitespace anywhere.
- **5** Everything usable and pleasant at every width; deterministic checks clean.
- **4** Usable; a minor spacing or density issue.
- **3** One element awkward on a phone (a wide table, a crowded simulation readout).
- **2** Poor structure that hinders use, or a description missing for an essential figure.
- **1** Essential content unusable (clipped, unreadable, unreachable by keyboard).

## House rules you apply (NOTES.md)
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
  an `aria-label` stays plain text. **Standing rule (teacher 2026-11-01, "jatkossa näin"):** the whole quantity, number
  and unit, is one inline formula in every language (fi, en, fi-easy) and every text a student reads (`lesson.md`,
  `inquiry.json` with its choices and feedback, `exercises.json`, `solutions.md`, `exit-ticket.json`): "noin 10 N" →
  "noin $10\,\text{N}$", "1,18 kN" → "$1{,}18\,\text{kN}$", "9,81 m/s²" → "$9{,}81\,\text{m/s}^2$", "45 m²" →
  "$45\,\text{m}^2$", case endings after the maths ("$12\,\text{N}$:n", "$1\,\text{N}$:ksi"). A lesson written
  or edited from now on has none in plain text (`lint_lesson.py` PLAIN_QTY: an error for a lesson being edited, a
  warning in a reviewed one until it is next edited); a reviewer reports a plain one in new or edited text as Major,
  in untouched reviewed text as Minor. The experiments' Alkutila line and table headers turn
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
- **No text walls.** One main idea per paragraph, about 120 words at most (lint warns over 130). A theory section with
  several ideas gets short, content-naming `###` subheadings ("Miksi aine laajenee?", "Lämpölaajeneminen arjessa"),
  not one before every pair of sentences (model: `content/fi/FY3/fy3-8` Ydinajatus). Bold only a key definition or
  conclusion, a few words, never a sentence run. No new coloured boxes: headings, spacing and type do the work.
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

## The text you judge (figure bodies collapsed)

### content/fi/FY6/sovella/tasks.json
```json
{
  "intro": "Neljä tehtävää kokoaa moduulin: pariston mittauksen, virtapiirin, sähkökentän ja kondensaattorin. Jokaisessa päätät itse, mitkä mallit tilanteeseen sopivat, ja perustelet valintasi.",
  "tasks": [
    {
      "id": "fy6-s1",
      "title": "Taskulampun paristo",
      "source": "example",
      "source_note": "Mittaustulokset on laadittu tehtävää varten, mutta ne ovat samaa suuruusluokkaa kuin uuden litteän taskulamppupariston mittauksessa.",
      "text": "Oppilas tutkii uutta litteää taskulamppuparistoa, jonka kyljessä lukee $4{,}5\\,\\text{V}$. Hän kytkee paristoon säädettävän vastuksen ja ampeerimittarin sekä jännitemittarin suoraan pariston napoihin (kuva). Hän säätää vastuksesta virran ja lukee sitä vastaavan napajännitteen $U$. Mittarit näyttävät virran $0{,}01\\,\\text{A}$:n ja jännitteen $0{,}01\\,\\text{V}$:n tarkkuudella. Oppilas mittasi virran kasvavassa järjestyksessä, ja piiri oli kytkettynä kunkin lukeman ajan noin minuutin. Paristo lämpeni mittausten aikana hieman, ja jännite näytti laskevan hitaasti myös silloin, kun virtaa ei muutettu. Sarjan jälkeen oppilas mittasi jännitteen vielä kerran virralla $0{,}10\\,\\text{A}$: lukema oli $4{,}45\\,\\text{V}$ eli $0{,}03\\,\\text{V}$ pienempi kuin sarjan alussa.\n\nMittaustulokset (virta $I$, napajännite $U$):\n\n- $I = 0{,}10\\,\\text{A}$, $U = 4{,}48\\,\\text{V}$\n- $I = 0{,}20\\,\\text{A}$, $U = 4{,}37\\,\\text{V}$\n- $I = 0{,}30\\,\\text{A}$, $U = 4{,}22\\,\\text{V}$\n- $I = 0{,}40\\,\\text{A}$, $U = 4{,}13\\,\\text{V}$\n- $I = 0{,}50\\,\\text{A}$, $U = 3{,}99\\,\\text{V}$\n- $I = 0{,}60\\,\\text{A}$, $U = 3{,}89\\,\\text{V}$",
      "figure": "fy6-sovella/fy6-s1-circuit",
      "parts": [
        {
          "id": "a",
          "kind": "graph",
          "points": 4,
          "text": "Oppilas haluaa selvittää, millaisena jännitelähteenä paristo toimii. Mallinna paristoa ja muodosta aineistosta kuvaaja, jonka pisteisiin mallin mukaan sopii suora.",
          "criteria": [
            {
              "text": "Mallintaa pariston ideaaliseksi jännitelähteeksi ja sen kanssa sarjassa olevaksi sisäiseksi resistanssiksi, jolloin napajännite on $U = E - R_\\text{s} I$, ja valitsee kuvaajan suureiksi $I$ ja $U$.",
              "tag": "transfer",
              "points": 1
            },
            {
              "key": "graph_axes",
              "points": 1,
              "detail": "$I\\ (\\text{A})$ vaaka-akselilla ja $U\\ (\\text{V})$ pystyakselilla; pystyakselin ei tarvitse alkaa nollasta, jos asteikko on merkitty."
            },
            {
              "key": "graph_points",
              "points": 1
            },
            {
              "key": "graph_fit",
              "points": 1,
              "detail": "Suora kulkee pisteiden lomitse ja sitä on jatkettu pystyakselille asti."
            }
          ]
        },
        {
          "id": "b",
          "kind": "calc",
          "points": 4,
          "text": "Määritä kuvaajasta pariston lähdejännite $E$ ja sisäinen resistanssi $R_\\text{s}$.",
          "answer": [
            {
              "name": "E",
              "value": 4.6,
              "unit": "V",
              "tolerance": 0.03
            },
            {
              "name": "Rs",
              "value": 1.2,
              "unit": "Ω",
              "tolerance": 0.09
            }
          ],
          "criteria": [
            {
              "key": "graph_read",
              "points": 1,
              "detail": "Kulmakerroin $\\dfrac{\\Delta U}{\\Delta I} \\approx -1{,}2\\,\\text{V/A}$ on luettu piirretyn suoran kahdesta kaukana toisistaan olevasta pisteestä, esimerkiksi $(0{,}10\\,\\text{A};\\ 4{,}48\\,\\text{V})$ ja $(0{,}60\\,\\text{A};\\ 3{,}88\\,\\text{V})$, ei vierekkäisistä mittauspisteistä."
            },
            {
              "key": "equation",
              "points": 1,
              "detail": "$U = E - R_\\text{s} I$: $E$ on suoran ja pystyakselin leikkauskohta ($I = 0$) ja $R_\\text{s}$ kulmakertoimen vastaluku."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$R_\\text{s} = \\dfrac{0{,}60\\,\\text{V}}{0{,}50\\,\\text{A}}$ ja $E = 4{,}48\\,\\text{V} + R_\\text{s} \\cdot 0{,}10\\,\\text{A}$ tai leikkauskohta luettuna suoralta."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$E \\approx 4{,}6\\,\\text{V}$ ja $R_\\text{s} \\approx 1{,}2\\,\\Omega$"
            }
          ]
        },
        {
          "id": "c",
          "kind": "calc",
          "points": 3,
          "text": "Paristoon kytketään $8{,}0\\,\\Omega$:n vastus. Kuinka suuri teho vastukseen siirtyy, ja kuinka suuri osa pariston koko sähkötehosta siirtyy lämpönä pariston sisäisessä resistanssissa?",
          "answer": [
            {
              "name": "P",
              "value": 2.0,
              "unit": "W",
              "tolerance": 0.03
            },
            {
              "name": "osuus",
              "value": 13,
              "unit": "%",
              "tolerance": 0.05
            }
          ],
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "$I = \\dfrac{E}{R + R_\\text{s}}$, vastuksen teho $P = R I^2$ ja pariston sisällä $P_\\text{s} = R_\\text{s} I^2$; osuus on $\\dfrac{P_\\text{s}}{P + P_\\text{s}}$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$I = 0{,}50\\,\\text{A}$, $P = 2{,}0\\,\\text{W}$ ja $P_\\text{s} = 0{,}30\\,\\text{W}$."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$P \\approx 2{,}0\\,\\text{W}$ ja osuus noin $13\\,\\%$"
            }
          ]
        },
        {
          "id": "d",
          "kind": "word",
          "points": 4,
          "text": "Arvioi, miten pariston purkautuminen ja lämpeneminen vaikuttavat b-kohdan tulokseen. Arvioi myös, kuinka paljon pisteiden hajonta jättää $R_\\text{s}$:n arvoon epävarmuutta (pisteet poikkeavat sovitetusta suorasta enintään $0{,}02\\,\\text{V}$), ja ehdota mittaukseen parannus.",
          "criteria": [
            {
              "key": "error_sources",
              "points": 1,
              "detail": "Pariston purkautuminen laskee jännitettä sarjan aikana, joten myöhemmin mitatut jännitteet (suuremmat virrat) ovat liian pieniä: suora on liian jyrkkä ja $R_\\text{s}$ tulee liian suureksi (systemaattinen virhe). Koska virtaa kasvatettiin vain yhteen suuntaan, ajan vaikutus sekoittuu kulmakertoimeen. Lämpeneminen muuttaa myös $R_\\text{s}$:ää mittauksen aikana (yleensä pienentää sitä), joten sen suunta on epävarma."
            },
            {
              "key": "uncertainty",
              "points": 1,
              "detail": "Ääriviivojen kulmakertoimet poikkeavat toisistaan $\\dfrac{2 \\cdot 0{,}02\\,\\text{V}}{0{,}50\\,\\text{A}} = 0{,}08\\,\\Omega$, joten $R_\\text{s} = (1{,}20 \\pm 0{,}08)\\,\\Omega$ pelkän hajonnan perusteella."
            },
            {
              "text": "Ehdottaa parannuksen, joka vähentää purkautumisen vaikutusta: virrat satunnaisessa järjestyksessä, piiri kytkettynä vain lukeman ajan tai sarja toistettuna käänteisessä järjestyksessä ja tulosten vertailu.",
              "tag": "experiment",
              "points": 1
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Arvioi ajautuman vaikutuksen: jännite laski sarjan aikana noin $0{,}03\\,\\text{V}$, joten kulmakerroin on enintään noin $\\dfrac{0{,}03\\,\\text{V}}{0{,}50\\,\\text{A}} = 0{,}06\\,\\Omega$ liian suuri. Se on samaa suuruusluokkaa kuin hajonnan $0{,}08\\,\\Omega$, joten $R_\\text{s}$ on noin $1{,}1\\ldots1{,}2\\,\\Omega$ ja arvo $1{,}2\\,\\Omega$ on pikemmin yläraja."
            }
          ]
        }
      ],
      "links": {
        "transfer": "fy6-8",
        "math": "fy6-8",
        "graph": "fy6-8",
        "experiment": "fy6-2",
        "communication": "fy6-8"
      }
    },
    {
      "id": "fy6-s2",
      "title": "Mökin pihavalot",
      "source": "example",
      "source_note": "Kaapelin resistanssi ja lamppujen tiedot ovat keksittyjä, mutta samaa suuruusluokkaa kuin 12 voltin mökkisähköjärjestelmässä.",
      "text": "Mökin pihavalot saavat sähkönsä $12{,}0\\,\\text{V}$:n akustosta. Akustolta lamppuihin johtaa pitkä kaapeli, jonka molempien johtimien yhteinen resistanssi on $0{,}80\\,\\Omega$. Piirissä on akuston jälkeen sulake. Kaapelin päässä on kaksi rinnan kytkettyä lamppua (kuva). Lamppu A on merkitty $12\\,\\text{V},\\ 24\\,\\text{W}$ ja lamppu B $12\\,\\text{V},\\ 12\\,\\text{W}$: merkintä kertoo tehon, kun lamppuun kytketään nimellisjännite. Oleta lamppujen resistanssit vakioiksi. Akuston sisäinen resistanssi on niin pieni, että sen voi jättää huomiotta.\n\nMuita tietoja:\n\n- sulakkeen nimellisvirta on $3{,}15\\,\\text{A}$\n- kaapeli kestää pitkäaikaisesti enintään $4{,}0\\,\\text{A}$ virran",
      "figure": "fy6-sovella/fy6-s2-circuit",
      "parts": [
        {
          "id": "a",
          "kind": "calc",
          "points": 4,
          "text": "Kuinka suuri virta kulkee akustosta, kun molemmat lamput palavat?",
          "answer": {
            "value": 2.5,
            "unit": "A",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "text": "Hahmottaa piirin: kaapeli on sarjassa rinnankytkettyjen lamppujen kanssa, ja laskee lamppujen resistanssit nimellisarvoista, esimerkiksi $R = \\dfrac{U^2}{P}$: $R_\\text{A} = 6{,}0\\,\\Omega$ ja $R_\\text{B} = 12\\,\\Omega$.",
              "tag": "transfer",
              "points": 1
            },
            {
              "key": "equation",
              "points": 1,
              "detail": "$\\dfrac{1}{R_\\text{r}} = \\dfrac{1}{R_\\text{A}} + \\dfrac{1}{R_\\text{B}}$, $R = R_\\text{k} + R_\\text{r}$ ja $I = \\dfrac{E}{R}$ ratkaistuna ennen lukuarvoja."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$R_\\text{r} = 4{,}0\\,\\Omega$ ja $R = 4{,}8\\,\\Omega$."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$I = 2{,}5\\,\\text{A}$"
            }
          ]
        },
        {
          "id": "b",
          "kind": "calc",
          "points": 3,
          "text": "Kuinka suuri teho lamppuun A todellisuudessa siirtyy? Vertaa tulosta lampun nimellistehoon.",
          "answer": {
            "value": 16.7,
            "unit": "W",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "Silmukkasääntö $E - R_\\text{k} I - U_\\text{L} = 0$ antaa lamppujen jännitteen $U_\\text{L} = E - R_\\text{k} I$; lampun teho $P = \\dfrac{U_\\text{L}^2}{R_\\text{A}}$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$U_\\text{L} = 12{,}0\\,\\text{V} - 0{,}80\\,\\Omega \\cdot 2{,}5\\,\\text{A} = 10{,}0\\,\\text{V}$ ja $P_\\text{A} = \\dfrac{(10{,}0\\,\\text{V})^2}{6{,}0\\,\\Omega} = 16{,}7\\,\\text{W}$."
            },
            {
              "key": "reasonableness",
              "points": 1,
              "detail": "$17\\,\\text{W}$ on vähemmän kuin nimellinen $24\\,\\text{W}$, koska kaapelin jännitehäviö jättää lampulle alle $12\\,\\text{V}$. Tarkistus: akuston teho $30\\,\\text{W}$ on $16{,}7\\,\\text{W} + 8{,}3\\,\\text{W} + 5{,}0\\,\\text{W}$."
            }
          ]
        },
        {
          "id": "c",
          "kind": "word",
          "points": 4,
          "text": "Lamppu B palaa loppuun, eikä se enää johda virtaa. Miten lampun A kirkkaus, akuston virta ja kaapelin lämpeneminen muuttuvat? Perustele, ja tarkista perustelusi laskemalla lampun A teho.",
          "criteria": [
            {
              "text": "Päättelee, että kokonaisresistanssi kasvaa, kun toinen rinnakkainen haara poistuu, joten akuston virta pienenee: $I = \\dfrac{12{,}0\\,\\text{V}}{6{,}8\\,\\Omega} \\approx 1{,}8\\,\\text{A}$.",
              "tag": "concept",
              "points": 1
            },
            {
              "text": "Perustelee, että pienempi virta pienentää jännitehäviötä kaapelissa ($R_\\text{k} I$ pienenee), jolloin lampulle A jää suurempi jännite ja se palaa kirkkaammin, vaikka sen oma haara ei muuttunut.",
              "tag": "concept",
              "points": 1
            },
            {
              "text": "Laskee lampun A tehon: $U_\\text{A} \\approx 10{,}6\\,\\text{V}$ ja $P_\\text{A} \\approx 18{,}7\\,\\text{W}$, aiemmin $16{,}7\\,\\text{W}$.",
              "tag": "math",
              "points": 1
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Toteaa, että rinnankytketyt lamput eivät ole täysin toisistaan riippumattomia, kun kaapelilla on resistanssi: jos kaapelin resistanssi olisi nolla, lampun A kirkkaus ei muuttuisi."
            }
          ]
        },
        {
          "id": "d",
          "kind": "calc",
          "points": 4,
          "text": "Omistaja lisää piiriin rinnan kolmannen lampun C, joka on merkitty $12\\,\\text{V},\\ 36\\,\\text{W}$. Kuinka suuri virta akustosta tulee nyt kulkemaan? Mitä sulakkeelle tapahtuu, ja miksi sulakkeen nimellisvirta on valittu kaapelin mukaan? Laske myös lamppujen jännite.",
          "answer": {
            "value": 4.3,
            "unit": "A",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "Kolme rinnakkaista lamppua: $\\dfrac{1}{R_\\text{r}} = \\dfrac{1}{R_\\text{A}} + \\dfrac{1}{R_\\text{B}} + \\dfrac{1}{R_\\text{C}}$ ja $I = \\dfrac{E}{R_\\text{k} + R_\\text{r}}$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$R_\\text{C} = \\dfrac{(12\\,\\text{V})^2}{36\\,\\text{W}} = 4{,}0\\,\\Omega$, $R_\\text{r} = 2{,}0\\,\\Omega$ ja $I = \\dfrac{12{,}0\\,\\text{V}}{2{,}8\\,\\Omega} = 4{,}3\\,\\text{A}$."
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Virta $4{,}3\\,\\text{A}$ ylittää sulakkeen $3{,}15\\,\\text{A}$ ja kaapelin sallitun $4{,}0\\,\\text{A}$, joten sulake todennäköisesti palaa ylivirran jatkuessa ja katkaisee piirin; sulakkeen toiminta-aika on yksinkertaistettu, sillä pieni ylivirta voi kestää hetken. Sulake mitoitetaan suojaamaan heikointa osaa eli kaapelia, joten sen nimellisvirta on kaapelin sallittua virtaa pienempi."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "Lamppujen jännite on $R_\\text{r} I = 2{,}0\\,\\Omega \\cdot 4{,}3\\,\\text{A} \\approx 8{,}6\\,\\text{V}$, joten lamput palavat himmeämmin kuin $10{,}0\\,\\text{V}$:n jännitteellä."
            }
          ]
        }
      ],
      "links": {
        "transfer": "fy6-4",
        "math": "fy6-5",
        "concept": "fy6-6",
        "communication": "fy6-5"
      }
    },
    {
      "id": "fy6-s3",
      "title": "Ruiskumaalaus",
      "source": "example",
      "source_note": "Suuruusluokat ovat samaa luokkaa kuin teollisessa sähköstaattisessa ruiskumaalauksessa, mutta tehtävän arvot on pyöristetty ja yksinkertaistettu.",
      "text": "Autonosa maalataan sähköstaattisella ruiskulla. Suutinlevyn potentiaali on $+60\\,\\text{kV}$ ja maadoitettu työkappale on $20\\,\\text{cm}$:n päässä. Suuttimesta lähtevät maalipisarat saavat positiivisen varauksen, ja ne kulkevat työkappaletta kohti. Oletetaan, että suutinlevyn ja työkappaleen välinen sähkökenttä on homogeeninen (kuva).\n\nYksi maalipisara:\n\n- massa $4{,}0 \\cdot 10^{-10}\\,\\text{kg}$\n- varaus $q = +6{,}0 \\cdot 10^{-13}\\,\\text{C}$\n- lähtee levossa suutinlevyltä\n\nMuita tietoja: ilman läpilyöntilujuus on noin $3\\,\\text{MV/m}$, putoamiskiihtyvyys $9{,}81\\,\\text{m/s}^2$ ja Coulombin lain vakio $k = 8{,}988 \\cdot 10^{9}\\,\\tfrac{\\text{N}\\cdot\\text{m}^2}{\\text{C}^2}$.",
      "figure": "fy6-sovella/fy6-s3-field",
      "parts": [
        {
          "id": "a",
          "kind": "calc",
          "points": 4,
          "text": "Kuinka suuri sähkövoima pisaraan vaikuttaa? Onko pisaran painon huomiotta jättäminen perusteltua, ja syntyykö kenttään kipinöintiä?",
          "answer": {
            "value": 1.8e-07,
            "unit": "N",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "Homogeenisessa kentässä $E = \\dfrac{U}{d}$ ja pisaraan vaikuttaa voima $F = qE$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$E = \\dfrac{60\\,000\\,\\text{V}}{0{,}20\\,\\text{m}} = 3{,}0 \\cdot 10^{5}\\,\\text{V/m}$"
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$F \\approx 1{,}8 \\cdot 10^{-7}\\,\\text{N}$"
            },
            {
              "key": "reasonableness",
              "points": 1,
              "detail": "Paino $mg \\approx 3{,}9 \\cdot 10^{-9}\\,\\text{N}$ on vain noin $2\\,\\%$ sähkövoimasta, joten sen voi jättää huomiotta. Kenttä on noin kymmenesosa ilman läpilyöntilujuudesta, joten kipinöintiä ei synny."
            }
          ]
        },
        {
          "id": "b",
          "kind": "calc",
          "points": 4,
          "text": "Kuinka suurella nopeudella pisara osuu työkappaleeseen, kun ilmanvastusta ei oteta huomioon?",
          "answer": {
            "value": 13.4,
            "unit": "m/s",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "text": "Valitsee energiaperiaatteen: sähkökentän tekemä työ $qU$ kasvattaa pisaran liike-energiaa, kun paino ja ilmanvastus jätetään pois; kentän voimakkuutta tai kiihtyvyyttä ei tarvita.",
              "tag": "transfer",
              "points": 1
            },
            {
              "key": "equation",
              "points": 1,
              "detail": "$q U = \\dfrac{1}{2} m v^2$, josta $v = \\sqrt{\\dfrac{2 q U}{m}}$; $U$ on suutinlevyn ja työkappaleen potentiaaliero."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$qU = 6{,}0 \\cdot 10^{-13}\\,\\text{C} \\cdot 6{,}0 \\cdot 10^{4}\\,\\text{V} = 3{,}6 \\cdot 10^{-8}\\,\\text{J}$ ja $v = \\sqrt{\\dfrac{2 \\cdot 3{,}6 \\cdot 10^{-8}\\,\\text{J}}{4{,}0 \\cdot 10^{-10}\\,\\text{kg}}}$."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$v \\approx 13\\,\\text{m/s}$"
            }
          ]
        },
        {
          "id": "c",
          "kind": "word",
          "points": 4,
          "text": "Mittauksessa pisaroiden osumanopeudeksi saadaan noin $5{,}0\\,\\text{m/s}$. Selitä, miksi se on paljon pienempi kuin b-kohdan tulos, ja päättele, minne sähkökentän tekemä työ jää.",
          "criteria": [
            {
              "text": "Tunnistaa, että b-kohdan malli jätti ilmanvastuksen pois: ilma vastustaa pisaran liikettä, ja nopeuden kasvaessa ilmanvastus kasvaa, kunnes se on likimain yhtä suuri kuin sähkövoima.",
              "tag": "concept",
              "points": 1
            },
            {
              "text": "Laskee todellisen liike-energian $\\dfrac{1}{2} m v^2 = 5{,}0 \\cdot 10^{-9}\\,\\text{J}$ ja vertaa sitä kentän tekemään työhön $3{,}6 \\cdot 10^{-8}\\,\\text{J}$: se on vain noin $14\\,\\%$.",
              "tag": "math",
              "points": 1
            },
            {
              "text": "Päättelee, että loput noin $3{,}1 \\cdot 10^{-8}\\,\\text{J}$ siirtyy ilmaan: ilman sisäenergia kasvaa ja energia siirtyy edelleen lämpönä ympäristöön. Energia ei häviä.",
              "tag": "concept",
              "points": 1
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Päättelee, että b-kohdan tulos on ilmanvastuksen puuttuessa suurin mahdollinen nopeus (yläraja) ja että energia ei häviä vaan siirtyy ilmaan."
            }
          ]
        },
        {
          "id": "d",
          "kind": "calc",
          "points": 4,
          "text": "Kaksi vierekkäistä pisaraa on $1{,}0\\,\\text{mm}$:n päässä toisistaan, ja kummankin varaus on $+6{,}0 \\cdot 10^{-13}\\,\\text{C}$. Kuinka suuri voima pisaroiden välillä on? Mitä tulos kertoo pisarapilven käyttäytymisestä?",
          "answer": {
            "value": 3.2e-09,
            "unit": "N",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "Coulombin laki pistemäisille varauksille: $F = k\\dfrac{q_1 q_2}{r^2}$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "Muunnos $1{,}0\\,\\text{mm} = 1{,}0 \\cdot 10^{-3}\\,\\text{m}$; $F = 8{,}988 \\cdot 10^{9}\\,\\tfrac{\\text{N}\\cdot\\text{m}^2}{\\text{C}^2} \\cdot \\dfrac{(6{,}0 \\cdot 10^{-13}\\,\\text{C})^2}{(1{,}0 \\cdot 10^{-3}\\,\\text{m})^2}$."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$F \\approx 3{,}2 \\cdot 10^{-9}\\,\\text{N}$"
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Samanmerkkiset varaukset hylkivät toisiaan, joten pisarapilvi levenee sivusuunnassa. Voima on noin $2\\,\\%$ kentän voimasta mutta lähes saman suuruinen kuin pisaran paino ($0{,}8$-kertainen), joten pisarat kulkevat silti kohti työkappaletta mutta leviävät."
            }
          ]
        }
      ],
      "links": {
        "transfer": "fy6-12",
        "math": "fy6-11",
        "concept": "fy6-11",
        "communication": "fy6-10"
      }
    },
    {
      "id": "fy6-s4",
      "title": "Kameran salama",
      "source": "example",
      "source_note": "Kondensaattorin arvot ovat samaa suuruusluokkaa kuin kameran salamalaitteessa, mutta ne on valittu tehtävää varten.",
      "text": "Kameran salamalaitteessa pieni paristo lataa kondensaattorin jännitettä nostavan piirin avulla jännitteeseen $300\\,\\text{V}$. Kondensaattorin kapasitanssi on $330\\,\\mu\\text{F}$. Kun salama välähtää, kondensaattori purkautuu salamaputken kautta noin $1{,}0\\,\\text{ms}$:ssa, ja sen jännite laskee arvoon $220\\,\\text{V}$. Salamaan siirtynyt energia lähtee laitteesta valona ja lämpönä.",
      "parts": [
        {
          "id": "a",
          "kind": "calc",
          "points": 3,
          "text": "Kuinka suuri energia on varastoituneena kondensaattoriin ennen salamaa?",
          "answer": {
            "value": 14.85,
            "unit": "J",
            "tolerance": 0.02
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "Kondensaattorin energia $E = \\dfrac{1}{2} C U^2$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "Muunnos $330\\,\\mu\\text{F} = 330 \\cdot 10^{-6}\\,\\text{F}$; $E = \\dfrac{1}{2} \\cdot 330 \\cdot 10^{-6}\\,\\text{F} \\cdot (300\\,\\text{V})^2$."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$E \\approx 15\\,\\text{J}$"
            }
          ]
        },
        {
          "id": "b",
          "kind": "calc",
          "points": 4,
          "text": "Kuinka suuri energia siirtyi salamaan? Kuinka suuri osa varastoidusta energiasta tämä on, ja miksi osuus on suurempi kuin jännitteen pieneneminen?",
          "answer": {
            "value": 6.86,
            "unit": "J",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "text": "Päättelee, että salamaan siirtynyt energia on kondensaattorin energian muutos: energiat lasketaan erikseen ennen ja jälkeen eikä jännitteen muutoksella $\\Delta U$ yksin.",
              "tag": "transfer",
              "points": 1
            },
            {
              "key": "equation",
              "points": 1,
              "detail": "$\\Delta E = \\dfrac{1}{2} C U_1^2 - \\dfrac{1}{2} C U_2^2$"
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$E_2 = \\dfrac{1}{2} \\cdot 330 \\cdot 10^{-6}\\,\\text{F} \\cdot (220\\,\\text{V})^2 = 7{,}99\\,\\text{J}$ ja $\\Delta E = 14{,}85\\,\\text{J} - 7{,}99\\,\\text{J} = 6{,}9\\,\\text{J}$."
            },
            {
              "key": "reasonableness",
              "points": 1,
              "detail": "Osuus on noin $46\\,\\%$, vaikka jännite pieneni vain noin $27\\,\\%$, koska energia riippuu jännitteen neliöstä: $1 - \\left(\\dfrac{220}{300}\\right)^2 \\approx 0{,}46$."
            }
          ]
        },
        {
          "id": "c",
          "kind": "calc",
          "points": 3,
          "text": "Kuinka suuri on kondensaattorista salaman aikana kulkenut keskimääräinen virta?",
          "answer": {
            "value": 26.4,
            "unit": "A",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "$I = \\dfrac{\\Delta Q}{\\Delta t}$, missä siirtynyt varaus $\\Delta Q = C\\,\\Delta U$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$\\Delta Q = 330 \\cdot 10^{-6}\\,\\text{F} \\cdot 80\\,\\text{V} = 0{,}0264\\,\\text{C}$ ja $\\Delta t = 1{,}0 \\cdot 10^{-3}\\,\\text{s}$."
            },
            {
              "key": "reasonableness",
              "points": 1,
              "detail": "$I \\approx 26\\,\\text{A}$ ja keskiteho $\\dfrac{6{,}9\\,\\text{J}}{1{,}0\\,\\text{ms}} \\approx 6{,}9\\,\\text{kW}$ ovat paljon suurempia kuin pieni paristo voisi antaa näin lyhyessä pulssissa; siksi energia varastoidaan ensin kondensaattoriin."
            }
          ]
        },
        {
          "id": "d",
          "kind": "word",
          "points": 4,
          "text": "Korjaaja irrottaa salamalaitteesta pariston ja avaa laitteen heti sen jälkeen. Arvioi, onko kondensaattorissa vaaraa, ja kuvaile, miten kondensaattori puretaan turvallisesti. Arvioi vaaraa myös laskemalla virta, jos ihmisen kehon resistanssi on noin $1{,}0\\,\\text{k}\\Omega$.",
          "criteria": [
            {
              "text": "Tietää, että kondensaattori säilyttää varauksensa ja energiansa, kun paristo irrotetaan: se on edelleen $300\\,\\text{V}$:ssa ja siinä on noin $15\\,\\text{J}$, vaikka laitetta syöttää pieni paristo.",
              "tag": "concept",
              "points": 1
            },
            {
              "text": "Laskee virran kehon läpi: $I = \\dfrac{U}{R} = \\dfrac{300\\,\\text{V}}{1{,}0 \\cdot 10^{3}\\,\\Omega} = 0{,}30\\,\\text{A}$, mikä on moninkertainen verrattuna muutamaan kymmeneen milliampeeriin, jotka voivat jo olla vaarallisia.",
              "tag": "math",
              "points": 1
            },
            {
              "text": "Kuvaa turvallisen purkamisen: napojen väliin kytketään eristetyillä työkaluilla sopiva vastus, esimerkiksi $10\\,\\text{k}\\Omega$, jolloin energia siirtyy vastuksen sisäenergiaksi ja edelleen lämpönä ympäristöön; alkuvirta on $\\dfrac{300\\,\\text{V}}{10\\,\\text{k}\\Omega} = 30\\,\\text{mA}$. Napoja ei oikosulkuteta, ja jännite varmistetaan mittarilla. Vastuksen on kestettävä alussa noin $\\dfrac{(300\\,\\text{V})^2}{10\\,\\text{k}\\Omega} = 9\\,\\text{W}$, joten sen tehonkesto on valittava sen mukaan. Kuvaus on tarkoitettu ymmärtämiseen: älä yritä purkaa itse.",
              "tag": "concept",
              "points": 1
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Päättelee, että laitetta ei saa avata heti: vaara johtuu varastoituneesta energiasta ja jännitteestä eikä pariston koosta. Kehon resistanssi vaihtelee (esimerkiksi kostea iho), joten arvio on suuruusluokka."
            }
          ]
        }
      ],
      "links": {
        "transfer": "fy6-13",
        "math": "fy6-13",
        "concept": "fy6-15",
        "communication": "fy6-15"
      }
    }
  ]
}
```

### content/fi/FY6/sovella/solutions.md
```markdown
## fy6-s1

### a)
**Kysytty:** kuvaaja, jonka pisteisiin pariston mallin mukaan sopii suora
**Kuvaaja:** Paristo mallinnetaan ideaaliseksi jännitelähteeksi, jonka lähdejännite on $E$, ja sen kanssa sarjassa olevaksi sisäiseksi resistanssiksi $R_\text{s}$. Kun paristosta kulkee virta $I$, sisäisen resistanssin yli on jännite $R_\text{s} I$, ja napajännite on $U = E - R_\text{s} I$. Tämä on suoran yhtälö: kun virta $I$ on vaaka-akselilla ja napajännite $U$ pystyakselilla, suora leikkaa pystyakselin kohdassa $E$ ja sen kulmakerroin on $-R_\text{s}$. Mittaukset viedään siis kuvaajaan sellaisinaan.

| $I\ (\text{A})$ | $U\ (\text{V})$ |
|---|---|
| $0{,}10$ | $4{,}48$ |
| $0{,}20$ | $4{,}37$ |
| $0{,}30$ | $4{,}22$ |
| $0{,}40$ | $4{,}13$ |
| $0{,}50$ | $3{,}99$ |
| $0{,}60$ | $3{,}89$ |

Pystyakselin asteikko alkaa arvosta $3{,}6\,\text{V}$, jotta pisteiden vähäinen lasku erottuu, ja alku on merkitty kuvaan.

<svg data-fig="fy6-s1-graph" viewBox="0 0 600 380" role="img" aria-label="Kuvaaja: pariston napajännite U voltteina virran I funktiona ampeereina. Kuusi mustaa … <!-- figure body omitted (lines 18–85): see the inventory and the captures --></svg>

**Mallivastaus:** Kuusi pistettä asettuu lähes samalle suoralle, joten malli $U = E - R_\text{s} I$ kuvaa pariston käyttäytymistä mittausalueella hyvin: napajännite pienenee tasaisesti virran kasvaessa. Suora on sovitettu pisteiden lomitse eikä pisteitä ole yhdistetty murtoviivaksi. Suoraa on jatkettu katkoviivana pystyakselille, jotta lähdejännitteen kohta $I = 0$ näkyy.

### b)
**Annettu:** a-kohdan suora, jolta luetaan pisteet $(0{,}10\,\text{A};\ 4{,}48\,\text{V})$ ja $(0{,}60\,\text{A};\ 3{,}88\,\text{V})$
**Kysytty:** lähdejännite $E$ ja sisäinen resistanssi $R_\text{s}$
**Periaate:** Mallin mukaan napajännite on $U = E - R_\text{s} I$. Suoran leikkauskohta pystyakselilla on virran arvolla nolla, jolloin pariston sisällä ei synny jännitehäviötä, joten leikkauskohta on $E$. Kulmakerroin kertoo, kuinka paljon napajännite laskee virran kasvaessa, joten se on $-R_\text{s}$.
**Kuvaajan lukeminen:** Kulmakerroin luetaan piirretyn suoran kahdesta kaukana toisistaan olevasta pisteestä eikä vierekkäisistä mittauspisteistä: $(0{,}10\,\text{A};\ 4{,}48\,\text{V})$ ja $(0{,}60\,\text{A};\ 3{,}88\,\text{V})$. Niiden välillä $\Delta I = 0{,}50\,\text{A}$ ja $\Delta U = -0{,}60\,\text{V}$ (kuvaajan kulmakertoimen kolmio). Suora leikkaa pystyakselin kohdassa $4{,}60\,\text{V}$.
**Kaava:** $R_\text{s} = -\dfrac{\Delta U}{\Delta I}$ ja $E = U + R_\text{s} I$ mistä tahansa suoran pisteestä.
**Muunnokset:** Ei tarvita: jännite on voltteina ja virta ampeereina, ja $1\,\text{V/A} = 1\,\Omega$.
**Sijoitus:** $R_\text{s} = -\dfrac{-0{,}60\,\text{V}}{0{,}50\,\text{A}} = 1{,}2\,\Omega$ ja $E = 4{,}48\,\text{V} + 1{,}2\,\Omega \cdot 0{,}10\,\text{A} = 4{,}48\,\text{V} + 0{,}12\,\text{V} = 4{,}60\,\text{V}$
**Vastaus:** $E \approx 4{,}6\,\text{V}$ ja $R_\text{s} \approx 1{,}2\,\Omega$, kaksi merkitsevää numeroa, koska kulmakerroin luetaan kuvaajalta eikä sitä voi lukea tarkemmin kuin kahden numeron tarkkuudella.
**Järkevyys:** Lähdejännite on hieman pariston nimellisjännitettä $4{,}5\,\text{V}$ suurempi, mikä sopii uudelle paristolle. Sisäinen resistanssi on ohmin luokkaa, kuten litteillä taskulamppuparistoilla. Oikosulkuvirta olisi $\dfrac{E}{R_\text{s}} \approx 3{,}8\,\text{A}$.

### c)
**Annettu:** $E = 4{,}60\,\text{V}$, $R_\text{s} = 1{,}2\,\Omega$ ja ulkoinen vastus $R = 8{,}0\,\Omega$
**Kysytty:** vastukseen siirtyvä teho $P$ ja pariston sisäisessä resistanssissa lämpönä siirtyvän tehon osuus pariston koko sähkötehosta
**Periaate:** Virtapiirissä paristo, sisäinen resistanssi ja vastus ovat sarjassa, joten kaikkien läpi kulkee sama virta. Silmukkasäännön mukaan lähdejännite jakautuu sisäisen resistanssin ja vastuksen yli: $E - R_\text{s} I - R I = 0$. Sähkötehosta siirtyy lämpönä sekä vastuksessa että pariston sisällä, ja pariston koko teho on näiden summa $E I$.
**Kaava:** $I = \dfrac{E}{R + R_\text{s}}$, $P = R I^2$, $P_\text{s} = R_\text{s} I^2$ ja osuus $\dfrac{P_\text{s}}{P + P_\text{s}} = \dfrac{R_\text{s}}{R + R_\text{s}}$
**Muunnokset:** Ei tarvita, kaikki suureet ovat perusyksiköissä.
**Sijoitus:** $I = \dfrac{4{,}60\,\text{V}}{8{,}0\,\Omega + 1{,}2\,\Omega} = \dfrac{4{,}60\,\text{V}}{9{,}2\,\Omega} = 0{,}50\,\text{A}$, $P = 8{,}0\,\Omega \cdot (0{,}50\,\text{A})^2 = 2{,}0\,\text{W}$ ja $P_\text{s} = 1{,}2\,\Omega \cdot (0{,}50\,\text{A})^2 = 0{,}30\,\text{W}$. Osuus on $\dfrac{0{,}30\,\text{W}}{2{,}0\,\text{W} + 0{,}30\,\text{W}} = 0{,}13$.
**Vastaus:** Vastukseen siirtyy teho $P \approx 2{,}0\,\text{W}$, ja noin $13\,\%$ pariston sähkötehosta siirtyy lämpönä pariston sisällä. Tulos on annettu kahden merkitsevän numeron tarkkuudella kuten lähtötiedot.
**Järkevyys:** Napajännite on $R I = 4{,}0\,\text{V}$, mikä on sama kuin $E - R_\text{s} I = 4{,}60\,\text{V} - 0{,}60\,\text{V}$, ja kuvaajalla virran $0{,}50\,\text{A}$ kohdalla jännite on noin $4{,}0\,\text{V}$. Koska ulkoinen vastus on yli seitsemän kertaa sisäistä resistanssia suurempi, vain pieni osa tehosta jää pariston sisälle.

### d)
**Kysytty:** purkautumisen ja lämpenemisen vaikutus lähdejännitteen ja sisäisen resistanssin tulokseen, hajonnan aiheuttama epävarmuus $R_\text{s}$:ssä ja mittauksen parannus
**Periaate:** Malli $U = E - R_\text{s} I$ olettaa, että $E$ ja $R_\text{s}$ pysyvät vakioina koko mittauksen ajan. Jos paristo purkautuu tai lämpenee, ne muuttuvat mittauksen aikana, ja kuvaajan suora kuvaa jonkinlaista keskiarvoa. Hajonta kertoo satunnaisista virheistä eli siitä, kuinka paljon sovitettu suora voisi kääntyä.
**Mallivastaus:** *Systemaattinen virhe.* Virtaa kasvatettiin koko ajan samaan suuntaan, ja jokaista lukemaa varten piiri oli kytkettynä noin minuutin. Pariston purkautuminen laskee jännitettä ajan myötä, joten myöhemmin mitatut jännitteet eli suurimpia virtoja vastaavat jännitteet ovat liian pieniä. Koska aika ja virta kasvavat yhtä aikaa, ajan vaikutus sekoittuu kulmakertoimeen: suora laskee liian jyrkästi ja $R_\text{s}$ tulee liian suureksi. Lämpeneminen muuttaa myös $R_\text{s}$:ää mittauksen aikana (yleensä pienentää sitä), joten sen vaikutuksen suunta on epävarma. Lähdejännitteeseen vaikutus on pieni, koska pienimmällä virralla mitattiin ensin tuoreella paristolla.

*Ajautuman suuruus.* Uusi mittaus virralla $0{,}10\,\text{A}$ antoi $4{,}45\,\text{V}$ eli $0{,}03\,\text{V}$ vähemmän kuin sarjan alussa. Pahimmillaan viimeinen piste on siis noin $0{,}03\,\text{V}$ liian alhaalla, ja kulmakerroin on liian suuri enintään $\dfrac{0{,}03\,\text{V}}{0{,}50\,\text{A}} = 0{,}06\,\Omega$.

*Epävarmuus.* Pisteet poikkeavat sovitetusta suorasta enintään $0{,}02\,\text{V}$. Jos suoran toinen pää nousee ja toinen laskee tämän verran, kulmakerroin muuttuu $\dfrac{2 \cdot 0{,}02\,\text{V}}{0{,}50\,\text{A}} = 0{,}08\,\Omega$ eli $R_\text{s} = (1{,}20 \pm 0{,}08)\,\Omega$. Epävarmuus on pyöristetty yhteen merkitsevään numeroon.

*Parannus.* Virrat mitataan satunnaisessa järjestyksessä tai sarja toistetaan käänteisessä järjestyksessä, ja piiri kytketään päälle vain lukeman ajaksi. Jos tulokset eroavat toisistaan, ero kertoo purkautumisen vaikutuksen suuruuden.

*Johtopäätös.* Ajautuman vaikutus ($0{,}06\,\Omega$) on samaa suuruusluokkaa kuin hajonnan ($0{,}08\,\Omega$), joten $R_\text{s}$ on noin $1{,}1\ldots1{,}2\,\Omega$. Arvo $1{,}2\,\Omega$ on pikemmin yläraja, koska systemaattinen virhe kasvattaa sitä.

### Hyväksytään myös
- a-kohdassa kuvaajan pystyakseli voi alkaa nollasta, kunhan pisteet ja $E$ erottuvat; silloin suora voidaan jatkaa myös vaaka-akselille, jossa $I_\text{k} = \dfrac{E}{R_\text{s}} \approx 3{,}8\,\text{A}$.
- b-kohdassa kulmakertoimen lukema $-1{,}1\ldots-1{,}3\,\text{V/A}$ (vastaus $R_\text{s}$ noin $1{,}1\ldots1{,}3\,\Omega$) ja lähdejännite $4{,}5\ldots4{,}7\,\text{V}$ hyväksytään. Myös laskimen tai taulukkolaskennan sovitus hyväksytään.
- d-kohdassa epävarmuuden saa arvioida myös sovittamalla ääriviivat ja lukemalla niiden kulmakertoimet.

### Yleisiä virheitä
- Pisteet yhdistetään murtoviivaksi tai suora pakotetaan kulkemaan origon kautta, vaikka $U$ ei ole nolla virran ollessa nolla.
- Kulmakerroin luetaan kahdesta peräkkäisestä mittauspisteestä eikä kaukana toisistaan olevista suoran pisteistä.
- Kulmakertoimen etumerkki jätetään huomiotta, tai $R_\text{s}$ laskee $U : I$ yksittäisestä mittauksesta, jolloin saadaan ulkoisen vastuksen arvo, ei sisäistä resistanssia.
- c-kohdassa vastuksen jännitteeksi otetaan koko lähdejännite $E$ ja unohdetaan sisäisen resistanssin jännitehäviö.
- Epävarmuudeksi kirjoitetaan mittarin lukematarkkuus $0{,}01\,\text{V}$ sellaisenaan eikä oteta huomioon pisteiden hajontaa eikä systemaattista virhettä.

## fy6-s2

### a)
**Annettu:** lähdejännite $E = 12{,}0\,\text{V}$, kaapelin resistanssi $R_\text{k} = 0{,}80\,\Omega$, lamppu A $12\,\text{V},\ 24\,\text{W}$ ja lamppu B $12\,\text{V},\ 12\,\text{W}$
**Kysytty:** akustosta kulkeva virta $I$, kun molemmat lamput palavat
**Periaate:** Lamppu käsitellään vakioresistanssina, jonka arvo saadaan nimellisarvoista: nimellisjännitteellä teho on $P = \dfrac{U^2}{R}$. Lamput A ja B ovat rinnan, joten niillä on sama jännite, ja kaapeli on niiden kanssa sarjassa, joten koko virta kulkee kaapelin kautta. Silloin kokonaisresistanssi on kaapelin resistanssin ja rinnankytkennän korvaavan resistanssin summa.
**Kaava:** $R_\text{A} = \dfrac{U_\text{n}^2}{P_\text{A}}$, $R_\text{B} = \dfrac{U_\text{n}^2}{P_\text{B}}$, $\dfrac{1}{R_\text{r}} = \dfrac{1}{R_\text{A}} + \dfrac{1}{R_\text{B}}$, $R = R_\text{k} + R_\text{r}$ ja $I = \dfrac{E}{R}$
**Muunnokset:** Ei tarvita: $1\,\text{V}^2/\text{W} = 1\,\Omega$.
**Sijoitus:** $R_\text{A} = \dfrac{(12\,\text{V})^2}{24\,\text{W}} = 6{,}0\,\Omega$ ja $R_\text{B} = \dfrac{(12\,\text{V})^2}{12\,\text{W}} = 12\,\Omega$. Rinnankytkentä: $\dfrac{1}{R_\text{r}} = \dfrac{1}{6{,}0\,\Omega} + \dfrac{1}{12\,\Omega} = \dfrac{3}{12\,\Omega}$, joten $R_\text{r} = 4{,}0\,\Omega$. Kokonaisresistanssi on $R = 0{,}80\,\Omega + 4{,}0\,\Omega = 4{,}8\,\Omega$ ja virta $I = \dfrac{12{,}0\,\text{V}}{4{,}8\,\Omega} = 2{,}5\,\text{A}$.
**Vastaus:** $I = 2{,}5\,\text{A}$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Jos lamput saisivat nimellisjännitteen, niiden virrat olisivat $2{,}0\,\text{A}$ ja $1{,}0\,\text{A}$ eli yhteensä $3{,}0\,\text{A}$. Kaapeli ottaa osan jännitteestä, joten virta jää tätä pienemmäksi. Virta on myös sulakkeen $3{,}15\,\text{A}$ ja kaapelin $4{,}0\,\text{A}$ rajojen alapuolella.

### b)
**Annettu:** $E = 12{,}0\,\text{V}$, $R_\text{k} = 0{,}80\,\Omega$, $R_\text{A} = 6{,}0\,\Omega$ ja a-kohdan virta $I = 2{,}5\,\text{A}$
**Kysytty:** lampun A todellinen teho $P_\text{A}$ ja sen vertailu nimellistehoon $24\,\text{W}$
**Periaate:** Silmukkasäännön mukaan akun jännite jakautuu kaapelin jännitehäviön ja lamppujen jännitteen kesken: $E - R_\text{k} I - U_\text{L} = 0$. Lamppujen jännite jää siksi nimellisjännitettä pienemmäksi, ja teho lasketaan tästä todellisesta jännitteestä.
**Kaava:** $U_\text{L} = E - R_\text{k} I$ ja $P_\text{A} = \dfrac{U_\text{L}^2}{R_\text{A}}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $U_\text{L} = 12{,}0\,\text{V} - 0{,}80\,\Omega \cdot 2{,}5\,\text{A} = 12{,}0\,\text{V} - 2{,}0\,\text{V} = 10{,}0\,\text{V}$ ja $P_\text{A} = \dfrac{(10{,}0\,\text{V})^2}{6{,}0\,\Omega} = 16{,}7\,\text{W}$
**Vastaus:** $P_\text{A} \approx 17\,\text{W}$, noin $70\,\%$ nimellisarvosta $24\,\text{W}$, kaksi merkitsevää numeroa kuten lähtötiedoissa ($0{,}80\,\Omega$, $24\,\text{W}$, $12\,\text{V}$).
**Järkevyys:** Lamppu palaa himmeämmin kuin nimellisjännitteellä, koska sen jännite on vain $10{,}0\,\text{V}$. Tarkistus: lampun B teho on $\dfrac{(10{,}0\,\text{V})^2}{12\,\Omega} = 8{,}3\,\text{W}$ ja kaapeliin siirtyy lämpönä $0{,}80\,\Omega \cdot (2{,}5\,\text{A})^2 = 5{,}0\,\text{W}$. Summa $16{,}7\,\text{W} + 8{,}3\,\text{W} + 5{,}0\,\text{W} = 30\,\text{W}$ on yhtä suuri kuin akuston teho $12{,}0\,\text{V} \cdot 2{,}5\,\text{A} = 30\,\text{W}$.

### c)
**Kysytty:** miten lampun A kirkkaus, akuston virta ja kaapelin lämpeneminen muuttuvat, kun lamppu B poistuu piiristä, sekä lampun A tehon tarkistus laskemalla
**Periaate:** Akusto antaa piiriin vakiojännitteen $12{,}0\,\text{V}$. Kun toinen rinnakkainen haara poistuu, rinnankytkennän korvaava resistanssi kasvaa ja kokonaisresistanssi kasvaa, joten virta pienenee. Kaapeli on sarjassa lampun A kanssa, joten sen jännitehäviö riippuu koko virrasta.
**Mallivastaus:** *Virta.* Kokonaisresistanssi on nyt $R = 0{,}80\,\Omega + 6{,}0\,\Omega = 6{,}8\,\Omega$ ja virta $I = \dfrac{12{,}0\,\text{V}}{6{,}8\,\Omega} \approx 1{,}8\,\text{A}$, aiemmin $2{,}5\,\text{A}$.

*Kirkkaus.* Pienempi virta pienentää kaapelin jännitehäviötä: $0{,}80\,\Omega \cdot 1{,}76\,\text{A} \approx 1{,}4\,\text{V}$, aiemmin $2{,}0\,\text{V}$. Lampulle A jää siksi suurempi jännite $U_\text{A} \approx 10{,}6\,\text{V}$, ja sen teho on $\dfrac{(10{,}6\,\text{V})^2}{6{,}0\,\Omega} \approx 18{,}7\,\text{W}$, aiemmin $16{,}7\,\text{W}$. Lamppu A siis palaa kirkkaammin, vaikka sen omassa haarassa ei muuttunut mikään.

*Johtopäätös.* Rinnankytketyt lamput ovat toisistaan riippumattomia vain, jos jännite niiden yli pysyy vakiona. Kaapelin resistanssi tekee lampuista hieman riippuvaisia toisistaan: jos kaapelin resistanssi olisi nolla, lampun A kirkkaus ei muuttuisi lainkaan.

### d)
**Annettu:** $E = 12{,}0\,\text{V}$, $R_\text{k} = 0{,}80\,\Omega$, $R_\text{A} = 6{,}0\,\Omega$, $R_\text{B} = 12\,\Omega$, uusi lamppu C $12\,\text{V},\ 36\,\text{W}$, sulake $3{,}15\,\text{A}$ ja kaapelin raja $4{,}0\,\text{A}$
**Kysytty:** akuston virta $I$ kolmella lampulla ja sulakkeen toiminta
**Periaate:** Lamput ovat edelleen rinnan, joten niillä on yhteinen jännite ja resistanssit lasketaan yhteen käänteislukuina. Kaapeli on sarjassa kaikkien kanssa. Sulake on virtapiirin suojalaite: se palaa ja katkaisee piirin, jos virta ylittää sen nimellisvirran liian pitkään.
**Kaava:** $R_\text{C} = \dfrac{U_\text{n}^2}{P_\text{C}}$, $\dfrac{1}{R_\text{r}} = \dfrac{1}{R_\text{A}} + \dfrac{1}{R_\text{B}} + \dfrac{1}{R_\text{C}}$ ja $I = \dfrac{E}{R_\text{k} + R_\text{r}}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $R_\text{C} = \dfrac{(12\,\text{V})^2}{36\,\text{W}} = 4{,}0\,\Omega$ ja $\dfrac{1}{R_\text{r}} = \dfrac{1}{6{,}0\,\Omega} + \dfrac{1}{12\,\Omega} + \dfrac{1}{4{,}0\,\Omega} = \dfrac{2 + 1 + 3}{12\,\Omega} = \dfrac{1}{2{,}0\,\Omega}$, joten $R_\text{r} = 2{,}0\,\Omega$. Virta on $I = \dfrac{12{,}0\,\text{V}}{0{,}80\,\Omega + 2{,}0\,\Omega} = \dfrac{12{,}0\,\text{V}}{2{,}8\,\Omega} = 4{,}3\,\text{A}$.
**Vastaus:** $I \approx 4{,}3\,\text{A}$. Virta ylittää sekä sulakkeen nimellisvirran $3{,}15\,\text{A}$ että kaapelin sallitun virran $4{,}0\,\text{A}$, joten sulake todennäköisesti palaa ylivirran jatkuessa ja katkaisee piirin (todellinen toiminta-aika riippuu sulakkeen tyypistä, joten tämä on yksinkertaistus). Lamppujen jännite on $R_\text{r} I = 2{,}0\,\Omega \cdot 4{,}3\,\text{A} \approx 8{,}6\,\text{V}$, joten ne palavat himmeämmin kuin aiemmin. Sulake mitoitetaan suojaamaan piirin heikointa osaa eli kaapelia: sen nimellisvirta on kaapelin sallittua virtaa pienempi, jotta kaapeli ei lämpene vaarallisesti ennen kuin piiri katkeaa.
**Järkevyys:** Kolmas lamppu pienentää rinnankytkennän resistanssin $4{,}0\,\Omega$:sta $2{,}0\,\Omega$:iin, joten virran täytyy kasvaa $2{,}5\,\text{A}$:sta. Jos sulaketta ei olisi, kaapeliin siirtyisi lämpönä $0{,}80\,\Omega \cdot (4{,}3\,\text{A})^2 \approx 15\,\text{W}$, melkein kolminkertainen teho aiempaan $5{,}0\,\text{W}$:iin verrattuna. Lamppujen resistanssit on laskettu nimellisarvoista, joten tulos on arvio.

### Hyväksytään myös
- a-kohdan voi laskea lampun nimellisvirroista $I = \dfrac{P}{U}$ ja resistansseista $R = \dfrac{U}{I}$, kunhan tulokset ovat samat: $2{,}0\,\text{A}$ ja $1{,}0\,\text{A}$, $6{,}0\,\Omega$ ja $12\,\Omega$.
- b-kohdassa lampun jännitteen saa laskea myös suoraan $U_\text{L} = R_\text{r} I = 4{,}0\,\Omega \cdot 2{,}5\,\text{A}$.
- d-kohdassa lamppujen jännitteen ($8{,}6\,\text{V}$) voi lisäksi laskea ja todeta, että lamput palavat himmeämmin kuin aiemmin.

### Yleisiä virheitä
- Lamppujen resistanssit lasketaan kaavalla $R = \dfrac{P}{U}$ tai $R = \dfrac{U}{P}$.
- Rinnankytkennän resistanssi lasketaan summana $6{,}0\,\Omega + 12\,\Omega$ tai korvaavaksi resistanssiksi saadaan käänteisluku, jota ei muuteta takaisin ($\tfrac{1}{4{,}0\,\Omega} = 0{,}25\,\text{S}$ kirjoitetaan resistanssiksi $0{,}25\,\Omega$).
- Lamppujen jännitteeksi otetaan koko akuston jännite $12{,}0\,\text{V}$, ja kaapelin jännitehäviö unohdetaan.
- c-kohdassa päätellään, että lamppu A ei muutu lainkaan, koska se on rinnan: unohdetaan, että kaapeli on sarjassa.
- d-kohdassa sulakkeen ylittyminen todetaan, mutta sulakkeen tarkoitusta kaapelin suojaajana ei selitetä.

## fy6-s3

### a)
**Annettu:** potentiaaliero $U = 60\,\text{kV} = 6{,}0 \cdot 10^{4}\,\text{V}$, etäisyys $d = 20\,\text{cm}$, varaus $q = 6{,}0 \cdot 10^{-13}\,\text{C}$ ja massa $m = 4{,}0 \cdot 10^{-10}\,\text{kg}$
**Kysytty:** pisaraan vaikuttava sähkövoima $F$, painon merkitys ja kipinöinnin mahdollisuus
**Periaate:** Levyjen välissä on homogeeninen sähkökenttä, jonka voimakkuus on potentiaaliero jaettuna etäisyydellä. Positiivisesti varautuneeseen pisaraan vaikuttaa kentän suuntainen voima, joten pisara kulkee kohti pienempää potentiaalia eli maadoitettua työkappaletta. Painon merkitys arvioidaan vertaamalla sitä sähkövoimaan, ja kipinöinti kentän voimakkuutta ilman läpilyöntilujuuteen.
**Kaava:** $E = \dfrac{U}{d}$ ja $F = qE$
**Muunnokset:** $20\,\text{cm} = 0{,}20\,\text{m}$ ja $60\,\text{kV} = 60 \cdot 1000\,\text{V} = 6{,}0 \cdot 10^{4}\,\text{V}$.
**Sijoitus:** $E = \dfrac{6{,}0 \cdot 10^{4}\,\text{V}}{0{,}20\,\text{m}} = 3{,}0 \cdot 10^{5}\,\text{V/m}$ ja $F = 6{,}0 \cdot 10^{-13}\,\text{C} \cdot 3{,}0 \cdot 10^{5}\,\text{V/m} = 1{,}8 \cdot 10^{-7}\,\text{N}$
**Vastaus:** $F \approx 1{,}8 \cdot 10^{-7}\,\text{N}$ kentän suuntaan kohti työkappaletta, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Pisaran paino on $mg = 4{,}0 \cdot 10^{-10}\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 = 3{,}9 \cdot 10^{-9}\,\text{N}$, eli vain noin $2\,\%$ sähkövoimasta, joten painon voi jättää huomiotta. Kentän voimakkuus $3{,}0 \cdot 10^{5}\,\text{V/m} = 0{,}30\,\text{MV/m}$ on noin kymmenesosa ilman läpilyöntilujuudesta $3\,\text{MV/m}$, joten kipinöintiä ei synny.

### b)
**Annettu:** $q = 6{,}0 \cdot 10^{-13}\,\text{C}$, $U = 6{,}0 \cdot 10^{4}\,\text{V}$, $m = 4{,}0 \cdot 10^{-10}\,\text{kg}$ ja pisara lähtee levosta
**Kysytty:** pisaran nopeus $v$ osuessaan työkappaleeseen, kun ilmanvastusta ei oteta huomioon
**Periaate:** Sähkökentän pisaraan tekemä työ on varaus kertaa potentiaaliero, $W = qU$, ja se kasvattaa pisaran liike-energiaa. Paino ja ilmanvastus jätetään pois, joten muita voimia ei ole. Tällä tavalla riittää tietää potentiaaliero, eikä kentän voimakkuutta tai kiihtyvyyttä tarvita.
**Kaava:** $q U = \dfrac{1}{2} m v^2$, josta $v = \sqrt{\dfrac{2 q U}{m}}$
**Muunnokset:** Ei tarvita, kaikki suureet ovat perusyksiköissä; $1\,\text{C} \cdot 1\,\text{V} = 1\,\text{J}$.
**Sijoitus:** $qU = 6{,}0 \cdot 10^{-13}\,\text{C} \cdot 6{,}0 \cdot 10^{4}\,\text{V} = 3{,}6 \cdot 10^{-8}\,\text{J}$ ja $v = \sqrt{\dfrac{2 \cdot 3{,}6 \cdot 10^{-8}\,\text{J}}{4{,}0 \cdot 10^{-10}\,\text{kg}}} = \sqrt{180\,\text{m}^2/\text{s}^2} = 13{,}4\,\text{m/s}$
**Vastaus:** $v \approx 13\,\text{m/s}$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Kiihtyvyys on $\dfrac{F}{m} = \dfrac{1{,}8 \cdot 10^{-7}\,\text{N}}{4{,}0 \cdot 10^{-10}\,\text{kg}} = 450\,\text{m/s}^2$, joten $0{,}20\,\text{m}$:n matkalla nopeus olisi $\sqrt{2 \cdot 450\,\text{m/s}^2 \cdot 0{,}20\,\text{m}} = 13{,}4\,\text{m/s}$, mikä vahvistaa tuloksen. Painon työ koko matkalla olisi vain $7{,}8 \cdot 10^{-10}\,\text{J}$ eli noin $2\,\%$ sähkökentän työstä.

### c)
**Kysytty:** miksi mitattu osumanopeus $5{,}0\,\text{m/s}$ on paljon pienempi kuin b-kohdan tulos ja minne sähkökentän tekemä työ jää
**Periaate:** B-kohdan malli jätti ilmanvastuksen pois. Ilmanvastus vaikuttaa pisaran liikkeen suuntaa vastaan, ja sen tekemä työ on negatiivista. Kun pisaran nopeus kasvaa, ilmanvastus kasvaa, ja pisara etenee nopeudella, jolla ilmanvastus ja sähkövoima ovat likimain yhtä suuret. Energian säilymisen mukaan sähkökentän tekemä työ ei häviä, vaan se siirtyy muualle.
**Mallivastaus:** *Selitys.* B-kohdan nopeus $13\,\text{m/s}$ olisi mahdollinen vain tyhjiössä. Ilmassa ilmanvastus rajoittaa nopeuden paljon pienemmäksi, joten b-kohdan tulos on pisaran suurin mahdollinen nopeus eli yläraja.

*Laskenta.* Pisaran todellinen liike-energia on $\dfrac{1}{2} m v^2 = \dfrac{1}{2} \cdot 4{,}0 \cdot 10^{-10}\,\text{kg} \cdot (5{,}0\,\text{m/s})^2 = 5{,}0 \cdot 10^{-9}\,\text{J}$. Sähkökentän tekemä työ on $3{,}6 \cdot 10^{-8}\,\text{J}$, joten liike-energiaksi päätyy vain $\dfrac{5{,}0 \cdot 10^{-9}\,\text{J}}{3{,}6 \cdot 10^{-8}\,\text{J}} \approx 14\,\%$.

*Energian kohtalo.* Loput $3{,}6 \cdot 10^{-8}\,\text{J} - 5{,}0 \cdot 10^{-9}\,\text{J} = 3{,}1 \cdot 10^{-8}\,\text{J}$ siirtyy ilmaan. Ilman sisäenergia kasvaa, ja energia siirtyy edelleen lämpönä ympäristöön. Energia ei siis häviä.

*Johtopäätös.* B-kohdan oletus (ei ilmanvastusta) tekee nopeudesta liian suuren, joten tulos on suurin mahdollinen nopeus. Energia ei häviä, vaan se siirtyy ilmaan.

### d)
**Annettu:** $q_1 = q_2 = 6{,}0 \cdot 10^{-13}\,\text{C}$, $r = 1{,}0\,\text{mm}$ ja $k = 8{,}988 \cdot 10^{9}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{C}^2}$
**Kysytty:** pisaroiden välinen voima $F$ ja sen merkitys pisarapilven käyttäytymiselle
**Periaate:** Pisarat ovat paljon pienempiä kuin niiden etäisyys, joten ne voi käsitellä pistemäisinä varauksina. Niiden välinen voima noudattaa Coulombin lakia: samanmerkkiset varaukset hylkivät toisiaan.
**Kaava:** $F = k\dfrac{q_1 q_2}{r^2}$
**Muunnokset:** $1{,}0\,\text{mm} = 1{,}0 \cdot 10^{-3}\,\text{m}$
**Sijoitus:** $F = 8{,}988 \cdot 10^{9}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{C}^2} \cdot \dfrac{(6{,}0 \cdot 10^{-13}\,\text{C})^2}{(1{,}0 \cdot 10^{-3}\,\text{m})^2} = 8{,}988 \cdot 10^{9} \cdot \dfrac{3{,}6 \cdot 10^{-25}}{1{,}0 \cdot 10^{-6}}\,\text{N} = 3{,}2 \cdot 10^{-9}\,\text{N}$
**Vastaus:** $F \approx 3{,}2 \cdot 10^{-9}\,\text{N}$, hylkivä, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Voima on noin $1{,}8\,\%$ kentän voimasta $1{,}8 \cdot 10^{-7}\,\text{N}$ mutta $0{,}8$-kertainen pisaran painoon $3{,}9 \cdot 10^{-9}\,\text{N}$ verrattuna. Hylkimisvoima on siis pieni verrattuna sähkökentän voimaan, joten pisarat kulkevat edelleen kohti työkappaletta, mutta hylkiminen levittää pisarapilveä sivusuunnassa. Tämä on osa sitä, miksi suihku leviää suuttimen jälkeen.

### Hyväksytään myös
- a-kohdassa kentän voimakkuuden saa ilmoittaa yksikössä $\text{kV/m}$: $300\,\text{kV/m}$.
- b-kohdan voi ratkaista myös kiihtyvyydestä: $a = \dfrac{F}{m} = 450\,\text{m/s}^2$ ja $v = \sqrt{2 a d}$, kunhan ratkaisu perustuu a-kohdan voimaan ja matkaan $0{,}20\,\text{m}$.

### Yleisiä virheitä
- Potentiaaliero $60\,\text{kV}$ sijoitetaan kilovoltteina, jolloin kenttä saadaan väärin tuhatkertaisena tai tuhannesosana.
- Voimaksi lasketaan $U : d$, jolloin kentän voimakkuus sekoitetaan voimaan.
- b-kohdassa käytetään kaavaa $v = \sqrt{2 a d}$ kiihtyvyydellä $g$ tai lasketaan työ painosta.
- Pisaran energian ilmoitetaan "muuttuvan lämmöksi" tai "hukkuvan"; energia siirtyy ilmaan ja sieltä lämpönä.
- d-kohdassa etäisyys sijoitetaan millimetreinä, tai unohdetaan neliöinti.

## fy6-s4

### a)
**Annettu:** $C = 330\,\mu\text{F}$ ja $U = 300\,\text{V}$
**Kysytty:** kondensaattoriin varastoitunut energia $E$ ennen salamaa
**Periaate:** Ladattuun kondensaattoriin on varastoitunut energiaa, koska varaus on siirretty sen levyille jännitettä vastaan. Energia riippuu kapasitanssista ja jännitteen neliöstä.
**Kaava:** $E = \dfrac{1}{2} C U^2$
**Muunnokset:** $330\,\mu\text{F} = 330 \cdot 10^{-6}\,\text{F}$
**Sijoitus:** $E = \dfrac{1}{2} \cdot 330 \cdot 10^{-6}\,\text{F} \cdot (300\,\text{V})^2 = \dfrac{1}{2} \cdot 330 \cdot 10^{-6}\,\text{F} \cdot 90\,000\,\text{V}^2 = 14{,}85\,\text{J}$
**Vastaus:** $E \approx 15\,\text{J}$ ($14{,}85\,\text{J}$), kaksi merkitsevää numeroa, koska jännitteen $300\,\text{V}$ ja kapasitanssin $330\,\mu\text{F}$ tarkkuus on enintään kaksi tai kolme numeroa.
**Järkevyys:** Energia on joulen luokkaa, kuten pienen salamalaitteen kondensaattorissa. Jos tämä energia siirtyisi nostamaan kilon painoista kappaletta, se nousisi noin $1{,}5\,\text{m}$.

### b)
**Annettu:** $C = 330\,\mu\text{F}$, jännite ennen salamaa $U_1 = 300\,\text{V}$ ja sen jälkeen $U_2 = 220\,\text{V}$
**Kysytty:** salamaan siirtynyt energia $\Delta E$, sen osuus varastoidusta energiasta ja osuuden suuruuden syy
**Periaate:** Salamaan siirtynyt energia on kondensaattorin energian muutos: se on energia ennen salamaa vähennettynä energialla salaman jälkeen. Jännite on energiakaavassa neliönä, joten kumpikin energia lasketaan erikseen; pelkkä jännitteen muutos $\Delta U$ ei riitä.
**Kaava:** $\Delta E = \dfrac{1}{2} C U_1^2 - \dfrac{1}{2} C U_2^2$
**Muunnokset:** $330\,\mu\text{F} = 330 \cdot 10^{-6}\,\text{F}$
**Sijoitus:** $E_1 = 14{,}85\,\text{J}$ ja $E_2 = \dfrac{1}{2} \cdot 330 \cdot 10^{-6}\,\text{F} \cdot (220\,\text{V})^2 = \dfrac{1}{2} \cdot 330 \cdot 10^{-6}\,\text{F} \cdot 48\,400\,\text{V}^2 = 7{,}99\,\text{J}$, joten $\Delta E = 14{,}85\,\text{J} - 7{,}99\,\text{J} = 6{,}86\,\text{J}$. Osuus on $\dfrac{6{,}86\,\text{J}}{14{,}85\,\text{J}} = 0{,}46$.
**Vastaus:** Salamaan siirtyi $\Delta E \approx 6{,}9\,\text{J}$, noin $46\,\%$ varastoidusta energiasta, kaksi merkitsevää numeroa kuten a-kohdassa.
**Järkevyys:** Jännite pieneni vain $\dfrac{80\,\text{V}}{300\,\text{V}} \approx 27\,\%$, mutta energiaa siirtyi $46\,\%$, koska energia on verrannollinen jännitteen neliöön: $1 - \left(\dfrac{220}{300}\right)^2 = 0{,}46$. Siirtynyt energia on pienempi kuin alkuenergia, kuten pitääkin.

### c)
**Annettu:** $C = 330\,\mu\text{F}$, jännitteen muutos $\Delta U = 300\,\text{V} - 220\,\text{V} = 80\,\text{V}$ ja kesto $\Delta t = 1{,}0\,\text{ms}$
**Kysytty:** keskimääräinen virta $I$ salaman aikana
**Periaate:** Virta on varauksen siirtymisnopeus. Kondensaattorin varaus on $Q = C U$, joten jännitteen pienentyessä $80\,\text{V}$ kondensaattorilta on lähtenyt varausta $\Delta Q = C\,\Delta U$ salamaputken kautta.
**Kaava:** $I = \dfrac{\Delta Q}{\Delta t}$ ja $\Delta Q = C\,\Delta U$
**Muunnokset:** $330\,\mu\text{F} = 330 \cdot 10^{-6}\,\text{F}$ ja $1{,}0\,\text{ms} = 1{,}0 \cdot 10^{-3}\,\text{s}$
**Sijoitus:** $\Delta Q = 330 \cdot 10^{-6}\,\text{F} \cdot 80\,\text{V} = 0{,}0264\,\text{C}$ ja $I = \dfrac{0{,}0264\,\text{C}}{1{,}0 \cdot 10^{-3}\,\text{s}} = 26{,}4\,\text{A}$
**Vastaus:** $I \approx 26\,\text{A}$, kaksi merkitsevää numeroa kuten keston $1{,}0\,\text{ms}$ tarkkuus.
**Järkevyys:** Keskiteho on $\dfrac{6{,}86\,\text{J}}{1{,}0 \cdot 10^{-3}\,\text{s}} \approx 6{,}9\,\text{kW}$ ja virta $26\,\text{A}$: nämä ovat paljon suurempia kuin pieni paristo voisi antaa näin lyhyessä pulssissa. Siksi energia varastoidaan ensin kondensaattoriin, joka luovuttaa sen nopeasti.

### d)
**Kysytty:** onko kondensaattorissa vaaraa pariston irrottamisen jälkeen, miten se puretaan turvallisesti ja kuinka suuri virta kulkisi kehon läpi
**Periaate:** Kondensaattori varastoi varauksen ja energian levyilleen eikä sen jännite katoa, kun lataava paristo irrotetaan. Vaara riippuu varastoituneesta energiasta ja jännitteestä, ei paristosta. Virran suuruus kehon läpi saadaan jännitteestä ja resistanssista.
**Mallivastaus:** *Vaara.* Kondensaattori on pariston irrottamisen jälkeen edelleen $300\,\text{V}$:ssa, ja siinä on noin $15\,\text{J}$. Laite ei saa jännitettä pienestä paristosta, vaan kondensaattorista, joka voi purkautua korjaajan kehon kautta.

*Virta.* Jos kehon resistanssi on $1{,}0\,\text{k}\Omega$, virta olisi aluksi $I = \dfrac{U}{R} = \dfrac{300\,\text{V}}{1{,}0 \cdot 10^{3}\,\Omega} = 0{,}30\,\text{A}$. Se on moninkertainen verrattuna muutamaan kymmeneen milliampeeriin, jotka voivat jo olla vaarallisia. Virta pienenee kondensaattorin purkautuessa, mutta alun virta riittää vaaralliseen sähköiskuun.

*Turvallinen purku* (vain ymmärtämiseksi: älä yritä purkaa kondensaattoria itse). Kondensaattorin napojen väliin kytketään eristetyillä työkaluilla sopiva vastus, esimerkiksi $10\,\text{k}\Omega$. Alkuvirta on silloin $\dfrac{300\,\text{V}}{10\,\text{k}\Omega} = 30\,\text{mA}$, ja kondensaattorin energia siirtyy vastuksen sisäenergiaksi ja siitä lämpönä ympäristöön. Vastuksen teho on aluksi $\dfrac{(300\,\text{V})^2}{10\,\text{k}\Omega} = 9\,\text{W}$, joten vastuksen tehonkeston on oltava sen mukainen. Napoja ei oikosulkuteta ruuvimeisselillä, koska silloin virta on hyvin suuri ja syntyy kipinä. Lopuksi jännite varmistetaan mittarilla.

*Johtopäätös.* Laitetta ei saa avata heti. Vaara johtuu kondensaattorin varastoimasta energiasta ja jännitteestä eikä pariston koosta. Kehon resistanssi vaihtelee esimerkiksi ihon kosteuden mukaan, joten laskettu virta on suuruusluokka-arvio.

### Hyväksytään myös
- a-kohdassa energian saa laskea myös kaavalla $E = \dfrac{1}{2} Q U$, missä $Q = C U = 0{,}099\,\text{C}$.
- b-kohdassa osuuden saa laskea suoraan jännitteiden suhteesta $1 - \left(\dfrac{U_2}{U_1}\right)^2$.
- c-kohdassa tuloksen saa laskea myös varauksen ja ajan suhteena ilman erillistä $\Delta Q$:n laskua: $I = \dfrac{C\,\Delta U}{\Delta t}$.

### Yleisiä virheitä
- Kapasitanssi sijoitetaan mikrofaradeina kertomatta sitä luvulla $10^{-6}$.
- Energian laskemisessa unohdetaan jännitteen neliöinti, tai salamaan siirtynyt energia lasketaan kaavasta $\tfrac{1}{2} C (\Delta U)^2$.
- Virta lasketaan jakamalla energia ajalla, jolloin saadaan teho.
- Todetaan, että kondensaattori on vaaraton, koska laitteessa on vain pieni paristo.
- Kondensaattori puretaan oikosulkemalla se metallityökalulla.
```

## Figure inventory (inline figures; the captures `fig-N-390` show them in page order)
- `content/fi/FY6/sovella/solutions.md:18–85` [fy6-s1-graph] in “a)”: Kuvaaja: pariston napajännite U voltteina virran I funktiona ampeereina. Kuusi mustaa pistettä virroilla 0,10–0,60 A; jännite pienenee arvosta 4,48 V arvoon 3,89 V. Pisteisiin on sovitettu suora, joka kulkee pisteiden lo — labels: $0{,}1$ · $0{,}2$ · $0{,}3$ · $0{,}4$ · $0{,}5$ · $0{,}6$ · $0{,}7$ · $0{,}8$ · $3{,}8$ · $4{,}0$ · $4{,}2$ · $4{,}4$ · $4{,}6$ · $4{,}8$ · $I\ (\text{A})$ · $U\ (\text{V})$ · $3{,}6$ · $0$ · <span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta I = 0{,}50\,\text{A}$</span> · <spa

## Screenshots (current: they show the content hash above; paths relative to the folder that holds review/; contact sheets first, then the captures your judgement needs at full size)
| file | shows | px | ≈ tokens |
|---|---|---|---|
| review/shots/contact-1.png | contact sheet: captures #1–#12 | 1260×1932 | 3245 |
| review/shots/contact-2.png | contact sheet: captures #13–#24 | 1260×1932 | 3245 |
| review/shots/contact-3.png | contact sheet: captures #25–#36 | 1260×1932 | 3245 |
| review/shots/contact-4.png | contact sheet: captures #37–#48 | 1260×1932 | 3245 |
| review/shots/contact-5.png | contact sheet: captures #49–#60 | 1260×1932 | 3245 |
| review/shots/contact-6.png | contact sheet: captures #61–#72 | 1260×1932 | 3245 |
| review/shots/contact-7.png | contact sheet: captures #73–#84 | 1260×1932 | 3245 |
| review/shots/contact-8.png | contact sheet: captures #85–#96 | 1260×1932 | 3245 |
| review/shots/contact-9.png | contact sheet: captures #97–#108 | 1260×1932 | 3245 |
| review/shots/contact-10.png | contact sheet: captures #109–#120 | 1260×1224 | 2056 |
| review/shots/contact-11.png | contact sheet: captures #121–#132 | 1260×1224 | 2056 |
| review/shots/contact-12.png | contact sheet: captures #133–#134 | 1260×416 | 698 |
| review/shots/FY6-sovella-top-390.png | #1 first screen at 390 px | 390×844 | 438 |
| review/shots/FY6-sovella-page-390-1.png | #2 the whole page at 390 px, every box open (teacher's notes included) (part 1/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-2.png | #3 the whole page at 390 px, every box open (teacher's notes included) (part 2/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-3.png | #4 the whole page at 390 px, every box open (teacher's notes included) (part 3/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-4.png | #5 the whole page at 390 px, every box open (teacher's notes included) (part 4/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-5.png | #6 the whole page at 390 px, every box open (teacher's notes included) (part 5/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-6.png | #7 the whole page at 390 px, every box open (teacher's notes included) (part 6/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-7.png | #8 the whole page at 390 px, every box open (teacher's notes included) (part 7/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-8.png | #9 the whole page at 390 px, every box open (teacher's notes included) (part 8/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-9.png | #10 the whole page at 390 px, every box open (teacher's notes included) (part 9/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-10.png | #11 the whole page at 390 px, every box open (teacher's notes included) (part 10/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-11.png | #12 the whole page at 390 px, every box open (teacher's notes included) (part 11/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-12.png | #13 the whole page at 390 px, every box open (teacher's notes included) (part 12/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-13.png | #14 the whole page at 390 px, every box open (teacher's notes included) (part 13/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-14.png | #15 the whole page at 390 px, every box open (teacher's notes included) (part 14/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-15.png | #16 the whole page at 390 px, every box open (teacher's notes included) (part 15/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-16.png | #17 the whole page at 390 px, every box open (teacher's notes included) (part 16/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-17.png | #18 the whole page at 390 px, every box open (teacher's notes included) (part 17/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-18.png | #19 the whole page at 390 px, every box open (teacher's notes included) (part 18/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-19.png | #20 the whole page at 390 px, every box open (teacher's notes included) (part 19/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-20.png | #21 the whole page at 390 px, every box open (teacher's notes included) (part 20/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-21.png | #22 the whole page at 390 px, every box open (teacher's notes included) (part 21/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-22.png | #23 the whole page at 390 px, every box open (teacher's notes included) (part 22/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-23.png | #24 the whole page at 390 px, every box open (teacher's notes included) (part 23/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-24.png | #25 the whole page at 390 px, every box open (teacher's notes included) (part 24/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-25.png | #26 the whole page at 390 px, every box open (teacher's notes included) (part 25/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-26.png | #27 the whole page at 390 px, every box open (teacher's notes included) (part 26/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-27.png | #28 the whole page at 390 px, every box open (teacher's notes included) (part 27/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-28.png | #29 the whole page at 390 px, every box open (teacher's notes included) (part 28/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-29.png | #30 the whole page at 390 px, every box open (teacher's notes included) (part 29/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-30.png | #31 the whole page at 390 px, every box open (teacher's notes included) (part 30/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-31.png | #32 the whole page at 390 px, every box open (teacher's notes included) (part 31/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-32.png | #33 the whole page at 390 px, every box open (teacher's notes included) (part 32/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-33.png | #34 the whole page at 390 px, every box open (teacher's notes included) (part 33/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-34.png | #35 the whole page at 390 px, every box open (teacher's notes included) (part 34/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-35.png | #36 the whole page at 390 px, every box open (teacher's notes included) (part 35/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-36.png | #37 the whole page at 390 px, every box open (teacher's notes included) (part 36/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-37.png | #38 the whole page at 390 px, every box open (teacher's notes included) (part 37/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-38.png | #39 the whole page at 390 px, every box open (teacher's notes included) (part 38/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-39.png | #40 the whole page at 390 px, every box open (teacher's notes included) (part 39/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-40.png | #41 the whole page at 390 px, every box open (teacher's notes included) (part 40/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-41.png | #42 the whole page at 390 px, every box open (teacher's notes included) (part 41/42) | 366×1408 | 687 |
| review/shots/FY6-sovella-page-390-42.png | #43 the whole page at 390 px, every box open (teacher's notes included) (part 42/42) | 366×323 | 157 |
| review/shots/FY6-sovella-fig-1-390.png | #44 figure 1 in “1Taskulampun paristo 15 pistettä”: Kytkentäkaavio, ei mittakaavassa: pariston mittaus. Vasemmalla on tutkittava paristo, plus | 331×182 | 80 |
| review/shots/FY6-sovella-fig-2-390.png | #45 figure 2 in “1Taskulampun paristo 15 pistettä”:  | 28×28 | 1 |
| review/shots/FY6-sovella-fig-3-390.png | #46 figure 3 in “Mallivastaus”: Kuvaaja: pariston napajännite U voltteina virran I funktiona ampeereina. Kuusi mustaa pist | 305×202 | 82 |
| review/shots/FY6-sovella-fig-4-390.png | #47 figure 4 in “Mallivastaus”:  | 28×28 | 1 |
| review/shots/FY6-sovella-fig-5-390.png | #48 figure 5 in “2Mökin pihavalot 15 pistettä”: Kytkentäkaavio, ei mittakaavassa: mökin valaistus. Vasemmalla on 12 voltin akku, plusnapa  | 331×182 | 80 |
| review/shots/FY6-sovella-fig-6-390.png | #49 figure 6 in “2Mökin pihavalot 15 pistettä”:  | 28×28 | 1 |
| review/shots/FY6-sovella-fig-7-390.png | #50 figure 7 in “3Ruiskumaalaus 16 pistettä”: Kaaviokuva, ei mittakaavassa: ruiskumaalauksen sähkökenttä. Ylhäällä on vaakasuora suutinl | 331×203 | 89 |
| review/shots/FY6-sovella-fig-8-390.png | #51 figure 8 in “3Ruiskumaalaus 16 pistettä”:  | 28×28 | 1 |
| review/shots/FY6-sovella-fig-9-390.png | #52 figure 9 in “Mallivastaus”:  | 69×59 | 5 |
| review/shots/FY6-sovella-fig-10-390.png | #53 figure 10 in “Mallivastaus”:  | 128×60 | 10 |
| review/shots/FY6-sovella-fig-11-390.png | #54 figure 11 in “Mallivastaus”:  | 96×29 | 3 |
| review/shots/FY6-sovella-fig-12-390.png | #55 figure 12 in “Mallivastaus”:  | 190×44 | 11 |
| review/shots/FY6-sovella-fig-13-390.png | #56 figure 13 in “Hyväksytään myös”:  | 59×31 | 2 |
| review/shots/FY6-sovella-fig-14-390.png | #57 figure 14 in “Yleisiä virheitä”:  | 59×31 | 2 |
| review/shots/FY6-sovella-fig-15-390.png | #58 figure 15 in “Pisteytys ja itsearviointi”:  | 69×59 | 5 |
| review/shots/FY6-sovella-fig-16-390.png | #59 figure 16 in “Pisteytys ja itsearviointi”:  | 153×71 | 14 |
| review/shots/FY6-sovella-stage-fy6-s1-390-1.png | #60 inquiry stage Taskulampun paristo 15 pistettä (part 1/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-2.png | #61 inquiry stage Taskulampun paristo 15 pistettä (part 2/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-3.png | #62 inquiry stage Taskulampun paristo 15 pistettä (part 3/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-4.png | #63 inquiry stage Taskulampun paristo 15 pistettä (part 4/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-5.png | #64 inquiry stage Taskulampun paristo 15 pistettä (part 5/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-6.png | #65 inquiry stage Taskulampun paristo 15 pistettä (part 6/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-7.png | #66 inquiry stage Taskulampun paristo 15 pistettä (part 7/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-8.png | #67 inquiry stage Taskulampun paristo 15 pistettä (part 8/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-9.png | #68 inquiry stage Taskulampun paristo 15 pistettä (part 9/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-10.png | #69 inquiry stage Taskulampun paristo 15 pistettä (part 10/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-11.png | #70 inquiry stage Taskulampun paristo 15 pistettä (part 11/12) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s1-390-12.png | #71 inquiry stage Taskulampun paristo 15 pistettä (part 12/12) | 366×249 | 121 |
| review/shots/FY6-sovella-stage-fy6-s2-390-1.png | #72 inquiry stage Mökin pihavalot 15 pistettä (part 1/11) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s2-390-2.png | #73 inquiry stage Mökin pihavalot 15 pistettä (part 2/11) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s2-390-3.png | #74 inquiry stage Mökin pihavalot 15 pistettä (part 3/11) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s2-390-4.png | #75 inquiry stage Mökin pihavalot 15 pistettä (part 4/11) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s2-390-5.png | #76 inquiry stage Mökin pihavalot 15 pistettä (part 5/11) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s2-390-6.png | #77 inquiry stage Mökin pihavalot 15 pistettä (part 6/11) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s2-390-7.png | #78 inquiry stage Mökin pihavalot 15 pistettä (part 7/11) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s2-390-8.png | #79 inquiry stage Mökin pihavalot 15 pistettä (part 8/11) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s2-390-9.png | #80 inquiry stage Mökin pihavalot 15 pistettä (part 9/11) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s2-390-10.png | #81 inquiry stage Mökin pihavalot 15 pistettä (part 10/11) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s2-390-11.png | #82 inquiry stage Mökin pihavalot 15 pistettä (part 11/11) | 366×878 | 428 |
| review/shots/FY6-sovella-stage-fy6-s3-390-1.png | #83 inquiry stage Ruiskumaalaus 16 pistettä (part 1/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s3-390-2.png | #84 inquiry stage Ruiskumaalaus 16 pistettä (part 2/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s3-390-3.png | #85 inquiry stage Ruiskumaalaus 16 pistettä (part 3/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s3-390-4.png | #86 inquiry stage Ruiskumaalaus 16 pistettä (part 4/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s3-390-5.png | #87 inquiry stage Ruiskumaalaus 16 pistettä (part 5/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s3-390-6.png | #88 inquiry stage Ruiskumaalaus 16 pistettä (part 6/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s3-390-7.png | #89 inquiry stage Ruiskumaalaus 16 pistettä (part 7/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s3-390-8.png | #90 inquiry stage Ruiskumaalaus 16 pistettä (part 8/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s3-390-9.png | #91 inquiry stage Ruiskumaalaus 16 pistettä (part 9/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s3-390-10.png | #92 inquiry stage Ruiskumaalaus 16 pistettä (part 10/10) | 366×1026 | 500 |
| review/shots/FY6-sovella-stage-fy6-s4-390-1.png | #93 inquiry stage Kameran salama 14 pistettä (part 1/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s4-390-2.png | #94 inquiry stage Kameran salama 14 pistettä (part 2/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s4-390-3.png | #95 inquiry stage Kameran salama 14 pistettä (part 3/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s4-390-4.png | #96 inquiry stage Kameran salama 14 pistettä (part 4/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s4-390-5.png | #97 inquiry stage Kameran salama 14 pistettä (part 5/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s4-390-6.png | #98 inquiry stage Kameran salama 14 pistettä (part 6/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s4-390-7.png | #99 inquiry stage Kameran salama 14 pistettä (part 7/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s4-390-8.png | #100 inquiry stage Kameran salama 14 pistettä (part 8/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s4-390-9.png | #101 inquiry stage Kameran salama 14 pistettä (part 9/10) | 366×1408 | 687 |
| review/shots/FY6-sovella-stage-fy6-s4-390-10.png | #102 inquiry stage Kameran salama 14 pistettä (part 10/10) | 366×279 | 136 |
| review/shots/FY6-sovella-top-1280.png | #103 first screen at 1280 px | 1280×900 | 1536 |
| review/shots/FY6-sovella-page-1280-1.png | #104 the whole page at 1280 px, every box open (teacher's notes included) (part 1/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-2.png | #105 the whole page at 1280 px, every box open (teacher's notes included) (part 2/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-3.png | #106 the whole page at 1280 px, every box open (teacher's notes included) (part 3/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-4.png | #107 the whole page at 1280 px, every box open (teacher's notes included) (part 4/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-5.png | #108 the whole page at 1280 px, every box open (teacher's notes included) (part 5/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-6.png | #109 the whole page at 1280 px, every box open (teacher's notes included) (part 6/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-7.png | #110 the whole page at 1280 px, every box open (teacher's notes included) (part 7/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-8.png | #111 the whole page at 1280 px, every box open (teacher's notes included) (part 8/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-9.png | #112 the whole page at 1280 px, every box open (teacher's notes included) (part 9/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-10.png | #113 the whole page at 1280 px, every box open (teacher's notes included) (part 10/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-11.png | #114 the whole page at 1280 px, every box open (teacher's notes included) (part 11/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-12.png | #115 the whole page at 1280 px, every box open (teacher's notes included) (part 12/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-13.png | #116 the whole page at 1280 px, every box open (teacher's notes included) (part 13/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-14.png | #117 the whole page at 1280 px, every box open (teacher's notes included) (part 14/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-15.png | #118 the whole page at 1280 px, every box open (teacher's notes included) (part 15/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-16.png | #119 the whole page at 1280 px, every box open (teacher's notes included) (part 16/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-17.png | #120 the whole page at 1280 px, every box open (teacher's notes included) (part 17/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-18.png | #121 the whole page at 1280 px, every box open (teacher's notes included) (part 18/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-19.png | #122 the whole page at 1280 px, every box open (teacher's notes included) (part 19/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-20.png | #123 the whole page at 1280 px, every box open (teacher's notes included) (part 20/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-21.png | #124 the whole page at 1280 px, every box open (teacher's notes included) (part 21/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-22.png | #125 the whole page at 1280 px, every box open (teacher's notes included) (part 22/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-23.png | #126 the whole page at 1280 px, every box open (teacher's notes included) (part 23/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-24.png | #127 the whole page at 1280 px, every box open (teacher's notes included) (part 24/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-25.png | #128 the whole page at 1280 px, every box open (teacher's notes included) (part 25/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-26.png | #129 the whole page at 1280 px, every box open (teacher's notes included) (part 26/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-27.png | #130 the whole page at 1280 px, every box open (teacher's notes included) (part 27/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-28.png | #131 the whole page at 1280 px, every box open (teacher's notes included) (part 28/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-29.png | #132 the whole page at 1280 px, every box open (teacher's notes included) (part 29/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-30.png | #133 the whole page at 1280 px, every box open (teacher's notes included) (part 30/31) | 1160×1408 | 2177 |
| review/shots/FY6-sovella-page-1280-31.png | #134 the whole page at 1280 px, every box open (teacher's notes included) (part 31/31) | 1160×1300 | 2010 |

## Report: write `content/fi/FY6/sovella/review/visual.md` (format and severities: .claude/agents/visual-editorial-reviewer.md), under 400 words
Line 1 `VERDICT: PASS` or `VERDICT: FAIL`; line 2 `CONTENT-HASH: <output of python3 scripts/practice.py hash FY6>` run at the start and again at the end. Then `## Blocking` (FAIL if and only if non-empty; `[Critical|Major] file/figure — problem — why it matters — fix`), `## Polish` (at most five `[Minor]`), `## Checked` (the captures you opened; at most ten lines), `## Scores` (illustrations · typography · Finnish · accessibility, 1–5). A PASS needs the captures: if you could not look, FAIL with `visual verification incomplete`. Never edit any file but your report.
