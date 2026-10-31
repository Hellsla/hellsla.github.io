# Ruukkilabra (Fysiikkalabra)

The site is called **Ruukkilabra**, subtitle *Lukion fysiikka* / *Upper secondary physics* (teacher 2026-10-29); the
folder, the URL and the scripts keep the old working name fysiikkalabra. Logos: `assets/shared/brand/`.

A digital textbook for Finnish upper-secondary physics (LOPS 2019): theory, p5.js simulations and exercises,
written and reviewed with Claude Code agents, served by GitHub Pages from the committed `site/` folder at
`https://hellsla.github.io/fysiikkalabra/site/`. House rules for agents: `CLAUDE.md`; writing rules: `NOTES.md`.

## Quick start
```bash
cd fysiikkalabra
pip install markdown playwright && playwright install chromium
python scripts/check_lesson.py fy3-9     # lint, LaTeX, preview build, simulation and inquiry tests, answer positions, 360 px, review state
python scripts/build.py fy3-9            # preview/fy3-9.html (git-ignored), any lesson
python scripts/build.py --all            # preview/ with every lesson, drafts included (what CI tests)
python scripts/build.py                  # site/ from the lessons whose reviews are current (atomic; commit it)
python scripts/reviews.py status         # reviewed | legacy | draft for every lesson, and why
python scripts/reviews.py impact         # which lessons this branch touches and which review each needs
python scripts/test_reviews.py           # tests of the publishing rule
python scripts/test_courses.py           # a temporary FY4 course through the whole pipeline, nothing published
python scripts/usage.py report FY3 --by agent   # tokens and cost per agent and model
```
If the pip `playwright` version does not match the installed browser: `PW_CHROMIUM=/path/to/chrome python scripts/test_sims.py`.

Inside Claude Code, `/lesson fy3-9` runs one lesson through the pipeline (orchestrated on Sonnet): the **developer**
(Sonnet; Opus only for demanding physics or a numerical model) writes or fixes, `check_lesson.py` must pass, the
**science-reviewer** (Opus) and the **pedagogy-reviewer** (Sonnet) judge it independently from packet files, fixes and
re-reviews for at most three rounds, then a draft pull request with a teacher summary and the measured token usage.
Agents live in `.claude/agents/` and the commands in `.claude/commands/` at the repository root (`../.claude/`), so a
session opened at the root, as a cloud session is, finds them; each starts by working in `fysiikkalabra/`.

## A new course
```
/new-course FY4        # scripts/new_course.py FY4: checks curriculum.json against LOPS 2019, creates the folders
/lesson fy4-1          # creates content/fi/FY4/fy4-1/meta.json from the slot, then drafts, checks and reviews it
/lesson fy4-2
```
Everything course-specific comes from the course's entry in `curriculum.json` (LOPS goals and central contents,
lesson slots, `scope_notes`, optional `exercise_levels`); `scripts/courses.py` resolves a lesson id to its course and
folders. Lesson texts go to `content/fi/FY4/<id>/` (the exercises to its `exercises/`), their code (`answers.py`, `figures.py`) to `lessons/FY4/<id>/`, pictures to `assets/pics/fy4/` (text refers to `pics/fy4/<file>`),
simulations to `assets/sims/fy4/<name>/` (published at `sims/fy4/<name>/`), shared assets to `assets/shared/`
(`assets/README.md`). The course page `site/FY4.html` lists the slots and links each lesson once it is reviewed.

## The publishing rule
`scripts/reviews.py` decides what is on the site: a lesson is **reviewed** when `review/science.md`,
`review/pedagogy.md` and `review/visual.md` all say `VERDICT: PASS` with the lesson's current `CONTENT-HASH`. The hash covers the lesson
files, its simulation folder, its pictures and its simulation tests (not the exercise set: below), and ignores only line endings, trailing
whitespace, blank-line runs and JSON layout; build scripts and templates are not content. What changed decides who
reviews again (`reviews.py scope`): a physics change needs the science reviewer in full, a learning-design change the
pedagogy reviewer, simulation code both, a figure's styling the pedagogy and visual reviewers, a formula re-set without a change of meaning (category
`typography`) only the visual reviewer, comments and tightened tests none of them; a PASS carried over such a change is recorded in `review/carry.tsv` and re-checked by CI. A **legacy**
lesson (`review/legacy.md`, written by `reviews.py legacy <id>` in the migration) was published before the
pipeline and stays visible, labelled as a prototype, until a content edit retires the marker. Everything else
is a **draft** and never reaches `site/`. The exercise set has the same rule of its own (Exercises, below).

**The visual & editorial review and its baseline** (teacher 2026-10-31). The third reviewer
(`.claude/agents/visual-editorial-reviewer.md`, Sonnet) judges illustrations, graphs, mathematical typography, Finnish
and presentation from the rendered captures (`screenshot.py <id> --if-stale`, contact sheets for triage) against
`docs/EDITORIAL_QUALITY_STANDARD.md`. Everything both other reviewers had passed when the gate was switched on is
listed, hash by hash, in `docs/visual-baseline.tsv` (`reviews.py baseline init`, run once): a row lets exactly that
version stay published without a visual PASS, and no PASS report was written for it. A change the visual reviewer
need not see is carried over the baseline like any carry; any other change needs the first genuine visual review,
in full. A visual FAIL from an audit leaves the row in force (auditing never unpublishes); rows are only removed,
and CI (`reviews.py verify`) fails on an added one. `python scripts/reviews.py baseline` lists what still awaits
its baseline review. Investigations, TVT guides and Sovella sets follow the same three-review rule (their baseline
rows hold for their exact hash). `VISUAL_GATE` in reviews.py is the switch.

Merging a pull request is the teacher's publication decision. CI (`.github/workflows/fysiikkalabra-ci.yml`)
lints every lesson, builds all previews, runs the review and course tests, the simulation tests, every lesson's
inquiry tests, the answer-position check and the LaTeX check, verifies carried reviews from history, lists the
review impact of the branch,
rebuilds `site/` and fails if the committed copy differs, and checks every published page at 360 px. A lesson
whose reviews went stale is left out of the build with a WARNING (a CI annotation), never silently.

## Libraries
p5.js 1.9.4 and KaTeX 0.16.11 are vendored in `templates/vendor/` and copied to `site/vendor/` on build; fonts
are self-hosted. Pages and headless tests work without a CDN.

## Curriculum
`curriculum.json` covers FY1–FY8 with module goals, central contents and a proposed lesson-slot list per
module, generated from the LOPS 2019 texts in `docs/lops2019/`. The reference lesson is `content/_gold/`.

## Inquiry sequence

A lesson with `inquiry.json` is rendered as inquiry stages (Pohdinta → Ennusta → Tutki → Teoriatiivistelmä → Sovella → Tarkista osaamisesi, then Tehtävät last) around the same theory, simulation, exercises and exit ticket; the page form (wide-screen columns, the closed Ennusta box, the simulation's boxes, named formula sections) is CLAUDE.md "Lesson page". Format, activity types, the simulation adapter, migration steps and tests: `docs/inquiry.md`; the teacher's brief: `docs/inquiry-spec.md`. Validate with `python scripts/inquiry.py <id>`, test with `python scripts/test_inquiry.py`.

## Exercises
A lesson's exercises are a part of their own (teacher 2026-10-28), so they can be added to and reworked without the
lesson text, and without touching the lesson's reviews:

```
content/fi/<COURSE>/<id>/exercises/exercises.json   the tasks (schema below)
content/fi/<COURSE>/<id>/exercises/solutions.md     one complete solution per task (CLAUDE.md "Lesson form" 7)
content/fi/<COURSE>/<id>/exercises/review/          their own science.md, pedagogy.md, carry.tsv
lessons/<COURSE>/<id>/answers.py                    every exercise answer (lesson-answers.py holds the lesson's own numbers)
```

- **Reviews**: `reviews.py hash|scope|carry <id> --exercises` work on the exercise set as the plain commands do on the
  lesson; `reviews.py status` shows both. Changing an exercise stales only the exercise reviews; changing the lesson
  only the lesson's.
- **Publishing**: a lesson on the site shows the exercises both exercise reviewers last passed. While a new version
  waits for review, the page keeps the previous one (taken from git, `reviews.published_exercises`) and the build
  warns; when no version has passed yet, the page says the exercises are coming.
- **Agents**: `/exercises <id> <task>` runs the developer and the two reviewers on the exercise set alone.
  `review_packet.py <id> --role developer|science|pedagogy --exercises` writes their packets to
  `exercises/review/`: the **exercise brief** (the lesson's formula sections, worked example, misconception and summary,
  figures left out) and the current exercises, so an agent never reads the lesson text, the inquiry or the simulation.
  A new lesson's first review covers both parts in one run per reviewer, which writes both reports.
- **The split itself** (2026-10-28) moved `exercises.json` and `solutions.md` into `exercises/` and cut seven
  `answers.py` files line for line into `answers.py` and `lesson-answers.py`. Every PASS from before carried over
  (category `split`, `review/carry.tsv` and `exercises/review/carry.tsv`): `reviews.py verify` re-derives each one from
  git history, checking that every file is the one that was passed and that each answers file's lines and values come
  from the one passed `answers.py`.

## Exercise schema
```json
{ "id": "fy3-2-L2-03", "level": 2, "text": "...", "answer": 2.0, "unit": "m/s²", "tolerance": 0.05 }
```
Optional `"core": true` marks an exercise as a core exercise (*Ydintehtävä*, teacher 2026-10-29): the page tags it and the exercise path says core first, then extra practice, then the challenging level. Without any `core` flag the first two exercises of levels 1 and 2 are core (build.py `core_ids`).

Force-diagram tasks (docs/force-diagrams.md, teacher 2026-10-29): `"fbd": "identify" | "select" | "error" | "draw" | "equations"` says which force-diagram skill an exercise practises (`coverage.py` checks the lesson's plan in curriculum.json). A drawing task (`"fbd": "draw"`) asks the student to draw on paper and shows its model diagram, `"model_figure": "<owner>/<name>"`, at the top of the solution.

`answers.py` in `lessons/<course>/<id>/` computes every exercise answer and prints `{id: value}`; the lint compares it with
`exercises/exercises.json`. The page checks a typed answer within `tolerance` in the browser; nothing is stored or sent.
Every exercise shows its complete worked solution from `solutions.md` behind its own *Näytä ratkaisu* button (`meta.solutions` is `all`, teacher 2026-10-27); `scripts/check_solutions.py --all` lists any missing or incomplete solution.

## Languages
Every text a visitor sees is outside the code, so a new language is two things and nothing else:

```
lang/<lang>.json                     short interface texts: menus, buttons, headings, messages, the simulations' labels
content/<lang>/<COURSE>/<id>/        a lesson's texts: lesson.md, inquiry.json, exit-ticket.json, meta.json,
                                     exercises/exercises.json, exercises/solutions.md (+ figures.json: the figures' words, below)
content/<lang>/courses.json          course titles, goals and lesson titles ({"FY3": {"title", "tavoitteet", "lessons": {id: title}}})
```

Finnish (`fi`) is the source: `lang/fi.json`, `content/fi/` and `curriculum.json`. To add English, copy
`lang/fi.json` to `lang/en.json` and translate the values (keep every `{{placeholder}}`, formula, number and unit;
`format` sets `html_lang`, `og_locale`, the decimal sign and the language's own name for the language menu), then
copy a lesson folder from `content/fi/` to `content/en/` (without `review/` and `exercises/review/`) and translate its texts. The `##`
headings of lesson.md are translated through `sections` in the language file; inquiry.json keeps the Finnish keys.
The code half of a lesson (`lessons/<COURSE>/<id>/`: answers.py, lesson-answers.py, figures.py, sim.js, sim-spec.md), the simulations,
pictures, templates and scripts are shared by every language.

- **Figures**: `figures.py` is written once. `content/<lang>/<COURSE>/<id>/figures.json` maps each Finnish text it
  draws (the words in `\text{}` and each figure's description) to the translation, and
  `python scripts/figures.py <id> --lang en` writes the figures into that language's lesson.md with its decimal sign.
- **Check**: `python scripts/check_i18n.py` (CI) lists lessons not translated yet and fails when a language misses
  a key, a course title or a figure text, or when a translation differs from the Finnish lesson in anything but its
  texts: an answer, unit, tolerance, correct option, experiment setting, id, section, figure or formula.
- **Reviews**: a translation is a lesson of its own for `reviews.py`: its hash covers its texts (and the simulation
  with that language's labels), its reports go in its own `review/` (and `exercises/review/` for its exercises), and `build.py` publishes it only when both
  reviews pass, like a Finnish lesson.
- **Build**: Finnish stays at `site/`; every other language is built into `site/<lang>/` with the same page names,
  sharing the style, scripts, simulations and pictures of `site/`. While there is one language the pages have no
  language menu; with two or more, each page has a language control linking to the same page in the other languages;
  when that language has not published the page, the link goes to its module page, whose note `#unavailable-<id>`
  says so (teacher 2026-10-29; `scripts/test_home.py`).
- Finnish only, for now: the agents' briefs, the lint's text rules (`lint_lesson.py`, `check_solutions.py`) and the
  reference lesson `content/_gold/`.

## Physics consistency
Lessons are reviewed one by one; three small tools keep one physics idea the same across chapters (teacher 2026-10-28):
- `docs/physics-guardrails.md`: the rules the FY1–FY3 audit (`docs/audits/fy1-fy3-physics-audit.md`) found broken,
  with the agreed Finnish wordings. Every developer and science-reviewer packet carries it.
- `python scripts/physics_phrases.py [<folder>]`: high-precision warnings for known wrong claims taught as fact (a wrong
  option, a named misconception and a stated model are skipped); the lint prints them, `test_physics_phrases.py` (CI)
  tests every rule on right and wrong sentences and fails if one is taught again.
- `python scripts/concepts.py list | packet <concept> | changed [<ref>]`: the sentences about one concept (uncertainty,
  fit, internal-energy, temperature, phase-change, efficiency, heat-transfer, gas, fuel) from every chapter, with file
  and place, in a packet of about 15–25 k tokens instead of the courses' 2 MB of sources; `changed` names the concepts a
  pull request touches, so a concept-wide correction gets one cross-chapter science review (`.claude/commands/lesson.md`).

## Sovella itsenäisesti
Each course ends with a few independent, exam-style tasks (teacher 2026-10-28; principles in NOTES.md §9), a part of
their own like an exercise set:

```
content/<lang>/<COURSE>/sovella/tasks.json     the tasks (schema below)
content/<lang>/<COURSE>/sovella/solutions.md   ## <task id>, ### a) … per part, ### Yleisiä virheitä, ### Hyväksytään myös
content/<lang>/<COURSE>/sovella/review/        science.md, pedagogy.md (hash: practice.py hash <COURSE>)
lessons/<COURSE>/sovella/answers.py            every number of the solutions; figures.py the model graphs
```
```json
{"intro": "…", "tasks": [{"id": "fy3-s1", "title": "Aurinkokeräin", "source": "example", "source_note": "…", "text": "situation + data (markdown)",
  "parts": [{"id": "a", "kind": "graph|calc|word", "points": 3, "text": "…", "answer": {"value": 240, "unit": "W", "tolerance": 0.08},
             "criteria": [{"key": "graph_axes", "points": 1}, {"key": "units_precision", "points": 1, "detail": "…"},
                          {"text": "task-specific criterion", "tag": "transfer", "points": 1}]}],
  "links": {"graph": "fy3-13", "math": "fy3-6"}}]}
```
A part that asks for several quantities (two waxes' coefficients) gives `"answer"` as a list of such objects, each
with a `name`; answers.py computes each as `<task>-<part>-<name>`, so every asked value is checked, not only the first.
A task of `"kind": "own"` (with one part of kind `own`) is a rubric for the student's own work, such as the FY1
investigation report, and has no solution. `python scripts/practice.py check` (CI) checks ids, points against
criteria, competency tags and shared keys (`competencies.json`), their texts in every language, chapter links,
complete solutions, answers against answers.py, figures against figures.py and translations against Finnish;
`test_practice.py` proves each check fires. `build.py` publishes `site/<COURSE>-sovella.html` when both reviews pass
(`build.py <COURSE>-sovella` previews it) and links it from the course page. Every lesson with `learn` also gets
`python scripts/coverage.py <COURSE>` writes `docs/coverage/<COURSE>.md` and `python scripts/assessment.py <COURSE>`
`docs/assessment/<COURSE>.md` (checks, figure tasks, exit ticket and possible repeats per chapter).

## Figures in tasks
Figures are drawn once, in `lessons/<COURSE>/<id>/figures.py` (or `lessons/<COURSE>/sovella/figures.py`) with
`scripts/figlib.py`. The catalog `docs/figures/catalog.json` (`python scripts/figcat.py build`; CI: `--check`) makes
them findable without opening a lesson: one line per figure with its id `<owner>/<name>`, kind, description,
labels, source, where it is used and a `reuse` note (`safe`, `reveals: …`, `decorative`, `unchecked`; the only hand
annotation, `REUSE = {name: note}` in figures.py). Lesson topics are stored once per lesson in `lessons`.
```
python scripts/figcat.py find paine syvyys --course FY3    # id, kind, reuse, use count, chapter | description
python scripts/figcat.py show fy3-9/boyle-points           # the entry and the code that draws it (no SVG)
python scripts/figcat.py render fy3-9/boyle-points --lang en
```
A task refers to a figure by id, and the build draws it in the page's language:
```json
{ "id": "fy3-9-L1-03", "level": 1, "text": "Kuvaajassa on …", "figure": "fy3-9/boyle-points", "answer": 80, "unit": "kPa", "tolerance": 0.03 }
```
The same key works on inquiry tasks (hook, text, choice, numeric, explain, interpret and an interpret task's
`question`) and on Sovella tasks and parts. A variant for a task (the same data without the fitted line or curve) is
one more FIGURES entry in the owner's figures.py with its own description. The exercise set's hash (and a lesson's,
for its inquiry tasks; Sovella's, for another chapter's figure) covers the code slice that draws each referenced
figure (`figcat.source_slice`), so only a change to that figure stales the review. In another language the figure's
words come from the owner's `content/<lang>/…/figures.json`, its decimal sign from `lang/<lang>.json`.
`python scripts/test_figcat.py` tests all of this.

