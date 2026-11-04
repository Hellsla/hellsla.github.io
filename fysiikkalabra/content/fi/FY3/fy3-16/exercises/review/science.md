VERDICT: FAIL
CONTENT-HASH: 65a4524d88dce239

## Blocking
- exercises.json:305 / solutions.md:193ff / answers.py (fy3-16-L3-05) — A: the mass of a 0,030 m *ice* layer is computed with the density of *water* (1000 kg/m³). 54 m³ of ice has mass about 49 500 kg (ρ_jää ≈ 917 kg/m³); the answer 592 kW would become 543 kW. — Fix (simplest): make the given volume water, e.g. "ruiskutetaan betonilaatalle 0,030 m:n paksuinen kerros 12-asteista vettä" (keep a) "Laske jäädytettävän veden massa", answer unchanged); or give ρ_jää = 917 kg/m³ and recompute (answer 540 kW).
- solutions.md:205 (L3-05 d) — A, guardrail "a heat pump has a lämpökerroin, not an efficiency": "koneen oma hyötysuhde on alle 100 %" is not a reason for the required cooling power to be larger; the heat to remove does not depend on the machine, and its electrical power is P divided by the kylmäkerroin (can be smaller than P). — Fix: delete that clause; keep the extra heat loads (air, lights, spectators, slab, ground) as the reason the model gives a lower bound. Optionally add "koneen sähköteho riippuu sen kylmäkertoimesta".

## Polish
- solutions.md:167 (L2-06 Vastaus) — "kolme merkitsevää numeroa … noin 140 W/K" contradicts itself; state 1,4·10² W/K, two significant figures, limited by the fit.
- solutions.md:185 (L3-04) — "Teho UA = … W/K": UA is not a power; write "Lämpöhäviökerroin UA".
- exercises.json:257 (L3-04) — one U-value 0,50 for walls, roof and windows; add "keskimääräinen" so the simplification is visible.
- Plan (docs/exercise-bank/FY3.md): the level-1 löyly multiple choice and the level-2 thermos comparison experiment are not in the set (L1-08 kettle, L2-05 sauna data stand in). Update the plan or note the swap.
- L2-05 b: "P = UAΔT" for stones is an analogy; "häviöteho kasvaa lämpötilaeron mukana" is enough.

## Checked
- One script recomputed all new answers: L1-08 251,4 s; L2-05 75,6 %; L2-06 least-squares slope −99,8 kWh/K → 138,6 W/K, intercept 20,1 °C; L2-07 2,913 h (student 912 s reproduced); L3-04 5443 kWh, 816,5 € vs 335,9 €, difference 480,6 €, break-even 0,44 €/kg; L3-05 21,32 GJ, 592 kW, freezing 85 %. All match answers.py.
- L1-06/L1-07: one correct option each, distractors wrong with correct feedback; guardrail wording for melting and net transfer used.
- L2-05: efficiency defined in the task; per-interval efficiencies 82/75/70 % right.
- L2-07: the error (ΔT = 299 K) and ratio 299/26 = 11,5 check right.
- Scope: Q = cmΔT, sm, rm, P = UAΔT, efficiency and fuel heating value; all in FY3 and its prerequisites.
- No duplicates with existing L1-01…L3-03.
- Hash identical at start and end.
