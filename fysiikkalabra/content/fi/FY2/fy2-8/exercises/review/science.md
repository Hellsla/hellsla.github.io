VERDICT: PASS
CONTENT-HASH: 5059516b77ef58a8

## Blocking

## Polish
- exercises.json:94 (L1-07) — the correct option alone starts with "Esimerkkiväite:", which gives the answer away. Drop the prefix and mark the invented statements in the stem instead, or use a real FMI normal with its source. Rovaniemi's January normal for 1991–2020 is closer to −11 … −12 °C than to −10 °C.
- exercises.json:57 (L1-06, option 1 feedback) — "Kasvihuonekaasut vaikuttavat vasta maanpinnan lähettämään lämpösäteilyyn" is too absolute, because water vapour and CO₂ also absorb part of the incoming solar infrared. Use "ennen kaikkea", which matches the lesson's "suurelta osin läpi".
- exercises.json:149 and :292 (L2-05, L3-04) — the data are labelled "esimerkkiaineisto, pyöristetty Mauna Loan …". The FY2 data rule asks for real values with a named source and year (NOAA GML, Mauna Loa annual means, retrieved year). Verify the cells against the current NOAA file (2005 and 2015 may differ by about 0,2 ppm) and drop "esimerkkiaineisto". solutions.md:146 speaks of a "piirretty pistejoukko" that the task never shows. Either ask the student to draw it, or say "taulukon pisteet".
- exercises.json:331 (L3-05) — "oppitunnin elinkaaren päästökertoimilla": the lesson gives 11–12 g/kWh for wind. Name 12 g/kWh in the task (the answer is 62 % with either value). Part c) needs CO₂ sinks and residence time, which the brief's lesson does not teach. One given sentence in the task ("luonnon nielut sitovat vain osan päästöistä") would make the task fair.
- docs/exercise-bank/FY2.md:50 — the plan's temperature-anomaly graph task (trend vs. year-to-year variation) and the real Finnish sector data are missing: L2-06 uses an invented country. Record this or add them later. In exercises.json:253 (L2-07), the correct option gives 1,64 kg from 2,0 kWh. Write 1,6 kg, as the model answer does.

## Checked
- Recomputed all 5 new numeric answers in one script: L1-08 480 kg, L2-05 2,225 ppm/a, L2-06 26,2 %, L3-04 458,7 ppm, L3-05 61,9 %. All agree within tolerance, and answers.py matches.
- Every Järkevyys and Johtopäätös number is true: 820/12 ≈ 68; 2,0 and 2,7 ppm/a on the end intervals; rates 1,1/1,5/2,2 ppm/a; whole-data forecast 446,6 ppm, 12 ppm lower; 44,5/21,9 ≈ 2,0; 12 of the 16 Mt = 75 %; coal causes 63 % of the emissions from 40 % of the energy.
- L3-04 c) addresses the extrapolation range and the accelerating growth, as the guardrail requires.
- L3-05 c) physics is right: concentration is a stock and grows while emissions exceed sinks.
- L1-06, L1-07, L2-07: exactly one correct option each, every distractor is wrong, and every feedback is right. The climate definition (30 years) is correct.
- Scope: m = e·E, linear models and percentages only, nothing from FY3. Notation (m, e, E) matches the lesson.
- The hash was unchanged at the end.
