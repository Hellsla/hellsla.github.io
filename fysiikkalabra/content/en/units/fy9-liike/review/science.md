VERDICT: PASS
CONTENT-HASH: ade08f40cf7c7bfe
SCOPE: full review of unit fy9-liike (en): unit.md, inquiry.json, teacher.md, Sovella s1-s8, answers.py; the three new ```pysahdy boxes judged first against the Finnish unit (fi PASS, hash 67b2709b5b162498).

## Blocking
- (none)

## Polish
- Kartta figure (from before this change, the same in fi): "distance from the velocity graph → under the graph: area". The text and pysahdy box 3 say the signed area is the *displacement*, with the part below the axis counted negative. Distance is the area with every part counted positive. Writing "displacement" in the figure, or "distance: areas counted positive", would remove the apparent contradiction. (Also noted in the fi report.)
- Pysahdy 3: "reduces the displacement" is right. Adding "but increases the distance" would tie it to the Key idea's displacement/distance distinction. Optional, as in fi.

## Checked
1. Pysahdy boxes, against fi unit.md lines 15-19, 118-122, 128-132: the physics is the same in all three. (1) The slope of (t,x) is the velocity and the area under (t,v) is the displacement, which agrees with the Key idea and the "Slope and area" text. (2) Velocity positive and acceleration negative means the speed decreases because the two are opposite, which agrees with the formula text and the Common mistakes item. (3) Area below the axis is negative and reduces the displacement, which agrees with the text. Each box sits right after the paragraph it asks about. No guardrail break; no A or B finding.
2. Diff since the passed version (15ee3d8e9b8696db): the hero SVG became a WebP image (no physics, no labels); the inquiry explain model answer was split into three paragraphs with the same words and numbers. Nothing else changed in tasks.json, solutions.md or answers.py.
3. Definitions and models in unit.md: position, displacement, velocity, acceleration and distance; the average-velocity and average-acceleration formulas with MAFY names; uniform acceleration stated as the condition of v = v0 + at and of the x(t) formula; free fall with "air resistance small"; the derivation in the johda box goes symbolic to the end and agrees with the trapezium area; meeting x_A = x_B; greatest distance at equal velocities, with its condition stated; a = 2A from the fit.
4. Quantitative: one script recomputed every answer from the task data with my own formulas and matched answers.py and tasks.json: s1 12.0 s, 1.25 m/s², 17.5 m; s2 8.84 m, 0.625 s, 7.08 m, vA 5.87 and vB -6.13 m/s; s3 -0.645 m/s², 481 m; s4 81.8 km/h; s5 0.9375 m/s²; s6 8.88, 0.10, 9.77 m/s²; s7 3.0, -2.0 m/s, 2.67 s and 8.0 s, 0.40 m/s; s8 ±2.0 m/s, 4.0 s, 12.0 m, 5.33 s, 14.7 m. `practice.py check`: OK for fi, en and fi-easy (8 tasks, 124 points).
5. Hash ade08f40cf7c7bfe at the start and at the end.
