VERDICT: FAIL
CONTENT-HASH: eaff5be82b3b554c

## Blocking
- content/fi/FY2/fy2-4/inquiry.json:262 — (A, assessment correctness) The johtopäätös now comes after koe-2 (the lamp, 40 W). Its prompt and model answer are about the lamp. But its third self-assessment criterion still asks the student to say "bensiinimoottorin häviöt ovat suuri osa otetusta tehosta ja että ne ovat lämpöä". The prompt does not ask about the engine. The engine experiment (koe-1) is now `optional`, so a student on the core path has no engine data. The model answer itself does not meet the criterion either: it speaks of the lamp's 95 % losses. — Fix: point the criterion at the lamp, e.g. "Sanoin, että hehkulampun häviöt (noin $95\,\%$) ovat suurin osa otetusta energiasta ja että ne ovat pääosin lämpöä."

## Polish
- None.

## Checked
- Delta review, round 3: ennuste-1 and koe-1 are now `optional`, the koe-1 hint is in kJ, and the johtopäätös is rewritten for koe-2.
- ennuste-1 (optional) still reveals after koe-1 (also optional), so the gating stays consistent. ennuste-2 and koe-2 stay on the core path, so the lesson keeps a core prediction and the experiment that tests it.
- koe-1 hint 3: 60 kW · 10 s = 600 kJ, and 75 % of that is 450 kJ of losses. 450 : 600 = 0,75 is right, and the unit change from J to kJ is consistent.
- Johtopäätös model answer, recomputed with my own formulas: with the lamp model's η = 0,05 at P_o = 40 W, t = 10 s gives E_o = 400 J and E_a = 20 J, and t = 20 s gives 800 J and 40 J. Both ratios are 5 %, equal to 2 W : 40 W, and the losses are 95 %. These agree with sim.js (`lamppu` eta 0.05) and with lesson-answers.py (inq-koe2-*).
- The model answer's physics is right: E = P·t at constant power, so time cancels and η = E_a/E_o = P_a/P_o. It names the model assumption (constant η) and calls the numbers the model's values.
- The new prompt (why the running time does not matter) fits koe-2's setup: P_o and laite are locked and only t varies.
- The content hash was the same at the start and the end.
