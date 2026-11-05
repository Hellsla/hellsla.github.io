VERDICT: PASS
CONTENT-HASH: 3eae36b389eddded

Round 2 (round 1: FAIL, 1 Blocking). New YO-skill task L2-08; the rest of the set was PASS before and is unchanged.

## Blocking

## Polish
- exercises.json L2-08, correct reason "…sähköverkkoon lähtee paljon enemmän energiaa…" and the correct choice's feedback "pienempikin osuus on energiana suurempi". "Much more energy" decides only because the energy ratio (1000 : 300 = 3,3) is larger than the share ratio (9,0 : 4,0 = 2,3). This is C at FY2 level, since the solution shows 40 MWh against 27 MWh. Optional fix: "…niin paljon enemmän, että osuus kertaa energia on suurempi".

## Checked
- Round-1 Blocking (exercises.json:261, the "Yhtä paljon molemmissa" feedback): resolved. It now gives 0,040 · 1000 MWh = 40 MWh and 0,090 · 300 MWh = 27 MWh, and the invalid inference is gone.
- Round-1 Polish (the speed feedback): resolved. It now says "Energia siirtyy sähköverkossa todella nopeasti".
- The reworded reasons, judged one by one. The percentage-alone reason is wrong, and its feedback names the misconception. The length reason is wrong, because the task gives no distances. The speed reason is wrong, because speed does not set the loss. The correct reason is true. Each feedback still fits its new text.
- Exactly one correct choice and one correct reason. The answer equals the correct choice's text.
- Recomputed L2-08 from the task text: the electricity grid loses 40 MWh and district heating 27 MWh, so the answer is Sähköverkossa. The solution is unchanged and agrees.
- Ran answers.py against exercises.json in one script: all 18 numeric answers are within tolerance.
- Scope and notation: only $E_\text{häviö} = p\,E_\text{lähtö}$. The data are marked as an example, and 4 % and 9 % match the lesson.
- The hash was unchanged at the start and at the end (3eae36b389eddded).
