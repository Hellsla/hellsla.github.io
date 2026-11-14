VERDICT: PASS
CONTENT-HASH: 57f90cde845360e2

## Blocking

## Polish
- lesson.md:68 — "hiekka … kuumenee samalla energialla moninkertaisesti enemmän" leaves the mass implicit (per volume the ratio is about 3, not 5) — add "kilogrammaa kohti" or "yhtä suuri massa".
- lesson.md:177 — "Eristetyssä astiassa energia säilyy, kun astian omaa lämpökapasiteettia ei oteta huomioon" ties conservation to the approximation. Energy is conserved either way; only the two-body equation needs the vessel left out — e.g. "Kun astian omaa lämpökapasiteettia ei oteta huomioon, kuuman kappaleen luovuttama …".
- inquiry.json:66 (ennuste-1, the sand distractor) — the option says sand "varastoi … lämpöä", but its feedback does not correct the idea of stored heat (guardrail: a body has internal energy, not heat). Add half a sentence: "kappale ei varastoi lämpöä vaan sisäenergiaa".
- inquiry.json:275 (siirto) — `answer` is 29.1, but the solution gives 29 kg (two significant figures, justified by 8,0 K). Both fall within the tolerance; make them match.
- lessons/FY3/fy3-6/ has no lesson-answers.py, although inquiry.json and the worked example contain computed numbers (all correct, see Checked). Consider adding one.

## Checked
- Worked example: c_m = 374,6 J/(kg·K) → 3,7·10² (two significant figures justified by ΔT = 4,5 K). Reading 24,6 °C → 383. A lossless 0,200 kg copper body gives 24,6 °C, which matches the sim's default state. C_v = 1257 J/K, C_m ≈ 75 J/K. The solution is symbolic first.
- ennuste-1: sand 26,8 °C and 8,5 kJ, water 44,0 °C and 30,2 kJ, C = 838 and 160 J/K. ennuste-2: 40,0, 55,0 and 63,1 °C. Exactly one option is correct in each, and every distractor's feedback is correct.
- virhe: the wrong result is 6,6 °C and the right one 30,0 °C. The kelvin-shift argument holds (the result is again 6,6 °C). siirto: 29,09 kg; the mistakes 220 and 21,3 kg are both reproduced.
- tarkistus-2: 890,6 → 891 J/(kg·K); the mistakes 768 and 501 are reproduced; C_m = 134 J/K and the ratio 6,3 are right. tarkistus-1: 4500 vs 838 J/K, 50-fold mass. check-c2: 35 °C, and the 65 °C counter-case is right.
- Exit ticket: 419 kJ, and the ratio of about 9 (4190/450 = 9,3) is right. The misconception box (35 °C, "lähes kymmenkertainen") is right.
- Figures: the water–sand ΔT bars are 20 vs 105 px (ratio 5,25 vs 5,24), so to scale as the caption says. The c-bars are within 1 px of the values at 93,5 px per 1000. The calorimeter figure's numbers match the worked example. The formula section's name is right.
- Sim: T_eq = ΣCT/ΣC and Q = C_B(T_B0 − T_eq) are the lesson's model. The equal-τ exponential approach to T_eq conserves energy at every instant, and the model box says it is only an illustration. The no-phase-change and no-loss limits are stated. simState gives Teq and CB.
- koe-1 and koe-2: the initial values exist among the controls ("800" and "4190" are select values, and the slider ranges cover them). Only the varied parameter is unlocked, so each setup isolates it.
- Conditions: Q = cmΔT is stated "kun olomuoto ei muutu". ΔT in K equals ΔT in °C. The signs of Q are stated. Scope is inside FY3's central contents.
- The explain model answers (johtopäätös, järvi) agree with the theory and present the sim's numbers as model values.
