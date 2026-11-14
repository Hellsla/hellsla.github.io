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
2. ~~Exercise reviews FY1, fy4-8, FY5, FY6, FY7~~: done (#537, #555, #540, #556, #557; 2026-11-14).
3. MAFY formulas for the courses step 2 does not cover: FY8, FY10, FY14.
4. Fixes to the FY10 investigations and TVT guides after the audit (#536): the eight Major findings first, fy10-liukukitka
   with a science review; Minor findings in a later batch.
5. CI tooling: a way to run the browser checks in CI's container image locally, and failure messages that name the
   overflowing element. Shared files: alone, merged first.
6. Picture tasks for FY8, FY9, FY10 and FY14; MAFY-table tasks for FY8 and FY9 only (teacher 2026-11-14) (queue). They add review work, so they start when step 2
   is done.
7. ~~Desktop layout: a centred text column and a margin column~~: dropped (teacher 2026-11-14 chose option B: the
   38 rem column stays and the figure rows are fixed, step 11 U3).
8. Misconception as its own component in Teoria: the component once, then content chapter by chapter, each with
   all three reviews.
9. Example exams for FY7 and FY8 (`/exam`). FY8 can start any time; FY7 after its exercise reviews (step 2).
10. Simulation interface (queue 10, `docs/audits/2026-11-14-simulaatioiden-kayttoliittyma.md`): PR 1–PR 5 in order,
    pilots stop for the teacher's approval. Shared files: alone, one at a time, merged before content.
11. Task view and theory layout (queue 11, teacher 2026-11-14): U4 first, as soon as no other shared change is open;
    then U1, U2, U3, which start only after step 10's PR 1–PR 5 are merged (same `site.css`, `lesson.js`). Shared
    files: alone, one at a time, merged before content. No new interface text without the teacher's permission.
11b. FY9 adaptive exam coach (queue 11b, `docs/FY9_ADAPTIVE_PLAN.md`, teacher approved 2026-11-14): PR 1 (YTL facts)
    any time; the shared PR 2–8 one at a time after step 10's PR 1–PR 5 and step 11's U1.
12. Targeted content corrections in FY3–FY8 (queue 12, teacher 2026-11-14, `docs/audits/2026-11-14-kohdennetut-sisaltokorjaukset.md`):
    thirteen small fixes to reviewed content, delta reviews of the changed passages only, one pull request.
13. English concept cards for FY6 and FY8 (queue: later, the teacher's decision).
14. Ahjo and LUMA-tutor onto the shared unit template (`jaksot.py` blocks, as Kilparobotiikka). Shared files,
    so alone.
15. Editorial final review of FY1–FY8 (queue 15, teacher 2026-11-14): after every other step except the booklets (step 16); a report first, course by course, with verified
    errors, possible problems and optional improvements apart; no source changes until the teacher has read it.
16. Last (teacher 2026-11-14): printed A5 booklets for FY1–FY8 in the current compact layout (`print_book.py --publish`): FY1–FY4 again, FY5–FY8
    new; each course after its MAFY formulas (step 3) are merged.

Area D waits for the teacher's decision on which plan (FY10, Dronelabra, others) is approved for building.

## In parallel
At most three worker sessions, each on a different course or area:
- now, once `main` is green: FY1 exercises, FY5 exercises, FY10 visual audit;
- not with anything else: step 5 and any other change to shared files;
- one after another: two items on the same course.
