# FY9 – Fysiikan ylioppilaskertaus: plan

The teacher asked on 2026-11-04 (00.27 Helsinki): "Aloita suunnittelemaan kertauskurssia ylioppilaskokeeseen. Tässä tulee
olla 16 tuntia ja paljon tehtäviä." Two minutes later he wrote "Lähde tekemään ehdotuksellasi", so the plan below
is being built without a separate approval round. The plan document is https://claude.ai/artifact/HR1AoyJch7H9k2mzn3EwVN.
This file is its durable summary. The code FY9 is a default and is still open (see Open questions).

## What the course is
- A school-specific course (`local-courses.json` `FY9`, language `fi`, status `building`). It is not a national
  module, so it has no national goals and is not in curriculum.json. It has 16 lessons: one course unit each
  (`scripts/units.py`, `content/fi/units/fy9-*/`, kind `review`).
- It reviews FY1–FY8 and practises exam task types with **many original tasks** in the style of the matriculation
  exam. Two sources are never used: the teacher's timetable PDFs in the repository root, which follow a commercial
  textbook, and past YTL or textbook tasks, which must not be copied or paraphrased. All tasks are written new.
- Every task names the chapters whose skills it uses (`skills`: lesson ids). The page shows them as chapter-name
  links, never as ids, so a student can go back to the chapter they need to review.

## Lesson form (every review unit)
| Stage | What | Count |
|---|---|---|
| Pohdinta (`herata`) | a short exam-like situation and one question | 1 hook |
| Ennusta | lähtötasotesti: conceptual `choice` items. Each option's feedback corrects a misconception and names the chapter to review | 6 |
| Tutki | one `interpret` task: a table, graph or figure (reuse catalog figures) with a question. Not a new simulation | 1 |
| Teoriatiivistelmä | concise review: one concept-map figure, the key laws as display LaTeX with their conditions of validity, a "Yleisiä virheitä" section, and chapter links in "luvussa *Name*" form. At most about 600 words | – |
| Sovella | short Osa I-type tasks: `choice` statements and `numeric` items with complete solutions, mistakes and hints | 8 |
| Tarkista osaamisesi | three checks (choice, numeric, explain) with `practice` links to chapters, then the exit ticket | 3 |
| Tehtävät (the unit's task set) | long exam-style tasks in the Sovella itsenäisesti format (`sovella/tasks.json`): 2 `calc`, 1 data → graph → fit → interpret, 1 explanation (`word`), 1 experimental design or report critique, 1 cross-module task combining an earlier module | 6 |

Lesson 1 (`fy9-koe`) covers the exam and answering technique. It has a diagnostic of 24 items over the whole
course in Sovella, and 4 long example tasks, one of each type, with model answers and rubrics. Lesson 16
(`fy9-harjoituskoe`) is the mock exam: a set of short tasks plus long tasks to choose from. Its structure follows
the YTL rules that are current when it is written, verified from ylioppilastutkinto.fi.

## Lessons
1 fy9-koe · 2 fy9-mittaaminen (FY1 measuring, uncertainty, graphs, FY10) · 3 fy9-kokeellisuus (FY1 own
investigation, FY10) · 4 fy9-energia (FY2, fy3-15) · 5 fy9-lampo (FY3 heat) · 6 fy9-kaasut (FY3 pressure, gases,
heat engines) · 7 fy9-liike (fy1-5, FY4 kinematics) · 8 fy9-voimat (FY4 Newton, FBD, friction, coupled bodies) ·
9 fy9-sailymislait (FY4 energy, momentum) · 10 fy9-ympyraliike (FY5 1–6) · 11 fy9-aallot (FY5 7–17) ·
12 fy9-tasavirta (FY6 1–9) · 13 fy9-sahkokentta (FY6 10–16) · 14 fy9-magnetismi-valo (FY7) · 15 fy9-moderni
(FY8) · 16 fy9-harjoituskoe.

## How it is built (`scripts/practice.py`, `scripts/units.py`, `scripts/build.py`)
- A unit's task set lives in `content/fi/units/<id>/sovella/{tasks.json,solutions.md}` and
  `lessons/units/<id>/sovella/{answers.py,figures.py}`. Its key in practice.py is `units/<id>` and its task ids are
  `<id>-s<n>`. `practice.py check units/<id>` and `units.py check` validate it. It is part of the unit's content
  hash, so the unit's three reviews (science, pedagogy, visual) cover it. The page renders it as the unit's
  Tehtävät, last, with the shared rubric component (`selfassess.js`).
- Any Sovella task, in a module or a unit, may carry `"skills": ["fy1-4", "fy4-5"]`. These render as "Taidot
  luvuista: …" with chapter-name links.

## Stages (one PR each)
1. Frame and lessons 1–4. 2. Lessons 5–9. 3. Lessons 10–11. 4. Lessons 12–15, after the FY6–FY8 chapters they
review are published. 5. Mock exam. The YO-sekoitin page (`scripts/mixer.py`, built in stage 1) mixes every long task of FY9 with the modules'
Sovella tasks and can be filtered by module, competency and task type. English and fi-easy are translated after
review, as in the other courses. Units support one language per course today, so the translations need units.py to
allow several languages for a course.

## Open questions for the teacher
- The course code and name (FY9 "Fysiikan ylioppilaskertaus" is a default).
- Whether the mock exam is a shortened 75-minute lesson or a full-length separate session.
- Whether about 320 tasks is enough.
