VERDICT: FAIL
CONTENT-HASH: ec64640943cb91d8

## Blocking
- exercises.json:315 and solutions.md:191 (L3-05) — **B, missing condition.** All of $E_\text{v} - \Delta U$ is called heat "vedestä ympäristöön", and c) says it went to the air and table. In a real kettle much of it warms the element and kettle body, and the task never says this is neglected. — Fix: add to the task "Oletetaan, että vastuksen ja keittimen rungon oma lämpeneminen on merkityksetön" (keep 34,8 kJ). Alternatively, call $E_\text{v} - \Delta U$ "häviö" and in c) name both the kettle's own warming and the heat to the air and table. Drop "kuten hyvin eristetyllä keittimellä pitää" (solutions.md:192): a 14,5 % loss is not small.

## Polish
- exercises.json:76 (L1-07) — The correct option says the hot water's loss equals the cold water's gain "täsmälleen", but the vessel itself also warms. Add "astian oma lämpeneminen jätetään huomiotta" to the stem; the plan's level-2 error item (forgetting the calorimeter) depends on this distinction.
- solutions.md:169 (L2-07) — 50,4 J with "kolme merkitsevää numeroa kuten keskiarvossa 4,20 N". The readings have two figures and spread ±0,2 N (about ±5 %), so 50 J is the honest result.
- solutions.md:145 (L2-05) — ΔU = 0 holds for any gas back in the same state; the ideal-gas clause suggests it is needed. Suggest "koska kaasu palaa täsmälleen samaan tilaan".
- Plan's L2 error item (forgetting the calorimeter) became a sign error (L2-06): fine physically, pedagogy to judge.

## Checked
- All eight new answers were recomputed with my own formulas, and they agree with answers.py: L1-08 0,80 kW·45 s = 36 kJ; L2-05 ΣQ = 130 J, known ΣW = −40 J → W4 = −90 J, and the cycle balances; L2-06 −10 + 30 = 20 J; L2-07 21,0/5·0,600·20 = 50,4 J; L3-04 trapezoid 0,04 m·468 N = 18,72 J, slow Q = −14,0 J; L3-05 P = 1999 W, Q = 34,8 kJ (14,5 %), cumulative loss 8,1/16,3/26,1/34,8 kJ.
- L3-04 data plausible (A ≈ 5 cm²; adiabatic model ≈ 17,5 J, isothermal ≈ 14,7 J), so W_fast > W_slow and c) are right.
- Signs follow the lesson's ΔU = Q + W convention throughout. L2-06's diagnosis is right.
- L1-06, L1-07: one correct option each; feedback follows the guardrails.
- L2-07 system, constant speed and Q = 0 stated. Scope is Fs and graphical integration only. Levels fit 8/7/5, no duplicates.
- L3-05 1280 px screenshot renders cleanly; hash same at start and end.
