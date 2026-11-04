VERDICT: FAIL
CONTENT-HASH: 50aa496a1262650f

## Blocking
- exercises/solutions.md:175 and :178 (fy6-11-L3-04, Periaate and b) — (A) wrong inference. "pienin varaus on yksi tai useampi alkeisvaraus ja muut ovat sen kokonaislukukertoja" is false (2e and 3e are not multiples of 2e). b) then sets n = 1 for drop 3 with no reason given, and that choice is the whole point of the Millikan logic. — Fix: Periaate: "Kaikki varaukset ovat saman askeleen kokonaislukukertoja. Pienimmän varauksen oletetaan olevan yksi askel, jos muiden suhteet siihen ovat kokonaislukuja." In b), after the ratios 2,0; 3,0; 4,0; 3,0, add: "Suhteet ovat kokonaislukuja, joten pisaran 3 varaus on yksi alkeisvaraus (n = 1). c-kohdan kirjallisuusarvo tukee valintaa."

## Polish
- solutions.md:179 (L3-04 c) — "alle 0,2 %" overstates the precision: the masses have two significant figures (about ±1,3 %). Say "alle 1 %, mittaustarkkuuden rajoissa".
- solutions.md:179 (L3-04 d) — "myös kevyemmät ... hiukkaset kerääntyvät": light particles are collected anyway. Write "raskaammat ja vähemmän varautuneet".
- exercises.json:239,243 (L2-07) — the example data drop 13,5 % one plate gap inside the edge (x = 8 cm). For wide plates it is only a few per cent weaker there. About 58 µN would be realistic. Optional.
- docs/exercise-bank/FY6.md fy6-11 Taso 2 — the plan's graph task (droplet deflection, figure) became the error-analysis task L2-06, and no new task has a graph. Update the plan line.

## Checked
- Hash 50aa496a1262650f at start and end. All 8 new answers recomputed independently in one script: 7,5 mm; 400,1 V; 0,12 mN; 2,98e4 V/m; 1,6017e-19 C; 1,667 mm. All agree with answers.py and exercises.json.
- L1-06, L1-07: exactly one correct option, and the feedback is right.
- L2-05: E·d = 408, 393, 408, 390, 408, 393,6 V, with no trend, so the product is U.
- L2-06: the error (ball's distance used instead of the plate gap) is right.
- L2-07: deviations 0,7 / 1,2 / 2,0 / 13,5 / 45,2 %. The four-point mean matches U : d to within 0,6 %.
- L3-04: q = mgd : U per drop (3,20; 4,84; 1,59; 6,38; 4,83 e-19 C), sign negative (positive plate on top), check on drop 3 right.
- L3-05: F : G = 1360, so gravity can be neglected. t = 0,5 ms. Doubled voltage: hits the plate at 8,7 mm < 10 mm.
- New tasks are inside the scope (uniform field, E = U : d, F = qE, FY4 kinematics). No duplicates. Levels fit.
