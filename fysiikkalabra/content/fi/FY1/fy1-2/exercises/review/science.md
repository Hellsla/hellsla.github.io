VERDICT: FAIL
CONTENT-HASH: b6a2f4899768c96b

## Blocking
- content/fi/FY1/fy1-2/exercises/solutions.md:54 (L1-06, A) — "Perusyksikön tunnistaa siitä, ettei sitä ole määritelty toisten yksiköiden avulla" is false in the current SI: the metre is defined through the second, and the kilogram (the correct option) through the metre and the second. — Fix: "Perusyksiköt on sovittu järjestelmän perustaksi; johdetut yksiköt ilmaistaan perusyksiköiden tuloina ja osamäärinä (esim. N = kg·m/s²)."
- content/fi/FY1/fy1-2/exercises/exercises.json:66 and solutions.md:54 (L1-06, A) — "Gramma on kilogrammasta johdettu yksikkö" and "johdetaan … tai etuliitteellä" give *johdettu yksikkö* a meaning the glossary (m/s, N) and the SI do not: a gram is a decimal submultiple (prefix + gram), not a derived unit. — Fix: "Gramma on kilogramman tuhannesosa, etuliitteellä muodostettu yksikkö, …", and drop "tai etuliitteellä" from the definition of derived units.

## Polish
- content/fi/FY1/fy1-2/exercises/exercises.json:180–185 (L2-05) — a cyclist at 14,0 m/s (50 km/h) and a fishing boat at 21,0 knots (39 km/h) are unrealistic as typical values, and the solution (line 120) passes over the 50 km/h. Something like 8,0 m/s and 10,0 knots keeps the same order and answer.
- content/fi/FY1/fy1-2/exercises/exercises.json:291 (L3-05) — answer 1.5, while answers.py gives 1,536 → 1,54; a student who enters 1,54 is 2,7 % off. Store 1.54 (the field value) as the other tasks do (9.33, 4.23) and keep "1,5 h" as the shown answer.

## Checked
- Recomputed all 18 numeric answers in one script: all agree (e.g. L2-05 19,549 m/s; L3-05 7,647 h − 6,111 h = 1,536 h).
- L1-08: exactly one correct option, and each distractor's feedback is right.
- L1-06: exactly one correct option (kg). The litre is correctly called a non-SI unit accepted for use with the SI.
- L2-05: the knot (1,852 km/h) is exact; the order follows from the table.
- L2-06: the error is unique (head says kg, values are grams); apples of about 155 g are realistic; four figures follow from the 0,1 g readings.
- L2-07: the unit check l²/s exposes t = qV; V = qt is right.
- L3-04: dimensional analysis c = 0, b = −½, a = ½ is right; T ∝ √L is consistent with a real pendulum (2π√(0,25/9,81) = 1,00 s).
- L3-05: the conversions kWh → J and kW → W are right; the claim's error (comparing numbers in different units) is identified; two figures follow from 0,65 kWh.
- Old 12: unchanged apart from the typography.
