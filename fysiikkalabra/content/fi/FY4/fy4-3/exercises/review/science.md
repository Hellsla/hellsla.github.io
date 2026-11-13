VERDICT: PASS
CONTENT-HASH: f51ce1c022766434

## Blocking

## Polish
- content/fi/FY4/fy4-3/exercises/exercises.json (L2-09) — a student who measures between the first and last points that are not zero (0,06 s → 0,14 s) gets 0,08 s, which is 20 % off and is rejected at tolerance 0,1. A clause such as "lue hetket, joilla lukema lähtee nollasta ja palaa nollaan" would rule that reading out. The solution already reads it this way.
- content/fi/FY4/fy4-3/exercises/exercises.json (L2-08) — the text still opens with "Esimerkkiarvot:". Other sets dropped that prefix.
- content/fi/FY4/fy4-3/exercises/solutions.md (L3-05 c) — "kärry vetää köyttä ja oppilasta": the cart pulls the rope, and the massless rope pulls the student. C, so optional.

## Checked
- Figure fy4-3/anturit: I reran collision_data(). At t = 0,10 s the readings are F_A = −4,02 N and F_B = +3,94 N. Contact starts at T0 = 0,05 s and ends at T1 = 0,15 s, both on grid lines, with ±4 N grid lines. L1-09 reads 4,0 N, which is 1,5 % from 3,94 N and inside 4 %. L2-09 reads 0,15 s − 0,05 s = 0,10 s. Both tasks can be read from the figure. The description gives the same information without the answers.
- Sign and object in L1-09: the force of A on B is sensor B's reading, positive to the right. A, on the left, pushes B to the right. Consistent with $\overline{F}_{AB} = -\overline{F}_{BA}$.
- The two figure tasks do not repeat each other (one asks a force, the other a duration) or any other task in the set. Notation (F_A, F_B, F_{AB}) is the chapter's.
- Recomputed all 19 numeric answers in one script (my formulas beside python -I answers.py). All agree within tolerance: for example L1-05 6,377 → 6,4 N, L2-03 833,9 → 830 N, L2-04 8,939 → 8,9 kN, L3-04 450/480 N, L3-05 3,40 N.
- MC tasks L1-06, L1-07, L2-07 and L2-08 (with its reason): each has exactly one correct option, and every distractor's feedback says why it is wrong.
- First law used only where the velocity is constant. Third-law pairs are always on different bodies and of the same kind. Weight and normal force are never called a pair. The guardrails hold.
- Force-diagram blocks: forces agree with the motion, velocity is drawn apart from the forces, and the third-law partner is left out of the body's own diagram (L1-03, L1-05).
- Hash f51ce1c022766434 at the start and at the end.
