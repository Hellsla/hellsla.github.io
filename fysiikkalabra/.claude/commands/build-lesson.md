---
description: Draft one lesson with the human, then run producers and reviewers
argument-hint: <lesson-id>
---
Lesson id: $ARGUMENTS

1. Read `CLAUDE.md`, `curriculum.json` and `content/_gold/`. Show me the slot's goals and prerequisites.
2. Draft `lesson.md` with me in dialogue: propose a motivating question and outline first, wait for my answer, then write the theory. Match the gold standard.
3. Use the exercise-author agent to draft `exercises.json` and `solutions.md`; show me its "least sure" list.
4. Draft `exit-ticket.json`. Ask me for a one-paragraph `sim-spec.md` if `curriculum.json` says `sim: true`.
5. Write `meta.json` with `"status": "draft"`.
6. Run the orchestrator agent on this lesson and show me its summary.
