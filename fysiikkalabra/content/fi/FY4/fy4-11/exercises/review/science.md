VERDICT: PASS
CONTENT-HASH: 0ecc1231135aa3d4

## Blocking

## Polish
- content/fi/FY4/fy4-11/exercises/solutions.md:252 (L3-05 Vastaus) — "kolme merkitsevää numeroa kuten nopeuden muutoksessa 4,5 m/s": 4,5 m/s has two significant figures (from 10,1 − 5,6, both to 0,1 m/s) — write "18 kN, kaksi merkitsevää numeroa kuten nopeuden muutoksessa 4,5 m/s"; the answer box value 18,0 with tolerance 0,02 is unaffected.
- content/fi/FY4/fy4-11/exercises/solutions.md:125 (L2-05 Vastaus) — "jarrutusmatkat on mitattu kolmen tai neljän numeron tarkkuudella": the data are 6,5 (two) and 14,1/25,9/39,6 (three) — write "kahden tai kolmen numeron tarkkuudella".
- content/fi/FY4/fy4-11/exercises/exercises.json:186 (L2-06) — Δt = 0,200 s from 60 km/h means about 1,7 m of stopping distance, more than crumple zone plus belt travel allow — drop that row or call it a test setting.
- docs/exercise-bank/FY4.md — the planned level-2 crash-test acceleration figure became the L3-05 velocity table; update the plan line.

## Checked
- All 18 numeric answers recomputed in one script with my own formulas and from answers.py: all agree within tolerance.
- L3-04: my least-squares fit of s_p/v on v gives t_r = 1,21 s, a = 5,10 m/s², v_max = 65,9 km/h, s_p(80) = 75 m, impact 52 km/h.
- L2-05: least-squares slope through the origin gives a = 7,85 m/s²; the origin is physically justified.
- L2-06: F·Δt = 1,24–1,27 kN·s in every row, v_0 = 60,0 km/h. L2-07: 12,0 m · 1,8² = 38,9 m.
- L3-05: distance 0,79 m, F_ka = 10,0 kN, peak 18,0 kN (40–60 ms); assumptions stated; (d) right, belt and airbag together.
- L1-06, L1-07: exactly one correct option; distractor feedback right. L1-08: a = μg with conditions stated.
- Scope and notation as in the lesson; level 3 tasks multi-step YO style; no duplicates.
- Hash 0ecc1231135aa3d4 at the start and at the end.
