VERDICT: FAIL
CONTENT-HASH: bb6a74d1fc3c3922

## Blocking
- exercises.json:95-96 (fy2-1-L1-07, third option) — A, assessment: "Liike-energia kuluu loppuun, mutta kokonaisenergia pysyy silti samana" can be defended as correct. The car's kinetic energy really does fall to zero while the total stays the same, and the option's own feedback (line 96) and the lesson define "kuluminen" as conversion into a hard-to-use form, which makes the option true. So two options are defensible. Fix: make the distractor clearly wrong, e.g. "Liike-energia muuttuu jarruissa lämpöenergiaksi, mutta kokonaisenergia pienenee, koska lämpö siirtyy ympäristöön." (Feedback: the surroundings are part of the system.) Then change solutions.md:55 "katoaa tai kuluu loppuun" to "katoaa tai pienenee".

## Polish
- solutions.md:105 (L2-05 Periaate) — the reason given for summing ("koska kulutettu energia muuttuu ... lämpöenergiaksi eikä sitä lasketa kahteen kertaan") does not follow. The sum is valid because the uses do not overlap. Write: "koska käyttökohteet eivät mene päällekkäin".
- exercises.json:218-228 (L2-07) — 720 kJ per hour means a 200 W lamp, which is not realistic for an LED, and a halogen lamp's light share of 12,5 % is high (realistically about 7 %). Suggest 216 kJ (60 W) with light 11 / 16 / 54 kJ, or say the lamps are examples.
- exercises.json:309 (L3-05) — "loppu energia muuttuu vaiheessa lämpöenergiaksi" is stated as the model. For the panel, part of the light is reflected, so add "(paneelissa osa myös heijastuu)" or "muuttuu lämpöenergiaksi tai heijastuu" (C as written, since the assumption is stated).

## Checked
- I recomputed every new answer in one script: L2-05 60,0 %; L2-06 20 J (100 J of Ep restored + 20 J to the lamp from 100 J); L2-07 684 − 540 = 144 kJ; L3-04 470/1200 = 39,2 % and 1,2·10⁹ GJ / 5,5·10⁶ = 218 GJ; L3-05 4,20 + 0,16 + 0,08 + 0,42 = 4,86 MJ, panel share 86 %, light 2,8 %. All of them match answers.py, exercises.json and solutions.md.
- L1-06 (one correct option), L1-08 (energy chain) and L2-06 (the pump needs at least 100 J) are right.
- Scope: no mgh, no c·m·ΔT, no work or force, and no product of chain efficiencies (L3-05 uses differences only). All tasks are energy balance and prefix conversions.
- The solutions solve symbolically first and their checks are real. No new task duplicates an existing one, and the levels fit. The hash did not change.
