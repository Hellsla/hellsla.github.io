VERDICT: PASS
CONTENT-HASH: b0961359725131ff
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: s7 b, Järkevyys: the 1 % difference between 8,77 m/s^2 and 8,69 m/s^2 comes from the rounded period and from the chosen model altitude together (the period that fits 400 km is 92,4 min); "kiertoaika ja korkeus on pyöristetty" would be complete.
- A: s7 e: the shadow geometry (sin θ = R/r, cylinder shadow, Sun in the orbital plane) goes beyond what the part asks; it is rightly absent from the rubric, a word such as "lisätieto" would tell the student so.

## Checked
- Item 18 hunks: s1 d, "lähtökitka eli täysin kehittynyt lepokitka pienenisi" carries P8 and the physics holds (smaller normal force on the rear wheels, smaller maximum static friction); 30 kg · 1,40 m / 3,25 m = 12,9 kg. s3 a, "Pisteet ovat laskevalla käyrällä. Käyrä loivenee, kun kierrosaika kasvaa": right for F proportional to 1/T^2 (the old "kaartuu alaspäin" was not).
- s7 recomputed with own formulas: r = 6771 km, T = 5520 s, v = 7707 m/s = 27 750 km/h; sqrt(γM/r) = 7,67 km/s; altitude range 90 km = 1,3 % of r; a_n = 8,773 m/s^2 = 89,4 % of g; γM/r^2 = 8,69 m/s^2, difference 0,9 %; P = 735 000 kWh / 8760 h = 83,90 kW (83,67 kW with 366 d), 42 kettles; 15,65 orbits a day; θ = 70,2°, shadow 39,0 % = 35,9 min; 84 kW / 0,61 = 138 kW. All agree with tasks.json, the solution and answers.py.
- s7 physics: r = R + h, a_n = 4π^2 r/T^2 in symbols, gravity as the only force and the source of the normal acceleration, weightlessness as N = 0 from G − N = m a_n (not absence of gravity, no centrifugal force), mean power hides the variation. Symbols G and N are MAFY. Points 4+3+3+3+2 = 15.
- `python scripts/practice.py check units/fy9-ympyraliike`: OK (7 tasks, 110 points). Hash equal at start and end.
