VERDICT: PASS
CONTENT-HASH: 7f004187f71ef3f5
Mode: full
Round: 1

## Blocking

## Fixed
- exercises.json fy6-4-L1-07: term explained in place: "ideaaliseen paristoon (sen jännite ei laske, vaikka virta kasvaa)".
- exercises.json fy6-4-L2-05: "yleismittarilla (mittarilla, joka mittaa mm. resistanssia)" and "virheraja eli suurin mittausvirhe" added so the terms are explained.

## Polish

## Checked
- Scripted comparison against content/fi (exercises.json, all 20 exercises incl. the 8 new L1-06..08, L2-05..07, L3-04..05): keys, ids, answers, units, tolerances, correct flags, choices, feedback, data-table cells identical; every number identical in exercises.json and in solutions.md (fi-easy (selkosuomi); decimal point in en JSON/LaTeX where required).
- Answers recomputed: 33 ohm concept, 60, 102.1, 198, 40.4 ohm, 36 mA, 1.32 % (L3-05: 560 || 2700 = 463.8 ohm), all equal to the Finnish.
- check_i18n.py fi-easy: 0 errors for fy6-4 (remaining errors are in fy6-1..3, outside this task).
