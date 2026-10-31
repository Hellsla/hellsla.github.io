# Editorial quality standard (teacher's brief 2026-10-31)

What "publication quality" means for every Ruukkilabra page: lessons and their exercise sets, FY10 experimental
investigations, TVT guides and the module-end *Sovella itsenäisesti* tasks, now and in future. It is the yardstick
of the four-agent team (developer, science-reviewer, pedagogy-reviewer, visual-editorial-reviewer) and of
`/quality-audit`. It adds no new rules where the house rules already have one: CLAUDE.md, NOTES.md,
`docs/physics-guardrails.md`, `docs/force-diagrams.md` and `docs/inquiry.md` stay the detailed sources, and this
document points to them.

**Authorities.** The educational authorities are LOPS 2019 (`docs/lops2019/`), the physics guardrails and the
grading principles of the Finnish matriculation examination (YTL: the published descriptions of good answers and
the grading instructions; never copied). **Benchmarks.** Studeo, Otava's Vipu, Sanoma Pro and e-Oppi's Resonanssi
are the commercial materials a Finnish physics teacher compares with. Their chapters are not in this repository and
no reviewer has access to them, so this standard describes none of them: a comparison is made only from material the
teacher has legitimately available (publishers' public sample pages, the school's own licences), by the teacher or
from what the teacher puts in `docs/benchmarks/` (none yet). Nothing is copied from them, text or illustration.

**Scores.** Each dimension has a 1–5 rubric. The target for published content is **at least 4 in every dimension and
no known Critical issue**. Scores are internal indicators of where the work stands and what to fix next; they do not
prove equivalence with a commercial textbook, and a score never overrides a Blocking finding.

**Who scores what.** Science reviewer: 1 and the physics of 6. Pedagogy reviewer: 2–6 (5 and 6 for exam and
experimental work). Visual & editorial reviewer: 7–10. An audit (`/quality-audit`) collects them into one table.

**Severity** (every reviewer, every dimension):
- **Critical — blocks publication**: a physically misleading statement or figure; essential information unreadable,
  clipped or missing; broken or ambiguous mathematical notation; an editorial ambiguity that changes the scientific
  meaning; an accessibility failure that prevents use of essential content.
- **Major — normally blocks**: a confusing or inconsistent diagram; clearly poor mathematical readability; a weak or
  misleading graph; a serious language or presentation problem; a structure that substantially hinders
  comprehension; (science and pedagogy keep their own Blocking criteria in their agent files).
- **Minor — polish**: small stylistic inconsistencies, decorative details, wording, subtle spacing that does not
  affect use. A subjective aesthetic preference alone is never a finding above Minor.

## Ruukkilabra's identity: inquiry first
Every chapter keeps **Pohdinta → Ennusta → Tutki → Teoriatiivistelmä → Sovella → Tarkista osaamisesi** (then
Tehtävät), as a learning process and not a template: each stage must help the student understand or apply physics.
The aim is to exceed a commercial textbook through better learning experiences, not more content or decorative UI:
strong independent written reasoning, data interpretation, experimental design, graphical analysis, physical
modelling and fair YO-style applications. A complex open task is never replaced by an automatically checked numeric
one because the latter is easier to build. No extra figures or exercises merely to increase their number.

## 1. Physics and mathematical correctness (science)
Definitions, models and their conditions, causality, quantities, internal consistency and assessment correctness
as `docs/physics-guardrails.md` and the science reviewer's seven checks define them.
- **5** Every claim, number and figure right; every model's conditions stated where it is used; the chapter agrees
  with the chapters it builds on; recomputation reproduces every answer.
- **4** Correct throughout; at most minor imprecision with no wrong picture (category C simplifications).
- **3** One unstated condition (B) or an inconsistency between theory and a task, nothing taught wrong.
- **2** An error (A) in a task, solution or figure, or several B findings.
- **1** An error in the theory itself or a misleading model.

## 2. Conceptual clarity (pedagogy)
- **5** The core idea is named, explained by its mechanism, shown in a figure and used; misconceptions are met
  head-on; a student with only the prerequisites can follow every step.
- **4** Clear and complete; one step could be smoother.
- **3** Correct but a step is asserted rather than explained, or a key idea has no picture where it needs one.
- **2** The explanation leaves a gap a student cannot cross alone.
- **1** The core idea is not explained.

## 3. Pedagogical effectiveness (pedagogy)
- **5** The inquiry stages lead to the idea: a prediction worth arguing about, evidence the student acts on that can
  refute it, theory that answers the opening question, transfer, checks with misconception-based distractors and
  feedback that repairs the misconception; one lesson's workload.
- **4** Effective; one activity weaker than the rest.
- **3** The stages are present but one is mechanical (a prediction nobody can argue about, a simulation for show).
- **2** The evidence cannot refute the prediction, or answers are disclosed before the student acts.
- **1** No real inquiry.

## 4. Exercise quality and variety (pedagogy, science for the physics)
- **5** Levels 1–3 in the course's counts, each level doing its job (CLAUDE.md "Exercise levels"), everyday contexts,
  word, graph and data tasks where the topic allows, none repeating the worked example, every task with a complete
  model solution (CLAUDE.md Lesson form 7).
- **4** Good set; one task weak or two too alike.
- **3** Mostly plug-in tasks, or level 3 not really reasoning.
- **2** Tasks that need what the chapter does not teach, or incomplete solutions.
- **1** Tasks with errors or no solutions.

## 5. YO examination readiness (pedagogy)
- **5** Level 3 and the transfer tasks need independent application; the module's *Sovella itsenäisesti* tasks are
  original, authentic, multi-part, with source material to interpret and a fair point rubric (NOTES.md §9);
  written answers are self-assessed against observable criteria.
- **4** Ready; one competency (concept, math, graph, experiment, communication, transfer) thinly practised.
- **3** Exam skills appear only in the Sovella tasks.
- **2** No independent application in the chapter.
- **1** Only recall and plug-in work.

## 6. Experimental reasoning and data analysis (pedagogy; science for models and uncertainty)
- **5** The student plans or follows a measurement, controls variables, reads and fits real or clearly labelled data,
  states the uncertainty (`\Delta x`) and distinguishes observation, conclusion and assumption; an investigation's
  F and E levels are honest; TVT guides are linked, not copied.
- **4** Sound; one element (uncertainty, controlled variables) thin.
- **3** Data are given but only read, not interpreted.
- **2** Invented or unlabelled data presented as measured, or a conclusion the data do not support.
- **1** No experimental reasoning where the topic calls for it.

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
`{,}` in Finnish; SI units upright with a thin space (`9{,}81\,\text{m/s}^2`); `\cdot` for multiplication, a colon for
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
correct case after a number and unit ("80 N:n voimalla"). A complete explanation is better than a shorter
incomplete one: never shorten for brevity, never rewrite a correct sentence because another phrasing is possible.
English and Selkeä suomi versions are judged in their own language by the same standard.
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

## How the gate uses this standard
A new or modified lesson is published only with current PASS reports from all three reviewers (`scripts/reviews.py`,
README "The publishing rule"); its exercise set, an investigation, a TVT guide and a Sovella set each have their own
three reports. Content that was published before the visual reviewer existed (2026-10-31) stays published under a
hash-bound **visual baseline** (`docs/visual-baseline.tsv`) until its first material change, when it needs a
genuine visual PASS; `python scripts/reviews.py baseline` lists what still awaits its baseline review. Automated
checks verify what is objective; reviewers judge what no script can; the teacher makes the publication decision.
A reviewer never passes content because the checks pass, a professional appearance never hides a conceptual or
mathematical error, and a correct chapter whose presentation seriously hinders learning is not finished.
