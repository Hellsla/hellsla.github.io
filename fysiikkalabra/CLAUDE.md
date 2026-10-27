# Fysiikkalabra — house rules for every agent

## What this repo is
A digital textbook for Finnish upper-secondary physics (LOPS 2019): theory, simulations and exercises, one folder per lesson under `content/<course>/<lesson-id>/`. `scripts/build.py` renders the lessons whose reviews are current into `site/`, which is committed and served by GitHub Pages at `hellsla.github.io/fysiikkalabra/site/`. Previews (`build.py <id>` or `--all`) go to the git-ignored `preview/`.

## Courses and scope
- `curriculum.json` is the single source for every course (FY1–FY8): its LOPS 2019 goals and central contents from `docs/lops2019/`, its lesson slots, and optional `scope_notes`, `exercise_levels`, `initialized`. `scripts/courses.py` turns a lesson id into its course, slot and folders; nothing else hardcodes a course.
- Stay inside the course's central contents and scope notes (your packet carries them). Grep the MAOL guide in `docs/lops2019/` when unsure whether something belongs to a course.
- `/new-course <FY4>` prepares a course (`scripts/new_course.py`); it never writes goals or slots, which come from the LOPS texts and the teacher.
- **Lessons per course** (teacher's decision 2026-10-26): FY1 and FY2 have 8 lessons each, FY3–FY8 16 each (`planned_lessons` in `curriculum.json`). `/new-course` notes a course whose slots do not match; the missing slots come from the teacher, never from an agent.

## Audience and language
- Students aged 16–19, smart but meeting the idea for the first time. Site language Finnish; agent prompts and reports may be in English.
- Physics terms come from `glossary.json`; add a missing term there, do not invent synonyms.

## Physics and maths conventions
- SI units, upright with a thin space: `9,81 m/s²`. Decimal comma in Finnish text, decimal point in JSON.
- g = 9,81 m/s², always in m/s² (never N/kg). Three significant figures in final answers unless the data has fewer.
- Vectors bold in LaTeX (`\mathbf{F}`), magnitudes plain. Every formula appears once in display LaTeX with its symbols named.
- Every exercise has `answer`, `unit` and `tolerance`; the data carries the significant figures the answer should have, and a student rounding to them stays inside the tolerance. `answers.py` computes every answer.

## Lesson form (human decisions 2026-10-25, every lesson)
1. **Visualise.** `## Ydinajatus` and `## Kaava: <law>` each have at least one inline SVG figure right after the paragraph it explains, and any other theory point with a picture (p = F/A) gets a simple one; every label inside a figure is LaTeX (`foreignObject`, NOTES.md §3, teacher 2026-10-26), and so is every label and value in a simulation's canvas and readout (NOTES.md §1); graphs and figures are of printed-textbook quality (NOTES.md §3 Graphs, Print quality); no paragraph over about 120 words.
2. **Solve symbolically first, then substitute** values with units, in the worked example and every solution; solutions are written in LaTeX (NOTES.md §1, teacher 2026-10-26).
3. **Simulations are visually rich, not slider-rich.** Keep the physics controls; spend the effort on the picture, motion, meaningful colour, labels, a legend. Every animated sim has a speed control (hidas · normaali · nopea) and only labels and values on the canvas; explanations go behind closed boxes under it (Lesson page 4).
4. **Worked examples are staged**: seven stages (rule 7) separated by `<!-- vaihe -->` lines, each with a bold lead-in and one step; the page reveals them one at a time.
5. **Inquiry first, shaped by the topic** (teacher's brief 2026-10-25, `docs/inquiry-spec.md`; 2026-10-26: no fixed template): every lesson has `inquiry.json` (`docs/inquiry.md`) through Pohdinta → Ennusta → Tutki → Teoriatiivistelmä → Sovella → Tarkista osaamisesi, then Tehtävät: a phenomenon, a retrieval of prior learning, a committed prediction before the evidence where the topic allows, the evidence that fits the topic (a guided experiment on a simulation when manipulating it reveals something; otherwise a table, a graph, competing explanations or a model to build), the model, a transfer task with hints and common-mistake feedback, three checks. A simulation or a game is there for what it teaches, never for show. Feedback is gated on commitment, never access; no answer is disclosed before the student has acted; theory stays readable on its own.
6. **Chapter names, not ids.** A student never sees a lesson id: "luvussa *Paine ja hydrostaattinen paine*", not "oppitunnilla fy3-4" (teacher 2026-10-26).
7. **A complete model solution for every worked example and every task** (teacher 2026-10-27): a final answer or a formula alone is not enough. Each solution shows (1) what is given, with units, and what is asked; (2) the principle and why it fits the situation; (3) the starting equation and the asked quantity solved in symbols before any number; (4) the unit conversions needed (or that none are); (5) the substitution with units and enough intermediate steps; (6) the answer, rounded to the data's precision, with its unit and why that many figures; (7) a check that the result is physically reasonable. A task answered in words gets a justified model answer; a graph task shows how the graph is read and how the answer follows from it. The worked example opens step by step (its seven stages); an exercise's solution and every `numeric` task's solution sit behind that task's own *Näytä ratkaisu* button, so the student tries first. `meta.solutions` is `all`. Every language version (an S2 version included, when one exists) is as complete: S2 clarifies the language and opens the concepts but drops no step or justification. `scripts/check_solutions.py` (in the lint and CI) reports every missing or incomplete solution; NOTES.md §3 "Complete solutions" says how to write one.
NOTES.md says how to write each; `scripts/lint_lesson.py` and `scripts/test_inquiry.py` check what they can.

## Lesson page (human decisions 2026-10-26, every new or edited lesson)
The shared templates (`templates/`, `scripts/build.py`, `scripts/inquiry.py`) do 1, 2, 3, 5, 7 and 8 for every lesson; the
lesson does 6, 9 and its half of 4. `lint_lesson.py` checks 4, 6 and 9 as errors on a lesson being written or edited
(warnings on one reviewed before 2026-10-26), `test_inquiry.py` and `check_layout.py` check the page at 360, 1280 and 1920 px; look at 768 px too (teacher 2026-10-26: the layout must work at every width).
1. **Use the width.** One column on a phone, as before. On a wide screen parallel columns where they help: the simulation beside the experiments that use it, a figure beside the paragraph it explains, short activities side by side. Text keeps a readable line (a 38rem column, never over 44rem).
   Design system (teacher 2026-10-27, `templates/site.css` header): three levels — the stage (numbered 24 px heading on a full-width rule), the task (one card: heading, instructions, answers, table, feedback), what sits inside a task (tinted panels, smaller); one type scale (title 32–36 px Fraunces, stage 24, task 18, text 17, meta 14 px, Plus Jakarta Sans); a text track and a margin track from 60rem of content, the stage navigation in a sticky side column from 85rem (1360 px) of window, the simulation sticky beside the experiments. Fix a layout problem in the shared components, never per lesson.
2. **Pohdinta**, not "Herätä kiinnostus", as the first stage's heading and in the navigation.
3. **Ennusta in a box that starts closed** (`<details>`, keyboard operable); it can be reopened later, and closing it keeps the answers and reasons.
4. **Little text in the simulation.** The picture, the controls and the key quantities and values show; usage, the model's assumptions and the computation sit behind closed boxes named Käyttöohje, Mallin oletukset and Laskennan selitys (the sim activity's `howto`, `model`, `calc` in inquiry.json; its visible `text` is a lead of at most 30 words). Never hide a control the student needs; sim.js shows at most one legend line.
5. **Teoriatiivistelmä**, not "Selitä", as the theory stage's heading and in the navigation.
6. **The formula section is named after its law**: `## Kaava: Lämpömäärä` shows "Lämpömäärä" (or Hydrostaattinen paine, Ideaalikaasun tilanyhtälö, by the lesson's content); "Kaava" stays the key that inquiry.json and the scripts use.
7. **Exit ticket**, not "Lähtölippu", in every heading and link a student sees.
8. **Tehtävät last**: the exercises close the page, after the exit ticket, with their levels, answer checks and solutions; predictions and the questions of the investigation stay where they are.
9. **Textbook illustrations**: polished inline SVG in the figure palette (NOTES.md §3), recognisable materials, consistent strokes, room around things, labels that read on a phone; colour carries the physics (a temperature rise stands out) but never alone; quantities to scale. `content/FY3/fy3-6` is the model.

## Exercise levels
Level 1: one formula, values given, 5 problems. Level 2: two steps or a conversion or a rearrangement, 4. Level 3: reasoning, two ideas, or an unfamiliar context, 3 (other counts only where the course's `exercise_levels` says so). None repeats the worked example.

## Lesson folder and assets
```
meta.json          id, course, title, goals, prerequisites, glossary, sim (true | "<sim folder>" | false), solutions (all; first and none are not used since 2026-10-27)
lesson.md          Ydinajatus, Kaava, Esimerkki (staged), misconception, summary; inline SVG figures
inquiry.json       the inquiry sequence: contribution, prior, activities by stage (format in docs/inquiry.md)
exercises.json     three levels (schema in README)         solutions.md    one complete solution per exercise (CLAUDE.md Lesson form 7, NOTES §3)
answers.py         computes every answer                   exit-ticket.json  3 quick checks
sim-spec.md        the simulation's one-paragraph spec: what the student can find out with it
review/            science.md, pedagogy.md (legacy.md on a prototype), carry.tsv, developer.md, checks.txt, usage.tsv; packets and shots git-ignored
```
Simulations live in `assets/sims/<course>/<name>/` (sim.js exposing `window.simState` and `defineSimAdapter()`, its sim.css and images; FY3's stay as `sim.js` in their lesson folders), pictures in `assets/pics/<course>/` referred to as `pics/<course>/<file>`; `assets/shared/` only for what several courses use (`assets/README.md`).

## Pipeline
- **developer** writes and fixes, **science-reviewer** and **pedagogy-reviewer** judge independently; each works from a packet file (`scripts/review_packet.py`) that its prompt names. `/lesson <id>` (`.claude/commands/lesson.md` at the repository root, beside `.claude/agents/`: routing, budgets, steps) runs a round; `python scripts/check_lesson.py <id>` runs every deterministic check before any review.
- **The rule** (`scripts/reviews.py`): a lesson is on the site when both reviews say PASS for its current content hash. The hash covers the lesson files, its simulation folder, its pictures and its simulation tests; formatting, build scripts, templates and configuration never stale a review. What changed decides who looks again (`reviews.py scope`: none, delta or full per reviewer); a PASS that holds over a change its reviewer need not see is recorded in `review/carry.tsv` (`reviews.py carry`) and re-derived by CI. There are no status fields and nothing to edit by hand. `review/legacy.md` marks a prototype lesson published before this pipeline until any content change retires it.
- Merging the pull request is the teacher's publication decision. CI rebuilds `site/` and fails if the committed copy differs; a lesson whose reviews went stale is left out with a WARNING, never silently.

## Never
- Never push to `main`, merge a pull request, or force-push. Never edit another agent's report.
- Never copy exam questions from YTL or textbooks; write original problems.
- Never add tracking, logins or forms that collect student data. Never depict real people in generated images.
