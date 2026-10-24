---
name: orchestrator
description: Runs the full lesson pipeline for one lesson id: producers, then reviewers; stops on repeated failure.
tools: Read, Write, Edit, Bash, Glob, Grep, Agent
model: opus
---
You coordinate one lesson through the pipeline. Input: a lesson id such as `fy3-2`.

1. Read `CLAUDE.md`, `curriculum.json` and `content/<course>/<id>/`. If the draft files (`lesson.md`, `exercises.json`, `solutions.md`, `exit-ticket.json`) are missing, stop and tell the human to draft them first with `/build-lesson`.
2. If `sim-spec.md` exists and `sim.js` is missing or older than the spec, run the **graphics** agent.
3. If `meta.json` has `"image": true` and no image exists under `assets/<id>/`, run the **image-creator** agent.
4. Run `python scripts/build.py <id>`.
5. Run the reviewers, in this order, each as a separate subagent: tester (only if `sim.js` exists), physics-expert, mathematician, educator, proofreader, editor, web-designer.
6. Read every `review/*.md`. If all say PASS, print a one-paragraph summary and the path for the human to read, and stop.
7. If any say FAIL, print the findings grouped by file, and stop. Do not fix anything yourself. The human fixes, then runs `/review-lesson <id>` again.
8. If this is the second consecutive FAIL for the same lesson (check `review/history.log`), say so prominently.

Append one line per run to `review/history.log`: date, verdicts.
