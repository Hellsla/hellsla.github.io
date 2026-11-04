VERDICT: PASS
CONTENT-HASH: bebeb9ecaaeaf3c1
Round: 2

Round 1 had no Blocking items. All five round-1 Polish items are addressed:
- L1-08 now justifies its figures by 144 MJ, and answers.py computes `144 / 3.6`.
- The L2-07 data now scatter.
- The L3-05 Järkevyys slip is fixed.
- L3-04 and L3-05 share the boiler values (85 % and 90 %).
- The plan no longer lists the candle task.

The changed tasks are correct.

## Blocking

## Polish
- content/fi/FY2/fy2-5/exercises/exercises.json:355 (L3-05) — the difference of the rounded a) masses (3400 − 2500 = 900 kg) is 4 % off 940, so it fails. Set the tolerance to 0.05, or add "laske pyöristämättömillä massoilla" to b).
- content/fi/FY2/fy2-5/exercises/exercises.json:60 (L1-06, a distractor) — "riippumatta määrästä" makes no sense. Drop it.
- L3-04 and L3-05 (partly carried over) — both still follow the same chain (m = E/(ηH), then η falls). The plan's level 3 asks for "polttoainemäärä ja päästöt", and neither task has emissions. Add an emissions part to one of them in the next round.

## Checked
- Recomputed in one script: L1-07 15,0 kg; L1-08 40,0 kWh; L2-05 5,63 kg; L2-07 18,4 kW; L3-04 3313 kg (oil 1237, η 0,70: +710, ratio 2,68); L3-05 937 kg (wood 3429, pellets 2491, oil 930; η 0,75: 2824, +332). answers.py, json and solutions agree.
- L2-07: the least-squares fit of the new data is m = 11,998 − 0,0650·t. Reading the slope from the line ends (0; 12,00) and (40; 9,40) is therefore valid.
- L3-05 a)–d) and Järkevyys (2120 : 0,85 = 2490; 2824 : 2491 = 1,13 = 0,85 : 0,75) are true.
- L3-04 c): 2,5 · (0,90 : 0,85) = 2,7, and the direction is right.
- MC L1-06 and L2-06 (options reordered): exactly one correct option each, and every feedback matches its option. No solution names an option by its position (the options are shuffled).
- FY2 scope: no c·m·ΔT, and one efficiency per chain.
