VERDICT: PASS
CONTENT-HASH: 83dc08db7ea57a37
Round: 2

## Blocking
(none)

## Polish
- docs/exercise-bank/FY3.md:97ff — the plan still names a level-1 löyly multiple choice and a level-2 thermos comparison experiment. Neither is in the set: L1-08 (kettle) and L2-05 (sauna data) stand in for them (carried over). Update the plan or note the swap.
- exercises.json:303 (L3-05) — the task gives ρ, c_vesi and c_jää, but not s, which the solution takes "taulukosta". For consistency with L2-07, add "veden ominaissulamislämpö 334 kJ/kg" to the task.
- solutions.md:195ff (L3-05 d) — "kylmäkerroin" appears only here and is not defined in the brief. Either add a few words ("vastaa lämpöpumpun lämpökerrointa") or drop the sentence.

## Checked
- Round-1 Blocking 1 resolved: L3-05 now freezes "0,030 m paksuinen kerros vettä", so m = ρ_vesi V = 54 000 kg is correct. The answer of 590 kW is unchanged, and answers.py says so in its comment.
- Round-1 Blocking 2 resolved: d) no longer cites the machine's "hyötysuhde". The extra heat loads (air, lights, spectators, slab, ground) give a lower bound, and the electrical power is tied to the kylmäkerroin. This fits the guardrail.
- Round-1 Polish resolved: L2-06 Vastaus now gives 1,4·10² W/K with two significant figures, limited by the fit. L3-04 says "Lämpöhäviökerroin UA" and the task text says "keskimääräinen U-arvo". L2-05 b) says only that the loss grows with the temperature difference.
- One script recomputed every new answer from the task text: L1-08 251,4 s; L2-05 75,56 %; L2-06 least-squares slope −99,8 kWh/K, which gives 138,6 W/K, with the intercept at 20,1 °C; L2-07 2,913 h; L3-04 480,6 € (break-even 0,44 €/kg); L3-05 21,32 GJ, 592 kW, with freezing 85 % of the energy. All agree with exercises.json and answers.py within tolerance.
- L1-06 and L1-07: each has exactly one correct option, the answer field equals it, and every distractor is wrong with correct feedback. The guardrail wording on melting and net transfer is used.
- L3-05: the three phases are computed separately, with no cΔT during freezing. Energy is released on freezing, as the guardrail requires.
- Scope: Q = cmΔT, sm, P = UAΔT, efficiency and heating value. No duplicates, and the levels fit.
- The hash was identical at the start and the end.
