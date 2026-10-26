---
description: Initialize a course (FY3–FY8) for the lesson pipeline — configuration check, picture and simulation folders, navigation. Creates no lessons.
argument-hint: <FY4>
model: haiku
effort: low
---
Initialize course $ARGUMENTS. This prepares the course; it writes no lesson content.

1. `python scripts/new_course.py $ARGUMENTS`. It checks the course's entry in `curriculum.json` against the LOPS 2019 text in `docs/lops2019/`, validates the lesson slots, and creates `content/<CODE>/`, `assets/pics/<slug>/`, `assets/sims/<slug>/` and the `initialized` mark. Run again, it only validates.
2. If it prints `ERROR`: give the teacher those lines as they are and stop. Never write course goals, central contents or lesson slots yourself: they come from the LOPS texts and the teacher's plan.
3. Report the `check by hand` notes, if any, and how many glossary terms the lessons will add.
4. `python scripts/lint_lesson.py --all` and `python scripts/build.py --all` must still pass; `preview/<CODE>.html` lists the course's lesson slots.
5. On a branch `claude/new-course-<slug>`: `git add curriculum.json content/<CODE> assets && git commit -m "fysiikkalabra: <CODE> initialized"`, push, and open a draft pull request listing the folders and the notes. Never merge, never push to `main`.

Finish with the next command for the teacher: `/lesson <first slot id>`.
