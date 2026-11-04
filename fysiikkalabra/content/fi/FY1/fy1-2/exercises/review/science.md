VERDICT: PASS
CONTENT-HASH: 858946470e7d35ed

## Blocking

## Polish
- content/fi/FY1/fy1-2/exercises/solutions.md:175 (L3-04) — "k … ei riipu pituudesta tai paikasta" holds within the task's premise. Strictly, k depends on the amplitude, which the premise leaves out. — Optional: "kun heilahdukset ovat yhtä pieniä".
- content/fi/FY1/fy1-2/exercises/exercises.json:66 and solutions.md:55 (L1-06) — "kilogrammasta etuliitteellä muodostettu osa": the gram itself carries no prefix. — Write: "Gramma on kilogramman tuhannesosa; massan etuliitteet liitetään grammaan (mg, kg)."
- content/fi/FY1/fy1-2/exercises/solutions.md:54 (L1-06) — "Etuliite … muodostaa perusyksikön osan tai monikerran": prefixes apply to every SI unit (kN, MJ). — Write "yksikön osan tai monikerran".

## Checked
- The round-2 Blocking item (L3-04, B) is fixed. solutions.md:179 now says "pienillä heilahduksilla pätee T = 2π√(L/g)", and "tarkka" is gone. This was the only change (`git diff HEAD~1 -- content/fi/FY1`).
- L3-04 recomputed: dimensional analysis gives a = 1/2, b = −1/2, c = 0, and T₂ = 1,00 s·√4 = 2,00 s. The data agree with 2π√(L/g): this gives 1,003 s for 0,250 m and 2,006 s for 1,00 m.
- Everything else is unchanged since round 2. The round-2 checks still apply: L2-05 speeds, L3-05 at 1,536 h, L1-06 options, L2-07 unit check, and answers.py agreeing with exercises.json.
- The hash was the same at the start and the end.
