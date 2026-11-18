VERDICT: FAIL
CONTENT-HASH: d6a1f284318a9815

## Blocking
- [Major] inquiry.json, Pohdinta "Kertaa: siirtymän fotoni" (both feedback texts) — the prompt gives $633\,\text{nm}$, but the correct-answer and the "ylemmän tason energia" feedback say "Aallonpituutta $650\,\text{nm}$ vastaa energia ... $1{,}91\,\text{eV}$". The student sees two different wavelengths for one photon; for an S2 reader this reads as an error or as a second photon. (633 nm gives $1{,}96\,\text{eV}$, as exercise 7-1 shows.) — Fix: write $633\,\text{nm}$ and $\approx 1{,}96\,\text{eV}$ in both feedbacks (the lesson-answers.py key kert-633-eV already holds 1,96 eV). Same wording sits in the fi version; for science: confirm.

## Polish
- [Minor] feedback of "Fotoni lähtee aina samaan suuntaan": "Se on tasojen erotus." in the second feedback is a short, bare sentence after the formula; "Se on tasojen erotus" could name the subject ("Tämä energia on tasojen erotus").
- [Minor] Previous polish items (Esimerkki 3 "lämpö" vs "sisäenergia"; key concept "kvanttipiste") unchanged, may wait.

## Checked
- Delta round 2: changed Kertaa task (prompt, choices, feedbacks) read from the diff and the current inquiry.json; stage-herata-390 opened (task sits closed as "Valinnainen", layout fine, 1 mW in LaTeX).
- open-exercises-1280-1 opened for the 633 nm cross-check (1,96 eV).
- The opened Kertaa feedback has no capture of its own; judged from the text.
- lesson.md only paragraph presentation changed; lesson-answers.py is not visible text.

## Scores
illustrations 4 · typography 4 · Finnish 3 · accessibility 4
