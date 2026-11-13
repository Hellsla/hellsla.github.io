# Quality assurance: who checks what

A map, not new rules (teacher 2026-11-13). The rules are in `CLAUDE.md` (this folder's), `NOTES.md`,
`EDITORIAL_QUALITY_STANDARD.md` and `physics-guardrails.md`; the checks are in `.github/workflows/fysiikkalabra-ci.yml`
(each step's name says what it checks). Read this to find the right gate, and add a row when a gate is added.

## The gates, in the order a change meets them
| Gate | Who | Covers | Does not cover |
|---|---|---|---|
| 1. Deterministic checks | `python scripts/check_lesson.py <id>` (developer, before any review) | lint, complete solutions, notation, LaTeX, answers, build, simulation and inquiry tests, layout at 360 px | anything a script cannot judge |
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

## Known gaps (2026-11-13)
1. **Browser checks are scoped.** A pull request tests the pages it can change, `main` the pages its push can change
   against the previous `main`; the two can differ. A page can be broken without any run testing it until the weekly
   run (Sunday 21:00). After a merge, look at the run on `main`.
2. **Local runs differ from CI.** CI runs the browser checks in `mcr.microsoft.com/playwright/python:v1.65.0-noble`; a
   session's Chromium is another build, so a layout failure in CI may not reproduce locally (en/fy1-1, 2026-11-13).
   Roadmap step 5.
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
- Layout is checked by `check_lesson.py` (360 px) and again by CI (eight widths): the local check is the quick filter,
  CI the gate. Do not skip the local one to save time; a CI round costs more.
- `reviews.py verify` in CI re-derives every carry; a carry written by hand fails there, so never write one.
