VERDICT: FAIL
CONTENT-HASH: d31dfe55c8d54663

## Blocking
- content/fi/FY1/fy1-2/exercises/solutions.md:179 and :175 (L3-04, B; new in this round) — "tarkka kaava on T = 2π√(L/g)" holds only for small swings: the period grows with the amplitude. Line 175's "k … ei riipu pituudesta tai paikasta" is right within the task's premise, but k = 2π likewise needs small swings. — Fix: "pienillä heilahduksilla pätee T = 2π√(L/g)", and drop "tarkka".

## Polish
- content/fi/FY1/fy1-2/exercises/exercises.json:66 and solutions.md:55 (L1-06) — "kilogrammasta etuliitteellä muodostettu osa": the gram itself carries no prefix. It is the kilogram without kilo-, and SI prefixes attach to the gram. — Write: "Gramma on kilogramman tuhannesosa; massan etuliitteet liitetään grammaan (mg, kg)."
- content/fi/FY1/fy1-2/exercises/solutions.md:54 (L1-06) — "Etuliite … muodostaa perusyksikön osan tai monikerran": prefixes apply to every SI unit (kN, MJ), not only to base units. — Write "yksikön osan tai monikerran".

## Checked
- Round-1 Blocking 1 is fixed. The false "not defined through other units" is gone, and base units are now "sovittu", with derived units as products and quotients (N = kg·m/s²).
- Round-1 Blocking 2 is fixed. The gram is no longer called a derived unit, in the feedback or in the model answer.
- L2-05 recomputed with the new data: ship 19,55, train 18,33, cyclist 9,0 and boat 6,17 m/s. The order and the answer 19,5 m/s are right, and both speeds are now realistic.
- L3-05: the stored answer is 1.54 (1,536 h). The added 1 kWh = 3,6 MJ is right.
- L1-06: exactly one option is correct, and each distractor's feedback is right.
- L2-07 rewording: unit check l²/s and t = V/q = 60 s are unchanged.
- answers.py agrees with exercises.json for every numeric task.
- The hash was the same at the start and the end.
