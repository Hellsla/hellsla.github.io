VERDICT: PASS
CONTENT-HASH: f6445c788e2b7dfa
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- B: s7 e: "varjon reuna on kulmassa θ" does not say from where the angle is measured; add "Maan keskipisteestä katsottuna Auringosta poispäin osoittavasta suunnasta".
- A: s7 e: the 39 % is the largest shadow share (Sun in the orbital plane, cylindrical shadow); the text says the condition, and "enintään noin 39 %" in the sentence with 140 kW would keep it visible.

## Checked
- Item 18 hunk (s3 a): F against T follows 1/T^2, a falling curve that flattens as T grows; "laskevalle käyrälle" is right and the fourfold force at half the period agrees.
- s7 recomputed in one script: r = 6771 km, T = 5520 s, v = 7707 m/s = 27 746 km/h; 90 km / 6771 km = 1,3 %; sqrt(γM/r) = 7,67 km/s; a_n = 8,773 m/s^2 = 89,4 % of g; γM/r^2 = 8,69 m/s^2 (0,9 % lower, explained correctly by the two-figure period); P = 83,90 kW (366 d: 83,67 kW); 42 kettles; 15,65 orbits a day; θ = 70,2°, shadow 39,0 % = 35,9 min; 84 kW / 0,61 = 138 ≈ 140 kW. All agree with tasks.json answers, solutions.md and answers.py; `practice.py check` OK (7 tasks, 110 points; s7 4+3+3+3+2).
- Physics of c: gravity is the only force and gives a_n; N = 0 because gravity gives station and astronaut the same acceleration; weightlessness = no support force; the centrifugal-force error is named and refuted correctly. Symbolic solution first in a, b and d; rounding reasons given.
