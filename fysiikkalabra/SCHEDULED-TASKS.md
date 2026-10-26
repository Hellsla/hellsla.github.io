# Scheduled tasks

Checks that scripts can do run in GitHub Actions, at no token cost: every push and pull request, and every Sunday at
21:00 Helsinki (`.github/workflows/fysiikkalabra-ci.yml`; GitHub emails on a failure). No AI task repeats them. The
review state of every lesson is one command, `python scripts/reviews.py status`, not a task. There is no nightly
lesson generation (teacher's decision 2026-10-26): lessons start with `/lesson <id>`.

| Task | Schedule (Europe/Helsinki) | Model | Prompt for the scheduled task |
| --- | --- | --- | --- |
| Monthly documentation review | first Monday of the month, 07:31 | Sonnet | In `fysiikkalabra/`: read `CLAUDE.md`, `NOTES.md`, `.claude/agents/*.md` and `.claude/commands/*.md`. Propose, as a draft pull request, (1) lines that repeat each other or a script's own check, (2) rules contradicted by a newer dated one, (3) lines that concern one course and belong in its `scope_notes` in `curriculum.json`, (4) instructions the main session does not need that an agent or command file could hold. Never delete a dated human decision; list it for the teacher instead. Add the output of `python scripts/usage.py report --all --by agent` and say which agent and model cost the most. Do not merge. |

Create it as a scheduled task in Claude (each run starts a fresh session with this repo), using the prompt above.

The daily news and weekly newsletter tasks are parked with their agents in `.claude/parked/` until the site renders their output.
