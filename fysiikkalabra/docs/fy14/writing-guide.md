# FY14 Road to Fusion — writing guide for units (developers and reviewers)

Read with `docs/FY14_PLAN.md` (the course, its chapters and the architecture) and `scripts/units.py` (the format).
The house rules in `CLAUDE.md` and `NOTES.md` apply unless this guide says otherwise; where they speak of Finnish,
read English. This guide is the yardstick the three reviewers (science, pedagogy, visual & editorial) use for FY14.

## 1. Who and how
- Upper-secondary students (16–19), Finnish, studying physics **in English** (clear academic English, B1–B2): short
  sentences, one idea per paragraph (at most about 100 words), key terms in **bold** at first use and explained in
  plain words, no idioms a learner cannot look up. Never simplify the physics into something false.
- **CLIL is the method, not decoration.** Every unit practises language with the content: vocabulary in context,
  reading a source, listening (a video), explaining a diagram, describing a process, comparing, arguing from
  evidence, writing a short summary, discussing in pairs. Give a **word bank** and **sentence starters** for every
  harder speaking or writing task:
  `<div class="wordbank" markdown="1">` … `</div>` is not supported; write the box as raw HTML:
  `<div class="wordbank"><h4>Word bank</h4><p>…</p></div>` and `<div class="wordbank"><h4>Sentence starters</h4><ul><li>The evidence suggests that …</li></ul></div>`
  (inside raw HTML write HTML, not Markdown; maths `$…$` works).
- **French corner**: every physics, history and CLIL unit ends with one short `<div class="french-corner"><h4>Le coin
  français</h4>…</div>`: three to six French words or one sentence tied to the unit (*la lumière*, *un électron*,
  *la fusion*, *l'énergie*), with `lang="fr"` on every French span (`<span lang="fr">la lumière</span>`), and a
  `say` component when pronunciation matters. The French chapter units are mostly French with English instructions.
- **Discussion, not only quizzes.** Use `explain` tasks with `"pair": true` style prompts ("Discuss with a partner,
  then write…"), role-plays, debates and source analysis. Every written task has a model answer and observable
  criteria (what the answer shows), revealed only after the student has written something.

## 2. The unit page (inquiry stages, docs/inquiry.md)
Think about it → Predict → Investigate → Theory summary → Apply → Check your understanding. Adapt them to the topic:
a history unit investigates sources, a timeline or competing explanations; a language unit investigates a dialogue
or a text; a lab unit predicts and plans. A simulation only where manipulating it teaches something. Every unit:
1. an engaging scientific or historical question (`> **Why** …?` under the title; one question);
2. `learn`: 2–3 goals completing *In this lesson, you will learn to* ("calculate …", "explain …", "compare … and
   evaluate …"; `scripts/objectives.py`); `prior` where earlier units are needed ("… (chapter *Title of unit*)");
3. a committed prediction or discussion before the evidence;
4. an investigation: a simulation experiment, a source, a data table, a timeline, a map, a video, a dialogue;
5. an accessible explanation (`unit.md` sections placed by `theory` activities; own section names such as
   `## Why classical physics failed`, plus `## Key idea`, `## Formula: <law>`, `## Worked example` (staged with
   `<!-- vaihe -->` and the seven solution stages), `## Common misconception`, `## Summary` where they fit);
6. application tasks (`numeric` with complete solutions, `explain`, error-spotting `choice`);
7. a short understanding check: 2–3 `choice` checks in `tarkista` with misconception-specific feedback, plus an
   `explain` or transfer task. Correct options vary in place (the page shuffles; never refer to "option A"), and the
   right answer is not systematically the longest. Avoid predictable patterns.
Optional extensions go in `"optional": true` activities; hints (≤ 3) for scaffolding. `teacher.md`: timing for a
75-minute lesson, organisation (pairs, groups), what to prepare, how to assess (transparent criteria), common
difficulties, extension ideas. Never answers to graded work beyond what the page already shows.

## 3. Physics and mathematics (the teacher's standing rules)
- **Every mathematical symbol in LaTeX**, in the text, the figures, the tasks, the solutions and the simulations'
  labels and readouts (`$E = hf$`, `$17.6\ \text{MeV}$`). Units upright (`\text{eV}`), a thin space before them.
- Multiplication `\cdot` (never ×); written division with a colon in prose; vectors `\overline{F}`, `\overline{v}`,
  `\overline{B}` (never `\vec`, `\mathbf`); measurement uncertainty `\Delta x`.
- English pages use the **decimal point** (`2.36 eV`); three significant figures unless the data has fewer.
- Velocity, acceleration and force arrows always in **different colours** in every figure and simulation (force
  red `#c92a2a`, velocity blue `#1971c2`, acceleration orange `#e8590c`); the magnetic field its own colour (green
  `#2b8a3e`) and drawn with ⊙/⊗ where it points out of / into the page.
- Understanding before formulas: unit conversions by substitution (`1\ \text{eV} = 1.602 \cdot 10^{-19}\ \text{J}`),
  no unnecessary auxiliary quantities. Solve symbolically first, then substitute with units.
- **Complete model solution** for every worked example and every `numeric` task (CLAUDE.md "Lesson form" 7):
  given and asked, principle and why it fits, equation solved in symbols, conversions, substitution with units,
  answer rounded with its unit and why that precision, reasonableness check, each step on its own line with a bold
  label: `**Given:**`, `**Principle:**`, `**Formula:**`, `**Unit conversions:**`, `**Substitution:**`, `**Answer:**`,
  `**Reasonableness:**` (as in `content/en/FY3/fy3-6/exercises/solutions.md`).
- Nuclear notation `^{2}_{1}\text{H}`, reactions balanced in nucleon number and charge, energies with their sources
  (masses from AME/NIST with the table named). D–T: $^{2}_{1}\text{H} + {}^{3}_{1}\text{H} \to {}^{4}_{2}\text{He}
  (3.5\ \text{MeV}) + \text{n}\ (14.1\ \text{MeV})$, total $17.6\ \text{MeV}$.
- `docs/physics-guardrails.md` applies. Distinguish models from reality: the single-particle orbit is not plasma
  behaviour; "hotter than the Sun's core" refers to temperature, not to the pressure or the reaction rate; scientific
  gain $Q$ is not electricity; tritium is radioactive (half-life 12.3 a) and must be bred; neutrons activate the
  structure (low- and intermediate-level waste, no long-lived high-level waste from the fuel); a fusion reactor
  cannot run away like a chain reaction, but it has real hazards (tritium, activation, magnets, heat).

## 4. History and sources
- **Verify every date, name, number and claim** with reliable public sources (WebFetch works for iter.org,
  en.wikipedia.org, helsinki.fi, many lab sites; hs.fi and Wikimedia Commons do not, from this sandbox). Prefer primary
  and institutional sources (ITER, IAEA, EUROfusion, UKAEA, PPPL, national labs, the original papers) and use
  Wikipedia to find them. Every unit lists its sources in `unit.json` `sources` with the date each was checked.
- Things that change (ITER schedule, records, device status, private companies) carry their date in the text
  ("In 2024, ITER announced …", "as of November 2026 …"). Distinguish established results, institutional plans and
  corporate claims explicitly; never present a prediction of when fusion electricity arrives as fact.
- Write original text: never copy passages, questions or diagrams from textbooks, slides, videos or articles.
  Biographies are short (60–100 words), original and accurate, and say why the person matters to this story.
- People are never depicted in generated images; photographs come only from the photo manifest
  (`/mnt/project-files/fy14/photos/photos.json`, licensed and credited); until a photo exists, mark its place with
  an HTML comment `<!-- photo: <subject id> -->` and draw an original SVG figure if the point needs a picture.

## 5. Figures (NOTES.md §3, printed-textbook quality)
- Every unit opens with an **opening illustration** (`<svg data-fig="hero">`, `herolib.hero`, 1200 × 600) of its
  Why question, drawn in `lessons/units/<id>/figures.py` (`python3 scripts/units.py figures <id>` writes it in).
  Other figures in the same file; every label LaTeX through `Fig.tex`; words in `\text{}`; an `aria-label` that
  describes what is drawn; quantities to scale where scale matters; colour carries meaning but never alone.
- No decorative pictures. A diagram explains one thing. Figures stay right after the paragraph they explain.

## 6. Components (assets/units/fy14/fx/, `units.js`)
Place one as raw HTML on its own lines (blank line before and after), with a unique id:
```
<div class="fx" data-fx="match" id="fx-photon-words"><script type="application/json">{"prompt": "…", "options": ["…"], "items": [{"text": "…", "answer": "…", "feedback": "…"}]}</script></div>
```
`match` (also for sorting into categories), `order`, `gapfill` (`[[right|wrong|wrong]]` gaps), `say` (French phrases,
browser voice), `dialogue` (roles, lines with `fr`, `en`, `cue`), `video` (`id`, `title`, `channel`, `year`, `length`).
Each file's header comment documents its data. Feedback explains why, not only right/wrong. In an inquiry activity
the same HTML can be the `text` of a `text` or `interpret` activity.

## 7. Before you hand over
`python3 scripts/units.py check` (no errors), `python3 scripts/build.py <id>` (preview in `preview/en/<id>.html`),
`python3 scripts/check_layout.py <id> --width 360` and `--width 1280` (every line OK), `python3 scripts/screenshot.py <id>`
and look at the captures yourself (`review/shots.md` lists them).
Report in `review/developer.md` (`VERDICT: DONE`, files changed, facts verified with their sources, open questions).

## 8. Reviews (the gate, scripts/reviews.py)
`review/science.md`, `review/pedagogy.md`, `review/visual.md`, each starting
```
VERDICT: PASS
CONTENT-HASH: <python3 scripts/units.py hash <id>>
```
(or FAIL with numbered findings: Blocking first, then Polish). Science: physics, mathematics, history and dates,
sources, currency of changing facts, scientific gain vs electricity, no outdated predictions. Pedagogy: the inquiry
sequence, CLIL (language support, discussion, writing), French, B1–B2 English, scaffolding and extensions,
feedback, workload of one 75-minute lesson, no answer disclosed before the student acts. Visual & editorial
(`docs/EDITORIAL_QUALITY_STANDARD.md`, the captures in `review/shots/`): figures, mathematical typography, English
(and French) language, layout at 390 and 1280 px, components readable and operable.
