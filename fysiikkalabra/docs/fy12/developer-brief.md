# FY12 — brief for a unit developer

You write one lesson (course unit) of FY12 *Fysiikan ylioppilaskertaus*, the Finnish exam-review course (16 lessons
reviewing FY1–FY8 with many original exam-style tasks). Work in `fysiikkalabra/`. All student text is **Finnish**.

## Read first (in this order)
1. `docs/FY12_PLAN.md`: the course, the lesson form table (the counts are your specification) and the lesson list.
2. `CLAUDE.md`: the house rules. Read "Physics and maths conventions", "Lesson form", "Readability" and "Exam
   readiness" closely, then NOTES.md §1 (LaTeX), §3 (figures, complete solutions), §8 (readability), §9 (Sovella).
3. `scripts/units.py` docstring (unit format), `docs/inquiry.md` (activity types and fields), README
   "Sovella itsenäisesti" (task-set schema) and `competencies.json` (criteria keys).
4. Models. Copy the form, never the text:
   - unit structure: `content/en/units/fy14-photoelectric/` + `lessons/units/fy14-photoelectric/figures.py`;
   - Finnish inquiry tasks, feedback and complete solutions: `content/fi/FY4/fy4-5/inquiry.json`, `content/fi/FY3/fy3-6/`;
   - long exam-style tasks, solutions, answers.py and figures.py: `content/fi/FY4/sovella/`, `content/fi/FY3/sovella/`,
     `lessons/FY4/sovella/`, `lessons/FY3/sovella/`.
5. The chapters you review. Read their `content/fi/<COURSE>/<id>/lesson.md` (theory and Esimerkki only) so that your
   wording, symbols and conditions match what the student was taught. Use `docs/physics-guardrails.md` for the
   agreed wordings.

## What you write (only these)
- `content/fi/units/<id>/unit.json` (course `FY12`, `chapter` and `order` as listed in `local-courses.json`
  FY12, `kind` `review`, `minutes` 75, `subjects` `["physics"]`, `sources` with checked dates for any fact that may
  change), `unit.md`, `inquiry.json`, `teacher.md`, `exit-ticket.json` (optional).
- `content/fi/units/<id>/sovella/tasks.json` and `solutions.md`; `lessons/units/<id>/sovella/answers.py` and
  `figures.py` (model graphs); `lessons/units/<id>/figures.py` (hero and theory figures).
- `content/fi/units/<id>/review/developer.md`.
- Do not edit shared files (`scripts/`, `templates/`, `lang/`, `local-courses.json`, other units, chapters or
  `site/`). Put a needed shared change under "Shared issues" in your report. Do not commit. Do not run the full
  `build.py`; build only your unit.

## Content rules
- **Original tasks only.** Never copy or paraphrase YTL exam tasks, textbook tasks or the PDFs in the repository
  root (they follow a commercial textbook). Write new, realistic, Finnish situations: everyday life, technology,
  nature, Finnish places, sport, the school lab. Data must be realistic and computed in Python.
- **Exam style.** Long tasks give a situation and source material (a table, figure or short text), then parts a), b), c)
  with points. No part names the formula or the model. Points are 12–20 per task: graph/data tasks and cross-module
  tasks about 15–20, the rest about 12–15. The rubric uses shared criteria keys plus task-specific criteria. Every
  calc part has the full step set (Annettu · Kysytty · Periaate · Kaava · Muunnokset · Sijoitus · Vastaus ·
  Järkevyys). Word parts have Kysytty · Periaate · Mallivastaus, and graph parts have Kysytty · Kuvaaja ·
  Mallivastaus with a model graph from figures.py. Every task has `### Yleisiä virheitä`.
- **Skills links.** Every long task has `"skills"`, the 1–4 chapters (lesson ids with a folder) whose skills it uses,
  and `"links"`, one chapter per competency used. Every Ennusta and Tarkista choice feedback and every `practice`
  text names the chapter to review as `luvussa *Chapter name*`, never as an id. Links in markdown are
  `[*Chapter name*](<id>.html)`.
- **Short tasks.** Sovella has 8 tasks: about 4 `choice` (claims, error-spotting, which graph, which force diagram)
  and 4 `numeric` with a complete `solution`, `hints` (at most 3) and `mistakes` for typical wrong values. Ennusta
  has 6 `choice` items as a diagnostic. Every option has feedback that corrects the specific misconception. The
  correct option is not the longest: keep options within about ±30 % of each other in length, and vary which
  option is correct.
- **Theory summary** (unit.md `##` sections placed by `theory` activities): a concept map or overview figure, the key
  laws once each in display LaTeX with symbols named and conditions of validity, "Yleisiä virheitä", and "Kertaa
  tarvittaessa" with chapter links. At most about 600 words. No new physics beyond FY1–FY8 and the chapters you
  review.
- **Project rules.** Everything mathematical is LaTeX, including every number with its unit in prose
  (`$12\,\text{N}$`). Use `\cdot` for multiplication and a colon for written division, `\Delta x` for uncertainty,
  and `\overline{F}` for vectors (never `\vec` or `\mathbf`). Velocity, acceleration and force always have different
  colours in figures (force red, velocity blue, acceleration orange). Use a decimal comma in the text and g =
  $9{,}81\,\text{m/s}^2$. Unit conversions are done by substitution ($4{,}2\,\text{km} = 4{,}2 \cdot 1000\,\text{m}$).
  Results have three significant figures unless the data has fewer, and the solution says why. The opening
  illustration (`hero`) is a polished SVG with no text and no real people. Figures are printed-textbook quality and
  labels are at least 14 px at 390 px width.
- **teacher.md**: a 75-minute plan (which tasks are done in class and which at home), how to use the diagnostic,
  pair work, and what to do for fast and slow students.
- `learn` has 2–3 goals that complete "Tällä tunnilla opit": "ratkaisemaan …", "laatimaan …", "arvioimaan …".
  `prior` items end with "(luku *Name*)".

## Checks before you hand over
`python3 scripts/practice.py figures units/<id>` · `python3 scripts/units.py figures <id>` ·
`python3 scripts/practice.py check units/<id>` and `python3 scripts/units.py check` (no errors) ·
`python3 scripts/build.py <id>` → `preview/<id>.html` · `python3 scripts/check_layout.py <id> --width 360` and
`--width 1280` · open the page with Playwright (`scripts/_browser.launch(pw)`). Answer every task once, open every
solution and model answer, and confirm that there are no console errors, raw `$` or `.katex-error`. Take screenshots
at 390 and 1280 and look at them yourself. `screenshot.py` may not know units, so if it fails, capture with
Playwright.

`review/developer.md`: `VERDICT: DONE` on line 1, then the files, task counts per type, numbers computed, open
questions and Shared issues. Report back in under 200 words.
