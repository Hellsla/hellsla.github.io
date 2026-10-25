---
description: Take one lesson from draft to a reviewed pull request: developer, checks, two independent reviews, fixes, PR with a teacher summary
argument-hint: <lesson-id>
---
Run lesson $ARGUMENTS through the pipeline. You coordinate; the agents do the work. Keep your own reading to `CLAUDE.md`, `python scripts/reviews.py status $ARGUMENTS` and the reports; never open lesson files yourself.

1. If the lesson folder has no `lesson.md`, run the **developer** agent with "draft"; otherwise skip to step 2.
2. Run `python scripts/check_lesson.py $ARGUMENTS`. If anything fails, run the **developer** with "fix: make the checks pass" and repeat (at most twice).
3. Run the **science-reviewer** and the **pedagogy-reviewer** as two separate subagents, in parallel, each with only the lesson id. Then `python scripts/reviews.py status $ARGUMENTS`.
4. If the state is `reviewed`, go to step 6. If either report says FAIL, run the **developer** with "fix" (it reads both reports), then repeat from step 2. At most three review rounds; after the third, stop and report which blocking findings remain.
5. Commit once per round: `git add content tests/sims glossary.json && git commit -m "fysiikkalabra: $ARGUMENTS review round <n>"`.
6. Finish: `python scripts/build.py --all`, `python scripts/build.py` (plain, so `site/` carries the lesson when it is reviewed), commit `site/`, push the branch (`git push -u origin <branch>`), and open or update the pull request with this body, in this order:
   - **Oppitunti**: id and title, one sentence on what it teaches, what changes on the live site (new page, or which pages are removed with the build's WARNING lines, if any).
   - **Tarkistukset**: the last `check_lesson.py` lines and the two verdicts with their hashes.
   - **Kierrokset**: rounds run and the blocking findings fixed in each, one line per finding.
   - **Kulutus**: one line per agent run (agent, model, duration, tokens as the tool result reports them), copied from `review/usage.log` — append a line there after every agent call.
   - **Avoimet kohdat**: polish items left as they are, and anything the teacher must decide.
   Merging the pull request is the teacher's publication decision: never merge, never push to `main`.
