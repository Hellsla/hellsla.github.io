VERDICT: PASS
CONTENT-HASH: f5f87a72cec845ae
Round: 3

Round 2 had no Blocking items. The round-2 Polish on L3-05 b) is fixed: the tolerance is now 0.01, and b) says "Käytä a)-kohdan pyöristämättömiä massoja". Nothing else changed (`git diff HEAD~1`).

## Blocking

## Polish
- content/fi/FY2/fy2-5/exercises/exercises.json:60 (L1-06, second distractor) — "riippumatta määrästä" makes no sense in the sentence (carried over). Drop the phrase.
- L3-04 and L3-05 — both still follow the same chain (m = E/(ηH), then η falls), and the plan's level 3 asks for "polttoainemäärä ja päästöt" (carried over). Add an emissions part (factor × fuel energy) to one of them when the set is next edited.

## Checked
- L3-05 recomputed: wood 3428,6 kg, pellets 2491,3 kg, difference 937,2 kg. That is 0,3 % from 940, inside 0,01. The 3-figure a) values (3430 − 2490 = 940) also pass. The 2-figure values (3400 − 2500 = 900, −4,3 %) fail, as they should now that b) says to use unrounded masses.
- L3-05 solution: the Sijoitus difference 3429 − 2491 = 938 kg, the Vastaus 940 kg and answer 940 agree. The b) instruction does not conflict with the 2-figure rounding in the a) Vastaus.
- L3-05 c), d) and Järkevyys are unchanged and still correct: 2824 kg, +330 kg, 1,13 = 0,85 : 0,75, and 43 : 15 = 2,9.
- Round-2 checks still stand for the unchanged tasks (L1-07 15,0 kg; L1-08 40,0 kWh; L2-05 5,63 kg; L2-07 18,4 kW; L3-04 3313 kg). Each MC has exactly one correct option, and no solution names an option by its position.
- FY2 scope: no c·m·ΔT, and one efficiency per chain.
