VERDICT: PASS
CONTENT-HASH: c062ee293a88ae2f

Round 1 (new task fy7-8-L2-08, order of magnitude; rest of set PASS before)

## Blocking
(none)

## Polish
- exercises.json:237 — options are 0,1 kW, 10 kW, 10 MW, 1000 MW: gaps of 100, 1000, 100. The task says values a factor 10-100 apart; use a spacing of 10-100 throughout, e.g. 0,1 kW, 10 kW, 1 MW, 100 MW, and re-check that each feedback still matches its value.
- exercises.json (feedback of 10 MW) — "mikä on mahdotonta" is right only for 10 MW (above 3,0 MW); the 1000 MW option is also impossible but its feedback does not say it. One sentence "Tämä olisi myös moninkertaisesti voimalan tehoa suurempi" helps.
- exercises.json:237 — the answer says "noin 10 kW" while the calculation gives 11 kW; fine, but add "Pyöristä suuruusluokkaan" to the stem so students do not look for 11 kW.

## Checked
- Recomputed: I = 150 A, P_h = 11,25 kW; wrong options 75 V read as watts (0,1 kW), I = 4350 A at 690 V giving 9,5 MW, U squared over R = 800 MW.
- Distractors catch the chapter's warned mistake (P = U^2 : R, option 4) and the lesson's "voltage drop is R I" idea (option 1).
- Correct option not identifiable by form: options ascending, answer is second; not the only one with the unit kW.
- Within chapter: P = U I, P_h = R I^2 and ideal transformer only. Situation first, question last as own sentence.
- Solution step by step with sanity check.
- Checked from text only (no renders; pedagogy role); inline formulas measured as KaTeX renders at 390 px: I 122 px, P_h 174 px, fit.
