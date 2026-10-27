VERDICT: FAIL
CONTENT-HASH: 4c0ea14d24c36a07

## Blocking
- inquiry.json siirto `solution` (Vastaus; prompt and `answer` 29.1) — "kolme merkitsevää numeroa kuten massassa 80,0 kg ja lämpötiloissa" ignores the limiting datum. The quantities used are the differences 38,0 − 30,0 = 8,0 K (two figures) and 22,0 K. The worked example (lesson.md, Tulos) and L1-04 justify the figures by ΔT, and by that rule the answer has two figures: a reading 0,1 K higher gives 29,6 kg, so the third figure means nothing. My round-1 fix wrongly allowed "29,1 kg with three figures". I correct that here. — Fix: either give "29 kg, kaksi merkitsevää numeroa, koska lämpötilan muutos 8,0 K tunnetaan kahden numeron tarkkuudella" and set `answer` 29, or change the data so that both ΔT have three figures (e.g. T_a = 25,0 °C: 13,0 K and 22,0 K → 47,3 kg; update hints and mistakes to match).

## Polish
- solutions.md L1-02 Vastaus — "kaksi merkitsevää numeroa kuten massassa 2,4 kg" is right. 195 K has three figures, so naming 2,4 kg as the limiting value would make the reason explicit. Optional.
- solutions.md L1-04 Sijoitus — "≈ −35,2 MJ" followed by the answer −35 MJ is fine. The intermediate value could keep more digits (−35,196 MJ) to match the other solutions.

## Checked
- All 12 exercises recomputed in one script: they match answers.py and exercises.json within tolerance. L1-04 now uses 38,0 / 31,0 °C, ΔT = 7,0 K, giving −35,2 → −35 MJ. Its rounding is now justified by ΔT, which is correct.
- Every other solution's rounding follows from its least precise datum or ΔT (L1-05 18 K; L3-01 30 K; tarkistus-2 11,0 / 69,0 K → 891).
- Siirto physics is correct: 80,0·8,0/22,0 = 29,09 kg. Mistakes 220 and 21,3 are correct. The symbols are solved first, and the 640 kg·K check is a real check.
- Worked example: 5656,5 J and 374,6 → 3,7·10². The sensitivity case (24,6 °C → 383) is right, the lossless copper case gives 24,6 °C, and 1257 vs 75 J/K is right.
- inquiry: ennuste-1 (26,8 / 44,0 °C, 8,5 / 30,2 kJ, 838 / 160 J/K), ennuste-2 (40,0 / 55,0 / 63,1 °C), virhe (6,6 vs 30,0 °C), tarkistus-1 (4500 vs 838 J/K), tarkistus-2 (890,6, mistakes 768 / 501, 838 vs 134 J/K).
- Lesson: the T derivation and the 35 °C misconception example are right. The exit ticket is right (419 kJ, ≈9×, 65 °C).
- Sim: Teq and Q match the lesson's formula, and the equal-τ relaxation conserves energy. koe-1 and koe-2 lock everything except cB or mB, and simState carries Teq and CB.
- Scope stays inside FY3 "aineen lämpeneminen ja jäähtyminen". There are no phase changes, and L1-05 stays below 0 °C.
