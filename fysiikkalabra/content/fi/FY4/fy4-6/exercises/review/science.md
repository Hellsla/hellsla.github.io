VERDICT: PASS
CONTENT-HASH: 9c86d3f377cf47f7

## Blocking

## Polish
- solutions.md L1-03 *Järkevyys*: "tavallinen arvo puulle lattiaa vasten". The task does not name the box's material. Say "tavallinen arvo laatikolle lattiaa vasten".
- solutions.md L1-01 *Voimakuvio*: it draws N equal to G, assuming the astronaut stands at rest on the surface, which the task does not say. Draw G only, or state the assumption (C).
- L2-01: the unrounded answer 0,134 is 3,4 % from 0,13 against a 4 % tolerance. It is inside, but the margin is thin.

## Checked
- All 12 answers were recomputed independently in one script and compared with exercises.json: 259,2 N; 35,3 N; 0,306; 7,37 N; 58,9 N; 0,134; 0,807 m/s²; 0,214 (the points match the *mittaus* figure, least-squares 0,2145); 8,05 N; 0,357; 0,795 m; 0,330 m/s². Each lies within its tolerance.
- Models are chosen correctly: kinetic vs static friction; L2-04 compares $\mu_0 N$ with $G_x$ and confirms it with tan 35° > 0,60; L3-01 friction points forward and $\mu_0 \ge a/g$; L3-02 has both $G_x$ and friction down the slope while moving up, and states the $\mu_0 \ge \tan 20^\circ$ condition for staying put; L3-03 has the same μ on the Moon, so $a$ scales with g.
- Every solution has a diagram described in words, solves symbolically first, has rounding justified by the limiting datum, and ends with a real reasonableness check. The signs agree with the stated axes.
- L2-03 now calls the data example data in both the task and the figure, and reads the slope from a fitted line through the origin.
- Notation uses \overline and \cdot. Scope fits FY4.
