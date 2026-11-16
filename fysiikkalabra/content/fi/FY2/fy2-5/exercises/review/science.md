VERDICT: FAIL
CONTENT-HASH: 9a3a2d43c4c1b265

## Blocking
- exercises.json:428 (fy2-5-L3-05 data, row "Öljykattila") vs solutions.md:201–215 — A: the task's table still gives oil H = 43 MJ/kg, but the solution's Annettu says "taulukosta … öljy H = 40,6 MJ/kg" and computes m_öljy = 985 kg → 990 kg and d) 40,6 : 15 = 2,7. A student using the given 43 gets 930 kg and 2,9, and the model solution contradicts the task data. — fix: change the table row to 40,6 (MAFY, kevyt polttoöljy) as in L3-01 and L3-04, or restore 43 / 930 kg / 2,9 in the solution. The box answer (b, 940 kg) is unaffected.

## Polish
- exercises.json fy2-5-L3-01 and L3-04 text — "$40,6\,…$" is written with a bare comma, which LaTeX sets as "40, 6"; write `40{,}6` as everywhere else.
- solutions.md L3-04 — "massana noin 2,5 kertaa": 3313 : 1310 = 2,53, right; the old ratio 2,7 no longer appears. Fine.
- Earlier items outside this delta (L2-08 104 MJ figures, L1-06 distractor, L2-09 axis wording) are still open.

## Checked
- Delta review: hash 9a3a2d43c4c1b265 at the start and the end; I judged the oil value change in L3-01, L3-04, L3-05 and the L2-08 wording.
- 40,6 MJ/kg is MAFY's light fuel oil (docs/mafy-arvot.tsv, VERIFIED).
- L3-01 recomputed: 120 : 15 = 8,0 kg, 120 : 40,6 = 2,96 kg, Δm = 5,04 → 5,0 kg; answers.py 5,044, exercises.json 5,0 (0,02). Ratio 40,6 : 15 = 2,71, checks right.
- L3-04 recomputed: 47 880 : 0,90 : 40,6 = 1310 kg → 1300 kg; 40,6 : 17 = 2,39; 2,39 · 0,90/0,85 = 2,53; box answer 3313 → 3300 kg unchanged.
- L3-05 recomputed: wood 3429, pellets 2491, Δm = 937 → 940 kg (answers.py 937,2); oil 36 000 : (0,90 · 40,6) = 985 kg (but see Blocking).
- L2-08: "bensiinissä on yli 40 MJ kilogrammaa kohti" is right for 43 MJ/kg.
