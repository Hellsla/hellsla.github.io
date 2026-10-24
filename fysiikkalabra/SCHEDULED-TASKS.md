# Scheduled tasks (set these up once)

| Task | Schedule (Europe/Helsinki) | Prompt for the scheduled task |
| --- | --- | --- |
| Daily news | 06:00 every day | In this repo run `/daily-news`, then commit to branch `news` and open a PR titled with today's date. |
| Weekly newsletter | Friday 15:00 | Run `/weekly-newsletter`; message me the draft path. |
| Weekly QA | Sunday 21:00 | Run `python scripts/build.py && python scripts/test_sims.py`, then the tester and web-designer agents on `all`; message me only if anything fails. |
| Review digest | after each batch (manual) | List every lesson with `status: draft` and the latest `review/*.md` verdicts as a table. |

Create them as scheduled tasks in Claude (each run starts a fresh session with this repo), using the prompts above.
