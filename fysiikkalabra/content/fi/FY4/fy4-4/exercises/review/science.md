VERDICT: FAIL
CONTENT-HASH: afe7f0a40e2cab00

## Blocking
- exercises.json fy4-4-L1-04 — B: the round-2 edit removed the duplicated "vaakasuoralla" and with it the only statement that the 38 N pull is horizontal; "vedetään vaakasuoralla lattialla 38 N:n voimalla" no longer fixes the pull's direction, yet the answer 1,5 m/s² and the solution's "Annettu: … vaakasuoraan" and force diagram need it (a slanted pull changes the horizontal component) — write "vedetään vaakasuoralla lattialla vaakasuoraan suuntaan 38 N:n voimalla" (or "vaakasuoralla narulla").

## Polish
- solutions.md fy4-4-L1-04 — "Narun jännitysvoima $\overline{F}$": the task names no rope, and the lesson writes tension as $\overline{T}$; say "vetävä voima $\overline{F}$" or put a rope in the task.
- solutions.md fy4-4-L2-02 — one clause "kun vastapainoa ja kitkaa ei oteta huomioon" would make the lift model explicit (C as it stands).

## Checked
- All 12 answers recomputed with my own formulas: 2,4; 120; 15; 1,5; 78,48; 3000; 7479; 1297; 0,50; 0,981 (down); 20; 6,67 — equal to exercises.json and answers.py.
- Rounded answers (78, 7500, 1300, 0,98, 6,7) stay inside the 2 % tolerance.
- Signs and directions: L2-02 positive down, T = m(g − a); L2-03 slowing downward → a up, T = m(g + a); L3-01 N < G → a down; L3-03 only friction horizontal.
- Force solutions name the object, forces with causes, positive direction, rectangle diagram (G from centre, N from the contact face, friction from the bottom edge, v and a beside, never as forces) before the equation; symbolic first.
- Conversions (90 km/h, 36 km/h, t → kg) and significant figures justified by the limiting datum; reasonableness checks are real checks.
- Notation: \overline{} vectors, \cdot, all symbols in LaTeX.
- Hash identical at start and end.
