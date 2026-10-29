VERDICT: FAIL
CONTENT-HASH: 224a5aaa95e7a082

## Blocking
- exercises.json fy4-4-L1-04 — B (round-2 finding, still open): "vedetään vaakasuoralla lattialla $38\,\text{N}$:n voimalla" says the floor is horizontal but not the pull; the answer 1,5 m/s², the solution's "Annettu: … vaakasuoraan" and its force diagram need a horizontal pull (a slanted one changes both the horizontal component and N, hence friction) — write "vedetään vaakasuoralla lattialla vaakasuoralla narulla $38\,\text{N}$:n voimalla" or "… vaakasuoraan suuntaan $38\,\text{N}$:n voimalla".

## Polish
- solutions.md fy4-4-L2-02 — one clause "kun vastapainoa ja kitkaa ei oteta huomioon" would make the lift model explicit (C as it stands).

## Checked
- Round-2 polish fixed: L1-04 solution now says "Vetävä voima $\overline{F}$" (no rope the task lacks); symbol, equation and answer unchanged.
- All 12 answers recomputed with my own formulas: 2,4; 120; 15; 1,5; 78,48; 3000; 7479; 1297; 0,50; 0,981 (down); 20; 6,67 — equal to exercises.json and answers.py.
- Rounded answers (78, 7500, 1300, 0,98, 6,7) inside the 2 % tolerance.
- Signs and directions: L2-02 positive down, T = m(g − a); L2-03 slowing downward → a up, T = m(g + a); L3-01 N < G → a down; L3-03 only friction horizontal.
- Force solutions: object, forces with their causes, positive direction, rectangle diagram before the equation; v and a never drawn as forces; symbolic first.
- Conversions (90 km/h, 36 km/h, t → kg) and significant figures justified by the limiting datum; reasonableness checks are real.
- Hash identical at start and end.
