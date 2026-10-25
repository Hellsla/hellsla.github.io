---
description: Take a drafted lesson all the way to published without a human in between
argument-hint: <lesson-id>
---
Lesson id: $ARGUMENTS

Run the orchestrator agent on this lesson from the start: reviewers in parallel, the fixer on any FAIL, reviewers again (at most three rounds), then the publisher. The publisher commits to the current branch only through `python scripts/gate.py $ARGUMENTS --publish`. Report one paragraph: rounds used, verdicts, hash, and whether the push succeeded. If the lesson could not be published, list the remaining findings and why the fixer could not resolve them.
