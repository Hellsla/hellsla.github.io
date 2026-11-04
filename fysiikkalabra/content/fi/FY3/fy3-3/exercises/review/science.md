VERDICT: FAIL
CONTENT-HASH: ba1c9a6597054a40

Exercise-bank round: 8 new tasks reviewed in full; old tasks unchanged.

## Blocking
- solutions.md:180 (fy3-3-L3-04 Järkevyys) — A (guardrail "Measurement and data"): "Toistaminen pienentää satunnaista hajontaa" is false: repeating does not shrink the spread (hajonta) of the readings, only the random error of their mean. It is the take-away sentence of the task's c)/d) reasoning. — Fix: "Toistaminen pienentää keskiarvon satunnaista virhettä mutta ei poista systemaattista virhettä, joten …".

## Polish
- solutions.md:188–189 (L3-05) — the intermediate is shown as 418,6 − 273,15 = 145,5 °C and then answered 145 °C; a student rounds 145,5 to 146. Show $T_3 = 418{,}61\,\text{K}$, $\theta_3 = 145{,}46\,{}^\circ\text{C}$ so the rounding to 145 is visible (answer and tolerance fine).
- exercises.json:360 (L3-05) — "ylipaine" is used without being defined in the task or the brief's lesson (pressure is "treated later"); add "(ylipaine = kokonaispaine − ilmanpaine)".
- L3-05 vs plan (docs/exercise-bank/FY3.md) — the plan's L3 reasoning task "miksi lämpötila ei ole lämmön määrä (sama T, eri energia)" is not in the set; L3-05 is a gauge/total-pressure modelling task instead. Fine physics, but either update the plan or swap.
- L2-06 data — 80,0 → 48,6 °C in 4 h (≈10 K/h at first) is a very poor thermos; values like 90 → 75 °C over 4 h would be more realistic.

## Checked
- One script recomputed every new answer: L1-07 255 K; L2-05 sum 7,5 → 1,5 K, bath 37,1 °C; L2-06 drops 10,1/8,6/6,9/5,8 K, ratio 1,741 → 1,7, relative drops ≈0,17 each; L2-07 gaps 12,0/3,6/0,9/0,3 K → 40 s; L3-04 sums 185,0/182,0/185,0, Δ 0,6 K, half ranges 0,2/0,35/0,1 K, 37,0 °C < 37,5 °C; L3-05 796,7 kPa / 695,7 kPa, T3 = 418,61 K → 145,46 °C, KE +13,6 %, gauge +16 %, wrong model 166,6 °C. All match answers.py and solutions.
- Tolerances admit the stated rounding (L2-06 1,74; L3-04 0,54–0,66; L3-05 ±2,9 °C).
- L1-06 and L1-08: exactly one correct option; every distractor wrong and its feedback right (closed = no mass transfer; rigid = constant V; p and mean KE rise).
- L2-05 systematic vs random argument and correction sign right; L2-07 "mittari näyttää omaa lämpötilaansa" right.
- L3-05 p ∝ T applied to total, not gauge, pressure, with the condition stated in the task.
- Notation T = θ + 273,15 and symbols match the brief; levels fit (data at L2, multi-step YO-style at L3); no duplicate of an old task.
- New L3 captures render without overflow.
