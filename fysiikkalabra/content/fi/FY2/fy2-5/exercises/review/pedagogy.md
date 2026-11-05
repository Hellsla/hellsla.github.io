VERDICT: PASS
CONTENT-HASH: f28649f7c45795b2
Round: 1

## Blocking
- none

## Polish
- solutions.md fy2-5-L2-08 (sanity line) — "bensiini on lähes $40\,\text{MJ}$ kilogrammaa kohti mutta vain pieni määrä" is wrong (43 is over 40) and the sentence is clumsy. Fix: "bensiinin lämpöarvo on suurin, yli $40\,\text{MJ/kg}$, mutta sen massa on pienin, joten sen energia jää pienimmäksi."
- exercises.json fy2-5-L2-08 text — "Laske ... ja järjestä polttoaineet." duplicates the `prompt`; keep the last sentence as the question only, e.g. end the text at the data and let the prompt ask the order.
- exercises.json fy2-5-L3-04/L3-05 and L1-06 (carried over) — L3-05 repeats the L3-04 idea (swap one for cost or emissions per energy); L1-06 correct option is the shortest, lengthen it.
- docs/exercise-bank/FY2.md (carried over) — note the CO2 table is realised in fy2-8, not fy2-5.

## Checked
- New L2-08 (ordering): 64,5 / 75 / 104 / 120 MJ is the correct order; it differs from the mass order (bensiini, hiili, puu, turve), so ordering by mass or by H fails; the g and t conversions are the one lesson-prepared trap (L2-06 teaches t).
- Level 2 fits: four E = Hm products with unit conversion, no hidden new idea; not a copy of the worked example (wood, 6 kg).
- Solution has principle, conversion, four substitutions, order, comparison with the mass order; followable.
- Rest of the set unchanged since the PASS (8/8/5); numbers of L2-05, L2-07, L3-05 verified earlier.
- Phone view of the order widget not opened (tested by the inquiry checks).
