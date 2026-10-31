---
description: Audit existing published content against the editorial quality standard (all three reviewers, visual & editorial first), and with --fix correct what the audit found, through the normal review gate
argument-hint: <lesson-id | lesson-id --exercises | investigation-id | tvt-guide-id | COURSE-sovella> --audit-only | --fix [--deep] [--lang en] [--warn 200000] [--limit 350000]
model: sonnet
effort: medium
---
Audit $ARGUMENTS against `docs/EDITORIAL_QUALITY_STANDARD.md`. Work in `fysiikkalabra/` (`cd fysiikkalabra` first): every path below is relative to it. You coordinate; the agents work from packets. Read only the scripts' output and the agents' reports; never open a packet, a lesson file or a capture yourself.

**Route by content type** (never pass an investigation through the lesson steps):

| id | type | hash · status | packets | screenshots |
|---|---|---|---|---|
| `fy4-6` | lesson (and its exercise set with `--exercises`, or both when both are asked) | `reviews.py hash/status <id> [--exercises]` | `review_packet.py <id> --role <r> [--exercises]` | `screenshot.py <id> --if-stale` |
| `fy10-jousivakio` | experimental investigation (`content/fi/tutkimukset/`) | `investigations.py hash/status` | `review_packet.py <id> --role visual`; science and pedagogy as the investigation's earlier reviews were run (their agent files, the investigation's files) | `screenshot.py <id> --if-stale` |
| `tvt-kuvaaja` | TVT guide (`content/fi/tvt/`) | `guides.py hash/status` | `review_packet.py <id> --role visual` | `screenshot.py <id> --if-stale` |
| `FY3-sovella` | Sovella itsenäisesti set | `practice.py hash/status FY3` | `practice.py packet FY3 --role science|pedagogy|visual` | `screenshot.py FY3-sovella --if-stale` |

Anything else: stop and say which types exist. `--lang en` / `fi-easy` audits a translation (every script takes `--lang`).

**Routing of agents** (as `/lesson`; `.claude/agents/`): visual-editorial-reviewer Sonnet medium; pedagogy-reviewer Sonnet medium; science-reviewer Opus medium; developer Sonnet medium (Opus medium only on `/lesson`'s conditions). Pass `model` and `effort` on every Agent call. If the agent types are not registered in this session, run a general-purpose agent with the same model and the first line `Read .claude/agents/<name>.md and follow it as your instructions.` The prompt is one line naming the packet: `Read <packet path> and follow it. Lesson: <id>. Mode: <mode>. Round: <n>.` (an audit says `Mode: audit (<mode>)`).

**Budget.** Warning 200 000 and hard limit 350 000 per audited id unless `--warn`/`--limit` say otherwise, counted like `/lesson` (the sum of the agents' final context sizes). Past the hard limit, stop safely and report what remains. Never skip a needed review to stay under a number.

## --audit-only: find the quality gaps, change no content
1. `python scripts/check_lesson.py <id>` for a lesson (writes `review/checks.txt`); for the others their `check` command (`investigations.py check`, `guides.py check`, `practice.py check <COURSE>`). A failing deterministic check is a finding in itself.
2. `python scripts/screenshot.py <id> --if-stale` (reuses unchanged captures).
3. Status: which reviews are current. **Visual**: run the visual-editorial-reviewer whenever its report is not a current PASS (on the visual baseline it has never been run): `review_packet.py … --role visual`, one agent. **Science and pedagogy**: their current PASS reports stand for the gate and are not re-run; their earlier reports are the audit's evidence for dimensions 1–6. Only with `--deep` (the teacher asks for a fresh assessment of physics and learning, e.g. the pilot) run them too, in parallel with the visual reviewer, on full packets, telling them in the prompt: `Audit: judge as in a full review, score your dimensions of docs/EDITORIAL_QUALITY_STANDARD.md (1–5 each) under a closing "## Scores" section, and write review/audit-<role>.md instead of review/<role>.md.` (an audit report is not a gate report: it never replaces the PASS that publishes the content). A science or pedagogy report that is not a current PASS is run as in `/lesson` step 3 instead.
4. Write `review/audit.md` (for an exercise set `exercises/review/audit.md`): date, the content hashes, the checks' result, one row per reviewer (verdict, mode, which report), the scores of dimensions 1–10 that the reports give (leave a dimension blank when no report scored it, never guess), and every finding classified **Critical**, **Major** or **Minor** with its file and the reviewer that found it. End with the three most valuable corrections. This file is the orchestrator's summary and is committed with the reports.
5. Commit the reports (`git add content && git commit -m "fysiikkalabra: <id> quality audit"`); content files are untouched (`git diff --stat` shows only `review/` files). A visual FAIL on content still under the visual baseline does not unpublish it (`reviews.py` module docstring): the audit records the gap; `python scripts/reviews.py baseline` lists it.

## --fix: correct what the audit found, through the gate
1. Start from `review/audit.md` and the reports it names when they are for the current hash; otherwise run `--audit-only` first.
2. Choose the corrections: every Critical and Major finding, and the Minor ones that are objective (a wrong term, a clipped label), never a rewrite for taste, never extra figures or tasks to raise a count. A finding that needs the teacher's decision (a project-wide colour, notation or structure) is left for the PR's **Avoimet kohdat**.
3. `python scripts/review_packet.py <id> --role developer --fix` (`--exercises` for the exercise set; Sovella: `practice.py packet <COURSE> --role developer`), then the developer with `Polish to fix: <ids, or none>.` and the findings to fix named in its prompt. Figures are changed in `figures.py` and regenerated (`python scripts/figures.py <id>`), never hand-edited in lesson.md when figures.py draws them.
4. `python scripts/check_lesson.py <id>` (or the type's check) until every line is ok; at most twice through the developer.
5. `python scripts/screenshot.py <id> --if-stale`, then `python scripts/reviews.py scope <id>` (and `--exercises`): every reviewer whose mode is `none` is carried (`reviews.py carry`); the others run on their packets in parallel (a figure restyled: visual delta, science none; a force direction changed: science and visual). Content under the visual baseline gets its first genuine visual review in full. Repeat fix → checks → affected reviews at most three rounds.
6. Finish as `/lesson` step 6: `python scripts/usage.py collect <id> --round <n>`, `python scripts/build.py --all`, `python scripts/build.py`, check that `site/` still has every page it had (`git status site/` shows no deleted page; `reviews.py status <id>` reviewed), commit, push the branch and open or update the **draft** pull request: **Auditointi** (scores before and after), **Korjaukset** (each finding and what changed), **Tarkistukset**, **Kulutus** (`python scripts/usage.py report <id>`), **Avoimet kohdat**. Merging is the teacher's publication decision.

**Learning loop** as in `/lesson`: an objectively testable recurring finding gets a check; otherwise a dated line in NOTES.md. A recurring visual or editorial finding across audited chapters is proposed as an addition to `docs/EDITORIAL_QUALITY_STANDARD.md`, never silently enforced.
