VERDICT: PASS
CONTENT-HASH: a4254015fd08611c
SCOPE: delta added-exercise from 2492493ba54a8626 base 415cbc7c6bc3

## Blocking

## Polish
- content/fi-easy/FY8/fy8-9/exercises/solutions.md:183 — the rounding reason is "noin 30 a", while the task and the Annettu step tell the student to treat 30 a as exact. This is defensible (the computation uses 30 a, but the real half-life is only known as "noin"), but it reads as a contradiction — write "lasketaan arvolla 30 a, mutta todellinen puoliintumisaika on annettu vain likimäärin (noin 30 a), joten kaksi merkitsevää numeroa".

## Checked
- Recomputed: t = 40 a, (1/2)^(40/30) = 0,39685 → 39,7 % → 40 %; answers.py gives 39,685 ✓. Relative tolerance 0,03 accepts 38,8–41,2 %, so both 40 and 39,7 are accepted ✓.
- Model condition stated: the task says the caesium is lost only by decay, so the physical half-life alone applies (no environmental or ecological loss). The reasonableness bounds of 25–50 % are right.
- Source facts against the verified list: Chernobyl 1986 and atmospheric weapons tests in the 1950s–60s; weapons tests before 1986 and mainly Chernobyl after; caesium still in berries, fish, mushrooms and game; decreasing amounts; table 9.2 rows Helsinki 14–413 (12), Tampere 3,5–670 (13), Rovaniemi 76 (2); Tampere in the highest-fallout area — all ✓.
- Part c) is explicitly the solution's own reasoning (rain in spring 1986, soil, mycelium depth), not attributed to STUK ✓. Part d): 670/3,5 = 191 ✓, plus the small sample sizes, species, place and measurement uncertainty.
- Scope: the decay law N = N0(1/2)^(t/T½), as the course scope and the lesson give it.
- Hash a4254015fd08611c at the start and the end.
