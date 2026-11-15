VERDICT: PASS
CONTENT-HASH: 4d73a243c59b4c6d

## Blocking

## Polish
- solutions.md:763 (fy7-15-L2-09 Principle) — "Light reflected from … glass is partly polarised" holds for an oblique view; at perpendicular viewing the reflection is not polarised. The task's observation implies the oblique view, so this is a fair simplification (C) — optionally add "when the window is viewed at an angle".
- solutions.md:764 (fy7-15-L2-09) — light from the goods also crosses the glass obliquely and becomes slightly polarised (Fresnel, n = 1.5: at about 56° the two components pass 73 % and 100 %), which is why the task rightly says "hardly changes"; the model answer could say "almost unpolarised". Not required at this level.
- exercises.json:439 (fy7-15-L3-04) — still says "The data is example data." although the sentence was removed from L2-05 and L2-06 — remove here too for consistency, if the teacher's decision covers it.
- lessons/FY7/fy7-15/answers.py:818 — comment dates the teacher's decision 2026-11-16 — check the date.

## Checked
- All 22 numeric answers recomputed independently from the task texts (Malus, halving, Brewster, Snell for L2-04, least-squares fits for L2-05 and L2-08, maximum search for L3-04): all agree with exercises.json and answers.py.
- L2-09: reflection from an insulator partly polarised parallel to the surface, filter crossed to it absorbs most of it, unpolarised light halved in every position, quarter turn passes the reflection, partial polarisation explains why it does not vanish: correct, qualitative, on the core path (LOPS "polarisaatio kvalitatiivisesti"), consistent with the glossary and with L1-06.
- L2-09 answer field, model answer and answers.py comment say the same thing; no Malus or Brewster needed, so "core": true is right.
- L2-05 without the example-data sentence: fit slope 313.9 lx, intercept 6.9 lx; background subtracted correctly; 322 lx (no subtraction) falls outside the tolerance.
- L2-06 without the sentence: table values scatter around cos² θ within ±0.02; curve reading about 51–52°, inside the 3 % tolerance of 50.8°.
- L3-02 and L2-07: index order for light inside the denser medium right; 36.9° is below the critical angle 48.8°.
- L3-05: Sun's height 36.9°, glare 40 · cos² 65° = 7.14 W/m², threshold tilt 33.2° right.
- Figures graph-task and fit: generators give the values the solutions read (0.67 at 35°; 15 lx and 375 lx); neither gives the answer away.
