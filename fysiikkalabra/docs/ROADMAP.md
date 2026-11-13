# Ruukkilabra: roadmap

The order of work the teacher approved on 2026-11-13. What each item means in detail is in `docs/tyojono.md` (the
queue) and in the course plans (`FY9_PLAN.md`, `FY10_PLAN.md`, `FY14_PLAN.md`, `DRONELABRA_PLAN.md`,
`PORTAL_ARCHITECTURE.md`). This file only orders them and says what may run at the same time; how sessions share the
work is in `CLAUDE.md` at the repository root. Update it when the teacher changes the order.

## Areas
| Area | Covers | Tools |
|---|---|---|
| A. Physics content and pedagogy | lessons, exercises, Sovella itsenäisesti, example exams, MAFY notation | `/lesson`, `/exercises`, `/practice`, `/exam`; developer, science-reviewer, pedagogy-reviewer |
| B. Site, simulations, UI/UX | `scripts/`, `templates/`, `site/site.css`, simulations, CI | developer; shared files, so one change at a time |
| C. Figures and visual consistency | SVG figures, illustration audit, first visual reviews | `/figure-fixes`, `/quality-audit`; visual-editorial-reviewer; teacher approves figures |
| D. Ahjo Makerspace and new courses | `jaksot/ahjo/` (Ahjo 1–2, Dronelabra), FY9, FY10, FY14, Kilparobotiikka, LUMA-tutor | `/new-course`, the plans above; nothing is built before the teacher approves the plan |

## State on 2026-11-13
- Every FY1–FY8 lesson is reviewed. Exercise sets reviewed: FY2, FY3, FY4 (except fy4-8), FY8.
- 51 exercise sets wait for their reviews and are not shown to students: FY1 (8), fy4-8 (1), FY5 (13), FY6 (15),
  FY7 (14), each in fi, en and fi-easy (`python scripts/reviews.py status`).
- 36 published parts wait for their first visual review: the 27 FY10 investigations and 9 TVT guides
  (`python scripts/reviews.py baseline`).
- `main` was red after #528 (`test_writepad.py`, en/fy1-1 at 360 px), green again after #534.

## Order
1. ~~`main` green (en/fy1-1 editor at 360 px)~~: done (#534, 2026-11-13; the failure did not recur, the test now names an overflowing element if it does).
2. Exercise reviews, in course order: FY1, fy4-8, FY5, FY6, FY7. The course's MAFY formulas (queue) go in the same
   session or right after, never in parallel on the same course.
3. MAFY formulas for the courses step 2 does not cover: FY8, FY10, FY14.
4. Fixes to the FY10 investigations and TVT guides after the audit (#536): the eight Major findings first, fy10-liukukitka
   with a science review; Minor findings in a later batch.
5. CI tooling: a way to run the browser checks in CI's container image locally, and failure messages that name the
   overflowing element. Shared files: alone, merged first.
6. Picture and MAFY-table tasks for FY8, FY9, FY10 and FY14 (queue). They add review work, so they start when step 2
   is done.
7. Desktop layout: a centred text column and a margin column. The largest structural UI change left; shared files,
   so alone, after an assessment with comparison captures for the teacher.
8. Misconception as its own component in Teoria: the component once, then content chapter by chapter, each with
   all three reviews.
9. Example exams for FY7 and FY8 (`/exam`). FY8 can start any time; FY7 after its exercise reviews (step 2).
10. English concept cards for FY6 and FY8 (queue: later, the teacher's decision).
11. Ahjo and LUMA-tutor onto the shared unit template (`jaksot.py` blocks, as Kilparobotiikka). Last; shared files,
    so alone.
12. Printed A5 booklets for FY1–FY8 in the current compact layout (`print_book.py --publish`): FY1–FY4 again, FY5–FY8
    new; each course after its MAFY formulas (step 3) are merged.

Area D waits for the teacher's decision on which plan (FY10, Dronelabra, others) is approved for building.

## In parallel
At most three worker sessions, each on a different course or area:
- now, once `main` is green: FY1 exercises, FY5 exercises, FY10 visual audit;
- not with anything else: step 5 and any other change to shared files;
- one after another: two items on the same course.
