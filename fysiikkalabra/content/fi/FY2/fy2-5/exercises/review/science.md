VERDICT: PASS
CONTENT-HASH: 5ca23e469a626f1f

## Blocking

## Polish
- Earlier items outside this delta (L2-08 104 MJ figures, L1-06 distractor, L2-09 axis wording) are still open, as recorded in round 1.

## Checked
- Delta review, round 2: hash 5ca23e469a626f1f at the start and the end. I judged the fix for my round-1 Blocking item (L3-05 oil row) and the 40{,}6 notation in L3-01 and L3-04.
- exercises.json:427–428 (L3-05): the row now reads "Öljykattila (kevyt polttoöljy, MAFY-taulukko)", 40.6, 90. The task data and the solution's Annettu (40,6) now agree. The decimal point in the JSON row follows the convention other sets use, e.g. fy1-1 "0.387".
- L3-05 recomputed with my own formula m = E_hyöty/(ηH): wood 3429 kg, pellets 2491 kg, oil 985 kg (written as 990 kg), Δm = 937 kg (written as 940 kg); answers.py gives 937,22, box 940, tolerance 0,01. At η = 0,75: 2824 kg, 332 kg more (written as 330 kg). d) 40,6 : 15 = 2,71 (written as 2,7). The solution matches every value.
- L3-01: 120 : 15 = 8,0 kg, 120 : 40,6 = 2,96 kg, Δm = 5,04 kg (written as 5,0 kg); answers.py 5,044, box 5,0, tolerance 0,02. Text and solution write 40{,}6, and the earlier round's Polish item is fixed.
- L3-04: 13 300 kWh · 3,6 = 47 880 MJ. Pellets 3313 kg (written as 3300 kg, the box answer). Oil 1310 kg (written as 1300 kg). Mass ratio 2,53, heating-value ratio 2,39, and 2,39 · 0,90/0,85 = 2,53. The task text writes 40{,}6 with "MAFY-taulukko".
- 40,6 MJ/kg is MAFY's value for light fuel oil (guardrail P8: a clear contradiction takes MAFY's value). It is now the same in all three oil tasks.
- answers.py comments match the new values (1310 kg, 985 kg).
