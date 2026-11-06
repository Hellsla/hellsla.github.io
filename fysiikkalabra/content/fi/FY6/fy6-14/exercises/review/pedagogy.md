VERDICT: PASS
CONTENT-HASH: dd712fc8e155ee45
Round: 1

## Blocking
(none)

## Polish
- exercises.json:277,281,285 — the feedback of three wrong first-stage answers already states the second-stage reasons ("diodi johtaa, kun anodi on plusnavan puolella"; "haarat ovat rinnan ... haaran 1 virta kulkee muista haaroista riippumatta"; "sarjassa oleva piidiodi ... katkaisee haaran 3 virran"). The two stages are separate components, so a student who errs at stage 1 reads the answer to stage 2. Keep only the diagnosis of the error in stage 1 ("Tässä anodi ja katodi on sekoitettu"), leave the principle to the reason stage.
- exercises.json:259 — a three-branch circuit with anode/cathode directions told only in words is hard to hold in the head on a phone; add a circuit figure (IEC symbols) and keep the text as the figure's description.
- exercises.json:259 — the lesson's own warned mistakes (R = U : I, diode as a resistor, I_k · U_oc) are not touched; fine for a direction task, but the packet should say which part of the lesson this task practises.
- solutions.md:172 — "Lampun lanka johtaisi kumpaankin suuntaan" rests on fy6-3 (lamp as a resistor) and is not in this lesson; one clause "kuten vastus" would tie it back.

## Checked
- Text only (no render); no formula chain longer than "4,5 V - 2,0 V = 2,5 V" (not measured separately, short).
- Physics recomputed: branch 1 forward, 2.5 V over the series resistor; branch 2 LED B reverse; branch 3 silicon diode reverse so the lamp is dark; answer "Vain LED A" is correct.
- Options cover the sensible error classes (lamp lit despite the diode, A and B confused, one reverse diode kills everything); correct option "Vain LED A" is not distinguishable by length or hedge.
- Reasons: four of 87-104 characters; the correct one is not the longest, none hedged; reason 4 is true but irrelevant, as the type requires.
- Correct choice's feedback at stage 1 ("Oikein: vain LED A palaa.") gives nothing away; stage 2 correct feedback does the explaining.
- Within fy6-14 and fy6-3 (diode direction, parallel branches); question "Mitkä valot palavat?" is the last sentence; Finnish correct (anodi, katodi, estosuunta, etuvastus).
- Not a duplicate of L1-06 (one diode in series with a resistor); level 2, kind concept + reasoning.
- Hash unchanged at the start and end.
