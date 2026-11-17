# Quality assurance: who checks what

A map, not new rules (teacher 2026-11-13). The rules are in `CLAUDE.md` (this folder's), `NOTES.md`,
`EDITORIAL_QUALITY_STANDARD.md` and `physics-guardrails.md`; the checks are in `.github/workflows/fysiikkalabra-ci.yml`
(each step's name says what it checks). Read this to find the right gate, and add a row when a gate is added.

## The gates, in the order a change meets them
| Gate | Who | Covers | Does not cover |
|---|---|---|---|
| 1. Deterministic checks | `python scripts/check_lesson.py <id>` (developer, before any review; the orchestrator runs it inside `python scripts/round.py <id>`, which also regenerates the catalog, assessment and coverage files, carries, captures and packets) | lint, complete solutions, notation, LaTeX, answers, build, simulation and inquiry tests, layout at 360, 390, 768 and 1280 px (CI's browser image when Docker is available) | anything a script cannot judge |
| 2. Science review | science-reviewer (Opus) | physics and mathematics; the only judge of scientific correctness | readability, layout |
| 3. Pedagogy review | pedagogy-reviewer | whether a 16–19-year-old can learn from it, on a phone and a laptop | physics |
| 4. Visual and editorial review | visual-editorial-reviewer, from the captures | figures, graphs, mathematical typography, Finnish, presentation | physics (sent to the science reviewer) |
| 5. Publication rule | `scripts/reviews.py` | a part is built only when all three PASS for its current hash; `scope` decides who looks again, `carry` records a PASS that holds | whether the teacher agrees |
| 6. CI | `fysiikkalabra-ci` | every check of 1 in full, `reviews.py verify`, committed `site/` equals a fresh render; browser checks (simulations, inquiry, layout at eight widths) only for the pages `ci_scope.py` names | pages outside the scope until the weekly run |
| 7. Teacher | the teacher | figure approvals (`approve-figures`), presentation-only rows, plans, merging = publication | — |

The three reviewers each see only their own packet and never another's report. Automatic review never replaces the
teacher's approval of a figure, of a plan, or of a material content change: the teacher merges.

## Where each kind of content is checked
| Content | Command | Reviews | CI |
|---|---|---|---|
| FY1–FY8 lesson | `/lesson` | 2–4 for the lesson | full checks; browser checks for its pages |
| Exercise set | `/exercises` | 2–4 for the set (own hash); the page shows the last passed version | as above |
| Sovella itsenäisesti | `/practice` | 2–4 | `practice.py check` |
| Example exam | `/exam` | 2–4 | — |
| Investigation, TVT guide, course unit | `/quality-audit` | 2–4 (or the visual baseline until the first material change) | `investigations.py`, `guides.py`, `units.py` |
| Teacher figures | `/figure-fixes` | none after the teacher's approval; layout checked | `figcat.py`, layout |
| Ahjo, Kilparobotiikka, LUMA-tutor (`jaksot/`) | — | none | their own page tests |
| Scripts, templates, CI | developer | none (no content hash) | unit tests; the SMOKE sample of pages |

## Known gaps (2026-11-13; 1 and 2 narrowed 2026-11-16, work queue 5)
1. **Browser checks are scoped.** A pull request tests the pages it can change, `main` the pages its push can change
   against the previous `main`; the two can differ. A page can be broken without any run testing it until the weekly
   run (Sunday 21:00). After a merge, look at the run on `main`. A page whose only change is its `?v=` cache tokens is
   not counted as changed (`ci_scope.py`); a layout failure names its task, solution step and element, so a failure on
   `main` can be fixed from the log.
2. **Local runs differ from CI unless run in CI's image.** CI runs the browser checks in
   `mcr.microsoft.com/playwright/python:v<version>-noble`, the version `requirements-ci.txt` pins (`ci_env.py check`
   keeps the two equal). A session's own Chromium is another build with other fonts and measured formulas 4-9 px
   narrower (en/fy1-1 2026-11-13; fy2-3 at 360 px: 3 clipped formulas locally, 13 in the image). `python
   scripts/ci_env.py run <command>` runs a check in that image (Docker), and `check_lesson.py` does it for its layout
   checks by itself; without Docker the gap remains. In a Claude Code cloud session (root, Docker installed, daemon not
   running) `ci_env.py` starts `dockerd` itself and pulls the image through the session's proxy (about 2 GB, once per
   session; checked 2026-11-17, work queue 0d: fy2-3 at 360 px gives 5 + 3 + 5 = 13 known clipped formulas in the image),
   so no change to the environment is needed. The session's own Playwright (the cloud image has 1.63; `pip install -r
   requirements-ci.txt` gives 1.65) matters only when Docker is missing; the browser checks run in the image's 1.65.
   `round.py` also checks the session before a round: a shallow clone (which makes `reviews.py scope` answer FULL for
   "not in git history") is deepened with `git fetch --unshallow`, and a missing Python package stops it with the
   `pip install -r requirements-ci.txt` command.
3. **Reviewers share a model family.** Three independent reviews are independent in their packets, not in their blind
   spots. The teacher's own reading is the check on that, above all for new physics.
4. **Language versions.** en and fi-easy are judged by the same agents and `check_i18n.py`; no person checks them.
5. **The `jaksot/` units** (Ahjo, Dronelabra, Kilparobotiikka, LUMA-tutor) have page tests but no review gate; the
   teacher's reading is their review.
6. **Pages at the repository root** (`*.html` outside `fysiikkalabra/`) are outside this pipeline and its CI.
7. **Volume.** Unreviewed exercise sets are not shown, so nothing wrong is published, but the backlog grows when new
   tasks are written faster than they are reviewed (51 sets on 2026-11-13). Write new tasks for a course after its
   backlog is reviewed (`ROADMAP.md`).

## Overlaps worth knowing
- Layout is checked by `check_lesson.py` (360, 390, 768, 1280 px) and again by CI (eight widths): the local check is the quick filter,
  CI the gate. Do not skip the local one to save time; a CI round costs more.
- `reviews.py verify` in CI re-derives every carry; a carry written by hand fails there, so never write one.
- `reviews.py check-report <id> [--lang L] [--exercises]` (and `verify`) rejects a report with a free-form `SCOPE:` line or, in a translation, the Finnish source's hash; run it before accepting a reviewer's report (work queue 0c).
