# Scheduled tasks (set these up once)

| Task | Schedule (Europe/Helsinki) | Prompt for the scheduled task |
| --- | --- | --- |
| Weekly QA | Sunday 21:00 | Run `python scripts/lint_lesson.py --all && python scripts/build.py && python scripts/test_sims.py`, then the tester and web-designer agents on `all`; message me only if anything fails. |
| Review digest | after each batch (manual) | List every lesson with `status: draft` and the latest `review/*.md` verdicts as a table. |

Create them as scheduled tasks in Claude (each run starts a fresh session with this repo), using the prompts above.

The daily news and weekly newsletter tasks are parked with their agents in `.claude/parked/` until the site renders their output.
