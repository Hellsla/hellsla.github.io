---
description: Take one lesson from its curriculum slot to a reviewed draft pull request (packets by reference, reviews by what changed, measured usage)
argument-hint: <lesson-id> [--warn 300000] [--limit 450000]
model: sonnet
effort: medium
---
Run lesson $ARGUMENTS through the pipeline. Work in `fysiikkalabra/` (`cd fysiikkalabra` first): every path below is relative to it. You coordinate; the agents do the work from packets. Read only the scripts' output and the agents' reports; never open a packet or a lesson file yourself.

**Routing** (the agent types `developer`, `science-reviewer` and `pedagogy-reviewer` are defined in `.claude/agents/` at the repository root; pass `model` and `effort` on every Agent call; say in the PR which model ran each step and why):

| step | agent | model, effort |
|---|---|---|
| this orchestration | — | Sonnet (this command's `model`) |
| draft, fix | developer | Sonnet medium. Opus medium only for a new numerical model (time integration, particle dynamics, a quantity that must emerge from the simulation), physics the course has not used before, or after a Sonnet attempt failed `check_lesson.py` twice or a science review found physics errors in its work. A simulation alone is not a reason: interface, layout, labels, colours, the adapter and test assertions stay Sonnet. Opus high only after Opus medium failed; Fable never without the teacher's word. |
| science review | science-reviewer | Opus medium |
| pedagogy review | pedagogy-reviewer | Sonnet medium |

**Prompts.** An agent's prompt is one line naming its packet, never the packet itself: `Read <path printed by review_packet.py> and follow it. Lesson: <id>. Mode: <mode>. Round: <n>.` For a fix, add one line: `Polish to fix: <ids, or none>.` and, after a failed check, the failing lines of `check_lesson.py`.

**Budget.** Warning 300 000 and hard limit 450 000 per lesson unless `--warn`/`--limit` say otherwise, counted as the sum of the agents' final context sizes the task notifications report (the measure every earlier run used; typical: draft 80–150 k, full review 50–110 k, fix 30–60 k, delta review 15–30 k). Past the warning, say so in the PR and continue; past the hard limit, stop safely: finish nothing half-way, commit what exists, and open the draft PR with a "Kesken" section saying which review or fix remains. Never shorten or skip a necessary review or correction to stay under a number.

0. `python scripts/courses.py init-lesson <id>` (meta.json from the curriculum slot; if the course is not initialized, tell the teacher to run `/new-course <course>` and stop).
1. If the folder has no `lesson.md`: `python scripts/review_packet.py <id> --role developer`, then the developer ("draft").
2. `python scripts/check_lesson.py <id>`: lint (with the page rules of CLAUDE.md "Lesson page", errors on a lesson being written or edited), LaTeX, build, simulation tests, inquiry tests with the page form at 360, 1280 and 1920 px, answer positions, 360 px. On FAIL run the developer with `--role developer --fix` and the failing lines; at most twice.
3. `python scripts/screenshot.py <id>`, then `python scripts/reviews.py scope <id>`. A reviewer whose mode is `none` (the change is outside its judgement) is not run: `python scripts/reviews.py carry <id>` records that its PASS carries over. For the others `python scripts/review_packet.py <id> --role science` / `--role pedagogy` and the reviewers as two parallel subagents. Then `python scripts/reviews.py status <id>`.
4. If `reviewed`: go to 6. If a report says `ESCALATE`: commit, regenerate that packet, and if it is still delta add `Full review required.` to the prompt. If a report says FAIL: classify every finding (Blocking and Polish) as **A** scientific/pedagogical, **B** usability/accessibility or **C** cosmetic. Run the developer with `--fix`, naming the A and B Polish items; C items go to the PR only. Then from step 2. At most three review rounds; after the third, stop and report what remains.
5. Commit after each round's reviews and before a fix, so the next scope finds the reviewed version: `git add content tests/sims glossary.json assets && git commit -m "fysiikkalabra: <id> round <n>"`.
6. Finish: `python scripts/usage.py collect <id> --round <n>` (measured tokens and cost of every agent and of this session's share; nothing from the transcripts but numbers), `python scripts/build.py --all`, `python scripts/build.py`, commit `site/` and `review/`, push the branch `claude/lesson-<id>`, and open or update the draft pull request: **Oppitunti** (id, title, one sentence, what changes on the site, build WARNING lines); **Tarkistukset** (the last `check_lesson.py` lines, the verdicts with hashes, carried-over reviews and why, CI link); **Kierrokset** (rounds, Blocking findings fixed, A/B Polish applied, C left); **Kulutus** (`python scripts/usage.py report <id>`, and the model of each step with its reason); **Vaikutus** (`python scripts/reviews.py impact origin/main`); **Opittua** (rules or tests added); **Avoimet kohdat**. Merging is the teacher's publication decision: never merge, never push to `main`.

**Batch.** When one small change of the same kind goes to many lessons (a law named, a sim text moved into its boxes, figures recoloured line for line; all classified by `reviews.py scope` as delta or none), run it as one batch instead of a /lesson per lesson: the developer per lesson with a narrow prompt, `check_lesson.py` per lesson, then `reviews.py carry` for every lesson whose reviewer is `none`, `python scripts/review_packet.py --batch <id>,<id>,... --role science` / `--role pedagogy` and ONE reviewer of each kind (prompt `Read review-batch/packet-<role>.md and follow it. Lessons: <id>, <id>, .... Mode: delta. Round: 1.`), which writes each lesson's own report. `usage.py collect <id>,<id>,...` shares the batch runs among the lessons. A lesson the scope puts in full review leaves the batch for a /lesson of its own.

**Simulations.** The developer creates the lesson's own folder (`assets/sims/<course>/<id>/`), reuses one the course already has (`"sim": "<name>"` in meta.json) or modifies one. Modifying a folder another lesson uses re-opens that lesson's reviews too (`reviews.py impact` lists them): do it only when the packet's task or the teacher says so, and name every affected lesson in the PR.

**Learning loop.** When a finding is an objectively testable, recurring error: fix it, then add a check (`lint_lesson.py`, `test_sims.py`, `check_layout.py`, `test_inquiry.py`) with a test that catches the original case and passes on every other lesson; if it is not testable, add one dated line to `NOTES.md` under the right heading, with the lesson id (`(2026-11-02, fy4-3)`). Mention it in the PR.
