VERDICT: PASS
CONTENT-HASH: b799bf141b539b27

## Blocking

## Polish
- inquiry.json siirto `answer` 29.1 — The Vastaus gives 29 kg, two figures, justified by ΔT = 8,0 K, which is correct. The stored answer keeps three figures. It is not shown, and a typed 29 passes (0,3 % off, tolerance 2 %). — Fix: set `answer` to 29 so the data carries the answer's figures.
- inquiry.json tarkistus-2 Vastaus — "kuten mittaustuloksissa" is right, since all data and both differences (11,0 K, 69,0 K) have three figures. Naming ΔT 11,0 K would match the worked example, L1-04 and siirto. Optional.

## Checked
- One script recomputed the 12 exercises plus siirto and tarkistus-2. All match answers.py and the stored answers, with a largest deviation of 0,8 %.
- Siirto: symbols come first, then 80,0·8,0/22,0 = 29,09 → 29 kg. A reading 0,1 K higher gives 29,6 kg, so two figures is right. The 640 kg·K balance check is real. Mistakes 220 and 21,3 kg are right.
- Every solution's rounding follows its limiting datum or difference (L1-04 7,0 K; L1-05 18 K; L3-01 20 kg / 30 K; L3-02 18 MJ / 1,2 m). The reasonableness checks are real estimates or balances.
- The principles fit. No task has a phase change (L1-05 stays below 0 °C). c cancels in the water–water tasks. Substituting Celsius readings into the weighted mean is justified correctly.
- Worked example: 5656,5 J → 374,6 → 3,7·10². The sensitivity case 24,6 °C → 383 holds. Lossless copper gives 24,6 °C, the same as the sim reset. 1257 vs 75 J/K holds.
- Lesson: the derivation of T, the 35 °C misconception case, sand c ≈ 1/5 of water ("≈ 5 ΔT" in figure 2) and iron ≈ 1/9 of water are all right.
- Inquiry:
  - ennuste-1: 26,8 / 44,0 °C; 8,5 / 30,2 kJ; 838 / 160 J/K.
  - ennuste-2: 40,0 / 55,0 / 63,1 °C.
  - virhe: 6,6 vs 30,0 °C; the Kelvin shift also passes through the wrong formula.
  - tarkistus-1: 4500 vs 838 J/K.
  - tarkistus-2: 890,6; mistakes 768 and 501; 134 J/K.
- Exit ticket: 419 kJ, ≈ 9×, 65 °C.
- Sim: Teq, Q and QW match the lesson. The equal-τ exponential approach conserves energy, and its limits are stated. koe-1 and koe-2 lock every parameter except cB or mB, and simState carries Teq and CB.
- Scope stays inside FY3 "aineen lämpeneminen ja jäähtyminen".
